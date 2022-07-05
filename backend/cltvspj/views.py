from django.shortcuts import render
from django.http import JsonResponse
from backend.cltvspj.models import Calculator, Email
from abc import ABC, abstractmethod

# Create your views here.
def index(request):
    
    class CalculateDiscount(ABC):
        minimal_mensal_salary = 1212
        minimal_annual_revenue_to_declare_irrf = 28559.70
        mensal_salary: int = 0

        @abstractmethod
        def calculate_salary(self) -> float: pass

        @abstractmethod
        def discount_inss(self) -> float: pass

        @abstractmethod
        def discount_irrf(self) -> float: pass

        @staticmethod
        def check_percent_of_irrf(value: float) -> float:
            range_of_irff = {1: 0, 2: 7.50, 3: 15, 4: 22.50, 5: 27.50}

            if value <= 1903.98:
                range_ = 1
            elif 1903.99 >= value < 2826.65:
                range_ = 2
            elif 2826.66 >= value < 3751.05:
                range_ = 3
            elif 3751.06 >= value < 4664.68:
                range_ = 4
            else:
                range_ = 5
            
            return range_of_irff[range_]


        @staticmethod
        def calculate_percent(value: float, percent: float) -> float:
            return value * (percent / 100)
            
    class IndividualMicroEntrepreneur(CalculateDiscount):
        
        def __init__(self) -> None:
            super().__init__()
            self.mensal_salary = 0
            self.total_salary = self.mensal_salary*12
        
        values_of_discount = {
            "comercy_or_industry": {"total": 61.60, "percent_isent_of_irrf": 8},
            "services_provision": {"total": 65.60, "percent_isent_of_irrf": 32},
            "comercy_and_services": {"total": 66.60, "percent_isent_of_irrf": 16}
        }

        maximum_annual_revenue = 81000

        annual_revenue : float = 0
        type_of_work: str = "comercy_or_industry"
        # PREENCHI POIS NO FORM NAO HAVIA COMO PREENCHER ENTAO DEIXEI COMERCCIO COMO PADRAO SÓ PRA FORÇAR O FUNCIONAMENTO!
        expenditure: float = 0
        mensal_salary: int = 0

        def calculate_salary(self) -> tuple:
            salary = self.annual_revenue/12
            inss = self.discount_inss()
            irrf = self.discount_irrf()
            return salary - (inss + irrf)

        def discount_inss(self) -> float:
            return self.calculate_percent(self.minimal_mensal_salary, 5)

        def discount_irrf(self) -> float:
            isent_revenue = self.calculate_percent(self.annual_revenue, self.values_of_discount[self.type_of_work]["percent_isent_of_irrf"])
            revenue = self.annual_revenue - isent_revenue - self.expenditure
            
            if revenue > self.minimal_annual_revenue_to_declare_irrf:
                percent = self.check_percent_of_irrf(revenue/12)
                return self.calculate_percent(revenue, percent)
            
            return 0

    class SalariedWorker(CalculateDiscount):
        # salario mensal no modelo CLT

        def __init__(self) -> None:
            super().__init__()
            self.mensal_salary = 0
            self.total_salary = float(self.mensal_salary)*12
            
        def discount_inss(self) -> float:
            return self.check_percent_of_irrf(self.mensal_salary)
        
        def discount_irrf(self) -> float:
            return super().discount_irrf()
        
        def calculate_salary(self) -> float:
            return self.total_salary*( 1 -  self.calculate_percent(self.mensal_salary, self.discount_inss()))

    class JuridicPersonFactory():
        factories = {
            "mei": IndividualMicroEntrepreneur(),
        }

        def get_salary_and_discounts(self, type):
            return self.factories[type]
        
    if(request.method == 'GET'):
        return render(request, 'cltvspj/form.html')

    elif(request.method == 'POST'):
        
        print(request.POST.get('clt'))
        print(request.POST.get('pj'))

        salaried_worker = SalariedWorker()
        salaried_worker.mensal_salary = float(request.POST.get('clt', False))
        mei_worker = IndividualMicroEntrepreneur()
        mei_worker.mensal_salary = float(request.POST.get('pj', False))
        # realiza operacoes de calculo aqui
        return JsonResponse({'clt': salaried_worker.calculate_salary(), 'pj': mei_worker.calculate_salary()}, safe=False)
