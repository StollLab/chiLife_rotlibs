# Accessible volume only spin labels

Labels in this directory have only one, or a few rotamers and do not accurately represent the conformational diversity of the enclosed label. Accordingly **These rotamer libraries should only be used with accessible volume sampling methods**. This can be achieved wither by using the ``sample`` keyword argument or the ``from_wizard`` class method.

```python
import chilife as xl
SL1 = xl.SpinLabel('XYZ', resi, protein, sample=10000)
SL2 = xl.SpinLabel.from_wizard('XYZ', resi, protein)
```


## rotamer library descriptions
ACD      : L-Acridonylalanine non-canonical amino acid (Fluor)  
CYM      : Cu(II) Cyclen Maleimide  
DAB      : Dabcyl C2 maleimide (dabcylM) organic fluor quencher  
FPB      : Fe(II) phenanthroline maleimide label capped with two bipyridyl molecules  
FPM      : Fe(II) phenanthroline maleimide label capped with two additional phenanthroline molecules  
PHM      : Cu(II) phenanthroline maleimide label with no cap  
PHM      : Fe(II) phenanthroline maleimide label with no cap  
