Run the command using sox and this program https://github.com/cbs228/sameold:
```
/home/kali/CTF/UIUCTF23/misc/tornado [git::uiuctf23 *] [kali@kali] [18:54]
> sox warning.wav -t raw -r 22.5k -e signed -b 16 -c 1 - | ./samedec-x86_64-unknown-linux-gnu -r 22050 -v
 INFO  samedec > SAME decoder reading standard input
 INFO  sameold::receiver > [1400          ]: event [link]: searching
 INFO  sameold::receiver::framing > burst: started: after 20 bytes
 INFO  sameold::receiver          > [7992          ]: event [link]: reading
 INFO  sameold::receiver          > [22467         ]: event [link]: decoded burst: "ZCZC-UXU-TFR-R18007ST_45-0910BR5-KIND3RWS-"
 INFO  sameold::receiver          > [22467         ]: event [transport]: assembling
 INFO  sameold::receiver          > [22488         ]: event [link]: no carrier
 INFO  sameold::receiver          > [44369         ]: event [link]: searching
 INFO  sameold::receiver::framing > burst: started: after 19 bytes
 INFO  sameold::receiver          > [50614         ]: event [link]: reading
 INFO  sameold::receiver          > [65087         ]: event [link]: decoded burst: "ZCZC-WIR-TO{3018W0R+00T5-09UT115-K_EV/NWS-"
 INFO  sameold::receiver          > [65108         ]: event [link]: no carrier
 INFO  sameold::receiver          > [86644         ]: event [link]: searching
 INFO  sameold::receiver::framing > burst: started: after 20 bytes
 INFO  sameold::receiver          > [93236         ]: event [link]: reading
 INFO  sameold::receiver          > [107708        ]: event [link]: decoded burst: "ZCZC-WXRCTOR-0D_007+004OR_O1011E@KIND/N}S-"
 INFO  sameold::receiver          > [107729        ]: event [link]: no carrier
 INFO  sameold::receiver          > [136628        ]: event [transport]: message: (100.0% voting, 120 errors) "ZCZC-WXR-TOR-018007+0045-0910115-KIND/NWS-"
ZCZC-WXR-TOR-018007+0045-0910115-KIND/NWS-
 INFO  sameold::receiver          > [136671        ]: event [transport]: assembling
 INFO  sameold::receiver          > [347741        ]: event [transport]: idle
 INFO  sameold::receiver          > [2006035       ]: event [link]: searching
 INFO  sameold::receiver::framing > burst: started: after 20 bytes
 INFO  sameold::receiver          > [2012622       ]: event [link]: reading
 INFO  sameold::receiver          > [2013916       ]: event [link]: decoded burst: "NNNNfff"
 INFO  sameold::receiver          > [2013916       ]: event [transport]: message: (0.0% voting, 0 errors) "NNNN"
NNNN
 INFO  sameold::receiver          > [2013937       ]: event [link]: no carrier
 INFO  sameold::receiver          > [2013937       ]: event [transport]: assembling
 INFO  sameold::receiver          > [2035822       ]: event [link]: searching
 INFO  sameold::receiver::framing > burst: started: after 19 bytes
 INFO  sameold::receiver          > [2042061       ]: event [link]: reading
 INFO  sameold::receiver          > [2043355       ]: event [link]: decoded burst: "NNNNfff"
 INFO  sameold::receiver          > [2043377       ]: event [link]: no carrier
 INFO  sameold::receiver          > [2064914       ]: event [link]: searching
 INFO  sameold::receiver::framing > burst: started: after 20 bytes
 INFO  sameold::receiver          > [2071503       ]: event [link]: reading
 INFO  sameold::receiver          > [2072798       ]: event [link]: decoded burst: "NNNNfff"
 INFO  sameold::receiver          > [2072819       ]: event [link]: no carrier
 ```

 Then decode the message from the three strings (choose the unique character from each):
 ```
ZCZC-UXU-TFR-R18007ST_45-0910BR5-KIND3RWS-
ZCZC-WIR-TO{3018W0R+00T5-09UT115-K_EV/NWS-
ZCZC-WXRCTOR-0D_007+004OR_O1011E@KIND/N}S-
 ```

Becomes:
```
UIUCF{3RD_WRST_TOR_OUTBRE@_EV3R}
```
