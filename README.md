# CPF Field para usar nos seus Models e ModelForms

Essa é uma implementação simples e enxuta de validadores para CPF de usuários.

Caso alguma coisa deixe de funcionar nas próximas versões do Django, não me comprometo em manter a biblioteca.

## Instalação

```console
pip install django-cpf
```

Adicione a aplicação `cpf_field` entre a suas apps e as apps do django.

```python
INSTALLED_APPS = [
    # Django apps
    'cpf_field',
    # My Apps
]
```

## Como utilizar:

No seu arquivo de `models.py`, importe o `CPFField` e insira no seu atributo de classe.

```python
from django.db import models
from cpf_field.models import CPFField

class MyModel(models.Model):
    # ....
    cpf = CPFField('cpf')

```

O CPFField é derivado de `models.CharField` e vem inicializado, por padrão, com o `max_length=14`.

## CPFs inválidos

CPFs que são considerados inválidos para o ``CPFField`` são aqueles que:

1. Não possuem 11 números.
2. O cálculo dos digitos verificadores não bate com os digitos informados.

#### Exemplos de CPFs inválidos

```python
from .forms import ClientForm

form = ClientForm()
form.cpf = '12312312312' # inválido
form.cpf = '123.123.123-12' # inválido
form.cpf = 'ABC12312312' # inválido
form.cpf = 'ABC.123.123-12' # inválido
```

## CPF válidos

Os CPFs válidos são aqueles que:

1. Possuem 11 números.
2. O cálculo dos digitos verificadores bate com os digitos informados.

## Observações

O `CPFField` valida o CPF com ou sem máscara.

Então, os CPFs nos formatos `XXXXXXXXXXX` e `XXX.XXX.XXX-XX` são válidos.

Se você precisa que seu CPF seja salvo num formato específico (sem máscara, por exemplo) você tem que implementar o
método `clean_cpf` no seu `ModelForm`, para formatar o valor enviado pelo usuário.
