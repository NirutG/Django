from django import template

register = template.Library()

@register.filter(name='power2')
def square(var):
    return var ** 2

@register.filter
def plus(var, number):
    return var + number

@register.filter
def thaidate(var):
    n = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม', 'มิถุนายน', \
         'กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']

    d = var.day
    m = n[var.month - 1]
    y = var.year + 543

    return f'{d} {m} {y}'