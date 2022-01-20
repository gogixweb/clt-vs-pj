from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):

    melhor = {}
    melhor['salario'] = ''

    if(request.method == 'GET'):
       return render(request, 'cltvspj/form.html', {'melhor': melhor})

    elif(request.method == 'POST'):
        salario_pj =  request.POST['PJ']
        salario_clt = request.POST['CLT']
        # iss = request.POST['ISS']
        # irrf = request.POST['IRRF']

        receita_bruta_anual = request.POST['receita_bruta_anual']   # Receita bruta anual
        aliquota = 0     # Aliquota indicada no anexo enviado
        parcela_deduzida = 0       # Parcela a ser deduzida de acordo com o anexo enviado
        inss = 0     # Contribuicao para INSS (salario CLT)
        irrf = 0     # Imposto de Renda (CLT)

        print(request.POST)   

        # SIMULACAO DOS VALORES CONSIDERANDO O ANEXO v!!!
        if(float(salario_pj) <= 180000):
            aliquota = 0.155
            parcela_deduzida = 4500
        elif(float(salario_pj) <= 360000):
            aliquota = 0.18
            parcela_deduzida = 9900
        elif(float(salario_pj) <= 1800000):
            aliquota = 0.205
            parcela_deduzida = 17100
        elif(float(salario_pj) <= 3600000):
            aliquota = 0.23
            parcela_deduzida = 62000
        elif(float(salario_pj) <= 4800000):
            aliquota = 0.305
            parcela_deduzida = 540000

        # DESCONTOS DE ISS E IRRF PARA SALARIO CLT!!!
        if(float(salario_clt) < 1045):
            inss = 0.075
        elif(float(salario_clt) < 2098):
            inss = 0.09
        elif(float(salario_clt) < 3134):
            inss = 0.12
        elif(float(salario_clt) < 6101):
            inss = 0.14

        if(float(salario_clt) < 1903):
            irrf = 0
        elif(float(salario_clt) < 2826):
            irrf = 0.75
        elif(float(salario_clt) < 3751):
            irrf = 0.15
        elif(float(salario_clt) < 4664):
            irrf = 0.225
        else:
            irrf = 0.275

        formula_DAS = ((float(receita_bruta_anual)*float(aliquota)) - float(parcela_deduzida))/float(receita_bruta_anual)
        salario_pj = float(salario_pj)*(1-float(formula_DAS))
        salario_clt = float(salario_clt) - (float(inss + irrf))

        if(salario_pj >= salario_clt):
            melhor['salario'] = 'salario PJ eh melhor!!!'
        else:
            melhor['salario'] = 'salario CLT eh melhor!!!'
    
#     return render(request, 'cltvspj/melhorsalario.html', {'melhor': melhor})
    return JsonResponse({'melhor salario': melhor['salario']})

def contact(request):
    return render(request, 'cltvspj/contact.html' )
