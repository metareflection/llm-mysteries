nohup: ignoring input
/home/sraja/mambaforge/envs/llm-mysteries/lib/python3.10/site-packages/transformers/models/auto/auto_factory.py:472: FutureWarning: The `use_auth_token` argument is deprecated and will be removed in v5 of Transformers. Please use `token` instead.
  warnings.warn(
Loading checkpoint shards:   0%|          | 0/3 [00:00<?, ?it/s]Loading checkpoint shards:  33%|███▎      | 1/3 [00:01<00:03,  1.88s/it]Loading checkpoint shards:  67%|██████▋   | 2/3 [00:03<00:01,  1.98s/it]Loading checkpoint shards: 100%|██████████| 3/3 [00:05<00:00,  1.66s/it]Loading checkpoint shards: 100%|██████████| 3/3 [00:05<00:00,  1.74s/it]
/home/sraja/mambaforge/envs/llm-mysteries/lib/python3.10/site-packages/dill/_dill.py:412: PicklingWarning: Cannot locate reference to <class '_ctypes.PyCFuncPtrType'>.
  StockPickler.save(self, obj, save_persistent_id)
/home/sraja/mambaforge/envs/llm-mysteries/lib/python3.10/site-packages/dill/_dill.py:412: PicklingWarning: Cannot pickle <class '_ctypes.PyCFuncPtrType'>: _ctypes.PyCFuncPtrType has recursive self-references that trigger a RecursionError.
  StockPickler.save(self, obj, save_persistent_id)
Parameter 'function'=<function processCase at 0x7f03a2ca4b80> of the transform datasets.arrow_dataset.Dataset._map_single couldn't be hashed properly, a random hash was used instead. Make sure your transforms and parameters are serializable with pickle or dill for the dataset fingerprinting and caching to work. If you reuse this transform, the caching mechanism will consider it to be different from the previous calls and recompute everything. This warning is only showed once. Subsequent hashing failures won't be showed.
Map:   0%|          | 0/203 [00:00<?, ? examples/s]Map:   0%|          | 1/203 [00:09<33:14,  9.87s/ examples]Map:   1%|          | 2/203 [00:17<29:28,  8.80s/ examples]Map:   1%|▏         | 3/203 [00:26<29:13,  8.77s/ examples]Map:   2%|▏         | 4/203 [00:34<27:17,  8.23s/ examples]## 5minutemystery-who-let-the-frogs-out
Kyle Kravetsky is guilty: True or False?
True (0.9274947665741009)
Kyle Kravetsky has mean: True or False?
True (0.9164093141890854)
Kyle Kravetsky has motive: True or False?
True (0.9393594296838563)
Kyle Kravetsky has opportunity: True or False?
True (0.7420480767433203)
Marnie Pepper is guilty: True or False?
True (0.8418256636710214)
Marnie Pepper has mean: True or False?
True (0.8727817583545995)
Marnie Pepper has motive: True or False?
True (0.8539127077831877)
Marnie Pepper has opportunity: True or False?
True (0.5087881523495457)
Matilda Robbens is guilty: True or False?
True (0.8895288719962232)
Matilda Robbens has mean: True or False?
True (0.9086179121100144)
Matilda Robbens has motive: True or False?
True (0.9257686153543061)
Matilda Robbens has opportunity: True or False?
True (0.7940657699545044)
Sergio Ramos is guilty: True or False?
True (0.9669140569738693)
Sergio Ramos has mean: True or False?
True (0.9336731438527403)
Sergio Ramos has motive: True or False?
True (0.9489172681310486)
Sergio Ramos has opportunity: True or False?
True (0.8795611817678315)
### Kyle Kravetsky
- mean: False (0.08359068581091456)
- motive: False (0.06064057031614367)
- opportunity: False (0.2579519232566797)

### Marnie Pepper
- mean: False (0.12721824164540052)
- motive: False (0.14608729221681227)
- opportunity: False (0.49121184765045434)

### Matilda Robbens
- mean: False (0.09138208788998559)
- motive: False (0.0742313846456939)
- opportunity: False (0.2059342300454956)

### Sergio Ramos
- mean: True (0.9336731438527403)
- motive: True (0.9489172681310486)
- opportunity: True (0.8795611817678315)

The culprit is Sergio Ramos.
In fact, it is Matilda Robbens.
## 5minutemystery-uncle-buck-field-trip
Collin is guilty: True or False?
True (0.8686040692746866)
Collin has mean: True or False?
True (0.7570766705324253)
Collin has motive: True or False?
True (0.858955389767532)
Collin has opportunity: True or False?
True (0.7914989614633984)
Erica is guilty: True or False?
True (0.851212260635415)
Erica has mean: True or False?
True (0.8860265599597172)
Erica has motive: True or False?
True (0.8858291535164952)
Erica has opportunity: True or False?
True (0.5438324636094939)
Rory is guilty: True or False?
True (0.9293122320338961)
Rory has mean: True or False?
True (0.7725306828324007)
Rory has motive: True or False?
True (0.9635748850103736)
Rory has opportunity: True or False?
True (0.8688268116310761)
Rusty is guilty: True or False?
True (0.9396923188104354)
Rusty has mean: True or False?
True (0.7759445334082792)
Rusty has motive: True or False?
True (0.9294404371753803)
Rusty has opportunity: True or False?
True (0.8848377441095496)
### Collin
- mean: False (0.24292332946757467)
- motive: False (0.14104461023246795)
- opportunity: False (0.20850103853660162)

### Erica
- mean: False (0.11397344004028276)
- motive: False (0.11417084648350484)
- opportunity: False (0.4561675363905061)

### Rory
- mean: True (0.7725306828324007)
- motive: True (0.9635748850103736)
- opportunity: True (0.8688268116310761)

### Rusty
- mean: False (0.22405546659172082)
- motive: False (0.07055956282461973)
- opportunity: False (0.11516225589045037)

The culprit is Rory.
In fact, it is Rory.
## 5minutemystery-mystery-of-the-white-hats
Captain Stark is guilty: True or False?
True (0.8534248451958423)
Captain Stark has mean: True or False?
True (0.9329437018480795)
Captain Stark has motive: True or False?
True (0.9091032147468773)
Captain Stark has opportunity: True or False?
True (0.7988152492192591)
Chet is guilty: True or False?
True (0.6800292740030767)
Chet has mean: True or False?
True (0.8868131040663721)
Chet has motive: True or False?
True (0.8868130446009216)
Chet has opportunity: True or False?
True (0.8386797310322072)
Doug is guilty: True or False?
True (0.5841525779336078)
Doug has mean: True or False?
True (0.9073122118500465)
Doug has motive: True or False?
True (0.802555560073231)
Doug has opportunity: True or False?
True (0.7549149897594328)
Ernie is guilty: True or False?
True (0.580352018589158)
Ernie has mean: True or False?
True (0.8577681165234065)
Ernie has motive: True or False?
True (0.8504686406728537)
Ernie has opportunity: True or False?
True (0.72951977676791)
### Captain Stark
- mean: True (0.9329437018480795)
- motive: True (0.9091032147468773)
- opportunity: True (0.7988152492192591)

### Chet
- mean: False (0.11318689593362785)
- motive: False (0.11318695539907841)
- opportunity: False (0.16132026896779283)

### Doug
- mean: False (0.09268778814995349)
- motive: False (0.19744443992676897)
- opportunity: False (0.24508501024056717)

### Ernie
- mean: False (0.14223188347659355)
- motive: False (0.14953135932714634)
- opportunity: False (0.27048022323209)

The culprit is Captain Stark.
In fact, it is Chet.
## 5minutemystery-the-missing-popcorn
Private First Class Dicky Mosier is guilty: True or False?
True (0.85729086409805)
Private First Class Dicky Mosier has mean: True or False?
True (0.9235923286659299)
Private First Class Dicky Mosier has motive: True or False?
True (0.8824278665848695)
Private First Class Dicky Mosier has opportunity: True or False?
True (0.811078188867804)
Private Joe Locke is guilty: True or False?
True (0.8652241235443877)
Private Joe Locke has mean: True or False?
True (0.8086723099497763)
Private Joe Locke has motive: True or False?
True (0.9264369634617509)
Private Joe Locke has opportunity: True or False?
True (0.7813306496768853)
Specialist Fifth Class Ron Henson is guilty: True or False?
True (0.7697732451157533)
Specialist Fifth Class Ron Henson has mean: True or False?
True (0.7527403228571042)
Specialist Fifth Class Ron Henson has motive: True or False?
True (0.7627776774954688)
Specialist Fifth Class Ron Henson has opportunity: True or False?
True (0.6967842494573921)
Specialist Fourth Class Patrick Macnamara is guilty: True or False?
True (0.7969253675907205)
Specialist Fourth Class Patrick Macnamara has mean: True or False?
True (0.6486889055472267)
Specialist Fourth Class Patrick Macnamara has motive: True or False?
True (0.5973730125048408)
Specialist Fourth Class Patrick Macnamara has opportunity: True or False?
True (0.5039061393777357)
### Private First Class Dicky Mosier
- mean: True (0.9235923286659299)
- motive: True (0.8824278665848695)
- opportunity: True (0.811078188867804)

### Private Joe Locke
- mean: False (0.19132769005022365)
- motive: False (0.07356303653824914)
- opportunity: False (0.21866935032311474)

### Specialist Fifth Class Ron Henson
- mean: False (0.24725967714289576)
- motive: False (0.23722232250453124)
- opportunity: False (0.30321575054260785)

### Specialist Fourth Class Patrick Macnamara
- mean: False (0.3513110944527733)
- motive: False (0.40262698749515924)
- opportunity: False (0.49609386062226435)

The culprit is Private First Class Dicky Mosier.
In fact, it is Private Joe Locke.
## 5minutemystery-mystery-on-the-moor
Jack MacGinnis is guilty: True or False?
True (0.9091032147468773)
Jack MacGinnis has mean: True or False?
True (0.8128673413132903)
Jack MacGinnis has motive: True or False?
True (0.7905303264811482)
Jack MacGinnis has opportunity: True or False?
True (0.6876299924560524)
James Macready is guilty: True or False?
True (0.8895288719962232)
James Macready has mean: True or False?
True (0.8719117627136385)
James Macready has motive: True or False?
True (0.8858291535164952)
James Macready has opportunity: True or False?
True (0.6662796746479285)
Samuel Doone is guilty: True or False?
True (0.7779753136455794)
Samuel Doone has mean: True or False?
True (0.784649255215384)
Samuel Doone has motive: True or False?
True (0.7988152492192591)
Samuel Doone has opportunity: True or False?
True (0.5765419579552815)
Tom Jenkins is guilty: True or False?
True (0.8560919228396967)
Tom Jenkins has mean: True or False?
True (0.8116760258690822)
Tom Jenkins has motive: True or False?
True (0.9219218506394821)
Tom Jenkins has opportunity: True or False?
True (0.7461389980806673)
### Jack MacGinnis
- mean: False (0.1871326586867097)
- motive: False (0.20946967351885182)
- opportunity: False (0.3123700075439476)

Map:   2%|▏         | 5/203 [00:45<31:14,  9.47s/ examples]Map:   3%|▎         | 6/203 [01:07<45:12, 13.77s/ examples]Map:   3%|▎         | 7/203 [01:27<50:47, 15.55s/ examples]Map:   4%|▍         | 8/203 [01:41<49:47, 15.32s/ examples]Map:   4%|▍         | 9/203 [01:54<47:11, 14.60s/ examples]### James Macready
- mean: False (0.12808823728636154)
- motive: False (0.11417084648350484)
- opportunity: False (0.3337203253520715)

### Samuel Doone
- mean: False (0.21535074478461602)
- motive: False (0.20118475078074094)
- opportunity: False (0.4234580420447185)

### Tom Jenkins
- mean: True (0.8116760258690822)
- motive: True (0.9219218506394821)
- opportunity: True (0.7461389980806673)

The culprit is Tom Jenkins.
In fact, it is James Macready.
## 5minutemystery-who-stole-curious-george
Dexter is guilty: True or False?
True (0.7956581141325956)
Dexter has mean: True or False?
True (0.7872777601997338)
Dexter has motive: True or False?
True (0.8725647371909419)
Dexter has opportunity: True or False?
True (0.7905303264811482)
Mr. Ferguson is guilty: True or False?
True (0.7049732238008671)
Mr. Ferguson has mean: True or False?
False (0.5273165696704634)
Mr. Ferguson has motive: True or False?
True (0.7379142672364736)
Mr. Ferguson has opportunity: True or False?
False (0.673191669892235)
Mrs. Yee is guilty: True or False?
True (0.7708099365638504)
Mrs. Yee has mean: True or False?
True (0.65489470935198)
Mrs. Yee has motive: True or False?
True (0.7013040666282004)
Mrs. Yee has opportunity: True or False?
True (0.5869964306477841)
Skyler is guilty: True or False?
True (0.6859494535376744)
Skyler has mean: True or False?
False (0.591723272524637)
Skyler has motive: True or False?
True (0.7931059536445917)
Skyler has opportunity: True or False?
True (0.5679366075542497)
### Dexter
- mean: True (0.7872777601997338)
- motive: True (0.8725647371909419)
- opportunity: True (0.7905303264811482)

### Mr. Ferguson
- mean: False (0.5273165696704634)
- motive: False (0.2620857327635264)
- opportunity: False (0.673191669892235)

### Mrs. Yee
- mean: False (0.34510529064802)
- motive: False (0.29869593337179956)
- opportunity: False (0.41300356935221594)

### Skyler
- mean: False (0.591723272524637)
- motive: False (0.2068940463554083)
- opportunity: False (0.4320633924457503)

The culprit is Dexter.
In fact, it is Dexter.
## 5minutemystery-the-saxophones-ghost
Building Manager is guilty: True or False?
True (0.5698527222023703)
Building Manager has mean: True or False?
False (0.7041601500399041)
Building Manager has motive: True or False?
True (0.6610481693322063)
Building Manager has opportunity: True or False?
False (0.8250265073476026)
Eric is guilty: True or False?
True (0.5621764690603255)
Eric has mean: True or False?
True (0.6334102859975052)
Eric has motive: True or False?
True (0.7225270177274575)
Eric has opportunity: True or False?
False (0.5457699116223576)
Lenny is guilty: True or False?
False (0.5573635130218721)
Lenny has mean: True or False?
True (0.5438324636094939)
Lenny has motive: True or False?
True (0.570331332344394)
Lenny has opportunity: True or False?
False (0.5341265295318852)
Red is guilty: True or False?
False (0.5992506238662876)
Red has mean: True or False?
False (0.5506073202694327)
Red has motive: True or False?
False (0.5282900845448565)
Red has opportunity: True or False?
False (0.6688802830862913)
### Building Manager
- mean: False (0.7041601500399041)
- motive: False (0.33895183066779366)
- opportunity: False (0.8250265073476026)

### Eric
- mean: True (0.6334102859975052)
- motive: True (0.7225270177274575)
- opportunity: True (0.45423008837764245)

### Lenny
- mean: False (0.4561675363905061)
- motive: False (0.42966866765560596)
- opportunity: False (0.5341265295318852)

### Red
- mean: False (0.5506073202694327)
- motive: False (0.5282900845448565)
- opportunity: False (0.6688802830862913)

The culprit is Eric.
In fact, it is Building Manager.
## 5minutemystery-who-shot-mom
Dad is guilty: True or False?
True (0.9125920562149515)
Dad has mean: True or False?
True (0.8824278665848695)
Dad has motive: True or False?
True (0.8906751280163339)
Dad has opportunity: True or False?
True (0.8856314413364714)
Randy is guilty: True or False?
True (0.8181563669811865)
Randy has mean: True or False?
True (0.9457010626376176)
Randy has motive: True or False?
True (0.7431679939957333)
Randy has opportunity: True or False?
True (0.8582439976623328)
Roger is guilty: True or False?
True (0.8842393754985511)
Roger has mean: True or False?
True (0.8991213421091365)
Roger has motive: True or False?
True (0.7931059536445917)
Roger has opportunity: True or False?
True (0.8013146490010521)
Rory is guilty: True or False?
True (0.8152325155686644)
Rory has mean: True or False?
True (0.8727816933272936)
Rory has motive: True or False?
True (0.7718434926244166)
Rory has opportunity: True or False?
True (0.7772998201448375)
### Dad
- mean: True (0.8824278665848695)
- motive: True (0.8906751280163339)
- opportunity: True (0.8856314413364714)

### Randy
- mean: False (0.05429893736238245)
- motive: False (0.2568320060042667)
- opportunity: False (0.14175600233766716)

### Roger
- mean: False (0.10087865789086348)
- motive: False (0.2068940463554083)
- opportunity: False (0.1986853509989479)

### Rory
- mean: False (0.1272183066727064)
- motive: False (0.22815650737558335)
- opportunity: False (0.22270017985516255)

The culprit is Dad.
In fact, it is Randy.
## 5minutemystery-finding-the-flower-fund
James Faust is guilty: True or False?
True (0.5389832197022594)
James Faust has mean: True or False?
True (0.8086723099497763)
James Faust has motive: True or False?
True (0.5131804871639641)
James Faust has opportunity: True or False?
False (0.555435161888281)
Justin Thorn is guilty: True or False?
False (0.5175709123121337)
Justin Thorn has mean: True or False?
True (0.844921525814193)
Justin Thorn has motive: True or False?
True (0.5936092727363199)
Justin Thorn has opportunity: True or False?
False (0.6067315356525022)
Lincoln Smith is guilty: True or False?
True (0.6876299924560524)
Lincoln Smith has mean: True or False?
True (0.7431679939957333)
Lincoln Smith has motive: True or False?
True (0.615087855649269)
Lincoln Smith has opportunity: True or False?
True (0.5794003525136094)
Linda Hinton is guilty: True or False?
True (0.6557770400181139)
Linda Hinton has mean: True or False?
True (0.8080671968507699)
Linda Hinton has motive: True or False?
True (0.5727227727404994)
Linda Hinton has opportunity: True or False?
True (0.5945512478395265)
### James Faust
- mean: False (0.19132769005022365)
- motive: False (0.48681951283603586)
- opportunity: False (0.555435161888281)

### Justin Thorn
- mean: False (0.155078474185807)
- motive: False (0.4063907272636801)
- opportunity: False (0.6067315356525022)

### Lincoln Smith
- mean: False (0.2568320060042667)
- motive: False (0.38491214435073096)
- opportunity: False (0.42059964748639056)

### Linda Hinton
- mean: True (0.8080671968507699)
- motive: True (0.5727227727404994)
- opportunity: True (0.5945512478395265)

The culprit is Linda Hinton.
In fact, it is Lincoln Smith.
## 5minutemystery-map-of-the-traitor
Benjamin is guilty: True or False?
True (0.7138307731576955)
Benjamin has mean: True or False?
True (0.642432441257838)
Benjamin has motive: True or False?
True (0.7256486384635821)
Benjamin has opportunity: True or False?
False (0.5602526707659626)
Edward is guilty: True or False?
True (0.686790355176806)
Edward has mean: True or False?
True (0.6566582306092376)
Edward has motive: True or False?
True (0.7146280500737092)
Edward has opportunity: True or False?
False (0.6011253583932805)
Jonathan is guilty: True or False?
True (0.5621764690603255)
Jonathan has mean: True or False?
True (0.6388352560545881)
Jonathan has motive: True or False?
True (0.7431679939957333)
Jonathan has opportunity: True or False?
False (0.595492552580428)
Lucius is guilty: True or False?
True (0.685107355950278)
Lucius has mean: True or False?
True (0.6984322578436808)
Lucius has motive: True or False?
True (0.7885831565209055)
Lucius has opportunity: True or False?
False (0.5126925663186335)
### Benjamin
- mean: False (0.35756755874216195)
- motive: False (0.2743513615364179)
- opportunity: False (0.5602526707659626)

### Edward
- mean: False (0.34334176939076244)
- motive: False (0.2853719499262908)
- opportunity: False (0.6011253583932805)

### Jonathan
- mean: False (0.36116474394541187)
Map:   5%|▍         | 10/203 [02:12<49:54, 15.52s/ examples]Map:   5%|▌         | 11/203 [02:29<51:04, 15.96s/ examples]Map:   6%|▌         | 12/203 [02:57<1:02:19, 19.58s/ examples]Map:   6%|▋         | 13/203 [03:15<1:00:36, 19.14s/ examples]Map:   7%|▋         | 14/203 [03:34<1:00:07, 19.09s/ examples]- motive: False (0.2568320060042667)
- opportunity: False (0.595492552580428)

### Lucius
- mean: True (0.6984322578436808)
- motive: True (0.7885831565209055)
- opportunity: True (0.48730743368136653)

The culprit is Lucius.
In fact, it is Jonathan.
## 5minutemystery-the-crusaders-robe
Captain Fosters is guilty: True or False?
True (0.873646672673131)
Captain Fosters has mean: True or False?
True (0.8591918406281239)
Captain Fosters has motive: True or False?
True (0.8216173055802608)
Captain Fosters has opportunity: True or False?
True (0.6992543888266708)
Godefroi is guilty: True or False?
True (0.9246877442701001)
Godefroi has mean: True or False?
True (0.9497626419596781)
Godefroi has motive: True or False?
True (0.9212159548464016)
Godefroi has opportunity: True or False?
True (0.8261514850267767)
Morgan Grant is guilty: True or False?
True (0.9095862487848758)
Morgan Grant has mean: True or False?
True (0.9422946582938823)
Morgan Grant has motive: True or False?
True (0.9388007508488514)
Morgan Grant has opportunity: True or False?
True (0.745398395394548)
Sir Francis Walters is guilty: True or False?
True (0.9113376724203427)
Sir Francis Walters has mean: True or False?
True (0.9417613738325554)
Sir Francis Walters has motive: True or False?
True (0.9048188910591489)
Sir Francis Walters has opportunity: True or False?
True (0.7049732868303878)
### Captain Fosters
- mean: False (0.14080815937187607)
- motive: False (0.1783826944197392)
- opportunity: False (0.3007456111733292)

### Godefroi
- mean: True (0.9497626419596781)
- motive: True (0.9212159548464016)
- opportunity: True (0.8261514850267767)

### Morgan Grant
- mean: False (0.05770534170611774)
- motive: False (0.061199249151148605)
- opportunity: False (0.254601604605452)

### Sir Francis Walters
- mean: False (0.058238626167444574)
- motive: False (0.09518110894085108)
- opportunity: False (0.29502671316961215)

The culprit is Godefroi.
In fact, it is Godefroi.
## 5minutemystery-mr-patricks-history-class
Corporal Tom Patrick is guilty: True or False?
True (0.9209319968384807)
Corporal Tom Patrick has mean: True or False?
True (0.9492946258008691)
Corporal Tom Patrick has motive: True or False?
True (0.8889517173369674)
Corporal Tom Patrick has opportunity: True or False?
True (0.8410438346117795)
Pvt. Billy Calhoun is guilty: True or False?
True (0.9528381231454964)
Pvt. Billy Calhoun has mean: True or False?
True (0.9637117373129486)
Pvt. Billy Calhoun has motive: True or False?
True (0.9336731438527403)
Pvt. Billy Calhoun has opportunity: True or False?
True (0.9385759849623091)
Pvt. Jack Trueblood is guilty: True or False?
True (0.9463989149207153)
Pvt. Jack Trueblood has mean: True or False?
True (0.9691495281980984)
Pvt. Jack Trueblood has motive: True or False?
True (0.9515039936355008)
Pvt. Jack Trueblood has opportunity: True or False?
True (0.9456006903352807)
Sgt. Patrick Culpepper is guilty: True or False?
True (0.9594592463344039)
Sgt. Patrick Culpepper has mean: True or False?
True (0.9458013187522837)
Sgt. Patrick Culpepper has motive: True or False?
True (0.9365176577773374)
Sgt. Patrick Culpepper has opportunity: True or False?
True (0.9158089188126235)
### Corporal Tom Patrick
- mean: False (0.050705374199130904)
- motive: False (0.11104828266303257)
- opportunity: False (0.15895616538822055)

### Pvt. Billy Calhoun
- mean: False (0.03628826268705143)
- motive: False (0.06632685614725975)
- opportunity: False (0.061424015037690904)

### Pvt. Jack Trueblood
- mean: True (0.9691495281980984)
- motive: True (0.9515039936355008)
- opportunity: True (0.9456006903352807)

### Sgt. Patrick Culpepper
- mean: False (0.05419868124771632)
- motive: False (0.06348234222266258)
- opportunity: False (0.0841910811873765)

The culprit is Pvt. Jack Trueblood.
In fact, it is Pvt. Billy Calhoun.
## 5minutemystery-bigfoot-mystery
Burt is guilty: True or False?
True (0.6951311179371613)
Burt has mean: True or False?
True (0.7162185953247016)
Burt has motive: True or False?
True (0.8098781635062345)
Burt has opportunity: True or False?
False (0.5175708506128766)
Jerry is guilty: True or False?
True (0.8044059309478723)
Jerry has mean: True or False?
True (0.8524448242555318)
Jerry has motive: True or False?
True (0.8577681165234065)
Jerry has opportunity: True or False?
True (0.6575384693006662)
Leng is guilty: True or False?
True (0.6379334932841956)
Leng has mean: True or False?
True (0.5107405858633529)
Leng has motive: True or False?
True (0.7178037814283548)
Leng has opportunity: True or False?
True (0.5973730125048408)
Winston is guilty: True or False?
True (0.7885832152749314)
Winston has mean: True or False?
True (0.779321849347754)
Winston has motive: True or False?
True (0.7193836643711469)
Winston has opportunity: True or False?
True (0.5496406401666291)
### Burt
- mean: False (0.28378140467529844)
- motive: False (0.19012183649376546)
- opportunity: False (0.5175708506128766)

### Jerry
- mean: True (0.8524448242555318)
- motive: True (0.8577681165234065)
- opportunity: True (0.6575384693006662)

### Leng
- mean: False (0.4892594141366471)
- motive: False (0.28219621857164523)
- opportunity: False (0.40262698749515924)

### Winston
- mean: False (0.22067815065224605)
- motive: False (0.28061633562885313)
- opportunity: False (0.45035935983337094)

The culprit is Jerry.
In fact, it is Jerry.
## 5minutemystery-missing-movie-money
Billy is guilty: True or False?
True (0.9347534165970482)
Billy has mean: True or False?
True (0.8868131040663721)
Billy has motive: True or False?
True (0.9769347912465448)
Billy has opportunity: True or False?
True (0.8987665204865408)
Cody is guilty: True or False?
True (0.9087799803825275)
Cody has mean: True or False?
True (0.8381506247725498)
Cody has motive: True or False?
True (0.9699566358821189)
Cody has opportunity: True or False?
True (0.9031234959323464)
Juliet is guilty: True or False?
True (0.905989824801558)
Juliet has mean: True or False?
True (0.9114953293645017)
Juliet has motive: True or False?
True (0.9708816405035137)
Juliet has opportunity: True or False?
True (0.9403530947748038)
Tammy is guilty: True or False?
True (0.6662796746479285)
Tammy has mean: True or False?
True (0.7074046739492601)
Tammy has motive: True or False?
True (0.8980535302052036)
Tammy has opportunity: True or False?
True (0.6469064338453809)
### Billy
- mean: False (0.11318689593362785)
- motive: False (0.02306520875345519)
- opportunity: False (0.10123347951345918)

### Cody
- mean: False (0.16184937522745024)
- motive: False (0.03004336411788111)
- opportunity: False (0.09687650406765358)

### Juliet
- mean: True (0.9114953293645017)
- motive: True (0.9708816405035137)
- opportunity: True (0.9403530947748038)

### Tammy
- mean: False (0.2925953260507399)
- motive: False (0.10194646979479638)
- opportunity: False (0.35309356615461907)

The culprit is Juliet.
In fact, it is Cody.
## 5minutemystery-missing-ammunition
Henry is guilty: True or False?
True (0.8238958672039278)
Henry has mean: True or False?
True (0.7556369876990674)
Henry has motive: True or False?
True (0.9026095892260383)
Henry has opportunity: True or False?
True (0.5234203246639862)
Mr. Samuel is guilty: True or False?
True (0.9127477403975288)
Mr. Samuel has mean: True or False?
True (0.8895288719962232)
Mr. Samuel has motive: True or False?
True (0.9433475737015985)
Mr. Samuel has opportunity: True or False?
True (0.6774740084332073)
Mr. Smith is guilty: True or False?
True (0.9260365949489886)
Mr. Smith has mean: True or False?
True (0.8766344170435998)
Mr. Smith has motive: True or False?
True (0.9445871723447916)
Mr. Smith has opportunity: True or False?
True (0.8019357965963964)
Young Soldier is guilty: True or False?
True (0.8418256009501243)
Young Soldier has mean: True or False?
True (0.9399133323582882)
Young Soldier has motive: True or False?
True (0.8994751578343994)
Young Soldier has opportunity: True or False?
True (0.6951311179371613)
### Henry
- mean: False (0.2443630123009326)
- motive: False (0.09739041077396171)
- opportunity: False (0.47657967533601375)

### Mr. Samuel
- mean: False (0.11047112800377679)
- motive: False (0.056652426298401504)
Map:   7%|▋         | 15/203 [03:51<57:50, 18.46s/ examples]  Map:   8%|▊         | 16/203 [04:11<59:14, 19.01s/ examples]Map:   8%|▊         | 17/203 [04:29<57:32, 18.56s/ examples]Map:   9%|▉         | 18/203 [04:51<1:00:35, 19.65s/ examples]Map:   9%|▉         | 19/203 [05:13<1:02:06, 20.25s/ examples]- opportunity: False (0.32252599156679274)

### Mr. Smith
- mean: True (0.8766344170435998)
- motive: True (0.9445871723447916)
- opportunity: True (0.8019357965963964)

### Young Soldier
- mean: False (0.06008666764171178)
- motive: False (0.10052484216560065)
- opportunity: False (0.3048688820628387)

The culprit is Mr. Smith.
In fact, it is Henry.
## 5minutemystery-the-sky-sleuths
Bug collector is guilty: True or False?
True (0.7541915239138703)
Bug collector has mean: True or False?
True (0.591723272524637)
Bug collector has motive: True or False?
True (0.8357517746704994)
Bug collector has opportunity: True or False?
True (0.685107355950278)
Elderly man is guilty: True or False?
True (0.673191669892235)
Elderly man has mean: True or False?
True (0.5136684743338078)
Elderly man has motive: True or False?
True (0.8255897087847518)
Elderly man has opportunity: True or False?
False (0.5631377056275331)
Family man is guilty: True or False?
True (0.6943026818003076)
Family man has mean: True or False?
False (0.5992506238662876)
Family man has motive: True or False?
True (0.5860491337676195)
Family man has opportunity: True or False?
False (0.5389832197022594)
Motorcyclist is guilty: True or False?
False (0.5370413742099674)
Motorcyclist has mean: True or False?
True (0.589834510337428)
Motorcyclist has motive: True or False?
True (0.6370307821695329)
Motorcyclist has opportunity: True or False?
True (0.5438324636094939)
### Bug collector
- mean: True (0.591723272524637)
- motive: True (0.8357517746704994)
- opportunity: True (0.685107355950278)

### Elderly man
- mean: False (0.4863315256661922)
- motive: False (0.1744102912152482)
- opportunity: False (0.5631377056275331)

### Family man
- mean: False (0.5992506238662876)
- motive: False (0.41395086623238053)
- opportunity: False (0.5389832197022594)

### Motorcyclist
- mean: False (0.41016548966257205)
- motive: False (0.3629692178304671)
- opportunity: False (0.4561675363905061)

The culprit is Bug collector.
In fact, it is Bug collector.
## 5minutemystery-battle-of-the-bulge
Anderson is guilty: True or False?
True (0.5409238326546766)
Anderson has mean: True or False?
False (0.5175708506128766)
Anderson has motive: True or False?
False (0.5457699116223576)
Anderson has opportunity: True or False?
False (0.6817267588564826)
Dilworth is guilty: True or False?
True (0.6242935037467142)
Dilworth has mean: True or False?
True (0.64779823427608)
Dilworth has motive: True or False?
False (0.5727227727404994)
Dilworth has opportunity: True or False?
False (0.6315942370470465)
Maguire is guilty: True or False?
False (0.6504672743423094)
Maguire has mean: True or False?
False (0.7577943897558946)
Maguire has motive: True or False?
False (0.6557770400181139)
Maguire has opportunity: True or False?
False (0.7918210572836727)
Siegel is guilty: True or False?
True (0.5669777909748143)
Siegel has mean: True or False?
False (0.5736783792247284)
Siegel has motive: True or False?
False (0.6141626144170799)
Siegel has opportunity: True or False?
False (0.7468781997658912)
### Anderson
- mean: False (0.5175708506128766)
- motive: False (0.5457699116223576)
- opportunity: False (0.6817267588564826)

### Dilworth
- mean: True (0.64779823427608)
- motive: True (0.42727722725950057)
- opportunity: True (0.36840576295295346)

### Maguire
- mean: False (0.7577943897558946)
- motive: False (0.6557770400181139)
- opportunity: False (0.7918210572836727)

### Siegel
- mean: False (0.5736783792247284)
- motive: False (0.6141626144170799)
- opportunity: False (0.7468781997658912)

The culprit is Dilworth.
In fact, it is Dilworth.
## 5minutemystery-the-missing-button
Eliza Murray is guilty: True or False?
True (0.740174341079517)
Eliza Murray has mean: True or False?
True (0.8514594452543962)
Eliza Murray has motive: True or False?
True (0.9027811324949335)
Eliza Murray has opportunity: True or False?
True (0.6242935781683038)
George Sanders is guilty: True or False?
True (0.6197014353942354)
George Sanders has mean: True or False?
False (0.5370414382302919)
George Sanders has motive: True or False?
False (0.5292633777076584)
George Sanders has opportunity: True or False?
False (0.7962924261546153)
Stable boy Ian is guilty: True or False?
False (0.8883720049821552)
Stable boy Ian has mean: True or False?
False (0.7866228249849953)
Stable boy Ian has motive: True or False?
False (0.7620701143808404)
Stable boy Ian has opportunity: True or False?
False (0.8322366416985943)
Thomas Murray is guilty: True or False?
True (0.7333563569098757)
Thomas Murray has mean: True or False?
True (0.8037906314112822)
Thomas Murray has motive: True or False?
True (0.8654516347931567)
Thomas Murray has opportunity: True or False?
True (0.5360700410935405)
### Eliza Murray
- mean: True (0.8514594452543962)
- motive: True (0.9027811324949335)
- opportunity: True (0.6242935781683038)

### George Sanders
- mean: False (0.5370414382302919)
- motive: False (0.5292633777076584)
- opportunity: False (0.7962924261546153)

### Stable boy Ian
- mean: False (0.7866228249849953)
- motive: False (0.7620701143808404)
- opportunity: False (0.8322366416985943)

### Thomas Murray
- mean: False (0.19620936858871785)
- motive: False (0.13454836520684332)
- opportunity: False (0.4639299589064595)

The culprit is Eliza Murray.
In fact, it is Stable boy Ian.
## 5minutemystery-the-railroad-mystery
Alvarado is guilty: True or False?
True (0.5851012033999957)
Alvarado has mean: True or False?
True (0.5263427467960875)
Alvarado has motive: True or False?
True (0.6749080895533367)
Alvarado has opportunity: True or False?
False (0.5457699116223576)
The engineer is guilty: True or False?
True (0.5370414382302919)
The engineer has mean: True or False?
True (0.6104534962074417)
The engineer has motive: True or False?
True (0.7348812840309261)
The engineer has opportunity: True or False?
True (0.644225125126315)
The mechanic is guilty: True or False?
True (0.6297746298200823)
The mechanic has mean: True or False?
True (0.8122723669190336)
The mechanic has motive: True or False?
True (0.8464508054137014)
The mechanic has opportunity: True or False?
True (0.8397339530959691)
Zebediah is guilty: True or False?
True (0.6486889055472267)
Zebediah has mean: True or False?
True (0.7570766705324253)
Zebediah has motive: True or False?
True (0.8283841584202847)
Zebediah has opportunity: True or False?
True (0.5784481782924303)
### Alvarado
- mean: False (0.4736572532039125)
- motive: False (0.3250919104466633)
- opportunity: False (0.5457699116223576)

### The engineer
- mean: False (0.3895465037925583)
- motive: False (0.2651187159690739)
- opportunity: False (0.355774874873685)

### The mechanic
- mean: True (0.8122723669190336)
- motive: True (0.8464508054137014)
- opportunity: True (0.8397339530959691)

### Zebediah
- mean: False (0.24292332946757467)
- motive: False (0.17161584157971532)
- opportunity: False (0.42155182170756966)

The culprit is The mechanic.
In fact, it is Zebediah.
## 5minutemystery-the-date
Bob is guilty: True or False?
True (0.9599126594957205)
Bob has mean: True or False?
True (0.9826243527033713)
Bob has motive: True or False?
True (0.9410069597342015)
Bob has opportunity: True or False?
True (0.9751071938949272)
Cynthia is guilty: True or False?
True (0.7592253761865491)
Cynthia has mean: True or False?
True (0.9431384818142104)
Cynthia has motive: True or False?
True (0.9063219998220023)
Cynthia has opportunity: True or False?
True (0.7662936378892937)
Diane is guilty: True or False?
True (0.7813306496768853)
Diane has mean: True or False?
True (0.9317114347547434)
Diane has motive: True or False?
True (0.821044090050916)
Diane has opportunity: True or False?
True (0.8397339530959691)
Kristin is guilty: True or False?
True (0.6749080895533367)
Kristin has mean: True or False?
True (0.8376199551237796)
Kristin has motive: True or False?
True (0.7655933544531522)
Kristin has opportunity: True or False?
True (0.8204694405411458)
### Bob
- mean: True (0.9826243527033713)
- motive: True (0.9410069597342015)
- opportunity: True (0.9751071938949272)

### Cynthia
- mean: False (0.05686151818578955)
- motive: False (0.09367800017799766)
Map:  10%|▉         | 20/203 [05:37<1:05:40, 21.53s/ examples]Map:  10%|█         | 21/203 [06:01<1:07:37, 22.29s/ examples]Map:  11%|█         | 22/203 [06:34<1:16:35, 25.39s/ examples]Map:  11%|█▏        | 23/203 [06:57<1:14:22, 24.79s/ examples]Map:  12%|█▏        | 24/203 [07:22<1:13:37, 24.68s/ examples]- opportunity: False (0.23370636211070628)

### Diane
- mean: False (0.06828856524525662)
- motive: False (0.17895590994908395)
- opportunity: False (0.1602660469040309)

### Kristin
- mean: False (0.16238004487622038)
- motive: False (0.23440664554684776)
- opportunity: False (0.1795305594588542)

The culprit is Bob.
In fact, it is Bob.
## 5minutemystery-b-movie-murder
Angela is guilty: True or False?
True (0.5698526542706361)
Angela has mean: True or False?
True (0.5746334908651781)
Angela has motive: True or False?
True (0.6893056096647525)
Angela has opportunity: True or False?
True (0.7287482572006113)
Debbie is guilty: True or False?
True (0.5592899914849522)
Debbie has mean: True or False?
True (0.6187804294217345)
Debbie has motive: True or False?
True (0.5926666351772785)
Debbie has opportunity: True or False?
True (0.7017130830397807)
Sal is guilty: True or False?
True (0.5964331434971528)
Sal has mean: True or False?
True (0.686790355176806)
Sal has motive: True or False?
True (0.7655932860037753)
Sal has opportunity: True or False?
True (0.7859663967519771)
Tom is guilty: True or False?
True (0.5312093625105829)
Tom has mean: True or False?
False (0.5755879969637064)
Tom has motive: True or False?
True (0.6469064916833258)
Tom has opportunity: True or False?
True (0.7233095190955371)
### Angela
- mean: False (0.4253665091348219)
- motive: False (0.3106943903352475)
- opportunity: False (0.2712517427993887)

### Debbie
- mean: False (0.3812195705782655)
- motive: False (0.40733336482272153)
- opportunity: False (0.29828691696021925)

### Sal
- mean: True (0.686790355176806)
- motive: True (0.7655932860037753)
- opportunity: True (0.7859663967519771)

### Tom
- mean: False (0.5755879969637064)
- motive: False (0.3530935083166742)
- opportunity: False (0.2766904809044629)

The culprit is Sal.
In fact, it is Angela.
## 5minutemystery-the-jackie-mitchell-autographed-baseball-mystery
Dr. Edgar Newton is guilty: True or False?
True (0.7472472734767229)
Dr. Edgar Newton has mean: True or False?
True (0.6076631662366868)
Dr. Edgar Newton has motive: True or False?
True (0.7017130830397807)
Dr. Edgar Newton has opportunity: True or False?
False (0.5477060024984176)
Melinda Baker is guilty: True or False?
True (0.821044090050916)
Melinda Baker has mean: True or False?
True (0.8591918406281239)
Melinda Baker has motive: True or False?
True (0.5087881523495457)
Melinda Baker has opportunity: True or False?
False (0.6825737331070684)
Simon Plympton is guilty: True or False?
True (0.8524447734458623)
Simon Plympton has mean: True or False?
True (0.8591918406281239)
Simon Plympton has motive: True or False?
True (0.7804952298233097)
Simon Plympton has opportunity: True or False?
True (0.5640984675176304)
Susan Plympton is guilty: True or False?
True (0.781664133797069)
Susan Plympton has mean: True or False?
True (0.8086723099497763)
Susan Plympton has motive: True or False?
True (0.6109178653970281)
Susan Plympton has opportunity: True or False?
False (0.6011253583932805)
### Dr. Edgar Newton
- mean: False (0.3923368337633132)
- motive: False (0.29828691696021925)
- opportunity: False (0.5477060024984176)

### Melinda Baker
- mean: False (0.14080815937187607)
- motive: False (0.49121184765045434)
- opportunity: False (0.6825737331070684)

### Simon Plympton
- mean: True (0.8591918406281239)
- motive: True (0.7804952298233097)
- opportunity: True (0.5640984675176304)

### Susan Plympton
- mean: False (0.19132769005022365)
- motive: False (0.3890821346029719)
- opportunity: False (0.6011253583932805)

The culprit is Simon Plympton.
In fact, it is Susan Plympton.
## 5minutemystery-the-easter-egg-mystery
Anna is guilty: True or False?
True (0.6187804294217345)
Anna has mean: True or False?
True (0.700075275973927)
Anna has motive: True or False?
True (0.8820220178442959)
Anna has opportunity: True or False?
True (0.8381505623254643)
Cole is guilty: True or False?
True (0.6619228707202935)
Cole has mean: True or False?
True (0.8413048399699521)
Cole has motive: True or False?
True (0.8423451152856819)
Cole has opportunity: True or False?
True (0.8181563669811865)
Justin is guilty: True or False?
True (0.612309626324874)
Justin has mean: True or False?
True (0.7217431689117048)
Justin has motive: True or False?
True (0.8524448242555318)
Justin has opportunity: True or False?
True (0.7969253675907205)
Lizzie is guilty: True or False?
True (0.7240905157396584)
Lizzie has mean: True or False?
True (0.7017130830397807)
Lizzie has motive: True or False?
True (0.815232454829111)
Lizzie has opportunity: True or False?
True (0.8994751578343994)
Rachel is guilty: True or False?
True (0.6959583025067009)
Rachel has mean: True or False?
True (0.7853085971692302)
Rachel has motive: True or False?
True (0.8587185689177256)
Rachel has opportunity: True or False?
True (0.8238958672039278)
### Anna
- mean: False (0.29992472402607295)
- motive: False (0.1179779821557041)
- opportunity: False (0.16184943767453575)

### Cole
- mean: True (0.8413048399699521)
- motive: True (0.8423451152856819)
- opportunity: True (0.8181563669811865)

### Justin
- mean: False (0.27825683108829524)
- motive: False (0.1475551757444682)
- opportunity: False (0.20307463240927948)

### Lizzie
- mean: False (0.29828691696021925)
- motive: False (0.184767545170889)
- opportunity: False (0.10052484216560065)

### Rachel
- mean: False (0.21469140283076982)
- motive: False (0.14128143108227442)
- opportunity: False (0.17610413279607218)

The culprit is Cole.
In fact, it is Lizzie.
## 5minutemystery-easter-rhyme
Abbott is guilty: True or False?
True (0.8539127077831877)
Abbott has mean: True or False?
True (0.8459423727595791)
Abbott has motive: True or False?
True (0.8795611817678315)
Abbott has opportunity: True or False?
True (0.8354835531737983)
Andy is guilty: True or False?
True (0.8344068526674736)
Andy has mean: True or False?
True (0.8089742709319104)
Andy has motive: True or False?
True (0.8499711693725173)
Andy has opportunity: True or False?
True (0.7725306828324007)
Randy is guilty: True or False?
True (0.851212260635415)
Randy has mean: True or False?
True (0.8638517255508926)
Randy has motive: True or False?
True (0.84619676525883)
Randy has opportunity: True or False?
True (0.8267117710471246)
Speedy is guilty: True or False?
True (0.8558511727823209)
Speedy has mean: True or False?
True (0.8723473540228537)
Speedy has motive: True or False?
True (0.8580061839163521)
Speedy has opportunity: True or False?
True (0.794384956668203)
### Abbott
- mean: True (0.8459423727595791)
- motive: True (0.8795611817678315)
- opportunity: True (0.8354835531737983)

### Andy
- mean: False (0.19102572906808957)
- motive: False (0.15002883062748273)
- opportunity: False (0.22746931716759933)

### Randy
- mean: False (0.13614827444910738)
- motive: False (0.15380323474116997)
- opportunity: False (0.17328822895287543)

### Speedy
- mean: False (0.12765264597714632)
- motive: False (0.14199381608364792)
- opportunity: False (0.20561504333179703)

The culprit is Abbott.
In fact, it is Speedy.
## 5minutemystery-the-april-fool
Boston, MA is guilty: True or False?
True (0.7634837587244478)
Boston, MA has mean: True or False?
True (0.7439129430200341)
Boston, MA has motive: True or False?
True (0.8649961951944259)
Boston, MA has opportunity: True or False?
True (0.8797679608387514)
Philadelphia, PA is guilty: True or False?
True (0.8204694405411458)
Philadelphia, PA has mean: True or False?
True (0.8936811689868521)
Philadelphia, PA has motive: True or False?
True (0.844921525814193)
Philadelphia, PA has opportunity: True or False?
True (0.929696145502287)
Pittsburgh, PA is guilty: True or False?
True (0.7994422859301654)
Pittsburgh, PA has mean: True or False?
True (0.8620035048683017)
Pittsburgh, PA has motive: True or False?
True (0.8539127714046447)
Pittsburgh, PA has opportunity: True or False?
True (0.921357630313903)
Raleigh, NC is guilty: True or False?
True (0.6740504984987916)
Raleigh, NC has mean: True or False?
True (0.7718434926244166)
Raleigh, NC has motive: True or False?
True (0.7745833916423246)
Raleigh, NC has opportunity: True or False?
True (0.7981867775042927)
Map:  12%|█▏        | 25/203 [07:52<1:18:37, 26.50s/ examples]Map:  13%|█▎        | 26/203 [08:17<1:16:47, 26.03s/ examples]Map:  13%|█▎        | 27/203 [08:42<1:14:54, 25.54s/ examples]Map:  14%|█▍        | 28/203 [09:09<1:15:44, 25.97s/ examples]Map:  14%|█▍        | 29/203 [09:35<1:15:36, 26.07s/ examples]Washington, DC is guilty: True or False?
True (0.7592253761865491)
Washington, DC has mean: True or False?
True (0.8044059309478723)
Washington, DC has motive: True or False?
True (0.8080671968507699)
Washington, DC has opportunity: True or False?
True (0.8807970862580315)
### Boston, MA
- mean: False (0.2560870569799659)
- motive: False (0.13500380480557406)
- opportunity: False (0.12023203916124858)

### Philadelphia, PA
- mean: True (0.8936811689868521)
- motive: True (0.844921525814193)
- opportunity: True (0.929696145502287)

### Pittsburgh, PA
- mean: False (0.13799649513169832)
- motive: False (0.14608722859535528)
- opportunity: False (0.07864236968609695)

### Raleigh, NC
- mean: False (0.22815650737558335)
- motive: False (0.2254166083576754)
- opportunity: False (0.20181322249570732)

### Washington, DC
- mean: False (0.19559406905212773)
- motive: False (0.1919328031492301)
- opportunity: False (0.11920291374196845)

The culprit is Philadelphia, PA.
In fact, it is Washington, DC.
## 5minutemystery-green-feet
Carm is guilty: True or False?
True (0.811078188867804)
Carm has mean: True or False?
True (0.7585106418731645)
Carm has motive: True or False?
True (0.8086723099497763)
Carm has opportunity: True or False?
True (0.6901415551283886)
Diane is guilty: True or False?
True (0.7813306496768853)
Diane has mean: True or False?
True (0.8787311338092536)
Diane has motive: True or False?
True (0.9289262900494157)
Diane has opportunity: True or False?
True (0.8474634858439474)
Jen is guilty: True or False?
True (0.6976089520497016)
Jen has mean: True or False?
True (0.769080279275001)
Jen has motive: True or False?
True (0.8438951328214825)
Jen has opportunity: True or False?
True (0.769080279275001)
Maureen is guilty: True or False?
True (0.685107355950278)
Maureen has mean: True or False?
True (0.6859494535376744)
Maureen has motive: True or False?
True (0.5341265295318852)
Maureen has opportunity: True or False?
False (0.6926419789019715)
### Carm
- mean: False (0.24148935812683547)
- motive: False (0.19132769005022365)
- opportunity: False (0.3098584448716114)

### Diane
- mean: True (0.8787311338092536)
- motive: True (0.9289262900494157)
- opportunity: True (0.8474634858439474)

### Jen
- mean: False (0.230919720724999)
- motive: False (0.15610486717851746)
- opportunity: False (0.230919720724999)

### Maureen
- mean: False (0.31405054646232555)
- motive: False (0.4658734704681148)
- opportunity: False (0.6926419789019715)

The culprit is Diane.
In fact, it is Diane.
## 5minutemystery-restaurant-roulette
Atsushi Nishi is guilty: True or False?
True (0.8116760258690822)
Atsushi Nishi has mean: True or False?
True (0.8305941261447712)
Atsushi Nishi has motive: True or False?
True (0.6976088896786037)
Atsushi Nishi has opportunity: True or False?
True (0.6749080895533367)
Gianni Girodano is guilty: True or False?
True (0.7534665957068495)
Gianni Girodano has mean: True or False?
True (0.8766343647921183)
Gianni Girodano has motive: True or False?
True (0.7549149897594328)
Gianni Girodano has opportunity: True or False?
True (0.7527403228571042)
Jack McDonald is guilty: True or False?
True (0.8238958672039278)
Jack McDonald has mean: True or False?
True (0.7879311977554747)
Jack McDonald has motive: True or False?
True (0.8647679145346777)
Jack McDonald has opportunity: True or False?
True (0.8255897087847518)
Jean-Pierre Dubois is guilty: True or False?
True (0.9092645024391882)
Jean-Pierre Dubois has mean: True or False?
True (0.9293122320338961)
Jean-Pierre Dubois has motive: True or False?
True (0.925499741040984)
Jean-Pierre Dubois has opportunity: True or False?
True (0.814643384779728)
### Atsushi Nishi
- mean: False (0.16940587385522876)
- motive: False (0.3023911103213963)
- opportunity: False (0.3250919104466633)

### Gianni Girodano
- mean: False (0.12336563520788169)
- motive: False (0.24508501024056717)
- opportunity: False (0.24725967714289576)

### Jack McDonald
- mean: False (0.2120688022445253)
- motive: False (0.13523208546532228)
- opportunity: False (0.1744102912152482)

### Jean-Pierre Dubois
- mean: True (0.9293122320338961)
- motive: True (0.925499741040984)
- opportunity: True (0.814643384779728)

The culprit is Jean-Pierre Dubois.
In fact, it is Gianni Girodano.
## 5minutemystery-violating-the-pirate-code
Bosun Ridley is guilty: True or False?
True (0.8868131040663721)
Bosun Ridley has mean: True or False?
True (0.8606036289596553)
Bosun Ridley has motive: True or False?
True (0.8236122680985841)
Bosun Ridley has opportunity: True or False?
True (0.6610482284345209)
Mr Arbuthnot is guilty: True or False?
True (0.8357518369388613)
Mr Arbuthnot has mean: True or False?
True (0.7648916137833577)
Mr Arbuthnot has motive: True or False?
True (0.7516481378170605)
Mr Arbuthnot has opportunity: True or False?
True (0.5331543669186894)
Nehemiah is guilty: True or False?
True (0.8591918406281239)
Nehemiah has mean: True or False?
True (0.7563575572780217)
Nehemiah has motive: True or False?
True (0.8025555002781843)
Nehemiah has opportunity: True or False?
True (0.7924643196339045)
Will is guilty: True or False?
True (0.844921525814193)
Will has mean: True or False?
True (0.7556369876990674)
Will has motive: True or False?
True (0.8846386054372942)
Will has opportunity: True or False?
True (0.7181992613394055)
### Bosun Ridley
- mean: False (0.13939637104034475)
- motive: False (0.17638773190141588)
- opportunity: False (0.33895177156547907)

### Mr Arbuthnot
- mean: False (0.23510838621664232)
- motive: False (0.24835186218293948)
- opportunity: False (0.46684563308131055)

### Nehemiah
- mean: False (0.24364244272197833)
- motive: False (0.19744449972181566)
- opportunity: False (0.2075356803660955)

### Will
- mean: True (0.7556369876990674)
- motive: True (0.8846386054372942)
- opportunity: True (0.7181992613394055)

The culprit is Will.
In fact, it is Bosun Ridley.
## 5minutemystery-space-station-sagittarius-six-suffers-sabotage
Cpl. Bennington is guilty: True or False?
True (0.9177460685312047)
Cpl. Bennington has mean: True or False?
True (0.9152045868398637)
Cpl. Bennington has motive: True or False?
True (0.8955227118091885)
Cpl. Bennington has opportunity: True or False?
True (0.8333246107254184)
Scrivine is guilty: True or False?
True (0.9076402191395381)
Scrivine has mean: True or False?
True (0.8484706263347676)
Scrivine has motive: True or False?
True (0.8933094122075369)
Scrivine has opportunity: True or False?
True (0.8683809699466569)
Sgt. O'Hennessey is guilty: True or False?
True (0.9375547191885567)
Sgt. O'Hennessey has mean: True or False?
True (0.8868130446009216)
Sgt. O'Hennessey has motive: True or False?
True (0.8050197941712954)
Sgt. O'Hennessey has opportunity: True or False?
True (0.7279754274224494)
Sgt.Valance is guilty: True or False?
True (0.9496693599006181)
Sgt.Valance has mean: True or False?
True (0.8807970862580315)
Sgt.Valance has motive: True or False?
True (0.9199306971612747)
Sgt.Valance has opportunity: True or False?
True (0.9265699426348812)
### Cpl. Bennington
- mean: False (0.08479541316013628)
- motive: False (0.10447728819081148)
- opportunity: False (0.1666753892745816)

### Scrivine
- mean: False (0.15152937366523245)
- motive: False (0.1066905877924631)
- opportunity: False (0.13161903005334308)

### Sgt. O'Hennessey
- mean: False (0.11318695539907841)
- motive: False (0.19498020582870457)
- opportunity: False (0.27202457257755064)

### Sgt.Valance
- mean: True (0.8807970862580315)
- motive: True (0.9199306971612747)
- opportunity: True (0.9265699426348812)

The culprit is Sgt.Valance.
In fact, it is Sgt.Valance.
## 5minutemystery-flying-saucer-of-new-mexico
Dora is guilty: True or False?
False (0.6415346823638186)
Dora has mean: True or False?
True (0.6842640081724978)
Dora has motive: True or False?
True (0.6039317779631047)
Dora has opportunity: True or False?
False (0.5869964306477841)
Lester is guilty: True or False?
True (0.5774953314585229)
Lester has mean: True or False?
True (0.8376200175313318)
Lester has motive: True or False?
True (0.7779753136455794)
Lester has opportunity: True or False?
False (0.5175709123121337)
Uncle Art is guilty: True or False?
Map:  15%|█▍        | 30/203 [09:59<1:13:49, 25.61s/ examples]Map:  15%|█▌        | 31/203 [10:28<1:16:11, 26.58s/ examples]Map:  16%|█▌        | 32/203 [11:01<1:21:22, 28.55s/ examples]Map:  16%|█▋        | 33/203 [11:27<1:18:13, 27.61s/ examples]Map:  17%|█▋        | 34/203 [11:56<1:18:59, 28.04s/ examples]True (0.6469064338453809)
Uncle Art has mean: True or False?
True (0.8816149238192855)
Uncle Art has motive: True or False?
True (0.8000678954040312)
Uncle Art has opportunity: True or False?
True (0.5860490988363701)
Zach is guilty: True or False?
False (0.6076631662366868)
Zach has mean: True or False?
True (0.8278281666221954)
Zach has motive: True or False?
True (0.7690802105138688)
Zach has opportunity: True or False?
True (0.687629930977143)
### Dora
- mean: False (0.3157359918275022)
- motive: False (0.3960682220368953)
- opportunity: False (0.5869964306477841)

### Lester
- mean: False (0.16237998246866825)
- motive: False (0.22202468635442063)
- opportunity: False (0.5175709123121337)

### Uncle Art
- mean: False (0.11838507618071448)
- motive: False (0.19993210459596877)
- opportunity: False (0.41395090116362987)

### Zach
- mean: True (0.8278281666221954)
- motive: True (0.7690802105138688)
- opportunity: True (0.687629930977143)

The culprit is Zach.
In fact, it is Dora.
## 5minutemystery-great-musket-mystery
Lyle Day is guilty: True or False?
True (0.8509646659219744)
Lyle Day has mean: True or False?
True (0.8951566249612815)
Lyle Day has motive: True or False?
True (0.9018342514529875)
Lyle Day has opportunity: True or False?
True (0.8620035690925699)
Mary Wright is guilty: True or False?
True (0.8303191093049147)
Mary Wright has mean: True or False?
True (0.8198933606225757)
Mary Wright has motive: True or False?
True (0.7799928701983835)
Mary Wright has opportunity: True or False?
True (0.6311396940785249)
Paul Revere is guilty: True or False?
True (0.7641883982873323)
Paul Revere has mean: True or False?
True (0.8098781635062345)
Paul Revere has motive: True or False?
True (0.8591918406281239)
Paul Revere has opportunity: True or False?
True (0.7613610520273686)
Stevie Brown is guilty: True or False?
True (0.8795611817678315)
Stevie Brown has mean: True or False?
True (0.9355823382423648)
Stevie Brown has motive: True or False?
True (0.9170058945178141)
Stevie Brown has opportunity: True or False?
True (0.8984105603938967)
### Lyle Day
- mean: False (0.10484337503871854)
- motive: False (0.09816574854701254)
- opportunity: False (0.13799643090743008)

### Mary Wright
- mean: False (0.18010663937742433)
- motive: False (0.22000712980161652)
- opportunity: False (0.3688603059214751)

### Paul Revere
- mean: False (0.19012183649376546)
- motive: False (0.14080815937187607)
- opportunity: False (0.2386389479726314)

### Stevie Brown
- mean: True (0.9355823382423648)
- motive: True (0.9170058945178141)
- opportunity: True (0.8984105603938967)

The culprit is Stevie Brown.
In fact, it is Lyle Day.
## 5minutemystery-true-green-a-st-patricks-day-mystery
Emily Carpenter is guilty: True or False?
True (0.8902941942359355)
Emily Carpenter has mean: True or False?
True (0.8577681165234065)
Emily Carpenter has motive: True or False?
True (0.8872045854516336)
Emily Carpenter has opportunity: True or False?
True (0.7325918054337844)
Evan Carpenter is guilty: True or False?
True (0.8842393162056825)
Evan Carpenter has mean: True or False?
True (0.7988153087356352)
Evan Carpenter has motive: True or False?
True (0.9198588150310912)
Evan Carpenter has opportunity: True or False?
True (0.8654516347931567)
Richie Harris is guilty: True or False?
True (0.9000915285488901)
Richie Harris has mean: True or False?
True (0.8413047772878592)
Richie Harris has motive: True or False?
True (0.9218515162673044)
Richie Harris has opportunity: True or False?
True (0.8918110138739693)
Zachary MacDonald is guilty: True or False?
True (0.9194980842090085)
Zachary MacDonald has mean: True or False?
True (0.9326989068252284)
Zachary MacDonald has motive: True or False?
True (0.947913945956991)
Zachary MacDonald has opportunity: True or False?
True (0.8929365260632085)
### Emily Carpenter
- mean: False (0.14223188347659355)
- motive: False (0.11279541454836639)
- opportunity: False (0.26740819456621556)

### Evan Carpenter
- mean: False (0.20118469126436478)
- motive: False (0.08014118496890876)
- opportunity: False (0.13454836520684332)

### Richie Harris
- mean: False (0.15869522271214076)
- motive: False (0.07814848373269556)
- opportunity: False (0.10818898612603067)

### Zachary MacDonald
- mean: True (0.9326989068252284)
- motive: True (0.947913945956991)
- opportunity: True (0.8929365260632085)

The culprit is Zachary MacDonald.
In fact, it is Emily Carpenter.
## 5minutemystery-st-patricks-day-pearls
Christopher is guilty: True or False?
True (0.8019358443954961)
Christopher has mean: True or False?
True (0.8591918406281239)
Christopher has motive: True or False?
True (0.5409238971378262)
Christopher has opportunity: True or False?
True (0.6224592927728324)
Earl is guilty: True or False?
True (0.5973730125048408)
Earl has mean: True or False?
True (0.897695304229796)
Earl has motive: True or False?
True (0.5312093625105829)
Earl has opportunity: True or False?
True (0.5195213440667139)
Robert is guilty: True or False?
True (0.6048657973050737)
Robert has mean: True or False?
True (0.8499711693725173)
Robert has motive: True or False?
False (0.5496406074054949)
Robert has opportunity: True or False?
True (0.5009765603034438)
Tom is guilty: True or False?
True (0.7599387683150569)
Tom has mean: True or False?
True (0.8615382357584752)
Tom has motive: True or False?
False (0.6388353131709135)
Tom has opportunity: True or False?
True (0.5592900581575188)
### Christopher
- mean: True (0.8591918406281239)
- motive: True (0.5409238971378262)
- opportunity: True (0.6224592927728324)

### Earl
- mean: False (0.10230469577020396)
- motive: False (0.4687906374894171)
- opportunity: False (0.4804786559332861)

### Robert
- mean: False (0.15002883062748273)
- motive: False (0.5496406074054949)
- opportunity: False (0.49902343969655616)

### Tom
- mean: False (0.1384617642415248)
- motive: False (0.6388353131709135)
- opportunity: False (0.44070994184248125)

The culprit is Christopher.
In fact, it is Tom.
## 5minutemystery-death-in-the-theatre
Helen Smith is guilty: True or False?
True (0.8264318083792933)
Helen Smith has mean: True or False?
True (0.7819973291046377)
Helen Smith has motive: True or False?
True (0.8134607635851566)
Helen Smith has opportunity: True or False?
True (0.6654105193867614)
Joanne Driscoll is guilty: True or False?
True (0.8155264872684852)
Joanne Driscoll has mean: True or False?
True (0.9265699426348812)
Joanne Driscoll has motive: True or False?
True (0.7759445796581789)
Joanne Driscoll has opportunity: True or False?
True (0.6636689235052821)
Kevin Doyle is guilty: True or False?
True (0.8504685773080045)
Kevin Doyle has mean: True or False?
True (0.8128672807499561)
Kevin Doyle has motive: True or False?
True (0.7563575572780217)
Kevin Doyle has opportunity: True or False?
True (0.6834195192071987)
Sarah Jones is guilty: True or False?
True (0.8255897087847518)
Sarah Jones has mean: True or False?
True (0.8543993851297865)
Sarah Jones has motive: True or False?
True (0.7386690954574974)
Sarah Jones has opportunity: True or False?
True (0.5496406074054949)
### Helen Smith
- mean: False (0.2180026708953623)
- motive: False (0.18653923641484338)
- opportunity: False (0.33458948061323857)

### Joanne Driscoll
- mean: True (0.9265699426348812)
- motive: True (0.7759445796581789)
- opportunity: True (0.6636689235052821)

### Kevin Doyle
- mean: False (0.18713271925004393)
- motive: False (0.24364244272197833)
- opportunity: False (0.3165804807928013)

### Sarah Jones
- mean: False (0.14560061487021347)
- motive: False (0.26133090454250263)
- opportunity: False (0.4503593925945051)

The culprit is Joanne Driscoll.
In fact, it is Kevin Doyle.
## 5minutemystery-death-at-andersonville
Corporal Wardlow Horner is guilty: True or False?
True (0.8267118326419537)
Corporal Wardlow Horner has mean: True or False?
True (0.7978720077929541)
Corporal Wardlow Horner has motive: True or False?
True (0.7209580648179327)
Corporal Wardlow Horner has opportunity: True or False?
True (0.6415346250061509)
Private Jamie Whisenant is guilty: True or False?
True (0.7541915688671895)
Private Jamie Whisenant has mean: True or False?
True (0.6662796746479285)
Map:  17%|█▋        | 35/203 [12:18<1:13:44, 26.34s/ examples]Map:  18%|█▊        | 36/203 [12:43<1:12:09, 25.93s/ examples]Map:  18%|█▊        | 37/203 [13:05<1:08:06, 24.62s/ examples]Map:  19%|█▊        | 38/203 [13:26<1:04:41, 23.52s/ examples]Map:  19%|█▉        | 39/203 [13:52<1:06:50, 24.46s/ examples]Private Jamie Whisenant has motive: True or False?
True (0.6141626144170799)
Private Jamie Whisenant has opportunity: True or False?
False (0.6992544513448877)
Sergeant Coleman Crosby is guilty: True or False?
True (0.7302898714065358)
Sergeant Coleman Crosby has mean: True or False?
True (0.7997552678397243)
Sergeant Coleman Crosby has motive: True or False?
True (0.49999999904767284)
Sergeant Coleman Crosby has opportunity: True or False?
True (0.5029296229885981)
Sergeant Josiah Thornton is guilty: True or False?
True (0.7098244343353132)
Sergeant Josiah Thornton has mean: True or False?
True (0.6817267588564826)
Sergeant Josiah Thornton has motive: True or False?
False (0.6001883144765984)
Sergeant Josiah Thornton has opportunity: True or False?
False (0.5331544304756466)
### Corporal Wardlow Horner
- mean: True (0.7978720077929541)
- motive: True (0.7209580648179327)
- opportunity: True (0.6415346250061509)

### Private Jamie Whisenant
- mean: False (0.3337203253520715)
- motive: False (0.38583738558292013)
- opportunity: False (0.6992544513448877)

### Sergeant Coleman Crosby
- mean: False (0.20024473216027572)
- motive: False (0.5000000009523271)
- opportunity: False (0.4970703770114019)

### Sergeant Josiah Thornton
- mean: False (0.3182732411435174)
- motive: False (0.6001883144765984)
- opportunity: False (0.5331544304756466)

The culprit is Corporal Wardlow Horner.
In fact, it is Sergeant Josiah Thornton.
## 5minutemystery-the-big-game
Carli Antor is guilty: True or False?
True (0.9273632783787477)
Carli Antor has mean: True or False?
True (0.9449946880768697)
Carli Antor has motive: True or False?
True (0.8816149238192855)
Carli Antor has opportunity: True or False?
True (0.5418937216067536)
Chuck Jarrett is guilty: True or False?
True (0.9114953904850286)
Chuck Jarrett has mean: True or False?
True (0.9073122118500465)
Chuck Jarrett has motive: True or False?
True (0.8514594452543962)
Chuck Jarrett has opportunity: True or False?
True (0.5841525779336078)
Rich Pender is guilty: True or False?
True (0.905656637917298)
Rich Pender has mean: True or False?
True (0.9355823382423648)
Rich Pender has motive: True or False?
True (0.6233768940588188)
Rich Pender has opportunity: True or False?
False (0.5688949093320547)
Tom Barrett is guilty: True or False?
True (0.9196425651151865)
Tom Barrett has mean: True or False?
True (0.8951566249612815)
Tom Barrett has motive: True or False?
True (0.769080279275001)
Tom Barrett has opportunity: True or False?
True (0.5631377056275331)
### Carli Antor
- mean: True (0.9449946880768697)
- motive: True (0.8816149238192855)
- opportunity: True (0.5418937216067536)

### Chuck Jarrett
- mean: False (0.09268778814995349)
- motive: False (0.1485405547456038)
- opportunity: False (0.41584742206639225)

### Rich Pender
- mean: False (0.06441766175763519)
- motive: False (0.3766231059411812)
- opportunity: False (0.5688949093320547)

### Tom Barrett
- mean: False (0.10484337503871854)
- motive: False (0.230919720724999)
- opportunity: False (0.43686229437246693)

The culprit is Carli Antor.
In fact, it is Tom Barrett.
## 5minutemystery-the-liberty-gun
Bob Turkle is guilty: True or False?
True (0.6884683992569801)
Bob Turkle has mean: True or False?
True (0.5621764690603255)
Bob Turkle has motive: True or False?
True (0.833053108978257)
Bob Turkle has opportunity: True or False?
True (0.6817267588564826)
Captain Parker is guilty: True or False?
True (0.8824278665848695)
Captain Parker has mean: True or False?
True (0.6909763109505791)
Captain Parker has motive: True or False?
True (0.8891444205417208)
Captain Parker has opportunity: True or False?
True (0.8354835531737983)
Paul Rhodes is guilty: True or False?
True (0.6671476985798853)
Paul Rhodes has mean: True or False?
False (0.6504672161860058)
Paul Rhodes has motive: True or False?
True (0.7468781997658912)
Paul Rhodes has opportunity: True or False?
True (0.5380123829088157)
Tom Wise is guilty: True or False?
True (0.6884684608108543)
Tom Wise has mean: True or False?
False (0.5612148661921673)
Tom Wise has motive: True or False?
True (0.7759445334082792)
Tom Wise has opportunity: True or False?
True (0.5389832197022594)
### Bob Turkle
- mean: False (0.4378235309396745)
- motive: False (0.16694689102174298)
- opportunity: False (0.3182732411435174)

### Captain Parker
- mean: True (0.6909763109505791)
- motive: True (0.8891444205417208)
- opportunity: True (0.8354835531737983)

### Paul Rhodes
- mean: False (0.6504672161860058)
- motive: False (0.2531218002341088)
- opportunity: False (0.4619876170911843)

### Tom Wise
- mean: False (0.5612148661921673)
- motive: False (0.22405546659172082)
- opportunity: False (0.4610167802977406)

The culprit is Captain Parker.
In fact, it is Captain Parker.
## 5minutemystery-summer-camp
Allie is guilty: True or False?
True (0.8062431235779619)
Allie has mean: True or False?
True (0.8828325273478573)
Allie has motive: True or False?
True (0.9173026661190045)
Allie has opportunity: True or False?
True (0.9066531685310133)
Danny is guilty: True or False?
True (0.8267118326419537)
Danny has mean: True or False?
True (0.9447913165152162)
Danny has motive: True or False?
True (0.9032942081209032)
Danny has opportunity: True or False?
True (0.9233161821369215)
Diane's campers is guilty: True or False?
False (0.5136684743338078)
Diane's campers has mean: True or False?
True (0.8820220178442959)
Diane's campers has motive: True or False?
True (0.8958875533219306)
Diane's campers has opportunity: True or False?
True (0.779321849347754)
Tom is guilty: True or False?
True (0.8044058710149623)
Tom has mean: True or False?
True (0.8322366416985943)
Tom has motive: True or False?
True (0.9407897579933674)
Tom has opportunity: True or False?
True (0.9299510719523877)
### Allie
- mean: False (0.11716747265214267)
- motive: False (0.08269733388099554)
- opportunity: False (0.0933468314689867)

### Danny
- mean: True (0.9447913165152162)
- motive: True (0.9032942081209032)
- opportunity: True (0.9233161821369215)

### Diane's campers
- mean: False (0.1179779821557041)
- motive: False (0.1041124466780694)
- opportunity: False (0.22067815065224605)

### Tom
- mean: False (0.16776335830140565)
- motive: False (0.05921024200663261)
- opportunity: False (0.07004892804761231)

The culprit is Danny.
In fact, it is Tom.
## 5minutemystery-mystery-at-lyndleys-fort
Bo is guilty: True or False?
True (0.6261241441180464)
Bo has mean: True or False?
True (0.772530728878819)
Bo has motive: True or False?
True (0.7162185953247016)
Bo has opportunity: True or False?
True (0.6113819501087365)
John is guilty: True or False?
True (0.6513547823127435)
John has mean: True or False?
True (0.6671476389322356)
John has motive: True or False?
True (0.6548947679041324)
John has opportunity: True or False?
False (0.5204963206682631)
John's wife is guilty: True or False?
True (0.5936093435000638)
John's wife has mean: True or False?
True (0.514644215419305)
John's wife has motive: True or False?
True (0.6123096993178739)
John's wife has opportunity: True or False?
False (0.5794003525136094)
Nathan Drew is guilty: True or False?
True (0.7512833387594996)
Nathan Drew has mean: True or False?
True (0.7918210572836727)
Nathan Drew has motive: True or False?
True (0.5058591351869154)
Nathan Drew has opportunity: True or False?
True (0.525368812147771)
### Bo
- mean: True (0.772530728878819)
- motive: True (0.7162185953247016)
- opportunity: True (0.6113819501087365)

### John
- mean: False (0.3328523610677644)
- motive: False (0.34510523209586763)
- opportunity: False (0.5204963206682631)

### John's wife
- mean: False (0.48535578458069495)
- motive: False (0.38769030068212607)
- opportunity: False (0.5794003525136094)

### Nathan Drew
- mean: False (0.2081789427163273)
- motive: False (0.4941408648130846)
- opportunity: False (0.474631187852229)

The culprit is Bo.
In fact, it is Nathan Drew.
## 5minutemystery-riddle-of-the-confederate-spy
Garrett is guilty: True or False?
True (0.8134607635851566)
Garrett has mean: True or False?
True (0.6774740084332073)
Garrett has motive: True or False?
True (0.7302898278778687)
Garrett has opportunity: True or False?
Map:  20%|█▉        | 40/203 [14:13<1:03:34, 23.40s/ examples]Map:  20%|██        | 41/203 [14:43<1:08:13, 25.27s/ examples]Map:  21%|██        | 42/203 [15:11<1:10:15, 26.18s/ examples]Map:  21%|██        | 43/203 [15:36<1:08:32, 25.70s/ examples]True (0.6242935037467142)
McMurty is guilty: True or False?
True (0.811078188867804)
McMurty has mean: True or False?
True (0.646013666311734)
McMurty has motive: True or False?
True (0.6592954931819778)
McMurty has opportunity: True or False?
True (0.589834510337428)
Parker is guilty: True or False?
True (0.8294919722593475)
Parker has mean: True or False?
False (0.5583269696343842)
Parker has motive: True or False?
True (0.7098243920264812)
Parker has opportunity: True or False?
True (0.6297746298200823)
Winslow is guilty: True or False?
True (0.7416740115009234)
Winslow has mean: True or False?
True (0.7872777601997338)
Winslow has motive: True or False?
True (0.7371581892031299)
Winslow has opportunity: True or False?
True (0.6187805031861143)
### Garrett
- mean: False (0.32252599156679274)
- motive: False (0.26971017212213133)
- opportunity: False (0.3757064962532858)

### McMurty
- mean: False (0.35398633368826604)
- motive: False (0.3407045068180222)
- opportunity: False (0.41016548966257205)

### Parker
- mean: False (0.5583269696343842)
- motive: False (0.2901756079735188)
- opportunity: False (0.37022537017991775)

### Winslow
- mean: True (0.7872777601997338)
- motive: True (0.7371581892031299)
- opportunity: True (0.6187805031861143)

The culprit is Winslow.
In fact, it is Parker.
## 5minutemystery-thin-ice
Hortence Lacombe is guilty: True or False?
True (1.1753115908088394)
Hortence Lacombe has mean: True or False?
True (0.8193157928301305)
Hortence Lacombe has motive: True or False?
True (0.875361437979977)
Hortence Lacombe has opportunity: True or False?
True (0.7162185953247016)
Joe Tucker is guilty: True or False?
True (1.3047351787611419)
Joe Tucker has mean: True or False?
True (0.9092645024391882)
Joe Tucker has motive: True or False?
True (0.9644220465248259)
Joe Tucker has opportunity: True or False?
True (0.7956581141325956)
Mikey Chanowski is guilty: True or False?
True (0.955152093302995)
Mikey Chanowski has mean: True or False?
True (0.7826624547920057)
Mikey Chanowski has motive: True or False?
True (0.9412234437340664)
Mikey Chanowski has opportunity: True or False?
True (0.7409249009267298)
Shea Callaghan is guilty: True or False?
True (0.9177460685312047)
Shea Callaghan has mean: True or False?
True (0.8899121304559661)
Shea Callaghan has motive: True or False?
True (0.8322366416985943)
Shea Callaghan has opportunity: True or False?
True (0.7759445334082792)
### Hortence Lacombe
- mean: False (0.18068420716986955)
- motive: False (0.12463856202002299)
- opportunity: False (0.28378140467529844)

### Joe Tucker
- mean: True (0.9092645024391882)
- motive: True (0.9644220465248259)
- opportunity: True (0.7956581141325956)

### Mikey Chanowski
- mean: False (0.2173375452079943)
- motive: False (0.05877655626593359)
- opportunity: False (0.2590750990732702)

### Shea Callaghan
- mean: False (0.11008786954403393)
- motive: False (0.16776335830140565)
- opportunity: False (0.22405546659172082)

The culprit is Joe Tucker.
In fact, it is Shea Callaghan.
## 5minutemystery-flouted
Chloe Streamer is guilty: True or False?
True (0.7364006034245382)
Chloe Streamer has mean: True or False?
True (0.7563575572780217)
Chloe Streamer has motive: True or False?
True (0.8381505623254643)
Chloe Streamer has opportunity: True or False?
False (0.6076631662366868)
Lyle Esposito is guilty: True or False?
True (0.8899121304559661)
Lyle Esposito has mean: True or False?
True (0.9127477403975288)
Lyle Esposito has motive: True or False?
True (0.8710367026584496)
Lyle Esposito has opportunity: True or False?
True (0.6388353131709135)
Marty Nolan is guilty: True or False?
True (0.8740772565226612)
Marty Nolan has mean: True or False?
True (0.9086178579521682)
Marty Nolan has motive: True or False?
True (0.8795611817678315)
Marty Nolan has opportunity: True or False?
True (0.6178585826183487)
Susan Moorgate is guilty: True or False?
True (0.8370879250561812)
Susan Moorgate has mean: True or False?
True (0.9049869164790318)
Susan Moorgate has motive: True or False?
True (0.7969253675907205)
Susan Moorgate has opportunity: True or False?
False (0.5907791930117218)
### Chloe Streamer
- mean: False (0.24364244272197833)
- motive: False (0.16184943767453575)
- opportunity: False (0.6076631662366868)

### Lyle Esposito
- mean: True (0.9127477403975288)
- motive: True (0.8710367026584496)
- opportunity: True (0.6388353131709135)

### Marty Nolan
- mean: False (0.0913821420478318)
- motive: False (0.12043881823216851)
- opportunity: False (0.3821414173816513)

### Susan Moorgate
- mean: False (0.09501308352096816)
- motive: False (0.20307463240927948)
- opportunity: False (0.5907791930117218)

The culprit is Lyle Esposito.
In fact, it is Marty Nolan.
## 5minutemystery-car-trouble
Mr. Carlson is guilty: True or False?
True (0.7806625377756776)
Mr. Carlson has mean: True or False?
True (0.8883720049821552)
Mr. Carlson has motive: True or False?
True (0.9175984877579624)
Mr. Carlson has opportunity: True or False?
True (0.7988153087356352)
Mr. Leamington is guilty: True or False?
True (0.879146760693242)
Mr. Leamington has mean: True or False?
True (0.8906751877407573)
Mr. Leamington has motive: True or False?
True (0.9224823751318276)
Mr. Leamington has opportunity: True or False?
True (0.8238958672039278)
Mrs. Roberts is guilty: True or False?
True (0.8812065732757132)
Mrs. Roberts has mean: True or False?
True (0.9381240005131491)
Mrs. Roberts has motive: True or False?
True (0.952397347230678)
Mrs. Roberts has opportunity: True or False?
True (0.8906751877407573)
Randy Peters is guilty: True or False?
True (0.816406362162552)
Randy Peters has mean: True or False?
True (0.8683809699466569)
Randy Peters has motive: True or False?
True (0.879146760693242)
Randy Peters has opportunity: True or False?
True (0.6680145240815963)
### Mr. Carlson
- mean: False (0.11162799501784482)
- motive: False (0.08240151224203762)
- opportunity: False (0.20118469126436478)

### Mr. Leamington
- mean: False (0.10932481225924273)
- motive: False (0.07751762486817237)
- opportunity: False (0.17610413279607218)

### Mrs. Roberts
- mean: True (0.9381240005131491)
- motive: True (0.952397347230678)
- opportunity: True (0.8906751877407573)

### Randy Peters
- mean: False (0.13161903005334308)
- motive: False (0.12085323930675795)
- opportunity: False (0.33198547591840366)

The culprit is Mrs. Roberts.
In fact, it is Randy Peters.
## 5minutemystery-mr-poes-birthday-party
Anthony is guilty: True or False?
True (0.6370307821695329)
Anthony has mean: True or False?
True (0.7592253761865491)
Anthony has motive: True or False?
True (0.8918110736745599)
Anthony has opportunity: True or False?
True (0.6951311179371613)
Connor is guilty: True or False?
True (0.7969253675907205)
Connor has mean: True or False?
True (0.7911764307711107)
Connor has motive: True or False?
True (0.9479621664653681)
Connor has opportunity: True or False?
True (0.814643384779728)
Skylar is guilty: True or False?
True (0.6893056096647525)
Skylar has mean: True or False?
True (0.6388353131709135)
Skylar has motive: True or False?
True (0.8050197941712954)
Skylar has opportunity: True or False?
False (0.5234203246639862)
Stephen is guilty: True or False?
True (0.7606506998655483)
Stephen has mean: True or False?
True (0.767689835247798)
Stephen has motive: True or False?
True (0.9099069836112468)
Stephen has opportunity: True or False?
True (0.6918097672776748)
Tommy is guilty: True or False?
True (0.6592954931819778)
Tommy has mean: True or False?
True (0.821044090050916)
Tommy has motive: True or False?
True (0.7264255794048772)
Tommy has opportunity: True or False?
True (0.6370307821695329)
### Anthony
- mean: False (0.24077462381345094)
- motive: False (0.10818892632544008)
- opportunity: False (0.3048688820628387)

### Connor
- mean: True (0.7911764307711107)
- motive: True (0.9479621664653681)
- opportunity: True (0.814643384779728)

### Skylar
- mean: False (0.36116468682908653)
- motive: False (0.19498020582870457)
- opportunity: False (0.5234203246639862)

### Stephen
- mean: False (0.232310164752202)
- motive: False (0.09009301638875322)
- opportunity: False (0.30819023272232515)

### Tommy
Map:  22%|██▏       | 44/203 [16:06<1:11:18, 26.91s/ examples]Map:  22%|██▏       | 45/203 [16:32<1:10:22, 26.72s/ examples]Map:  23%|██▎       | 46/203 [17:01<1:11:29, 27.32s/ examples]Map:  23%|██▎       | 47/203 [17:27<1:10:37, 27.16s/ examples]Map:  24%|██▎       | 48/203 [17:53<1:09:23, 26.86s/ examples]- mean: False (0.17895590994908395)
- motive: False (0.2735744205951228)
- opportunity: False (0.3629692178304671)

The culprit is Connor.
In fact, it is Connor.
## 5minutemystery-the-root-of-all-evil
Bryan Durell is guilty: True or False?
True (0.884837803442546)
Bryan Durell has mean: True or False?
True (0.8216173667955227)
Bryan Durell has motive: True or False?
True (0.6522414601874995)
Bryan Durell has opportunity: True or False?
True (0.5841525779336078)
Grieve Collier is guilty: True or False?
True (0.7310585348819939)
Grieve Collier has mean: True or False?
True (0.5973730125048408)
Grieve Collier has motive: True or False?
True (0.5360700410935405)
Grieve Collier has opportunity: True or False?
True (0.5321819753403337)
Jacques Bourbonne is guilty: True or False?
True (0.867485409735739)
Jacques Bourbonne has mean: True or False?
True (0.811078188867804)
Jacques Bourbonne has motive: True or False?
True (0.7950222460539826)
Jacques Bourbonne has opportunity: True or False?
True (0.6252093370817647)
Ruth Majick is guilty: True or False?
True (0.8947895144283036)
Ruth Majick has mean: True or False?
True (0.8000678477162699)
Ruth Majick has motive: True or False?
True (0.7962924854830264)
Ruth Majick has opportunity: True or False?
True (0.7711548223101617)
### Bryan Durell
- mean: False (0.17838263320447734)
- motive: False (0.3477585398125005)
- opportunity: False (0.41584742206639225)

### Grieve Collier
- mean: False (0.40262698749515924)
- motive: False (0.4639299589064595)
- opportunity: False (0.46781802465966627)

### Jacques Bourbonne
- mean: False (0.18892181113219597)
- motive: False (0.20497775394601736)
- opportunity: False (0.37479066291823526)

### Ruth Majick
- mean: True (0.8000678477162699)
- motive: True (0.7962924854830264)
- opportunity: True (0.7711548223101617)

The culprit is Ruth Majick.
In fact, it is Bryan Durell.
## 5minutemystery-get-the-lead-out
Benjamin Trodger is guilty: True or False?
True (0.9548162209309636)
Benjamin Trodger has mean: True or False?
True (0.8828325273478573)
Benjamin Trodger has motive: True or False?
True (0.9677776702396809)
Benjamin Trodger has opportunity: True or False?
True (0.9008791478232747)
Cynthia Kirwan is guilty: True or False?
True (0.8795611817678315)
Cynthia Kirwan has mean: True or False?
True (0.794384956668203)
Cynthia Kirwan has motive: True or False?
True (0.8529354946829077)
Cynthia Kirwan has opportunity: True or False?
False (0.5467381591701916)
Dan Skinner is guilty: True or False?
True (0.945399403620829)
Dan Skinner has mean: True or False?
True (0.8402589628813668)
Dan Skinner has motive: True or False?
True (0.9428234118096998)
Dan Skinner has opportunity: True or False?
True (0.8056321690561029)
Shel Jonas is guilty: True or False?
True (0.8807970862580315)
Shel Jonas has mean: True or False?
True (0.869271276026005)
Shel Jonas has motive: True or False?
True (0.873646672673131)
Shel Jonas has opportunity: True or False?
True (0.580352018589158)
### Benjamin Trodger
- mean: True (0.8828325273478573)
- motive: True (0.9677776702396809)
- opportunity: True (0.9008791478232747)

### Cynthia Kirwan
- mean: False (0.20561504333179703)
- motive: False (0.14706450531709225)
- opportunity: False (0.5467381591701916)

### Dan Skinner
- mean: False (0.1597410371186332)
- motive: False (0.05717658819030025)
- opportunity: False (0.1943678309438971)

### Shel Jonas
- mean: False (0.13072872397399504)
- motive: False (0.126353327326869)
- opportunity: False (0.41964798141084203)

The culprit is Benjamin Trodger.
In fact, it is Dan Skinner.
## 5minutemystery-popping-a-wheelie
Cory is guilty: True or False?
True (0.8803863464576128)
Cory has mean: True or False?
True (0.924959242644946)
Cory has motive: True or False?
True (0.9142907234091052)
Cory has opportunity: True or False?
True (0.8283842201397164)
David is guilty: True or False?
True (0.884837803442546)
David has mean: True or False?
True (0.9036349079321685)
David has motive: True or False?
True (0.9563089618154458)
David has opportunity: True or False?
True (0.8467044802440825)
Mark is guilty: True or False?
True (0.8484706895507578)
Mark has mean: True or False?
True (0.9190632712053527)
Mark has motive: True or False?
True (0.9481545078856665)
Mark has opportunity: True or False?
True (0.802555560073231)
String is guilty: True or False?
True (0.8247443993706964)
String has mean: True or False?
True (0.8734309071535719)
String has motive: True or False?
True (0.9472835653937188)
String has opportunity: True or False?
True (0.8565725156795254)
### Cory
- mean: False (0.075040757355054)
- motive: False (0.08570927659089478)
- opportunity: False (0.17161577986028365)

### David
- mean: True (0.9036349079321685)
- motive: True (0.9563089618154458)
- opportunity: True (0.8467044802440825)

### Mark
- mean: False (0.0809367287946473)
- motive: False (0.051845492114333536)
- opportunity: False (0.19744443992676897)

### String
- mean: False (0.12656909284642814)
- motive: False (0.05271643460628117)
- opportunity: False (0.14342748432047459)

The culprit is David.
In fact, it is David.
## 5minutemystery-the-mystery-of-the-leprechauns-trophy
Barry is guilty: True or False?
True (0.9274947665741009)
Barry has mean: True or False?
True (0.7556369876990674)
Barry has motive: True or False?
True (0.9105453462677353)
Barry has opportunity: True or False?
True (0.875361437979977)
Casey is guilty: True or False?
True (0.9019206778000431)
Casey has mean: True or False?
True (0.6477981763584071)
Casey has motive: True or False?
True (0.927099763868178)
Casey has opportunity: True or False?
True (0.8868131040663721)
Mr. Carswell is guilty: True or False?
True (0.8677098176365254)
Mr. Carswell has mean: True or False?
True (0.7225270177274575)
Mr. Carswell has motive: True or False?
True (0.7826624547920057)
Mr. Carswell has opportunity: True or False?
True (0.6451199006197486)
Tony is guilty: True or False?
True (0.7994423454932595)
Tony has mean: True or False?
False (0.6619228707202935)
Tony has motive: True or False?
True (0.7862948177096581)
Tony has opportunity: True or False?
True (0.5506073202694327)
### Barry
- mean: True (0.7556369876990674)
- motive: True (0.9105453462677353)
- opportunity: True (0.875361437979977)

### Casey
- mean: False (0.3522018236415929)
- motive: False (0.07290023613182195)
- opportunity: False (0.11318689593362785)

### Mr. Carswell
- mean: False (0.27747298227254247)
- motive: False (0.2173375452079943)
- opportunity: False (0.35488009938025145)

### Tony
- mean: False (0.6619228707202935)
- motive: False (0.21370518229034186)
- opportunity: False (0.4493926797305673)

The culprit is Barry.
In fact, it is Tony.
## 5minutemystery-the-mysterious-chicken
Ed is guilty: True or False?
True (0.8294919722593475)
Ed has mean: True or False?
True (0.8656789607733094)
Ed has motive: True or False?
True (0.9629528509146777)
Ed has opportunity: True or False?
True (0.8349459127213729)
Ed's mother is guilty: True or False?
True (0.7759445334082792)
Ed's mother has mean: True or False?
False (0.503906199448032)
Ed's mother has motive: True or False?
True (0.9196425103002197)
Ed's mother has opportunity: True or False?
True (0.6757646168022439)
Ed’s Husky is guilty: True or False?
True (0.8873999116020591)
Ed’s Husky has mean: True or False?
True (0.842345065078002)
Ed’s Husky has motive: True or False?
True (0.9289262900494157)
Ed’s Husky has opportunity: True or False?
True (0.8652240590801695)
Zeke is guilty: True or False?
True (0.9187722208906307)
Zeke has mean: True or False?
True (0.875361437979977)
Zeke has motive: True or False?
True (0.9529258022651363)
Zeke has opportunity: True or False?
True (0.9113376724203427)
### Ed
- mean: False (0.1343210392266906)
- motive: False (0.03704714908532225)
- opportunity: False (0.16505408727862714)

### Ed's mother
- mean: False (0.503906199448032)
- motive: False (0.0803574896997803)
- opportunity: False (0.32423538319775613)

### Ed’s Husky
- mean: False (0.157654934921998)
- motive: False (0.07107370995058426)
- opportunity: False (0.13477594091983047)

### Zeke
- mean: True (0.875361437979977)
- motive: True (0.9529258022651363)
Map:  24%|██▍       | 49/203 [18:19<1:07:34, 26.33s/ examples]Map:  25%|██▍       | 50/203 [18:37<1:00:51, 23.87s/ examples]Map:  25%|██▌       | 51/203 [19:08<1:06:06, 26.09s/ examples]Map:  26%|██▌       | 52/203 [19:36<1:07:02, 26.64s/ examples]Map:  26%|██▌       | 53/203 [20:05<1:08:18, 27.33s/ examples]- opportunity: True (0.9113376724203427)

The culprit is Zeke.
In fact, it is Ed.
## 5minutemystery-the-late-night-horror-show
Andrew is guilty: True or False?
False (0.6020615685826383)
Andrew has mean: True or False?
True (0.5243946792389143)
Andrew has motive: True or False?
True (0.7446563307563252)
Andrew has opportunity: True or False?
False (0.5486734987923966)
David is guilty: True or False?
True (0.5736784476125245)
David has mean: True or False?
True (0.7599387683150569)
David has motive: True or False?
True (0.8891444205417208)
David has opportunity: True or False?
True (0.8454326959560526)
Dennis is guilty: True or False?
True (0.5312093941731293)
Dennis has mean: True or False?
True (0.7033457711626864)
Dennis has motive: True or False?
True (0.6766198919456847)
Dennis has opportunity: True or False?
True (0.7041600870830834)
Matthew is guilty: True or False?
True (0.5370414382302919)
Matthew has mean: True or False?
True (0.8013146490010521)
Matthew has motive: True or False?
True (0.8519527857346616)
Matthew has opportunity: True or False?
True (0.833324548637899)
### Andrew
- mean: False (0.47560532076108575)
- motive: False (0.2553436692436748)
- opportunity: False (0.5486734987923966)

### David
- mean: True (0.7599387683150569)
- motive: True (0.8891444205417208)
- opportunity: True (0.8454326959560526)

### Dennis
- mean: False (0.2966542288373136)
- motive: False (0.3233801080543153)
- opportunity: False (0.2958399129169166)

### Matthew
- mean: False (0.1986853509989479)
- motive: False (0.1480472142653384)
- opportunity: False (0.16667545136210105)

The culprit is David.
In fact, it is David.
## 5minutemystery-making-partner
Dan Cartman is guilty: True or False?
True (0.7985012549449481)
Dan Cartman has mean: True or False?
True (0.9049869771631355)
Dan Cartman has motive: True or False?
True (0.8255897087847518)
Dan Cartman has opportunity: True or False?
True (0.7756047866813147)
Jill is guilty: True or False?
False (0.5292633777076584)
Jill has mean: True or False?
True (0.8546421464778325)
Jill has motive: True or False?
True (0.7221353097845661)
Jill has opportunity: True or False?
False (0.5525396910980834)
Mike Creighton is guilty: True or False?
True (0.71582149676272)
Mike Creighton has mean: True or False?
True (0.6909763109505791)
Mike Creighton has motive: True or False?
True (0.5893619100975267)
Mike Creighton has opportunity: True or False?
True (0.5302364729224919)
Mrs. Krantz is guilty: True or False?
True (0.7829945121976718)
Mrs. Krantz has mean: True or False?
True (0.7836574849371717)
Mrs. Krantz has motive: True or False?
True (0.7154240000492645)
Mrs. Krantz has opportunity: True or False?
True (0.6817267588564826)
### Dan Cartman
- mean: True (0.9049869771631355)
- motive: True (0.8255897087847518)
- opportunity: True (0.7756047866813147)

### Jill
- mean: False (0.14535785352216746)
- motive: False (0.2778646902154339)
- opportunity: False (0.5525396910980834)

### Mike Creighton
- mean: False (0.3090236890494209)
- motive: False (0.4106380899024733)
- opportunity: False (0.4697635270775081)

### Mrs. Krantz
- mean: False (0.2163425150628283)
- motive: False (0.28457599995073546)
- opportunity: False (0.3182732411435174)

The culprit is Dan Cartman.
In fact, it is Mike Creighton.
## 5minutemystery-no-retreat-from-death
Amanda Kent is guilty: True or False?
False (0.5185462156586879)
Amanda Kent has mean: True or False?
True (0.8376200175313318)
Amanda Kent has motive: True or False?
True (0.5350984235603058)
Amanda Kent has opportunity: True or False?
False (0.6288633913849659)
Craig Willis is guilty: True or False?
True (0.7272012283179254)
Craig Willis has mean: True or False?
True (0.8499711693725173)
Craig Willis has motive: True or False?
True (0.6774740084332073)
Craig Willis has opportunity: True or False?
True (0.5869964306477841)
Niles Anderson is guilty: True or False?
True (0.6315943123389512)
Niles Anderson has mean: True or False?
True (0.7937461674149602)
Niles Anderson has motive: True or False?
True (0.6224593484250324)
Niles Anderson has opportunity: True or False?
False (0.5136684743338078)
Stephanie Clark is guilty: True or False?
False (0.5583269696343842)
Stephanie Clark has mean: True or False?
True (0.5992506238662876)
Stephanie Clark has motive: True or False?
False (0.6076631662366868)
Stephanie Clark has opportunity: True or False?
False (0.8122724274380432)
### Amanda Kent
- mean: False (0.16237998246866825)
- motive: False (0.4649015764396942)
- opportunity: False (0.6288633913849659)

### Craig Willis
- mean: True (0.8499711693725173)
- motive: True (0.6774740084332073)
- opportunity: True (0.5869964306477841)

### Niles Anderson
- mean: False (0.20625383258503982)
- motive: False (0.37754065157496763)
- opportunity: False (0.5136684743338078)

### Stephanie Clark
- mean: False (0.4007493761337124)
- motive: False (0.6076631662366868)
- opportunity: False (0.8122724274380432)

The culprit is Craig Willis.
In fact, it is Niles Anderson.
## 5minutemystery-a-monster-of-a-mystery
Donald is guilty: True or False?
True (0.8044059309478723)
Donald has mean: True or False?
True (0.8762112821835625)
Donald has motive: True or False?
True (0.8764230069135861)
Donald has opportunity: True or False?
True (0.705785027818136)
Linda is guilty: True or False?
True (0.7431679939957333)
Linda has mean: True or False?
True (0.9102267057681164)
Linda has motive: True or False?
True (0.8770562402180104)
Linda has opportunity: True or False?
True (0.6274948163226559)
Randy is guilty: True or False?
True (0.6884683992569801)
Randy has mean: True or False?
True (0.9268353022276509)
Randy has motive: True or False?
True (0.9403530352223053)
Randy has opportunity: True or False?
True (0.8022458575739914)
Wendell is guilty: True or False?
True (0.5156199352405011)
Wendell has mean: True or False?
True (0.7859664553110391)
Wendell has motive: True or False?
True (0.6901415551283886)
Wendell has opportunity: True or False?
False (0.5292634408007735)
### Donald
- mean: False (0.12378871781643752)
- motive: False (0.1235769930864139)
- opportunity: False (0.294214972181864)

### Linda
- mean: False (0.08977329423188363)
- motive: False (0.12294375978198957)
- opportunity: False (0.3725051836773441)

### Randy
- mean: True (0.9268353022276509)
- motive: True (0.9403530352223053)
- opportunity: True (0.8022458575739914)

### Wendell
- mean: False (0.21403354468896085)
- motive: False (0.3098584448716114)
- opportunity: False (0.5292634408007735)

The culprit is Randy.
In fact, it is Linda.
## 5minutemystery-chow-baby
Beryl Hives is guilty: True or False?
False (0.5204963827162634)
Beryl Hives has mean: True or False?
True (0.6976088896786037)
Beryl Hives has motive: True or False?
True (0.6988435356735703)
Beryl Hives has opportunity: True or False?
False (0.6261242000979097)
Dawn de Jong is guilty: True or False?
True (0.5331543669186894)
Dawn de Jong has mean: True or False?
True (0.5321819753403337)
Dawn de Jong has motive: True or False?
True (0.5568816117266226)
Dawn de Jong has opportunity: True or False?
False (0.7272012283179254)
Konrad Pushkin is guilty: True or False?
True (0.7178038242127955)
Konrad Pushkin has mean: True or False?
True (0.5078118305218892)
Konrad Pushkin has motive: True or False?
True (0.7352616086060775)
Konrad Pushkin has opportunity: True or False?
False (0.5888891269161294)
Pete Stampkowski is guilty: True or False?
True (0.7170118721569225)
Pete Stampkowski has mean: True or False?
True (0.6893056096647525)
Pete Stampkowski has motive: True or False?
True (0.8207569718385453)
Pete Stampkowski has opportunity: True or False?
True (0.5156199352405011)
### Beryl Hives
- mean: False (0.3023911103213963)
- motive: False (0.30115646432642973)
- opportunity: False (0.6261242000979097)

### Dawn de Jong
- mean: False (0.46781802465966627)
- motive: False (0.44311838827337735)
- opportunity: False (0.7272012283179254)

### Konrad Pushkin
- mean: False (0.49218816947811084)
- motive: False (0.2647383913939225)
- opportunity: False (0.5888891269161294)

### Pete Stampkowski
- mean: True (0.6893056096647525)
- motive: True (0.8207569718385453)
Map:  27%|██▋       | 54/203 [20:31<1:07:18, 27.11s/ examples]Map:  27%|██▋       | 55/203 [21:09<1:14:31, 30.21s/ examples]Map:  28%|██▊       | 56/203 [21:44<1:17:53, 31.79s/ examples]Map:  28%|██▊       | 57/203 [22:18<1:18:20, 32.19s/ examples]Map:  29%|██▊       | 58/203 [22:51<1:18:37, 32.54s/ examples]- opportunity: True (0.5156199352405011)

The culprit is Pete Stampkowski.
In fact, it is Beryl Hives.
## 5minutemystery-the-mystery-of-the-frowning-clown
Bumbo is guilty: True or False?
True (0.6992544513448877)
Bumbo has mean: True or False?
True (0.8193157317863493)
Bumbo has motive: True or False?
True (0.8883720049821552)
Bumbo has opportunity: True or False?
True (0.7721872989468889)
Dusty is guilty: True or False?
True (0.7859664553110391)
Dusty has mean: True or False?
True (0.7924642605907138)
Dusty has motive: True or False?
True (0.8940517282497483)
Dusty has opportunity: True or False?
True (0.8104789202520752)
Mr. Green is guilty: True or False?
True (0.8428632044363634)
Mr. Green has mean: True or False?
True (0.9081302297583123)
Mr. Green has motive: True or False?
True (0.9312751898083738)
Mr. Green has opportunity: True or False?
True (0.8040984260198152)
Stage Manager is guilty: True or False?
True (0.7627776774954688)
Stage Manager has mean: True or False?
True (0.8454326455643386)
Stage Manager has motive: True or False?
True (0.8050197941712954)
Stage Manager has opportunity: True or False?
True (0.7364006034245382)
### Bumbo
- mean: False (0.1806842682136507)
- motive: False (0.11162799501784482)
- opportunity: False (0.22781270105311113)

### Dusty
- mean: False (0.20753573940928616)
- motive: False (0.10594827175025168)
- opportunity: False (0.18952107974792476)

### Mr. Green
- mean: True (0.9081302297583123)
- motive: True (0.9312751898083738)
- opportunity: True (0.8040984260198152)

### Stage Manager
- mean: False (0.15456735443566139)
- motive: False (0.19498020582870457)
- opportunity: False (0.26359939657546183)

The culprit is Mr. Green.
In fact, it is Stage Manager.
## 5minutemystery-the-strangest-sport-of-all
Ernie is guilty: True or False?
True (0.9246877442701001)
Ernie has mean: True or False?
True (0.8951566249612815)
Ernie has motive: True or False?
True (0.9322068701708559)
Ernie has opportunity: True or False?
True (0.9012274173198201)
Gordon is guilty: True or False?
True (0.9481545078856665)
Gordon has mean: True or False?
True (0.9233161821369215)
Gordon has motive: True or False?
True (0.9733929040540585)
Gordon has opportunity: True or False?
True (0.9324532728823121)
Jesse is guilty: True or False?
True (0.9335520893498362)
Jesse has mean: True or False?
True (0.869271276026005)
Jesse has motive: True or False?
True (0.9210741501882456)
Jesse has opportunity: True or False?
True (0.8929365260632085)
Mac is guilty: True or False?
True (0.9677167542009312)
Mac has mean: True or False?
True (0.8951566849862127)
Mac has motive: True or False?
True (0.9529258022651363)
Mac has opportunity: True or False?
True (0.8933094122075369)
### Ernie
- mean: False (0.10484337503871854)
- motive: False (0.0677931298291441)
- opportunity: False (0.09877258268017985)

### Gordon
- mean: True (0.9233161821369215)
- motive: True (0.9733929040540585)
- opportunity: True (0.9324532728823121)

### Jesse
- mean: False (0.13072872397399504)
- motive: False (0.07892584981175443)
- opportunity: False (0.1070634739367915)

### Mac
- mean: False (0.1048433150137873)
- motive: False (0.047074197734863654)
- opportunity: False (0.1066905877924631)

The culprit is Gordon.
In fact, it is Jesse.
## 5minutemystery-who-stole-storimons-wallet
Danny is guilty: True or False?
True (0.8875949368741688)
Danny has mean: True or False?
True (0.8998277786460391)
Danny has motive: True or False?
True (0.9314625284362855)
Danny has opportunity: True or False?
True (0.8349459127213729)
Mick is guilty: True or False?
True (0.7634837587244478)
Mick has mean: True or False?
True (0.9284088027271398)
Mick has motive: True or False?
True (0.8244619332958376)
Mick has opportunity: True or False?
True (0.8047130138702729)
Mr. Storimon is guilty: True or False?
True (0.9177460685312047)
Mr. Storimon has mean: True or False?
True (0.9001793304600783)
Mr. Storimon has motive: True or False?
True (0.9174506641307638)
Mr. Storimon has opportunity: True or False?
True (0.81197440178368)
Policeman is guilty: True or False?
True (0.7641883982873323)
Policeman has mean: True or False?
True (0.7498207054286419)
Policeman has motive: True or False?
True (0.8333246107254184)
Policeman has opportunity: True or False?
True (0.6996649413792725)
### Danny
- mean: True (0.8998277786460391)
- motive: True (0.9314625284362855)
- opportunity: True (0.8349459127213729)

### Mick
- mean: False (0.07159119727286023)
- motive: False (0.1755380667041624)
- opportunity: False (0.19528698612972706)

### Mr. Storimon
- mean: False (0.09982066953992175)
- motive: False (0.08254933586923618)
- opportunity: False (0.18802559821632003)

### Policeman
- mean: False (0.2501792945713581)
- motive: False (0.1666753892745816)
- opportunity: False (0.3003350586207275)

The culprit is Danny.
In fact, it is Mr. Storimon.
## 5minutemystery-miles-archer-solves-a-case
Arnold Grossmecker is guilty: True or False?
True (0.8519527857346616)
Arnold Grossmecker has mean: True or False?
True (0.8407825844829613)
Arnold Grossmecker has motive: True or False?
True (0.8591918406281239)
Arnold Grossmecker has opportunity: True or False?
True (0.6825737331070684)
Brigid Jellicoe is guilty: True or False?
True (0.8929365260632085)
Brigid Jellicoe has mean: True or False?
True (0.905989824801558)
Brigid Jellicoe has motive: True or False?
True (0.8428631416381634)
Brigid Jellicoe has opportunity: True or False?
True (0.7962924854830264)
Quinton Jesselton is guilty: True or False?
True (0.8751481831208795)
Quinton Jesselton has mean: True or False?
True (0.911809923444246)
Quinton Jesselton has motive: True or False?
True (0.8762112821835625)
Quinton Jesselton has opportunity: True or False?
True (0.7240905804783984)
Sandra O’Malley is guilty: True or False?
True (0.8062431836477579)
Sandra O’Malley has mean: True or False?
True (0.9337940192482527)
Sandra O’Malley has motive: True or False?
True (0.8000678954040312)
Sandra O’Malley has opportunity: True or False?
True (0.6557770400181139)
### Arnold Grossmecker
- mean: False (0.15921741551703872)
- motive: False (0.14080815937187607)
- opportunity: False (0.31742626689293163)

### Brigid Jellicoe
- mean: True (0.905989824801558)
- motive: True (0.8428631416381634)
- opportunity: True (0.7962924854830264)

### Quinton Jesselton
- mean: False (0.08819007655575395)
- motive: False (0.12378871781643752)
- opportunity: False (0.27590941952160164)

### Sandra O’Malley
- mean: False (0.06620598075174733)
- motive: False (0.19993210459596877)
- opportunity: False (0.3442229599818861)

The culprit is Brigid Jellicoe.
In fact, it is Quinton Jesselton.
## 5minutemystery-murder-in-the-early-morning
Constance is guilty: True or False?
True (0.8107787408238168)
Constance has mean: True or False?
True (0.9319595674053855)
Constance has motive: True or False?
True (0.7669925046333297)
Constance has opportunity: True or False?
True (0.8338664756137771)
John is guilty: True or False?
True (0.6522414018725713)
John has mean: True or False?
True (0.8305941261447712)
John has motive: True or False?
True (0.6662796746479285)
John has opportunity: True or False?
True (0.7962924854830264)
Nancy is guilty: True or False?
True (0.6206215556999736)
Nancy has mean: True or False?
True (0.7356416038392981)
Nancy has motive: True or False?
True (0.6800292740030767)
Nancy has opportunity: True or False?
True (0.6680145240815963)
Vernon is guilty: True or False?
True (0.8241790481509624)
Vernon has mean: True or False?
True (0.8951566249612815)
Vernon has motive: True or False?
True (0.705785027818136)
Vernon has opportunity: True or False?
True (0.802555560073231)
### Constance
- mean: True (0.9319595674053855)
- motive: True (0.7669925046333297)
- opportunity: True (0.8338664756137771)

### John
- mean: False (0.16940587385522876)
- motive: False (0.3337203253520715)
- opportunity: False (0.20370751451697355)

### Nancy
- mean: False (0.2643583961607019)
- motive: False (0.31997072599692333)
- opportunity: False (0.33198547591840366)

### Vernon
- mean: False (0.10484337503871854)
- motive: False (0.294214972181864)
- opportunity: False (0.19744443992676897)

Map:  29%|██▉       | 59/203 [23:15<1:12:12, 30.08s/ examples]Map:  30%|██▉       | 60/203 [23:41<1:08:42, 28.83s/ examples]Map:  30%|███       | 61/203 [24:15<1:11:45, 30.32s/ examples]Map:  31%|███       | 62/203 [24:52<1:16:14, 32.45s/ examples]Map:  31%|███       | 63/203 [25:17<1:10:27, 30.19s/ examples]The culprit is Constance.
In fact, it is Vernon.
## 5minutemystery-raiding-cane
Brent Pearson is guilty: True or False?
False (0.5535053004623279)
Brent Pearson has mean: True or False?
True (0.5399537807786099)
Brent Pearson has motive: True or False?
False (0.5784481782924303)
Brent Pearson has opportunity: True or False?
False (0.8591917766133458)
Frank Weiss is guilty: True or False?
True (0.8679338697256817)
Frank Weiss has mean: True or False?
True (0.8606036289596553)
Frank Weiss has motive: True or False?
True (0.8659058819563623)
Frank Weiss has opportunity: True or False?
True (0.5640984675176304)
Michael Weiss is guilty: True or False?
True (0.6976089520497016)
Michael Weiss has mean: True or False?
True (0.8732148436000907)
Michael Weiss has motive: True or False?
True (0.6992543888266708)
Michael Weiss has opportunity: True or False?
False (0.6495786332146115)
Ronald Weiss is guilty: True or False?
True (0.6325027218909103)
Ronald Weiss has mean: True or False?
True (0.8723474190177988)
Ronald Weiss has motive: True or False?
True (0.6680145240815963)
Ronald Weiss has opportunity: True or False?
False (0.6513548405484016)
### Brent Pearson
- mean: False (0.4600462192213901)
- motive: False (0.5784481782924303)
- opportunity: False (0.8591917766133458)

### Frank Weiss
- mean: True (0.8606036289596553)
- motive: True (0.8659058819563623)
- opportunity: True (0.5640984675176304)

### Michael Weiss
- mean: False (0.12678515639990928)
- motive: False (0.3007456111733292)
- opportunity: False (0.6495786332146115)

### Ronald Weiss
- mean: False (0.12765258098220122)
- motive: False (0.33198547591840366)
- opportunity: False (0.6513548405484016)

The culprit is Frank Weiss.
In fact, it is Frank Weiss.
## 5minutemystery-the-missing-dagger
Chris Palmer is guilty: True or False?
True (0.9167081124681512)
Chris Palmer has mean: True or False?
True (0.8656789607733094)
Chris Palmer has motive: True or False?
True (0.9376689781587124)
Chris Palmer has opportunity: True or False?
True (0.7898827135821628)
Matthew Light is guilty: True or False?
True (0.8534247816107388)
Matthew Light has mean: True or False?
True (0.7745833916423246)
Matthew Light has motive: True or False?
True (0.920217993899809)
Matthew Light has opportunity: True or False?
True (0.8454326455643386)
Mitchell Land is guilty: True or False?
True (0.9012274173198201)
Mitchell Land has mean: True or False?
True (0.8524448242555318)
Mitchell Land has motive: True or False?
True (0.9631613481972502)
Mitchell Land has opportunity: True or False?
True (0.708212608228071)
Paul Benham is guilty: True or False?
True (0.8727816933272936)
Paul Benham has mean: True or False?
True (0.726425644352388)
Paul Benham has motive: True or False?
True (0.873646620599733)
Paul Benham has opportunity: True or False?
True (0.6918097672776748)
Russell Smith is guilty: True or False?
True (0.7648916137833577)
Russell Smith has mean: True or False?
True (0.8244619332958376)
Russell Smith has motive: True or False?
True (0.869271276026005)
Russell Smith has opportunity: True or False?
True (0.621540893468236)
### Chris Palmer
- mean: True (0.8656789607733094)
- motive: True (0.9376689781587124)
- opportunity: True (0.7898827135821628)

### Matthew Light
- mean: False (0.2254166083576754)
- motive: False (0.07978200610019104)
- opportunity: False (0.15456735443566139)

### Mitchell Land
- mean: False (0.1475551757444682)
- motive: False (0.03683865180274981)
- opportunity: False (0.29178739177192903)

### Paul Benham
- mean: False (0.273574355647612)
- motive: False (0.12635337940026703)
- opportunity: False (0.30819023272232515)

### Russell Smith
- mean: False (0.1755380667041624)
- motive: False (0.13072872397399504)
- opportunity: False (0.37845910653176396)

The culprit is Chris Palmer.
In fact, it is Paul Benham.
## 5minutemystery-mystery-of-the-bratty-kid
Angelita is guilty: True or False?
True (0.8887587777822111)
Angelita has mean: True or False?
True (0.847967740521315)
Angelita has motive: True or False?
True (0.8656789607733094)
Angelita has opportunity: True or False?
True (0.8887587777822111)
Emily is guilty: True or False?
True (0.8906751877407573)
Emily has mean: True or False?
True (0.9238675252821831)
Emily has motive: True or False?
True (0.8902942539348153)
Emily has opportunity: True or False?
True (0.9127478016020363)
Jessica is guilty: True or False?
True (0.8181563669811865)
Jessica has mean: True or False?
True (0.7931058945535956)
Jessica has motive: True or False?
True (0.8198933606225757)
Jessica has opportunity: True or False?
True (0.8539127714046447)
Percy Wellington is guilty: True or False?
True (0.9576753972844966)
Percy Wellington has mean: True or False?
True (0.9360516072812131)
Percy Wellington has motive: True or False?
True (0.9489172681310486)
Percy Wellington has opportunity: True or False?
True (0.9606574760904091)
### Angelita
- mean: False (0.15203225947868504)
- motive: False (0.1343210392266906)
- opportunity: False (0.11124122221778887)

### Emily
- mean: False (0.07613247471781692)
- motive: False (0.10970574606518468)
- opportunity: False (0.08725219839796372)

### Jessica
- mean: False (0.2068941054464044)
- motive: False (0.18010663937742433)
- opportunity: False (0.14608722859535528)

### Percy Wellington
- mean: True (0.9360516072812131)
- motive: True (0.9489172681310486)
- opportunity: True (0.9606574760904091)

The culprit is Percy Wellington.
In fact, it is Angelita.
## 5minutemystery-the-card-shark
The cowboy is guilty: True or False?
True (0.8519527857346616)
The cowboy has mean: True or False?
True (0.7146280500737092)
The cowboy has motive: True or False?
True (0.7752646804088963)
The cowboy has opportunity: True or False?
True (0.8056321690561029)
The gunslinger is guilty: True or False?
True (0.9216402157401415)
The gunslinger has mean: True or False?
True (0.8615382357584752)
The gunslinger has motive: True or False?
True (0.8872045854516336)
The gunslinger has opportunity: True or False?
True (0.8770561879413864)
The lady is guilty: True or False?
True (0.8098781635062345)
The lady has mean: True or False?
True (0.7697732451157533)
The lady has motive: True or False?
True (0.8868131040663721)
The lady has opportunity: True or False?
True (0.8272706865691472)
The sheriff is guilty: True or False?
True (0.8433798528114077)
The sheriff has mean: True or False?
True (0.743912876509037)
The sheriff has motive: True or False?
True (0.776622945813876)
The sheriff has opportunity: True or False?
True (0.8233283740192667)
### The cowboy
- mean: False (0.2853719499262908)
- motive: False (0.2247353195911037)
- opportunity: False (0.1943678309438971)

### The gunslinger
- mean: True (0.8615382357584752)
- motive: True (0.8872045854516336)
- opportunity: True (0.8770561879413864)

### The lady
- mean: False (0.2302267548842467)
- motive: False (0.11318689593362785)
- opportunity: False (0.17272931343085285)

### The sheriff
- mean: False (0.25608712349096296)
- motive: False (0.22337705418612397)
- opportunity: False (0.17667162598073327)

The culprit is The gunslinger.
In fact, it is The sheriff.
## 5minutemystery-department-store-murder
Ed Puckett is guilty: True or False?
True (0.6343168649455533)
Ed Puckett has mean: True or False?
True (0.5117165908639297)
Ed Puckett has motive: True or False?
True (0.7233094544266295)
Ed Puckett has opportunity: True or False?
True (0.6783269591477166)
Gene Roberts is guilty: True or False?
True (0.6842640081724978)
Gene Roberts has mean: True or False?
False (0.5418937216067536)
Gene Roberts has motive: True or False?
True (0.6504672161860058)
Gene Roberts has opportunity: True or False?
True (0.555435228101316)
George Whitley is guilty: True or False?
True (0.5583270361921496)
George Whitley has mean: True or False?
False (0.5592900581575188)
George Whitley has motive: True or False?
True (0.5350984235603058)
George Whitley has opportunity: True or False?
False (0.7498207054286419)
Justin Tanner is guilty: True or False?
True (0.5650587803792624)
Justin Tanner has mean: True or False?
True (0.5068355091660127)
Justin Tanner has motive: True or False?
True (0.6011253583932805)
Map:  32%|███▏      | 64/203 [25:38<1:03:27, 27.39s/ examples]Map:  32%|███▏      | 65/203 [26:06<1:03:30, 27.62s/ examples]Map:  33%|███▎      | 66/203 [26:40<1:07:34, 29.60s/ examples]Map:  33%|███▎      | 67/203 [27:06<1:04:10, 28.31s/ examples]Map:  33%|███▎      | 68/203 [27:36<1:05:16, 29.01s/ examples]Justin Tanner has opportunity: True or False?
False (0.5592900581575188)
### Ed Puckett
- mean: True (0.5117165908639297)
- motive: True (0.7233094544266295)
- opportunity: True (0.6783269591477166)

### Gene Roberts
- mean: False (0.5418937216067536)
- motive: False (0.3495327838139942)
- opportunity: False (0.44456477189868404)

### George Whitley
- mean: False (0.5592900581575188)
- motive: False (0.4649015764396942)
- opportunity: False (0.7498207054286419)

### Justin Tanner
- mean: False (0.4931644908339873)
- motive: False (0.3988746416067195)
- opportunity: False (0.5592900581575188)

The culprit is Ed Puckett.
In fact, it is Justin Tanner.
## 5minutemystery-the-candy-store-mystery
Brianna Cates is guilty: True or False?
False (0.5640984675176304)
Brianna Cates has mean: True or False?
True (0.5717666110200305)
Brianna Cates has motive: True or False?
True (0.779321849347754)
Brianna Cates has opportunity: True or False?
True (0.64779823427608)
Emilee Johnson is guilty: True or False?
False (0.6057990946577705)
Emilee Johnson has mean: True or False?
True (0.6095241271158658)
Emilee Johnson has motive: True or False?
True (0.7931059536445917)
Emilee Johnson has opportunity: True or False?
True (0.5822535180679596)
Justin Cates is guilty: True or False?
False (0.5669777909748143)
Justin Cates has mean: True or False?
False (0.5185462156586879)
Justin Cates has motive: True or False?
True (0.8068526417769779)
Justin Cates has opportunity: True or False?
True (0.5107405858633529)
Olivia (Livvie) Johnson is guilty: True or False?
False (0.5370414382302919)
Olivia (Livvie) Johnson has mean: True or False?
False (0.6297746298200823)
Olivia (Livvie) Johnson has motive: True or False?
True (0.7520125537161032)
Olivia (Livvie) Johnson has opportunity: True or False?
True (0.6513548405484016)
Trevor Cates is guilty: True or False?
False (0.5822535180679596)
Trevor Cates has mean: True or False?
True (0.6020616403539744)
Trevor Cates has motive: True or False?
True (0.6504672161860058)
Trevor Cates has opportunity: True or False?
True (0.5107405249783342)
### Brianna Cates
- mean: True (0.5717666110200305)
- motive: True (0.779321849347754)
- opportunity: True (0.64779823427608)

### Emilee Johnson
- mean: False (0.3904758728841342)
- motive: False (0.2068940463554083)
- opportunity: False (0.41774648193204045)

### Justin Cates
- mean: False (0.5185462156586879)
- motive: False (0.1931473582230221)
- opportunity: False (0.4892594141366471)

### Olivia (Livvie) Johnson
- mean: False (0.6297746298200823)
- motive: False (0.2479874462838968)
- opportunity: False (0.34864515945159835)

### Trevor Cates
- mean: False (0.39793835964602564)
- motive: False (0.3495327838139942)
- opportunity: False (0.4892594750216658)

The culprit is Brianna Cates.
In fact, it is Justin Cates.
## 5minutemystery-for-the-birds
Billy Mumms is guilty: True or False?
True (0.9456006304504523)
Billy Mumms has mean: True or False?
True (0.776622945813876)
Billy Mumms has motive: True or False?
True (1.4706562349249974)
Billy Mumms has opportunity: True or False?
True (0.761006053879754)
Cheryl Judson is guilty: True or False?
True (0.862930180750016)
Cheryl Judson has mean: True or False?
True (0.7809967375818414)
Cheryl Judson has motive: True or False?
True (2.272887661768761)
Cheryl Judson has opportunity: True or False?
False (0.43382908131769415)
Stan Mifflin is guilty: True or False?
True (0.9222025890552223)
Stan Mifflin has mean: True or False?
True (0.8003801084788502)
Stan Mifflin has motive: True or False?
True (0.9238675252821831)
Stan Mifflin has opportunity: True or False?
True (0.7969253675907205)
Tor Hansen is guilty: True or False?
True (0.9504569764036419)
Tor Hansen has mean: True or False?
True (0.7721872299079675)
Tor Hansen has motive: True or False?
True (7.849831281233191)
Tor Hansen has opportunity: True or False?
True (0.7819973291046377)
### Billy Mumms
- mean: False (0.22337705418612397)
- motive: False (0.0)
- opportunity: False (0.23899394612024605)

### Cheryl Judson
- mean: False (0.2190032624181586)
- motive: False (0.0)
- opportunity: False (0.43382908131769415)

### Stan Mifflin
- mean: False (0.19961989152114978)
- motive: False (0.07613247471781692)
- opportunity: False (0.20307463240927948)

### Tor Hansen
- mean: True (0.7721872299079675)
- motive: True (7.849831281233191)
- opportunity: True (0.7819973291046377)

The culprit is Tor Hansen.
In fact, it is Cheryl Judson.
## 5minutemystery-the-zoo-job
Cindy is guilty: True or False?
True (0.6662796150778861)
Cindy has mean: True or False?
True (0.7885832152749314)
Cindy has motive: True or False?
True (0.869271276026005)
Cindy has opportunity: True or False?
True (0.6388353131709135)
Henry is guilty: True or False?
True (0.6566582306092376)
Henry has mean: True or False?
True (0.7416740115009234)
Henry has motive: True or False?
True (0.8828325273478573)
Henry has opportunity: True or False?
True (0.5631377056275331)
Leonard is guilty: True or False?
True (0.642432441257838)
Leonard has mean: True or False?
True (0.8582439976623328)
Leonard has motive: True or False?
True (0.8272706865691472)
Leonard has opportunity: True or False?
True (0.5583270361921496)
Tom is guilty: True or False?
False (0.5136684743338078)
Tom has mean: True or False?
True (0.7272012283179254)
Tom has motive: True or False?
True (0.7846493136763113)
Tom has opportunity: True or False?
False (0.5360700410935405)
### Cindy
- mean: True (0.7885832152749314)
- motive: True (0.869271276026005)
- opportunity: True (0.6388353131709135)

### Henry
- mean: False (0.2583259884990766)
- motive: False (0.11716747265214267)
- opportunity: False (0.43686229437246693)

### Leonard
- mean: False (0.14175600233766716)
- motive: False (0.17272931343085285)
- opportunity: False (0.44167296380785037)

### Tom
- mean: False (0.27279877168207456)
- motive: False (0.2153506863236887)
- opportunity: False (0.5360700410935405)

The culprit is Cindy.
In fact, it is Cindy.
## 5minutemystery-did-the-vicar-solve-the-mystery
Elmer Tydings is guilty: True or False?
True (0.9377830065075011)
Elmer Tydings has mean: True or False?
True (0.9425067301242699)
Elmer Tydings has motive: True or False?
True (0.9167080509980843)
Elmer Tydings has opportunity: True or False?
True (0.9511421913058572)
John Stubbs is guilty: True or False?
True (0.8946054590684968)
John Stubbs has mean: True or False?
True (0.897695304229796)
John Stubbs has motive: True or False?
True (0.842085543919308)
John Stubbs has opportunity: True or False?
True (0.8314170225049837)
Katherine Tydings is guilty: True or False?
True (0.8820219652716884)
Katherine Tydings has mean: True or False?
True (0.8086723099497763)
Katherine Tydings has motive: True or False?
True (0.8426043397677332)
Katherine Tydings has opportunity: True or False?
True (0.8710367026584496)
Louise Stubbs is guilty: True or False?
True (0.8822251029233062)
Louise Stubbs has mean: True or False?
True (0.8918110736745599)
Louise Stubbs has motive: True or False?
True (0.8474634858439474)
Louise Stubbs has opportunity: True or False?
True (0.8502200840158227)
### Elmer Tydings
- mean: True (0.9425067301242699)
- motive: True (0.9167080509980843)
- opportunity: True (0.9511421913058572)

### John Stubbs
- mean: False (0.10230469577020396)
- motive: False (0.157914456080692)
- opportunity: False (0.16858297749501627)

### Katherine Tydings
- mean: False (0.19132769005022365)
- motive: False (0.1573956602322668)
- opportunity: False (0.12896329734155043)

### Louise Stubbs
- mean: False (0.10818892632544008)
- motive: False (0.15253651415605263)
- opportunity: False (0.14977991598417728)

The culprit is Elmer Tydings.
In fact, it is Katherine Tydings.
## 5minutemystery-who-scratched-the-porsche
Colonel Greenerbaum is guilty: True or False?
True (0.8267117710471246)
Colonel Greenerbaum has mean: True or False?
True (0.8606036289596553)
Colonel Greenerbaum has motive: True or False?
True (0.8122724274380432)
Colonel Greenerbaum has opportunity: True or False?
True (0.6288633913849659)
Fido is guilty: True or False?
False (0.6294825245063967)
Fido has mean: True or False?
True (0.8984105603938967)
Map:  34%|███▍      | 69/203 [28:10<1:08:06, 30.50s/ examples]Map:  34%|███▍      | 70/203 [28:37<1:05:02, 29.34s/ examples]Map:  35%|███▍      | 71/203 [29:03<1:02:06, 28.23s/ examples]Map:  35%|███▌      | 72/203 [29:33<1:02:52, 28.80s/ examples]Fido has motive: True or False?
False (1.0711799654134986)
Fido has opportunity: True or False?
False (1.2194432145551726)
Malcolm is guilty: True or False?
True (0.6834194581047349)
Malcolm has mean: True or False?
True (0.7634837587244478)
Malcolm has motive: True or False?
True (0.8294920340613177)
Malcolm has opportunity: True or False?
True (0.5195212821349473)
Roxie is guilty: True or False?
True (0.6132366084149281)
Roxie has mean: True or False?
True (0.7527403228571042)
Roxie has motive: True or False?
True (0.8360196960886609)
Roxie has opportunity: True or False?
True (0.5888891269161294)
### Colonel Greenerbaum
- mean: True (0.8606036289596553)
- motive: True (0.8122724274380432)
- opportunity: True (0.6288633913849659)

### Fido
- mean: False (0.10158943960610334)
- motive: False (1.0711799654134986)
- opportunity: False (1.2194432145551726)

### Malcolm
- mean: False (0.23651624127555215)
- motive: False (0.17050796593868234)
- opportunity: False (0.4804787178650527)

### Roxie
- mean: False (0.24725967714289576)
- motive: False (0.1639803039113391)
- opportunity: False (0.4111108730838706)

The culprit is Colonel Greenerbaum.
In fact, it is Colonel Greenerbaum.
## 5minutemystery-the-thief-in-the-night-mystery
Jon Shaw is guilty: True or False?
True (0.8591918406281239)
Jon Shaw has mean: True or False?
True (0.8019357965963964)
Jon Shaw has motive: True or False?
True (0.7972412725773819)
Jon Shaw has opportunity: True or False?
False (0.5987815071974216)
Max Reinke is guilty: True or False?
True (0.8172829725974129)
Max Reinke has mean: True or False?
False (0.7786493288700866)
Max Reinke has motive: True or False?
True (0.7310585348819939)
Max Reinke has opportunity: True or False?
False (0.7102264820691382)
Todd Summers is guilty: True or False?
True (0.8633916342942395)
Todd Summers has mean: True or False?
True (0.7683857617837733)
Todd Summers has motive: True or False?
True (0.8161134110084781)
Todd Summers has opportunity: True or False?
True (0.5631377056275331)
Zac Coulson is guilty: True or False?
True (0.9395815725100197)
Zac Coulson has mean: True or False?
True (0.6415346823638186)
Zac Coulson has motive: True or False?
True (0.8679338050595715)
Zac Coulson has opportunity: True or False?
True (0.6279512069990912)
### Jon Shaw
- mean: False (0.19806420340360364)
- motive: False (0.20275872742261813)
- opportunity: False (0.5987815071974216)

### Max Reinke
- mean: False (0.7786493288700866)
- motive: False (0.2689414651180061)
- opportunity: False (0.7102264820691382)

### Todd Summers
- mean: True (0.7683857617837733)
- motive: True (0.8161134110084781)
- opportunity: True (0.5631377056275331)

### Zac Coulson
- mean: False (0.3584653176361814)
- motive: False (0.13206619494042848)
- opportunity: False (0.37204879300090876)

The culprit is Todd Summers.
In fact, it is Zac Coulson.
## 5minutemystery-ladies-at-table
Alice is guilty: True or False?
True (0.6388352560545881)
Alice has mean: True or False?
True (0.8062431235779619)
Alice has motive: True or False?
True (0.6636689235052821)
Alice has opportunity: True or False?
True (0.6706082735718226)
Frances is guilty: True or False?
False (0.5126925663186335)
Frances has mean: True or False?
True (0.8158201638039532)
Frances has motive: True or False?
True (0.7424217332471881)
Frances has opportunity: True or False?
False (0.5592900581575188)
Leona is guilty: True or False?
True (0.5535053004623279)
Leona has mean: True or False?
True (0.7839884107482739)
Leona has motive: True or False?
True (0.6469064338453809)
Leona has opportunity: True or False?
True (0.525368812147771)
Mary is guilty: True or False?
False (0.6610481693322063)
Mary has mean: True or False?
True (0.7577943897558946)
Mary has motive: True or False?
True (0.5273165696704634)
Mary has opportunity: True or False?
False (0.6306849143569856)
Ruth is guilty: True or False?
True (0.6048657973050737)
Ruth has mean: True or False?
True (0.9041439284393449)
Ruth has motive: True or False?
True (0.8386797935187188)
Ruth has opportunity: True or False?
True (0.8181563669811865)
### Alice
- mean: False (0.1937568764220381)
- motive: False (0.33633107649471794)
- opportunity: False (0.3293917264281774)

### Frances
- mean: False (0.18417983619604683)
- motive: False (0.2575782667528119)
- opportunity: False (0.5592900581575188)

### Leona
- mean: False (0.21601158925172614)
- motive: False (0.35309356615461907)
- opportunity: False (0.474631187852229)

### Mary
- mean: False (0.24220561024410536)
- motive: False (0.47268343032953664)
- opportunity: False (0.6306849143569856)

### Ruth
- mean: True (0.9041439284393449)
- motive: True (0.8386797935187188)
- opportunity: True (0.8181563669811865)

The culprit is Ruth.
In fact, it is Leona.
## 5minutemystery-the-diamond-necklace
Abby Grant is guilty: True or False?
True (0.9246876822649571)
Abby Grant has mean: True or False?
True (0.776622945813876)
Abby Grant has motive: True or False?
True (0.9056565771882901)
Abby Grant has opportunity: True or False?
True (0.904313027820426)
Colonel Barrow is guilty: True or False?
True (0.9425596581002386)
Colonel Barrow has mean: True or False?
True (0.9415467969679381)
Colonel Barrow has motive: True or False?
True (0.9151287648632792)
Colonel Barrow has opportunity: True or False?
True (0.9284088027271398)
Fiona Duncan is guilty: True or False?
True (0.921357630313903)
Fiona Duncan has mean: True or False?
True (0.9187722824991111)
Fiona Duncan has motive: True or False?
True (0.8987665204865408)
Fiona Duncan has opportunity: True or False?
False (0.867271773267888)
Harold Duncan is guilty: True or False?
True (0.9430336353172679)
Harold Duncan has mean: True or False?
True (0.9257686153543061)
Harold Duncan has motive: True or False?
True (0.9170801638253802)
Harold Duncan has opportunity: True or False?
True (0.878314250659373)
Maurice Eades is guilty: True or False?
True (0.8172829725974129)
Maurice Eades has mean: True or False?
True (0.874934615163517)
Maurice Eades has motive: True or False?
True (0.7118317540033398)
Maurice Eades has opportunity: True or False?
True (0.7348812840309261)
### Abby Grant
- mean: False (0.22337705418612397)
- motive: False (0.09434342281170993)
- opportunity: False (0.095686972179574)

### Colonel Barrow
- mean: True (0.9415467969679381)
- motive: True (0.9151287648632792)
- opportunity: True (0.9284088027271398)

### Fiona Duncan
- mean: False (0.08122771750088886)
- motive: False (0.10123347951345918)
- opportunity: False (0.867271773267888)

### Harold Duncan
- mean: False (0.0742313846456939)
- motive: False (0.08291983617461984)
- opportunity: False (0.12168574934062704)

### Maurice Eades
- mean: False (0.125065384836483)
- motive: False (0.28816824599666024)
- opportunity: False (0.2651187159690739)

The culprit is Colonel Barrow.
In fact, it is Fiona Duncan.
## 5minutemystery-rhyming-presidents-mystery
George Bush is guilty: True or False?
True (0.8826303480425456)
George Bush has mean: True or False?
True (0.883437276390578)
George Bush has motive: True or False?
True (0.8787311338092536)
George Bush has opportunity: True or False?
True (0.7627776774954688)
Gerald Ford is guilty: True or False?
True (0.8446654650893471)
Gerald Ford has mean: True or False?
True (0.7962924854830264)
Gerald Ford has motive: True or False?
False (0.8711530453124382)
Gerald Ford has opportunity: True or False?
False (1.0412860786207854)
John Quincy Adams is guilty: True or False?
True (0.8613050536634502)
John Quincy Adams has mean: True or False?
True (0.7490872087035162)
John Quincy Adams has motive: True or False?
True (0.8181564157471076)
John Quincy Adams has opportunity: True or False?
True (0.7494540906858582)
Richard Nixon is guilty: True or False?
True (0.8640812064457842)
Richard Nixon has mean: True or False?
True (0.7813305798204846)
Richard Nixon has motive: True or False?
True (0.8092759828926619)
Richard Nixon has opportunity: True or False?
True (0.6808786440630326)
### George Bush
- mean: True (0.883437276390578)
- motive: True (0.8787311338092536)
- opportunity: True (0.7627776774954688)

### Gerald Ford
- mean: False (0.20370751451697355)
Map:  36%|███▌      | 73/203 [29:59<1:00:43, 28.02s/ examples]Map:  36%|███▋      | 74/203 [30:26<59:30, 27.68s/ examples]  Map:  37%|███▋      | 75/203 [30:54<59:10, 27.74s/ examples]Map:  37%|███▋      | 76/203 [31:21<58:12, 27.50s/ examples]Map:  38%|███▊      | 77/203 [31:54<1:01:23, 29.23s/ examples]- motive: False (0.8711530453124382)
- opportunity: False (1.0412860786207854)

### John Quincy Adams
- mean: False (0.2509127912964838)
- motive: False (0.18184358425289238)
- opportunity: False (0.2505459093141418)

### Richard Nixon
- mean: False (0.2186694201795154)
- motive: False (0.1907240171073381)
- opportunity: False (0.31912135593696744)

The culprit is George Bush.
In fact, it is Gerald Ford.
## 5minutemystery-the-white-house-ghosts
Andrew Jackson is guilty: True or False?
True (0.9823724633578762)
Andrew Jackson has mean: True or False?
True (0.9190632712053527)
Andrew Jackson has motive: True or False?
True (0.9707016952697487)
Andrew Jackson has opportunity: True or False?
True (0.9481545078856665)
Calvin Coolidge is guilty: True or False?
True (0.9716717007848752)
Calvin Coolidge has mean: True or False?
True (0.934872446722342)
Calvin Coolidge has motive: True or False?
True (0.9789554468203624)
Calvin Coolidge has opportunity: True or False?
True (0.9445871723447916)
John Adams is guilty: True or False?
True (0.9672250166644973)
John Adams has mean: True or False?
True (0.9509603994010378)
John Adams has motive: True or False?
True (0.9553191057869168)
John Adams has opportunity: True or False?
True (0.8891444205417208)
William Howard Taft is guilty: True or False?
True (0.9554855815192022)
William Howard Taft has mean: True or False?
True (0.9317114347547434)
William Howard Taft has motive: True or False?
True (0.9496343151593544)
William Howard Taft has opportunity: True or False?
True (0.9183338305905581)
### Andrew Jackson
- mean: False (0.0809367287946473)
- motive: False (0.0292983047302513)
- opportunity: False (0.051845492114333536)

### Calvin Coolidge
- mean: True (0.934872446722342)
- motive: True (0.9789554468203624)
- opportunity: True (0.9445871723447916)

### John Adams
- mean: False (0.049039600598962174)
- motive: False (0.04468089421308319)
- opportunity: False (0.11085557945827917)

### William Howard Taft
- mean: False (0.06828856524525662)
- motive: False (0.05036568484064563)
- opportunity: False (0.08166616940944194)

The culprit is Calvin Coolidge.
In fact, it is Calvin Coolidge.
## 5minutemystery-mr-patrick-and-the-graveyard-mystery
Grave no.1 is guilty: True or False?
True (0.9686788908454032)
Grave no.1 has mean: True or False?
True (0.9753900767342161)
Grave no.1 has motive: True or False?
True (0.9425066704353817)
Grave no.1 has opportunity: True or False?
True (0.9572778330298248)
Grave no.2 is guilty: True or False?
True (0.9529258022651363)
Grave no.2 has mean: True or False?
True (0.9680204387474981)
Grave no.2 has motive: True or False?
True (0.9246876822649571)
Grave no.2 has opportunity: True or False?
True (0.9394706502722077)
Grave no.3 is guilty: True or False?
True (0.9479621664653681)
Grave no.3 has mean: True or False?
True (0.9752018447706344)
Grave no.3 has motive: True or False?
True (0.9469902528343473)
Grave no.3 has opportunity: True or False?
True (0.948346255948953)
Grave no.4 is guilty: True or False?
True (0.9594593035226332)
Grave no.4 has mean: True or False?
True (0.9755769367349482)
Grave no.4 has motive: True or False?
True (0.9190632712053527)
Grave no.4 has opportunity: True or False?
True (0.9433475737015985)
Grave no.5 is guilty: True or False?
True (0.9729338284788606)
Grave no.5 has mean: True or False?
True (0.9773707989989006)
Grave no.5 has motive: True or False?
True (0.8887587777822111)
Grave no.5 has opportunity: True or False?
True (0.9139841191734227)
### Grave no.1
- mean: True (0.9753900767342161)
- motive: True (0.9425066704353817)
- opportunity: True (0.9572778330298248)

### Grave no.2
- mean: False (0.0319795612525019)
- motive: False (0.07531231773504288)
- opportunity: False (0.060529349727792336)

### Grave no.3
- mean: False (0.02479815522936557)
- motive: False (0.053009747165652654)
- opportunity: False (0.051653744051046946)

### Grave no.4
- mean: False (0.024423063265051836)
- motive: False (0.0809367287946473)
- opportunity: False (0.056652426298401504)

### Grave no.5
- mean: False (0.02262920100109944)
- motive: False (0.11124122221778887)
- opportunity: False (0.0860158808265773)

The culprit is Grave no.1.
In fact, it is Grave no.4.
## 5minutemystery-lockbox-100
Edward Frates is guilty: True or False?
True (0.7106282704218558)
Edward Frates has mean: True or False?
True (0.7994423454932595)
Edward Frates has motive: True or False?
True (0.6808786440630326)
Edward Frates has opportunity: True or False?
True (0.6934729802503211)
James Madigan is guilty: True or False?
True (0.740174341079517)
James Madigan has mean: True or False?
True (0.7512834059294674)
James Madigan has motive: True or False?
True (0.5992506595844092)
James Madigan has opportunity: True or False?
True (0.644225125126315)
Peter Zielny is guilty: True or False?
True (0.7193836000532381)
Peter Zielny has mean: True or False?
True (0.7371581892031299)
Peter Zielny has motive: True or False?
True (0.743912876509037)
Peter Zielny has opportunity: True or False?
True (0.5992506595844092)
Ronald Finch is guilty: True or False?
True (0.8175745039697023)
Ronald Finch has mean: True or False?
True (0.9039745373919651)
Ronald Finch has motive: True or False?
True (0.8134607635851566)
Ronald Finch has opportunity: True or False?
True (0.7937462383814009)
Russell Winwood is guilty: True or False?
True (0.8944211616820568)
Russell Winwood has mean: True or False?
True (0.9537942396657707)
Russell Winwood has motive: True or False?
True (0.9227612629515897)
Russell Winwood has opportunity: True or False?
True (0.9329437018480795)
### Edward Frates
- mean: False (0.20055765450674046)
- motive: False (0.31912135593696744)
- opportunity: False (0.3065270197496789)

### James Madigan
- mean: False (0.2487165940705326)
- motive: False (0.40074934041559085)
- opportunity: False (0.355774874873685)

### Peter Zielny
- mean: False (0.2628418107968701)
- motive: False (0.25608712349096296)
- opportunity: False (0.40074934041559085)

### Ronald Finch
- mean: False (0.0960254626080349)
- motive: False (0.18653923641484338)
- opportunity: False (0.2062537616185991)

### Russell Winwood
- mean: True (0.9537942396657707)
- motive: True (0.9227612629515897)
- opportunity: True (0.9329437018480795)

The culprit is Russell Winwood.
In fact, it is Russell Winwood.
## 5minutemystery-mystery-at-the-detectives-office
Joe the janitor is guilty: True or False?
True (0.9007918816809537)
Joe the janitor has mean: True or False?
True (0.8665848330592597)
Joe the janitor has motive: True or False?
True (0.9352283459368647)
Joe the janitor has opportunity: True or False?
True (0.9585765591512942)
Larry is guilty: True or False?
True (0.8198933606225757)
Larry has mean: True or False?
True (0.7570766705324253)
Larry has motive: True or False?
True (0.8187367896794966)
Larry has opportunity: True or False?
True (0.580352087772514)
Mr. Jorgensen is guilty: True or False?
True (0.811974341286875)
Mr. Jorgensen has mean: True or False?
True (0.7956581141325956)
Mr. Jorgensen has motive: True or False?
True (0.8169912043042492)
Mr. Jorgensen has opportunity: True or False?
True (0.612309626324874)
the building manager is guilty: True or False?
True (0.8778961263000082)
the building manager has mean: True or False?
True (0.6566582306092376)
the building manager has motive: True or False?
True (0.7882573622725895)
the building manager has opportunity: True or False?
True (0.6951311179371613)
### Joe the janitor
- mean: True (0.8665848330592597)
- motive: True (0.9352283459368647)
- opportunity: True (0.9585765591512942)

### Larry
- mean: False (0.24292332946757467)
- motive: False (0.1812632103205034)
- opportunity: False (0.419647912227486)

### Mr. Jorgensen
- mean: False (0.20434188586740443)
- motive: False (0.1830087956957508)
- opportunity: False (0.38769037367512604)

### the building manager
- mean: False (0.34334176939076244)
- motive: False (0.21174263772741053)
- opportunity: False (0.3048688820628387)

The culprit is Joe the janitor.
In fact, it is the building manager.
## 5minutemystery-the-secret-in-the-old-trunk
Dennis Boyles is guilty: True or False?
True (0.7711548682745724)
Map:  38%|███▊      | 78/203 [32:26<1:02:36, 30.05s/ examples]Map:  39%|███▉      | 79/203 [33:00<1:04:52, 31.39s/ examples]Map:  39%|███▉      | 80/203 [33:23<59:12, 28.88s/ examples]  Dennis Boyles has mean: True or False?
True (0.8875948773562923)
Dennis Boyles has motive: True or False?
True (0.6575384105121485)
Dennis Boyles has opportunity: True or False?
False (0.6791786560103119)
George Boyles is guilty: True or False?
True (0.7947037743192802)
George Boyles has mean: True or False?
True (0.8283842201397164)
George Boyles has motive: True or False?
True (0.7310586002437232)
George Boyles has opportunity: True or False?
False (0.7217432334405754)
John Boyles is guilty: True or False?
True (0.8303191093049147)
John Boyles has mean: True or False?
True (0.8354835531737983)
John Boyles has motive: True or False?
True (0.7512834059294674)
John Boyles has opportunity: True or False?
False (0.6774740084332073)
Patricia (Trish) Boyles Sykes is guilty: True or False?
True (0.7745833916423246)
Patricia (Trish) Boyles Sykes has mean: True or False?
True (0.8596637847360897)
Patricia (Trish) Boyles Sykes has motive: True or False?
True (0.673191669892235)
Patricia (Trish) Boyles Sykes has opportunity: True or False?
True (0.5755880655791468)
Patrick Boyles is guilty: True or False?
True (0.7086160238002551)
Patrick Boyles has mean: True or False?
True (0.7786493288700866)
Patrick Boyles has motive: True or False?
True (0.5755879969637064)
Patrick Boyles has opportunity: True or False?
False (0.7704647687904915)
### Dennis Boyles
- mean: False (0.11240512264370772)
- motive: False (0.34246158948785155)
- opportunity: False (0.6791786560103119)

### George Boyles
- mean: False (0.17161577986028365)
- motive: False (0.26894139975627684)
- opportunity: False (0.7217432334405754)

### John Boyles
- mean: False (0.1645164468262017)
- motive: False (0.2487165940705326)
- opportunity: False (0.6774740084332073)

### Patricia (Trish) Boyles Sykes
- mean: True (0.8596637847360897)
- motive: True (0.673191669892235)
- opportunity: True (0.5755880655791468)

### Patrick Boyles
- mean: False (0.22135067112991336)
- motive: False (0.42441200303629356)
- opportunity: False (0.7704647687904915)

The culprit is Patricia (Trish) Boyles Sykes.
In fact, it is Patrick Boyles.
## 5minutemystery-the-restless-ghost
Casey McCormick is guilty: True or False?
True (0.9210741501882456)
Casey McCormick has mean: True or False?
True (0.7154240000492645)
Casey McCormick has motive: True or False?
True (0.8376200175313318)
Casey McCormick has opportunity: True or False?
False (0.6279512069990912)
Connie McCormick is guilty: True or False?
True (0.815232454829111)
Connie McCormick has mean: True or False?
True (0.814643384779728)
Connie McCormick has motive: True or False?
True (0.847967740521315)
Connie McCormick has opportunity: True or False?
False (0.6984322578436808)
Ellen McCormick is guilty: True or False?
True (0.7287482572006113)
Ellen McCormick has mean: True or False?
True (0.6671476389322356)
Ellen McCormick has motive: True or False?
True (0.6984323202883935)
Ellen McCormick has opportunity: True or False?
False (0.7520125537161032)
Michael McCormick, Jr. is guilty: True or False?
True (0.9078038309924442)
Michael McCormick, Jr. has mean: True or False?
True (0.9388007508488514)
Michael McCormick, Jr. has motive: True or False?
True (0.9430336353172679)
Michael McCormick, Jr. has opportunity: True or False?
True (0.7138307093362539)
The ghost of Mike McCormick, Sr. is guilty: True or False?
True (0.8587185689177256)
The ghost of Mike McCormick, Sr. has mean: True or False?
True (0.8534248451958423)
The ghost of Mike McCormick, Sr. has motive: True or False?
True (0.8638516611889259)
The ghost of Mike McCormick, Sr. has opportunity: True or False?
True (0.6934729802503211)
### Casey McCormick
- mean: False (0.28457599995073546)
- motive: False (0.16237998246866825)
- opportunity: False (0.6279512069990912)

### Connie McCormick
- mean: False (0.18535661522027203)
- motive: False (0.15203225947868504)
- opportunity: False (0.6984322578436808)

### Ellen McCormick
- mean: False (0.3328523610677644)
- motive: False (0.3015676797116065)
- opportunity: False (0.7520125537161032)

### Michael McCormick, Jr.
- mean: True (0.9388007508488514)
- motive: True (0.9430336353172679)
- opportunity: True (0.7138307093362539)

### The ghost of Mike McCormick, Sr.
- mean: False (0.14657515480415773)
- motive: False (0.13614833881107413)
- opportunity: False (0.3065270197496789)

The culprit is Michael McCormick, Jr..
In fact, it is Casey McCormick.
## 5minutemystery-the-secret-friend
Bill Baker is guilty: True or False?
True (0.8152325155686644)
Bill Baker has mean: True or False?
True (0.9640516654033661)
Bill Baker has motive: True or False?
True (0.8169911556077801)
Bill Baker has opportunity: True or False?
True (0.7461389980806673)
Harold Coker is guilty: True or False?
True (0.9152045868398637)
Harold Coker has mean: True or False?
True (0.9362850185952675)
Harold Coker has motive: True or False?
True (0.9121235591541035)
Harold Coker has opportunity: True or False?
True (0.9213575753967104)
Lyn Baker is guilty: True or False?
True (0.8238958672039278)
Lyn Baker has mean: True or False?
True (0.9509603994010378)
Lyn Baker has motive: True or False?
True (0.9322068701708559)
Lyn Baker has opportunity: True or False?
True (0.8423451152856819)
Midge Coker is guilty: True or False?
True (0.8875949368741688)
Midge Coker has mean: True or False?
True (0.952397347230678)
Midge Coker has motive: True or False?
True (0.8568122940392877)
Midge Coker has opportunity: True or False?
True (0.8044059309478723)
### Bill Baker
- mean: False (0.035948334596633935)
- motive: False (0.18300884439221987)
- opportunity: False (0.2538610019193327)

### Harold Coker
- mean: True (0.9362850185952675)
- motive: True (0.9121235591541035)
- opportunity: True (0.9213575753967104)

### Lyn Baker
- mean: False (0.049039600598962174)
- motive: False (0.0677931298291441)
- opportunity: False (0.1576548847143181)

### Midge Coker
- mean: False (0.04760265276932196)
- motive: False (0.14318770596071229)
- opportunity: False (0.19559406905212773)

The culprit is Harold Coker.
In fact, it is Midge Coker.
## 5minutemystery-the-cross-homestead-mystery
Journal entry of Edith is guilty: True or False?
True (0.5973730125048408)
Journal entry of Edith has mean: True or False?
True (0.7563575572780217)
Journal entry of Edith has motive: True or False?
True (0.5679366075542497)
Journal entry of Edith has opportunity: True or False?
True (0.5448014304301324)
Journal entry of Leonard is guilty: True or False?
False (0.6531269509188588)
Journal entry of Leonard has mean: True or False?
True (0.8068526417769779)
Journal entry of Leonard has motive: True or False?
True (0.5869964306477841)
Journal entry of Leonard has opportunity: True or False?
True (0.5917232019857303)
Journal entry of Susie is guilty: True or False?
False (0.6842640081724978)
Journal entry of Susie has mean: True or False?
True (0.7732163648437078)
Journal entry of Susie has motive: True or False?
True (0.5964331079469681)
Journal entry of Susie has opportunity: True or False?
True (0.5438325284393795)
Journal entry of Victor is guilty: True or False?
False (0.5263427467960875)
Journal entry of Victor has mean: True or False?
True (0.8514594452543962)
Journal entry of Victor has motive: True or False?
True (0.7025300310583819)
Journal entry of Victor has opportunity: True or False?
True (0.6876299924560524)
Journal entry of Wilbur is guilty: True or False?
False (0.5841525779336078)
Journal entry of Wilbur has mean: True or False?
True (0.7655933544531522)
Journal entry of Wilbur has motive: True or False?
True (0.5312093625105829)
Journal entry of Wilbur has opportunity: True or False?
True (0.5341265295318852)
### Journal entry of Edith
- mean: False (0.24364244272197833)
- motive: False (0.4320633924457503)
- opportunity: False (0.4551985695698676)

### Journal entry of Leonard
- mean: False (0.1931473582230221)
- motive: False (0.41300356935221594)
- opportunity: False (0.40827679801426975)

### Journal entry of Susie
- mean: False (0.22678363515629218)
- motive: False (0.40356689205303187)
- opportunity: False (0.45616747156062054)

### Journal entry of Victor
- mean: True (0.8514594452543962)
Map:  40%|███▉      | 81/203 [33:57<1:01:42, 30.35s/ examples]Map:  40%|████      | 82/203 [34:22<57:34, 28.55s/ examples]  Map:  41%|████      | 83/203 [34:53<58:43, 29.37s/ examples]Map:  41%|████▏     | 84/203 [35:15<53:41, 27.07s/ examples]Map:  42%|████▏     | 85/203 [35:42<53:28, 27.19s/ examples]- motive: True (0.7025300310583819)
- opportunity: True (0.6876299924560524)

### Journal entry of Wilbur
- mean: False (0.23440664554684776)
- motive: False (0.4687906374894171)
- opportunity: False (0.4658734704681148)

The culprit is Journal entry of Victor.
In fact, it is Journal entry of Leonard.
## 5minutemystery-is-it-a-wonderful-life
Dr. Gilchrest is guilty: True or False?
True (0.9122799654606127)
Dr. Gilchrest has mean: True or False?
True (0.9181873182746905)
Dr. Gilchrest has motive: True or False?
True (0.884439109617765)
Dr. Gilchrest has opportunity: True or False?
True (0.8820219652716884)
Jonathan Cartright is guilty: True or False?
True (0.9147487268823872)
Jonathan Cartright has mean: True or False?
True (0.8980534699860239)
Jonathan Cartright has motive: True or False?
True (0.8931230927421242)
Jonathan Cartright has opportunity: True or False?
True (0.8314170225049837)
Miser James Cartright (suicide) is guilty: True or False?
True (0.8482193926289605)
Miser James Cartright (suicide) has mean: True or False?
True (0.81197440178368)
Miser James Cartright (suicide) has motive: True or False?
True (0.869271276026005)
Miser James Cartright (suicide) has opportunity: True or False?
True (0.8250265073476026)
Moira Laurie is guilty: True or False?
True (0.9121235591541035)
Moira Laurie has mean: True or False?
True (0.8701565822173906)
Moira Laurie has motive: True or False?
True (0.8719117627136385)
Moira Laurie has opportunity: True or False?
True (0.8877896676652527)
### Dr. Gilchrest
- mean: True (0.9181873182746905)
- motive: True (0.884439109617765)
- opportunity: True (0.8820219652716884)

### Jonathan Cartright
- mean: False (0.10194653001397613)
- motive: False (0.1068769072578758)
- opportunity: False (0.16858297749501627)

### Miser James Cartright (suicide)
- mean: False (0.18802559821632003)
- motive: False (0.13072872397399504)
- opportunity: False (0.17497349265239737)

### Moira Laurie
- mean: False (0.12984341778260944)
- motive: False (0.12808823728636154)
- opportunity: False (0.11221033233474731)

The culprit is Dr. Gilchrest.
In fact, it is Moira Laurie.
## 5minutemystery-lestrade-solves-a-case
Archibald Hopkins is guilty: True or False?
True (0.8652240590801695)
Archibald Hopkins has mean: True or False?
True (0.9066531685310133)
Archibald Hopkins has motive: True or False?
True (0.8914335992201801)
Archibald Hopkins has opportunity: True or False?
True (0.8261514850267767)
Countess Mannerley is guilty: True or False?
True (0.7937461674149602)
Countess Mannerley has mean: True or False?
True (0.8987665204865408)
Countess Mannerley has motive: True or False?
True (0.7431679939957333)
Countess Mannerley has opportunity: True or False?
True (0.6504672161860058)
Loralie Courtney is guilty: True or False?
True (0.8086723099497763)
Loralie Courtney has mean: True or False?
True (0.9124361266596831)
Loralie Courtney has motive: True or False?
True (0.767689835247798)
Loralie Courtney has opportunity: True or False?
True (0.7704647687904915)
Robert Bannington is guilty: True or False?
True (0.8665847814067802)
Robert Bannington has mean: True or False?
True (0.9136765013387816)
Robert Bannington has motive: True or False?
True (0.8755743533923891)
Robert Bannington has opportunity: True or False?
True (0.8727816933272936)
### Archibald Hopkins
- mean: False (0.0933468314689867)
- motive: False (0.10856640077981994)
- opportunity: False (0.1738485149732233)

### Countess Mannerley
- mean: False (0.10123347951345918)
- motive: False (0.2568320060042667)
- opportunity: False (0.3495327838139942)

### Loralie Courtney
- mean: False (0.0875638733403169)
- motive: False (0.232310164752202)
- opportunity: False (0.22953523120950847)

### Robert Bannington
- mean: True (0.9136765013387816)
- motive: True (0.8755743533923891)
- opportunity: True (0.8727816933272936)

The culprit is Robert Bannington.
In fact, it is Robert Bannington.
## 5minutemystery-whole-stole-the-new-years-kiss
Danny is guilty: True or False?
True (0.7826625131049049)
Danny has mean: True or False?
True (0.8951566249612815)
Danny has motive: True or False?
True (0.9690910565174785)
Danny has opportunity: True or False?
True (0.8803863464576128)
Jeremy is guilty: True or False?
True (0.5321819753403337)
Jeremy has mean: True or False?
True (0.8856315007226893)
Jeremy has motive: True or False?
True (0.9599877610290866)
Jeremy has opportunity: True or False?
True (0.7648916137833577)
RJ is guilty: True or False?
True (0.8992984268798617)
RJ has mean: True or False?
True (0.8955226517597132)
RJ has motive: True or False?
True (0.9689150454184371)
RJ has opportunity: True or False?
True (0.9010534302227574)
Reese is guilty: True or False?
True (0.8104789202520752)
Reese has mean: True or False?
True (0.7981867775042927)
Reese has motive: True or False?
True (0.9793540239608529)
Reese has opportunity: True or False?
True (0.8745065279415651)
### Danny
- mean: False (0.10484337503871854)
- motive: False (0.03090894348252149)
- opportunity: False (0.11961365354238718)

### Jeremy
- mean: False (0.11436849927731074)
- motive: False (0.04001223897091344)
- opportunity: False (0.23510838621664232)

### RJ
- mean: True (0.8955226517597132)
- motive: True (0.9689150454184371)
- opportunity: True (0.9010534302227574)

### Reese
- mean: False (0.20181322249570732)
- motive: False (0.020645976039147085)
- opportunity: False (0.12549347205843486)

The culprit is RJ.
In fact, it is RJ.
## 5minutemystery-the-new-years-eve-mystery
Juanita Wade is guilty: True or False?
True (0.8670357473609658)
Juanita Wade has mean: True or False?
True (0.941654207327861)
Juanita Wade has motive: True or False?
True (0.9241418261705818)
Juanita Wade has opportunity: True or False?
True (0.9431384818142104)
Mary Beth Sloan is guilty: True or False?
True (0.779321849347754)
Mary Beth Sloan has mean: True or False?
True (0.9577544910931239)
Mary Beth Sloan has motive: True or False?
True (0.9076402191395381)
Mary Beth Sloan has opportunity: True or False?
True (0.8762113474663927)
Noel King is guilty: True or False?
True (0.8812066389307215)
Noel King has mean: True or False?
True (0.9566342225308191)
Noel King has motive: True or False?
True (0.9281487460975983)
Noel King has opportunity: True or False?
True (0.9396923783210908)
Roy Wade is guilty: True or False?
True (0.8844391689240307)
Roy Wade has mean: True or False?
True (0.9383503780077049)
Roy Wade has motive: True or False?
True (0.883638264557296)
Roy Wade has opportunity: True or False?
True (0.927887794449634)
Theresa King is guilty: True or False?
True (0.9302050495103452)
Theresa King has mean: True or False?
True (0.9322068076615162)
Theresa King has motive: True or False?
True (0.9396923783210908)
Theresa King has opportunity: True or False?
True (0.9399133323582882)
### Juanita Wade
- mean: False (0.05834579267213902)
- motive: False (0.07585817382941817)
- opportunity: False (0.05686151818578955)

### Mary Beth Sloan
- mean: False (0.04224550890687606)
- motive: False (0.09235978086046193)
- opportunity: False (0.12378865253360727)

### Noel King
- mean: True (0.9566342225308191)
- motive: True (0.9281487460975983)
- opportunity: True (0.9396923783210908)

### Roy Wade
- mean: False (0.06164962199229507)
- motive: False (0.116361735442704)
- opportunity: False (0.07211220555036602)

### Theresa King
- mean: False (0.0677931923384838)
- motive: False (0.06030762167890924)
- opportunity: False (0.06008666764171178)

The culprit is Noel King.
In fact, it is Mary Beth Sloan.
## 5minutemystery-the-twelfth-night-mystery
Balthasar is guilty: True or False?
True (0.8701565303520181)
Balthasar has mean: True or False?
True (0.9605096001181298)
Balthasar has motive: True or False?
True (0.9207183689158278)
Balthasar has opportunity: True or False?
True (0.8388118129178417)
Caspar is guilty: True or False?
True (0.794384956668203)
Caspar has mean: True or False?
True (0.911809984585868)
Caspar has motive: True or False?
True (0.9368651509033574)
Caspar has opportunity: True or False?
True (0.9217811254507657)
Dad is guilty: True or False?
True (0.9703525306286271)
Dad has mean: True or False?
True (0.9460510011104621)
Map:  42%|████▏     | 86/203 [36:05<50:47, 26.04s/ examples]Map:  43%|████▎     | 87/203 [36:37<53:18, 27.57s/ examples]Map:  43%|████▎     | 88/203 [37:12<57:15, 29.88s/ examples]Map:  44%|████▍     | 89/203 [37:51<1:02:09, 32.72s/ examples]Dad has motive: True or False?
True (0.9678081855801772)
Dad has opportunity: True or False?
True (0.9606574760904091)
Melchoir is guilty: True or False?
True (0.9017477662022706)
Melchoir has mean: True or False?
True (0.9324532728823121)
Melchoir has motive: True or False?
True (0.9588086006815989)
Melchoir has opportunity: True or False?
True (0.9408984174410038)
### Balthasar
- mean: False (0.0394903998818702)
- motive: False (0.07928163108417219)
- opportunity: False (0.16118818708215832)

### Caspar
- mean: False (0.08819001541413196)
- motive: False (0.06313484909664258)
- opportunity: False (0.07821887454923426)

### Dad
- mean: True (0.9460510011104621)
- motive: True (0.9678081855801772)
- opportunity: True (0.9606574760904091)

### Melchoir
- mean: False (0.06754672711768794)
- motive: False (0.0411913993184011)
- opportunity: False (0.059101582558996224)

The culprit is Dad.
In fact, it is Caspar.
## 5minutemystery-sugar-lands-candy-crook
King Ted is guilty: True or False?
True (1.894016958997008)
King Ted has mean: True or False?
True (1.405571817019633)
King Ted has motive: True or False?
True (1.6973194813725263)
King Ted has opportunity: True or False?
True (0.9054425934549756)
Lancelot is guilty: True or False?
True (0.9167826786944403)
Lancelot has mean: True or False?
True (0.9139841191734227)
Lancelot has motive: True or False?
True (0.8594279851904003)
Lancelot has opportunity: True or False?
True (0.8893367679552574)
Pride is guilty: True or False?
True (1.0596613849072436)
Pride has mean: True or False?
True (1.2278680406317655)
Pride has motive: True or False?
True (1.2808118266097692)
Pride has opportunity: True or False?
True (0.9274290236011148)
Rupert is guilty: True or False?
True (0.9307735574385115)
Rupert has mean: True or False?
True (2.8285572852899734)
Rupert has motive: True or False?
True (0.9203612781944561)
Rupert has opportunity: True or False?
True (0.8399966422759665)
### King Ted
- mean: True (1.405571817019633)
- motive: True (1.6973194813725263)
- opportunity: True (0.9054425934549756)

### Lancelot
- mean: False (0.0860158808265773)
- motive: False (0.1405720148095997)
- opportunity: False (0.1106632320447426)

### Pride
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.07257097639888521)

### Rupert
- mean: False (0.0)
- motive: False (0.07963872180554388)
- opportunity: False (0.1600033577240335)

The culprit is King Ted.
In fact, it is King Ted.
## 5minutemystery-what-the-dickensa-christmas-eve-mystery
Fagin is guilty: True or False?
False (2.979449943812823)
Fagin has mean: True or False?
True (0.9121236203167563)
Fagin has motive: True or False?
True (0.8563323578093363)
Fagin has opportunity: True or False?
True (0.7898827135821628)
Nancy is guilty: True or False?
True (0.642432441257838)
Nancy has mean: True or False?
True (0.6279512069990912)
Nancy has motive: True or False?
True (0.8333246107254184)
Nancy has opportunity: True or False?
True (0.7606506998655483)
Oliver Twist is guilty: True or False?
True (0.5926665645259142)
Oliver Twist has mean: True or False?
True (0.7634837587244478)
Oliver Twist has motive: True or False?
True (0.8169911556077801)
Oliver Twist has opportunity: True or False?
True (0.5370413742099674)
The Artful Dodger is guilty: True or False?
True (0.5563995964631269)
The Artful Dodger has mean: True or False?
True (0.6934729802503211)
The Artful Dodger has motive: True or False?
True (0.6757646168022439)
The Artful Dodger has opportunity: True or False?
True (0.5409238971378262)
The Rich Gentleman is guilty: True or False?
True (0.7138307731576955)
The Rich Gentleman has mean: True or False?
True (0.8484706263347676)
The Rich Gentleman has motive: True or False?
True (0.8459424357871997)
The Rich Gentleman has opportunity: True or False?
True (0.6343168082332088)
### Fagin
- mean: True (0.9121236203167563)
- motive: True (0.8563323578093363)
- opportunity: True (0.7898827135821628)

### Nancy
- mean: False (0.37204879300090876)
- motive: False (0.1666753892745816)
- opportunity: False (0.23934930013445166)

### Oliver Twist
- mean: False (0.23651624127555215)
- motive: False (0.18300884439221987)
- opportunity: False (0.46295862579003255)

### The Artful Dodger
- mean: False (0.3065270197496789)
- motive: False (0.32423538319775613)
- opportunity: False (0.4590761028621738)

### The Rich Gentleman
- mean: False (0.15152937366523245)
- motive: False (0.15405756421280026)
- opportunity: False (0.3656831917667912)

The culprit is Fagin.
In fact, it is The Rich Gentleman.
## 5minutemystery-the-secret-santa-mystery
Al Busby is guilty: True or False?
True (0.8534248451958423)
Al Busby has mean: True or False?
True (0.7745833916423246)
Al Busby has motive: True or False?
True (0.7394224480813394)
Al Busby has opportunity: True or False?
False (0.6397360437814448)
Bob (Bobby) Key is guilty: True or False?
True (0.893681109060862)
Bob (Bobby) Key has mean: True or False?
True (0.6315943123389512)
Bob (Bobby) Key has motive: True or False?
True (0.7453983509653428)
Bob (Bobby) Key has opportunity: True or False?
True (0.7106282704218558)
Chuck Daughtry is guilty: True or False?
True (0.8558511727823209)
Chuck Daughtry has mean: True or False?
True (0.8080671968507699)
Chuck Daughtry has motive: True or False?
True (0.7585105966624085)
Chuck Daughtry has opportunity: True or False?
True (0.5573634465789677)
Jeff Reynolds is guilty: True or False?
True (0.878314250659373)
Jeff Reynolds has mean: True or False?
True (0.7272012283179254)
Jeff Reynolds has motive: True or False?
True (0.7853085386591824)
Jeff Reynolds has opportunity: True or False?
True (0.5832033700118571)
Jim Dockery is guilty: True or False?
True (0.8499711693725173)
Jim Dockery has mean: True or False?
True (0.5888891269161294)
Jim Dockery has motive: True or False?
True (0.6297745735138451)
Jim Dockery has opportunity: True or False?
False (0.644225125126315)
### Al Busby
- mean: False (0.2254166083576754)
- motive: False (0.2605775519186606)
- opportunity: False (0.6397360437814448)

### Bob (Bobby) Key
- mean: False (0.36840568766104875)
- motive: False (0.2546016490346572)
- opportunity: False (0.28937172957814417)

### Chuck Daughtry
- mean: True (0.8080671968507699)
- motive: True (0.7585105966624085)
- opportunity: True (0.5573634465789677)

### Jeff Reynolds
- mean: False (0.27279877168207456)
- motive: False (0.21469146134081762)
- opportunity: False (0.41679662998814293)

### Jim Dockery
- mean: False (0.4111108730838706)
- motive: False (0.37022542648615486)
- opportunity: False (0.644225125126315)

The culprit is Chuck Daughtry.
In fact, it is Jim Dockery.
## 5minutemystery-the-silly-santa-mystery
Mr. Corrigan is guilty: True or False?
True (0.8441522053247883)
Mr. Corrigan has mean: True or False?
True (0.7337380571259766)
Mr. Corrigan has motive: True or False?
False (0.4462024450672553)
Mr. Corrigan has opportunity: True or False?
True (0.7074046739492601)
Mrs. Martin is guilty: True or False?
True (0.9170058398600052)
Mrs. Martin has mean: True or False?
True (0.8322367037050584)
Mrs. Martin has motive: True or False?
True (0.84619676525883)
Mrs. Martin has opportunity: True or False?
True (0.8528129435683355)
Santa Claus is guilty: True or False?
True (0.8775817123105901)
Santa Claus has mean: True or False?
True (0.5258557890702972)
Santa Claus has motive: True or False?
True (0.779321849347754)
Santa Claus has opportunity: True or False?
True (0.7588681623522538)
The photographer is guilty: True or False?
True (0.6951311179371613)
The photographer has mean: True or False?
True (0.6757645563841816)
The photographer has motive: True or False?
True (0.7501869182201083)
The photographer has opportunity: True or False?
True (1.0680877473509556)
### Mr. Corrigan
- mean: False (0.2662619428740234)
- motive: False (0.4462024450672553)
- opportunity: False (0.2925953260507399)

### Mrs. Martin
- mean: True (0.8322367037050584)
- motive: True (0.84619676525883)
- opportunity: True (0.8528129435683355)

### Santa Claus
- mean: False (0.4741442109297028)
- motive: False (0.22067815065224605)
- opportunity: False (0.24113183764774615)

### The photographer
Map:  44%|████▍     | 90/203 [38:29<1:04:45, 34.39s/ examples]Map:  45%|████▍     | 91/203 [38:58<1:00:48, 32.58s/ examples]Map:  45%|████▌     | 92/203 [39:24<56:44, 30.67s/ examples]  Map:  46%|████▌     | 93/203 [39:50<53:38, 29.26s/ examples]Map:  46%|████▋     | 94/203 [40:19<52:51, 29.09s/ examples]- mean: False (0.32423544361581835)
- motive: False (0.2498130817798917)
- opportunity: False (0.0)

The culprit is Mrs. Martin.
In fact, it is The photographer.
## 5minutemystery-sky-jack
Clem Duster is guilty: True or False?
True (0.8354835531737983)
Clem Duster has mean: True or False?
True (0.8044059309478723)
Clem Duster has motive: True or False?
True (0.8294919722593475)
Clem Duster has opportunity: True or False?
True (0.725648573585541)
Cliff Snelling is guilty: True or False?
True (0.8311430212356835)
Cliff Snelling has mean: True or False?
True (0.8338664756137771)
Cliff Snelling has motive: True or False?
True (0.8665847814067802)
Cliff Snelling has opportunity: True or False?
True (0.7620701143808404)
David Loftkiss is guilty: True or False?
True (0.811078188867804)
David Loftkiss has mean: True or False?
True (0.8360197583769845)
David Loftkiss has motive: True or False?
True (0.8946054590684968)
David Loftkiss has opportunity: True or False?
True (0.7008947664177184)
Tom Jenks is guilty: True or False?
True (0.8181563669811865)
Tom Jenks has mean: True or False?
True (0.811078188867804)
Tom Jenks has motive: True or False?
True (0.8181563669811865)
Tom Jenks has opportunity: True or False?
True (0.644225125126315)
### Clem Duster
- mean: False (0.19559406905212773)
- motive: False (0.17050802774065255)
- opportunity: False (0.274351426414459)

### Cliff Snelling
- mean: True (0.8338664756137771)
- motive: True (0.8665847814067802)
- opportunity: True (0.7620701143808404)

### David Loftkiss
- mean: False (0.1639802416230155)
- motive: False (0.10539454093150324)
- opportunity: False (0.2991052335822816)

### Tom Jenks
- mean: False (0.18892181113219597)
- motive: False (0.18184363301881346)
- opportunity: False (0.355774874873685)

The culprit is Cliff Snelling.
In fact, it is Tom Jenks.
## 5minutemystery-dr-watson-and-the-thwarted-engagement
Georgette Pelham is guilty: True or False?
True (0.7527403228571042)
Georgette Pelham has mean: True or False?
True (0.5851012033999957)
Georgette Pelham has motive: True or False?
False (0.6039318499573872)
Georgette Pelham has opportunity: True or False?
False (0.6934729182490079)
Reverend Marvin Ingalls is guilty: True or False?
True (0.8006919661398397)
Reverend Marvin Ingalls has mean: True or False?
True (0.8056321690561029)
Reverend Marvin Ingalls has motive: True or False?
True (0.7264255794048772)
Reverend Marvin Ingalls has opportunity: True or False?
False (0.5621765360769869)
Sheila Ingalls is guilty: True or False?
True (0.7468781552484828)
Sheila Ingalls has mean: True or False?
True (0.8283842201397164)
Sheila Ingalls has motive: True or False?
True (0.6749080895533367)
Sheila Ingalls has opportunity: True or False?
False (0.5350984235603058)
Wallace Anders is guilty: True or False?
True (0.8413047772878592)
Wallace Anders has mean: True or False?
True (0.7017130830397807)
Wallace Anders has motive: True or False?
True (0.6996649413792725)
Wallace Anders has opportunity: True or False?
True (0.5832033352502285)
### Georgette Pelham
- mean: False (0.4148987966000043)
- motive: False (0.6039318499573872)
- opportunity: False (0.6934729182490079)

### Reverend Marvin Ingalls
- mean: False (0.1943678309438971)
- motive: False (0.2735744205951228)
- opportunity: False (0.5621765360769869)

### Sheila Ingalls
- mean: False (0.17161577986028365)
- motive: False (0.3250919104466633)
- opportunity: False (0.5350984235603058)

### Wallace Anders
- mean: True (0.7017130830397807)
- motive: True (0.6996649413792725)
- opportunity: True (0.5832033352502285)

The culprit is Wallace Anders.
In fact, it is Wallace Anders.
## 5minutemystery-shoot-out-at-splithead-canyon
Big George Ratcliffe is guilty: True or False?
True (0.9073122118500465)
Big George Ratcliffe has mean: True or False?
True (0.9403530352223053)
Big George Ratcliffe has motive: True or False?
True (0.8895288719962232)
Big George Ratcliffe has opportunity: True or False?
True (0.8701565822173906)
Chester Morris is guilty: True or False?
True (0.9063219998220023)
Chester Morris has mean: True or False?
True (0.9152045868398637)
Chester Morris has motive: True or False?
True (0.8951566249612815)
Chester Morris has opportunity: True or False?
True (0.832781310996106)
Joe Franklin is guilty: True or False?
True (0.9286679635448885)
Joe Franklin has mean: True or False?
True (0.9314625284362855)
Joe Franklin has motive: True or False?
True (0.9511421913058572)
Joe Franklin has opportunity: True or False?
True (0.9010534302227574)
Slim Jameson is guilty: True or False?
True (0.9235923286659299)
Slim Jameson has mean: True or False?
True (0.927099763868178)
Slim Jameson has motive: True or False?
True (0.9031234959323464)
Slim Jameson has opportunity: True or False?
True (0.8193157317863493)
### Big George Ratcliffe
- mean: False (0.05964696477769471)
- motive: False (0.11047112800377679)
- opportunity: False (0.12984341778260944)

### Chester Morris
- mean: False (0.08479541316013628)
- motive: False (0.10484337503871854)
- opportunity: False (0.16721868900389403)

### Joe Franklin
- mean: True (0.9314625284362855)
- motive: True (0.9511421913058572)
- opportunity: True (0.9010534302227574)

### Slim Jameson
- mean: False (0.07290023613182195)
- motive: False (0.09687650406765358)
- opportunity: False (0.1806842682136507)

The culprit is Joe Franklin.
In fact, it is Slim Jameson.
## 5minutemystery-the-mystery-of-the-american-raid
Admiral Taro is guilty: True or False?
False (0.5175709123121337)
Admiral Taro has mean: True or False?
True (0.7752647497229632)
Admiral Taro has motive: True or False?
True (0.6918097672776748)
Admiral Taro has opportunity: True or False?
True (0.5219585151310108)
Gina is guilty: True or False?
True (0.6714705301843162)
Gina has mean: True or False?
True (0.7853085971692302)
Gina has motive: True or False?
True (0.7908535601223919)
Gina has opportunity: True or False?
True (0.8134608241927087)
Kira is guilty: True or False?
True (0.6039318499573872)
Kira has mean: True or False?
True (0.5621765360769869)
Kira has motive: True or False?
True (0.8247443993706964)
Kira has opportunity: True or False?
True (0.8464508054137014)
The Emperor is guilty: True or False?
True (0.9170058945178141)
The Emperor has mean: True or False?
True (0.8984105603938967)
The Emperor has motive: True or False?
True (0.7606506998655483)
The Emperor has opportunity: True or False?
True (0.7275885284692245)
### Admiral Taro
- mean: False (0.22473525027703678)
- motive: False (0.30819023272232515)
- opportunity: False (0.47804148486898923)

### Gina
- mean: True (0.7853085971692302)
- motive: True (0.7908535601223919)
- opportunity: True (0.8134608241927087)

### Kira
- mean: False (0.4378234639230131)
- motive: False (0.17525560062930357)
- opportunity: False (0.15354919458629857)

### The Emperor
- mean: False (0.10158943960610334)
- motive: False (0.23934930013445166)
- opportunity: False (0.2724114715307755)

The culprit is Gina.
In fact, it is Admiral Taro.
## 5minutemystery-the-missing-ornament-mystery
Jackie Hadley is guilty: True or False?
True (0.9014011626580862)
Jackie Hadley has mean: True or False?
True (0.9731388097113137)
Jackie Hadley has motive: True or False?
True (0.9589241138134527)
Jackie Hadley has opportunity: True or False?
True (0.8649961307471897)
Lennie Hadley is guilty: True or False?
True (0.952397407545942)
Lennie Hadley has mean: True or False?
True (0.9575961815839735)
Lennie Hadley has motive: True or False?
True (0.9799765949220004)
Lennie Hadley has opportunity: True or False?
True (0.9291837815043049)
Mike Hadley is guilty: True or False?
True (0.947962222968318)
Mike Hadley has mean: True or False?
True (0.9777987599607383)
Mike Hadley has motive: True or False?
True (0.9819792515812888)
Mike Hadley has opportunity: True or False?
True (0.9413853274043543)
Sandy Hadley is guilty: True or False?
True (0.920789721359066)
Sandy Hadley has mean: True or False?
True (0.8895288719962232)
Sandy Hadley has motive: True or False?
True (0.971019387667922)
Sandy Hadley has opportunity: True or False?
True (0.8137569459807168)
Tommy Hadley is guilty: True or False?
True (0.954477967000386)
Map:  47%|████▋     | 95/203 [40:47<52:03, 28.92s/ examples]Map:  47%|████▋     | 96/203 [41:15<51:03, 28.63s/ examples]Map:  48%|████▊     | 97/203 [41:37<46:43, 26.45s/ examples]Map:  48%|████▊     | 98/203 [42:03<46:08, 26.36s/ examples]Map:  49%|████▉     | 99/203 [42:29<45:27, 26.23s/ examples]Tommy Hadley has mean: True or False?
True (0.9667888295116236)
Tommy Hadley has motive: True or False?
True (0.9912208913804552)
Tommy Hadley has opportunity: True or False?
True (0.9774139529645163)
### Jackie Hadley
- mean: False (0.026861190288686276)
- motive: False (0.04107588618654734)
- opportunity: False (0.13500386925281027)

### Lennie Hadley
- mean: False (0.04240381841602647)
- motive: False (0.0200234050779996)
- opportunity: False (0.07081621849569508)

### Mike Hadley
- mean: False (0.022201240039261716)
- motive: False (0.018020748418711152)
- opportunity: False (0.05861467259564568)

### Sandy Hadley
- mean: False (0.11047112800377679)
- motive: False (0.02898061233207805)
- opportunity: False (0.1862430540192832)

### Tommy Hadley
- mean: True (0.9667888295116236)
- motive: True (0.9912208913804552)
- opportunity: True (0.9774139529645163)

The culprit is Tommy Hadley.
In fact, it is Lennie Hadley.
## 5minutemystery-the-pilgrim-thanksgiving-puzzle
John Alden is guilty: True or False?
True (0.878314250659373)
John Alden has mean: True or False?
True (0.9026095892260383)
John Alden has motive: True or False?
True (0.7839884808423031)
John Alden has opportunity: True or False?
False (0.5660185688696566)
Miles Standish is guilty: True or False?
True (0.9295683483415352)
Miles Standish has mean: True or False?
True (0.8563323578093363)
Miles Standish has motive: True or False?
True (0.8289387819824735)
Miles Standish has opportunity: True or False?
True (0.6825736720802238)
Priscilla Mulllins is guilty: True or False?
True (0.8376200175313318)
Priscilla Mulllins has mean: True or False?
True (0.9043130884593419)
Priscilla Mulllins has motive: True or False?
True (0.6406358487498992)
Priscilla Mulllins has opportunity: True or False?
True (0.5224457875179084)
William Bradford is guilty: True or False?
True (0.7233095190955371)
William Bradford has mean: True or False?
True (0.8080671968507699)
William Bradford has motive: True or False?
True (0.6288633913849659)
William Bradford has opportunity: True or False?
False (0.6967841871600284)
### John Alden
- mean: False (0.09739041077396171)
- motive: False (0.2160115191576969)
- opportunity: False (0.5660185688696566)

### Miles Standish
- mean: True (0.8563323578093363)
- motive: True (0.8289387819824735)
- opportunity: True (0.6825736720802238)

### Priscilla Mulllins
- mean: False (0.09568691154065811)
- motive: False (0.3593641512501008)
- opportunity: False (0.4775542124820916)

### William Bradford
- mean: False (0.1919328031492301)
- motive: False (0.37113660861503406)
- opportunity: False (0.6967841871600284)

The culprit is Miles Standish.
In fact, it is John Alden.
## 5minutemystery-the-disappearing-turkey
Darby is guilty: True or False?
True (0.7490872087035162)
Darby has mean: True or False?
True (0.6406358487498992)
Darby has motive: True or False?
True (0.8278281666221954)
Darby has opportunity: True or False?
True (0.6662796746479285)
Father is guilty: True or False?
True (0.9615337835163564)
Father has mean: True or False?
True (0.77729988964086)
Father has motive: True or False?
True (0.9099069836112468)
Father has opportunity: True or False?
True (0.6584175136252488)
Greg is guilty: True or False?
True (0.8998277786460391)
Greg has mean: True or False?
True (0.7859664553110391)
Greg has motive: True or False?
True (0.9046505126460354)
Greg has opportunity: True or False?
True (0.7655933544531522)
Uncle Larry is guilty: True or False?
True (0.9299510095943111)
Uncle Larry has mean: True or False?
True (0.8661325012437474)
Uncle Larry has motive: True or False?
True (0.911809923444246)
Uncle Larry has opportunity: True or False?
True (0.8255897087847518)
### Darby
- mean: False (0.3593641512501008)
- motive: False (0.17217183337780462)
- opportunity: False (0.3337203253520715)

### Father
- mean: False (0.22270011035913995)
- motive: False (0.09009301638875322)
- opportunity: False (0.3415824863747512)

### Greg
- mean: False (0.21403354468896085)
- motive: False (0.09534948735396465)
- opportunity: False (0.23440664554684776)

### Uncle Larry
- mean: True (0.8661325012437474)
- motive: True (0.911809923444246)
- opportunity: True (0.8255897087847518)

The culprit is Uncle Larry.
In fact, it is Father.
## 5minutemystery-a-thanksgiving-mystery-poem
Libby is guilty: True or False?
True (0.9217811254507657)
Libby has mean: True or False?
True (0.8697145551802641)
Libby has motive: True or False?
True (0.9197868083117009)
Libby has opportunity: True or False?
True (0.8710367026584496)
Rusty is guilty: True or False?
True (0.8866169426295919)
Rusty has mean: True or False?
True (1.357561222574218)
Rusty has motive: True or False?
True (1.3169100678433772)
Rusty has opportunity: True or False?
True (0.7962924854830264)
Tiny is guilty: True or False?
True (1.582669490054393)
Tiny has mean: True or False?
True (1.156026542411078)
Tiny has motive: True or False?
True (1.3789815370569487)
Tiny has opportunity: True or False?
True (0.7969253675907205)
Tom is guilty: True or False?
True (0.8517062701455038)
Tom has mean: True or False?
True (0.7122322217365102)
Tom has motive: True or False?
True (0.8071567377359422)
Tom has opportunity: True or False?
True (0.7302898714065358)
### Libby
- mean: False (0.13028544481973592)
- motive: False (0.0802131916882991)
- opportunity: False (0.12896329734155043)

### Rusty
- mean: True (1.357561222574218)
- motive: True (1.3169100678433772)
- opportunity: True (0.7962924854830264)

### Tiny
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.20307463240927948)

### Tom
- mean: False (0.28776777826348976)
- motive: False (0.1928432622640578)
- opportunity: False (0.2697101285934642)

The culprit is Rusty.
In fact, it is Rusty.
## 5minutemystery-turkey-cull
Beaker is guilty: True or False?
True (0.8062431235779619)
Beaker has mean: True or False?
True (0.7669924589170153)
Beaker has motive: True or False?
True (0.9491062747098069)
Beaker has opportunity: True or False?
True (0.7008948290825966)
Beau is guilty: True or False?
True (0.8204693794114111)
Beau has mean: True or False?
True (0.8778961263000082)
Beau has motive: True or False?
True (0.9545627850600183)
Beau has opportunity: True or False?
True (0.8895288719962232)
Leaf is guilty: True or False?
True (0.8697145551802641)
Leaf has mean: True or False?
True (0.8074606715677252)
Leaf has motive: True or False?
True (0.8638516611889259)
Leaf has opportunity: True or False?
True (0.7766228995235426)
Red is guilty: True or False?
True (0.7549149897594328)
Red has mean: True or False?
True (0.8397339530959691)
Red has motive: True or False?
True (0.9170058945178141)
Red has opportunity: True or False?
True (0.7185943809170431)
### Beaker
- mean: False (0.23300754108298471)
- motive: False (0.05089372529019309)
- opportunity: False (0.2991051709174034)

### Beau
- mean: True (0.8778961263000082)
- motive: True (0.9545627850600183)
- opportunity: True (0.8895288719962232)

### Leaf
- mean: False (0.19253932843227484)
- motive: False (0.13614833881107413)
- opportunity: False (0.22337710047645742)

### Red
- mean: False (0.1602660469040309)
- motive: False (0.08299410548218589)
- opportunity: False (0.2814056190829569)

The culprit is Beau.
In fact, it is Beau.
## 5minutemystery-a-turkey-day-struggle
Aunt Rachel is guilty: True or False?
True (0.686790355176806)
Aunt Rachel has mean: True or False?
True (0.7527403228571042)
Aunt Rachel has motive: True or False?
True (0.7826624547920057)
Aunt Rachel has opportunity: True or False?
True (0.5273165068094335)
Chris is guilty: True or False?
True (0.740174341079517)
Chris has mean: True or False?
True (0.9099069836112468)
Chris has motive: True or False?
True (0.9294403817764149)
Chris has opportunity: True or False?
True (0.844921525814193)
Diane is guilty: True or False?
True (0.7185943809170431)
Diane has mean: True or False?
True (0.8238958672039278)
Diane has motive: True or False?
True (0.8933094122075369)
Diane has opportunity: True or False?
True (0.7041601500399041)
Jack the Dog is guilty: True or False?
True (0.8250265073476026)
Jack the Dog has mean: True or False?
True (0.8652240590801695)
Map:  49%|████▉     | 100/203 [42:53<43:54, 25.57s/ examples]Map:  50%|████▉     | 101/203 [43:15<41:54, 24.65s/ examples]Map:  50%|█████     | 102/203 [43:44<43:39, 25.93s/ examples]Map:  51%|█████     | 103/203 [44:07<41:52, 25.13s/ examples]Map:  51%|█████     | 104/203 [44:34<42:14, 25.60s/ examples]Jack the Dog has motive: True or False?
True (0.9193533657123177)
Jack the Dog has opportunity: True or False?
True (0.8227594449669557)
### Aunt Rachel
- mean: False (0.24725967714289576)
- motive: False (0.2173375452079943)
- opportunity: False (0.47268349319056646)

### Chris
- mean: True (0.9099069836112468)
- motive: True (0.9294403817764149)
- opportunity: True (0.844921525814193)

### Diane
- mean: False (0.17610413279607218)
- motive: False (0.1066905877924631)
- opportunity: False (0.29583984996009594)

### Jack the Dog
- mean: False (0.13477594091983047)
- motive: False (0.08064663428768226)
- opportunity: False (0.17724055503304426)

The culprit is Chris.
In fact, it is Chris.
## 5minutemystery-the-missing-briefcase
Porter 1 is guilty: True or False?
True (0.8006919661398397)
Porter 1 has mean: True or False?
True (0.861071588244826)
Porter 1 has motive: True or False?
True (0.8697145551802641)
Porter 1 has opportunity: True or False?
True (0.8227595062673136)
Porter 2 is guilty: True or False?
True (0.8000678954040312)
Porter 2 has mean: True or False?
True (0.8665847814067802)
Porter 2 has motive: True or False?
True (0.9329437018480795)
Porter 2 has opportunity: True or False?
True (0.925499741040984)
Porter 3 is guilty: True or False?
True (0.8294920340613177)
Porter 3 has mean: True or False?
True (0.9001793304600783)
Porter 3 has motive: True or False?
True (0.9422947179693436)
Porter 3 has opportunity: True or False?
True (0.9485372300670596)
Porter 4 is guilty: True or False?
True (0.8745065279415651)
Porter 4 has mean: True or False?
True (0.8984105603938967)
Porter 4 has motive: True or False?
True (0.8944211616820568)
Porter 4 has opportunity: True or False?
True (0.9105454073245608)
### Porter 1
- mean: False (0.138928411755174)
- motive: False (0.13028544481973592)
- opportunity: False (0.17724049373268635)

### Porter 2
- mean: False (0.1334152185932198)
- motive: False (0.06705629815192049)
- opportunity: False (0.07450025895901602)

### Porter 3
- mean: True (0.9001793304600783)
- motive: True (0.9422947179693436)
- opportunity: True (0.9485372300670596)

### Porter 4
- mean: False (0.10158943960610334)
- motive: False (0.10557883831794324)
- opportunity: False (0.0894545926754392)

The culprit is Porter 3.
In fact, it is Porter 3.
## 5minutemystery-everythings-not-just-ducky
Bethany is guilty: True or False?
True (0.9425067301242699)
Bethany has mean: True or False?
True (0.9433475737015985)
Bethany has motive: True or False?
True (0.9698426136593115)
Bethany has opportunity: True or False?
True (0.8670357473609658)
Connor is guilty: True or False?
True (0.9039744767757508)
Connor has mean: True or False?
True (0.94948238112973)
Connor has motive: True or False?
True (0.9736947425622681)
Connor has opportunity: True or False?
True (0.9284088027271398)
Emma is guilty: True or False?
True (0.8757869551856522)
Emma has mean: True or False?
True (0.9181872635464632)
Emma has motive: True or False?
True (0.911809984585868)
Emma has opportunity: True or False?
True (0.8776866221669275)
Tim is guilty: True or False?
True (0.8086723099497763)
Tim has mean: True or False?
True (0.947769104959166)
Tim has motive: True or False?
True (0.9540517932883525)
Tim has opportunity: True or False?
True (0.8881781721623143)
### Bethany
- mean: False (0.056652426298401504)
- motive: False (0.03015738634068854)
- opportunity: False (0.13296425263903422)

### Connor
- mean: True (0.94948238112973)
- motive: True (0.9736947425622681)
- opportunity: True (0.9284088027271398)

### Emma
- mean: False (0.08181273645353682)
- motive: False (0.08819001541413196)
- opportunity: False (0.1223133778330725)

### Tim
- mean: False (0.052230895040834)
- motive: False (0.045948206711647455)
- opportunity: False (0.11182182783768568)

The culprit is Connor.
In fact, it is Bethany.
## 5minutemystery-a-darkened-veterans-day
Colonel Abraham is guilty: True or False?
True (0.9158089188126235)
Colonel Abraham has mean: True or False?
True (0.8272706865691472)
Colonel Abraham has motive: True or False?
True (0.94620036983)
Colonel Abraham has opportunity: True or False?
True (0.8852351930010195)
Frank Thompson is guilty: True or False?
True (0.9479621664653681)
Frank Thompson has mean: True or False?
True (0.9145963197706802)
Frank Thompson has motive: True or False?
True (0.963230549923961)
Frank Thompson has opportunity: True or False?
True (0.865678909174824)
Mr. Landry is guilty: True or False?
True (0.7505527730327083)
Mr. Landry has mean: True or False?
True (0.7209580648179327)
Mr. Landry has motive: True or False?
True (0.8514594452543962)
Mr. Landry has opportunity: True or False?
True (0.7898827135821628)
Ryan Smith is guilty: True or False?
True (0.9063219998220023)
Ryan Smith has mean: True or False?
True (0.8799743689174987)
Ryan Smith has motive: True or False?
True (0.8933094122075369)
Ryan Smith has opportunity: True or False?
True (0.7819973291046377)
### Colonel Abraham
- mean: False (0.17272931343085285)
- motive: False (0.05379963017)
- opportunity: False (0.1147648069989805)

### Frank Thompson
- mean: True (0.9145963197706802)
- motive: True (0.963230549923961)
- opportunity: True (0.865678909174824)

### Mr. Landry
- mean: False (0.2790419351820673)
- motive: False (0.1485405547456038)
- opportunity: False (0.21011728641783722)

### Ryan Smith
- mean: False (0.1200256310825013)
- motive: False (0.1066905877924631)
- opportunity: False (0.2180026708953623)

The culprit is Frank Thompson.
In fact, it is Colonel Abraham.
## 5minutemystery-the-missing-ring
Fingers Ferguson is guilty: True or False?
False (0.7492284470473839)
Fingers Ferguson has mean: True or False?
True (0.8795611817678315)
Fingers Ferguson has motive: True or False?
False (0.6148266936950935)
Fingers Ferguson has opportunity: True or False?
False (0.8116560574095553)
Joe Morgan is guilty: True or False?
True (0.8092759828926619)
Joe Morgan has mean: True or False?
True (0.9066531685310133)
Joe Morgan has motive: True or False?
True (0.770464837675413)
Joe Morgan has opportunity: True or False?
True (0.7333563569098757)
Manuel Garcia is guilty: True or False?
True (0.5107405249783342)
Manuel Garcia has mean: True or False?
True (0.621540893468236)
Manuel Garcia has motive: True or False?
False (0.597373048111048)
Manuel Garcia has opportunity: True or False?
False (0.740174341079517)
Mr. Bridges is guilty: True or False?
True (0.6095241816115718)
Mr. Bridges has mean: True or False?
True (0.7905303264811482)
Mr. Bridges has motive: True or False?
True (0.6688802830862913)
Mr. Bridges has opportunity: True or False?
True (0.5185461538431656)
### Fingers Ferguson
- mean: False (0.12043881823216851)
- motive: False (0.6148266936950935)
- opportunity: False (0.8116560574095553)

### Joe Morgan
- mean: True (0.9066531685310133)
- motive: True (0.770464837675413)
- opportunity: True (0.7333563569098757)

### Manuel Garcia
- mean: False (0.37845910653176396)
- motive: False (0.597373048111048)
- opportunity: False (0.740174341079517)

### Mr. Bridges
- mean: False (0.20946967351885182)
- motive: False (0.3311197169137087)
- opportunity: False (0.4814538461568344)

The culprit is Joe Morgan.
In fact, it is Joe Morgan.
## 5minutemystery-brass-keyboard-mystery
April Key #4 is guilty: True or False?
True (0.7613611200983542)
April Key #4 has mean: True or False?
True (0.7098244343353132)
April Key #4 has motive: True or False?
True (0.7634837587244478)
April Key #4 has opportunity: True or False?
True (0.7233094544266295)
Denise Key #6 is guilty: True or False?
True (0.7541915688671895)
Denise Key #6 has mean: True or False?
True (0.7049732238008671)
Denise Key #6 has motive: True or False?
True (0.6178585826183487)
Denise Key #6 has opportunity: True or False?
True (0.5185462156586879)
Harold Key #1 is guilty: True or False?
True (0.7756047866813147)
Harold Key #1 has mean: True or False?
True (0.6884683992569801)
Harold Key #1 has motive: True or False?
True (0.6688802830862913)
Harold Key #1 has opportunity: True or False?
True (0.5428632463719839)
Kirsten Key #5 is guilty: True or False?
True (0.5195212821349473)
Kirsten Key #5 has mean: True or False?
Map:  52%|█████▏    | 105/203 [45:09<46:32, 28.49s/ examples]Map:  52%|█████▏    | 106/203 [45:39<46:31, 28.78s/ examples]Map:  53%|█████▎    | 107/203 [46:16<50:01, 31.26s/ examples]Map:  53%|█████▎    | 108/203 [46:41<46:33, 29.40s/ examples]Map:  54%|█████▎    | 109/203 [47:12<47:00, 30.00s/ examples]False (0.5964331079469681)
Kirsten Key #5 has motive: True or False?
False (0.6884684608108543)
Kirsten Key #5 has opportunity: True or False?
False (0.8665847814067802)
Robert (Buddy) Key #3 is guilty: True or False?
True (0.7412996266976789)
Robert (Buddy) Key #3 has mean: True or False?
True (0.8250265073476026)
Robert (Buddy) Key #3 has motive: True or False?
True (0.5156198737738186)
Robert (Buddy) Key #3 has opportunity: True or False?
True (0.5423785259821196)
### April Key #4
- mean: True (0.7098244343353132)
- motive: True (0.7634837587244478)
- opportunity: True (0.7233094544266295)

### Denise Key #6
- mean: False (0.29502677619913287)
- motive: False (0.3821414173816513)
- opportunity: False (0.48145378434131214)

### Harold Key #1
- mean: False (0.3115316007430199)
- motive: False (0.3311197169137087)
- opportunity: False (0.4571367536280161)

### Kirsten Key #5
- mean: False (0.5964331079469681)
- motive: False (0.6884684608108543)
- opportunity: False (0.8665847814067802)

### Robert (Buddy) Key #3
- mean: False (0.17497349265239737)
- motive: False (0.48438012622618143)
- opportunity: False (0.45762147401788045)

The culprit is April Key #4.
In fact, it is April Key #4.
## 5minutemystery-the-curse-of-the-unlucky-streak
Coach Williams is guilty: True or False?
True (0.8031737798924701)
Coach Williams has mean: True or False?
True (0.7345005213790038)
Coach Williams has motive: True or False?
True (0.8517062701455038)
Coach Williams has opportunity: True or False?
True (0.6592954931819778)
Joe is guilty: True or False?
True (0.5869964306477841)
Joe has mean: True or False?
True (0.8568122429692968)
Joe has motive: True or False?
True (0.861071588244826)
Joe has opportunity: True or False?
True (0.7178038242127955)
Mrs. Williams is guilty: True or False?
True (0.8957052808276003)
Mrs. Williams has mean: True or False?
True (0.8645393849369172)
Mrs. Williams has motive: True or False?
True (0.9485372300670596)
Mrs. Williams has opportunity: True or False?
True (0.8261514850267767)
Roderick is guilty: True or False?
True (0.6834194581047349)
Roderick has mean: True or False?
True (0.60859406896259)
Roderick has motive: True or False?
True (0.7711548223101617)
Roderick has opportunity: True or False?
True (0.6343168082332088)
### Coach Williams
- mean: False (0.2654994786209962)
- motive: False (0.14829372985449618)
- opportunity: False (0.3407045068180222)

### Joe
- mean: False (0.1431877570307032)
- motive: False (0.138928411755174)
- opportunity: False (0.28219617578720446)

### Mrs. Williams
- mean: True (0.8645393849369172)
- motive: True (0.9485372300670596)
- opportunity: True (0.8261514850267767)

### Roderick
- mean: False (0.39140593103740995)
- motive: False (0.22884517768983825)
- opportunity: False (0.3656831917667912)

The culprit is Mrs. Williams.
In fact, it is Joe.
## 5minutemystery-halloween-2008
Bride is guilty: True or False?
True (0.9124361266596831)
Bride has mean: True or False?
True (0.8558511727823209)
Bride has motive: True or False?
True (0.8620035048683017)
Bride has opportunity: True or False?
True (0.9171543708147702)
Groom is guilty: True or False?
True (0.9169315082548071)
Groom has mean: True or False?
True (0.8559715712342816)
Groom has motive: True or False?
True (0.901737077061468)
Groom has opportunity: True or False?
True (0.8912444703721882)
Indian Chief is guilty: True or False?
True (0.9178196797655932)
Indian Chief has mean: True or False?
True (0.9014011626580862)
Indian Chief has motive: True or False?
True (0.9083743698340163)
Indian Chief has opportunity: True or False?
True (0.9326375756581993)
Wealthy Woman is guilty: True or False?
True (0.9480103258576807)
Wealthy Woman has mean: True or False?
True (0.9243469854582533)
Wealthy Woman has motive: True or False?
True (0.9390807169043887)
Wealthy Woman has opportunity: True or False?
True (0.9355233894679749)
### Bride
- mean: False (0.14414882721767908)
- motive: False (0.13799649513169832)
- opportunity: False (0.08284562918522975)

### Groom
- mean: False (0.14402842876571842)
- motive: False (0.098262922938532)
- opportunity: False (0.10875552962781176)

### Indian Chief
- mean: False (0.09859883734191377)
- motive: False (0.09162563016598368)
- opportunity: False (0.06736242434180073)

### Wealthy Woman
- mean: True (0.9243469854582533)
- motive: True (0.9390807169043887)
- opportunity: True (0.9355233894679749)

The culprit is Wealthy Woman.
In fact, it is Groom.
## 5minutemystery-the-trick-or-treat-mystery
Dorothy is guilty: True or False?
True (0.8386797935187188)
Dorothy has mean: True or False?
True (0.7718435616326055)
Dorothy has motive: True or False?
True (0.8860265005470086)
Dorothy has opportunity: True or False?
True (0.920789721359066)
Superman is guilty: True or False?
True (0.8958875533219306)
Superman has mean: True or False?
True (0.8413048399699521)
Superman has motive: True or False?
True (0.9410069597342015)
Superman has opportunity: True or False?
True (0.8221891570741111)
The Ghost is guilty: True or False?
True (0.8128672807499561)
The Ghost has mean: True or False?
True (0.8056321690561029)
The Ghost has motive: True or False?
True (0.8386797935187188)
The Ghost has opportunity: True or False?
True (0.8227594449669557)
The Lion is guilty: True or False?
True (0.7333563569098757)
The Lion has mean: True or False?
True (0.779321849347754)
The Lion has motive: True or False?
True (0.8514594452543962)
The Lion has opportunity: True or False?
True (0.8397339530959691)
The Witch is guilty: True or False?
True (0.7669925046333297)
The Witch has mean: True or False?
True (0.7937461674149602)
The Witch has motive: True or False?
True (0.8727817583545995)
The Witch has opportunity: True or False?
True (0.8428631416381634)
### Dorothy
- mean: False (0.22815643836739452)
- motive: False (0.1139734994529914)
- opportunity: False (0.079210278640934)

### Superman
- mean: True (0.8413048399699521)
- motive: True (0.9410069597342015)
- opportunity: True (0.8221891570741111)

### The Ghost
- mean: False (0.1943678309438971)
- motive: False (0.1613202064812812)
- opportunity: False (0.17724055503304426)

### The Lion
- mean: False (0.22067815065224605)
- motive: False (0.1485405547456038)
- opportunity: False (0.1602660469040309)

### The Witch
- mean: False (0.20625383258503982)
- motive: False (0.12721824164540052)
- opportunity: False (0.15713685836183655)

The culprit is Superman.
In fact, it is The Witch.
## 5minutemystery-house-of-the-rising-pumpkin
Curtis is guilty: True or False?
True (0.7981867775042927)
Curtis has mean: True or False?
True (0.7711548682745724)
Curtis has motive: True or False?
True (0.9463988549853353)
Curtis has opportunity: True or False?
True (0.7779753136455794)
Dabney is guilty: True or False?
True (0.9216402157401415)
Dabney has mean: True or False?
True (0.905989824801558)
Dabney has motive: True or False?
True (0.9645224799532249)
Dabney has opportunity: True or False?
True (0.8984105001507761)
Kim is guilty: True or False?
True (0.8601343603168419)
Kim has mean: True or False?
True (0.9299510095943111)
Kim has motive: True or False?
True (0.9580694433457548)
Kim has opportunity: True or False?
True (0.9122799654606127)
Mary is guilty: True or False?
True (0.884837803442546)
Mary has mean: True or False?
True (0.8638516611889259)
Mary has motive: True or False?
True (0.9477691649813238)
Mary has opportunity: True or False?
True (0.8716934900924195)
### Curtis
- mean: False (0.22884513172542764)
- motive: False (0.05360114501466473)
- opportunity: False (0.22202468635442063)

### Dabney
- mean: False (0.09401017519844201)
- motive: False (0.03547752004677507)
- opportunity: False (0.10158949984922394)

### Kim
- mean: True (0.9299510095943111)
- motive: True (0.9580694433457548)
- opportunity: True (0.9122799654606127)

### Mary
- mean: False (0.13614833881107413)
- motive: False (0.0522308350186762)
- opportunity: False (0.12830650990758052)

The culprit is Kim.
In fact, it is Kim.
## 5minutemystery-the-secret-of-the-scarecrows-mask
Charles Kincaid is guilty: True or False?
True (0.9124361266596831)
Charles Kincaid has mean: True or False?
True (0.7898827724330132)
Map:  54%|█████▍    | 110/203 [47:37<44:13, 28.54s/ examples]Map:  55%|█████▍    | 111/203 [48:06<43:53, 28.62s/ examples]Map:  55%|█████▌    | 112/203 [48:27<39:41, 26.17s/ examples]Map:  56%|█████▌    | 113/203 [48:53<39:24, 26.27s/ examples]Map:  56%|█████▌    | 114/203 [49:18<38:18, 25.82s/ examples]Charles Kincaid has motive: True or False?
True (0.7975568155246964)
Charles Kincaid has opportunity: True or False?
True (0.6104534962074417)
Chester is guilty: True or False?
True (0.8591917766133458)
Chester has mean: True or False?
True (0.8624675215861032)
Chester has motive: True or False?
True (0.8204694405411458)
Chester has opportunity: True or False?
False (0.5360700410935405)
Mr. Winfrey is guilty: True or False?
True (0.9155072554665495)
Mr. Winfrey has mean: True or False?
True (0.8349459127213729)
Mr. Winfrey has motive: True or False?
True (0.7606506998655483)
Mr. Winfrey has opportunity: True or False?
True (0.7154240000492645)
Mrs. Winfrey is guilty: True or False?
True (0.8795611817678315)
Mrs. Winfrey has mean: True or False?
True (0.8338664756137771)
Mrs. Winfrey has motive: True or False?
True (0.7655933544531522)
Mrs. Winfrey has opportunity: True or False?
True (0.8074606715677252)
### Charles Kincaid
- mean: False (0.2101172275669868)
- motive: False (0.20244318447530363)
- opportunity: False (0.3895465037925583)

### Chester
- mean: False (0.13753247841389682)
- motive: False (0.1795305594588542)
- opportunity: False (0.5360700410935405)

### Mr. Winfrey
- mean: False (0.16505408727862714)
- motive: False (0.23934930013445166)
- opportunity: False (0.28457599995073546)

### Mrs. Winfrey
- mean: True (0.8338664756137771)
- motive: True (0.7655933544531522)
- opportunity: True (0.8074606715677252)

The culprit is Mrs. Winfrey.
In fact, it is Chester.
## 5minutemystery-the-scarecrow-slasher
Annie is guilty: True or False?
False (0.5525396910980834)
Annie has mean: True or False?
True (0.6206216296838327)
Annie has motive: True or False?
True (0.7122321792841629)
Annie has opportunity: True or False?
True (0.6984323202883935)
Mr. Forbes is guilty: True or False?
True (0.7697732451157533)
Mr. Forbes has mean: True or False?
True (0.8454326959560526)
Mr. Forbes has motive: True or False?
True (0.7975568155246964)
Mr. Forbes has opportunity: True or False?
True (0.6645402797838648)
Mrs. Avery is guilty: True or False?
True (0.7752646804088963)
Mrs. Avery has mean: True or False?
True (0.7333564224770464)
Mrs. Avery has motive: True or False?
True (0.7541915239138703)
Mrs. Avery has opportunity: True or False?
True (0.6477981763584071)
Philips is guilty: True or False?
True (0.6967842494573921)
Philips has mean: True or False?
False (0.5165954726976894)
Philips has motive: True or False?
True (0.6406358487498992)
Philips has opportunity: True or False?
True (0.5068355091660127)
### Annie
- mean: False (0.3793783703161673)
- motive: False (0.28776782071583706)
- opportunity: False (0.3015676797116065)

### Mr. Forbes
- mean: True (0.8454326959560526)
- motive: True (0.7975568155246964)
- opportunity: True (0.6645402797838648)

### Mrs. Avery
- mean: False (0.26664357752295365)
- motive: False (0.24580847608612966)
- opportunity: False (0.3522018236415929)

### Philips
- mean: False (0.5165954726976894)
- motive: False (0.3593641512501008)
- opportunity: False (0.4931644908339873)

The culprit is Mr. Forbes.
In fact, it is Philips.
## 5minutemystery-the-golden-ruse
Miss Jones is guilty: True or False?
True (0.6575384105121485)
Miss Jones has mean: True or False?
True (0.8652240590801695)
Miss Jones has motive: True or False?
True (0.7711548682745724)
Miss Jones has opportunity: True or False?
True (0.5563995964631269)
Miss. Pendlebury is guilty: True or False?
True (0.7209580648179327)
Miss. Pendlebury has mean: True or False?
True (0.867485409735739)
Miss. Pendlebury has motive: True or False?
True (0.7859663967519771)
Miss. Pendlebury has opportunity: True or False?
True (0.7130321332210621)
Mr. Horgan is guilty: True or False?
True (0.8080671968507699)
Mr. Horgan has mean: True or False?
True (0.9046505126460354)
Mr. Horgan has motive: True or False?
True (0.8740772044235984)
Mr. Horgan has opportunity: True or False?
True (0.7962924261546153)
Mr. Reese is guilty: True or False?
True (0.7033457711626864)
Mr. Reese has mean: True or False?
True (0.9502265454272235)
Mr. Reese has motive: True or False?
True (0.8474634858439474)
Mr. Reese has opportunity: True or False?
True (0.7217432334405754)
### Miss Jones
- mean: False (0.13477594091983047)
- motive: False (0.22884513172542764)
- opportunity: False (0.44360040353687313)

### Miss. Pendlebury
- mean: False (0.13251459026426105)
- motive: False (0.2140336032480229)
- opportunity: False (0.28696786677893793)

### Mr. Horgan
- mean: True (0.9046505126460354)
- motive: True (0.8740772044235984)
- opportunity: True (0.7962924261546153)

### Mr. Reese
- mean: False (0.04977345457277649)
- motive: False (0.15253651415605263)
- opportunity: False (0.27825676655942455)

The culprit is Mr. Horgan.
In fact, it is Mr. Horgan.
## 5minutemystery-hound-of-the-buskerville
Balloon Twister is guilty: True or False?
True (0.9548162209309636)
Balloon Twister has mean: True or False?
True (0.96920782287766)
Balloon Twister has motive: True or False?
True (0.9366337094376229)
Balloon Twister has opportunity: True or False?
True (0.8584814679672361)
Living Statue is guilty: True or False?
True (0.9015746123467522)
Living Statue has mean: True or False?
True (0.9478657243703977)
Living Statue has motive: True or False?
True (0.8624675215861032)
Living Statue has opportunity: True or False?
True (0.7446563307563252)
Mime is guilty: True or False?
True (0.8906751877407573)
Mime has mean: True or False?
True (0.9066531685310133)
Mime has motive: True or False?
True (0.8816149238192855)
Mime has opportunity: True or False?
True (0.8255897087847518)
Stilt-Walker is guilty: True or False?
True (0.9263036859044167)
Stilt-Walker has mean: True or False?
True (0.9346342066470359)
Stilt-Walker has motive: True or False?
True (0.9073122118500465)
Stilt-Walker has opportunity: True or False?
True (0.802555560073231)
### Balloon Twister
- mean: True (0.96920782287766)
- motive: True (0.9366337094376229)
- opportunity: True (0.8584814679672361)

### Living Statue
- mean: False (0.05213427562960227)
- motive: False (0.13753247841389682)
- opportunity: False (0.2553436692436748)

### Mime
- mean: False (0.0933468314689867)
- motive: False (0.11838507618071448)
- opportunity: False (0.1744102912152482)

### Stilt-Walker
- mean: False (0.06536579335296411)
- motive: False (0.09268778814995349)
- opportunity: False (0.19744443992676897)

The culprit is Balloon Twister.
In fact, it is Stilt-Walker.
## 5minutemystery-moriarty-picks-a-murderer-part-two
Hansom Cab Driver is guilty: True or False?
True (0.7885832152749314)
Hansom Cab Driver has mean: True or False?
True (0.802555560073231)
Hansom Cab Driver has motive: True or False?
True (0.944073857204818)
Hansom Cab Driver has opportunity: True or False?
True (0.9044818892710186)
Policeman is guilty: True or False?
True (0.6842640081724978)
Policeman has mean: True or False?
True (0.5794003525136094)
Policeman has motive: True or False?
True (0.9206470837359207)
Policeman has opportunity: True or False?
True (0.9095862487848758)
Theater Usher is guilty: True or False?
True (0.893681109060862)
Theater Usher has mean: True or False?
True (0.7895583472451868)
Theater Usher has motive: True or False?
True (0.907803776883121)
Theater Usher has opportunity: True or False?
True (0.7655933544531522)
Ticket Seller is guilty: True or False?
True (0.8494723435042196)
Ticket Seller has mean: True or False?
True (0.8556100696922833)
Ticket Seller has motive: True or False?
True (0.9464977993639099)
Ticket Seller has opportunity: True or False?
True (0.8966140148346177)
### Hansom Cab Driver
- mean: False (0.19744443992676897)
- motive: False (0.05592614279518204)
- opportunity: False (0.09551811072898142)

### Policeman
- mean: False (0.42059964748639056)
- motive: False (0.07935291626407925)
- opportunity: False (0.09041375121512418)

### Theater Usher
- mean: False (0.2104416527548132)
- motive: False (0.09219622311687903)
- opportunity: False (0.23440664554684776)

### Ticket Seller
- mean: True (0.8556100696922833)
- motive: True (0.9464977993639099)
- opportunity: True (0.8966140148346177)

The culprit is Ticket Seller.
In fact, it is Theater Usher.
Map:  57%|█████▋    | 115/203 [49:41<36:33, 24.93s/ examples]Map:  57%|█████▋    | 116/203 [50:06<36:23, 25.10s/ examples]Map:  58%|█████▊    | 117/203 [50:36<37:53, 26.43s/ examples]Map:  58%|█████▊    | 118/203 [50:59<35:57, 25.38s/ examples]## 5minutemystery-the-scent-of-a-thief
Betty is guilty: True or False?
True (0.7879311977554747)
Betty has mean: True or False?
True (0.725648573585541)
Betty has motive: True or False?
True (0.7371581892031299)
Betty has opportunity: True or False?
True (0.5486734660889085)
Darlene is guilty: True or False?
True (0.8407825844829613)
Darlene has mean: True or False?
True (0.7641883982873323)
Darlene has motive: True or False?
True (0.7386690954574974)
Darlene has opportunity: True or False?
True (0.612309626324874)
Mr. Danby is guilty: True or False?
True (0.7924642605907138)
Mr. Danby has mean: True or False?
True (0.6706082735718226)
Mr. Danby has motive: True or False?
True (0.6601724005812412)
Mr. Danby has opportunity: True or False?
True (0.6680145240815963)
Mr. Harrison is guilty: True or False?
True (0.8428631416381634)
Mr. Harrison has mean: True or False?
True (0.7697732451157533)
Mr. Harrison has motive: True or False?
True (0.6766198919456847)
Mr. Harrison has opportunity: True or False?
True (0.6370307821695329)
### Betty
- mean: False (0.274351426414459)
- motive: False (0.2628418107968701)
- opportunity: False (0.45132653391109145)

### Darlene
- mean: True (0.7641883982873323)
- motive: True (0.7386690954574974)
- opportunity: True (0.612309626324874)

### Mr. Danby
- mean: False (0.3293917264281774)
- motive: False (0.33982759941875884)
- opportunity: False (0.33198547591840366)

### Mr. Harrison
- mean: False (0.2302267548842467)
- motive: False (0.3233801080543153)
- opportunity: False (0.3629692178304671)

The culprit is Darlene.
In fact, it is Mr. Harrison.
## 5minutemystery-moriarty-picks-a-murderer-part-one
Ed the Bludgeoner is guilty: True or False?
True (0.7872777601997338)
Ed the Bludgeoner has mean: True or False?
True (0.6076631662366868)
Ed the Bludgeoner has motive: True or False?
True (0.7739006258141444)
Ed the Bludgeoner has opportunity: True or False?
True (0.7505527730327083)
Fastidious Fred Fielder is guilty: True or False?
True (0.727201163301072)
Fastidious Fred Fielder has mean: True or False?
True (0.7885832152749314)
Fastidious Fred Fielder has motive: True or False?
True (0.731825826396729)
Fastidious Fred Fielder has opportunity: True or False?
True (0.6723316913929156)
Herman Houlihan is guilty: True or False?
True (0.8062431235779619)
Herman Houlihan has mean: True or False?
True (0.589834510337428)
Herman Houlihan has motive: True or False?
True (0.7527403228571042)
Herman Houlihan has opportunity: True or False?
True (0.6029970803636248)
Morris the Ascot Dandy is guilty: True or False?
True (0.7490872087035162)
Morris the Ascot Dandy has mean: True or False?
True (0.740174341079517)
Morris the Ascot Dandy has motive: True or False?
True (0.7318258918270596)
Morris the Ascot Dandy has opportunity: True or False?
True (0.7240905804783984)
### Ed the Bludgeoner
- mean: False (0.3923368337633132)
- motive: False (0.22609937418585557)
- opportunity: False (0.2494472269672917)

### Fastidious Fred Fielder
- mean: False (0.21141678472506864)
- motive: False (0.268174173603271)
- opportunity: False (0.3276683086070844)

### Herman Houlihan
- mean: False (0.41016548966257205)
- motive: False (0.24725967714289576)
- opportunity: False (0.39700291963637524)

### Morris the Ascot Dandy
- mean: True (0.740174341079517)
- motive: True (0.7318258918270596)
- opportunity: True (0.7240905804783984)

The culprit is Morris the Ascot Dandy.
In fact, it is Fastidious Fred Fielder.
## 5minutemystery-the-geneva-summit-goldfish-mystery
Ermina Glandon is guilty: True or False?
True (0.5097643762740132)
Ermina Glandon has mean: True or False?
True (0.875361437979977)
Ermina Glandon has motive: True or False?
True (0.5983121871760707)
Ermina Glandon has opportunity: True or False?
False (0.64779823427608)
George Adams is guilty: True or False?
True (0.644225125126315)
George Adams has mean: True or False?
True (0.8745065279415651)
George Adams has motive: True or False?
True (0.7233094544266295)
George Adams has opportunity: True or False?
False (0.5243946167262008)
Matthew O'Leary is guilty: True or False?
True (0.5467381591701916)
Matthew O'Leary has mean: True or False?
True (0.9543079730970608)
Matthew O'Leary has motive: True or False?
True (0.6224592927728324)
Matthew O'Leary has opportunity: True or False?
True (0.8050197941712954)
Prince Rahim is guilty: True or False?
True (0.6531268925247615)
Prince Rahim has mean: True or False?
True (0.6680145240815963)
Prince Rahim has motive: True or False?
True (0.5583270361921496)
Prince Rahim has opportunity: True or False?
False (0.6397360437814448)
Ronald Reagan is guilty: True or False?
True (0.644225125126315)
Ronald Reagan has mean: True or False?
True (0.8966140749572745)
Ronald Reagan has motive: True or False?
True (0.5204963206682631)
Ronald Reagan has opportunity: True or False?
True (0.5612147992901458)
### Ermina Glandon
- mean: False (0.12463856202002299)
- motive: False (0.4016878128239293)
- opportunity: False (0.64779823427608)

### George Adams
- mean: False (0.12549347205843486)
- motive: False (0.27669054557337047)
- opportunity: False (0.5243946167262008)

### Matthew O'Leary
- mean: True (0.9543079730970608)
- motive: True (0.6224592927728324)
- opportunity: True (0.8050197941712954)

### Prince Rahim
- mean: False (0.33198547591840366)
- motive: False (0.44167296380785037)
- opportunity: False (0.6397360437814448)

### Ronald Reagan
- mean: False (0.10338592504272548)
- motive: False (0.4795036793317369)
- opportunity: False (0.43878520070985416)

The culprit is Matthew O'Leary.
In fact, it is Ronald Reagan.
## 5minutemystery-a-straw-stuffed-mystery
Bill Albertson is guilty: True or False?
True (0.6513548405484016)
Bill Albertson has mean: True or False?
True (0.5832033352502285)
Bill Albertson has motive: True or False?
True (0.8688267468984366)
Bill Albertson has opportunity: True or False?
True (0.5563995964631269)
Mr. Fletcher is guilty: True or False?
True (0.5888891620166576)
Mr. Fletcher has mean: True or False?
False (0.642432441257838)
Mr. Fletcher has motive: True or False?
True (0.769080279275001)
Mr. Fletcher has opportunity: True or False?
True (0.6522414018725713)
Professor Surenie is guilty: True or False?
True (0.5936093435000638)
Professor Surenie has mean: True or False?
False (0.5917232019857303)
Professor Surenie has motive: True or False?
True (0.8227595062673136)
Professor Surenie has opportunity: True or False?
False (0.5204963206682631)
Rachel Beaton is guilty: True or False?
False (0.5058591351869154)
Rachel Beaton has mean: True or False?
True (0.525368812147771)
Rachel Beaton has motive: True or False?
True (0.7170118721569225)
Rachel Beaton has opportunity: True or False?
False (0.6774740084332073)
### Bill Albertson
- mean: True (0.5832033352502285)
- motive: True (0.8688267468984366)
- opportunity: True (0.5563995964631269)

### Mr. Fletcher
- mean: False (0.642432441257838)
- motive: False (0.230919720724999)
- opportunity: False (0.3477585981274287)

### Professor Surenie
- mean: False (0.5917232019857303)
- motive: False (0.17724049373268635)
- opportunity: False (0.5204963206682631)

### Rachel Beaton
- mean: False (0.474631187852229)
- motive: False (0.2829881278430775)
- opportunity: False (0.6774740084332073)

The culprit is Bill Albertson.
In fact, it is Mr. Fletcher.
## 5minutemystery-ask-marthathe-shoplifter
Jane Croydon is guilty: True or False?
True (0.8019357965963964)
Jane Croydon has mean: True or False?
True (0.7310585348819939)
Jane Croydon has motive: True or False?
True (0.770464837675413)
Jane Croydon has opportunity: True or False?
False (0.5631377056275331)
Johnny Martin is guilty: True or False?
True (0.9024378096057211)
Johnny Martin has mean: True or False?
True (0.7826625131049049)
Johnny Martin has motive: True or False?
True (0.8526903338256402)
Johnny Martin has opportunity: True or False?
True (0.816406362162552)
Martha Hampden is guilty: True or False?
True (0.776283919986686)
Martha Hampden has mean: True or False?
True (0.7648916137833577)
Martha Hampden has motive: True or False?
True (0.6719012932095527)
Martha Hampden has opportunity: True or False?
False (0.5248817856312722)
Map:  59%|█████▊    | 119/203 [51:31<38:24, 27.44s/ examples]Map:  59%|█████▉    | 120/203 [51:54<36:07, 26.12s/ examples]Map:  60%|█████▉    | 121/203 [52:18<34:54, 25.54s/ examples]Map:  60%|██████    | 122/203 [52:40<33:08, 24.54s/ examples]Map:  61%|██████    | 123/203 [53:04<32:09, 24.12s/ examples]Steve Kravitz is guilty: True or False?
True (0.8774768149941248)
Steve Kravitz has mean: True or False?
True (0.64779823427608)
Steve Kravitz has motive: True or False?
True (0.7869504648517817)
Steve Kravitz has opportunity: True or False?
True (0.5278033071427191)
### Jane Croydon
- mean: False (0.2689414651180061)
- motive: False (0.22953516232458704)
- opportunity: False (0.5631377056275331)

### Johnny Martin
- mean: True (0.7826625131049049)
- motive: True (0.8526903338256402)
- opportunity: True (0.816406362162552)

### Martha Hampden
- mean: False (0.23510838621664232)
- motive: False (0.3280987067904473)
- opportunity: False (0.5248817856312722)

### Steve Kravitz
- mean: False (0.35220176572392004)
- motive: False (0.21304953514821834)
- opportunity: False (0.47219669285728094)

The culprit is Johnny Martin.
In fact, it is Johnny Martin.
## 5minutemystery-the-hanging-figure
Daisy Morris is guilty: True or False?
True (0.6627964974378784)
Daisy Morris has mean: True or False?
True (0.5477060677900649)
Daisy Morris has motive: True or False?
True (0.7248703250005105)
Daisy Morris has opportunity: True or False?
True (0.5214711377329961)
Dale Clark is guilty: True or False?
True (0.6334102859975052)
Dale Clark has mean: True or False?
True (0.8615382357584752)
Dale Clark has motive: True or False?
True (0.65489470935198)
Dale Clark has opportunity: True or False?
False (0.5224457875179084)
Iain Potts is guilty: True or False?
True (0.5583270361921496)
Iain Potts has mean: True or False?
True (0.8255897087847518)
Iain Potts has motive: True or False?
True (0.7648916137833577)
Iain Potts has opportunity: True or False?
False (0.5917232019857303)
Lucy Smith is guilty: True or False?
True (0.740174341079517)
Lucy Smith has mean: True or False?
True (0.7745833916423246)
Lucy Smith has motive: True or False?
True (0.7872777601997338)
Lucy Smith has opportunity: True or False?
True (0.5535053004623279)
### Daisy Morris
- mean: False (0.4522939322099351)
- motive: False (0.2751296749994895)
- opportunity: False (0.47852886226700386)

### Dale Clark
- mean: False (0.1384617642415248)
- motive: False (0.34510529064802)
- opportunity: False (0.5224457875179084)

### Iain Potts
- mean: False (0.1744102912152482)
- motive: False (0.23510838621664232)
- opportunity: False (0.5917232019857303)

### Lucy Smith
- mean: True (0.7745833916423246)
- motive: True (0.7872777601997338)
- opportunity: True (0.5535053004623279)

The culprit is Lucy Smith.
In fact, it is Dale Clark.
## 5minutemystery-our-quarterback-is-missing
Coach Roster is guilty: True or False?
True (0.8338664756137771)
Coach Roster has mean: True or False?
True (0.7386690294153369)
Coach Roster has motive: True or False?
True (0.8037906314112822)
Coach Roster has opportunity: True or False?
True (0.7356416476869558)
Eddie is guilty: True or False?
True (0.6206215556999736)
Eddie has mean: True or False?
False (0.5039061393777357)
Eddie has motive: True or False?
False (0.615087855649269)
Eddie has opportunity: True or False?
False (0.570809902165233)
Eddie's Mom is guilty: True or False?
True (0.791821116278941)
Eddie's Mom has mean: True or False?
False (0.6215409675616889)
Eddie's Mom has motive: True or False?
True (0.7937461674149602)
Eddie's Mom has opportunity: True or False?
False (0.5204963206682631)
Marissa is guilty: True or False?
True (0.6141626144170799)
Marissa has mean: True or False?
False (0.5117165908639297)
Marissa has motive: True or False?
False (0.591723272524637)
Marissa has opportunity: True or False?
False (0.6654105193867614)
### Coach Roster
- mean: True (0.7386690294153369)
- motive: True (0.8037906314112822)
- opportunity: True (0.7356416476869558)

### Eddie
- mean: False (0.5039061393777357)
- motive: False (0.615087855649269)
- opportunity: False (0.570809902165233)

### Eddie's Mom
- mean: False (0.6215409675616889)
- motive: False (0.20625383258503982)
- opportunity: False (0.5204963206682631)

### Marissa
- mean: False (0.5117165908639297)
- motive: False (0.591723272524637)
- opportunity: False (0.6654105193867614)

The culprit is Coach Roster.
In fact, it is Eddie's Mom.
## 5minutemystery-ask-marthathe-case-of-the-missing-canary
Alex Johnston is guilty: True or False?
True (0.591723272524637)
Alex Johnston has mean: True or False?
True (0.5926666351772785)
Alex Johnston has motive: True or False?
True (0.7599387683150569)
Alex Johnston has opportunity: True or False?
True (0.5583269696343842)
Jimmy Carstairs is guilty: True or False?
True (0.5360699771890155)
Jimmy Carstairs has mean: True or False?
True (0.7962924261546153)
Jimmy Carstairs has motive: True or False?
True (0.7325918709325988)
Jimmy Carstairs has opportunity: True or False?
True (0.6379335503198971)
Lydia Carstairs is guilty: True or False?
False (0.5068355091660127)
Lydia Carstairs has mean: True or False?
True (0.6619228707202935)
Lydia Carstairs has motive: True or False?
True (0.7082125449089324)
Lydia Carstairs has opportunity: True or False?
True (0.5708098341193941)
Sarabelle is guilty: True or False?
True (0.6671476389322356)
Sarabelle has mean: True or False?
True (0.6893056096647525)
Sarabelle has motive: True or False?
True (0.8294920340613177)
Sarabelle has opportunity: True or False?
True (0.5869964306477841)
### Alex Johnston
- mean: False (0.40733336482272153)
- motive: False (0.2400612316849431)
- opportunity: False (0.4416730303656158)

### Jimmy Carstairs
- mean: True (0.7962924261546153)
- motive: True (0.7325918709325988)
- opportunity: True (0.6379335503198971)

### Lydia Carstairs
- mean: False (0.33807712927970646)
- motive: False (0.2917874550910676)
- opportunity: False (0.4291901658806059)

### Sarabelle
- mean: False (0.3106943903352475)
- motive: False (0.17050796593868234)
- opportunity: False (0.41300356935221594)

The culprit is Jimmy Carstairs.
In fact, it is Alex Johnston.
## 5minutemystery-register-robbery
Dan is guilty: True or False?
True (0.7969253675907205)
Dan has mean: True or False?
True (0.7146279861809854)
Dan has motive: True or False?
True (0.7839884107482739)
Dan has opportunity: True or False?
True (0.5360700410935405)
David is guilty: True or False?
True (0.7793217912837537)
David has mean: True or False?
True (0.7033457082786769)
David has motive: True or False?
True (0.784649255215384)
David has opportunity: True or False?
True (0.5822535180679596)
Robert is guilty: True or False?
True (0.8740772044235984)
Robert has mean: True or False?
True (0.7409249450892966)
Robert has motive: True or False?
True (0.8727816933272936)
Robert has opportunity: True or False?
True (0.6531268925247615)
Teresa is guilty: True or False?
True (0.7527403228571042)
Teresa has mean: True or False?
True (0.6522414018725713)
Teresa has motive: True or False?
True (0.8606036289596553)
Teresa has opportunity: True or False?
True (0.5418937216067536)
### Dan
- mean: False (0.28537201381901456)
- motive: False (0.21601158925172614)
- opportunity: False (0.4639299589064595)

### David
- mean: False (0.29665429172132307)
- motive: False (0.21535074478461602)
- opportunity: False (0.41774648193204045)

### Robert
- mean: True (0.7409249450892966)
- motive: True (0.8727816933272936)
- opportunity: True (0.6531268925247615)

### Teresa
- mean: False (0.3477585981274287)
- motive: False (0.13939637104034475)
- opportunity: False (0.45810627839324636)

The culprit is Robert.
In fact, it is David.
## 5minutemystery-mr-patrick-back-in-class
CSA currency is guilty: True or False?
True (0.8723473540228537)
CSA currency has mean: True or False?
True (0.9029524325377104)
CSA currency has motive: True or False?
True (0.8745065279415651)
CSA currency has opportunity: True or False?
True (0.8370879250561812)
Diamond necklace is guilty: True or False?
True (0.6001883860246252)
Diamond necklace has mean: True or False?
True (0.7662936378892937)
Diamond necklace has motive: True or False?
True (0.6592954931819778)
Diamond necklace has opportunity: True or False?
True (0.5234203246639862)
Gold money clip is guilty: True or False?
True (0.8134607635851566)
Gold money clip has mean: True or False?
True (0.8504686406728537)
Gold money clip has motive: True or False?
Map:  61%|██████    | 124/203 [53:43<37:53, 28.78s/ examples]Map:  62%|██████▏   | 125/203 [54:12<37:24, 28.77s/ examples]Map:  62%|██████▏   | 126/203 [54:45<38:27, 29.96s/ examples]Map:  63%|██████▎   | 127/203 [55:19<39:37, 31.28s/ examples]True (0.7356416476869558)
Gold money clip has opportunity: True or False?
True (0.6757646168022439)
Jewel encrusted pistol is guilty: True or False?
True (0.7520125537161032)
Jewel encrusted pistol has mean: True or False?
True (0.7490872087035162)
Jewel encrusted pistol has motive: True or False?
True (0.7461389980806673)
Jewel encrusted pistol has opportunity: True or False?
True (0.6800292740030767)
Lithograph photo is guilty: True or False?
True (0.7534666630720156)
Lithograph photo has mean: True or False?
True (0.8349459127213729)
Lithograph photo has motive: True or False?
True (0.7585105966624085)
Lithograph photo has opportunity: True or False?
True (0.7826625131049049)
### CSA currency
- mean: True (0.9029524325377104)
- motive: True (0.8745065279415651)
- opportunity: True (0.8370879250561812)

### Diamond necklace
- mean: False (0.23370636211070628)
- motive: False (0.3407045068180222)
- opportunity: False (0.47657967533601375)

### Gold money clip
- mean: False (0.14953135932714634)
- motive: False (0.26435835231304416)
- opportunity: False (0.32423538319775613)

### Jewel encrusted pistol
- mean: False (0.2509127912964838)
- motive: False (0.2538610019193327)
- opportunity: False (0.31997072599692333)

### Lithograph photo
- mean: False (0.16505408727862714)
- motive: False (0.2414894033375915)
- opportunity: False (0.21733748689509513)

The culprit is CSA currency.
In fact, it is Lithograph photo.
## 5minutemystery-ask-marthathe-blackmailer
Horace Sage is guilty: True or False?
True (0.9010534302227574)
Horace Sage has mean: True or False?
True (0.7806624796117883)
Horace Sage has motive: True or False?
True (0.900179384114949)
Horace Sage has opportunity: True or False?
True (0.7742421642081551)
Martin Amberton is guilty: True or False?
True (0.8812066389307215)
Martin Amberton has mean: True or False?
True (0.8095772283237919)
Martin Amberton has motive: True or False?
True (0.8107787408238168)
Martin Amberton has opportunity: True or False?
True (0.8185918283825985)
Mary Devers is guilty: True or False?
True (0.6169357925086439)
Mary Devers has mean: True or False?
True (0.7146280500737092)
Mary Devers has motive: True or False?
True (0.591723272524637)
Mary Devers has opportunity: True or False?
True (0.5765419579552815)
Susan Royster is guilty: True or False?
True (0.8074606715677252)
Susan Royster has mean: True or False?
True (0.9017477662022706)
Susan Royster has motive: True or False?
True (0.7424217332471881)
Susan Royster has opportunity: True or False?
True (0.729905005312225)
### Horace Sage
- mean: True (0.7806624796117883)
- motive: True (0.900179384114949)
- opportunity: True (0.7742421642081551)

### Martin Amberton
- mean: False (0.19042277167620814)
- motive: False (0.18922125917618315)
- opportunity: False (0.18140817161740153)

### Mary Devers
- mean: False (0.2853719499262908)
- motive: False (0.40827672747536303)
- opportunity: False (0.4234580420447185)

### Susan Royster
- mean: False (0.0982522337977294)
- motive: False (0.2575782667528119)
- opportunity: False (0.270094994687775)

The culprit is Horace Sage.
In fact, it is Mary Devers.
## 5minutemystery-a-dream-of-old-salem
Abigail Thorpe is guilty: True or False?
True (0.8670357473609658)
Abigail Thorpe has mean: True or False?
True (0.8068526417769779)
Abigail Thorpe has motive: True or False?
True (0.7728736896481636)
Abigail Thorpe has opportunity: True or False?
True (0.5983121871760707)
Adam Browne is guilty: True or False?
True (0.8418256009501243)
Adam Browne has mean: True or False?
True (0.7676898810056793)
Adam Browne has motive: True or False?
True (0.7989721855047863)
Adam Browne has opportunity: True or False?
True (0.7680379714749807)
Goodwife Browne is guilty: True or False?
True (0.8615382357584752)
Goodwife Browne has mean: True or False?
True (0.8933093589621482)
Goodwife Browne has motive: True or False?
True (0.8596637847360897)
Goodwife Browne has opportunity: True or False?
True (0.8785228180531032)
Sarah Goodwin is guilty: True or False?
True (0.5717666110200305)
Sarah Goodwin has mean: True or False?
True (0.8305940642606888)
Sarah Goodwin has motive: True or False?
True (0.7382918489137783)
Sarah Goodwin has opportunity: True or False?
True (0.525368812147771)
### Abigail Thorpe
- mean: False (0.1931473582230221)
- motive: False (0.2271263103518364)
- opportunity: False (0.4016878128239293)

### Adam Browne
- mean: False (0.23231011899432075)
- motive: False (0.20102781449521367)
- opportunity: False (0.23196202852501935)

### Goodwife Browne
- mean: True (0.8933093589621482)
- motive: True (0.8596637847360897)
- opportunity: True (0.8785228180531032)

### Sarah Goodwin
- mean: False (0.16940593573931118)
- motive: False (0.2617081510862217)
- opportunity: False (0.474631187852229)

The culprit is Goodwife Browne.
In fact, it is Adam Browne.
## 5minutemystery-the-antique-clock-mystery
The grandfather clock (stopped at 10:10 p.m.) is guilty: True or False?
True (0.6279512069990912)
The grandfather clock (stopped at 10:10 p.m.) has mean: True or False?
True (0.8283841584202847)
The grandfather clock (stopped at 10:10 p.m.) has motive: True or False?
True (0.878314250659373)
The grandfather clock (stopped at 10:10 p.m.) has opportunity: True or False?
True (0.8140528237853677)
The mantle clock (stopped at 10:59 p.m.) is guilty: True or False?
True (0.6757646168022439)
The mantle clock (stopped at 10:59 p.m.) has mean: True or False?
True (0.7333563569098757)
The mantle clock (stopped at 10:59 p.m.) has motive: True or False?
True (0.8019358443954961)
The mantle clock (stopped at 10:59 p.m.) has opportunity: True or False?
True (0.7859664553110391)
The pocket watch (stopped at 3:18 a.m.) is guilty: True or False?
True (0.6926419789019715)
The pocket watch (stopped at 3:18 a.m.) has mean: True or False?
True (0.874934615163517)
The pocket watch (stopped at 3:18 a.m.) has motive: True or False?
True (0.844921525814193)
The pocket watch (stopped at 3:18 a.m.) has opportunity: True or False?
True (0.854884620116169)
The wall clock (stopped at 2:01 a.m.) is guilty: True or False?
True (0.7098243920264812)
The wall clock (stopped at 2:01 a.m.) has mean: True or False?
True (0.7620701143808404)
The wall clock (stopped at 2:01 a.m.) has motive: True or False?
True (0.8489722037469682)
The wall clock (stopped at 2:01 a.m.) has opportunity: True or False?
True (0.8278281666221954)
The wristwatch (stopped at 5:22 p.m.) is guilty: True or False?
True (0.5224458497983033)
The wristwatch (stopped at 5:22 p.m.) has mean: True or False?
True (0.784649255215384)
The wristwatch (stopped at 5:22 p.m.) has motive: True or False?
True (0.7264255794048772)
The wristwatch (stopped at 5:22 p.m.) has opportunity: True or False?
True (0.7325918709325988)
### The grandfather clock (stopped at 10:10 p.m.)
- mean: False (0.17161584157971532)
- motive: False (0.12168574934062704)
- opportunity: False (0.1859471762146323)

### The mantle clock (stopped at 10:59 p.m.)
- mean: False (0.26664364309012434)
- motive: False (0.19806415560450386)
- opportunity: False (0.21403354468896085)

### The pocket watch (stopped at 3:18 a.m.)
- mean: True (0.874934615163517)
- motive: True (0.844921525814193)
- opportunity: True (0.854884620116169)

### The wall clock (stopped at 2:01 a.m.)
- mean: False (0.23792988561915962)
- motive: False (0.15102779625303175)
- opportunity: False (0.17217183337780462)

### The wristwatch (stopped at 5:22 p.m.)
- mean: False (0.21535074478461602)
- motive: False (0.2735744205951228)
- opportunity: False (0.2674081290674012)

The culprit is The pocket watch (stopped at 3:18 a.m.).
In fact, it is The mantle clock (stopped at 10:59 p.m.).
## 5minutemystery-ask-marthathe-perjurer
Horace Osamway is guilty: True or False?
True (0.9472835653937188)
Horace Osamway has mean: True or False?
True (0.8140527631337082)
Horace Osamway has motive: True or False?
True (0.8770562402180104)
Horace Osamway has opportunity: True or False?
True (0.8253083182831968)
John Eberley is guilty: True or False?
True (0.9122799654606127)
John Eberley has mean: True or False?
True (0.8370879250561812)
John Eberley has motive: True or False?
Map:  63%|██████▎   | 128/203 [55:52<39:44, 31.79s/ examples]Map:  64%|██████▎   | 129/203 [56:25<39:39, 32.15s/ examples]Map:  64%|██████▍   | 130/203 [56:49<36:04, 29.65s/ examples]Map:  65%|██████▍   | 131/203 [57:22<36:48, 30.68s/ examples]Map:  65%|██████▌   | 132/203 [57:47<34:18, 28.99s/ examples]True (0.8101787517928931)
John Eberley has opportunity: True or False?
True (0.6693127155643409)
Martha Cranston is guilty: True or False?
True (0.8213309048233545)
Martha Cranston has mean: True or False?
True (0.7505527730327083)
Martha Cranston has motive: True or False?
True (0.6256667878365441)
Martha Cranston has opportunity: True or False?
True (0.5907791930117218)
Mildred Greene is guilty: True or False?
True (0.8887587777822111)
Mildred Greene has mean: True or False?
True (0.7879311977554747)
Mildred Greene has motive: True or False?
True (0.7225270177274575)
Mildred Greene has opportunity: True or False?
True (0.7786493288700866)
### Horace Osamway
- mean: True (0.8140527631337082)
- motive: True (0.8770562402180104)
- opportunity: True (0.8253083182831968)

### John Eberley
- mean: False (0.16291207494381876)
- motive: False (0.18982124820710689)
- opportunity: False (0.3306872844356591)

### Martha Cranston
- mean: False (0.2494472269672917)
- motive: False (0.37433321216345594)
- opportunity: False (0.40922080698827823)

### Mildred Greene
- mean: False (0.2120688022445253)
- motive: False (0.27747298227254247)
- opportunity: False (0.22135067112991336)

The culprit is Horace Osamway.
In fact, it is John Eberley.
## 5minutemystery-ask-marthathe-embezzler
Joan Carstairs is guilty: True or False?
True (0.8647679660788636)
Joan Carstairs has mean: True or False?
True (0.84440905415483)
Joan Carstairs has motive: True or False?
True (0.8778961263000082)
Joan Carstairs has opportunity: True or False?
True (0.8426043397677332)
Les Nolting is guilty: True or False?
True (0.8591918406281239)
Les Nolting has mean: True or False?
True (0.8795611817678315)
Les Nolting has motive: True or False?
True (0.8665847814067802)
Les Nolting has opportunity: True or False?
True (0.8051730422074252)
Paul Brassard is guilty: True or False?
True (0.908941745727715)
Paul Brassard has mean: True or False?
True (0.9074763054739992)
Paul Brassard has motive: True or False?
True (0.8819203351368529)
Paul Brassard has opportunity: True or False?
True (0.7796575431744809)
Sarah Kimble is guilty: True or False?
True (0.8056321690561029)
Sarah Kimble has mean: True or False?
True (0.8980535302052036)
Sarah Kimble has motive: True or False?
True (0.8994751578343994)
Sarah Kimble has opportunity: True or False?
True (0.7966091010940959)
### Joan Carstairs
- mean: False (0.15559094584516997)
- motive: False (0.12210387369999176)
- opportunity: False (0.1573956602322668)

### Les Nolting
- mean: False (0.12043881823216851)
- motive: False (0.1334152185932198)
- opportunity: False (0.19482695779257475)

### Paul Brassard
- mean: False (0.09252369452600084)
- motive: False (0.11807966486314714)
- opportunity: False (0.22034245682551912)

### Sarah Kimble
- mean: True (0.8980535302052036)
- motive: True (0.8994751578343994)
- opportunity: True (0.7966091010940959)

The culprit is Sarah Kimble.
In fact, it is Sarah Kimble.
## 5minutemystery-the-backyard-slumber-party
Justin Scott is guilty: True or False?
True (0.8316905440184192)
Justin Scott has mean: True or False?
True (0.8710367026584496)
Justin Scott has motive: True or False?
True (0.7950222460539826)
Justin Scott has opportunity: True or False?
True (0.6315943123389512)
Martin Simmons is guilty: True or False?
True (0.7859664553110391)
Martin Simmons has mean: True or False?
True (0.6141626144170799)
Martin Simmons has motive: True or False?
True (0.6934729182490079)
Martin Simmons has opportunity: True or False?
False (0.6627964381792564)
Stephen Kennelly is guilty: True or False?
True (0.621540893468236)
Stephen Kennelly has mean: True or False?
False (0.5039061393777357)
Stephen Kennelly has motive: True or False?
True (0.6749080895533367)
Stephen Kennelly has opportunity: True or False?
False (0.7446563307563252)
Trevor Sutherland is guilty: True or False?
True (0.5360700410935405)
Trevor Sutherland has mean: True or False?
True (0.5312093941731293)
Trevor Sutherland has motive: True or False?
True (0.642432441257838)
Trevor Sutherland has opportunity: True or False?
False (0.6592954931819778)
### Justin Scott
- mean: True (0.8710367026584496)
- motive: True (0.7950222460539826)
- opportunity: True (0.6315943123389512)

### Martin Simmons
- mean: False (0.38583738558292013)
- motive: False (0.3065270817509921)
- opportunity: False (0.6627964381792564)

### Stephen Kennelly
- mean: False (0.5039061393777357)
- motive: False (0.3250919104466633)
- opportunity: False (0.7446563307563252)

### Trevor Sutherland
- mean: False (0.4687906058268707)
- motive: False (0.35756755874216195)
- opportunity: False (0.6592954931819778)

The culprit is Justin Scott.
In fact, it is Trevor Sutherland.
## 5minutemystery-the-rock-star-mystery
Gorg is guilty: True or False?
True (0.944176853162527)
Gorg has mean: True or False?
True (0.9399133323582882)
Gorg has motive: True or False?
True (0.9752960797421999)
Gorg has opportunity: True or False?
True (0.9252299038987163)
Stu is guilty: True or False?
True (0.8587185689177256)
Stu has mean: True or False?
True (0.7937461674149602)
Stu has motive: True or False?
True (0.8341368378998062)
Stu has opportunity: True or False?
True (0.5983121871760707)
The Neighborhood Burgler is guilty: True or False?
True (0.942081869103903)
The Neighborhood Burgler has mean: True or False?
True (0.941654147692963)
The Neighborhood Burgler has motive: True or False?
True (0.9442796704001448)
The Neighborhood Burgler has opportunity: True or False?
True (0.9095862487848758)
Tina is guilty: True or False?
True (0.8504685773080045)
Tina has mean: True or False?
True (0.8723474190177988)
Tina has motive: True or False?
True (0.8610715240899957)
Tina has opportunity: True or False?
True (0.7318258918270596)
### Gorg
- mean: True (0.9399133323582882)
- motive: True (0.9752960797421999)
- opportunity: True (0.9252299038987163)

### Stu
- mean: False (0.20625383258503982)
- motive: False (0.1658631621001938)
- opportunity: False (0.4016878128239293)

### The Neighborhood Burgler
- mean: False (0.05834585230703704)
- motive: False (0.05572032959985518)
- opportunity: False (0.09041375121512418)

### Tina
- mean: False (0.12765258098220122)
- motive: False (0.13892847591000435)
- opportunity: False (0.2681741081729404)

The culprit is Gorg.
In fact, it is Tina.
## 5minutemystery-ask-marthathe-arsonist
Keen Observer is guilty: True or False?
True (0.5784481782924303)
Keen Observer has mean: True or False?
True (0.9193533657123177)
Keen Observer has motive: True or False?
True (0.6959583025067009)
Keen Observer has opportunity: True or False?
True (0.6901415551283886)
Minding My Own Business is guilty: True or False?
True (0.6297746298200823)
Minding My Own Business has mean: True or False?
True (0.981944620412271)
Minding My Own Business has motive: True or False?
True (0.5765420266844429)
Minding My Own Business has opportunity: True or False?
True (0.7786493288700866)
Scared Stiff is guilty: True or False?
True (0.6197015092684077)
Scared Stiff has mean: True or False?
True (0.9076402191395381)
Scared Stiff has motive: True or False?
True (0.621540893468236)
Scared Stiff has opportunity: True or False?
True (0.7000752133823226)
Watchful Waiter is guilty: True or False?
True (0.6104534962074417)
Watchful Waiter has mean: True or False?
True (0.9314625284362855)
Watchful Waiter has motive: True or False?
True (0.6731917300802632)
Watchful Waiter has opportunity: True or False?
True (0.7341195403199204)
### Keen Observer
- mean: False (0.08064663428768226)
- motive: False (0.3040416974932991)
- opportunity: False (0.3098584448716114)

### Minding My Own Business
- mean: True (0.981944620412271)
- motive: True (0.5765420266844429)
- opportunity: True (0.7786493288700866)

### Scared Stiff
- mean: False (0.09235978086046193)
- motive: False (0.37845910653176396)
- opportunity: False (0.2999247866176774)

### Watchful Waiter
- mean: False (0.06853747156371448)
- motive: False (0.32680826991973677)
- opportunity: False (0.26588045968007956)

The culprit is Minding My Own Business.
In fact, it is Watchful Waiter.
## 5minutemystery-fatal-computer-crash
Alex Redoff is guilty: True or False?
Map:  66%|██████▌   | 133/203 [58:17<34:16, 29.38s/ examples]Map:  66%|██████▌   | 134/203 [58:47<34:00, 29.57s/ examples]Map:  67%|██████▋   | 135/203 [59:13<32:03, 28.28s/ examples]Map:  67%|██████▋   | 136/203 [59:39<31:02, 27.80s/ examples]True (0.9099070446252667)
Alex Redoff has mean: True or False?
True (0.7248703250005105)
Alex Redoff has motive: True or False?
True (0.7483522884503825)
Alex Redoff has opportunity: True or False?
True (0.7570766705324253)
Cheryl Compton is guilty: True or False?
True (0.842345065078002)
Cheryl Compton has mean: True or False?
True (0.8807970862580315)
Cheryl Compton has motive: True or False?
True (0.7074046739492601)
Cheryl Compton has opportunity: True or False?
True (0.720171518230031)
Claire Denninger is guilty: True or False?
True (0.8661325012437474)
Claire Denninger has mean: True or False?
True (0.9022656660556747)
Claire Denninger has motive: True or False?
True (0.8381505623254643)
Claire Denninger has opportunity: True or False?
True (0.7669924589170153)
Natalie Sampson is guilty: True or False?
True (0.776622945813876)
Natalie Sampson has mean: True or False?
True (0.7468781997658912)
Natalie Sampson has motive: True or False?
True (0.6575384105121485)
Natalie Sampson has opportunity: True or False?
True (0.5765419579552815)
### Alex Redoff
- mean: False (0.2751296749994895)
- motive: False (0.2516477115496175)
- opportunity: False (0.24292332946757467)

### Cheryl Compton
- mean: False (0.11920291374196845)
- motive: False (0.2925953260507399)
- opportunity: False (0.279828481769969)

### Claire Denninger
- mean: True (0.9022656660556747)
- motive: True (0.8381505623254643)
- opportunity: True (0.7669924589170153)

### Natalie Sampson
- mean: False (0.2531218002341088)
- motive: False (0.34246158948785155)
- opportunity: False (0.4234580420447185)

The culprit is Claire Denninger.
In fact, it is Natalie Sampson.
## 5minutemystery-the-rob-club-murder-mystery
Al Gibson is guilty: True or False?
True (0.9029524325377104)
Al Gibson has mean: True or False?
True (0.9429286143036572)
Al Gibson has motive: True or False?
True (0.9205042693180057)
Al Gibson has opportunity: True or False?
True (0.8582439976623328)
Johnny Woodward is guilty: True or False?
True (0.9076402191395381)
Johnny Woodward has mean: True or False?
True (0.9518632280135741)
Johnny Woodward has motive: True or False?
True (0.9511422515416323)
Johnny Woodward has opportunity: True or False?
True (0.9401335713518422)
Ray Shields is guilty: True or False?
True (0.7931059536445917)
Ray Shields has mean: True or False?
True (0.8175744430556572)
Ray Shields has motive: True or False?
True (0.8056321690561029)
Ray Shields has opportunity: True or False?
True (0.8006919661398397)
Tim Acord is guilty: True or False?
True (0.7745833916423246)
Tim Acord has mean: True or False?
True (0.9019206778000431)
Tim Acord has motive: True or False?
True (0.8193157928301305)
Tim Acord has opportunity: True or False?
True (0.7975568155246964)
Watson Treadway is guilty: True or False?
True (0.8596637206861489)
Watson Treadway has mean: True or False?
True (0.8799743689174987)
Watson Treadway has motive: True or False?
True (0.8962513815714083)
Watson Treadway has opportunity: True or False?
True (0.9155072008980665)
### Al Gibson
- mean: False (0.05707138569634285)
- motive: False (0.07949573068199434)
- opportunity: False (0.14175600233766716)

### Johnny Woodward
- mean: True (0.9518632280135741)
- motive: True (0.9511422515416323)
- opportunity: True (0.9401335713518422)

### Ray Shields
- mean: False (0.18242555694434281)
- motive: False (0.1943678309438971)
- opportunity: False (0.19930803386016027)

### Tim Acord
- mean: False (0.09807932219995685)
- motive: False (0.18068420716986955)
- opportunity: False (0.20244318447530363)

### Watson Treadway
- mean: False (0.1200256310825013)
- motive: False (0.10374861842859173)
- opportunity: False (0.08449279910193352)

The culprit is Johnny Woodward.
In fact, it is Johnny Woodward.
## 5minutemystery-ask-marthathe-litterer
Concerned Neighbor is guilty: True or False?
True (0.6486889055472267)
Concerned Neighbor has mean: True or False?
True (0.9238675252821831)
Concerned Neighbor has motive: True or False?
True (0.8333246107254184)
Concerned Neighbor has opportunity: True or False?
True (0.7697732451157533)
Confused Commuter is guilty: True or False?
True (0.7711548682745724)
Confused Commuter has mean: True or False?
True (0.9435559526996434)
Confused Commuter has motive: True or False?
True (0.8187367896794966)
Confused Commuter has opportunity: True or False?
True (0.6379334932841956)
Perplexed Dog Walker is guilty: True or False?
True (0.7431679939957333)
Perplexed Dog Walker has mean: True or False?
True (0.9603611244019274)
Perplexed Dog Walker has motive: True or False?
True (0.8778961263000082)
Perplexed Dog Walker has opportunity: True or False?
True (0.7704647687904915)
Smug in Suburbia is guilty: True or False?
True (0.6817267588564826)
Smug in Suburbia has mean: True or False?
True (0.8745065279415651)
Smug in Suburbia has motive: True or False?
True (0.8418256009501243)
Smug in Suburbia has opportunity: True or False?
True (0.5214711377329961)
### Concerned Neighbor
- mean: False (0.07613247471781692)
- motive: False (0.1666753892745816)
- opportunity: False (0.2302267548842467)

### Confused Commuter
- mean: False (0.05644404730035657)
- motive: False (0.1812632103205034)
- opportunity: False (0.3620665067158044)

### Perplexed Dog Walker
- mean: True (0.9603611244019274)
- motive: True (0.8778961263000082)
- opportunity: True (0.7704647687904915)

### Smug in Suburbia
- mean: False (0.12549347205843486)
- motive: False (0.15817439904987574)
- opportunity: False (0.47852886226700386)

The culprit is Perplexed Dog Walker.
In fact, it is Smug in Suburbia.
## 5minutemystery-drama-queen
Alfred Cooper is guilty: True or False?
True (0.6252092625510083)
Alfred Cooper has mean: True or False?
True (0.7431679939957333)
Alfred Cooper has motive: True or False?
True (0.6918097672776748)
Alfred Cooper has opportunity: True or False?
True (0.525368812147771)
Isabelle Rogers is guilty: True or False?
True (0.6315943123389512)
Isabelle Rogers has mean: True or False?
True (0.6270381219830087)
Isabelle Rogers has motive: True or False?
True (0.6076632024562351)
Isabelle Rogers has opportunity: True or False?
False (0.7162185953247016)
James Fennimore is guilty: True or False?
True (0.5698526542706361)
James Fennimore has mean: True or False?
True (0.7739006258141444)
James Fennimore has motive: True or False?
True (0.7839884808423031)
James Fennimore has opportunity: True or False?
False (0.6893056096647525)
Madge Anderson is guilty: True or False?
True (0.5136684743338078)
Madge Anderson has mean: True or False?
True (0.6388353131709135)
Madge Anderson has motive: True or False?
True (0.5973730125048408)
Madge Anderson has opportunity: True or False?
False (0.7170118721569225)
### Alfred Cooper
- mean: True (0.7431679939957333)
- motive: True (0.6918097672776748)
- opportunity: True (0.525368812147771)

### Isabelle Rogers
- mean: False (0.3729618780169913)
- motive: False (0.39233679754376494)
- opportunity: False (0.7162185953247016)

### James Fennimore
- mean: False (0.22609937418585557)
- motive: False (0.2160115191576969)
- opportunity: False (0.6893056096647525)

### Madge Anderson
- mean: False (0.36116468682908653)
- motive: False (0.40262698749515924)
- opportunity: False (0.7170118721569225)

The culprit is Alfred Cooper.
In fact, it is James Fennimore.
## 5minutemystery-the-gourmet-mystery
Antoine is guilty: True or False?
True (0.8877896081343184)
Antoine has mean: True or False?
True (0.814643384779728)
Antoine has motive: True or False?
True (0.8519527857346616)
Antoine has opportunity: True or False?
True (0.6976089520497016)
Georges Monceau is guilty: True or False?
True (0.9391922928557355)
Georges Monceau has mean: True or False?
True (0.84619676525883)
Georges Monceau has motive: True or False?
True (0.8807970337584357)
Georges Monceau has opportunity: True or False?
True (0.795181328342443)
Sally Horvats is guilty: True or False?
True (0.9201462264331123)
Sally Horvats has mean: True or False?
True (0.8104789202520752)
Sally Horvats has motive: True or False?
True (0.9280183890155084)
Sally Horvats has opportunity: True or False?
True (0.7735586847891339)
Sam Wheeler is guilty: True or False?
Map:  67%|██████▋   | 137/203 [1:00:07<30:26, 27.67s/ examples]Map:  68%|██████▊   | 138/203 [1:00:42<32:28, 29.98s/ examples]Map:  68%|██████▊   | 139/203 [1:01:12<31:58, 29.97s/ examples]Map:  69%|██████▉   | 140/203 [1:01:40<30:53, 29.42s/ examples]Map:  69%|██████▉   | 141/203 [1:02:17<32:41, 31.64s/ examples]False (0.6390576676453745)
Sam Wheeler has mean: True or False?
True (0.7412996266976789)
Sam Wheeler has motive: True or False?
True (0.7325918054337844)
Sam Wheeler has opportunity: True or False?
True (0.615087855649269)
### Antoine
- mean: False (0.18535661522027203)
- motive: False (0.1480472142653384)
- opportunity: False (0.30239104795029836)

### Georges Monceau
- mean: True (0.84619676525883)
- motive: True (0.8807970337584357)
- opportunity: True (0.795181328342443)

### Sally Horvats
- mean: False (0.18952107974792476)
- motive: False (0.07198161098449163)
- opportunity: False (0.22644131521086608)

### Sam Wheeler
- mean: False (0.2587003733023211)
- motive: False (0.26740819456621556)
- opportunity: False (0.38491214435073096)

The culprit is Georges Monceau.
In fact, it is Sally Horvats.
## 5minutemystery-the-potter-book-mystery
Alfred is guilty: True or False?
True (0.9229003224709645)
Alfred has mean: True or False?
True (0.5107405249783342)
Alfred has motive: True or False?
True (0.8507168263103924)
Alfred has opportunity: True or False?
True (0.7520125537161032)
Ann is guilty: True or False?
True (0.8521990171094214)
Ann has mean: True or False?
True (0.7217432334405754)
Ann has motive: True or False?
True (0.884439109617765)
Ann has opportunity: True or False?
True (0.7694269364202454)
Rusty is guilty: True or False?
True (0.9165588616316169)
Rusty has mean: True or False?
True (0.8428631416381634)
Rusty has motive: True or False?
True (0.9430860272459268)
Rusty has opportunity: True or False?
True (0.878314250659373)
Uncle Ezra is guilty: True or False?
True (0.9545627850600183)
Uncle Ezra has mean: True or False?
True (0.8582439976623328)
Uncle Ezra has motive: True or False?
True (0.9171543708147702)
Uncle Ezra has opportunity: True or False?
True (0.9099069836112468)
### Alfred
- mean: False (0.4892594750216658)
- motive: False (0.14928317368960764)
- opportunity: False (0.2479874462838968)

### Ann
- mean: False (0.27825676655942455)
- motive: False (0.11556089038223505)
- opportunity: False (0.2305730635797546)

### Rusty
- mean: False (0.15713685836183655)
- motive: False (0.05691397275407317)
- opportunity: False (0.12168574934062704)

### Uncle Ezra
- mean: True (0.8582439976623328)
- motive: True (0.9171543708147702)
- opportunity: True (0.9099069836112468)

The culprit is Uncle Ezra.
In fact, it is Uncle Ezra.
## 5minutemystery-death-in-the-office
Cynthia Peck is guilty: True or False?
True (0.6926419789019715)
Cynthia Peck has mean: True or False?
True (0.8514594452543962)
Cynthia Peck has motive: True or False?
True (0.7648916137833577)
Cynthia Peck has opportunity: True or False?
True (0.6749081498948247)
Josh Kesler is guilty: True or False?
True (0.784649255215384)
Josh Kesler has mean: True or False?
True (0.7799928701983835)
Josh Kesler has motive: True or False?
True (0.7752646804088963)
Josh Kesler has opportunity: True or False?
True (0.6791787167336184)
Megan Brewer is guilty: True or False?
True (0.595492552580428)
Megan Brewer has mean: True or False?
True (0.64779823427608)
Megan Brewer has motive: True or False?
True (0.5399537164111071)
Megan Brewer has opportunity: True or False?
True (0.5087881523495457)
Steve Ledbetter is guilty: True or False?
True (0.7839884107482739)
Steve Ledbetter has mean: True or False?
True (0.9082930704920021)
Steve Ledbetter has motive: True or False?
True (0.6424325178417575)
Steve Ledbetter has opportunity: True or False?
True (0.591723272524637)
### Cynthia Peck
- mean: True (0.8514594452543962)
- motive: True (0.7648916137833577)
- opportunity: True (0.6749081498948247)

### Josh Kesler
- mean: False (0.22000712980161652)
- motive: False (0.2247353195911037)
- opportunity: False (0.3208212832663816)

### Megan Brewer
- mean: False (0.35220176572392004)
- motive: False (0.4600462835888929)
- opportunity: False (0.49121184765045434)

### Steve Ledbetter
- mean: False (0.09170692950799786)
- motive: False (0.3575674821582425)
- opportunity: False (0.40827672747536303)

The culprit is Cynthia Peck.
In fact, it is Megan Brewer.
## 5minutemystery-chief-inspector-japp-solves-a-case
Alan Harrison is guilty: True or False?
True (0.8438951328214825)
Alan Harrison has mean: True or False?
True (0.6067314814064781)
Alan Harrison has motive: True or False?
True (0.7704647687904915)
Alan Harrison has opportunity: True or False?
True (0.6934729802503211)
Evelyn Johnston is guilty: True or False?
True (0.7786493288700866)
Evelyn Johnston has mean: True or False?
True (0.5679366075542497)
Evelyn Johnston has motive: True or False?
True (0.5936092727363199)
Evelyn Johnston has opportunity: True or False?
True (0.6178585826183487)
George Smythe is guilty: True or False?
True (0.8852352523606669)
George Smythe has mean: True or False?
True (0.6242935781683038)
George Smythe has motive: True or False?
True (0.7302898278778687)
George Smythe has opportunity: True or False?
True (0.6783269591477166)
Herbert Grosvenor is guilty: True or False?
True (0.9173026661190045)
Herbert Grosvenor has mean: True or False?
True (0.5477060024984176)
Herbert Grosvenor has motive: True or False?
True (0.8098781635062345)
Herbert Grosvenor has opportunity: True or False?
True (0.7563574896543893)
### Alan Harrison
- mean: False (0.39326851859352185)
- motive: False (0.22953523120950847)
- opportunity: False (0.3065270197496789)

### Evelyn Johnston
- mean: False (0.4320633924457503)
- motive: False (0.4063907272636801)
- opportunity: False (0.3821414173816513)

### George Smythe
- mean: False (0.3757064218316962)
- motive: False (0.26971017212213133)
- opportunity: False (0.32167304085228343)

### Herbert Grosvenor
- mean: True (0.5477060024984176)
- motive: True (0.8098781635062345)
- opportunity: True (0.7563574896543893)

The culprit is Herbert Grosvenor.
In fact, it is Alan Harrison.
## 5minutemystery-who-stole-the-cavemans-dinner
Dinosaur is guilty: True or False?
True (0.8169911556077801)
Dinosaur has mean: True or False?
True (0.6370307821695329)
Dinosaur has motive: True or False?
True (0.89010334411601)
Dinosaur has opportunity: True or False?
True (0.6627964381792564)
Droo is guilty: True or False?
True (0.9247556906264367)
Droo has mean: True or False?
True (0.7994422859301654)
Droo has motive: True or False?
True (0.9687528016079104)
Droo has opportunity: True or False?
True (0.9223425402045055)
Father is guilty: True or False?
False (0.8231134325685282)
Father has mean: True or False?
False (0.3059238951257538)
Father has motive: True or False?
False (0.5304191471149083)
Father has opportunity: True or False?
False (0.3641133616723893)
Monkeys is guilty: True or False?
True (0.6187804294217345)
Monkeys has mean: True or False?
False (0.5282900845448565)
Monkeys has motive: True or False?
True (0.6160122877297346)
Monkeys has opportunity: True or False?
False (0.5428633110863297)
### Dinosaur
- mean: False (0.3629692178304671)
- motive: False (0.10989665588399)
- opportunity: False (0.3372035618207436)

### Droo
- mean: True (0.7994422859301654)
- motive: True (0.9687528016079104)
- opportunity: True (0.9223425402045055)

### Father
- mean: False (0.3059238951257538)
- motive: False (0.5304191471149083)
- opportunity: False (0.3641133616723893)

### Monkeys
- mean: False (0.5282900845448565)
- motive: False (0.3839877122702654)
- opportunity: False (0.5428633110863297)

The culprit is Droo.
In fact, it is Dinosaur.
## 5minutemystery-the-stolen-car-mystery
David Kelly is guilty: True or False?
True (0.6783269591477166)
David Kelly has mean: True or False?
True (0.867485409735739)
David Kelly has motive: True or False?
True (0.7138307731576955)
David Kelly has opportunity: True or False?
True (0.7348812840309261)
Donna Allen is guilty: True or False?
True (0.6113819501087365)
Donna Allen has mean: True or False?
True (0.8438951328214825)
Donna Allen has motive: True or False?
True (0.5907791930117218)
Donna Allen has opportunity: True or False?
True (0.5727227727404994)
Larry Roberts is guilty: True or False?
True (0.5973730125048408)
Larry Roberts has mean: True or False?
True (0.7468781997658912)
Larry Roberts has motive: True or False?
True (0.5907792634380938)
Map:  70%|██████▉   | 142/203 [1:02:37<28:35, 28.12s/ examples]Map:  70%|███████   | 143/203 [1:03:19<32:25, 32.42s/ examples]Map:  71%|███████   | 144/203 [1:03:42<29:09, 29.66s/ examples]Map:  71%|███████▏  | 145/203 [1:04:08<27:23, 28.33s/ examples]Map:  72%|███████▏  | 146/203 [1:04:35<26:44, 28.15s/ examples]Larry Roberts has opportunity: True or False?
True (0.5117165908639297)
Nancy Lee is guilty: True or False?
True (0.5746335251160043)
Nancy Lee has mean: True or False?
True (0.745398395394548)
Nancy Lee has motive: True or False?
True (0.8122724274380432)
Nancy Lee has opportunity: True or False?
True (0.6540113633452196)
### David Kelly
- mean: True (0.867485409735739)
- motive: True (0.7138307731576955)
- opportunity: True (0.7348812840309261)

### Donna Allen
- mean: False (0.15610486717851746)
- motive: False (0.40922080698827823)
- opportunity: False (0.42727722725950057)

### Larry Roberts
- mean: False (0.2531218002341088)
- motive: False (0.40922073656190616)
- opportunity: False (0.48828340913607027)

### Nancy Lee
- mean: False (0.254601604605452)
- motive: False (0.18772757256195682)
- opportunity: False (0.3459886366547804)

The culprit is David Kelly.
In fact, it is Donna Allen.
## 5minutemystery-the-straw-hat-theater-mysteriesfinal-curtain
Arthur Glendon is guilty: True or False?
True (0.946497859305556)
Arthur Glendon has mean: True or False?
True (0.6636689235052821)
Arthur Glendon has motive: True or False?
True (0.9343951361750445)
Arthur Glendon has opportunity: True or False?
True (0.9155072008980665)
Josh Whitehead is guilty: True or False?
True (0.9084556087677383)
Josh Whitehead has mean: True or False?
True (0.8433798528114077)
Josh Whitehead has motive: True or False?
True (0.9156581770494915)
Josh Whitehead has opportunity: True or False?
True (0.9309620852900756)
Linda Eberlie is guilty: True or False?
True (0.8818185984511544)
Linda Eberlie has mean: True or False?
True (0.8187367896794966)
Linda Eberlie has motive: True or False?
True (0.9219218506394821)
Linda Eberlie has opportunity: True or False?
True (0.9390248079664695)
Sam Watson is guilty: True or False?
True (0.8985886567144342)
Sam Watson has mean: True or False?
True (0.8175744430556572)
Sam Watson has motive: True or False?
True (0.8803863464576128)
Sam Watson has opportunity: True or False?
True (0.9144436110210817)
Stella Marlowe is guilty: True or False?
True (0.8158201638039532)
Stella Marlowe has mean: True or False?
True (0.5583269696343842)
Stella Marlowe has motive: True or False?
True (0.7683857617837733)
Stella Marlowe has opportunity: True or False?
True (0.8074606715677252)
### Arthur Glendon
- mean: False (0.33633107649471794)
- motive: False (0.06560486382495545)
- opportunity: False (0.08449279910193352)

### Josh Whitehead
- mean: True (0.8433798528114077)
- motive: True (0.9156581770494915)
- opportunity: True (0.9309620852900756)

### Linda Eberlie
- mean: False (0.1812632103205034)
- motive: False (0.07807814936051793)
- opportunity: False (0.06097519203353052)

### Sam Watson
- mean: False (0.18242555694434281)
- motive: False (0.11961365354238718)
- opportunity: False (0.08555638897891826)

### Stella Marlowe
- mean: False (0.4416730303656158)
- motive: False (0.23161423821622673)
- opportunity: False (0.19253932843227484)

The culprit is Josh Whitehead.
In fact, it is Linda Eberlie.
## 5minutemystery-itheft
Lea Thompson is guilty: True or False?
True (0.5486734987923966)
Lea Thompson has mean: True or False?
True (0.5428633110863297)
Lea Thompson has motive: True or False?
True (0.5992506595844092)
Lea Thompson has opportunity: True or False?
False (0.784649255215384)
Rachel Vermeer is guilty: True or False?
True (0.5774953314585229)
Rachel Vermeer has mean: True or False?
True (0.6531268925247615)
Rachel Vermeer has motive: True or False?
True (0.7956580548514487)
Rachel Vermeer has opportunity: True or False?
False (0.550607385906944)
Shawn Ramos is guilty: True or False?
True (0.6876299924560524)
Shawn Ramos has mean: True or False?
True (0.5841525082971981)
Shawn Ramos has motive: True or False?
True (0.6934729802503211)
Shawn Ramos has opportunity: True or False?
False (0.6723316913929156)
Shay Dulaney is guilty: True or False?
True (0.6645403391983984)
Shay Dulaney has mean: True or False?
True (0.6197014353942354)
Shay Dulaney has motive: True or False?
True (0.745398395394548)
Shay Dulaney has opportunity: True or False?
False (0.6601723415572317)
### Lea Thompson
- mean: False (0.4571366889136703)
- motive: False (0.40074934041559085)
- opportunity: False (0.784649255215384)

### Rachel Vermeer
- mean: True (0.6531268925247615)
- motive: True (0.7956580548514487)
- opportunity: True (0.449392614093056)

### Shawn Ramos
- mean: False (0.4158474917028019)
- motive: False (0.3065270197496789)
- opportunity: False (0.6723316913929156)

### Shay Dulaney
- mean: False (0.3802985646057646)
- motive: False (0.254601604605452)
- opportunity: False (0.6601723415572317)

The culprit is Rachel Vermeer.
In fact, it is Rachel Vermeer.
## 5minutemystery-the-punch-with-a-punch
Carole is guilty: True or False?
True (0.7017130830397807)
Carole has mean: True or False?
True (0.8464508054137014)
Carole has motive: True or False?
True (0.9372107968415931)
Carole has opportunity: True or False?
True (0.7613611200983542)
Dan is guilty: True or False?
True (0.6943026818003076)
Dan has mean: True or False?
True (0.7074046739492601)
Dan has motive: True or False?
True (0.9465966835599983)
Dan has opportunity: True or False?
True (0.7599387683150569)
Diane is guilty: True or False?
True (0.7541915688671895)
Diane has mean: True or False?
True (0.8484706263347676)
Diane has motive: True or False?
True (0.9658995287662642)
Diane has opportunity: True or False?
True (0.8131642285412432)
Principal Whittenmeyer is guilty: True or False?
True (0.5370413742099674)
Principal Whittenmeyer has mean: True or False?
True (0.702530072932436)
Principal Whittenmeyer has motive: True or False?
True (0.8745065930973813)
Principal Whittenmeyer has opportunity: True or False?
False (0.5746334908651781)
### Carole
- mean: False (0.15354919458629857)
- motive: False (0.06278920315840686)
- opportunity: False (0.23863887990164578)

### Dan
- mean: False (0.2925953260507399)
- motive: False (0.053403316440001736)
- opportunity: False (0.2400612316849431)

### Diane
- mean: True (0.8484706263347676)
- motive: True (0.9658995287662642)
- opportunity: True (0.8131642285412432)

### Principal Whittenmeyer
- mean: False (0.29746992706756403)
- motive: False (0.12549340690261868)
- opportunity: False (0.5746334908651781)

The culprit is Diane.
In fact, it is Carole.
## 5minutemystery-the-straw-hat-theater-mysteriesbox-office-nightmare
Basil Carmody is guilty: True or False?
True (0.7905303264811482)
Basil Carmody has mean: True or False?
True (0.9207896596153058)
Basil Carmody has motive: True or False?
True (0.8092759828926619)
Basil Carmody has opportunity: True or False?
True (0.6531268925247615)
John Franklin is guilty: True or False?
True (0.8652240590801695)
John Franklin has mean: True or False?
True (0.8086723099497763)
John Franklin has motive: True or False?
True (0.8386797935187188)
John Franklin has opportunity: True or False?
True (0.6976088896786037)
Lawrence Blake is guilty: True or False?
True (0.8464508054137014)
Lawrence Blake has mean: True or False?
True (0.7122321792841629)
Lawrence Blake has motive: True or False?
True (0.646013666311734)
Lawrence Blake has opportunity: True or False?
False (0.5009765603034438)
Martha Gilmont is guilty: True or False?
True (0.6206215556999736)
Martha Gilmont has mean: True or False?
True (0.5477060024984176)
Martha Gilmont has motive: True or False?
True (0.5350984235603058)
Martha Gilmont has opportunity: True or False?
False (0.7779753136455794)
### Basil Carmody
- mean: True (0.9207896596153058)
- motive: True (0.8092759828926619)
- opportunity: True (0.6531268925247615)

### John Franklin
- mean: False (0.19132769005022365)
- motive: False (0.1613202064812812)
- opportunity: False (0.3023911103213963)

### Lawrence Blake
- mean: False (0.28776782071583706)
- motive: False (0.35398633368826604)
- opportunity: False (0.5009765603034438)

### Martha Gilmont
- mean: False (0.4522939975015824)
- motive: False (0.4649015764396942)
- opportunity: False (0.7779753136455794)

The culprit is Basil Carmody.
In fact, it is John Franklin.
## 5minutemystery-the-waffle-man-mystery
Larry is guilty: True or False?
Map:  72%|███████▏  | 147/203 [1:05:09<27:49, 29.81s/ examples]Map:  73%|███████▎  | 148/203 [1:05:35<26:14, 28.62s/ examples]Map:  73%|███████▎  | 149/203 [1:06:00<24:50, 27.61s/ examples]Map:  74%|███████▍  | 150/203 [1:06:20<22:25, 25.39s/ examples]True (0.816406362162552)
Larry has mean: True or False?
True (0.8529354311342636)
Larry has motive: True or False?
True (0.8856314413364714)
Larry has opportunity: True or False?
True (0.7341195403199204)
The Old Man is guilty: True or False?
True (0.7962924261546153)
The Old Man has mean: True or False?
True (0.8936811689868521)
The Old Man has motive: True or False?
True (0.785637679813794)
The Old Man has opportunity: True or False?
True (0.6451199006197486)
The Waffle Man is guilty: True or False?
True (0.7049732238008671)
The Waffle Man has mean: True or False?
True (0.8402589628813668)
The Waffle Man has motive: True or False?
True (0.7759445334082792)
The Waffle Man has opportunity: True or False?
True (0.6697448487720212)
Vera is guilty: True or False?
True (0.7468781997658912)
Vera has mean: True or False?
True (0.7704647687904915)
Vera has motive: True or False?
True (0.8877896081343184)
Vera has opportunity: True or False?
True (0.7333563569098757)
### Larry
- mean: True (0.8529354311342636)
- motive: True (0.8856314413364714)
- opportunity: True (0.7341195403199204)

### The Old Man
- mean: False (0.10631883101314787)
- motive: False (0.21436232018620605)
- opportunity: False (0.35488009938025145)

### The Waffle Man
- mean: False (0.1597410371186332)
- motive: False (0.22405546659172082)
- opportunity: False (0.33025515122797877)

### Vera
- mean: False (0.22953523120950847)
- motive: False (0.1122103918656816)
- opportunity: False (0.26664364309012434)

The culprit is Larry.
In fact, it is Vera.
## 5minutemystery-the-sunday-school-tithe-mystery
Doc Bentson is guilty: True or False?
True (0.8278281666221954)
Doc Bentson has mean: True or False?
True (0.816406362162552)
Doc Bentson has motive: True or False?
True (0.7371581232960549)
Doc Bentson has opportunity: True or False?
True (0.5263427467960875)
Ellie Wilson is guilty: True or False?
True (0.6325027218909103)
Ellie Wilson has mean: True or False?
True (0.8349459127213729)
Ellie Wilson has motive: True or False?
True (0.6187804294217345)
Ellie Wilson has opportunity: True or False?
False (0.5243946792389143)
James Gant is guilty: True or False?
True (0.7371581232960549)
James Gant has mean: True or False?
True (0.8879840376027315)
James Gant has motive: True or False?
True (0.7209580648179327)
James Gant has opportunity: True or False?
False (0.5097643762740132)
Judy Gant is guilty: True or False?
True (0.615087818987177)
Judy Gant has mean: True or False?
True (0.8484706895507578)
Judy Gant has motive: True or False?
True (0.6766198919456847)
Judy Gant has opportunity: True or False?
False (0.5409238326546766)
Waylon Marsh is guilty: True or False?
True (0.7287483223557857)
Waylon Marsh has mean: True or False?
True (0.8872045854516336)
Waylon Marsh has motive: True or False?
True (0.5525396910980834)
Waylon Marsh has opportunity: True or False?
True (0.6680145240815963)
### Doc Bentson
- mean: False (0.18359363783744798)
- motive: False (0.2628418767039451)
- opportunity: False (0.4736572532039125)

### Ellie Wilson
- mean: False (0.16505408727862714)
- motive: False (0.3812195705782655)
- opportunity: False (0.5243946792389143)

### James Gant
- mean: False (0.11201596239726852)
- motive: False (0.2790419351820673)
- opportunity: False (0.5097643762740132)

### Judy Gant
- mean: False (0.15152931044924223)
- motive: False (0.3233801080543153)
- opportunity: False (0.5409238326546766)

### Waylon Marsh
- mean: True (0.8872045854516336)
- motive: True (0.5525396910980834)
- opportunity: True (0.6680145240815963)

The culprit is Waylon Marsh.
In fact, it is Waylon Marsh.
## 5minutemystery-the-straw-hat-theater-mysteriescasting-call
Alice Cartwright is guilty: True or False?
True (0.5650587803792624)
Alice Cartwright has mean: True or False?
True (0.6834194581047349)
Alice Cartwright has motive: True or False?
True (0.7008948290825966)
Alice Cartwright has opportunity: True or False?
False (0.6270381219830087)
Arthur Glendon is guilty: True or False?
True (0.7956580548514487)
Arthur Glendon has mean: True or False?
True (0.8591918406281239)
Arthur Glendon has motive: True or False?
True (0.8864203688833437)
Arthur Glendon has opportunity: True or False?
False (0.5559174351137421)
Janice Starling is guilty: True or False?
False (0.5650587803792624)
Janice Starling has mean: True or False?
True (0.8615382357584752)
Janice Starling has motive: True or False?
True (0.5832033352502285)
Janice Starling has opportunity: True or False?
False (0.7512834059294674)
Sandra Buckingham is guilty: True or False?
False (0.5983121871760707)
Sandra Buckingham has mean: True or False?
True (0.6680145240815963)
Sandra Buckingham has motive: True or False?
True (0.5832033700118571)
Sandra Buckingham has opportunity: True or False?
False (0.8807970862580315)
### Alice Cartwright
- mean: False (0.3165805418952651)
- motive: False (0.2991051709174034)
- opportunity: False (0.6270381219830087)

### Arthur Glendon
- mean: True (0.8591918406281239)
- motive: True (0.8864203688833437)
- opportunity: True (0.44408256488625786)

### Janice Starling
- mean: False (0.1384617642415248)
- motive: False (0.4167966647497715)
- opportunity: False (0.7512834059294674)

### Sandra Buckingham
- mean: False (0.33198547591840366)
- motive: False (0.41679662998814293)
- opportunity: False (0.8807970862580315)

The culprit is Arthur Glendon.
In fact, it is Arthur Glendon.
## 5minutemystery-the-anonymous-bank-robber
Edward Cantrell is guilty: True or False?
True (0.7325918709325988)
Edward Cantrell has mean: True or False?
True (0.6710395233636681)
Edward Cantrell has motive: True or False?
False (0.5983121871760707)
Edward Cantrell has opportunity: True or False?
False (0.7033457082786769)
Larry Brooks is guilty: True or False?
True (0.6766198919456847)
Larry Brooks has mean: True or False?
True (0.5165954726976894)
Larry Brooks has motive: True or False?
False (0.6522414018725713)
Larry Brooks has opportunity: True or False?
False (0.867485409735739)
Lester Barton is guilty: True or False?
True (0.8062431235779619)
Lester Barton has mean: True or False?
True (0.7371581232960549)
Lester Barton has motive: True or False?
False (0.5009765603034438)
Lester Barton has opportunity: True or False?
False (0.7424217332471881)
Oscar Jordan is guilty: True or False?
True (0.8086723099497763)
Oscar Jordan has mean: True or False?
True (0.6619228707202935)
Oscar Jordan has motive: True or False?
True (0.6601723415572317)
Oscar Jordan has opportunity: True or False?
False (0.5602526707659626)
### Edward Cantrell
- mean: False (0.3289604766363319)
- motive: False (0.5983121871760707)
- opportunity: False (0.7033457082786769)

### Larry Brooks
- mean: False (0.48340452730231065)
- motive: False (0.6522414018725713)
- opportunity: False (0.867485409735739)

### Lester Barton
- mean: False (0.2628418767039451)
- motive: False (0.5009765603034438)
- opportunity: False (0.7424217332471881)

### Oscar Jordan
- mean: True (0.6619228707202935)
- motive: True (0.6601723415572317)
- opportunity: True (0.43974732923403737)

The culprit is Oscar Jordan.
In fact, it is Lester Barton.
## 5minutemystery-the-house-of-lies
Debra is guilty: True or False?
True (0.5486734987923966)
Debra has mean: True or False?
True (0.7956581141325956)
Debra has motive: True or False?
True (0.7924642605907138)
Debra has opportunity: True or False?
True (0.6636689828419103)
Luke is guilty: True or False?
False (0.5360700410935405)
Luke has mean: True or False?
True (0.6076632024562351)
Luke has motive: True or False?
True (0.7189891821820716)
Luke has opportunity: True or False?
True (0.6178585273774891)
Olivia is guilty: True or False?
True (0.6020615685826383)
Olivia has mean: True or False?
True (0.6757646168022439)
Olivia has motive: True or False?
True (0.8679338697256817)
Olivia has opportunity: True or False?
True (0.7549149897594328)
The Butler is guilty: True or False?
True (0.9008791478232747)
The Butler has mean: True or False?
True (0.8322366416985943)
The Butler has motive: True or False?
True (0.795340359502468)
The Butler has opportunity: True or False?
True (0.7655933544531522)
### Debra
- mean: False (0.20434188586740443)
Map:  74%|███████▍  | 151/203 [1:06:50<23:10, 26.74s/ examples]Map:  75%|███████▍  | 152/203 [1:07:22<23:57, 28.18s/ examples]Map:  75%|███████▌  | 153/203 [1:07:46<22:26, 26.94s/ examples]Map:  76%|███████▌  | 154/203 [1:08:14<22:24, 27.44s/ examples]Map:  76%|███████▋  | 155/203 [1:08:36<20:38, 25.81s/ examples]- motive: False (0.20753573940928616)
- opportunity: False (0.33633101715808966)

### Luke
- mean: False (0.39233679754376494)
- motive: False (0.28101081781792836)
- opportunity: False (0.38214147262251086)

### Olivia
- mean: False (0.32423538319775613)
- motive: False (0.13206613027431835)
- opportunity: False (0.24508501024056717)

### The Butler
- mean: True (0.8322366416985943)
- motive: True (0.795340359502468)
- opportunity: True (0.7655933544531522)

The culprit is The Butler.
In fact, it is The Butler.
## 5minutemystery-the-straw-hat-theater-mysterieson-stage
Grace Upshaw is guilty: True or False?
True (0.8984105603938967)
Grace Upshaw has mean: True or False?
True (0.7341194746845218)
Grace Upshaw has motive: True or False?
True (0.8365545874520802)
Grace Upshaw has opportunity: True or False?
True (0.5945512478395265)
Linda Grant is guilty: True or False?
True (0.8474634858439474)
Linda Grant has mean: True or False?
True (0.7333563569098757)
Linda Grant has motive: True or False?
True (0.6667138235236917)
Linda Grant has opportunity: True or False?
False (0.5784481782924303)
Molly Trumbull is guilty: True or False?
True (0.7394224480813394)
Molly Trumbull has mean: True or False?
True (0.6909762697651828)
Molly Trumbull has motive: True or False?
True (0.5539879783000323)
Molly Trumbull has opportunity: True or False?
False (0.6897237229704902)
Samantha Powers is guilty: True or False?
True (0.873646620599733)
Samantha Powers has mean: True or False?
True (0.8193157317863493)
Samantha Powers has motive: True or False?
True (0.621540893468236)
Samantha Powers has opportunity: True or False?
False (0.6085939964125278)
### Grace Upshaw
- mean: True (0.7341194746845218)
- motive: True (0.8365545874520802)
- opportunity: True (0.5945512478395265)

### Linda Grant
- mean: False (0.26664364309012434)
- motive: False (0.3332861764763083)
- opportunity: False (0.5784481782924303)

### Molly Trumbull
- mean: False (0.3090237302348172)
- motive: False (0.4460120216999677)
- opportunity: False (0.6897237229704902)

### Samantha Powers
- mean: False (0.1806842682136507)
- motive: False (0.37845910653176396)
- opportunity: False (0.6085939964125278)

The culprit is Grace Upshaw.
In fact, it is Grace Upshaw.
## 5minutemystery-canada-day
Little black-haired girl is guilty: True or False?
False (0.5009765603034438)
Little black-haired girl has mean: True or False?
False (0.5515737608116735)
Little black-haired girl has motive: True or False?
True (0.7279754274224494)
Little black-haired girl has opportunity: True or False?
False (0.6951311179371613)
Redheaded woman is guilty: True or False?
True (0.6252092625510083)
Redheaded woman has mean: True or False?
True (0.5563995964631269)
Redheaded woman has motive: True or False?
True (0.8238959285889558)
Redheaded woman has opportunity: True or False?
True (0.570809902165233)
Stocky blonde man is guilty: True or False?
True (0.6943026818003076)
Stocky blonde man has mean: True or False?
True (0.5312093941731293)
Stocky blonde man has motive: True or False?
True (0.7033457082786769)
Stocky blonde man has opportunity: True or False?
False (0.7364006034245382)
Tall bald man is guilty: True or False?
True (0.5813030995752883)
Tall bald man has mean: True or False?
False (0.525368812147771)
Tall bald man has motive: True or False?
True (0.7041600870830834)
Tall bald man has opportunity: True or False?
False (0.7570767382203575)
### Little black-haired girl
- mean: False (0.5515737608116735)
- motive: False (0.27202457257755064)
- opportunity: False (0.6951311179371613)

### Redheaded woman
- mean: True (0.5563995964631269)
- motive: True (0.8238959285889558)
- opportunity: True (0.570809902165233)

### Stocky blonde man
- mean: False (0.4687906058268707)
- motive: False (0.29665429172132307)
- opportunity: False (0.7364006034245382)

### Tall bald man
- mean: False (0.525368812147771)
- motive: False (0.2958399129169166)
- opportunity: False (0.7570767382203575)

The culprit is Redheaded woman.
In fact, it is Tall bald man.
## 5minutemystery-the-missing-communion-set
Allison Jordan is guilty: True or False?
True (0.6469064338453809)
Allison Jordan has mean: True or False?
True (0.6791786560103119)
Allison Jordan has motive: True or False?
True (0.65489470935198)
Allison Jordan has opportunity: True or False?
False (0.6817267994905651)
Heather Guse is guilty: True or False?
True (0.6197014353942354)
Heather Guse has mean: True or False?
True (0.8031737798924701)
Heather Guse has motive: True or False?
True (0.8386797310322072)
Heather Guse has opportunity: True or False?
False (0.8365545251239088)
Janelle Herbst is guilty: True or False?
False (0.503906199448032)
Janelle Herbst has mean: True or False?
True (0.776622945813876)
Janelle Herbst has motive: True or False?
True (0.7386690294153369)
Janelle Herbst has opportunity: True or False?
False (0.7520125537161032)
Josh Darvin is guilty: True or False?
True (0.8187367896794966)
Josh Darvin has mean: True or False?
True (0.6976088896786037)
Josh Darvin has motive: True or False?
True (0.8499711693725173)
Josh Darvin has opportunity: True or False?
False (0.6433293282949071)
Justin Paul is guilty: True or False?
True (0.7090191197769757)
Justin Paul has mean: True or False?
True (0.6001883144765984)
Justin Paul has motive: True or False?
True (0.814643384779728)
Justin Paul has opportunity: True or False?
False (0.7570766705324253)
### Allison Jordan
- mean: False (0.3208213439896881)
- motive: False (0.34510529064802)
- opportunity: False (0.6817267994905651)

### Heather Guse
- mean: False (0.19682622010752993)
- motive: False (0.16132026896779283)
- opportunity: False (0.8365545251239088)

### Janelle Herbst
- mean: False (0.22337705418612397)
- motive: False (0.26133097058466315)
- opportunity: False (0.7520125537161032)

### Josh Darvin
- mean: True (0.6976088896786037)
- motive: True (0.8499711693725173)
- opportunity: True (0.3566706717050929)

### Justin Paul
- mean: False (0.3998116855234016)
- motive: False (0.18535661522027203)
- opportunity: False (0.7570766705324253)

The culprit is Josh Darvin.
In fact, it is Josh Darvin.
## 5minutemystery-who-stole-super-bowl-sunday
Aunt Mary is guilty: True or False?
True (0.7879311977554747)
Aunt Mary has mean: True or False?
True (0.8311430212356835)
Aunt Mary has motive: True or False?
True (0.8204694405411458)
Aunt Mary has opportunity: True or False?
True (0.5428632463719839)
Phil is guilty: True or False?
True (0.9246876822649571)
Phil has mean: True or False?
True (0.8006920257960423)
Phil has motive: True or False?
True (0.8062431235779619)
Phil has opportunity: True or False?
True (0.720171518230031)
Rick is guilty: True or False?
True (0.8885655424665229)
Rick has mean: True or False?
True (0.7704647687904915)
Rick has motive: True or False?
True (0.8300437258865985)
Rick has opportunity: True or False?
True (0.6415346823638186)
Uncle Charlie is guilty: True or False?
True (0.9709643714595256)
Uncle Charlie has mean: True or False?
True (0.9019206778000431)
Uncle Charlie has motive: True or False?
True (0.9235923286659299)
Uncle Charlie has opportunity: True or False?
True (0.8966140749572745)
### Aunt Mary
- mean: False (0.1688569787643165)
- motive: False (0.1795305594588542)
- opportunity: False (0.4571367536280161)

### Phil
- mean: False (0.19930797420395774)
- motive: False (0.1937568764220381)
- opportunity: False (0.279828481769969)

### Rick
- mean: False (0.22953523120950847)
- motive: False (0.16995627411340153)
- opportunity: False (0.3584653176361814)

### Uncle Charlie
- mean: True (0.9019206778000431)
- motive: True (0.9235923286659299)
- opportunity: True (0.8966140749572745)

The culprit is Uncle Charlie.
In fact, it is Aunt Mary.
## 5minutemystery-the-cocktail-conundrum
Ian Fairbank is guilty: True or False?
True (0.8019358443954961)
Ian Fairbank has mean: True or False?
True (0.8489722037469682)
Ian Fairbank has motive: True or False?
True (0.875361437979977)
Ian Fairbank has opportunity: True or False?
True (0.897695304229796)
Mr. Fairbank is guilty: True or False?
True (0.842345065078002)
Mr. Fairbank has mean: True or False?
True (0.8438950825214144)
Map:  77%|███████▋  | 156/203 [1:09:01<19:55, 25.44s/ examples]Map:  77%|███████▋  | 157/203 [1:09:27<19:33, 25.50s/ examples]Map:  78%|███████▊  | 158/203 [1:09:56<19:57, 26.61s/ examples]Map:  78%|███████▊  | 159/203 [1:10:24<19:49, 27.04s/ examples]Map:  79%|███████▉  | 160/203 [1:10:39<16:46, 23.40s/ examples]Mr. Fairbank has motive: True or False?
True (0.8216173055802608)
Mr. Fairbank has opportunity: True or False?
True (0.8601343090488404)
Mr. Lewis Rhys is guilty: True or False?
True (0.7461389980806673)
Mr. Lewis Rhys has mean: True or False?
True (0.9066531077351827)
Mr. Lewis Rhys has motive: True or False?
True (0.789233749534095)
Mr. Lewis Rhys has opportunity: True or False?
True (0.8134607635851566)
Mrs. Fairbank is guilty: True or False?
True (0.9190632712053527)
Mrs. Fairbank has mean: True or False?
True (0.9431384818142104)
Mrs. Fairbank has motive: True or False?
True (0.9456006903352807)
Mrs. Fairbank has opportunity: True or False?
True (0.9317114347547434)
### Ian Fairbank
- mean: False (0.15102779625303175)
- motive: False (0.12463856202002299)
- opportunity: False (0.10230469577020396)

### Mr. Fairbank
- mean: False (0.15610491747858557)
- motive: False (0.1783826944197392)
- opportunity: False (0.13986569095115964)

### Mr. Lewis Rhys
- mean: False (0.0933468922648173)
- motive: False (0.21076625046590503)
- opportunity: False (0.18653923641484338)

### Mrs. Fairbank
- mean: True (0.9431384818142104)
- motive: True (0.9456006903352807)
- opportunity: True (0.9317114347547434)

The culprit is Mrs. Fairbank.
In fact, it is Mrs. Fairbank.
## 5minutemystery-the-gypsys-secret-numbers
Great Marchelli is guilty: True or False?
True (0.9577545517476556)
Great Marchelli has mean: True or False?
True (0.9322068701708559)
Great Marchelli has motive: True or False?
True (0.966726005782453)
Great Marchelli has opportunity: True or False?
True (0.958769975577766)
Lorenzo is guilty: True or False?
True (0.924823579961238)
Lorenzo has mean: True or False?
True (0.8407825844829613)
Lorenzo has motive: True or False?
True (0.9456006903352807)
Lorenzo has opportunity: True or False?
True (0.940735282281303)
Ringmaster is guilty: True or False?
True (0.9324532728823121)
Ringmaster has mean: True or False?
True (0.9007046239919082)
Ringmaster has motive: True or False?
True (0.9717254050158363)
Ringmaster has opportunity: True or False?
True (0.9546474221708894)
Sheriff is guilty: True or False?
True (0.9100670238942131)
Sheriff has mean: True or False?
True (0.8860265599597172)
Sheriff has motive: True or False?
True (0.9522199623739209)
Sheriff has opportunity: True or False?
True (0.9493885642537184)
### Great Marchelli
- mean: True (0.9322068701708559)
- motive: True (0.966726005782453)
- opportunity: True (0.958769975577766)

### Lorenzo
- mean: False (0.15921741551703872)
- motive: False (0.054399309664719286)
- opportunity: False (0.05926471771869701)

### Ringmaster
- mean: False (0.0992953760080918)
- motive: False (0.028274594984163737)
- opportunity: False (0.04535257782911062)

### Sheriff
- mean: False (0.11397344004028276)
- motive: False (0.047780037626079075)
- opportunity: False (0.050611435746281574)

The culprit is Great Marchelli.
In fact, it is Sheriff.
## 5minutemystery-its-gone
Abe is guilty: True or False?
True (0.8244619332958376)
Abe has mean: True or False?
True (0.9224823751318276)
Abe has motive: True or False?
True (0.8799743689174987)
Abe has opportunity: True or False?
True (0.7680380401429294)
Lance is guilty: True or False?
True (0.8741846653426761)
Lance has mean: True or False?
True (0.7846493136763113)
Lance has motive: True or False?
True (0.9189178954169608)
Lance has opportunity: True or False?
True (0.8474634858439474)
The Amazing Andrew is guilty: True or False?
True (0.8940516749601143)
The Amazing Andrew has mean: True or False?
True (0.8958875533219306)
The Amazing Andrew has motive: True or False?
True (0.9328213936074807)
The Amazing Andrew has opportunity: True or False?
True (0.7563575572780217)
Zora the Magnificent is guilty: True or False?
True (0.8241790481509624)
Zora the Magnificent has mean: True or False?
True (0.769080279275001)
Zora the Magnificent has motive: True or False?
True (0.9095863097773887)
Zora the Magnificent has opportunity: True or False?
True (0.7585106418731645)
### Abe
- mean: False (0.07751762486817237)
- motive: False (0.1200256310825013)
- opportunity: False (0.23196195985707058)

### Lance
- mean: False (0.2153506863236887)
- motive: False (0.08108210458303922)
- opportunity: False (0.15253651415605263)

### The Amazing Andrew
- mean: True (0.8958875533219306)
- motive: True (0.9328213936074807)
- opportunity: True (0.7563575572780217)

### Zora the Magnificent
- mean: False (0.230919720724999)
- motive: False (0.09041369022261125)
- opportunity: False (0.24148935812683547)

The culprit is The Amazing Andrew.
In fact, it is The Amazing Andrew.
## 5minutemystery-the-misers-hoard
Bob Parsons is guilty: True or False?
True (0.9735944874605075)
Bob Parsons has mean: True or False?
True (0.9564718616162037)
Bob Parsons has motive: True or False?
True (0.9536650199751218)
Bob Parsons has opportunity: True or False?
True (0.7898827135821628)
John Entwhistle III is guilty: True or False?
True (0.9299510095943111)
John Entwhistle III has mean: True or False?
True (0.8879840376027315)
John Entwhistle III has motive: True or False?
True (0.9579909444975866)
John Entwhistle III has opportunity: True or False?
True (0.7098244343353132)
Sam Greenway is guilty: True or False?
True (0.9515039936355008)
Sam Greenway has mean: True or False?
True (0.91789335161495)
Sam Greenway has motive: True or False?
True (0.9173766997328059)
Sam Greenway has opportunity: True or False?
True (0.8181563669811865)
Sarah Parsons is guilty: True or False?
True (0.958769975577766)
Sarah Parsons has mean: True or False?
True (0.9173026661190045)
Sarah Parsons has motive: True or False?
True (0.9231777821690265)
Sarah Parsons has opportunity: True or False?
True (0.6992543888266708)
### Bob Parsons
- mean: True (0.9564718616162037)
- motive: True (0.9536650199751218)
- opportunity: True (0.7898827135821628)

### John Entwhistle III
- mean: False (0.11201596239726852)
- motive: False (0.042009055502413406)
- opportunity: False (0.29017556566468683)

### Sam Greenway
- mean: False (0.08210664838505)
- motive: False (0.08262330026719411)
- opportunity: False (0.18184363301881346)

### Sarah Parsons
- mean: False (0.08269733388099554)
- motive: False (0.07682221783097354)
- opportunity: False (0.3007456111733292)

The culprit is Bob Parsons.
In fact, it is Sarah Parsons.
## 5minutemystery-the-cornfield-caper
Austin is guilty: True or False?
True (0.7409249009267298)
Austin has mean: True or False?
True (0.854884620116169)
Austin has motive: True or False?
True (0.7074046739492601)
Austin has opportunity: True or False?
True (0.6113819501087365)
Billy is guilty: True or False?
True (0.621540893468236)
Billy has mean: True or False?
True (0.8175745039697023)
Billy has motive: True or False?
True (0.8104788598666923)
Billy has opportunity: True or False?
True (0.7994423454932595)
Nick is guilty: True or False?
False (0.5185461538431656)
Nick has mean: True or False?
True (0.7859664553110391)
Nick has motive: True or False?
True (0.7527403228571042)
Nick has opportunity: True or False?
True (0.678326898500563)
### Austin
- mean: False (0.14511537988383105)
- motive: False (0.2925953260507399)
- opportunity: False (0.3886180498912635)

### Billy
- mean: True (0.8175745039697023)
- motive: True (0.8104788598666923)
- opportunity: True (0.7994423454932595)

### Nick
- mean: False (0.21403354468896085)
- motive: False (0.24725967714289576)
- opportunity: False (0.32167310149943695)

The culprit is Billy.
In fact, it is Billy.
## 5minutemystery-a-stolen-future
Donna Blake is guilty: True or False?
True (0.789233749534095)
Donna Blake has mean: True or False?
True (0.8198933606225757)
Donna Blake has motive: True or False?
True (0.7394224480813394)
Donna Blake has opportunity: True or False?
True (0.7534666630720156)
George Wilson is guilty: True or False?
True (0.7498207054286419)
George Wilson has mean: True or False?
True (0.7098243920264812)
George Wilson has motive: True or False?
True (0.8322366416985943)
George Wilson has opportunity: True or False?
True (0.7008947664177184)
Jeffery Sharp is guilty: True or False?
True (0.8526903338256402)
Jeffery Sharp has mean: True or False?
True (0.6379334932841956)
Map:  79%|███████▉  | 161/203 [1:11:05<16:51, 24.07s/ examples]Map:  80%|███████▉  | 162/203 [1:11:41<18:58, 27.77s/ examples]Map:  80%|████████  | 163/203 [1:12:16<20:02, 30.05s/ examples]Map:  81%|████████  | 164/203 [1:12:43<18:53, 29.05s/ examples]Jeffery Sharp has motive: True or False?
True (0.816406362162552)
Jeffery Sharp has opportunity: True or False?
True (0.7786492592534148)
Pete Thompson is guilty: True or False?
True (0.9012274173198201)
Pete Thompson has mean: True or False?
True (0.7853085971692302)
Pete Thompson has motive: True or False?
True (0.7662936378892937)
Pete Thompson has opportunity: True or False?
True (0.7879311977554747)
### Donna Blake
- mean: False (0.18010663937742433)
- motive: False (0.2605775519186606)
- opportunity: False (0.2465333369279844)

### George Wilson
- mean: False (0.2901756079735188)
- motive: False (0.16776335830140565)
- opportunity: False (0.2991052335822816)

### Jeffery Sharp
- mean: False (0.3620665067158044)
- motive: False (0.18359363783744798)
- opportunity: False (0.22135074074658523)

### Pete Thompson
- mean: True (0.7853085971692302)
- motive: True (0.7662936378892937)
- opportunity: True (0.7879311977554747)

The culprit is Pete Thompson.
In fact, it is Jeffery Sharp.
## 5minutemystery-the-dirty-half-dozen
Bethany Knight is guilty: True or False?
True (0.8227594449669557)
Bethany Knight has mean: True or False?
True (0.9193534273597669)
Bethany Knight has motive: True or False?
True (0.8910549899564296)
Bethany Knight has opportunity: True or False?
True (0.7217431689117048)
Joe Clark is guilty: True or False?
True (0.8902942539348153)
Joe Clark has mean: True or False?
True (0.9358173616900589)
Joe Clark has motive: True or False?
True (0.9405717864730483)
Joe Clark has opportunity: True or False?
True (0.8056321690561029)
Sherry Fogle is guilty: True or False?
True (0.8050197941712954)
Sherry Fogle has mean: True or False?
True (0.8860265599597172)
Sherry Fogle has motive: True or False?
True (0.8479678036998373)
Sherry Fogle has opportunity: True or False?
False (0.5048826860345702)
Tonya Muse is guilty: True or False?
True (0.5822535180679596)
Tonya Muse has mean: True or False?
True (0.7872777601997338)
Tonya Muse has motive: True or False?
True (0.7697732451157533)
Tonya Muse has opportunity: True or False?
False (0.6671476389322356)
Wayne Clark is guilty: True or False?
True (0.9329437018480795)
Wayne Clark has mean: True or False?
True (0.9489172681310486)
Wayne Clark has motive: True or False?
True (0.9580694433457548)
Wayne Clark has opportunity: True or False?
True (0.8665847814067802)
### Bethany Knight
- mean: False (0.08064657264023312)
- motive: False (0.10894501004357038)
- opportunity: False (0.27825683108829524)

### Joe Clark
- mean: False (0.06418263830994109)
- motive: False (0.05942821352695171)
- opportunity: False (0.1943678309438971)

### Sherry Fogle
- mean: False (0.11397344004028276)
- motive: False (0.15203219630016274)
- opportunity: False (0.5048826860345702)

### Tonya Muse
- mean: False (0.21272223980026617)
- motive: False (0.2302267548842467)
- opportunity: False (0.6671476389322356)

### Wayne Clark
- mean: True (0.9489172681310486)
- motive: True (0.9580694433457548)
- opportunity: True (0.8665847814067802)

The culprit is Wayne Clark.
In fact, it is Wayne Clark.
## 5minutemystery-a-porsche-of-course
Amy Golden is guilty: True or False?
True (0.5428632463719839)
Amy Golden has mean: True or False?
False (0.5660185351323219)
Amy Golden has motive: True or False?
False (0.5068355091660127)
Amy Golden has opportunity: True or False?
False (0.8181563669811865)
Frankie Cole is guilty: True or False?
True (0.7697732451157533)
Frankie Cole has mean: True or False?
True (0.7505527730327083)
Frankie Cole has motive: True or False?
True (0.7563575572780217)
Frankie Cole has opportunity: True or False?
True (0.6654105788791005)
Jeremy Steele is guilty: True or False?
True (0.5907791930117218)
Jeremy Steele has mean: True or False?
True (0.5888891269161294)
Jeremy Steele has motive: True or False?
True (0.5746334908651781)
Jeremy Steele has opportunity: True or False?
False (0.5973730125048408)
Lionel Jacobs is guilty: True or False?
True (0.6926419789019715)
Lionel Jacobs has mean: True or False?
True (0.5136684743338078)
Lionel Jacobs has motive: True or False?
False (0.5273165068094335)
Lionel Jacobs has opportunity: True or False?
False (0.5477060024984176)
Susan Barker is guilty: True or False?
True (0.6671476985798853)
Susan Barker has mean: True or False?
False (0.5097643762740132)
Susan Barker has motive: True or False?
True (0.51464427676968)
Susan Barker has opportunity: True or False?
True (0.5698526542706361)
### Amy Golden
- mean: False (0.5660185351323219)
- motive: False (0.5068355091660127)
- opportunity: False (0.8181563669811865)

### Frankie Cole
- mean: True (0.7505527730327083)
- motive: True (0.7563575572780217)
- opportunity: True (0.6654105788791005)

### Jeremy Steele
- mean: False (0.4111108730838706)
- motive: False (0.4253665091348219)
- opportunity: False (0.5973730125048408)

### Lionel Jacobs
- mean: False (0.4863315256661922)
- motive: False (0.5273165068094335)
- opportunity: False (0.5477060024984176)

### Susan Barker
- mean: False (0.5097643762740132)
- motive: False (0.48535572323031995)
- opportunity: False (0.43014734572936386)

The culprit is Frankie Cole.
In fact, it is Frankie Cole.
## 5minutemystery-the-mystery-of-the-missing-story
Alex Rebmevon is guilty: True or False?
True (0.9407897579933674)
Alex Rebmevon has mean: True or False?
True (0.8489722037469682)
Alex Rebmevon has motive: True or False?
True (0.8951566249612815)
Alex Rebmevon has opportunity: True or False?
True (0.6876299924560524)
Amy is guilty: True or False?
True (0.7520125537161032)
Amy has mean: True or False?
True (0.6224593484250324)
Amy has motive: True or False?
True (0.7162185953247016)
Amy has opportunity: True or False?
True (0.6270381219830087)
Lucy is guilty: True or False?
True (0.6842640693504702)
Lucy has mean: True or False?
False (0.6693127155643409)
Lucy has motive: True or False?
True (0.6570984669319457)
Lucy has opportunity: True or False?
False (0.5131804871639641)
Sarah is guilty: True or False?
True (0.6288633913849659)
Sarah has mean: True or False?
False (0.5331543669186894)
Sarah has motive: True or False?
True (0.8565725156795254)
Sarah has opportunity: True or False?
True (0.6160122877297346)
### Alex Rebmevon
- mean: True (0.8489722037469682)
- motive: True (0.8951566249612815)
- opportunity: True (0.6876299924560524)

### Amy
- mean: False (0.37754065157496763)
- motive: False (0.28378140467529844)
- opportunity: False (0.3729618780169913)

### Lucy
- mean: False (0.6693127155643409)
- motive: False (0.34290153306805427)
- opportunity: False (0.5131804871639641)

### Sarah
- mean: False (0.5331543669186894)
- motive: False (0.14342748432047459)
- opportunity: False (0.3839877122702654)

The culprit is Alex Rebmevon.
In fact, it is Lucy.
## 5minutemystery-the-case-of-the-missing-friend
Billy Friend is guilty: True or False?
True (0.6020615685826383)
Billy Friend has mean: True or False?
True (0.811078188867804)
Billy Friend has motive: True or False?
True (0.7752647497229632)
Billy Friend has opportunity: True or False?
True (0.5612147992901458)
Diana Scott is guilty: True or False?
True (0.5936092727363199)
Diana Scott has mean: True or False?
True (0.7333563569098757)
Diana Scott has motive: True or False?
True (0.6397360437814448)
Diana Scott has opportunity: True or False?
True (0.5195213440667139)
Harrell Garner is guilty: True or False?
True (0.5879430860094185)
Harrell Garner has mean: True or False?
True (0.615087855649269)
Harrell Garner has motive: True or False?
True (0.5879431210535583)
Harrell Garner has opportunity: True or False?
True (0.503906199448032)
Susan Allen is guilty: True or False?
False (0.646013666311734)
Susan Allen has mean: True or False?
True (0.642432441257838)
Susan Allen has motive: True or False?
True (0.6477981763584071)
Susan Allen has opportunity: True or False?
False (0.6706082735718226)
### Billy Friend
- mean: True (0.811078188867804)
- motive: True (0.7752647497229632)
- opportunity: True (0.5612147992901458)

### Diana Scott
- mean: False (0.26664364309012434)
- motive: False (0.3602639562185552)
- opportunity: False (0.4804786559332861)

### Harrell Garner
- mean: False (0.38491214435073096)
Map:  81%|████████▏ | 165/203 [1:13:06<17:18, 27.33s/ examples]Map:  82%|████████▏ | 166/203 [1:13:33<16:43, 27.12s/ examples]Map:  82%|████████▏ | 167/203 [1:14:02<16:32, 27.57s/ examples]Map:  83%|████████▎ | 168/203 [1:14:28<15:50, 27.16s/ examples]Map:  83%|████████▎ | 169/203 [1:15:00<16:11, 28.58s/ examples]- motive: False (0.4120568789464417)
- opportunity: False (0.49609380055196795)

### Susan Allen
- mean: False (0.35756755874216195)
- motive: False (0.3522018236415929)
- opportunity: False (0.6706082735718226)

The culprit is Billy Friend.
In fact, it is Diana Scott.
## 5minutemystery-sweat-it-out
Chris Henderson is guilty: True or False?
True (0.7905303264811482)
Chris Henderson has mean: True or False?
True (0.85729086409805)
Chris Henderson has motive: True or False?
True (0.720171518230031)
Chris Henderson has opportunity: True or False?
False (0.6187804294217345)
Dave Perkins is guilty: True or False?
True (0.8864204283224634)
Dave Perkins has mean: True or False?
True (0.8438951328214825)
Dave Perkins has motive: True or False?
True (0.8241790481509624)
Dave Perkins has opportunity: True or False?
True (0.5945512478395265)
Larry Douglas is guilty: True or False?
True (0.8526902830013373)
Larry Douglas has mean: True or False?
True (0.7386690954574974)
Larry Douglas has motive: True or False?
True (0.6706082735718226)
Larry Douglas has opportunity: True or False?
False (0.5399537164111071)
Nathan Elliott is guilty: True or False?
True (0.8392075331266983)
Nathan Elliott has mean: True or False?
True (0.8828325273478573)
Nathan Elliott has motive: True or False?
True (0.7409249009267298)
Nathan Elliott has opportunity: True or False?
True (0.5302364729224919)
### Chris Henderson
- mean: False (0.14270913590195)
- motive: False (0.279828481769969)
- opportunity: False (0.6187804294217345)

### Dave Perkins
- mean: True (0.8438951328214825)
- motive: True (0.8241790481509624)
- opportunity: True (0.5945512478395265)

### Larry Douglas
- mean: False (0.26133090454250263)
- motive: False (0.3293917264281774)
- opportunity: False (0.5399537164111071)

### Nathan Elliott
- mean: False (0.11716747265214267)
- motive: False (0.2590750990732702)
- opportunity: False (0.4697635270775081)

The culprit is Dave Perkins.
In fact, it is Chris Henderson.
## 5minutemystery-mystery-of-the-missing-heart
Eric Winter is guilty: True or False?
True (0.8927496657814362)
Eric Winter has mean: True or False?
True (0.8674854614419002)
Eric Winter has motive: True or False?
True (0.8862236142219189)
Eric Winter has opportunity: True or False?
False (0.51464427676968)
Jenny Jackson is guilty: True or False?
True (0.7718435616326055)
Jenny Jackson has mean: True or False?
True (0.821044090050916)
Jenny Jackson has motive: True or False?
True (0.8681575656976329)
Jenny Jackson has opportunity: True or False?
True (0.6288633913849659)
Jimmy Jackson is guilty: True or False?
True (0.875574405580689)
Jimmy Jackson has mean: True or False?
True (0.7826624547920057)
Jimmy Jackson has motive: True or False?
True (0.8985886567144342)
Jimmy Jackson has opportunity: True or False?
True (0.7498206607358464)
Wendy LaRue is guilty: True or False?
True (0.8155265480299457)
Wendy LaRue has mean: True or False?
True (0.862930245043327)
Wendy LaRue has motive: True or False?
True (0.814643384779728)
Wendy LaRue has opportunity: True or False?
False (0.5009765603034438)
### Eric Winter
- mean: False (0.1325145385580998)
- motive: False (0.11377638577808113)
- opportunity: False (0.51464427676968)

### Jenny Jackson
- mean: False (0.17895590994908395)
- motive: False (0.13184243430236708)
- opportunity: False (0.37113660861503406)

### Jimmy Jackson
- mean: True (0.7826624547920057)
- motive: True (0.8985886567144342)
- opportunity: True (0.7498206607358464)

### Wendy LaRue
- mean: False (0.13706975495667295)
- motive: False (0.18535661522027203)
- opportunity: False (0.5009765603034438)

The culprit is Jimmy Jackson.
In fact, it is Eric Winter.
## 5minutemystery-stealing-second-base
Coach Joe Morgan is guilty: True or False?
True (0.8631610245991334)
Coach Joe Morgan has mean: True or False?
True (0.7505527730327083)
Coach Joe Morgan has motive: True or False?
True (0.5321819753403337)
Coach Joe Morgan has opportunity: True or False?
True (0.5087881220234095)
Mary Thornton is guilty: True or False?
True (0.8828325273478573)
Mary Thornton has mean: True or False?
True (0.770464837675413)
Mary Thornton has motive: True or False?
True (0.7937461674149602)
Mary Thornton has opportunity: True or False?
True (0.6029970803636248)
Randy Newsom is guilty: True or False?
True (0.9103861443438126)
Randy Newsom has mean: True or False?
True (0.9082930095862076)
Randy Newsom has motive: True or False?
True (0.8261514850267767)
Randy Newsom has opportunity: True or False?
False (0.514644215419305)
Shorty Gilstrap is guilty: True or False?
True (0.9036349079321685)
Shorty Gilstrap has mean: True or False?
True (0.893681109060862)
Shorty Gilstrap has motive: True or False?
True (0.8074606715677252)
Shorty Gilstrap has opportunity: True or False?
True (0.5650587803792624)
### Coach Joe Morgan
- mean: False (0.2494472269672917)
- motive: False (0.46781802465966627)
- opportunity: False (0.4912118779765905)

### Mary Thornton
- mean: False (0.22953516232458704)
- motive: False (0.20625383258503982)
- opportunity: False (0.39700291963637524)

### Randy Newsom
- mean: False (0.09170699041379238)
- motive: False (0.1738485149732233)
- opportunity: False (0.514644215419305)

### Shorty Gilstrap
- mean: True (0.893681109060862)
- motive: True (0.8074606715677252)
- opportunity: True (0.5650587803792624)

The culprit is Shorty Gilstrap.
In fact, it is Mary Thornton.
## 5minutemystery-murder-in-the-old-house
Bathroom is guilty: True or False?
True (0.8386797935187188)
Bathroom has mean: True or False?
True (0.6141625595066657)
Bathroom has motive: True or False?
True (0.642432441257838)
Bathroom has opportunity: True or False?
True (0.6085939964125278)
Bedroom of daughter, Anita Jensen is guilty: True or False?
True (0.6834194581047349)
Bedroom of daughter, Anita Jensen has mean: True or False?
True (0.7146280500737092)
Bedroom of daughter, Anita Jensen has motive: True or False?
True (0.6645402797838648)
Bedroom of daughter, Anita Jensen has opportunity: True or False?
True (0.5973730125048408)
Bedroom of oldest son, Harry Jensen is guilty: True or False?
False (0.5039061393777357)
Bedroom of oldest son, Harry Jensen has mean: True or False?
True (0.6522414018725713)
Bedroom of oldest son, Harry Jensen has motive: True or False?
False (0.5525396581641524)
Bedroom of oldest son, Harry Jensen has opportunity: True or False?
False (0.5936092727363199)
Bedroom of youngest son, Edward Jensen is guilty: True or False?
True (0.6169357925086439)
Bedroom of youngest son, Edward Jensen has mean: True or False?
True (0.7697733139388475)
Bedroom of youngest son, Edward Jensen has motive: True or False?
True (0.570809902165233)
Bedroom of youngest son, Edward Jensen has opportunity: True or False?
True (0.5650587803792624)
Master bedroom of Earl and Mildrid Jensen is guilty: True or False?
True (0.5727227727404994)
Master bedroom of Earl and Mildrid Jensen has mean: True or False?
True (0.7725306828324007)
Master bedroom of Earl and Mildrid Jensen has motive: True or False?
True (0.6918097672776748)
Master bedroom of Earl and Mildrid Jensen has opportunity: True or False?
True (0.686790355176806)
### Bathroom
- mean: False (0.38583744049333435)
- motive: False (0.35756755874216195)
- opportunity: False (0.39140600358747224)

### Bedroom of daughter, Anita Jensen
- mean: False (0.2853719499262908)
- motive: False (0.33545972021613524)
- opportunity: False (0.40262698749515924)

### Bedroom of oldest son, Harry Jensen
- mean: False (0.3477585981274287)
- motive: False (0.5525396581641524)
- opportunity: False (0.5936092727363199)

### Bedroom of youngest son, Edward Jensen
- mean: False (0.23022668606115249)
- motive: False (0.429190097834767)
- opportunity: False (0.4349412196207376)

### Master bedroom of Earl and Mildrid Jensen
- mean: True (0.7725306828324007)
- motive: True (0.6918097672776748)
- opportunity: True (0.686790355176806)

The culprit is Master bedroom of Earl and Mildrid Jensen.
In fact, it is Bathroom.
## 5minutemystery-the-chess-mystery
Father is guilty: True or False?
True (0.9443823686645129)
Father has mean: True or False?
True (0.7819973291046377)
Father has motive: True or False?
Map:  84%|████████▎ | 170/203 [1:15:27<15:26, 28.06s/ examples]Map:  84%|████████▍ | 171/203 [1:15:50<14:12, 26.64s/ examples]Map:  85%|████████▍ | 172/203 [1:16:15<13:34, 26.26s/ examples]Map:  85%|████████▌ | 173/203 [1:16:42<13:13, 26.46s/ examples]Map:  86%|████████▌ | 174/203 [1:17:08<12:38, 26.17s/ examples]True (0.9076402191395381)
Father has opportunity: True or False?
True (0.6451199006197486)
Greg is guilty: True or False?
True (0.873646620599733)
Greg has mean: True or False?
True (0.7994422859301654)
Greg has motive: True or False?
True (0.8998277786460391)
Greg has opportunity: True or False?
True (0.7379143332111532)
Tina is guilty: True or False?
True (0.7779752672746386)
Tina has mean: True or False?
True (0.7379142672364736)
Tina has motive: True or False?
True (0.7512834059294674)
Tina has opportunity: True or False?
True (0.6723316913929156)
Uncle Larry is guilty: True or False?
True (0.9392480858026054)
Uncle Larry has mean: True or False?
True (0.794384956668203)
Uncle Larry has motive: True or False?
True (0.847967740521315)
Uncle Larry has opportunity: True or False?
True (0.6959583025067009)
### Father
- mean: False (0.2180026708953623)
- motive: False (0.09235978086046193)
- opportunity: False (0.35488009938025145)

### Greg
- mean: True (0.7994422859301654)
- motive: True (0.8998277786460391)
- opportunity: True (0.7379143332111532)

### Tina
- mean: False (0.2620857327635264)
- motive: False (0.2487165940705326)
- opportunity: False (0.3276683086070844)

### Uncle Larry
- mean: False (0.20561504333179703)
- motive: False (0.15203225947868504)
- opportunity: False (0.3040416974932991)

The culprit is Greg.
In fact, it is Greg.
## 5minutemystery-lost-stolen-and-found
John Beddington is guilty: True or False?
True (0.8125700297166154)
John Beddington has mean: True or False?
True (0.9456006304504523)
John Beddington has motive: True or False?
True (0.7490872087035162)
John Beddington has opportunity: True or False?
True (0.8418256636710214)
Louisa Perry is guilty: True or False?
True (0.6297746298200823)
Louisa Perry has mean: True or False?
True (0.8899121304559661)
Louisa Perry has motive: True or False?
True (0.6575384693006662)
Louisa Perry has opportunity: True or False?
True (0.6039318499573872)
Mary Ingram is guilty: True or False?
True (0.5535053004623279)
Mary Ingram has mean: True or False?
True (0.8175745039697023)
Mary Ingram has motive: True or False?
True (0.7416740115009234)
Mary Ingram has opportunity: True or False?
True (0.6029970803636248)
Sarah Upton is guilty: True or False?
True (0.615087818987177)
Sarah Upton has mean: True or False?
True (0.8633916342942395)
Sarah Upton has motive: True or False?
True (0.612309626324874)
Sarah Upton has opportunity: True or False?
True (0.5794004215835179)
### John Beddington
- mean: True (0.9456006304504523)
- motive: True (0.7490872087035162)
- opportunity: True (0.8418256636710214)

### Louisa Perry
- mean: False (0.11008786954403393)
- motive: False (0.3424615306993338)
- opportunity: False (0.39606815004261275)

### Mary Ingram
- mean: False (0.18242549603029767)
- motive: False (0.2583259884990766)
- opportunity: False (0.39700291963637524)

### Sarah Upton
- mean: False (0.13660836570576051)
- motive: False (0.38769037367512604)
- opportunity: False (0.4205995784164821)

The culprit is John Beddington.
In fact, it is Louisa Perry.
## 5minutemystery-the-chocolate-cupcake-caper
Geraldine is guilty: True or False?
False (0.6662796746479285)
Geraldine has mean: True or False?
True (0.7348812840309261)
Geraldine has motive: True or False?
True (0.7094219376364089)
Geraldine has opportunity: True or False?
True (0.6020615685826383)
Julianna is guilty: True or False?
True (0.6926419789019715)
Julianna has mean: True or False?
True (0.9210740952879496)
Julianna has motive: True or False?
True (0.9492946258008691)
Julianna has opportunity: True or False?
True (0.7371581892031299)
Luis is guilty: True or False?
True (0.6141626144170799)
Luis has mean: True or False?
True (0.8080671968507699)
Luis has motive: True or False?
True (0.8868131040663721)
Luis has opportunity: True or False?
True (0.7905303264811482)
Mr. Bento is guilty: True or False?
False (0.6095241271158658)
Mr. Bento has mean: True or False?
True (0.8227594449669557)
Mr. Bento has motive: True or False?
True (0.8360197583769845)
Mr. Bento has opportunity: True or False?
True (0.589834510337428)
### Geraldine
- mean: False (0.2651187159690739)
- motive: False (0.29057806236359107)
- opportunity: False (0.39793843141736174)

### Julianna
- mean: True (0.9210740952879496)
- motive: True (0.9492946258008691)
- opportunity: True (0.7371581892031299)

### Luis
- mean: False (0.1919328031492301)
- motive: False (0.11318689593362785)
- opportunity: False (0.20946967351885182)

### Mr. Bento
- mean: False (0.17724055503304426)
- motive: False (0.1639802416230155)
- opportunity: False (0.41016548966257205)

The culprit is Julianna.
In fact, it is Geraldine.
## 5minutemystery-dead-mans-island
Grandpa is guilty: True or False?
True (0.8244619332958376)
Grandpa has mean: True or False?
True (0.8397340156610265)
Grandpa has motive: True or False?
True (0.9382373082603129)
Grandpa has opportunity: True or False?
False (0.5009765005823875)
Grandpa's grandfather is guilty: True or False?
True (0.6610481693322063)
Grandpa's grandfather has mean: True or False?
True (0.7185943809170431)
Grandpa's grandfather has motive: True or False?
True (0.9509603391767795)
Grandpa's grandfather has opportunity: True or False?
False (0.6800292740030767)
Lisa is guilty: True or False?
False (0.5312093941731293)
Lisa has mean: True or False?
False (0.6252093370817647)
Lisa has motive: True or False?
True (0.7174080061598618)
Lisa has opportunity: True or False?
False (0.5506073202694327)
Mike is guilty: True or False?
True (0.7416740115009234)
Mike has mean: True or False?
True (0.627038178044588)
Mike has motive: True or False?
True (0.8615382357584752)
Mike has opportunity: True or False?
True (0.7468781552484828)
### Grandpa
- mean: True (0.8397340156610265)
- motive: True (0.9382373082603129)
- opportunity: True (0.4990234994176125)

### Grandpa's grandfather
- mean: False (0.2814056190829569)
- motive: False (0.04903966082322053)
- opportunity: False (0.6800292740030767)

### Lisa
- mean: False (0.6252093370817647)
- motive: False (0.2825919938401382)
- opportunity: False (0.5506073202694327)

### Mike
- mean: False (0.37296182195541205)
- motive: False (0.1384617642415248)
- opportunity: False (0.2531218447515172)

The culprit is Grandpa.
In fact, it is Lisa.
## 5minutemystery-who-stole-the-rock-of-ages
Denise Hurst is guilty: True or False?
True (0.7745833916423246)
Denise Hurst has mean: True or False?
True (0.8615382357584752)
Denise Hurst has motive: True or False?
True (0.5602526707659626)
Denise Hurst has opportunity: True or False?
False (0.5107405858633529)
Jim Gaigon is guilty: True or False?
True (0.8272706865691472)
Jim Gaigon has mean: True or False?
True (0.7287483223557857)
Jim Gaigon has motive: True or False?
True (0.6297745735138451)
Jim Gaigon has opportunity: True or False?
False (0.5253688747766175)
Juan Carde is guilty: True or False?
True (0.858718632897247)
Juan Carde has mean: True or False?
True (0.9178934131644976)
Juan Carde has motive: True or False?
True (0.779321849347754)
Juan Carde has opportunity: True or False?
True (0.7106282704218558)
Skye Smith is guilty: True or False?
True (0.6415346823638186)
Skye Smith has mean: True or False?
True (0.6984323202883935)
Skye Smith has motive: True or False?
False (0.5097644370426659)
Skye Smith has opportunity: True or False?
False (0.6486889055472267)
### Denise Hurst
- mean: False (0.1384617642415248)
- motive: False (0.43974732923403737)
- opportunity: False (0.5107405858633529)

### Jim Gaigon
- mean: False (0.2712516776442143)
- motive: False (0.37022542648615486)
- opportunity: False (0.5253688747766175)

### Juan Carde
- mean: True (0.9178934131644976)
- motive: True (0.779321849347754)
- opportunity: True (0.7106282704218558)

### Skye Smith
- mean: False (0.3015676797116065)
- motive: False (0.5097644370426659)
- opportunity: False (0.6486889055472267)

The culprit is Juan Carde.
In fact, it is Juan Carde.
## 5minutemystery-all-washed-up
Captain Kildare is guilty: True or False?
True (0.8423451152856819)
Captain Kildare has mean: True or False?
True (0.9359345468898206)
Captain Kildare has motive: True or False?
True (0.9164093141890854)
Map:  86%|████████▌ | 175/203 [1:17:33<12:06, 25.94s/ examples]Map:  87%|████████▋ | 176/203 [1:17:55<11:09, 24.79s/ examples]Map:  87%|████████▋ | 177/203 [1:18:22<11:02, 25.48s/ examples]Map:  88%|████████▊ | 178/203 [1:18:51<11:01, 26.45s/ examples]Map:  88%|████████▊ | 179/203 [1:19:18<10:41, 26.71s/ examples]Captain Kildare has opportunity: True or False?
True (0.8560919228396967)
Latrisha Lanigan is guilty: True or False?
True (0.7394224480813394)
Latrisha Lanigan has mean: True or False?
True (0.7468781997658912)
Latrisha Lanigan has motive: True or False?
True (0.8710366507406179)
Latrisha Lanigan has opportunity: True or False?
True (0.685107355950278)
Mark Colson is guilty: True or False?
True (0.7839884808423031)
Mark Colson has mean: True or False?
True (0.7950222460539826)
Mark Colson has motive: True or False?
True (0.8086723099497763)
Mark Colson has opportunity: True or False?
True (0.615087855649269)
Marvin Fishback is guilty: True or False?
True (0.6315943123389512)
Marvin Fishback has mean: True or False?
True (0.6104534962074417)
Marvin Fishback has motive: True or False?
True (0.6495786332146115)
Marvin Fishback has opportunity: True or False?
False (0.5736784476125245)
### Captain Kildare
- mean: True (0.9359345468898206)
- motive: True (0.9164093141890854)
- opportunity: True (0.8560919228396967)

### Latrisha Lanigan
- mean: False (0.2531218002341088)
- motive: False (0.12896334925938213)
- opportunity: False (0.31489264404972195)

### Mark Colson
- mean: False (0.20497775394601736)
- motive: False (0.19132769005022365)
- opportunity: False (0.38491214435073096)

### Marvin Fishback
- mean: False (0.3895465037925583)
- motive: False (0.3504213667853885)
- opportunity: False (0.5736784476125245)

The culprit is Captain Kildare.
In fact, it is Mark Colson.
## 5minutemystery-the-hidden-messenger
Jean is guilty: True or False?
True (0.8444089912414552)
Jean has mean: True or False?
True (0.9063219998220023)
Jean has motive: True or False?
True (0.9479621664653681)
Jean has opportunity: True or False?
True (0.8740772565226612)
Marie is guilty: True or False?
True (0.6001883860246252)
Marie has mean: True or False?
True (0.7599387683150569)
Marie has motive: True or False?
True (0.7541915239138703)
Marie has opportunity: True or False?
True (0.5727227727404994)
Molly is guilty: True or False?
True (0.6817267994905651)
Molly has mean: True or False?
True (0.7394224480813394)
Molly has motive: True or False?
True (0.8267118326419537)
Molly has opportunity: True or False?
True (0.8025555002781843)
Smith is guilty: True or False?
True (0.7033457082786769)
Smith has mean: True or False?
True (0.7074046739492601)
Smith has motive: True or False?
True (0.7885831565209055)
Smith has opportunity: True or False?
True (0.7468781552484828)
### Jean
- mean: True (0.9063219998220023)
- motive: True (0.9479621664653681)
- opportunity: True (0.8740772565226612)

### Marie
- mean: False (0.2400612316849431)
- motive: False (0.24580847608612966)
- opportunity: False (0.42727722725950057)

### Molly
- mean: False (0.2605775519186606)
- motive: False (0.1732881673580463)
- opportunity: False (0.19744449972181566)

### Smith
- mean: False (0.2925953260507399)
- motive: False (0.2114168434790945)
- opportunity: False (0.2531218447515172)

The culprit is Jean.
In fact, it is Smith.
## 5minutemystery-the-disappearing-dollhouse
Julia is guilty: True or False?
True (0.7356416476869558)
Julia has mean: True or False?
True (0.7806625377756776)
Julia has motive: True or False?
True (0.8238958672039278)
Julia has opportunity: True or False?
True (0.7130321332210621)
Kyle is guilty: True or False?
True (0.5879431210535583)
Kyle has mean: True or False?
True (0.7662937064012869)
Kyle has motive: True or False?
True (0.6029971163050526)
Kyle has opportunity: True or False?
True (0.5583269696343842)
Lucius is guilty: True or False?
True (0.673191669892235)
Lucius has mean: True or False?
True (0.642432441257838)
Lucius has motive: True or False?
True (0.642432441257838)
Lucius has opportunity: True or False?
False (0.5418937216067536)
Reg is guilty: True or False?
True (0.6270381219830087)
Reg has mean: True or False?
True (0.5755879969637064)
Reg has motive: True or False?
True (0.5832033352502285)
Reg has opportunity: True or False?
False (0.5292633777076584)
### Julia
- mean: True (0.7806625377756776)
- motive: True (0.8238958672039278)
- opportunity: True (0.7130321332210621)

### Kyle
- mean: False (0.2337062935987131)
- motive: False (0.3970028836949474)
- opportunity: False (0.4416730303656158)

### Lucius
- mean: False (0.35756755874216195)
- motive: False (0.35756755874216195)
- opportunity: False (0.5418937216067536)

### Reg
- mean: False (0.42441200303629356)
- motive: False (0.4167966647497715)
- opportunity: False (0.5292633777076584)

The culprit is Julia.
In fact, it is Reg.
## 5minutemystery-a-bear-a-dog-and-a-mystery
Mom is guilty: True or False?
False (0.5765419579552815)
Mom has mean: True or False?
False (0.615087818987177)
Mom has motive: True or False?
False (0.6766198919456847)
Mom has opportunity: True or False?
False (0.8474634858439474)
Old Mugger is guilty: True or False?
False (0.7468781552484828)
Old Mugger has mean: True or False?
True (0.6067314814064781)
Old Mugger has motive: True or False?
False (0.5282900215677746)
Old Mugger has opportunity: True or False?
False (0.8050197941712954)
Orville is guilty: True or False?
True (0.595492552580428)
Orville has mean: True or False?
True (0.5983121871760707)
Orville has motive: True or False?
True (0.7563575572780217)
Orville has opportunity: True or False?
False (0.5964331434971528)
Taylor is guilty: True or False?
True (0.5631377056275331)
Taylor has mean: True or False?
True (0.5438325284393795)
Taylor has motive: True or False?
True (0.6749080895533367)
Taylor has opportunity: True or False?
True (0.5234203246639862)
### Mom
- mean: False (0.615087818987177)
- motive: False (0.6766198919456847)
- opportunity: False (0.8474634858439474)

### Old Mugger
- mean: False (0.39326851859352185)
- motive: False (0.5282900215677746)
- opportunity: False (0.8050197941712954)

### Orville
- mean: True (0.5983121871760707)
- motive: True (0.7563575572780217)
- opportunity: True (0.4035668565028472)

### Taylor
- mean: False (0.45616747156062054)
- motive: False (0.3250919104466633)
- opportunity: False (0.47657967533601375)

The culprit is Orville.
In fact, it is Taylor.
## 5minutemystery-the-mystery-of-the-talented-cat
Edith is guilty: True or False?
True (0.7739005566220397)
Edith has mean: True or False?
True (0.7648916137833577)
Edith has motive: True or False?
True (0.7645401872124011)
Edith has opportunity: True or False?
True (0.6192410564568527)
Joshua Sellers is guilty: True or False?
True (0.8778961263000082)
Joshua Sellers has mean: True or False?
True (0.8969755785184792)
Joshua Sellers has motive: True or False?
True (0.8077641180140109)
Joshua Sellers has opportunity: True or False?
True (0.6406358487498992)
Muggles is guilty: True or False?
True (0.8494724067948436)
Muggles has mean: True or False?
True (0.8494724067948436)
Muggles has motive: True or False?
True (0.8316905440184192)
Muggles has opportunity: True or False?
True (0.7310585348819939)
Rick is guilty: True or False?
True (0.6584174547581384)
Rick has mean: True or False?
True (0.7074047371961694)
Rick has motive: True or False?
True (0.5282900215677746)
Rick has opportunity: True or False?
False (0.6206216296838327)
### Edith
- mean: False (0.23510838621664232)
- motive: False (0.23545981278759887)
- opportunity: False (0.3807589435431473)

### Joshua Sellers
- mean: False (0.1030244214815208)
- motive: False (0.19223588198598907)
- opportunity: False (0.3593641512501008)

### Muggles
- mean: True (0.8494724067948436)
- motive: True (0.8316905440184192)
- opportunity: True (0.7310585348819939)

### Rick
- mean: False (0.29259526280383064)
- motive: False (0.4717099784322254)
- opportunity: False (0.6206216296838327)

The culprit is Muggles.
In fact, it is Edith.
## 5minutemystery-the-haunted-portrait
Jonathan Ingersoll is guilty: True or False?
True (0.8509646659219744)
Jonathan Ingersoll has mean: True or False?
True (0.8980534699860239)
Jonathan Ingersoll has motive: True or False?
True (0.8294919722593475)
Jonathan Ingersoll has opportunity: True or False?
True (0.7826624547920057)
Lucille Cameron is guilty: True or False?
True (0.8344069148356309)
Lucille Cameron has mean: True or False?
Map:  89%|████████▊ | 180/203 [1:19:49<10:42, 27.93s/ examples]Map:  89%|████████▉ | 181/203 [1:20:09<09:23, 25.59s/ examples]Map:  90%|████████▉ | 182/203 [1:20:38<09:18, 26.58s/ examples]Map:  90%|█████████ | 183/203 [1:21:06<09:01, 27.07s/ examples]True (0.9362850185952675)
Lucille Cameron has motive: True or False?
True (0.8795611817678315)
Lucille Cameron has opportunity: True or False?
True (0.8643104392003704)
Marion Montgomery is guilty: True or False?
True (0.8216173055802608)
Marion Montgomery has mean: True or False?
True (0.8261514850267767)
Marion Montgomery has motive: True or False?
True (0.8204694405411458)
Marion Montgomery has opportunity: True or False?
True (0.7988152492192591)
Teddy Auchinlech is guilty: True or False?
True (0.7461389980806673)
Teddy Auchinlech has mean: True or False?
True (0.8587185689177256)
Teddy Auchinlech has motive: True or False?
True (0.8122723669190336)
Teddy Auchinlech has opportunity: True or False?
True (0.7732163648437078)
### Jonathan Ingersoll
- mean: False (0.10194653001397613)
- motive: False (0.17050802774065255)
- opportunity: False (0.2173375452079943)

### Lucille Cameron
- mean: True (0.9362850185952675)
- motive: True (0.8795611817678315)
- opportunity: True (0.8643104392003704)

### Marion Montgomery
- mean: False (0.1738485149732233)
- motive: False (0.1795305594588542)
- opportunity: False (0.20118475078074094)

### Teddy Auchinlech
- mean: False (0.14128143108227442)
- motive: False (0.1877276330809664)
- opportunity: False (0.22678363515629218)

The culprit is Lucille Cameron.
In fact, it is Jonathan Ingersoll.
## 5minutemystery-the-classic-automobile-mystery
Gary Riggs is guilty: True or False?
True (0.8068525816617738)
Gary Riggs has mean: True or False?
True (0.6261242000979097)
Gary Riggs has motive: True or False?
True (0.5679366075542497)
Gary Riggs has opportunity: True or False?
False (0.7431679939957333)
Gerald "Doc" McCroy is guilty: True or False?
True (0.5755879969637064)
Gerald "Doc" McCroy has mean: True or False?
False (0.5708098341193941)
Gerald "Doc" McCroy has motive: True or False?
True (0.5679366075542497)
Gerald "Doc" McCroy has opportunity: True or False?
False (0.7975568155246964)
Mike Benson is guilty: True or False?
True (0.6160122877297346)
Mike Benson has mean: True or False?
True (0.6104534962074417)
Mike Benson has motive: True or False?
False (0.5165954111147137)
Mike Benson has opportunity: True or False?
False (0.8444089912414552)
Tommy Flowers is guilty: True or False?
True (0.5851011336505011)
Tommy Flowers has mean: True or False?
True (0.7178037814283548)
Tommy Flowers has motive: True or False?
True (0.6279512069990912)
Tommy Flowers has opportunity: True or False?
False (0.7431679939957333)
### Gary Riggs
- mean: False (0.3738757999020903)
- motive: False (0.4320633924457503)
- opportunity: False (0.7431679939957333)

### Gerald "Doc" McCroy
- mean: False (0.5708098341193941)
- motive: False (0.4320633924457503)
- opportunity: False (0.7975568155246964)

### Mike Benson
- mean: False (0.3895465037925583)
- motive: False (0.5165954111147137)
- opportunity: False (0.8444089912414552)

### Tommy Flowers
- mean: True (0.7178037814283548)
- motive: True (0.6279512069990912)
- opportunity: True (0.2568320060042667)

The culprit is Tommy Flowers.
In fact, it is Gerald "Doc" McCroy.
## 5minutemystery-rocks-and-feathers
Barley is guilty: True or False?
True (0.8464508054137014)
Barley has mean: True or False?
True (0.9073122118500465)
Barley has motive: True or False?
True (0.8362873170845201)
Barley has opportunity: True or False?
True (0.8233283740192667)
Bertha is guilty: True or False?
True (0.9116528030198908)
Bertha has mean: True or False?
True (0.8534247816107388)
Bertha has motive: True or False?
True (0.9223425402045055)
Bertha has opportunity: True or False?
True (0.862930245043327)
Joseph is guilty: True or False?
True (0.8596637847360897)
Joseph has mean: True or False?
True (0.8652240590801695)
Joseph has motive: True or False?
True (0.8727816933272936)
Joseph has opportunity: True or False?
True (0.7981867775042927)
Tom is guilty: True or False?
True (0.8322366416985943)
Tom has mean: True or False?
True (0.8647679145346777)
Tom has motive: True or False?
True (0.8652240590801695)
Tom has opportunity: True or False?
True (0.8068525816617738)
### Barley
- mean: False (0.09268778814995349)
- motive: False (0.1637126829154799)
- opportunity: False (0.17667162598073327)

### Bertha
- mean: True (0.8534247816107388)
- motive: True (0.9223425402045055)
- opportunity: True (0.862930245043327)

### Joseph
- mean: False (0.13477594091983047)
- motive: False (0.1272183066727064)
- opportunity: False (0.20181322249570732)

### Tom
- mean: False (0.13523208546532228)
- motive: False (0.13477594091983047)
- opportunity: False (0.19314741833822624)

The culprit is Bertha.
In fact, it is Tom.
## 5minutemystery-who-is-telling-the-truth
Bill Flowers is guilty: True or False?
True (0.8998277786460391)
Bill Flowers has mean: True or False?
True (0.9730365275631271)
Bill Flowers has motive: True or False?
True (0.8860265599597172)
Bill Flowers has opportunity: True or False?
True (0.854884620116169)
Jane Neal is guilty: True or False?
True (0.8883720049821552)
Jane Neal has mean: True or False?
True (0.9606574760904091)
Jane Neal has motive: True or False?
True (0.8727817583545995)
Jane Neal has opportunity: True or False?
True (0.844921525814193)
Jimmy Smith is guilty: True or False?
True (0.955152093302995)
Jimmy Smith has mean: True or False?
True (0.9661560069290531)
Jimmy Smith has motive: True or False?
True (0.8955226517597132)
Jimmy Smith has opportunity: True or False?
True (0.9139841191734227)
Larry Gerard is guilty: True or False?
True (0.9273633336539081)
Larry Gerard has mean: True or False?
True (0.9532750830575984)
Larry Gerard has motive: True or False?
True (0.8423451152856819)
Larry Gerard has opportunity: True or False?
True (0.8392075831473667)
Paula Newsome is guilty: True or False?
True (0.9260365949489886)
Paula Newsome has mean: True or False?
True (0.971563935671788)
Paula Newsome has motive: True or False?
True (0.8489722037469682)
Paula Newsome has opportunity: True or False?
True (0.8807970337584357)
### Bill Flowers
- mean: False (0.026963472436872915)
- motive: False (0.11397344004028276)
- opportunity: False (0.14511537988383105)

### Jane Neal
- mean: False (0.03934252390959092)
- motive: False (0.12721824164540052)
- opportunity: False (0.155078474185807)

### Jimmy Smith
- mean: True (0.9661560069290531)
- motive: True (0.8955226517597132)
- opportunity: True (0.9139841191734227)

### Larry Gerard
- mean: False (0.04672491694240155)
- motive: False (0.1576548847143181)
- opportunity: False (0.16079241685263335)

### Paula Newsome
- mean: False (0.028436064328211996)
- motive: False (0.15102779625303175)
- opportunity: False (0.11920296624156435)

The culprit is Jimmy Smith.
In fact, it is Paula Newsome.
## 5minutemystery-ask-marthathe-identity-thief
Grace Means is guilty: True or False?
True (0.874934615163517)
Grace Means has mean: True or False?
True (0.9324533354081785)
Grace Means has motive: True or False?
True (0.9149009617112335)
Grace Means has opportunity: True or False?
True (0.8056321690561029)
Joan Colthrop is guilty: True or False?
True (0.8910549302065384)
Joan Colthrop has mean: True or False?
True (0.9447913165152162)
Joan Colthrop has motive: True or False?
True (0.8770561879413864)
Joan Colthrop has opportunity: True or False?
True (0.6697448487720212)
Laura Parsons is guilty: True or False?
True (0.9181872635464632)
Laura Parsons has mean: True or False?
True (0.9284088027271398)
Laura Parsons has motive: True or False?
True (0.8068526417769779)
Laura Parsons has opportunity: True or False?
True (0.686790293772966)
Maybelle Johnson is guilty: True or False?
True (0.8397339530959691)
Maybelle Johnson has mean: True or False?
True (0.8514594452543962)
Maybelle Johnson has motive: True or False?
True (0.8633915828320894)
Maybelle Johnson has opportunity: True or False?
True (0.6067314814064781)
### Grace Means
- mean: True (0.9324533354081785)
- motive: True (0.9149009617112335)
- opportunity: True (0.8056321690561029)

### Joan Colthrop
- mean: False (0.055208683484783805)
- motive: False (0.1229438120586136)
- opportunity: False (0.33025515122797877)

### Laura Parsons
- mean: False (0.07159119727286023)
- motive: False (0.1931473582230221)
Map:  91%|█████████ | 184/203 [1:21:28<08:01, 25.34s/ examples]Map:  91%|█████████ | 185/203 [1:21:53<07:36, 25.37s/ examples]Map:  92%|█████████▏| 186/203 [1:22:11<06:35, 23.26s/ examples]Map:  92%|█████████▏| 187/203 [1:22:33<06:05, 22.84s/ examples]Map:  93%|█████████▎| 188/203 [1:22:57<05:45, 23.01s/ examples]- opportunity: False (0.31320970622703403)

### Maybelle Johnson
- mean: False (0.1485405547456038)
- motive: False (0.1366084171679106)
- opportunity: False (0.39326851859352185)

The culprit is Grace Means.
In fact, it is Joan Colthrop.
## 5minutemystery-ask-marthathe-pickpocket
Johnny Anderson is guilty: True or False?
True (0.7994422859301654)
Johnny Anderson has mean: True or False?
True (0.8092759828926619)
Johnny Anderson has motive: True or False?
True (0.8013146490010521)
Johnny Anderson has opportunity: True or False?
True (0.7534666630720156)
Morris Emerson is guilty: True or False?
True (0.8402589628813668)
Morris Emerson has mean: True or False?
True (0.7669925046333297)
Morris Emerson has motive: True or False?
True (0.7905303264811482)
Morris Emerson has opportunity: True or False?
True (0.6884683992569801)
Sarah Browne is guilty: True or False?
True (0.7799929399351836)
Sarah Browne has mean: True or False?
True (0.8652240590801695)
Sarah Browne has motive: True or False?
True (0.726425644352388)
Sarah Browne has opportunity: True or False?
True (0.6306849143569856)
Tom Blankenship is guilty: True or False?
True (0.7981867775042927)
Tom Blankenship has mean: True or False?
True (0.8092759828926619)
Tom Blankenship has motive: True or False?
True (0.811078188867804)
Tom Blankenship has opportunity: True or False?
True (0.6697448487720212)
### Johnny Anderson
- mean: True (0.8092759828926619)
- motive: True (0.8013146490010521)
- opportunity: True (0.7534666630720156)

### Morris Emerson
- mean: False (0.23300749536667031)
- motive: False (0.20946967351885182)
- opportunity: False (0.3115316007430199)

### Sarah Browne
- mean: False (0.13477594091983047)
- motive: False (0.273574355647612)
- opportunity: False (0.3693150856430144)

### Tom Blankenship
- mean: False (0.1907240171073381)
- motive: False (0.18892181113219597)
- opportunity: False (0.33025515122797877)

The culprit is Johnny Anderson.
In fact, it is Tom Blankenship.
## 5minutemystery-diamond-deception
Horace is guilty: True or False?
True (0.6680145240815963)
Horace has mean: True or False?
True (0.8524448242555318)
Horace has motive: True or False?
True (0.6984323202883935)
Horace has opportunity: True or False?
True (0.708212608228071)
Jake is guilty: True or False?
True (0.5679366075542497)
Jake has mean: True or False?
True (0.8056321690561029)
Jake has motive: True or False?
True (0.7348812183274223)
Jake has opportunity: True or False?
True (0.7394224480813394)
John is guilty: True or False?
True (0.6566582306092376)
John has mean: True or False?
True (0.8820219652716884)
John has motive: True or False?
True (0.8444089912414552)
John has opportunity: True or False?
True (0.8092759828926619)
Lewis is guilty: True or False?
True (0.6740504984987916)
Lewis has mean: True or False?
True (0.8860265599597172)
Lewis has motive: True or False?
True (0.7453983509653428)
Lewis has opportunity: True or False?
True (0.7409249009267298)
### Horace
- mean: False (0.1475551757444682)
- motive: False (0.3015676797116065)
- opportunity: False (0.29178739177192903)

### Jake
- mean: False (0.1943678309438971)
- motive: False (0.26511878167257774)
- opportunity: False (0.2605775519186606)

### John
- mean: True (0.8820219652716884)
- motive: True (0.8444089912414552)
- opportunity: True (0.8092759828926619)

### Lewis
- mean: False (0.11397344004028276)
- motive: False (0.2546016490346572)
- opportunity: False (0.2590750990732702)

The culprit is John.
In fact, it is Lewis.
## 5minutemystery-where-is-matthew
Andy's bedroom is guilty: True or False?
True (0.5592900581575188)
Andy's bedroom has mean: True or False?
True (0.8787311338092536)
Andy's bedroom has motive: True or False?
True (0.8158201638039532)
Andy's bedroom has opportunity: True or False?
True (0.5650587130190106)
Matthew's bedroom is guilty: True or False?
True (0.6343168082332088)
Matthew's bedroom has mean: True or False?
True (0.9142907234091052)
Matthew's bedroom has motive: True or False?
True (0.8606036289596553)
Matthew's bedroom has opportunity: True or False?
True (0.784649255215384)
The garage is guilty: True or False?
True (0.7577943897558946)
The garage has mean: True or False?
True (0.8044059309478723)
The garage has motive: True or False?
True (0.7170118721569225)
The garage has opportunity: True or False?
True (0.7416740115009234)
The hall closet is guilty: True or False?
True (0.5224458497983033)
The hall closet has mean: True or False?
True (0.7813306496768853)
The hall closet has motive: True or False?
True (0.7937461674149602)
The hall closet has opportunity: True or False?
True (0.7527403228571042)
The tree house is guilty: True or False?
True (0.5535053004623279)
The tree house has mean: True or False?
True (0.8244619332958376)
The tree house has motive: True or False?
True (0.8044059309478723)
The tree house has opportunity: True or False?
True (0.6645403391983984)
### Andy's bedroom
- mean: False (0.1212688661907464)
- motive: False (0.18417983619604683)
- opportunity: False (0.43494128698098944)

### Matthew's bedroom
- mean: True (0.9142907234091052)
- motive: True (0.8606036289596553)
- opportunity: True (0.784649255215384)

### The garage
- mean: False (0.19559406905212773)
- motive: False (0.2829881278430775)
- opportunity: False (0.2583259884990766)

### The hall closet
- mean: False (0.21866935032311474)
- motive: False (0.20625383258503982)
- opportunity: False (0.24725967714289576)

### The tree house
- mean: False (0.1755380667041624)
- motive: False (0.19559406905212773)
- opportunity: False (0.3354596608016016)

The culprit is Matthew's bedroom.
In fact, it is The tree house.
## 5minutemystery-the-mysterious-gift
CIndy is guilty: True or False?
True (0.7394223819718238)
CIndy has mean: True or False?
True (0.7813306496768853)
CIndy has motive: True or False?
True (0.72951977676791)
CIndy has opportunity: True or False?
True (0.5156198737738186)
Josie's mother is guilty: True or False?
False (0.6297746298200823)
Josie's mother has mean: True or False?
False (0.8994750975198919)
Josie's mother has motive: True or False?
True (0.595492552580428)
Josie's mother has opportunity: True or False?
False (0.8074606715677252)
Lester is guilty: True or False?
True (0.8122724274380432)
Lester has mean: True or False?
True (0.8365545874520802)
Lester has motive: True or False?
True (0.6992544513448877)
Lester has opportunity: True or False?
False (0.5097644370426659)
Lorraine is guilty: True or False?
True (0.6361271113853048)
Lorraine has mean: True or False?
True (0.7154240000492645)
Lorraine has motive: True or False?
True (0.7065955344877805)
Lorraine has opportunity: True or False?
False (0.5964331434971528)
### CIndy
- mean: False (0.21866935032311474)
- motive: False (0.27048022323209)
- opportunity: False (0.48438012622618143)

### Josie's mother
- mean: False (0.8994750975198919)
- motive: False (0.404507447419572)
- opportunity: False (0.8074606715677252)

### Lester
- mean: True (0.8365545874520802)
- motive: True (0.6992544513448877)
- opportunity: True (0.49023556295733406)

### Lorraine
- mean: False (0.28457599995073546)
- motive: False (0.29340446551221955)
- opportunity: False (0.5964331434971528)

The culprit is Lester.
In fact, it is Lorraine.
## 5minutemystery-perry-mason-and-the-high-school-crush-murder
Morris Ingalls is guilty: True or False?
True (0.9364013693337395)
Morris Ingalls has mean: True or False?
True (0.8062431235779619)
Morris Ingalls has motive: True or False?
True (0.9394706502722077)
Morris Ingalls has opportunity: True or False?
True (0.8982321647536474)
Randolph Johnson is guilty: True or False?
True (0.8640812064457842)
Randolph Johnson has mean: True or False?
True (0.8840392847025188)
Randolph Johnson has motive: True or False?
True (0.8454326455643386)
Randolph Johnson has opportunity: True or False?
True (0.8360197583769845)
Sarah Conrad is guilty: True or False?
True (0.7969253675907205)
Sarah Conrad has mean: True or False?
True (0.6893056096647525)
Sarah Conrad has motive: True or False?
True (0.8267117710471246)
Sarah Conrad has opportunity: True or False?
True (0.8278281666221954)
Tom Gooding is guilty: True or False?
Map:  93%|█████████▎| 189/203 [1:23:32<06:14, 26.73s/ examples]Map:  94%|█████████▎| 190/203 [1:23:57<05:41, 26.28s/ examples]Map:  94%|█████████▍| 191/203 [1:24:17<04:53, 24.42s/ examples]Map:  95%|█████████▍| 192/203 [1:24:37<04:11, 22.88s/ examples]Map:  95%|█████████▌| 193/203 [1:25:03<03:59, 23.91s/ examples]True (0.9309620852900756)
Tom Gooding has mean: True or False?
True (0.9121235591541035)
Tom Gooding has motive: True or False?
True (0.8893367679552574)
Tom Gooding has opportunity: True or False?
True (0.9094255002859922)
### Morris Ingalls
- mean: False (0.1937568764220381)
- motive: False (0.060529349727792336)
- opportunity: False (0.10176783524635258)

### Randolph Johnson
- mean: False (0.1159607152974812)
- motive: False (0.15456735443566139)
- opportunity: False (0.1639802416230155)

### Sarah Conrad
- mean: False (0.3106943903352475)
- motive: False (0.17328822895287543)
- opportunity: False (0.17217183337780462)

### Tom Gooding
- mean: True (0.9121235591541035)
- motive: True (0.8893367679552574)
- opportunity: True (0.9094255002859922)

The culprit is Tom Gooding.
In fact, it is Morris Ingalls.
## 5minutemystery-who-stole-super-tuesday
Barry is guilty: True or False?
True (0.8803862939824989)
Barry has mean: True or False?
True (0.9032942081209032)
Barry has motive: True or False?
True (0.9335520893498362)
Barry has opportunity: True or False?
True (0.809577288641998)
Ricky Churrelo is guilty: True or False?
True (0.7680380401429294)
Ricky Churrelo has mean: True or False?
False (0.6169357925086439)
Ricky Churrelo has motive: True or False?
True (0.6992543888266708)
Ricky Churrelo has opportunity: True or False?
False (0.7592253761865491)
Simon Knowles is guilty: True or False?
True (0.9298236969789664)
Simon Knowles has mean: True or False?
True (0.5525396910980834)
Simon Knowles has motive: True or False?
True (0.8143482752411424)
Simon Knowles has opportunity: True or False?
False (0.7325918709325988)
Xavier Ericksen is guilty: True or False?
True (0.8258708137274083)
Xavier Ericksen has mean: True or False?
False (0.7371581892031299)
Xavier Ericksen has motive: True or False?
True (0.5122046514309807)
Xavier Ericksen has opportunity: True or False?
False (0.8509646659219744)
### Barry
- mean: True (0.9032942081209032)
- motive: True (0.9335520893498362)
- opportunity: True (0.809577288641998)

### Ricky Churrelo
- mean: False (0.6169357925086439)
- motive: False (0.3007456111733292)
- opportunity: False (0.7592253761865491)

### Simon Knowles
- mean: False (0.44746030890191657)
- motive: False (0.1856517247588576)
- opportunity: False (0.7325918709325988)

### Xavier Ericksen
- mean: False (0.7371581892031299)
- motive: False (0.4877953485690193)
- opportunity: False (0.8509646659219744)

The culprit is Barry.
In fact, it is Simon Knowles.
## 5minutemystery-the-missing-son
Caleb is guilty: True or False?
True (0.8071567978738078)
Caleb has mean: True or False?
True (0.9178934131644976)
Caleb has motive: True or False?
True (0.9536218061663073)
Caleb has opportunity: True or False?
True (0.8563323578093363)
Conner is guilty: True or False?
True (0.7272012283179254)
Conner has mean: True or False?
True (0.934155284694701)
Conner has motive: True or False?
True (0.9515039936355008)
Conner has opportunity: True or False?
True (0.9076402191395381)
Jordan is guilty: True or False?
True (0.7559974119430289)
Jordan has mean: True or False?
True (0.8365545874520802)
Jordan has motive: True or False?
True (0.9046505665674094)
Jordan has opportunity: True or False?
True (0.5755880655791468)
Kyle is guilty: True or False?
True (0.7997552678397243)
Kyle has mean: True or False?
True (0.8454326455643386)
Kyle has motive: True or False?
True (0.9008791478232747)
Kyle has opportunity: True or False?
True (0.7302898278778687)
### Caleb
- mean: False (0.08210658683550243)
- motive: False (0.04637819383369268)
- opportunity: False (0.14366764219066375)

### Conner
- mean: True (0.934155284694701)
- motive: True (0.9515039936355008)
- opportunity: True (0.9076402191395381)

### Jordan
- mean: False (0.16344541254791978)
- motive: False (0.09534943343259061)
- opportunity: False (0.42441193442085323)

### Kyle
- mean: False (0.15456735443566139)
- motive: False (0.09912085217672528)
- opportunity: False (0.26971017212213133)

The culprit is Conner.
In fact, it is Caleb.
## 5minutemystery-the-stolen-cupcake
Angelica is guilty: True or False?
True (0.5185461538431656)
Angelica has mean: True or False?
False (0.6926419789019715)
Angelica has motive: True or False?
True (0.720171518230031)
Angelica has opportunity: True or False?
False (0.5312093625105829)
Caedon is guilty: True or False?
True (0.6057990946577705)
Caedon has mean: True or False?
True (0.5660185351323219)
Caedon has motive: True or False?
True (0.7613611200983542)
Caedon has opportunity: True or False?
False (0.5097643762740132)
Ross is guilty: True or False?
True (0.5813030649269245)
Ross has mean: True or False?
True (0.612309626324874)
Ross has motive: True or False?
True (0.8539127077831877)
Ross has opportunity: True or False?
True (0.6513548405484016)
Tony is guilty: True or False?
False (0.7541915239138703)
Tony has mean: True or False?
False (0.7620701143808404)
Tony has motive: True or False?
True (0.5888891269161294)
Tony has opportunity: True or False?
False (0.5631377056275331)
### Angelica
- mean: False (0.6926419789019715)
- motive: False (0.279828481769969)
- opportunity: False (0.5312093625105829)

### Caedon
- mean: False (0.4339814648676781)
- motive: False (0.23863887990164578)
- opportunity: False (0.5097643762740132)

### Ross
- mean: True (0.612309626324874)
- motive: True (0.8539127077831877)
- opportunity: True (0.6513548405484016)

### Tony
- mean: False (0.7620701143808404)
- motive: False (0.4111108730838706)
- opportunity: False (0.5631377056275331)

The culprit is Ross.
In fact, it is Caedon.
## 5minutemystery-school-trip
Beth is guilty: True or False?
False (0.7476159279883341)
Beth has mean: True or False?
True (0.7577943897558946)
Beth has motive: True or False?
True (0.7527403228571042)
Beth has opportunity: True or False?
False (0.6749080895533367)
Damon is guilty: True or False?
True (0.5879430860094185)
Damon has mean: True or False?
True (0.8289388437432279)
Damon has motive: True or False?
True (0.6424325178417575)
Damon has opportunity: True or False?
True (0.6714705702070799)
Leo is guilty: True or False?
False (0.5467381591701916)
Leo has mean: True or False?
True (0.6943026818003076)
Leo has motive: True or False?
True (0.8795611817678315)
Leo has opportunity: True or False?
True (0.7556369876990674)
Mr. Michael's is guilty: True or False?
False (0.642432441257838)
Mr. Michael's has mean: True or False?
True (0.7931058945535956)
Mr. Michael's has motive: True or False?
False (0.6076631662366868)
Mr. Michael's has opportunity: True or False?
False (0.7704647687904915)
The Seniors is guilty: True or False?
True (0.5389832197022594)
The Seniors has mean: True or False?
True (0.5784481782924303)
The Seniors has motive: True or False?
True (0.5370413742099674)
The Seniors has opportunity: True or False?
False (0.842345065078002)
### Beth
- mean: False (0.24220561024410536)
- motive: False (0.24725967714289576)
- opportunity: False (0.6749080895533367)

### Damon
- mean: False (0.1710611562567721)
- motive: False (0.3575674821582425)
- opportunity: False (0.3285294297929201)

### Leo
- mean: True (0.6943026818003076)
- motive: True (0.8795611817678315)
- opportunity: True (0.7556369876990674)

### Mr. Michael's
- mean: False (0.2068941054464044)
- motive: False (0.6076631662366868)
- opportunity: False (0.7704647687904915)

### The Seniors
- mean: False (0.42155182170756966)
- motive: False (0.46295862579003255)
- opportunity: False (0.842345065078002)

The culprit is Leo.
In fact, it is The Seniors.
## 5minutemystery-arsonist-attack
Jade Foster is guilty: True or False?
True (0.9449946880768697)
Jade Foster has mean: True or False?
True (0.9302051049548884)
Jade Foster has motive: True or False?
True (0.9082930095862076)
Jade Foster has opportunity: True or False?
True (0.8534247816107388)
Jock Matt is guilty: True or False?
True (0.9331876642092066)
Jock Matt has mean: True or False?
True (0.9346342066470359)
Jock Matt has motive: True or False?
True (0.865678909174824)
Jock Matt has opportunity: True or False?
True (0.8638516611889259)
Madelyn Reader is guilty: True or False?
True (0.9567959302164903)
Madelyn Reader has mean: True or False?Map:  96%|█████████▌| 194/203 [1:25:32<03:49, 25.55s/ examples]Map:  96%|█████████▌| 195/203 [1:25:54<03:15, 24.40s/ examples]Map:  97%|█████████▋| 196/203 [1:26:14<02:42, 23.20s/ examples]Map:  97%|█████████▋| 197/203 [1:26:38<02:19, 23.26s/ examples]
True (0.9341553473346962)
Madelyn Reader has motive: True or False?
True (0.9367495172436676)
Madelyn Reader has opportunity: True or False?
True (0.7505527730327083)
Max Crabgrass is guilty: True or False?
True (0.9252299038987163)
Max Crabgrass has mean: True or False?
True (0.9381240005131491)
Max Crabgrass has motive: True or False?
True (0.9056565771882901)
Max Crabgrass has opportunity: True or False?
True (0.8856314413364714)
Security Guard is guilty: True or False?
True (0.9543079126608008)
Security Guard has mean: True or False?
True (0.9273632783787477)
Security Guard has motive: True or False?
True (0.9276260107813639)
Security Guard has opportunity: True or False?
True (0.8397339530959691)
### Jade Foster
- mean: False (0.0697948950451116)
- motive: False (0.09170699041379238)
- opportunity: False (0.14657521838926124)

### Jock Matt
- mean: False (0.06536579335296411)
- motive: False (0.13432109082517596)
- opportunity: False (0.13614833881107413)

### Madelyn Reader
- mean: False (0.06584465266530382)
- motive: False (0.06325048275633238)
- opportunity: False (0.2494472269672917)

### Max Crabgrass
- mean: True (0.9381240005131491)
- motive: True (0.9056565771882901)
- opportunity: True (0.8856314413364714)

### Security Guard
- mean: False (0.07263672162125234)
- motive: False (0.07237398921863614)
- opportunity: False (0.1602660469040309)

The culprit is Max Crabgrass.
In fact, it is Jade Foster.
## 5minutemystery-investigation-sabotager
Emma is guilty: True or False?
True (0.9149009617112335)
Emma has mean: True or False?
True (0.9073122118500465)
Emma has motive: True or False?
True (0.9333093737798925)
Emma has opportunity: True or False?
True (0.9084555478510448)
Mary is guilty: True or False?
True (0.942400812874096)
Mary has mean: True or False?
True (0.9114953904850286)
Mary has motive: True or False?
True (0.9465966835599983)
Mary has opportunity: True or False?
True (0.9529258022651363)
Peter is guilty: True or False?
True (0.9187722824991111)
Peter has mean: True or False?
True (0.8294920340613177)
Peter has motive: True or False?
True (0.8824278665848695)
Peter has opportunity: True or False?
True (0.8918110736745599)
Tim is guilty: True or False?
True (0.8643104392003704)
Tim has mean: True or False?
True (0.8991213421091365)
Tim has motive: True or False?
True (0.884837803442546)
Tim has opportunity: True or False?
True (0.8250265688168699)
Valerie is guilty: True or False?
True (0.873646620599733)
Valerie has mean: True or False?
True (0.9343951361750445)
Valerie has motive: True or False?
True (0.9392481417861557)
Valerie has opportunity: True or False?
True (0.8960695891821668)
### Emma
- mean: False (0.09268778814995349)
- motive: False (0.06669062622010746)
- opportunity: False (0.09154445214895524)

### Mary
- mean: True (0.9114953904850286)
- motive: True (0.9465966835599983)
- opportunity: True (0.9529258022651363)

### Peter
- mean: False (0.17050796593868234)
- motive: False (0.11757213341513051)
- opportunity: False (0.10818892632544008)

### Tim
- mean: False (0.10087865789086348)
- motive: False (0.11516219655745397)
- opportunity: False (0.17497343118313013)

### Valerie
- mean: False (0.06560486382495545)
- motive: False (0.06075185821384432)
- opportunity: False (0.10393041081783316)

The culprit is Mary.
In fact, it is Emma.
## 5minutemystery-the-presidential-smear-campaint-a-jacelyn-drew-mystery
Brittany is guilty: True or False?
True (0.8255897087847518)
Brittany has mean: True or False?
True (0.8013146490010521)
Brittany has motive: True or False?
True (0.84440905415483)
Brittany has opportunity: True or False?
True (0.5907792634380938)
Isis is guilty: True or False?
True (0.9446893339351747)
Isis has mean: True or False?
True (0.7498207054286419)
Isis has motive: True or False?
True (0.905989824801558)
Isis has opportunity: True or False?
True (0.6513548405484016)
Marie is guilty: True or False?
True (0.7017130830397807)
Marie has mean: True or False?
True (0.7178038242127955)
Marie has motive: True or False?
True (0.7931059536445917)
Marie has opportunity: True or False?
True (0.6242935781683038)
Norma is guilty: True or False?
True (0.8056321690561029)
Norma has mean: True or False?
True (0.60859406896259)
Norma has motive: True or False?
True (0.8267117710471246)
Norma has opportunity: True or False?
True (0.5822535180679596)
### Brittany
- mean: False (0.1986853509989479)
- motive: False (0.15559094584516997)
- opportunity: False (0.40922073656190616)

### Isis
- mean: True (0.7498207054286419)
- motive: True (0.905989824801558)
- opportunity: True (0.6513548405484016)

### Marie
- mean: False (0.28219617578720446)
- motive: False (0.2068940463554083)
- opportunity: False (0.3757064218316962)

### Norma
- mean: False (0.39140593103740995)
- motive: False (0.17328822895287543)
- opportunity: False (0.41774648193204045)

The culprit is Isis.
In fact, it is Isis.
## 5minutemystery-the-sunday-mystery
Jack Jackson is guilty: True or False?
True (0.8740772044235984)
Jack Jackson has mean: True or False?
True (0.8601343090488404)
Jack Jackson has motive: True or False?
True (0.779321849347754)
Jack Jackson has opportunity: True or False?
False (0.525368812147771)
Jimmy Jackson is guilty: True or False?
True (0.8322366416985943)
Jimmy Jackson has mean: True or False?
True (0.8624675215861032)
Jimmy Jackson has motive: True or False?
True (0.8128672807499561)
Jimmy Jackson has opportunity: True or False?
True (0.5302364729224919)
Jon Jackson is guilty: True or False?
True (0.8553685501761973)
Jon Jackson has mean: True or False?
True (0.9022656660556747)
Jon Jackson has motive: True or False?
True (0.8940516749601143)
Jon Jackson has opportunity: True or False?
True (0.6714705702070799)
Maria Jackson is guilty: True or False?
True (0.8016254254291421)
Maria Jackson has mean: True or False?
True (0.8840392847025188)
Maria Jackson has motive: True or False?
True (0.879146760693242)
Maria Jackson has opportunity: True or False?
True (0.6557770400181139)
Spot is guilty: True or False?
True (0.6783269591477166)
Spot has mean: True or False?
True (0.8692713407917644)
Spot has motive: True or False?
True (0.7937462383814009)
Spot has opportunity: True or False?
True (0.5869964306477841)
### Jack Jackson
- mean: False (0.13986569095115964)
- motive: False (0.22067815065224605)
- opportunity: False (0.525368812147771)

### Jimmy Jackson
- mean: False (0.13753247841389682)
- motive: False (0.18713271925004393)
- opportunity: False (0.4697635270775081)

### Jon Jackson
- mean: True (0.9022656660556747)
- motive: True (0.8940516749601143)
- opportunity: True (0.6714705702070799)

### Maria Jackson
- mean: False (0.1159607152974812)
- motive: False (0.12085323930675795)
- opportunity: False (0.3442229599818861)

### Spot
- mean: False (0.13072865920823562)
- motive: False (0.2062537616185991)
- opportunity: False (0.41300356935221594)

The culprit is Jon Jackson.
In fact, it is Spot.
## 5minutemystery-the-mystery-of-heritage
Jack Anderson is guilty: True or False?
True (0.9564311500981832)
Jack Anderson has mean: True or False?
True (0.8850366506597954)
Jack Anderson has motive: True or False?
True (0.9381240005131491)
Jack Anderson has opportunity: True or False?
True (0.911809984585868)
Jessica Anderson is guilty: True or False?
True (0.9310874934413855)
Jessica Anderson has mean: True or False?
True (0.9029524325377104)
Jessica Anderson has motive: True or False?
True (0.8828325273478573)
Jessica Anderson has opportunity: True or False?
True (0.8221891570741111)
Martha Anderson is guilty: True or False?
True (0.9354645628936168)
Martha Anderson has mean: True or False?
True (0.8670358119601653)
Martha Anderson has motive: True or False?
True (0.9099069836112468)
Martha Anderson has opportunity: True or False?
True (0.8080671968507699)
Mrs. Neil is guilty: True or False?
True (0.9553191057869168)
Mrs. Neil has mean: True or False?
True (0.9537942396657707)
Mrs. Neil has motive: True or False?
True (0.969324171790829)
Mrs. Neil has opportunity: True or False?
True (0.9553191057869168)
### Jack Anderson
- mean: False (0.11496334934020458)
- motive: False (0.06187599948685085)
Map:  98%|█████████▊| 198/203 [1:26:54<01:45, 21.09s/ examples]Map:  98%|█████████▊| 199/203 [1:27:06<01:14, 18.52s/ examples]Map:  99%|█████████▊| 200/203 [1:27:28<00:58, 19.56s/ examples]Map:  99%|█████████▉| 201/203 [1:27:46<00:38, 19.04s/ examples]Map: 100%|█████████▉| 202/203 [1:28:08<00:19, 19.93s/ examples]- opportunity: False (0.08819001541413196)

### Jessica Anderson
- mean: False (0.0970475674622896)
- motive: False (0.11716747265214267)
- opportunity: False (0.1778108429258889)

### Martha Anderson
- mean: False (0.13296418803983467)
- motive: False (0.09009301638875322)
- opportunity: False (0.1919328031492301)

### Mrs. Neil
- mean: True (0.9537942396657707)
- motive: True (0.969324171790829)
- opportunity: True (0.9553191057869168)

The culprit is Mrs. Neil.
In fact, it is Jessica Anderson.
## 5minutemystery-murder-of-the-actor
Bruce Whittingley is guilty: True or False?
True (0.8714748565614324)
Bruce Whittingley has mean: True or False?
True (0.8300437877296776)
Bruce Whittingley has motive: True or False?
True (0.7017130830397807)
Bruce Whittingley has opportunity: True or False?
True (0.65489470935198)
Marie Carloette is guilty: True or False?
True (0.759938723019178)
Marie Carloette has mean: True or False?
True (0.7911763836133219)
Marie Carloette has motive: True or False?
True (0.8354834909254251)
Marie Carloette has opportunity: True or False?
True (0.8283841584202847)
Mario Marcino is guilty: True or False?
True (0.9079670935046645)
Mario Marcino has mean: True or False?
True (0.7988153087356352)
Mario Marcino has motive: True or False?
True (0.7950222460539826)
Mario Marcino has opportunity: True or False?
True (0.7310585348819939)
### Bruce Whittingley
- mean: False (0.16995621227032243)
- motive: False (0.29828691696021925)
- opportunity: False (0.34510529064802)

### Marie Carloette
- mean: True (0.7911763836133219)
- motive: True (0.8354834909254251)
- opportunity: True (0.8283841584202847)

### Mario Marcino
- mean: False (0.20118469126436478)
- motive: False (0.20497775394601736)
- opportunity: False (0.2689414651180061)

The culprit is Marie Carloette.
In fact, it is Marie Carloette.
## 5minutemystery-another-hotel-murder
Dianne Shelby is guilty: True or False?
True (0.7994423454932595)
Dianne Shelby has mean: True or False?
True (0.8227594449669557)
Dianne Shelby has motive: True or False?
True (0.7154240000492645)
Dianne Shelby has opportunity: True or False?
True (0.6800292132037243)
James Castro is guilty: True or False?
True (0.8620035048683017)
James Castro has mean: True or False?
True (0.8918110138739693)
James Castro has motive: True or False?
True (0.8370879250561812)
James Castro has opportunity: True or False?
True (0.847967740521315)
Kevin King is guilty: True or False?
True (0.9102267057681164)
Kevin King has mean: True or False?
True (0.9639160647221925)
Kevin King has motive: True or False?
True (0.7613610520273686)
Kevin King has opportunity: True or False?
True (0.776622945813876)
Roger Shelby is guilty: True or False?
True (0.8969755785184792)
Roger Shelby has mean: True or False?
True (0.8407825844829613)
Roger Shelby has motive: True or False?
True (0.702530072932436)
Roger Shelby has opportunity: True or False?
True (0.7017130830397807)
### Dianne Shelby
- mean: False (0.17724055503304426)
- motive: False (0.28457599995073546)
- opportunity: False (0.31997078679627566)

### James Castro
- mean: True (0.8918110138739693)
- motive: True (0.8370879250561812)
- opportunity: True (0.847967740521315)

### Kevin King
- mean: False (0.03608393527780751)
- motive: False (0.2386389479726314)
- opportunity: False (0.22337705418612397)

### Roger Shelby
- mean: False (0.15921741551703872)
- motive: False (0.29746992706756403)
- opportunity: False (0.29828691696021925)

The culprit is James Castro.
In fact, it is James Castro.
## 5minutemystery-the-missing-book
Brad is guilty: True or False?
True (0.5117165908639297)
Brad has mean: True or False?
True (0.7505527730327083)
Brad has motive: True or False?
True (0.6048658333578858)
Brad has opportunity: True or False?
True (0.5860491337676195)
Fred is guilty: True or False?
True (0.7424216889954057)
Fred has mean: True or False?
True (0.7799928701983835)
Fred has motive: True or False?
True (0.8086723702005608)
Fred has opportunity: True or False?
True (0.6825737331070684)
Mrs. Dunwoodee is guilty: True or False?
True (0.700075275973927)
Mrs. Dunwoodee has mean: True or False?
True (0.5973730125048408)
Mrs. Dunwoodee has motive: True or False?
True (0.7233094544266295)
Mrs. Dunwoodee has opportunity: True or False?
True (0.7732163648437078)
Ricky is guilty: True or False?
True (0.5592900581575188)
Ricky has mean: True or False?
True (0.7577943897558946)
Ricky has motive: True or False?
True (0.6206216296838327)
Ricky has opportunity: True or False?
True (0.6252093370817647)
### Brad
- mean: False (0.2494472269672917)
- motive: False (0.3951341666421142)
- opportunity: False (0.41395086623238053)

### Fred
- mean: True (0.7799928701983835)
- motive: True (0.8086723702005608)
- opportunity: True (0.6825737331070684)

### Mrs. Dunwoodee
- mean: False (0.40262698749515924)
- motive: False (0.27669054557337047)
- opportunity: False (0.22678363515629218)

### Ricky
- mean: False (0.24220561024410536)
- motive: False (0.3793783703161673)
- opportunity: False (0.37479066291823526)

The culprit is Fred.
In fact, it is Fred.
## 5minutemystery-the-necklace
Aunt Mary is guilty: True or False?
True (0.7826624547920057)
Aunt Mary has mean: True or False?
True (0.7969253675907205)
Aunt Mary has motive: True or False?
True (0.8013146490010521)
Aunt Mary has opportunity: True or False?
True (0.6584175136252488)
Dad is guilty: True or False?
True (0.9233161821369215)
Dad has mean: True or False?
True (0.8864203688833437)
Dad has motive: True or False?
True (0.8868131040663721)
Dad has opportunity: True or False?
True (0.7512833387594996)
Mom is guilty: True or False?
True (0.8509647293237851)
Mom has mean: True or False?
True (0.8433798528114077)
Mom has motive: True or False?
True (0.8484706263347676)
Mom has opportunity: True or False?
True (0.6132366084149281)
Uncle Henry is guilty: True or False?
True (0.8504686406728537)
Uncle Henry has mean: True or False?
True (0.7409249009267298)
Uncle Henry has motive: True or False?
True (0.8444089912414552)
Uncle Henry has opportunity: True or False?
True (0.7655932860037753)
Uncle John is guilty: True or False?
True (0.8204694405411458)
Uncle John has mean: True or False?
True (0.7483522884503825)
Uncle John has motive: True or False?
True (0.7924642605907138)
Uncle John has opportunity: True or False?
True (0.7256486384635821)
### Aunt Mary
- mean: False (0.20307463240927948)
- motive: False (0.1986853509989479)
- opportunity: False (0.3415824863747512)

### Dad
- mean: True (0.8864203688833437)
- motive: True (0.8868131040663721)
- opportunity: True (0.7512833387594996)

### Mom
- mean: False (0.1566201471885923)
- motive: False (0.15152937366523245)
- opportunity: False (0.3867633915850719)

### Uncle Henry
- mean: False (0.2590750990732702)
- motive: False (0.1555910087585448)
- opportunity: False (0.2344067139962247)

### Uncle John
- mean: False (0.2516477115496175)
- motive: False (0.20753573940928616)
- opportunity: False (0.2743513615364179)

The culprit is Dad.
In fact, it is Dad.
## 5minutemystery-the-purloined-wallet
Bill Buchanan is guilty: True or False?
True (0.9599877610290866)
Bill Buchanan has mean: True or False?
True (0.8519527857346616)
Bill Buchanan has motive: True or False?
True (0.844921525814193)
Bill Buchanan has opportunity: True or False?
True (0.8807970337584357)
Carson Thomson is guilty: True or False?
True (0.9509148001014369)
Carson Thomson has mean: True or False?
True (0.8596637847360897)
Carson Thomson has motive: True or False?
True (0.854884683810039)
Carson Thomson has opportunity: True or False?
True (0.8221890958162477)
Cooper is guilty: True or False?
True (0.921357630313903)
Cooper has mean: True or False?
True (0.5312093941731293)
Cooper has motive: True or False?
True (0.7356416476869558)
Cooper has opportunity: True or False?
True (0.8357518369388613)
David Nader is guilty: True or False?
True (0.9019206173215508)
David Nader has mean: True or False?
True (0.7272012283179254)
David Nader has motive: True or False?
True (0.869271276026005)
David Nader has opportunity: True or False?
True (0.8128672807499561)
Vincent Garcia is guilty: True or False?
True (0.9467446218678568)
Map: 100%|██████████| 203/203 [1:28:35<00:00, 21.84s/ examples]Map: 100%|██████████| 203/203 [1:28:35<00:00, 26.18s/ examples]
Vincent Garcia has mean: True or False?
True (0.8207569718385453)
Vincent Garcia has motive: True or False?
True (0.8624675215861032)
Vincent Garcia has opportunity: True or False?
True (0.8514594452543962)
### Bill Buchanan
- mean: True (0.8519527857346616)
- motive: True (0.844921525814193)
- opportunity: True (0.8807970337584357)

### Carson Thomson
- mean: False (0.14033621526391027)
- motive: False (0.14511531618996099)
- opportunity: False (0.17781090418375234)

### Cooper
- mean: False (0.4687906058268707)
- motive: False (0.26435835231304416)
- opportunity: False (0.16424816306113865)

### David Nader
- mean: False (0.27279877168207456)
- motive: False (0.13072872397399504)
- opportunity: False (0.18713271925004393)

### Vincent Garcia
- mean: False (0.17924302816145465)
- motive: False (0.13753247841389682)
- opportunity: False (0.1485405547456038)

The culprit is Bill Buchanan.
In fact, it is David Nader.
Solved 52 out of 203.
