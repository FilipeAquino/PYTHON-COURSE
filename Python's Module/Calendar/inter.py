# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
# use Get-WinsystemLocale para saber o seu

import calendar
import locale
# o locale serve pra trazer as coisas pra minha região
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')  # todas as config. vem para o BR
# deixar as aspas vazias sigf. o atual
print(locale.getlocale())  # meu locate
print(calendar.calendar(2022))
