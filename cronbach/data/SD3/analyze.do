* stata analysis code for comparison
*
* to run at the command line:
*
* stata -b do analyze
*
* this will save results in analyze.log
* a copy of this such results is saved in analyze.log.txt

import delimited data.tsv, varnames(1) clear delimiter(tab)

label define source ///
    1 "front page of website" ///
    2 "Google search" ///
    3 "other (based on HTTP referrer)" ///

label values source source

foreach i of varlist m1-p9 {
    replace `i' = . if `i' == 0
}

sum *

local reversed n2 n6 n8 p2 p7
foreach i of varlist `reversed' {
    replace `i' = 6 - `i'
}

alpha m1-m9, gen(m)
alpha n1-n9, gen(n)
alpha p1-p9, gen(p)
