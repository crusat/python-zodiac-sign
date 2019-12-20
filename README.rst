
Description
===========

Getting the Zodiac sign by date.

Languages:


* English (\ ``en_US``\ , default)
* Russian (\ ``ru_RU``\ )
* Portuguese (\ ``pt_BR``\ , ``pt_PT``\ ) - Thanks to @guilhermecomum
* Greek (\ ``el``\ , ``el_CY``\ , ``el_GR``\ ) - Thanks to @hargikas

Install
=======

.. code-block::

   $ pip install zodiac-sign


Example
=======

.. code-block::

   from zodiac_sign import get_zodiac_sign
   from datetime import date

   d = date(1988, 3, 6)

   # only data param
   print(get_zodiac_sign(d))

   # two params - day and month, without year
   print(get_zodiac_sign(6, 3))


Example with locale
-------------------

.. code-block::

   from zodiac_sign import get_zodiac_sign
   import locale

   locale.setlocale(locale.LC_ALL, 'ru_RU')
   print(get_zodiac_sign(6, 3))
   # out "Рыбы"

   locale.setlocale(locale.LC_ALL, 'en_US')
   print(get_zodiac_sign(6, 3))
   # out "Pisces"


Repository
==========

`https://github.com/crusat/python-zodiac-sign <https://github.com/crusat/python-zodiac-sign>`_

License
=======

MIT
