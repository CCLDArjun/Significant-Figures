# Significant-Figures
way to do math in python with respect to significant figures 

Evaluate expressions:
```py
>>> from sig_eval import seval
>>> seval("1.10+1")
2.E0
>>> seval("1.10+1") * seval("5.113+43.331")
1.E2
>>> seval("1.10+1.0000") * seval("5.113+43.331")
1.02E2
>>> seval("1.100000+1.0000") * seval("5.113+43.331")
1.017E2
>> def force(mass, accel):
  ...     return mass * accel
...
>>> force(seval("1.00"), seval("4.60"))
4.60E0
>>> def boyles_law(pressure1, volume1, pressure2):
...     return (pressure1 * volume1) / pressure2
...
>>> boyles_law(seval("4.50"), seval("8.09"), seval("1.200"))
3.03E1
```
