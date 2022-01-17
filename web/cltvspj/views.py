from django.shortcuts import render

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

        RBT_ANO = request.POST['RBT_ANO']   # Receita bruta anual
        ALIQ = 0     # Aliquota indicada no anexo enviado
        PD = 0       # Parcela a ser deduzida de acordo com o anexo enviado
        INSS = 0     # Contribuicao para INSS (salario CLT)
        IRRF = 0     # Imposto de Renda (CLT)

        print(request.POST['PJ'])   

        # SIMULACAO DOS VALORES CONSIDERANDO O ANEXO v!!!
        if(float(salario_pj) <= 180000):
            ALIQ = 0.155
            PD = 4500
        elif(float(salario_pj) <= 360000):
            ALIQ = 0.18
            PD = 9900
        elif(float(salario_pj) <= 1800000):
            ALIQ = 0.205
            PD = 17100
        elif(float(salario_pj) <= 3600000):
            ALIQ = 0.23
            PD = 62000
        elif(float(salario_pj) <= 4800000):
            ALIQ = 0.305
            PD = 540000

        # DESCONTOS DE ISS E IRRF PARA SALARIO CLT!!!
        if(float(salario_clt) < 1045):
            INSS = 0.075
        elif(float(salario_clt) < 2098):
            INSS = 0.09
        elif(float(salario_clt) < 3134):
            INSS = 0.12
        elif(float(salario_clt) < 6101):
            INSS = 0.14

        if(float(salario_clt) < 1903):
            IRRF = 0
        elif(float(salario_clt) < 2826):
            IRRF = 0.75
        elif(float(salario_clt) < 3751):
            IRRF = 0.15
        elif(float(salario_clt) < 4664):
            IRRF = 0.225
        else:
            IRRF = 0.275

        formula_DAS = ((float(RBT_ANO)*float(ALIQ)) - float(PD))/float(RBT_ANO)
        salario_pj = float(salario_pj)*(1-float(formula_DAS))
        salario_clt = float(salario_clt) - (float(INSS + IRRF))

        if(salario_pj >= salario_clt):
            melhor['salario'] = 'salario PJ eh melhor!!!'
        else:
            melhor['salario'] = 'salario CLT eh melhor!!!'
        
        print('clt: ')
        print(salario_clt)
        print('\n')
        print('pj: ')
        print(salario_pj)
    
    return render(request, 'cltvspj/melhorsalario.html', {'melhor': melhor})

def contact(request):
    return render(request, 'cltvspj/contact.html' )
