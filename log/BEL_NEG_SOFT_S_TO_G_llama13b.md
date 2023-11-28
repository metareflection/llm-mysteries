nohup: ignoring input
/home/sraja/mambaforge/envs/llm-mysteries/lib/python3.10/site-packages/transformers/models/auto/auto_factory.py:472: FutureWarning: The `use_auth_token` argument is deprecated and will be removed in v5 of Transformers. Please use `token` instead.
  warnings.warn(
Loading checkpoint shards:   0%|          | 0/3 [00:00<?, ?it/s]Loading checkpoint shards:  33%|███▎      | 1/3 [00:02<00:04,  2.23s/it]Loading checkpoint shards:  67%|██████▋   | 2/3 [00:04<00:02,  2.10s/it]Loading checkpoint shards: 100%|██████████| 3/3 [00:05<00:00,  1.72s/it]Loading checkpoint shards: 100%|██████████| 3/3 [00:05<00:00,  1.84s/it]
/home/sraja/mambaforge/envs/llm-mysteries/lib/python3.10/site-packages/dill/_dill.py:412: PicklingWarning: Cannot locate reference to <class '_ctypes.PyCFuncPtrType'>.
  StockPickler.save(self, obj, save_persistent_id)
/home/sraja/mambaforge/envs/llm-mysteries/lib/python3.10/site-packages/dill/_dill.py:412: PicklingWarning: Cannot pickle <class '_ctypes.PyCFuncPtrType'>: _ctypes.PyCFuncPtrType has recursive self-references that trigger a RecursionError.
  StockPickler.save(self, obj, save_persistent_id)
Parameter 'function'=<function processCase at 0x7fa96afd01f0> of the transform datasets.arrow_dataset.Dataset._map_single couldn't be hashed properly, a random hash was used instead. Make sure your transforms and parameters are serializable with pickle or dill for the dataset fingerprinting and caching to work. If you reuse this transform, the caching mechanism will consider it to be different from the previous calls and recompute everything. This warning is only showed once. Subsequent hashing failures won't be showed.
Map:   0%|          | 0/203 [00:00<?, ? examples/s]Map:   0%|          | 1/203 [00:19<1:05:36, 19.49s/ examples]Map:   1%|          | 2/203 [00:35<58:25, 17.44s/ examples]  Map:   1%|▏         | 3/203 [01:02<1:12:27, 21.74s/ examples]## 5minutemystery-who-let-the-frogs-out
Kyle Kravetsky is guilty: True or False?
True (0.9274947665741009)
Kyle Kravetsky is not guilty: True or False?
True (0.9014011022144301)
Kyle Kravetsky has mean: True or False?
True (0.9164093141890854)
Kyle Kravetsky has no mean: True or False?
True (0.6113820047705449)
Kyle Kravetsky has motive: True or False?
True (0.9393594296838563)
Kyle Kravetsky has no motive: True or False?
True (0.7461389980806673)
Kyle Kravetsky has opportunity: True or False?
True (0.7420480767433203)
Kyle Kravetsky has no opportunity: True or False?
True (0.5263427467960875)
Marnie Pepper is guilty: True or False?
True (0.8418256636710214)
Marnie Pepper is not guilty: True or False?
True (0.7364006034245382)
Marnie Pepper has mean: True or False?
True (0.8727817583545995)
Marnie Pepper has no mean: True or False?
False (0.5087881523495457)
Marnie Pepper has motive: True or False?
True (0.8539127077831877)
Marnie Pepper has no motive: True or False?
True (0.5964331434971528)
Marnie Pepper has opportunity: True or False?
True (0.5087881523495457)
Marnie Pepper has no opportunity: True or False?
False (0.7966091010940959)
Matilda Robbens is guilty: True or False?
True (0.8895288719962232)
Matilda Robbens is not guilty: True or False?
True (0.847967740521315)
Matilda Robbens has mean: True or False?
True (0.9086179121100144)
Matilda Robbens has no mean: True or False?
True (0.6757646168022439)
Matilda Robbens has motive: True or False?
True (0.9257686153543061)
Matilda Robbens has no motive: True or False?
True (0.7613610520273686)
Matilda Robbens has opportunity: True or False?
True (0.7940657699545044)
Matilda Robbens has no opportunity: True or False?
True (0.6039317779631047)
Sergio Ramos is guilty: True or False?
True (0.9669140569738693)
Sergio Ramos is not guilty: True or False?
True (0.9543930889248589)
Sergio Ramos has mean: True or False?
True (0.9336731438527403)
Sergio Ramos has no mean: True or False?
True (0.7975568155246964)
Sergio Ramos has motive: True or False?
True (0.9489172681310486)
Sergio Ramos has no motive: True or False?
True (0.95498442695849)
Sergio Ramos has opportunity: True or False?
True (0.8795611817678315)
Sergio Ramos has no opportunity: True or False?
True (0.8062431235779619)
### Kyle Kravetsky
- mean: False (0.38861799522945506)
- motive: False (0.2538610019193327)
- opportunity: False (0.4736572532039125)

### Marnie Pepper
- mean: True (0.8727817583545995)
- motive: True (0.8539127077831877)
- opportunity: True (0.5087881523495457)

### Matilda Robbens
- mean: False (0.32423538319775613)
- motive: False (0.2386389479726314)
- opportunity: False (0.3960682220368953)

### Sergio Ramos
- mean: False (0.20244318447530363)
- motive: False (0.04501557304151005)
- opportunity: False (0.1937568764220381)

The culprit is Marnie Pepper.
In fact, it is Matilda Robbens.
## 5minutemystery-uncle-buck-field-trip
Collin is guilty: True or False?
True (0.8686040692746866)
Collin is not guilty: True or False?
True (0.8300437258865985)
Collin has mean: True or False?
True (0.7570766705324253)
Collin has no mean: True or False?
True (0.5869964306477841)
Collin has motive: True or False?
True (0.858955389767532)
Collin has no motive: True or False?
True (0.743912876509037)
Collin has opportunity: True or False?
True (0.7914989614633984)
Collin has no opportunity: True or False?
False (0.5282900215677746)
Erica is guilty: True or False?
True (0.851212260635415)
Erica is not guilty: True or False?
True (0.8966829113636618)
Erica has mean: True or False?
True (0.8860265599597172)
Erica has no mean: True or False?
True (0.6160122877297346)
Erica has motive: True or False?
True (0.8858291535164952)
Erica has no motive: True or False?
True (0.6632328635094317)
Erica has opportunity: True or False?
True (0.5438324636094939)
Erica has no opportunity: True or False?
False (0.6680145240815963)
Rory is guilty: True or False?
True (0.9293122320338961)
Rory is not guilty: True or False?
True (0.9240047963507929)
Rory has mean: True or False?
True (0.7725306828324007)
Rory has no mean: True or False?
True (0.7931059536445917)
Rory has motive: True or False?
True (0.9635748850103736)
Rory has no motive: True or False?
True (0.883638264557296)
Rory has opportunity: True or False?
True (0.8688268116310761)
Rory has no opportunity: True or False?
True (0.6846858174822046)
Rusty is guilty: True or False?
True (0.9396923188104354)
Rusty is not guilty: True or False?
True (0.9266363358194398)
Rusty has mean: True or False?
True (0.7759445334082792)
Rusty has no mean: True or False?
True (0.7341195403199204)
Rusty has motive: True or False?
True (0.9294404371753803)
Rusty has no motive: True or False?
True (0.8558511727823209)
Rusty has opportunity: True or False?
True (0.8848377441095496)
Rusty has no opportunity: True or False?
True (0.7846493136763113)
### Collin
- mean: True (0.7570766705324253)
- motive: True (0.858955389767532)
- opportunity: True (0.7914989614633984)

### Erica
- mean: False (0.3839877122702654)
- motive: False (0.33676713649056833)
- opportunity: False (0.0)

### Rory
- mean: False (0.2068940463554083)
- motive: False (0.116361735442704)
- opportunity: False (0.3153141825177954)

### Rusty
- mean: False (0.26588045968007956)
- motive: False (0.14414882721767908)
- opportunity: False (0.2153506863236887)

The culprit is Collin.
In fact, it is Rory.
## 5minutemystery-mystery-of-the-white-hats
Captain Stark is guilty: True or False?
True (0.8534248451958423)
Captain Stark is not guilty: True or False?
True (0.8407825844829613)
Captain Stark has mean: True or False?
True (0.9329437018480795)
Captain Stark has no mean: True or False?
True (0.8438951328214825)
Captain Stark has motive: True or False?
True (0.9091032147468773)
Captain Stark has no motive: True or False?
True (0.7826624547920057)
Captain Stark has opportunity: True or False?
True (0.7988152492192591)
Captain Stark has no opportunity: True or False?
True (0.6415346823638186)
Chet is guilty: True or False?
True (0.6800292740030767)
Chet is not guilty: True or False?
True (0.811078188867804)
Chet has mean: True or False?
True (0.8868131040663721)
Chet has no mean: True or False?
True (0.794384956668203)
Chet has motive: True or False?
True (0.8868130446009216)
Chet has no motive: True or False?
True (0.6731917300802632)
Chet has opportunity: True or False?
True (0.8386797310322072)
Chet has no opportunity: True or False?
False (0.5136684743338078)
Doug is guilty: True or False?
True (0.5841525779336078)
Doug is not guilty: True or False?
True (0.7453983509653428)
Doug has mean: True or False?
True (0.9073122118500465)
Doug has no mean: True or False?
True (0.8679338050595715)
Doug has motive: True or False?
True (0.802555560073231)
Doug has no motive: True or False?
True (0.6020615685826383)
Doug has opportunity: True or False?
True (0.7549149897594328)
Doug has no opportunity: True or False?
True (0.5058590748838109)
Ernie is guilty: True or False?
True (0.580352018589158)
Ernie is not guilty: True or False?
True (0.6540113633452196)
Ernie has mean: True or False?
True (0.8577681165234065)
Ernie has no mean: True or False?
True (0.7859664553110391)
Ernie has motive: True or False?
True (0.8504686406728537)
Ernie has no motive: True or False?
True (0.5563995964631269)
Ernie has opportunity: True or False?
True (0.72951977676791)
Ernie has no opportunity: True or False?
False (0.7527403228571042)
### Captain Stark
- mean: False (0.15610486717851746)
- motive: False (0.2173375452079943)
- opportunity: False (0.3584653176361814)

### Chet
- mean: False (0.20561504333179703)
- motive: False (0.32680826991973677)
- opportunity: False (0.0)

### Doug
- mean: False (0.13206619494042848)
- motive: False (0.39793843141736174)
- opportunity: False (0.4941409251161891)

### Ernie
- mean: True (0.8577681165234065)
- motive: True (0.8504686406728537)
- opportunity: True (0.72951977676791)

The culprit is Ernie.
In fact, it is Chet.
## 5minutemystery-the-missing-popcorn
Private First Class Dicky Mosier is guilty: True or False?
True (0.85729086409805)
Private First Class Dicky Mosier is not guilty: True or False?
True (0.7364005375851966)
Map:   2%|▏         | 4/203 [01:34<1:25:46, 25.86s/ examples]Map:   2%|▏         | 5/203 [02:15<1:43:22, 31.32s/ examples]Private First Class Dicky Mosier has mean: True or False?
True (0.9235923286659299)
Private First Class Dicky Mosier has no mean: True or False?
True (0.7074046739492601)
Private First Class Dicky Mosier has motive: True or False?
True (0.8824278665848695)
Private First Class Dicky Mosier has no motive: True or False?
True (0.7669924589170153)
Private First Class Dicky Mosier has opportunity: True or False?
True (0.811078188867804)
Private First Class Dicky Mosier has no opportunity: True or False?
True (0.555435161888281)
Private Joe Locke is guilty: True or False?
True (0.8652241235443877)
Private Joe Locke is not guilty: True or False?
True (0.8068526417769779)
Private Joe Locke has mean: True or False?
True (0.8086723099497763)
Private Joe Locke has no mean: True or False?
True (0.5341265295318852)
Private Joe Locke has motive: True or False?
True (0.9264369634617509)
Private Joe Locke has no motive: True or False?
True (0.797556874947312)
Private Joe Locke has opportunity: True or False?
True (0.7813306496768853)
Private Joe Locke has no opportunity: True or False?
True (0.6783269591477166)
Specialist Fifth Class Ron Henson is guilty: True or False?
True (0.7697732451157533)
Specialist Fifth Class Ron Henson is not guilty: True or False?
True (0.580352087772514)
Specialist Fifth Class Ron Henson has mean: True or False?
True (0.7527403228571042)
Specialist Fifth Class Ron Henson has no mean: True or False?
True (0.5058590748838109)
Specialist Fifth Class Ron Henson has motive: True or False?
True (0.7627776774954688)
Specialist Fifth Class Ron Henson has no motive: True or False?
False (0.6187804294217345)
Specialist Fifth Class Ron Henson has opportunity: True or False?
True (0.6967842494573921)
Specialist Fifth Class Ron Henson has no opportunity: True or False?
False (0.5841525779336078)
Specialist Fourth Class Patrick Macnamara is guilty: True or False?
True (0.7969253675907205)
Specialist Fourth Class Patrick Macnamara is not guilty: True or False?
True (0.6104534962074417)
Specialist Fourth Class Patrick Macnamara has mean: True or False?
True (0.6486889055472267)
Specialist Fourth Class Patrick Macnamara has no mean: True or False?
False (0.612309626324874)
Specialist Fourth Class Patrick Macnamara has motive: True or False?
True (0.5973730125048408)
Specialist Fourth Class Patrick Macnamara has no motive: True or False?
False (0.6680145240815963)
Specialist Fourth Class Patrick Macnamara has opportunity: True or False?
True (0.5039061393777357)
Specialist Fourth Class Patrick Macnamara has no opportunity: True or False?
False (0.7759445334082792)
### Private First Class Dicky Mosier
- mean: False (0.2925953260507399)
- motive: False (0.23300754108298471)
- opportunity: False (0.444564838111719)

### Private Joe Locke
- mean: False (0.4658734704681148)
- motive: False (0.20244312505268802)
- opportunity: False (0.32167304085228343)

### Specialist Fifth Class Ron Henson
- mean: False (0.4941409251161891)
- motive: False (0.0)
- opportunity: False (0.0)

### Specialist Fourth Class Patrick Macnamara
- mean: True (0.6486889055472267)
- motive: True (0.5973730125048408)
- opportunity: True (0.5039061393777357)

The culprit is Specialist Fourth Class Patrick Macnamara.
In fact, it is Private Joe Locke.
## 5minutemystery-mystery-on-the-moor
Jack MacGinnis is guilty: True or False?
True (0.9091032147468773)
Jack MacGinnis is not guilty: True or False?
True (0.9205042693180057)
Jack MacGinnis has mean: True or False?
True (0.8128673413132903)
Jack MacGinnis has no mean: True or False?
True (0.7655933544531522)
Jack MacGinnis has motive: True or False?
True (0.7905303264811482)
Jack MacGinnis has no motive: True or False?
True (0.5973730125048408)
Jack MacGinnis has opportunity: True or False?
True (0.6876299924560524)
Jack MacGinnis has no opportunity: True or False?
False (0.5214711377329961)
James Macready is guilty: True or False?
True (0.8895288719962232)
James Macready is not guilty: True or False?
True (0.9210740952879496)
James Macready has mean: True or False?
True (0.8719117627136385)
James Macready has no mean: True or False?
True (0.7669924589170153)
James Macready has motive: True or False?
True (0.8858291535164952)
James Macready has no motive: True or False?
True (0.5708098341193941)
James Macready has opportunity: True or False?
True (0.6662796746479285)
James Macready has no opportunity: True or False?
False (0.5945512478395265)
Samuel Doone is guilty: True or False?
True (0.7779753136455794)
Samuel Doone is not guilty: True or False?
True (0.7950222460539826)
Samuel Doone has mean: True or False?
True (0.784649255215384)
Samuel Doone has no mean: True or False?
True (0.6893056096647525)
Samuel Doone has motive: True or False?
True (0.7988152492192591)
Samuel Doone has no motive: True or False?
True (0.5321820387813727)
Samuel Doone has opportunity: True or False?
True (0.5765419579552815)
Samuel Doone has no opportunity: True or False?
False (0.6619228707202935)
Tom Jenkins is guilty: True or False?
True (0.8560919228396967)
Tom Jenkins is not guilty: True or False?
True (0.8472108208062923)
Tom Jenkins has mean: True or False?
True (0.8116760258690822)
Tom Jenkins has no mean: True or False?
True (0.6306849143569856)
Tom Jenkins has motive: True or False?
True (0.9219218506394821)
Tom Jenkins has no motive: True or False?
True (0.740174341079517)
Tom Jenkins has opportunity: True or False?
True (0.7461389980806673)
Tom Jenkins has no opportunity: True or False?
True (0.5794003525136094)
### Jack MacGinnis
- mean: True (0.8128673413132903)
- motive: True (0.7905303264811482)
- opportunity: True (0.6876299924560524)

### James Macready
- mean: False (0.23300754108298471)
- motive: False (0.4291901658806059)
- opportunity: False (0.0)

### Samuel Doone
- mean: False (0.3106943903352475)
- motive: False (0.4678179612186273)
- opportunity: False (0.0)

### Tom Jenkins
- mean: False (0.3693150856430144)
- motive: False (0.25982565892048304)
- opportunity: False (0.42059964748639056)

The culprit is Jack MacGinnis.
In fact, it is James Macready.
## 5minutemystery-who-stole-curious-george
Dexter is guilty: True or False?
True (0.7956581141325956)
Dexter is not guilty: True or False?
True (0.8929365260632085)
Dexter has mean: True or False?
True (0.7872777601997338)
Dexter has no mean: True or False?
True (0.5717666110200305)
Dexter has motive: True or False?
True (0.8725647371909419)
Dexter has no motive: True or False?
True (0.5679366075542497)
Dexter has opportunity: True or False?
True (0.7905303264811482)
Dexter has no opportunity: True or False?
True (0.5039061393777357)
Mr. Ferguson is guilty: True or False?
True (0.7049732238008671)
Mr. Ferguson is not guilty: True or False?
True (0.6757646168022439)
Mr. Ferguson has mean: True or False?
False (0.5273165696704634)
Mr. Ferguson has no mean: True or False?
False (0.740174341079517)
Mr. Ferguson has motive: True or False?
True (0.7379142672364736)
Mr. Ferguson has no motive: True or False?
False (0.5736784476125245)
Mr. Ferguson has opportunity: True or False?
False (0.673191669892235)
Mr. Ferguson has no opportunity: True or False?
False (0.8216173055802608)
Mrs. Yee is guilty: True or False?
True (0.7708099365638504)
Mrs. Yee is not guilty: True or False?
True (0.811974341286875)
Mrs. Yee has mean: True or False?
True (0.65489470935198)
Mrs. Yee has no mean: True or False?
False (0.5964331434971528)
Mrs. Yee has motive: True or False?
True (0.7013040666282004)
Mrs. Yee has no motive: True or False?
True (0.6388353131709135)
Mrs. Yee has opportunity: True or False?
True (0.5869964306477841)
Mrs. Yee has no opportunity: True or False?
False (0.5263428095410362)
Skyler is guilty: True or False?
True (0.6859494535376744)
Skyler is not guilty: True or False?
True (0.8022458575739914)
Skyler has mean: True or False?
False (0.591723272524637)
Skyler has no mean: True or False?
False (0.6662796746479285)
Skyler has motive: True or False?
True (0.7931059536445917)
Skyler has no motive: True or False?
True (0.5097643762740132)
Skyler has opportunity: True or False?
True (0.5679366075542497)
Skyler has no opportunity: True or False?
False (0.7943848974819138)
### Dexter
Map:   3%|▎         | 6/203 [02:59<1:57:14, 35.71s/ examples]Map:   3%|▎         | 7/203 [03:37<1:58:53, 36.40s/ examples]Map:   4%|▍         | 8/203 [04:08<1:52:28, 34.61s/ examples]- mean: False (0.42823338897996954)
- motive: False (0.4320633924457503)
- opportunity: False (0.49609386062226435)

### Mr. Ferguson
- mean: False (0.5273165696704634)
- motive: False (0.0)
- opportunity: False (0.673191669892235)

### Mrs. Yee
- mean: True (0.65489470935198)
- motive: True (0.7013040666282004)
- opportunity: True (0.5869964306477841)

### Skyler
- mean: False (0.591723272524637)
- motive: False (0.49023562372598684)
- opportunity: False (0.0)

The culprit is Mrs. Yee.
In fact, it is Dexter.
## 5minutemystery-the-saxophones-ghost
Building Manager is guilty: True or False?
True (0.5698527222023703)
Building Manager is not guilty: True or False?
False (0.6783269591477166)
Building Manager has mean: True or False?
False (0.7041601500399041)
Building Manager has no mean: True or False?
False (0.8727816933272936)
Building Manager has motive: True or False?
True (0.6610481693322063)
Building Manager has no motive: True or False?
False (0.5954925880745511)
Building Manager has opportunity: True or False?
False (0.8250265073476026)
Building Manager has no opportunity: True or False?
False (0.867485409735739)
Eric is guilty: True or False?
True (0.5621764690603255)
Eric is not guilty: True or False?
False (0.589834510337428)
Eric has mean: True or False?
True (0.6334102859975052)
Eric has no mean: True or False?
False (0.5195213440667139)
Eric has motive: True or False?
True (0.7225270177274575)
Eric has no motive: True or False?
False (0.5273165068094335)
Eric has opportunity: True or False?
False (0.5457699116223576)
Eric has no opportunity: True or False?
False (0.7185943809170431)
Lenny is guilty: True or False?
False (0.5573635130218721)
Lenny is not guilty: True or False?
False (0.6791786560103119)
Lenny has mean: True or False?
True (0.5438324636094939)
Lenny has no mean: True or False?
False (0.7563575572780217)
Lenny has motive: True or False?
True (0.570331332344394)
Lenny has no motive: True or False?
False (0.8509647293237851)
Lenny has opportunity: True or False?
False (0.5341265295318852)
Lenny has no opportunity: True or False?
False (0.8216173055802608)
Red is guilty: True or False?
False (0.5992506238662876)
Red is not guilty: True or False?
False (0.6817267588564826)
Red has mean: True or False?
False (0.5506073202694327)
Red has no mean: True or False?
False (0.7379143332111532)
Red has motive: True or False?
False (0.5282900845448565)
Red has no motive: True or False?
False (0.7209580648179327)
Red has opportunity: True or False?
False (0.6688802830862913)
Red has no opportunity: True or False?
False (0.8514594452543962)
### Building Manager
- mean: False (0.7041601500399041)
- motive: False (0.0)
- opportunity: False (0.8250265073476026)

### Eric
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.5457699116223576)

### Lenny
- mean: True (0.5438324636094939)
- motive: True (0.570331332344394)
- opportunity: True (0.1783826944197392)

### Red
- mean: False (0.5506073202694327)
- motive: False (0.5282900845448565)
- opportunity: False (0.6688802830862913)

The culprit is Lenny.
In fact, it is Building Manager.
## 5minutemystery-who-shot-mom
Dad is guilty: True or False?
True (0.9125920562149515)
Dad is not guilty: True or False?
True (1.2942329189057704)
Dad has mean: True or False?
True (0.8824278665848695)
Dad has no mean: True or False?
True (0.8534247816107388)
Dad has motive: True or False?
True (0.8906751280163339)
Dad has no motive: True or False?
True (0.9365176577773374)
Dad has opportunity: True or False?
True (0.8856314413364714)
Dad has no opportunity: True or False?
True (0.8092759828926619)
Randy is guilty: True or False?
True (0.8181563669811865)
Randy is not guilty: True or False?
True (0.8980534699860239)
Randy has mean: True or False?
True (0.9457010626376176)
Randy has no mean: True or False?
True (0.8354835531737983)
Randy has motive: True or False?
True (0.7431679939957333)
Randy has no motive: True or False?
True (0.8719117627136385)
Randy has opportunity: True or False?
True (0.8582439976623328)
Randy has no opportunity: True or False?
False (0.5156198737738186)
Roger is guilty: True or False?
True (0.8842393754985511)
Roger is not guilty: True or False?
True (0.9393594856740431)
Roger has mean: True or False?
True (0.8991213421091365)
Roger has no mean: True or False?
True (0.6804540698550936)
Roger has motive: True or False?
True (0.7931059536445917)
Roger has no motive: True or False?
True (0.865678909174824)
Roger has opportunity: True or False?
True (0.8013146490010521)
Roger has no opportunity: True or False?
False (0.6187804294217345)
Rory is guilty: True or False?
True (0.8152325155686644)
Rory is not guilty: True or False?
True (0.9167080509980843)
Rory has mean: True or False?
True (0.8727816933272936)
Rory has no mean: True or False?
True (0.6601724005812412)
Rory has motive: True or False?
True (0.7718434926244166)
Rory has no motive: True or False?
True (0.8633916342942395)
Rory has opportunity: True or False?
True (0.7772998201448375)
Rory has no opportunity: True or False?
True (0.5282900845448565)
### Dad
- mean: False (0.14657521838926124)
- motive: False (0.06348234222266258)
- opportunity: False (0.1907240171073381)

### Randy
- mean: True (0.9457010626376176)
- motive: True (0.7431679939957333)
- opportunity: True (0.8582439976623328)

### Roger
- mean: False (0.3195459301449064)
- motive: False (0.13432109082517596)
- opportunity: False (0.0)

### Rory
- mean: False (0.33982759941875884)
- motive: False (0.13660836570576051)
- opportunity: False (0.4717099154551435)

The culprit is Randy.
In fact, it is Randy.
## 5minutemystery-finding-the-flower-fund
James Faust is guilty: True or False?
True (0.5389832197022594)
James Faust is not guilty: True or False?
False (0.6504672743423094)
James Faust has mean: True or False?
True (0.8086723099497763)
James Faust has no mean: True or False?
True (0.6619228707202935)
James Faust has motive: True or False?
True (0.5131804871639641)
James Faust has no motive: True or False?
False (0.5525396910980834)
James Faust has opportunity: True or False?
False (0.555435161888281)
James Faust has no opportunity: True or False?
False (0.8469578650997759)
Justin Thorn is guilty: True or False?
False (0.5175709123121337)
Justin Thorn is not guilty: True or False?
False (0.6592954931819778)
Justin Thorn has mean: True or False?
True (0.844921525814193)
Justin Thorn has no mean: True or False?
True (0.6039318499573872)
Justin Thorn has motive: True or False?
True (0.5936092727363199)
Justin Thorn has no motive: True or False?
True (0.5126925663186335)
Justin Thorn has opportunity: True or False?
False (0.6067315356525022)
Justin Thorn has no opportunity: True or False?
False (0.720171518230031)
Lincoln Smith is guilty: True or False?
True (0.6876299924560524)
Lincoln Smith is not guilty: True or False?
True (0.6531268925247615)
Lincoln Smith has mean: True or False?
True (0.7431679939957333)
Lincoln Smith has no mean: True or False?
True (0.550607385906944)
Lincoln Smith has motive: True or False?
True (0.615087855649269)
Lincoln Smith has no motive: True or False?
True (0.6370308391245257)
Lincoln Smith has opportunity: True or False?
True (0.5794003525136094)
Lincoln Smith has no opportunity: True or False?
False (0.5165954111147137)
Linda Hinton is guilty: True or False?
True (0.6557770400181139)
Linda Hinton is not guilty: True or False?
True (0.5068355091660127)
Linda Hinton has mean: True or False?
True (0.8080671968507699)
Linda Hinton has no mean: True or False?
True (0.7442848102536271)
Linda Hinton has motive: True or False?
True (0.5727227727404994)
Linda Hinton has no motive: True or False?
True (0.6306849143569856)
Linda Hinton has opportunity: True or False?
True (0.5945512478395265)
Linda Hinton has no opportunity: True or False?
False (0.6757646168022439)
### James Faust
- mean: False (0.33807712927970646)
- motive: False (0.0)
- opportunity: False (0.555435161888281)

### Justin Thorn
- mean: False (0.39606815004261275)
- motive: False (0.48730743368136653)
- opportunity: False (0.6067315356525022)

### Lincoln Smith
- mean: False (0.449392614093056)
- motive: False (0.36296916087547426)
Map:   4%|▍         | 9/203 [04:34<1:43:01, 31.86s/ examples]Map:   5%|▍         | 10/203 [05:09<1:45:36, 32.83s/ examples]Map:   5%|▌         | 11/203 [05:44<1:47:12, 33.50s/ examples]- opportunity: False (0.0)

### Linda Hinton
- mean: True (0.8080671968507699)
- motive: True (0.5727227727404994)
- opportunity: True (0.5945512478395265)

The culprit is Linda Hinton.
In fact, it is Lincoln Smith.
## 5minutemystery-map-of-the-traitor
Benjamin is guilty: True or False?
True (0.7138307731576955)
Benjamin is not guilty: True or False?
True (0.7606506998655483)
Benjamin has mean: True or False?
True (0.642432441257838)
Benjamin has no mean: True or False?
False (0.7033457711626864)
Benjamin has motive: True or False?
True (0.7256486384635821)
Benjamin has no motive: True or False?
False (0.5302364729224919)
Benjamin has opportunity: True or False?
False (0.5602526707659626)
Benjamin has no opportunity: True or False?
False (0.7606506998655483)
Edward is guilty: True or False?
True (0.686790355176806)
Edward is not guilty: True or False?
True (0.5879431210535583)
Edward has mean: True or False?
True (0.6566582306092376)
Edward has no mean: True or False?
False (0.6654105788791005)
Edward has motive: True or False?
True (0.7146280500737092)
Edward has no motive: True or False?
False (0.6057990946577705)
Edward has opportunity: True or False?
False (0.6011253583932805)
Edward has no opportunity: True or False?
False (0.8278281666221954)
Jonathan is guilty: True or False?
True (0.5621764690603255)
Jonathan is not guilty: True or False?
True (0.6566582893190611)
Jonathan has mean: True or False?
True (0.6388352560545881)
Jonathan has no mean: True or False?
False (0.5650587803792624)
Jonathan has motive: True or False?
True (0.7431679939957333)
Jonathan has no motive: True or False?
True (0.5370413742099674)
Jonathan has opportunity: True or False?
False (0.595492552580428)
Jonathan has no opportunity: True or False?
False (0.7641883982873323)
Lucius is guilty: True or False?
True (0.685107355950278)
Lucius is not guilty: True or False?
True (0.6104534962074417)
Lucius has mean: True or False?
True (0.6984322578436808)
Lucius has no mean: True or False?
False (0.6279512069990912)
Lucius has motive: True or False?
True (0.7885831565209055)
Lucius has no motive: True or False?
True (0.5078118305218892)
Lucius has opportunity: True or False?
False (0.5126925663186335)
Lucius has no opportunity: True or False?
False (0.7577943897558946)
### Benjamin
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.5602526707659626)

### Edward
- mean: True (0.6566582306092376)
- motive: True (0.7146280500737092)
- opportunity: True (0.17217183337780462)

### Jonathan
- mean: False (0.0)
- motive: False (0.46295862579003255)
- opportunity: False (0.595492552580428)

### Lucius
- mean: False (0.0)
- motive: False (0.49218816947811084)
- opportunity: False (0.5126925663186335)

The culprit is Edward.
In fact, it is Jonathan.
## 5minutemystery-the-crusaders-robe
Captain Fosters is guilty: True or False?
True (0.873646672673131)
Captain Fosters is not guilty: True or False?
True (0.9240047963507929)
Captain Fosters has mean: True or False?
True (0.8591918406281239)
Captain Fosters has no mean: True or False?
True (0.7264255794048772)
Captain Fosters has motive: True or False?
True (0.8216173055802608)
Captain Fosters has no motive: True or False?
True (0.8413048399699521)
Captain Fosters has opportunity: True or False?
True (0.6992543888266708)
Captain Fosters has no opportunity: True or False?
True (0.6242935037467142)
Godefroi is guilty: True or False?
True (0.9246877442701001)
Godefroi is not guilty: True or False?
True (0.9383503780077049)
Godefroi has mean: True or False?
True (0.9497626419596781)
Godefroi has no mean: True or False?
True (0.7833262085677729)
Godefroi has motive: True or False?
True (0.9212159548464016)
Godefroi has no motive: True or False?
True (0.8919993657480679)
Godefroi has opportunity: True or False?
True (0.8261514850267767)
Godefroi has no opportunity: True or False?
True (0.6740504984987916)
Morgan Grant is guilty: True or False?
True (0.9095862487848758)
Morgan Grant is not guilty: True or False?
True (0.9056565771882901)
Morgan Grant has mean: True or False?
True (0.9422946582938823)
Morgan Grant has no mean: True or False?
True (0.7592253761865491)
Morgan Grant has motive: True or False?
True (0.9388007508488514)
Morgan Grant has no motive: True or False?
True (0.8732148436000907)
Morgan Grant has opportunity: True or False?
True (0.745398395394548)
Morgan Grant has no opportunity: True or False?
True (0.6575384105121485)
Sir Francis Walters is guilty: True or False?
True (0.9113376724203427)
Sir Francis Walters is not guilty: True or False?
True (0.9141375412484458)
Sir Francis Walters has mean: True or False?
True (0.9417613738325554)
Sir Francis Walters has no mean: True or False?
True (0.7655933544531522)
Sir Francis Walters has motive: True or False?
True (0.9048188910591489)
Sir Francis Walters has no motive: True or False?
True (0.8929365260632085)
Sir Francis Walters has opportunity: True or False?
True (0.7049732868303878)
Sir Francis Walters has no opportunity: True or False?
True (0.6540113633452196)
### Captain Fosters
- mean: True (0.8591918406281239)
- motive: True (0.8216173055802608)
- opportunity: True (0.6992543888266708)

### Godefroi
- mean: False (0.2166737914322271)
- motive: False (0.10800063425193207)
- opportunity: False (0.3259495015012084)

### Morgan Grant
- mean: False (0.24077462381345094)
- motive: False (0.12678515639990928)
- opportunity: False (0.34246158948785155)

### Sir Francis Walters
- mean: False (0.23440664554684776)
- motive: False (0.1070634739367915)
- opportunity: False (0.3459886366547804)

The culprit is Captain Fosters.
In fact, it is Godefroi.
## 5minutemystery-mr-patricks-history-class
Corporal Tom Patrick is guilty: True or False?
True (0.9209319968384807)
Corporal Tom Patrick is not guilty: True or False?
True (0.9177460685312047)
Corporal Tom Patrick has mean: True or False?
True (0.9492946258008691)
Corporal Tom Patrick has no mean: True or False?
True (0.9181872635464632)
Corporal Tom Patrick has motive: True or False?
True (0.8889517173369674)
Corporal Tom Patrick has no motive: True or False?
True (0.8738620878252635)
Corporal Tom Patrick has opportunity: True or False?
True (0.8410438346117795)
Corporal Tom Patrick has no opportunity: True or False?
True (0.7991290097268059)
Pvt. Billy Calhoun is guilty: True or False?
True (0.9528381231454964)
Pvt. Billy Calhoun is not guilty: True or False?
True (0.9538802513450514)
Pvt. Billy Calhoun has mean: True or False?
True (0.9637117373129486)
Pvt. Billy Calhoun has no mean: True or False?
True (0.9418684262191025)
Pvt. Billy Calhoun has motive: True or False?
True (0.9336731438527403)
Pvt. Billy Calhoun has no motive: True or False?
True (0.9196425103002197)
Pvt. Billy Calhoun has opportunity: True or False?
True (0.9385759849623091)
Pvt. Billy Calhoun has no opportunity: True or False?
True (0.8832359917473193)
Pvt. Jack Trueblood is guilty: True or False?
True (0.9463989149207153)
Pvt. Jack Trueblood is not guilty: True or False?
True (0.9505029326253388)
Pvt. Jack Trueblood has mean: True or False?
True (0.9691495281980984)
Pvt. Jack Trueblood has no mean: True or False?
True (0.9430336353172679)
Pvt. Jack Trueblood has motive: True or False?
True (0.9515039936355008)
Pvt. Jack Trueblood has no motive: True or False?
True (0.943970619289785)
Pvt. Jack Trueblood has opportunity: True or False?
True (0.9456006903352807)
Pvt. Jack Trueblood has no opportunity: True or False?
True (0.9214990117475544)
Sgt. Patrick Culpepper is guilty: True or False?
True (0.9594592463344039)
Sgt. Patrick Culpepper is not guilty: True or False?
True (0.9540517932883525)
Sgt. Patrick Culpepper has mean: True or False?
True (0.9458013187522837)
Sgt. Patrick Culpepper has no mean: True or False?
True (0.897695304229796)
Sgt. Patrick Culpepper has motive: True or False?
True (0.9365176577773374)
Sgt. Patrick Culpepper has no motive: True or False?
True (0.9281487460975983)
Sgt. Patrick Culpepper has opportunity: True or False?
True (0.9158089188126235)
Sgt. Patrick Culpepper has no opportunity: True or False?
True (0.8899121304559661)
### Corporal Tom Patrick
- mean: False (0.08181273645353682)
Map:   6%|▌         | 12/203 [06:36<2:05:17, 39.36s/ examples]Map:   6%|▋         | 13/203 [07:12<2:01:17, 38.30s/ examples]Map:   7%|▋         | 14/203 [07:47<1:57:02, 37.16s/ examples]- motive: False (0.12613791217473647)
- opportunity: False (0.2008709902731941)

### Pvt. Billy Calhoun
- mean: False (0.058131573780897505)
- motive: False (0.0803574896997803)
- opportunity: False (0.11676400825268074)

### Pvt. Jack Trueblood
- mean: True (0.9691495281980984)
- motive: True (0.9515039936355008)
- opportunity: True (0.9456006903352807)

### Sgt. Patrick Culpepper
- mean: False (0.10230469577020396)
- motive: False (0.07185125390240166)
- opportunity: False (0.11008786954403393)

The culprit is Pvt. Jack Trueblood.
In fact, it is Pvt. Billy Calhoun.
## 5minutemystery-bigfoot-mystery
Burt is guilty: True or False?
True (0.6951311179371613)
Burt is not guilty: True or False?
True (0.6654105788791005)
Burt has mean: True or False?
True (0.7162185953247016)
Burt has no mean: True or False?
False (0.6671476985798853)
Burt has motive: True or False?
True (0.8098781635062345)
Burt has no motive: True or False?
False (0.6315943123389512)
Burt has opportunity: True or False?
False (0.5175708506128766)
Burt has no opportunity: True or False?
False (0.8464508054137014)
Jerry is guilty: True or False?
True (0.8044059309478723)
Jerry is not guilty: True or False?
True (0.740174341079517)
Jerry has mean: True or False?
True (0.8524448242555318)
Jerry has no mean: True or False?
True (0.5204963206682631)
Jerry has motive: True or False?
True (0.8577681165234065)
Jerry has no motive: True or False?
False (0.5496406401666291)
Jerry has opportunity: True or False?
True (0.6575384693006662)
Jerry has no opportunity: True or False?
False (0.7310585348819939)
Leng is guilty: True or False?
True (0.6379334932841956)
Leng is not guilty: True or False?
True (0.5964331434971528)
Leng has mean: True or False?
True (0.5107405858633529)
Leng has no mean: True or False?
False (0.7766228995235426)
Leng has motive: True or False?
True (0.7178037814283548)
Leng has no motive: True or False?
False (0.525368812147771)
Leng has opportunity: True or False?
True (0.5973730125048408)
Leng has no opportunity: True or False?
False (0.7577943897558946)
Winston is guilty: True or False?
True (0.7885832152749314)
Winston is not guilty: True or False?
True (0.7725306828324007)
Winston has mean: True or False?
True (0.779321849347754)
Winston has no mean: True or False?
False (0.6297746298200823)
Winston has motive: True or False?
True (0.7193836643711469)
Winston has no motive: True or False?
False (0.6901415551283886)
Winston has opportunity: True or False?
True (0.5496406401666291)
Winston has no opportunity: True or False?
False (0.7924642605907138)
### Burt
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.5175708506128766)

### Jerry
- mean: False (0.4795036793317369)
- motive: False (0.0)
- opportunity: False (0.0)

### Leng
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.0)

### Winston
- mean: True (0.779321849347754)
- motive: True (0.7193836643711469)
- opportunity: True (0.5496406401666291)

The culprit is Winston.
In fact, it is Jerry.
## 5minutemystery-missing-movie-money
Billy is guilty: True or False?
True (0.9347534165970482)
Billy is not guilty: True or False?
True (0.9398029451247769)
Billy has mean: True or False?
True (0.8868131040663721)
Billy has no mean: True or False?
True (0.6943026818003076)
Billy has motive: True or False?
True (0.9769347912465448)
Billy has no motive: True or False?
True (0.9264369634617509)
Billy has opportunity: True or False?
True (0.8987665204865408)
Billy has no opportunity: True or False?
True (0.6859494535376744)
Cody is guilty: True or False?
True (0.9087799803825275)
Cody is not guilty: True or False?
True (0.9095863097773887)
Cody has mean: True or False?
True (0.8381506247725498)
Cody has no mean: True or False?
True (0.685107355950278)
Cody has motive: True or False?
True (0.9699566358821189)
Cody has no motive: True or False?
True (0.9078038309924442)
Cody has opportunity: True or False?
True (0.9031234959323464)
Cody has no opportunity: True or False?
False (0.5048826258478675)
Juliet is guilty: True or False?
True (0.905989824801558)
Juliet is not guilty: True or False?
True (0.95150405034956)
Juliet has mean: True or False?
True (0.9114953293645017)
Juliet has no mean: True or False?
True (0.8539127077831877)
Juliet has motive: True or False?
True (0.9708816405035137)
Juliet has no motive: True or False?
True (0.9170058398600052)
Juliet has opportunity: True or False?
True (0.9403530947748038)
Juliet has no opportunity: True or False?
True (0.7627776774954688)
Tammy is guilty: True or False?
True (0.6662796746479285)
Tammy is not guilty: True or False?
True (0.65489470935198)
Tammy has mean: True or False?
True (0.7074046739492601)
Tammy has no mean: True or False?
False (0.5428633110863297)
Tammy has motive: True or False?
True (0.8980535302052036)
Tammy has no motive: True or False?
True (0.7416740778117503)
Tammy has opportunity: True or False?
True (0.6469064338453809)
Tammy has no opportunity: True or False?
False (0.5117165908639297)
### Billy
- mean: False (0.30569731819969237)
- motive: False (0.07356303653824914)
- opportunity: False (0.31405054646232555)

### Cody
- mean: False (0.31489264404972195)
- motive: False (0.09219616900755578)
- opportunity: False (0.0)

### Juliet
- mean: False (0.14608729221681227)
- motive: False (0.08299416013999483)
- opportunity: False (0.23722232250453124)

### Tammy
- mean: True (0.7074046739492601)
- motive: True (0.8980535302052036)
- opportunity: True (0.6469064338453809)

The culprit is Tammy.
In fact, it is Cody.
## 5minutemystery-missing-ammunition
Henry is guilty: True or False?
True (0.8238958672039278)
Henry is not guilty: True or False?
True (0.7826624547920057)
Henry has mean: True or False?
True (0.7556369876990674)
Henry has no mean: True or False?
False (0.6636689235052821)
Henry has motive: True or False?
True (0.9026095892260383)
Henry has no motive: True or False?
False (0.6113820047705449)
Henry has opportunity: True or False?
True (0.5234203246639862)
Henry has no opportunity: True or False?
False (0.7549149897594328)
Mr. Samuel is guilty: True or False?
True (0.9127477403975288)
Mr. Samuel is not guilty: True or False?
True (0.8509646659219744)
Mr. Samuel has mean: True or False?
True (0.8895288719962232)
Mr. Samuel has no mean: True or False?
True (0.5350984235603058)
Mr. Samuel has motive: True or False?
True (0.9433475737015985)
Mr. Samuel has no motive: True or False?
True (0.6749080895533367)
Mr. Samuel has opportunity: True or False?
True (0.6774740084332073)
Mr. Samuel has no opportunity: True or False?
False (0.5612147992901458)
Mr. Smith is guilty: True or False?
True (0.9260365949489886)
Mr. Smith is not guilty: True or False?
True (0.9031234959323464)
Mr. Smith has mean: True or False?
True (0.8766344170435998)
Mr. Smith has no mean: True or False?
True (0.7170118721569225)
Mr. Smith has motive: True or False?
True (0.9445871723447916)
Mr. Smith has no motive: True or False?
True (0.7866228249849953)
Mr. Smith has opportunity: True or False?
True (0.8019357965963964)
Mr. Smith has no opportunity: True or False?
True (0.6141626144170799)
Young Soldier is guilty: True or False?
True (0.8418256009501243)
Young Soldier is not guilty: True or False?
True (0.7853085971692302)
Young Soldier has mean: True or False?
True (0.9399133323582882)
Young Soldier has no mean: True or False?
True (0.7272012283179254)
Young Soldier has motive: True or False?
True (0.8994751578343994)
Young Soldier has no motive: True or False?
True (0.6901415551283886)
Young Soldier has opportunity: True or False?
True (0.6951311179371613)
Young Soldier has no opportunity: True or False?
True (0.7333564224770464)
### Henry
- mean: True (0.7556369876990674)
- motive: True (0.9026095892260383)
- opportunity: True (0.5234203246639862)

### Mr. Samuel
- mean: False (0.4649015764396942)
- motive: False (0.3250919104466633)
- opportunity: False (0.0)

### Mr. Smith
- mean: False (0.2829881278430775)
- motive: False (0.21337717501500475)
- opportunity: False (0.38583738558292013)

### Young Soldier
- mean: False (0.27279877168207456)
- motive: False (0.3098584448716114)
- opportunity: False (0.26664357752295365)

The culprit is Henry.
Map:   7%|▋         | 15/203 [08:20<1:52:22, 35.86s/ examples]Map:   8%|▊         | 16/203 [09:03<1:59:00, 38.18s/ examples]Map:   8%|▊         | 17/203 [09:39<1:55:39, 37.31s/ examples]In fact, it is Henry.
## 5minutemystery-the-sky-sleuths
Bug collector is guilty: True or False?
True (0.7541915239138703)
Bug collector is not guilty: True or False?
True (0.7749242151945704)
Bug collector has mean: True or False?
True (0.591723272524637)
Bug collector has no mean: True or False?
True (0.6540113048720497)
Bug collector has motive: True or False?
True (0.8357517746704994)
Bug collector has no motive: True or False?
True (0.8558511090164419)
Bug collector has opportunity: True or False?
True (0.685107355950278)
Bug collector has no opportunity: True or False?
True (0.5380124470448935)
Elderly man is guilty: True or False?
True (0.673191669892235)
Elderly man is not guilty: True or False?
True (0.678326898500563)
Elderly man has mean: True or False?
True (0.5136684743338078)
Elderly man has no mean: True or False?
False (0.5175709123121337)
Elderly man has motive: True or False?
True (0.8255897087847518)
Elderly man has no motive: True or False?
True (0.8624675215861032)
Elderly man has opportunity: True or False?
False (0.5631377056275331)
Elderly man has no opportunity: True or False?
False (0.5234203870605549)
Family man is guilty: True or False?
True (0.6943026818003076)
Family man is not guilty: True or False?
True (0.646013666311734)
Family man has mean: True or False?
False (0.5992506238662876)
Family man has no mean: True or False?
False (0.5583269696343842)
Family man has motive: True or False?
True (0.5860491337676195)
Family man has no motive: True or False?
True (0.7130321332210621)
Family man has opportunity: True or False?
False (0.5389832197022594)
Family man has no opportunity: True or False?
False (0.6379335503198971)
Motorcyclist is guilty: True or False?
False (0.5370413742099674)
Motorcyclist is not guilty: True or False?
False (0.5945512478395265)
Motorcyclist has mean: True or False?
True (0.589834510337428)
Motorcyclist has no mean: True or False?
False (0.580352018589158)
Motorcyclist has motive: True or False?
True (0.6370307821695329)
Motorcyclist has no motive: True or False?
True (0.6048657973050737)
Motorcyclist has opportunity: True or False?
True (0.5438324636094939)
Motorcyclist has no opportunity: True or False?
False (0.5438325284393795)
### Bug collector
- mean: False (0.3459886951279503)
- motive: False (0.1441488909835581)
- opportunity: False (0.4619875529551065)

### Elderly man
- mean: False (0.0)
- motive: False (0.13753247841389682)
- opportunity: False (0.5631377056275331)

### Family man
- mean: False (0.5992506238662876)
- motive: False (0.28696786677893793)
- opportunity: False (0.5389832197022594)

### Motorcyclist
- mean: True (0.589834510337428)
- motive: True (0.6370307821695329)
- opportunity: True (0.5438324636094939)

The culprit is Motorcyclist.
In fact, it is Bug collector.
## 5minutemystery-battle-of-the-bulge
Anderson is guilty: True or False?
True (0.5409238326546766)
Anderson is not guilty: True or False?
False (0.6057990946577705)
Anderson has mean: True or False?
False (0.5175708506128766)
Anderson has no mean: True or False?
False (0.7599387683150569)
Anderson has motive: True or False?
False (0.5457699116223576)
Anderson has no motive: True or False?
False (0.5879430860094185)
Anderson has opportunity: True or False?
False (0.6817267588564826)
Anderson has no opportunity: True or False?
False (0.8464508054137014)
Dilworth is guilty: True or False?
True (0.6242935037467142)
Dilworth is not guilty: True or False?
False (0.5841525779336078)
Dilworth has mean: True or False?
True (0.64779823427608)
Dilworth has no mean: True or False?
False (0.5794004215835179)
Dilworth has motive: True or False?
False (0.5727227727404994)
Dilworth has no motive: True or False?
False (0.6817267588564826)
Dilworth has opportunity: True or False?
False (0.6315942370470465)
Dilworth has no opportunity: True or False?
False (0.7287483223557857)
Maguire is guilty: True or False?
False (0.6504672743423094)
Maguire is not guilty: True or False?
False (0.8181563669811865)
Maguire has mean: True or False?
False (0.7577943897558946)
Maguire has no mean: True or False?
False (0.7287482572006113)
Maguire has motive: True or False?
False (0.6557770400181139)
Maguire has no motive: True or False?
False (0.7690802105138688)
Maguire has opportunity: True or False?
False (0.7918210572836727)
Maguire has no opportunity: True or False?
False (0.8940517282497483)
Siegel is guilty: True or False?
True (0.5669777909748143)
Siegel is not guilty: True or False?
False (0.7225270177274575)
Siegel has mean: True or False?
False (0.5736783792247284)
Siegel has no mean: True or False?
False (0.7416740115009234)
Siegel has motive: True or False?
False (0.6141626144170799)
Siegel has no motive: True or False?
False (0.7779753136455794)
Siegel has opportunity: True or False?
False (0.7468781997658912)
Siegel has no opportunity: True or False?
False (0.8910549899564296)
### Anderson
- mean: False (0.5175708506128766)
- motive: False (0.5457699116223576)
- opportunity: False (0.6817267588564826)

### Dilworth
- mean: True (0.64779823427608)
- motive: True (0.3182732411435174)
- opportunity: True (0.2712516776442143)

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
Eliza Murray is not guilty: True or False?
True (0.7352616086060775)
Eliza Murray has mean: True or False?
True (0.8514594452543962)
Eliza Murray has no mean: True or False?
True (0.8050197941712954)
Eliza Murray has motive: True or False?
True (0.9027811324949335)
Eliza Murray has no motive: True or False?
False (0.6976088896786037)
Eliza Murray has opportunity: True or False?
True (0.6242935781683038)
Eliza Murray has no opportunity: True or False?
False (0.8344069148356309)
George Sanders is guilty: True or False?
True (0.6197014353942354)
George Sanders is not guilty: True or False?
True (0.5136684743338078)
George Sanders has mean: True or False?
False (0.5370414382302919)
George Sanders has no mean: True or False?
False (0.6224592927728324)
George Sanders has motive: True or False?
False (0.5292633777076584)
George Sanders has no motive: True or False?
False (0.8643104392003704)
George Sanders has opportunity: True or False?
False (0.7962924261546153)
George Sanders has no opportunity: True or False?
False (0.9265699426348812)
Stable boy Ian is guilty: True or False?
False (0.8883720049821552)
Stable boy Ian is not guilty: True or False?
False (0.8193157928301305)
Stable boy Ian has mean: True or False?
False (0.7866228249849953)
Stable boy Ian has no mean: True or False?
False (0.8887587777822111)
Stable boy Ian has motive: True or False?
False (0.7620701143808404)
Stable boy Ian has no motive: True or False?
False (0.9403530352223053)
Stable boy Ian has opportunity: True or False?
False (0.8322366416985943)
Stable boy Ian has no opportunity: True or False?
False (0.9527502639818524)
Thomas Murray is guilty: True or False?
True (0.7333563569098757)
Thomas Murray is not guilty: True or False?
True (0.5389832197022594)
Thomas Murray has mean: True or False?
True (0.8037906314112822)
Thomas Murray has no mean: True or False?
True (0.7476159279883341)
Thomas Murray has motive: True or False?
True (0.8654516347931567)
Thomas Murray has no motive: True or False?
False (0.65489470935198)
Thomas Murray has opportunity: True or False?
True (0.5360700410935405)
Thomas Murray has no opportunity: True or False?
False (0.7859664553110391)
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
- mean: False (0.2523840720116659)
- motive: False (0.0)
Map:   9%|▉         | 18/203 [10:25<2:03:31, 40.06s/ examples]Map:   9%|▉         | 19/203 [11:07<2:04:32, 40.61s/ examples]Map:  10%|▉         | 20/203 [11:43<2:00:10, 39.40s/ examples]Map:  10%|█         | 21/203 [12:20<1:57:04, 38.59s/ examples]- opportunity: False (0.0)

The culprit is Eliza Murray.
In fact, it is Stable boy Ian.
## 5minutemystery-the-railroad-mystery
Alvarado is guilty: True or False?
True (0.5851012033999957)
Alvarado is not guilty: True or False?
True (0.5612147992901458)
Alvarado has mean: True or False?
True (0.5263427467960875)
Alvarado has no mean: True or False?
False (0.6706082735718226)
Alvarado has motive: True or False?
True (0.6749080895533367)
Alvarado has no motive: True or False?
False (0.5224458497983033)
Alvarado has opportunity: True or False?
False (0.5457699116223576)
Alvarado has no opportunity: True or False?
False (0.7209580003592615)
The engineer is guilty: True or False?
True (0.5370414382302919)
The engineer is not guilty: True or False?
True (0.7879311977554747)
The engineer has mean: True or False?
True (0.6104534962074417)
The engineer has no mean: True or False?
False (0.595492552580428)
The engineer has motive: True or False?
True (0.7348812840309261)
The engineer has no motive: True or False?
True (0.6379335503198971)
The engineer has opportunity: True or False?
True (0.644225125126315)
The engineer has no opportunity: True or False?
False (0.6039318499573872)
The mechanic is guilty: True or False?
True (0.6297746298200823)
The mechanic is not guilty: True or False?
True (0.8031737798924701)
The mechanic has mean: True or False?
True (0.8122723669190336)
The mechanic has no mean: True or False?
True (0.6178585826183487)
The mechanic has motive: True or False?
True (0.8464508054137014)
The mechanic has no motive: True or False?
True (0.7527403228571042)
The mechanic has opportunity: True or False?
True (0.8397339530959691)
The mechanic has no opportunity: True or False?
True (0.6486889055472267)
Zebediah is guilty: True or False?
True (0.6486889055472267)
Zebediah is not guilty: True or False?
True (0.8092759828926619)
Zebediah has mean: True or False?
True (0.7570766705324253)
Zebediah has no mean: True or False?
True (0.7209580003592615)
Zebediah has motive: True or False?
True (0.8283841584202847)
Zebediah has no motive: True or False?
True (0.7017130830397807)
Zebediah has opportunity: True or False?
True (0.5784481782924303)
Zebediah has no opportunity: True or False?
False (0.5612147992901458)
### Alvarado
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.5457699116223576)

### The engineer
- mean: True (0.6104534962074417)
- motive: True (0.7348812840309261)
- opportunity: True (0.644225125126315)

### The mechanic
- mean: False (0.3821414173816513)
- motive: False (0.24725967714289576)
- opportunity: False (0.3513110944527733)

### Zebediah
- mean: False (0.2790419996407385)
- motive: False (0.29828691696021925)
- opportunity: False (0.0)

The culprit is The engineer.
In fact, it is Zebediah.
## 5minutemystery-the-date
Bob is guilty: True or False?
True (0.9599126594957205)
Bob is not guilty: True or False?
True (0.9501803512501087)
Bob has mean: True or False?
True (0.9826243527033713)
Bob has no mean: True or False?
True (0.7885831565209055)
Bob has motive: True or False?
True (0.9410069597342015)
Bob has no motive: True or False?
True (0.8305941261447712)
Bob has opportunity: True or False?
True (0.9751071938949272)
Bob has no opportunity: True or False?
True (0.8415654247149972)
Cynthia is guilty: True or False?
True (0.7592253761865491)
Cynthia is not guilty: True or False?
True (0.8489721404936124)
Cynthia has mean: True or False?
True (0.9431384818142104)
Cynthia has no mean: True or False?
True (0.6039317779631047)
Cynthia has motive: True or False?
True (0.9063219998220023)
Cynthia has no motive: True or False?
True (0.6909762697651828)
Cynthia has opportunity: True or False?
True (0.7662936378892937)
Cynthia has no opportunity: True or False?
False (0.6433293282949071)
Diane is guilty: True or False?
True (0.7813306496768853)
Diane is not guilty: True or False?
True (0.8584814679672361)
Diane has mean: True or False?
True (0.9317114347547434)
Diane has no mean: True or False?
False (0.5029296829424847)
Diane has motive: True or False?
True (0.821044090050916)
Diane has no motive: True or False?
True (0.7872777601997338)
Diane has opportunity: True or False?
True (0.8397339530959691)
Diane has no opportunity: True or False?
True (0.5841525082971981)
Kristin is guilty: True or False?
True (0.6749080895533367)
Kristin is not guilty: True or False?
True (0.8757870204368676)
Kristin has mean: True or False?
True (0.8376199551237796)
Kristin has no mean: True or False?
True (0.5755879969637064)
Kristin has motive: True or False?
True (0.7655933544531522)
Kristin has no motive: True or False?
True (0.7520125537161032)
Kristin has opportunity: True or False?
True (0.8204694405411458)
Kristin has no opportunity: True or False?
True (0.7106283339569771)
### Bob
- mean: False (0.2114168434790945)
- motive: False (0.16940587385522876)
- opportunity: False (0.15843457528500282)

### Cynthia
- mean: False (0.3960682220368953)
- motive: False (0.3090237302348172)
- opportunity: False (0.0)

### Diane
- mean: True (0.9317114347547434)
- motive: True (0.821044090050916)
- opportunity: True (0.8397339530959691)

### Kristin
- mean: False (0.42441200303629356)
- motive: False (0.2479874462838968)
- opportunity: False (0.2893716660430229)

The culprit is Diane.
In fact, it is Bob.
## 5minutemystery-b-movie-murder
Angela is guilty: True or False?
True (0.5698526542706361)
Angela is not guilty: True or False?
True (0.5688948754232768)
Angela has mean: True or False?
True (0.5746334908651781)
Angela has no mean: True or False?
False (0.6178585826183487)
Angela has motive: True or False?
True (0.6893056096647525)
Angela has no motive: True or False?
False (0.6575384105121485)
Angela has opportunity: True or False?
True (0.7287482572006113)
Angela has no opportunity: True or False?
False (0.7981867775042927)
Debbie is guilty: True or False?
True (0.5592899914849522)
Debbie is not guilty: True or False?
False (0.5273165068094335)
Debbie has mean: True or False?
True (0.6187804294217345)
Debbie has no mean: True or False?
False (0.5794004215835179)
Debbie has motive: True or False?
True (0.5926666351772785)
Debbie has no motive: True or False?
False (0.6740504382339836)
Debbie has opportunity: True or False?
True (0.7017130830397807)
Debbie has no opportunity: True or False?
False (0.8227594449669557)
Sal is guilty: True or False?
True (0.5964331434971528)
Sal is not guilty: True or False?
False (0.5535053004623279)
Sal has mean: True or False?
True (0.686790355176806)
Sal has no mean: True or False?
False (0.5126925663186335)
Sal has motive: True or False?
True (0.7655932860037753)
Sal has no motive: True or False?
True (0.5019531141001669)
Sal has opportunity: True or False?
True (0.7859663967519771)
Sal has no opportunity: True or False?
False (0.6388352560545881)
Tom is guilty: True or False?
True (0.5312093625105829)
Tom is not guilty: True or False?
False (0.5822535180679596)
Tom has mean: True or False?
False (0.5755879969637064)
Tom has no mean: True or False?
False (0.8198933606225757)
Tom has motive: True or False?
True (0.6469064916833258)
Tom has no motive: True or False?
False (0.6297746298200823)
Tom has opportunity: True or False?
True (0.7233095190955371)
Tom has no opportunity: True or False?
False (0.8582439976623328)
### Angela
- mean: True (0.5746334908651781)
- motive: True (0.6893056096647525)
- opportunity: True (0.7287482572006113)

### Debbie
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.0)

### Sal
- mean: False (0.0)
- motive: False (0.49804688589983315)
- opportunity: False (0.0)

### Tom
- mean: False (0.5755879969637064)
- motive: False (0.0)
- opportunity: False (0.0)

The culprit is Angela.
In fact, it is Angela.
## 5minutemystery-the-jackie-mitchell-autographed-baseball-mystery
Dr. Edgar Newton is guilty: True or False?
True (0.7472472734767229)
Dr. Edgar Newton is not guilty: True or False?
False (0.3535381327532581)
Dr. Edgar Newton has mean: True or False?
True (0.6076631662366868)
Dr. Edgar Newton has no mean: True or False?
False (0.6160122877297346)
Dr. Edgar Newton has motive: True or False?
True (0.7017130830397807)
Map:  11%|█         | 22/203 [13:04<2:01:16, 40.20s/ examples]Map:  11%|█▏        | 23/203 [13:34<1:50:57, 36.98s/ examples]Map:  12%|█▏        | 24/203 [14:05<1:44:57, 35.18s/ examples]Dr. Edgar Newton has no motive: True or False?
True (0.5808276413728785)
Dr. Edgar Newton has opportunity: True or False?
False (0.5477060024984176)
Dr. Edgar Newton has no opportunity: True or False?
False (0.8255897087847518)
Melinda Baker is guilty: True or False?
True (0.821044090050916)
Melinda Baker is not guilty: True or False?
True (0.7756047866813147)
Melinda Baker has mean: True or False?
True (0.8591918406281239)
Melinda Baker has no mean: True or False?
False (0.6020615685826383)
Melinda Baker has motive: True or False?
True (0.5087881523495457)
Melinda Baker has no motive: True or False?
False (0.6808785831877406)
Melinda Baker has opportunity: True or False?
False (0.6825737331070684)
Melinda Baker has no opportunity: True or False?
False (0.8521990171094214)
Simon Plympton is guilty: True or False?
True (0.8524447734458623)
Simon Plympton is not guilty: True or False?
True (0.7927852843681614)
Simon Plympton has mean: True or False?
True (0.8591918406281239)
Simon Plympton has no mean: True or False?
True (0.6397360437814448)
Simon Plympton has motive: True or False?
True (0.7804952298233097)
Simon Plympton has no motive: True or False?
False (0.5544704821687028)
Simon Plympton has opportunity: True or False?
True (0.5640984675176304)
Simon Plympton has no opportunity: True or False?
False (0.7520125537161032)
Susan Plympton is guilty: True or False?
True (0.781664133797069)
Susan Plympton is not guilty: True or False?
True (0.6943026818003076)
Susan Plympton has mean: True or False?
True (0.8086723099497763)
Susan Plympton has no mean: True or False?
True (0.5399537164111071)
Susan Plympton has motive: True or False?
True (0.6109178653970281)
Susan Plympton has no motive: True or False?
False (0.6947170558884102)
Susan Plympton has opportunity: True or False?
False (0.6011253583932805)
Susan Plympton has no opportunity: True or False?
False (0.7490872087035162)
### Dr. Edgar Newton
- mean: False (0.0)
- motive: False (0.41917235862712154)
- opportunity: False (0.5477060024984176)

### Melinda Baker
- mean: True (0.8591918406281239)
- motive: True (0.5087881523495457)
- opportunity: True (0.14780098289057864)

### Simon Plympton
- mean: False (0.3602639562185552)
- motive: False (0.0)
- opportunity: False (0.0)

### Susan Plympton
- mean: False (0.4600462835888929)
- motive: False (0.0)
- opportunity: False (0.6011253583932805)

The culprit is Melinda Baker.
In fact, it is Susan Plympton.
## 5minutemystery-the-easter-egg-mystery
Anna is guilty: True or False?
True (0.6187804294217345)
Anna is not guilty: True or False?
True (0.6926419789019715)
Anna has mean: True or False?
True (0.700075275973927)
Anna has no mean: True or False?
True (0.5765419579552815)
Anna has motive: True or False?
True (0.8820220178442959)
Anna has no motive: True or False?
True (0.7033457711626864)
Anna has opportunity: True or False?
True (0.8381505623254643)
Anna has no opportunity: True or False?
True (0.6123096993178739)
Cole is guilty: True or False?
True (0.6619228707202935)
Cole is not guilty: True or False?
True (0.7549149897594328)
Cole has mean: True or False?
True (0.8413048399699521)
Cole has no mean: True or False?
True (0.6415346823638186)
Cole has motive: True or False?
True (0.8423451152856819)
Cole has no motive: True or False?
True (0.7704647687904915)
Cole has opportunity: True or False?
True (0.8181563669811865)
Cole has no opportunity: True or False?
True (0.64063590602721)
Justin is guilty: True or False?
True (0.612309626324874)
Justin is not guilty: True or False?
True (0.6876299924560524)
Justin has mean: True or False?
True (0.7217431689117048)
Justin has no mean: True or False?
True (0.591723272524637)
Justin has motive: True or False?
True (0.8524448242555318)
Justin has no motive: True or False?
True (0.7033457082786769)
Justin has opportunity: True or False?
True (0.7969253675907205)
Justin has no opportunity: True or False?
True (0.60859406896259)
Lizzie is guilty: True or False?
True (0.7240905157396584)
Lizzie is not guilty: True or False?
True (0.8333246107254184)
Lizzie has mean: True or False?
True (0.7017130830397807)
Lizzie has no mean: True or False?
True (0.6808785831877406)
Lizzie has motive: True or False?
True (0.815232454829111)
Lizzie has no motive: True or False?
True (0.7476159279883341)
Lizzie has opportunity: True or False?
True (0.8994751578343994)
Lizzie has no opportunity: True or False?
True (0.6252092625510083)
Rachel is guilty: True or False?
True (0.6959583025067009)
Rachel is not guilty: True or False?
True (0.7711548682745724)
Rachel has mean: True or False?
True (0.7853085971692302)
Rachel has no mean: True or False?
True (0.7193836000532381)
Rachel has motive: True or False?
True (0.8587185689177256)
Rachel has no motive: True or False?
True (0.8464508054137014)
Rachel has opportunity: True or False?
True (0.8238958672039278)
Rachel has no opportunity: True or False?
True (0.6901415551283886)
### Anna
- mean: False (0.4234580420447185)
- motive: False (0.2966542288373136)
- opportunity: False (0.38769030068212607)

### Cole
- mean: False (0.3584653176361814)
- motive: False (0.22953523120950847)
- opportunity: False (0.35936409397279)

### Justin
- mean: False (0.40827672747536303)
- motive: False (0.29665429172132307)
- opportunity: False (0.39140593103740995)

### Lizzie
- mean: False (0.31912141681225936)
- motive: False (0.2523840720116659)
- opportunity: False (0.3747907374489917)

### Rachel
- mean: True (0.7853085971692302)
- motive: True (0.8587185689177256)
- opportunity: True (0.8238958672039278)

The culprit is Rachel.
In fact, it is Lizzie.
## 5minutemystery-easter-rhyme
Abbott is guilty: True or False?
True (0.8539127077831877)
Abbott is not guilty: True or False?
True (0.8451772359637012)
Abbott has mean: True or False?
True (0.8459423727595791)
Abbott has no mean: True or False?
True (0.7956581141325956)
Abbott has motive: True or False?
True (0.8795611817678315)
Abbott has no motive: True or False?
True (0.8933094122075369)
Abbott has opportunity: True or False?
True (0.8354835531737983)
Abbott has no opportunity: True or False?
True (0.7697732451157533)
Andy is guilty: True or False?
True (0.8344068526674736)
Andy is not guilty: True or False?
True (0.8196047517921394)
Andy has mean: True or False?
True (0.8089742709319104)
Andy has no mean: True or False?
True (0.7225270177274575)
Andy has motive: True or False?
True (0.8499711693725173)
Andy has no motive: True or False?
True (0.8013146490010521)
Andy has opportunity: True or False?
True (0.7725306828324007)
Andy has no opportunity: True or False?
True (0.6370307821695329)
Randy is guilty: True or False?
True (0.851212260635415)
Randy is not guilty: True or False?
True (0.8402590129647053)
Randy has mean: True or False?
True (0.8638517255508926)
Randy has no mean: True or False?
True (0.8289387819824735)
Randy has motive: True or False?
True (0.84619676525883)
Randy has no motive: True or False?
True (0.8438951328214825)
Randy has opportunity: True or False?
True (0.8267117710471246)
Randy has no opportunity: True or False?
True (0.7461389980806673)
Speedy is guilty: True or False?
True (0.8558511727823209)
Speedy is not guilty: True or False?
True (0.8507168263103924)
Speedy has mean: True or False?
True (0.8723473540228537)
Speedy has no mean: True or False?
True (0.8297680628665619)
Speedy has motive: True or False?
True (0.8580061839163521)
Speedy has no motive: True or False?
True (0.833053108978257)
Speedy has opportunity: True or False?
True (0.794384956668203)
Speedy has no opportunity: True or False?
True (0.7138307093362539)
### Abbott
- mean: True (0.8459423727595791)
- motive: True (0.8795611817678315)
- opportunity: True (0.8354835531737983)

### Andy
- mean: False (0.27747298227254247)
- motive: False (0.1986853509989479)
- opportunity: False (0.3629692178304671)

### Randy
- mean: False (0.1710612180175265)
- motive: False (0.15610486717851746)
- opportunity: False (0.2538610019193327)

### Speedy
- mean: False (0.1702319371334381)
- motive: False (0.16694689102174298)
- opportunity: False (0.2861692906637461)

The culprit is Abbott.
In fact, it is Speedy.
## 5minutemystery-the-april-fool
Map:  12%|█▏        | 25/203 [14:45<1:49:18, 36.85s/ examples]Map:  13%|█▎        | 26/203 [15:17<1:43:54, 35.22s/ examples]Boston, MA is guilty: True or False?
True (0.7634837587244478)
Boston, MA is not guilty: True or False?
True (0.77729988964086)
Boston, MA has mean: True or False?
True (0.7439129430200341)
Boston, MA has no mean: True or False?
True (0.5477060024984176)
Boston, MA has motive: True or False?
True (0.8649961951944259)
Boston, MA has no motive: True or False?
True (0.5214711377329961)
Boston, MA has opportunity: True or False?
True (0.8797679608387514)
Boston, MA has no opportunity: True or False?
False (0.5156199352405011)
Philadelphia, PA is guilty: True or False?
True (0.8204694405411458)
Philadelphia, PA is not guilty: True or False?
True (0.784649255215384)
Philadelphia, PA has mean: True or False?
True (0.8936811689868521)
Philadelphia, PA has no mean: True or False?
True (0.6697448487720212)
Philadelphia, PA has motive: True or False?
True (0.844921525814193)
Philadelphia, PA has no motive: True or False?
True (0.5660185351323219)
Philadelphia, PA has opportunity: True or False?
True (0.929696145502287)
Philadelphia, PA has no opportunity: True or False?
True (0.5273165068094335)
Pittsburgh, PA is guilty: True or False?
True (0.7994422859301654)
Pittsburgh, PA is not guilty: True or False?
True (0.7872777015429719)
Pittsburgh, PA has mean: True or False?
True (0.8620035048683017)
Pittsburgh, PA has no mean: True or False?
True (0.6370307821695329)
Pittsburgh, PA has motive: True or False?
True (0.8539127714046447)
Pittsburgh, PA has no motive: True or False?
True (0.5019531141001669)
Pittsburgh, PA has opportunity: True or False?
True (0.921357630313903)
Pittsburgh, PA has no opportunity: True or False?
False (0.6495786332146115)
Raleigh, NC is guilty: True or False?
True (0.6740504984987916)
Raleigh, NC is not guilty: True or False?
True (0.6749081498948247)
Raleigh, NC has mean: True or False?
True (0.7718434926244166)
Raleigh, NC has no mean: True or False?
False (0.5535053004623279)
Raleigh, NC has motive: True or False?
True (0.7745833916423246)
Raleigh, NC has no motive: True or False?
False (0.5851012033999957)
Raleigh, NC has opportunity: True or False?
True (0.7981867775042927)
Raleigh, NC has no opportunity: True or False?
False (0.8381505623254643)
Washington, DC is guilty: True or False?
True (0.7592253761865491)
Washington, DC is not guilty: True or False?
True (0.7669924589170153)
Washington, DC has mean: True or False?
True (0.8044059309478723)
Washington, DC has no mean: True or False?
True (0.5717666110200305)
Washington, DC has motive: True or False?
True (0.8080671968507699)
Washington, DC has no motive: True or False?
True (0.5409238326546766)
Washington, DC has opportunity: True or False?
True (0.8807970862580315)
Washington, DC has no opportunity: True or False?
False (0.7606506318580792)
### Boston, MA
- mean: False (0.4522939975015824)
- motive: False (0.47852886226700386)
- opportunity: False (0.0)

### Philadelphia, PA
- mean: False (0.33025515122797877)
- motive: False (0.4339814648676781)
- opportunity: False (0.47268349319056646)

### Pittsburgh, PA
- mean: False (0.3629692178304671)
- motive: False (0.49804688589983315)
- opportunity: False (0.0)

### Raleigh, NC
- mean: True (0.7718434926244166)
- motive: True (0.7745833916423246)
- opportunity: True (0.7981867775042927)

### Washington, DC
- mean: False (0.42823338897996954)
- motive: False (0.4590761673453234)
- opportunity: False (0.0)

The culprit is Raleigh, NC.
In fact, it is Washington, DC.
## 5minutemystery-green-feet
Carm is guilty: True or False?
True (0.811078188867804)
Carm is not guilty: True or False?
True (0.7348812840309261)
Carm has mean: True or False?
True (0.7585106418731645)
Carm has no mean: True or False?
True (0.6325027218909103)
Carm has motive: True or False?
True (0.8086723099497763)
Carm has no motive: True or False?
True (0.65489470935198)
Carm has opportunity: True or False?
True (0.6901415551283886)
Carm has no opportunity: True or False?
False (0.5888891269161294)
Diane is guilty: True or False?
True (0.7813306496768853)
Diane is not guilty: True or False?
True (0.8294919722593475)
Diane has mean: True or False?
True (0.8787311338092536)
Diane has no mean: True or False?
True (0.7813306496768853)
Diane has motive: True or False?
True (0.9289262900494157)
Diane has no motive: True or False?
True (0.8714748565614324)
Diane has opportunity: True or False?
True (0.8474634858439474)
Diane has no opportunity: True or False?
True (0.6918097054250644)
Jen is guilty: True or False?
True (0.6976089520497016)
Jen is not guilty: True or False?
True (0.7256486384635821)
Jen has mean: True or False?
True (0.769080279275001)
Jen has no mean: True or False?
True (0.6224592927728324)
Jen has motive: True or False?
True (0.8438951328214825)
Jen has no motive: True or False?
True (0.7476159948304097)
Jen has opportunity: True or False?
True (0.769080279275001)
Jen has no opportunity: True or False?
False (0.5898344400236791)
Maureen is guilty: True or False?
True (0.685107355950278)
Maureen is not guilty: True or False?
True (0.6842640693504702)
Maureen has mean: True or False?
True (0.6859494535376744)
Maureen has no mean: True or False?
False (0.5945512478395265)
Maureen has motive: True or False?
True (0.5341265295318852)
Maureen has no motive: True or False?
True (0.6261241441180464)
Maureen has opportunity: True or False?
False (0.6926419789019715)
Maureen has no opportunity: True or False?
False (0.7527403228571042)
### Carm
- mean: False (0.3674972781090897)
- motive: False (0.34510529064802)
- opportunity: False (0.0)

### Diane
- mean: False (0.21866935032311474)
- motive: False (0.12852514343856758)
- opportunity: False (0.30819029457493563)

### Jen
- mean: False (0.3775407072271676)
- motive: False (0.25238400516959025)
- opportunity: False (0.0)

### Maureen
- mean: True (0.6859494535376744)
- motive: True (0.5341265295318852)
- opportunity: True (0.24725967714289576)

The culprit is Maureen.
In fact, it is Diane.
## 5minutemystery-restaurant-roulette
Atsushi Nishi is guilty: True or False?
True (0.8116760258690822)
Atsushi Nishi is not guilty: True or False?
True (0.6557770400181139)
Atsushi Nishi has mean: True or False?
True (0.8305941261447712)
Atsushi Nishi has no mean: True or False?
False (0.5234203246639862)
Atsushi Nishi has motive: True or False?
True (0.6976088896786037)
Atsushi Nishi has no motive: True or False?
False (0.6697448487720212)
Atsushi Nishi has opportunity: True or False?
True (0.6749080895533367)
Atsushi Nishi has no opportunity: True or False?
False (0.7225269746614925)
Gianni Girodano is guilty: True or False?
True (0.7534665957068495)
Gianni Girodano is not guilty: True or False?
True (0.589834510337428)
Gianni Girodano has mean: True or False?
True (0.8766343647921183)
Gianni Girodano has no mean: True or False?
True (0.5544704821687028)
Gianni Girodano has motive: True or False?
True (0.7549149897594328)
Gianni Girodano has no motive: True or False?
False (0.5945512478395265)
Gianni Girodano has opportunity: True or False?
True (0.7527403228571042)
Gianni Girodano has no opportunity: True or False?
False (0.7483522884503825)
Jack McDonald is guilty: True or False?
True (0.8238958672039278)
Jack McDonald is not guilty: True or False?
True (0.7599387683150569)
Jack McDonald has mean: True or False?
True (0.7879311977554747)
Jack McDonald has no mean: True or False?
False (0.5292633777076584)
Jack McDonald has motive: True or False?
True (0.8647679145346777)
Jack McDonald has no motive: True or False?
True (0.6233768569026616)
Jack McDonald has opportunity: True or False?
True (0.8255897087847518)
Jack McDonald has no opportunity: True or False?
False (0.591723272524637)
Jean-Pierre Dubois is guilty: True or False?
True (0.9092645024391882)
Jean-Pierre Dubois is not guilty: True or False?
True (0.7950222460539826)
Jean-Pierre Dubois has mean: True or False?
True (0.9293122320338961)
Jean-Pierre Dubois has no mean: True or False?
True (0.6592954931819778)
Jean-Pierre Dubois has motive: True or False?
True (0.925499741040984)
Jean-Pierre Dubois has no motive: True or False?
True (0.6076631662366868)
Jean-Pierre Dubois has opportunity: True or False?
True (0.814643384779728)
Map:  13%|█▎        | 27/203 [15:48<1:39:28, 33.91s/ examples]Map:  14%|█▍        | 28/203 [16:25<1:41:45, 34.89s/ examples]Map:  14%|█▍        | 29/203 [17:00<1:41:48, 35.11s/ examples]Jean-Pierre Dubois has no opportunity: True or False?
False (0.6048657973050737)
### Atsushi Nishi
- mean: True (0.8305941261447712)
- motive: True (0.6976088896786037)
- opportunity: True (0.6749080895533367)

### Gianni Girodano
- mean: False (0.44552951783129724)
- motive: False (0.0)
- opportunity: False (0.0)

### Jack McDonald
- mean: False (0.0)
- motive: False (0.37662314309733835)
- opportunity: False (0.0)

### Jean-Pierre Dubois
- mean: False (0.3407045068180222)
- motive: False (0.3923368337633132)
- opportunity: False (0.0)

The culprit is Atsushi Nishi.
In fact, it is Gianni Girodano.
## 5minutemystery-violating-the-pirate-code
Bosun Ridley is guilty: True or False?
True (0.8868131040663721)
Bosun Ridley is not guilty: True or False?
True (0.8598992261321269)
Bosun Ridley has mean: True or False?
True (0.8606036289596553)
Bosun Ridley has no mean: True or False?
True (0.7799929399351836)
Bosun Ridley has motive: True or False?
True (0.8236122680985841)
Bosun Ridley has no motive: True or False?
True (0.7545534399785333)
Bosun Ridley has opportunity: True or False?
True (0.6610482284345209)
Bosun Ridley has no opportunity: True or False?
True (0.5822535180679596)
Mr Arbuthnot is guilty: True or False?
True (0.8357518369388613)
Mr Arbuthnot is not guilty: True or False?
False (0.6319063237614042)
Mr Arbuthnot has mean: True or False?
True (0.7648916137833577)
Mr Arbuthnot has no mean: True or False?
True (0.7166153802549532)
Mr Arbuthnot has motive: True or False?
True (0.7516481378170605)
Mr Arbuthnot has no motive: True or False?
True (0.6842640693504702)
Mr Arbuthnot has opportunity: True or False?
True (0.5331543669186894)
Mr Arbuthnot has no opportunity: True or False?
False (0.34836943817950694)
Nehemiah is guilty: True or False?
True (0.8591918406281239)
Nehemiah is not guilty: True or False?
True (0.894973220907352)
Nehemiah has mean: True or False?
True (0.7563575572780217)
Nehemiah has no mean: True or False?
True (0.6104534962074417)
Nehemiah has motive: True or False?
True (0.8025555002781843)
Nehemiah has no motive: True or False?
True (0.6513548405484016)
Nehemiah has opportunity: True or False?
True (0.7924643196339045)
Nehemiah has no opportunity: True or False?
True (0.5784481093360381)
Will is guilty: True or False?
True (0.844921525814193)
Will is not guilty: True or False?
True (0.8325091054785035)
Will has mean: True or False?
True (0.7556369876990674)
Will has no mean: True or False?
True (0.642432441257838)
Will has motive: True or False?
True (0.8846386054372942)
Will has no motive: True or False?
True (0.6825736720802238)
Will has opportunity: True or False?
True (0.7181992613394055)
Will has no opportunity: True or False?
True (0.5063473433729075)
### Bosun Ridley
- mean: False (0.2200070600648164)
- motive: False (0.2454465600214667)
- opportunity: False (0.41774648193204045)

### Mr Arbuthnot
- mean: True (0.7648916137833577)
- motive: True (0.7516481378170605)
- opportunity: True (0.6516305618204931)

### Nehemiah
- mean: False (0.3895465037925583)
- motive: False (0.34864515945159835)
- opportunity: False (0.4215518906639619)

### Will
- mean: False (0.35756755874216195)
- motive: False (0.3174263279197762)
- opportunity: False (0.49365265662709246)

The culprit is Mr Arbuthnot.
In fact, it is Bosun Ridley.
## 5minutemystery-space-station-sagittarius-six-suffers-sabotage
Cpl. Bennington is guilty: True or False?
True (0.9177460685312047)
Cpl. Bennington is not guilty: True or False?
True (0.9053223122169206)
Cpl. Bennington has mean: True or False?
True (0.9152045868398637)
Cpl. Bennington has no mean: True or False?
True (0.8615382357584752)
Cpl. Bennington has motive: True or False?
True (0.8955227118091885)
Cpl. Bennington has no motive: True or False?
True (0.8705973031072073)
Cpl. Bennington has opportunity: True or False?
True (0.8333246107254184)
Cpl. Bennington has no opportunity: True or False?
True (0.7041600870830834)
Scrivine is guilty: True or False?
True (0.9076402191395381)
Scrivine is not guilty: True or False?
True (0.9066531077351827)
Scrivine has mean: True or False?
True (0.8484706263347676)
Scrivine has no mean: True or False?
True (0.7178037814283548)
Scrivine has motive: True or False?
True (0.8933094122075369)
Scrivine has no motive: True or False?
True (0.8933094122075369)
Scrivine has opportunity: True or False?
True (0.8683809699466569)
Scrivine has no opportunity: True or False?
True (0.7431679939957333)
Sgt. O'Hennessey is guilty: True or False?
True (0.9375547191885567)
Sgt. O'Hennessey is not guilty: True or False?
True (0.9265699426348812)
Sgt. O'Hennessey has mean: True or False?
True (0.8868130446009216)
Sgt. O'Hennessey has no mean: True or False?
True (0.6141626144170799)
Sgt. O'Hennessey has motive: True or False?
True (0.8050197941712954)
Sgt. O'Hennessey has no motive: True or False?
True (0.7937461674149602)
Sgt. O'Hennessey has opportunity: True or False?
True (0.7279754274224494)
Sgt. O'Hennessey has no opportunity: True or False?
False (0.550607385906944)
Sgt.Valance is guilty: True or False?
True (0.9496693599006181)
Sgt.Valance is not guilty: True or False?
True (0.94519740270931)
Sgt.Valance has mean: True or False?
True (0.8807970862580315)
Sgt.Valance has no mean: True or False?
True (0.7416740115009234)
Sgt.Valance has motive: True or False?
True (0.9199306971612747)
Sgt.Valance has no motive: True or False?
True (0.8955226517597132)
Sgt.Valance has opportunity: True or False?
True (0.9265699426348812)
Sgt.Valance has no opportunity: True or False?
True (0.7718434926244166)
### Cpl. Bennington
- mean: False (0.1384617642415248)
- motive: False (0.1294026968927927)
- opportunity: False (0.2958399129169166)

### Scrivine
- mean: False (0.28219621857164523)
- motive: False (0.1066905877924631)
- opportunity: False (0.2568320060042667)

### Sgt. O'Hennessey
- mean: True (0.8868130446009216)
- motive: True (0.8050197941712954)
- opportunity: True (0.7279754274224494)

### Sgt.Valance
- mean: False (0.2583259884990766)
- motive: False (0.10447734824028676)
- opportunity: False (0.22815650737558335)

The culprit is Sgt. O'Hennessey.
In fact, it is Sgt.Valance.
## 5minutemystery-flying-saucer-of-new-mexico
Dora is guilty: True or False?
False (0.6415346823638186)
Dora is not guilty: True or False?
False (0.6469064338453809)
Dora has mean: True or False?
True (0.6842640081724978)
Dora has no mean: True or False?
False (0.6926419789019715)
Dora has motive: True or False?
True (0.6039317779631047)
Dora has no motive: True or False?
True (0.5136684743338078)
Dora has opportunity: True or False?
False (0.5869964306477841)
Dora has no opportunity: True or False?
False (0.7662936378892937)
Lester is guilty: True or False?
True (0.5774953314585229)
Lester is not guilty: True or False?
True (0.5679366075542497)
Lester has mean: True or False?
True (0.8376200175313318)
Lester has no mean: True or False?
True (0.5544704821687028)
Lester has motive: True or False?
True (0.7779753136455794)
Lester has no motive: True or False?
False (0.550607385906944)
Lester has opportunity: True or False?
False (0.5175709123121337)
Lester has no opportunity: True or False?
False (0.7549149897594328)
Uncle Art is guilty: True or False?
True (0.6469064338453809)
Uncle Art is not guilty: True or False?
True (0.6757645563841816)
Uncle Art has mean: True or False?
True (0.8816149238192855)
Uncle Art has no mean: True or False?
True (0.6714705702070799)
Uncle Art has motive: True or False?
True (0.8000678954040312)
Uncle Art has no motive: True or False?
True (0.591723272524637)
Uncle Art has opportunity: True or False?
True (0.5860490988363701)
Uncle Art has no opportunity: True or False?
False (0.6901415551283886)
Zach is guilty: True or False?
False (0.6076631662366868)
Zach is not guilty: True or False?
False (0.5341265295318852)
Zach has mean: True or False?
True (0.8278281666221954)
Zach has no mean: True or False?
False (0.5156198737738186)
Zach has motive: True or False?
True (0.7690802105138688)
Zach has no motive: True or False?
False (0.5185461538431656)
Zach has opportunity: True or False?
True (0.687629930977143)
Zach has no opportunity: True or False?
Map:  15%|█▍        | 30/203 [17:36<1:41:14, 35.11s/ examples]Map:  15%|█▌        | 31/203 [18:18<1:46:36, 37.19s/ examples]Map:  16%|█▌        | 32/203 [19:05<1:54:31, 40.19s/ examples]False (0.7563575572780217)
### Dora
- mean: False (0.0)
- motive: False (0.4863315256661922)
- opportunity: False (0.5869964306477841)

### Lester
- mean: False (0.44552951783129724)
- motive: False (0.0)
- opportunity: False (0.5175709123121337)

### Uncle Art
- mean: False (0.3285294297929201)
- motive: False (0.40827672747536303)
- opportunity: False (0.0)

### Zach
- mean: True (0.8278281666221954)
- motive: True (0.7690802105138688)
- opportunity: True (0.687629930977143)

The culprit is Zach.
In fact, it is Dora.
## 5minutemystery-great-musket-mystery
Lyle Day is guilty: True or False?
True (0.8509646659219744)
Lyle Day is not guilty: True or False?
True (0.8278281666221954)
Lyle Day has mean: True or False?
True (0.8951566249612815)
Lyle Day has no mean: True or False?
True (0.678326898500563)
Lyle Day has motive: True or False?
True (0.9018342514529875)
Lyle Day has no motive: True or False?
True (0.6370308391245257)
Lyle Day has opportunity: True or False?
True (0.8620035690925699)
Lyle Day has no opportunity: True or False?
True (0.5535053004623279)
Mary Wright is guilty: True or False?
True (0.8303191093049147)
Mary Wright is not guilty: True or False?
True (0.7892336789711022)
Mary Wright has mean: True or False?
True (0.8198933606225757)
Mary Wright has no mean: True or False?
True (0.5583269696343842)
Mary Wright has motive: True or False?
True (0.7799928701983835)
Mary Wright has no motive: True or False?
False (0.5126925663186335)
Mary Wright has opportunity: True or False?
True (0.6311396940785249)
Mary Wright has no opportunity: True or False?
False (0.6123096993178739)
Paul Revere is guilty: True or False?
True (0.7641883982873323)
Paul Revere is not guilty: True or False?
True (0.779321849347754)
Paul Revere has mean: True or False?
True (0.8098781635062345)
Paul Revere has no mean: True or False?
True (0.7446563751413027)
Paul Revere has motive: True or False?
True (0.8591918406281239)
Paul Revere has no motive: True or False?
True (0.580352087772514)
Paul Revere has opportunity: True or False?
True (0.7613610520273686)
Paul Revere has no opportunity: True or False?
False (0.5860491337676195)
Stevie Brown is guilty: True or False?
True (0.8795611817678315)
Stevie Brown is not guilty: True or False?
True (0.861538171568877)
Stevie Brown has mean: True or False?
True (0.9355823382423648)
Stevie Brown has no mean: True or False?
True (0.8272706865691472)
Stevie Brown has motive: True or False?
True (0.9170058945178141)
Stevie Brown has no motive: True or False?
True (0.720171518230031)
Stevie Brown has opportunity: True or False?
True (0.8984105603938967)
Stevie Brown has no opportunity: True or False?
True (0.648688963544537)
### Lyle Day
- mean: False (0.32167310149943695)
- motive: False (0.36296916087547426)
- opportunity: False (0.44649469953767207)

### Mary Wright
- mean: True (0.8198933606225757)
- motive: True (0.7799928701983835)
- opportunity: True (0.6311396940785249)

### Paul Revere
- mean: False (0.2553436248586973)
- motive: False (0.419647912227486)
- opportunity: False (0.0)

### Stevie Brown
- mean: False (0.17272931343085285)
- motive: False (0.279828481769969)
- opportunity: False (0.351311036455463)

The culprit is Mary Wright.
In fact, it is Lyle Day.
## 5minutemystery-true-green-a-st-patricks-day-mystery
Emily Carpenter is guilty: True or False?
True (0.8902941942359355)
Emily Carpenter is not guilty: True or False?
True (0.9429286143036572)
Emily Carpenter has mean: True or False?
True (0.8577681165234065)
Emily Carpenter has no mean: True or False?
True (0.941654147692963)
Emily Carpenter has motive: True or False?
True (0.8872045854516336)
Emily Carpenter has no motive: True or False?
True (0.8712559403160255)
Emily Carpenter has opportunity: True or False?
True (0.7325918054337844)
Emily Carpenter has no opportunity: True or False?
True (0.6113819501087365)
Evan Carpenter is guilty: True or False?
True (0.8842393162056825)
Evan Carpenter is not guilty: True or False?
True (0.9333093181503205)
Evan Carpenter has mean: True or False?
True (0.7988153087356352)
Evan Carpenter has no mean: True or False?
True (0.9396923783210908)
Evan Carpenter has motive: True or False?
True (0.9198588150310912)
Evan Carpenter has no motive: True or False?
True (0.9069007629623109)
Evan Carpenter has opportunity: True or False?
True (0.8654516347931567)
Evan Carpenter has no opportunity: True or False?
True (0.6095241816115718)
Richie Harris is guilty: True or False?
True (0.9000915285488901)
Richie Harris is not guilty: True or False?
True (0.9418683665706381)
Richie Harris has mean: True or False?
True (0.8413047772878592)
Richie Harris has no mean: True or False?
True (0.9229002605856774)
Richie Harris has motive: True or False?
True (0.9218515162673044)
Richie Harris has no motive: True or False?
True (0.923523366861227)
Richie Harris has opportunity: True or False?
True (0.8918110138739693)
Richie Harris has no opportunity: True or False?
True (0.8341368378998062)
Zachary MacDonald is guilty: True or False?
True (0.9194980842090085)
Zachary MacDonald is not guilty: True or False?
True (0.9401335713518422)
Zachary MacDonald has mean: True or False?
True (0.9326989068252284)
Zachary MacDonald has no mean: True or False?
True (0.9449946880768697)
Zachary MacDonald has motive: True or False?
True (0.947913945956991)
Zachary MacDonald has no motive: True or False?
True (0.9281487460975983)
Zachary MacDonald has opportunity: True or False?
True (0.8929365260632085)
Zachary MacDonald has no opportunity: True or False?
True (0.8037906314112822)
### Emily Carpenter
- mean: False (0.05834585230703704)
- motive: False (0.1287440596839745)
- opportunity: False (0.3886180498912635)

### Evan Carpenter
- mean: False (0.06030762167890924)
- motive: False (0.09309923703768908)
- opportunity: False (0.39047581838842815)

### Richie Harris
- mean: True (0.8413047772878592)
- motive: True (0.9218515162673044)
- opportunity: True (0.8918110138739693)

### Zachary MacDonald
- mean: False (0.055005311923130296)
- motive: False (0.07185125390240166)
- opportunity: False (0.19620936858871785)

The culprit is Richie Harris.
In fact, it is Emily Carpenter.
## 5minutemystery-st-patricks-day-pearls
Christopher is guilty: True or False?
True (0.8019358443954961)
Christopher is not guilty: True or False?
True (0.6513548405484016)
Christopher has mean: True or False?
True (0.8591918406281239)
Christopher has no mean: True or False?
True (0.6297746298200823)
Christopher has motive: True or False?
True (0.5409238971378262)
Christopher has no motive: True or False?
False (0.525368812147771)
Christopher has opportunity: True or False?
True (0.6224592927728324)
Christopher has no opportunity: True or False?
False (0.7745833916423246)
Earl is guilty: True or False?
True (0.5973730125048408)
Earl is not guilty: True or False?
True (0.5428632463719839)
Earl has mean: True or False?
True (0.897695304229796)
Earl has no mean: True or False?
True (0.5273165068094335)
Earl has motive: True or False?
True (0.5312093625105829)
Earl has no motive: True or False?
False (0.6636689235052821)
Earl has opportunity: True or False?
True (0.5195213440667139)
Earl has no opportunity: True or False?
False (0.8887587777822111)
Robert is guilty: True or False?
True (0.6048657973050737)
Robert is not guilty: True or False?
True (0.5860491337676195)
Robert has mean: True or False?
True (0.8499711693725173)
Robert has no mean: True or False?
True (0.5165954111147137)
Robert has motive: True or False?
False (0.5496406074054949)
Robert has no motive: True or False?
False (0.5879430860094185)
Robert has opportunity: True or False?
True (0.5009765603034438)
Robert has no opportunity: True or False?
False (0.8940517282497483)
Tom is guilty: True or False?
True (0.7599387683150569)
Tom is not guilty: True or False?
True (0.673191669892235)
Tom has mean: True or False?
True (0.8615382357584752)
Tom has no mean: True or False?
True (0.6654105788791005)
Tom has motive: True or False?
False (0.6388353131709135)
Tom has no motive: True or False?
False (0.7041601500399041)
Tom has opportunity: True or False?
True (0.5592900581575188)
Tom has no opportunity: True or False?
Map:  16%|█▋        | 33/203 [19:39<1:48:40, 38.36s/ examples]Map:  17%|█▋        | 34/203 [20:17<1:47:30, 38.17s/ examples]Map:  17%|█▋        | 35/203 [20:48<1:40:49, 36.01s/ examples]False (0.8464508054137014)
### Christopher
- mean: False (0.37022537017991775)
- motive: False (0.0)
- opportunity: False (0.0)

### Earl
- mean: True (0.897695304229796)
- motive: True (0.5312093625105829)
- opportunity: True (0.5195213440667139)

### Robert
- mean: False (0.48340458888528626)
- motive: False (0.5496406074054949)
- opportunity: False (0.0)

### Tom
- mean: False (0.3345894211208995)
- motive: False (0.6388353131709135)
- opportunity: False (0.0)

The culprit is Earl.
In fact, it is Tom.
## 5minutemystery-death-in-the-theatre
Helen Smith is guilty: True or False?
True (0.8264318083792933)
Helen Smith is not guilty: True or False?
True (0.7029380655939949)
Helen Smith has mean: True or False?
True (0.7819973291046377)
Helen Smith has no mean: True or False?
True (0.6169357925086439)
Helen Smith has motive: True or False?
True (0.8134607635851566)
Helen Smith has no motive: True or False?
True (0.6636689235052821)
Helen Smith has opportunity: True or False?
True (0.6654105193867614)
Helen Smith has no opportunity: True or False?
False (0.6090592200072807)
Joanne Driscoll is guilty: True or False?
True (0.8155264872684852)
Joanne Driscoll is not guilty: True or False?
True (0.7386690954574974)
Joanne Driscoll has mean: True or False?
True (0.9265699426348812)
Joanne Driscoll has no mean: True or False?
True (0.6039318499573872)
Joanne Driscoll has motive: True or False?
True (0.7759445796581789)
Joanne Driscoll has no motive: True or False?
True (0.5860491337676195)
Joanne Driscoll has opportunity: True or False?
True (0.6636689235052821)
Joanne Driscoll has no opportunity: True or False?
False (0.5774954003013352)
Kevin Doyle is guilty: True or False?
True (0.8504685773080045)
Kevin Doyle is not guilty: True or False?
True (0.8250265688168699)
Kevin Doyle has mean: True or False?
True (0.8128672807499561)
Kevin Doyle has no mean: True or False?
True (0.7090191197769757)
Kevin Doyle has motive: True or False?
True (0.7563575572780217)
Kevin Doyle has no motive: True or False?
False (0.5068355091660127)
Kevin Doyle has opportunity: True or False?
True (0.6834195192071987)
Kevin Doyle has no opportunity: True or False?
True (0.6315943123389512)
Sarah Jones is guilty: True or False?
True (0.8255897087847518)
Sarah Jones is not guilty: True or False?
True (0.6976088896786037)
Sarah Jones has mean: True or False?
True (0.8543993851297865)
Sarah Jones has no mean: True or False?
True (0.6415346823638186)
Sarah Jones has motive: True or False?
True (0.7386690954574974)
Sarah Jones has no motive: True or False?
True (0.5467381591701916)
Sarah Jones has opportunity: True or False?
True (0.5496406074054949)
Sarah Jones has no opportunity: True or False?
False (0.5679366075542497)
### Helen Smith
- mean: False (0.38306420749135606)
- motive: False (0.33633107649471794)
- opportunity: False (0.0)

### Joanne Driscoll
- mean: False (0.39606815004261275)
- motive: False (0.41395086623238053)
- opportunity: False (0.0)

### Kevin Doyle
- mean: True (0.8128672807499561)
- motive: True (0.7563575572780217)
- opportunity: True (0.6834195192071987)

### Sarah Jones
- mean: False (0.3584653176361814)
- motive: False (0.45326184082980836)
- opportunity: False (0.0)

The culprit is Kevin Doyle.
In fact, it is Kevin Doyle.
## 5minutemystery-death-at-andersonville
Corporal Wardlow Horner is guilty: True or False?
True (0.8267118326419537)
Corporal Wardlow Horner is not guilty: True or False?
True (0.7341195403199204)
Corporal Wardlow Horner has mean: True or False?
True (0.7978720077929541)
Corporal Wardlow Horner has no mean: True or False?
True (0.6001883144765984)
Corporal Wardlow Horner has motive: True or False?
True (0.7209580648179327)
Corporal Wardlow Horner has no motive: True or False?
True (0.6279512069990912)
Corporal Wardlow Horner has opportunity: True or False?
True (0.6415346250061509)
Corporal Wardlow Horner has no opportunity: True or False?
True (0.5486734987923966)
Private Jamie Whisenant is guilty: True or False?
True (0.7541915688671895)
Private Jamie Whisenant is not guilty: True or False?
True (0.6566582306092376)
Private Jamie Whisenant has mean: True or False?
True (0.6662796746479285)
Private Jamie Whisenant has no mean: True or False?
False (0.6522414018725713)
Private Jamie Whisenant has motive: True or False?
True (0.6141626144170799)
Private Jamie Whisenant has no motive: True or False?
False (0.5224457875179084)
Private Jamie Whisenant has opportunity: True or False?
False (0.6992544513448877)
Private Jamie Whisenant has no opportunity: True or False?
False (0.5926666351772785)
Sergeant Coleman Crosby is guilty: True or False?
True (0.7302898714065358)
Sergeant Coleman Crosby is not guilty: True or False?
True (0.7138307731576955)
Sergeant Coleman Crosby has mean: True or False?
True (0.7997552678397243)
Sergeant Coleman Crosby has no mean: True or False?
True (0.6680145240815963)
Sergeant Coleman Crosby has motive: True or False?
True (0.49999999904767284)
Sergeant Coleman Crosby has no motive: True or False?
True (0.5312093941731293)
Sergeant Coleman Crosby has opportunity: True or False?
True (0.5029296229885981)
Sergeant Coleman Crosby has no opportunity: True or False?
True (0.5214711998972037)
Sergeant Josiah Thornton is guilty: True or False?
True (0.7098244343353132)
Sergeant Josiah Thornton is not guilty: True or False?
True (0.7225270177274575)
Sergeant Josiah Thornton has mean: True or False?
True (0.6817267588564826)
Sergeant Josiah Thornton has no mean: True or False?
False (0.5573635130218721)
Sergeant Josiah Thornton has motive: True or False?
False (0.6001883144765984)
Sergeant Josiah Thornton has no motive: True or False?
False (0.5360700410935405)
Sergeant Josiah Thornton has opportunity: True or False?
False (0.5331544304756466)
Sergeant Josiah Thornton has no opportunity: True or False?
False (0.6270381219830087)
### Corporal Wardlow Horner
- mean: False (0.3998116855234016)
- motive: False (0.37204879300090876)
- opportunity: False (0.4513265012076034)

### Private Jamie Whisenant
- mean: True (0.6662796746479285)
- motive: True (0.6141626144170799)
- opportunity: True (0.40733336482272153)

### Sergeant Coleman Crosby
- mean: False (0.33198547591840366)
- motive: False (0.4687906058268707)
- opportunity: False (0.4785288001027963)

### Sergeant Josiah Thornton
- mean: False (0.0)
- motive: False (0.6001883144765984)
- opportunity: False (0.5331544304756466)

The culprit is Private Jamie Whisenant.
In fact, it is Sergeant Josiah Thornton.
## 5minutemystery-the-big-game
Carli Antor is guilty: True or False?
True (0.9273632783787477)
Carli Antor is not guilty: True or False?
True (0.9049869771631355)
Carli Antor has mean: True or False?
True (0.9449946880768697)
Carli Antor has no mean: True or False?
True (0.7950223052877581)
Carli Antor has motive: True or False?
True (0.8816149238192855)
Carli Antor has no motive: True or False?
True (0.8688267468984366)
Carli Antor has opportunity: True or False?
True (0.5418937216067536)
Carli Antor has no opportunity: True or False?
True (0.6469064338453809)
Chuck Jarrett is guilty: True or False?
True (0.9114953904850286)
Chuck Jarrett is not guilty: True or False?
True (0.8397339530959691)
Chuck Jarrett has mean: True or False?
True (0.9073122118500465)
Chuck Jarrett has no mean: True or False?
True (0.7655933544531522)
Chuck Jarrett has motive: True or False?
True (0.8514594452543962)
Chuck Jarrett has no motive: True or False?
True (0.9105454073245608)
Chuck Jarrett has opportunity: True or False?
True (0.5841525779336078)
Chuck Jarrett has no opportunity: True or False?
True (0.6976088896786037)
Rich Pender is guilty: True or False?
True (0.905656637917298)
Rich Pender is not guilty: True or False?
True (0.8529354311342636)
Rich Pender has mean: True or False?
True (0.9355823382423648)
Rich Pender has no mean: True or False?
True (0.7090191831682278)
Rich Pender has motive: True or False?
True (0.6233768940588188)
Rich Pender has no motive: True or False?
True (0.8104789202520752)
Rich Pender has opportunity: True or False?
False (0.5688949093320547)
Rich Pender has no opportunity: True or False?
False (0.570809902165233)
Map:  18%|█▊        | 36/203 [21:24<1:40:30, 36.11s/ examples]Map:  18%|█▊        | 37/203 [21:55<1:36:08, 34.75s/ examples]Map:  19%|█▊        | 38/203 [22:23<1:29:24, 32.51s/ examples]Tom Barrett is guilty: True or False?
True (0.9196425651151865)
Tom Barrett is not guilty: True or False?
True (0.8241790481509624)
Tom Barrett has mean: True or False?
True (0.8951566249612815)
Tom Barrett has no mean: True or False?
True (0.5746334908651781)
Tom Barrett has motive: True or False?
True (0.769080279275001)
Tom Barrett has no motive: True or False?
True (0.8031737798924701)
Tom Barrett has opportunity: True or False?
True (0.5631377056275331)
Tom Barrett has no opportunity: True or False?
True (0.5078118910577802)
### Carli Antor
- mean: False (0.20497769471224192)
- motive: False (0.13117325310156336)
- opportunity: False (0.35309356615461907)

### Chuck Jarrett
- mean: True (0.9073122118500465)
- motive: True (0.8514594452543962)
- opportunity: True (0.5841525779336078)

### Rich Pender
- mean: False (0.29098081683177224)
- motive: False (0.18952107974792476)
- opportunity: False (0.5688949093320547)

### Tom Barrett
- mean: False (0.4253665091348219)
- motive: False (0.19682622010752993)
- opportunity: False (0.49218810894221976)

The culprit is Chuck Jarrett.
In fact, it is Tom Barrett.
## 5minutemystery-the-liberty-gun
Bob Turkle is guilty: True or False?
True (0.6884683992569801)
Bob Turkle is not guilty: True or False?
True (0.7057849857500714)
Bob Turkle has mean: True or False?
True (0.5621764690603255)
Bob Turkle has no mean: True or False?
False (0.5869964306477841)
Bob Turkle has motive: True or False?
True (0.833053108978257)
Bob Turkle has no motive: True or False?
True (0.7853085971692302)
Bob Turkle has opportunity: True or False?
True (0.6817267588564826)
Bob Turkle has no opportunity: True or False?
True (0.6370308391245257)
Captain Parker is guilty: True or False?
True (0.8824278665848695)
Captain Parker is not guilty: True or False?
True (0.9026095892260383)
Captain Parker has mean: True or False?
True (0.6909763109505791)
Captain Parker has no mean: True or False?
True (0.6379334932841956)
Captain Parker has motive: True or False?
True (0.8891444205417208)
Captain Parker has no motive: True or False?
True (0.8278281666221954)
Captain Parker has opportunity: True or False?
True (0.8354835531737983)
Captain Parker has no opportunity: True or False?
True (0.7217432334405754)
Paul Rhodes is guilty: True or False?
True (0.6671476985798853)
Paul Rhodes is not guilty: True or False?
True (0.6039318499573872)
Paul Rhodes has mean: True or False?
False (0.6504672161860058)
Paul Rhodes has no mean: True or False?
False (0.6967842494573921)
Paul Rhodes has motive: True or False?
True (0.7468781997658912)
Paul Rhodes has no motive: True or False?
True (0.7065955344877805)
Paul Rhodes has opportunity: True or False?
True (0.5380123829088157)
Paul Rhodes has no opportunity: True or False?
False (0.5380124470448935)
Tom Wise is guilty: True or False?
True (0.6884684608108543)
Tom Wise is not guilty: True or False?
True (0.6315943123389512)
Tom Wise has mean: True or False?
False (0.5612148661921673)
Tom Wise has no mean: True or False?
False (0.7379143332111532)
Tom Wise has motive: True or False?
True (0.7759445334082792)
Tom Wise has no motive: True or False?
True (0.6825737331070684)
Tom Wise has opportunity: True or False?
True (0.5389832197022594)
Tom Wise has no opportunity: True or False?
True (0.5688948754232768)
### Bob Turkle
- mean: True (0.5621764690603255)
- motive: True (0.833053108978257)
- opportunity: True (0.6817267588564826)

### Captain Parker
- mean: False (0.3620665067158044)
- motive: False (0.17217183337780462)
- opportunity: False (0.27825676655942455)

### Paul Rhodes
- mean: False (0.6504672161860058)
- motive: False (0.29340446551221955)
- opportunity: False (0.0)

### Tom Wise
- mean: False (0.5612148661921673)
- motive: False (0.31742626689293163)
- opportunity: False (0.43110512457672323)

The culprit is Bob Turkle.
In fact, it is Captain Parker.
## 5minutemystery-summer-camp
Allie is guilty: True or False?
True (0.8062431235779619)
Allie is not guilty: True or False?
True (0.8509647293237851)
Allie has mean: True or False?
True (0.8828325273478573)
Allie has no mean: True or False?
True (0.7592253761865491)
Allie has motive: True or False?
True (0.9173026661190045)
Allie has no motive: True or False?
True (0.7879311977554747)
Allie has opportunity: True or False?
True (0.9066531685310133)
Allie has no opportunity: True or False?
True (0.64779823427608)
Danny is guilty: True or False?
True (0.8267118326419537)
Danny is not guilty: True or False?
True (0.8349459127213729)
Danny has mean: True or False?
True (0.9447913165152162)
Danny has no mean: True or False?
True (0.8092759828926619)
Danny has motive: True or False?
True (0.9032942081209032)
Danny has no motive: True or False?
True (0.7846493136763113)
Danny has opportunity: True or False?
True (0.9233161821369215)
Danny has no opportunity: True or False?
True (0.7585106418731645)
Diane's campers is guilty: True or False?
False (0.5136684743338078)
Diane's campers is not guilty: True or False?
False (0.6495786332146115)
Diane's campers has mean: True or False?
True (0.8820220178442959)
Diane's campers has no mean: True or False?
False (0.5068355091660127)
Diane's campers has motive: True or False?
True (0.8958875533219306)
Diane's campers has no motive: True or False?
True (0.6020615685826383)
Diane's campers has opportunity: True or False?
True (0.779321849347754)
Diane's campers has no opportunity: True or False?
False (0.7490872087035162)
Tom is guilty: True or False?
True (0.8044058710149623)
Tom is not guilty: True or False?
True (0.8255897087847518)
Tom has mean: True or False?
True (0.8322366416985943)
Tom has no mean: True or False?
True (0.8050197941712954)
Tom has motive: True or False?
True (0.9407897579933674)
Tom has no motive: True or False?
True (0.7348812183274223)
Tom has opportunity: True or False?
True (0.9299510719523877)
Tom has no opportunity: True or False?
True (0.7711548682745724)
### Allie
- mean: False (0.24077462381345094)
- motive: False (0.2120688022445253)
- opportunity: False (0.35220176572392004)

### Danny
- mean: False (0.1907240171073381)
- motive: False (0.2153506863236887)
- opportunity: False (0.24148935812683547)

### Diane's campers
- mean: True (0.8820220178442959)
- motive: True (0.8958875533219306)
- opportunity: True (0.779321849347754)

### Tom
- mean: False (0.19498020582870457)
- motive: False (0.26511878167257774)
- opportunity: False (0.22884513172542764)

The culprit is Diane's campers.
In fact, it is Tom.
## 5minutemystery-mystery-at-lyndleys-fort
Bo is guilty: True or False?
True (0.6261241441180464)
Bo is not guilty: True or False?
True (0.7289910223595887)
Bo has mean: True or False?
True (0.772530728878819)
Bo has no mean: True or False?
False (0.5592899914849522)
Bo has motive: True or False?
True (0.7162185953247016)
Bo has no motive: True or False?
False (0.5640984675176304)
Bo has opportunity: True or False?
True (0.6113819501087365)
Bo has no opportunity: True or False?
False (0.6943026818003076)
John is guilty: True or False?
True (0.6513547823127435)
John is not guilty: True or False?
True (0.6706082735718226)
John has mean: True or False?
True (0.6671476389322356)
John has no mean: True or False?
False (0.6288633913849659)
John has motive: True or False?
True (0.6548947679041324)
John has no motive: True or False?
True (0.5273165696704634)
John has opportunity: True or False?
False (0.5204963206682631)
John has no opportunity: True or False?
False (0.7866228249849953)
John's wife is guilty: True or False?
True (0.5936093435000638)
John's wife is not guilty: True or False?
True (0.6206216296838327)
John's wife has mean: True or False?
True (0.514644215419305)
John's wife has no mean: True or False?
False (0.6697448487720212)
John's wife has motive: True or False?
True (0.6123096993178739)
John's wife has no motive: True or False?
True (0.5009765603034438)
John's wife has opportunity: True or False?
False (0.5794003525136094)
John's wife has no opportunity: True or False?
False (0.7711548223101617)
Nathan Drew is guilty: True or False?
True (0.7512833387594996)
Nathan Drew is not guilty: True or False?
True (0.7033457711626864)
Nathan Drew has mean: True or False?
Map:  19%|█▉        | 39/203 [23:01<1:33:31, 34.22s/ examples]Map:  20%|█▉        | 40/203 [23:32<1:30:27, 33.30s/ examples]Map:  20%|██        | 41/203 [24:12<1:35:30, 35.37s/ examples]True (0.7918210572836727)
Nathan Drew has no mean: True or False?
False (0.5117165908639297)
Nathan Drew has motive: True or False?
True (0.5058591351869154)
Nathan Drew has no motive: True or False?
False (0.5822535180679596)
Nathan Drew has opportunity: True or False?
True (0.525368812147771)
Nathan Drew has no opportunity: True or False?
False (0.6424325178417575)
### Bo
- mean: True (0.772530728878819)
- motive: True (0.7162185953247016)
- opportunity: True (0.6113819501087365)

### John
- mean: False (0.0)
- motive: False (0.47268343032953664)
- opportunity: False (0.5204963206682631)

### John's wife
- mean: False (0.0)
- motive: False (0.49902343969655616)
- opportunity: False (0.5794003525136094)

### Nathan Drew
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.0)

The culprit is Bo.
In fact, it is Nathan Drew.
## 5minutemystery-riddle-of-the-confederate-spy
Garrett is guilty: True or False?
True (0.8134607635851566)
Garrett is not guilty: True or False?
True (0.8019358443954961)
Garrett has mean: True or False?
True (0.6774740084332073)
Garrett has no mean: True or False?
False (0.5765419579552815)
Garrett has motive: True or False?
True (0.7302898278778687)
Garrett has no motive: True or False?
True (0.5973730125048408)
Garrett has opportunity: True or False?
True (0.6242935037467142)
Garrett has no opportunity: True or False?
False (0.5009765603034438)
McMurty is guilty: True or False?
True (0.811078188867804)
McMurty is not guilty: True or False?
True (0.7170118721569225)
McMurty has mean: True or False?
True (0.646013666311734)
McMurty has no mean: True or False?
False (0.6584174547581384)
McMurty has motive: True or False?
True (0.6592954931819778)
McMurty has no motive: True or False?
True (0.6224592927728324)
McMurty has opportunity: True or False?
True (0.589834510337428)
McMurty has no opportunity: True or False?
False (0.5438325284393795)
Parker is guilty: True or False?
True (0.8294919722593475)
Parker is not guilty: True or False?
True (0.779321849347754)
Parker has mean: True or False?
False (0.5583269696343842)
Parker has no mean: True or False?
False (0.6601723415572317)
Parker has motive: True or False?
True (0.7098243920264812)
Parker has no motive: True or False?
False (0.5448013654847448)
Parker has opportunity: True or False?
True (0.6297746298200823)
Parker has no opportunity: True or False?
False (0.6169357925086439)
Winslow is guilty: True or False?
True (0.7416740115009234)
Winslow is not guilty: True or False?
True (0.6884683992569801)
Winslow has mean: True or False?
True (0.7872777601997338)
Winslow has no mean: True or False?
False (0.6610481693322063)
Winslow has motive: True or False?
True (0.7371581892031299)
Winslow has no motive: True or False?
True (0.5156198737738186)
Winslow has opportunity: True or False?
True (0.6187805031861143)
Winslow has no opportunity: True or False?
False (0.5888891620166576)
### Garrett
- mean: False (0.0)
- motive: False (0.40262698749515924)
- opportunity: False (0.0)

### McMurty
- mean: False (0.0)
- motive: False (0.3775407072271676)
- opportunity: False (0.0)

### Parker
- mean: False (0.5583269696343842)
- motive: False (0.0)
- opportunity: False (0.0)

### Winslow
- mean: True (0.7872777601997338)
- motive: True (0.7371581892031299)
- opportunity: True (0.6187805031861143)

The culprit is Winslow.
In fact, it is Parker.
## 5minutemystery-thin-ice
Hortence Lacombe is guilty: True or False?
True (1.1753115908088394)
Hortence Lacombe is not guilty: True or False?
True (2.08588779141888)
Hortence Lacombe has mean: True or False?
True (0.8193157928301305)
Hortence Lacombe has no mean: True or False?
False (0.5660185351323219)
Hortence Lacombe has motive: True or False?
True (0.875361437979977)
Hortence Lacombe has no motive: True or False?
True (0.7229183995281547)
Hortence Lacombe has opportunity: True or False?
True (0.7162185953247016)
Hortence Lacombe has no opportunity: True or False?
True (0.5126925663186335)
Joe Tucker is guilty: True or False?
True (1.3047351787611419)
Joe Tucker is not guilty: True or False?
True (3.4605966327977717)
Joe Tucker has mean: True or False?
True (0.9092645024391882)
Joe Tucker has no mean: True or False?
True (0.6352224318508648)
Joe Tucker has motive: True or False?
True (0.9644220465248259)
Joe Tucker has no motive: True or False?
True (1.1675094501559435)
Joe Tucker has opportunity: True or False?
True (0.7956581141325956)
Joe Tucker has no opportunity: True or False?
True (0.8487329247174312)
Mikey Chanowski is guilty: True or False?
True (0.955152093302995)
Mikey Chanowski is not guilty: True or False?
True (1.3850158424012233)
Mikey Chanowski has mean: True or False?
True (0.7826624547920057)
Mikey Chanowski has no mean: True or False?
True (0.7017130830397807)
Mikey Chanowski has motive: True or False?
True (0.9412234437340664)
Mikey Chanowski has no motive: True or False?
True (0.8580061839163521)
Mikey Chanowski has opportunity: True or False?
True (0.7409249009267298)
Mikey Chanowski has no opportunity: True or False?
True (0.8122723669190336)
Shea Callaghan is guilty: True or False?
True (0.9177460685312047)
Shea Callaghan is not guilty: True or False?
True (1.1679726567218445)
Shea Callaghan has mean: True or False?
True (0.8899121304559661)
Shea Callaghan has no mean: True or False?
True (0.7962924261546153)
Shea Callaghan has motive: True or False?
True (0.8322366416985943)
Shea Callaghan has no motive: True or False?
True (0.6370308391245257)
Shea Callaghan has opportunity: True or False?
True (0.7759445334082792)
Shea Callaghan has no opportunity: True or False?
True (0.6001883144765984)
### Hortence Lacombe
- mean: True (0.8193157928301305)
- motive: True (0.875361437979977)
- opportunity: True (0.7162185953247016)

### Joe Tucker
- mean: False (0.3647775681491352)
- motive: False (0.0)
- opportunity: False (0.15126707528256877)

### Mikey Chanowski
- mean: False (0.29828691696021925)
- motive: False (0.14199381608364792)
- opportunity: False (0.1877276330809664)

### Shea Callaghan
- mean: False (0.20370757384538474)
- motive: False (0.36296916087547426)
- opportunity: False (0.3998116855234016)

The culprit is Hortence Lacombe.
In fact, it is Shea Callaghan.
## 5minutemystery-flouted
Chloe Streamer is guilty: True or False?
True (0.7364006034245382)
Chloe Streamer is not guilty: True or False?
True (0.7549149897594328)
Chloe Streamer has mean: True or False?
True (0.7563575572780217)
Chloe Streamer has no mean: True or False?
False (0.5399537164111071)
Chloe Streamer has motive: True or False?
True (0.8381505623254643)
Chloe Streamer has no motive: True or False?
True (0.720171518230031)
Chloe Streamer has opportunity: True or False?
False (0.6076631662366868)
Chloe Streamer has no opportunity: True or False?
False (0.6279512069990912)
Lyle Esposito is guilty: True or False?
True (0.8899121304559661)
Lyle Esposito is not guilty: True or False?
True (0.9135223603071148)
Lyle Esposito has mean: True or False?
True (0.9127477403975288)
Lyle Esposito has no mean: True or False?
True (0.6909763109505791)
Lyle Esposito has motive: True or False?
True (0.8710367026584496)
Lyle Esposito has no motive: True or False?
True (0.8158201638039532)
Lyle Esposito has opportunity: True or False?
True (0.6388353131709135)
Lyle Esposito has no opportunity: True or False?
False (0.5312093625105829)
Marty Nolan is guilty: True or False?
True (0.8740772565226612)
Marty Nolan is not guilty: True or False?
True (0.884439109617765)
Marty Nolan has mean: True or False?
True (0.9086178579521682)
Marty Nolan has no mean: True or False?
True (0.5774954003013352)
Marty Nolan has motive: True or False?
True (0.8795611817678315)
Marty Nolan has no motive: True or False?
True (0.7025300310583819)
Marty Nolan has opportunity: True or False?
True (0.6178585826183487)
Marty Nolan has no opportunity: True or False?
False (0.5688948754232768)
Susan Moorgate is guilty: True or False?
True (0.8370879250561812)
Susan Moorgate is not guilty: True or False?
True (0.7648915681922661)
Susan Moorgate has mean: True or False?
True (0.9049869164790318)
Susan Moorgate has no mean: True or False?
True (0.6388353131709135)
Map:  21%|██        | 42/203 [24:51<1:37:42, 36.41s/ examples]Map:  21%|██        | 43/203 [25:23<1:33:25, 35.04s/ examples]Map:  22%|██▏       | 44/203 [26:04<1:37:15, 36.70s/ examples]Susan Moorgate has motive: True or False?
True (0.7969253675907205)
Susan Moorgate has no motive: True or False?
True (0.6817267588564826)
Susan Moorgate has opportunity: True or False?
False (0.5907791930117218)
Susan Moorgate has no opportunity: True or False?
False (0.7287483223557857)
### Chloe Streamer
- mean: True (0.7563575572780217)
- motive: True (0.8381505623254643)
- opportunity: True (0.37204879300090876)

### Lyle Esposito
- mean: False (0.3090236890494209)
- motive: False (0.18417983619604683)
- opportunity: False (0.0)

### Marty Nolan
- mean: False (0.42250459969866483)
- motive: False (0.29746996894161815)
- opportunity: False (0.0)

### Susan Moorgate
- mean: False (0.36116468682908653)
- motive: False (0.3182732411435174)
- opportunity: False (0.5907791930117218)

The culprit is Chloe Streamer.
In fact, it is Marty Nolan.
## 5minutemystery-car-trouble
Mr. Carlson is guilty: True or False?
True (0.7806625377756776)
Mr. Carlson is not guilty: True or False?
True (0.7098243920264812)
Mr. Carlson has mean: True or False?
True (0.8883720049821552)
Mr. Carlson has no mean: True or False?
True (0.6662796746479285)
Mr. Carlson has motive: True or False?
True (0.9175984877579624)
Mr. Carlson has no motive: True or False?
True (0.8418256636710214)
Mr. Carlson has opportunity: True or False?
True (0.7988153087356352)
Mr. Carlson has no opportunity: True or False?
True (0.5126926274363537)
Mr. Leamington is guilty: True or False?
True (0.879146760693242)
Mr. Leamington is not guilty: True or False?
True (0.7898827135821628)
Mr. Leamington has mean: True or False?
True (0.8906751877407573)
Mr. Leamington has no mean: True or False?
True (0.6984323202883935)
Mr. Leamington has motive: True or False?
True (0.9224823751318276)
Mr. Leamington has no motive: True or False?
True (0.8891444205417208)
Mr. Leamington has opportunity: True or False?
True (0.8238958672039278)
Mr. Leamington has no opportunity: True or False?
True (0.5331543669186894)
Mrs. Roberts is guilty: True or False?
True (0.8812065732757132)
Mrs. Roberts is not guilty: True or False?
True (0.8464508684792033)
Mrs. Roberts has mean: True or False?
True (0.9381240005131491)
Mrs. Roberts has no mean: True or False?
True (0.7065954713132195)
Mrs. Roberts has motive: True or False?
True (0.952397347230678)
Mrs. Roberts has no motive: True or False?
True (0.8615382357584752)
Mrs. Roberts has opportunity: True or False?
True (0.8906751877407573)
Mrs. Roberts has no opportunity: True or False?
True (0.5292633777076584)
Randy Peters is guilty: True or False?
True (0.816406362162552)
Randy Peters is not guilty: True or False?
True (0.7356416476869558)
Randy Peters has mean: True or False?
True (0.8683809699466569)
Randy Peters has no mean: True or False?
True (0.6610481693322063)
Randy Peters has motive: True or False?
True (0.879146760693242)
Randy Peters has no motive: True or False?
True (0.7732163648437078)
Randy Peters has opportunity: True or False?
True (0.6680145240815963)
Randy Peters has no opportunity: True or False?
False (0.5936092727363199)
### Mr. Carlson
- mean: False (0.3337203253520715)
- motive: False (0.1581743363289786)
- opportunity: False (0.4873073725636463)

### Mr. Leamington
- mean: False (0.3015676797116065)
- motive: False (0.11085557945827917)
- opportunity: False (0.46684563308131055)

### Mrs. Roberts
- mean: False (0.29340452868678046)
- motive: False (0.1384617642415248)
- opportunity: False (0.4707366222923416)

### Randy Peters
- mean: True (0.8683809699466569)
- motive: True (0.879146760693242)
- opportunity: True (0.6680145240815963)

The culprit is Randy Peters.
In fact, it is Randy Peters.
## 5minutemystery-mr-poes-birthday-party
Anthony is guilty: True or False?
True (0.6370307821695329)
Anthony is not guilty: True or False?
True (0.6825736720802238)
Anthony has mean: True or False?
True (0.7592253761865491)
Anthony has no mean: True or False?
False (0.5888891269161294)
Anthony has motive: True or False?
True (0.8918110736745599)
Anthony has no motive: True or False?
True (0.5573635130218721)
Anthony has opportunity: True or False?
True (0.6951311179371613)
Anthony has no opportunity: True or False?
False (0.6315943123389512)
Connor is guilty: True or False?
True (0.7969253675907205)
Connor is not guilty: True or False?
True (0.814643384779728)
Connor has mean: True or False?
True (0.7911764307711107)
Connor has no mean: True or False?
True (0.595492552580428)
Connor has motive: True or False?
True (0.9479621664653681)
Connor has no motive: True or False?
True (0.7138307093362539)
Connor has opportunity: True or False?
True (0.814643384779728)
Connor has no opportunity: True or False?
False (0.5621764690603255)
Skylar is guilty: True or False?
True (0.6893056096647525)
Skylar is not guilty: True or False?
True (0.743912876509037)
Skylar has mean: True or False?
True (0.6388353131709135)
Skylar has no mean: True or False?
False (0.7041600870830834)
Skylar has motive: True or False?
True (0.8050197941712954)
Skylar has no motive: True or False?
True (0.555435161888281)
Skylar has opportunity: True or False?
False (0.5234203246639862)
Skylar has no opportunity: True or False?
False (0.7333564224770464)
Stephen is guilty: True or False?
True (0.7606506998655483)
Stephen is not guilty: True or False?
True (0.814643384779728)
Stephen has mean: True or False?
True (0.767689835247798)
Stephen has no mean: True or False?
False (0.5409238326546766)
Stephen has motive: True or False?
True (0.9099069836112468)
Stephen has no motive: True or False?
True (0.7839884808423031)
Stephen has opportunity: True or False?
True (0.6918097672776748)
Stephen has no opportunity: True or False?
False (0.5195212821349473)
Tommy is guilty: True or False?
True (0.6592954931819778)
Tommy is not guilty: True or False?
True (0.7287483223557857)
Tommy has mean: True or False?
True (0.821044090050916)
Tommy has no mean: True or False?
False (0.6132365353114321)
Tommy has motive: True or False?
True (0.7264255794048772)
Tommy has no motive: True or False?
False (0.6011253583932805)
Tommy has opportunity: True or False?
True (0.6370307821695329)
Tommy has no opportunity: True or False?
False (0.7394224480813394)
### Anthony
- mean: False (0.0)
- motive: False (0.44263648697812785)
- opportunity: False (0.0)

### Connor
- mean: False (0.404507447419572)
- motive: False (0.2861692906637461)
- opportunity: False (0.0)

### Skylar
- mean: False (0.0)
- motive: False (0.444564838111719)
- opportunity: False (0.5234203246639862)

### Stephen
- mean: False (0.0)
- motive: False (0.2160115191576969)
- opportunity: False (0.0)

### Tommy
- mean: True (0.821044090050916)
- motive: True (0.7264255794048772)
- opportunity: True (0.6370307821695329)

The culprit is Tommy.
In fact, it is Connor.
## 5minutemystery-the-root-of-all-evil
Bryan Durell is guilty: True or False?
True (0.884837803442546)
Bryan Durell is not guilty: True or False?
True (0.7885831565209055)
Bryan Durell has mean: True or False?
True (0.8216173667955227)
Bryan Durell has no mean: True or False?
False (0.5888891269161294)
Bryan Durell has motive: True or False?
True (0.6522414601874995)
Bryan Durell has no motive: True or False?
True (0.5204963206682631)
Bryan Durell has opportunity: True or False?
True (0.5841525779336078)
Bryan Durell has no opportunity: True or False?
False (0.5708098341193941)
Grieve Collier is guilty: True or False?
True (0.7310585348819939)
Grieve Collier is not guilty: True or False?
True (0.5841525779336078)
Grieve Collier has mean: True or False?
True (0.5973730125048408)
Grieve Collier has no mean: True or False?
False (0.7185943809170431)
Grieve Collier has motive: True or False?
True (0.5360700410935405)
Grieve Collier has no motive: True or False?
True (0.550607385906944)
Grieve Collier has opportunity: True or False?
True (0.5321819753403337)
Grieve Collier has no opportunity: True or False?
False (0.5841525779336078)
Jacques Bourbonne is guilty: True or False?
True (0.867485409735739)
Jacques Bourbonne is not guilty: True or False?
True (0.7592253761865491)
Jacques Bourbonne has mean: True or False?
True (0.811078188867804)
Jacques Bourbonne has no mean: True or False?
Map:  22%|██▏       | 45/203 [26:39<1:35:51, 36.40s/ examples]Map:  23%|██▎       | 46/203 [27:18<1:37:12, 37.15s/ examples]Map:  23%|██▎       | 47/203 [27:53<1:34:39, 36.41s/ examples]True (0.5448014304301324)
Jacques Bourbonne has motive: True or False?
True (0.7950222460539826)
Jacques Bourbonne has no motive: True or False?
True (0.5602526707659626)
Jacques Bourbonne has opportunity: True or False?
True (0.6252093370817647)
Jacques Bourbonne has no opportunity: True or False?
False (0.5165954726976894)
Ruth Majick is guilty: True or False?
True (0.8947895144283036)
Ruth Majick is not guilty: True or False?
True (0.8098781635062345)
Ruth Majick has mean: True or False?
True (0.8000678477162699)
Ruth Majick has no mean: True or False?
True (0.5869964306477841)
Ruth Majick has motive: True or False?
True (0.7962924854830264)
Ruth Majick has no motive: True or False?
True (0.6636689235052821)
Ruth Majick has opportunity: True or False?
True (0.7711548223101617)
Ruth Majick has no opportunity: True or False?
True (0.6334102859975052)
### Bryan Durell
- mean: True (0.8216173667955227)
- motive: True (0.6522414601874995)
- opportunity: True (0.5841525779336078)

### Grieve Collier
- mean: False (0.0)
- motive: False (0.449392614093056)
- opportunity: False (0.0)

### Jacques Bourbonne
- mean: False (0.4551985695698676)
- motive: False (0.43974732923403737)
- opportunity: False (0.0)

### Ruth Majick
- mean: False (0.41300356935221594)
- motive: False (0.33633107649471794)
- opportunity: False (0.36658971400249485)

The culprit is Bryan Durell.
In fact, it is Bryan Durell.
## 5minutemystery-get-the-lead-out
Benjamin Trodger is guilty: True or False?
True (0.9548162209309636)
Benjamin Trodger is not guilty: True or False?
True (0.9431384220853135)
Benjamin Trodger has mean: True or False?
True (0.8828325273478573)
Benjamin Trodger has no mean: True or False?
True (0.8140528237853677)
Benjamin Trodger has motive: True or False?
True (0.9677776702396809)
Benjamin Trodger has no motive: True or False?
True (0.9445872321654378)
Benjamin Trodger has opportunity: True or False?
True (0.9008791478232747)
Benjamin Trodger has no opportunity: True or False?
True (0.7264255794048772)
Cynthia Kirwan is guilty: True or False?
True (0.8795611817678315)
Cynthia Kirwan is not guilty: True or False?
True (0.844921525814193)
Cynthia Kirwan has mean: True or False?
True (0.794384956668203)
Cynthia Kirwan has no mean: True or False?
True (0.589834510337428)
Cynthia Kirwan has motive: True or False?
True (0.8529354946829077)
Cynthia Kirwan has no motive: True or False?
True (0.8677098176365254)
Cynthia Kirwan has opportunity: True or False?
False (0.5467381591701916)
Cynthia Kirwan has no opportunity: True or False?
False (0.6723316913929156)
Dan Skinner is guilty: True or False?
True (0.945399403620829)
Dan Skinner is not guilty: True or False?
True (0.9263037480179213)
Dan Skinner has mean: True or False?
True (0.8402589628813668)
Dan Skinner has no mean: True or False?
True (0.6352224318508648)
Dan Skinner has motive: True or False?
True (0.9428234118096998)
Dan Skinner has no motive: True or False?
True (0.911809923444246)
Dan Skinner has opportunity: True or False?
True (0.8056321690561029)
Dan Skinner has no opportunity: True or False?
True (0.6976088896786037)
Shel Jonas is guilty: True or False?
True (0.8807970862580315)
Shel Jonas is not guilty: True or False?
True (0.8365545874520802)
Shel Jonas has mean: True or False?
True (0.869271276026005)
Shel Jonas has no mean: True or False?
True (0.5117165908639297)
Shel Jonas has motive: True or False?
True (0.873646672673131)
Shel Jonas has no motive: True or False?
True (0.7911764307711107)
Shel Jonas has opportunity: True or False?
True (0.580352018589158)
Shel Jonas has no opportunity: True or False?
False (0.6859494535376744)
### Benjamin Trodger
- mean: False (0.1859471762146323)
- motive: False (0.05541276783456217)
- opportunity: False (0.2735744205951228)

### Cynthia Kirwan
- mean: False (0.41016548966257205)
- motive: False (0.13229018236347456)
- opportunity: False (0.5467381591701916)

### Dan Skinner
- mean: False (0.3647775681491352)
- motive: False (0.08819007655575395)
- opportunity: False (0.3023911103213963)

### Shel Jonas
- mean: True (0.869271276026005)
- motive: True (0.873646672673131)
- opportunity: True (0.580352018589158)

The culprit is Shel Jonas.
In fact, it is Dan Skinner.
## 5minutemystery-popping-a-wheelie
Cory is guilty: True or False?
True (0.8803863464576128)
Cory is not guilty: True or False?
True (0.8910549302065384)
Cory has mean: True or False?
True (0.924959242644946)
Cory has no mean: True or False?
True (0.7033457082786769)
Cory has motive: True or False?
True (0.9142907234091052)
Cory has no motive: True or False?
True (0.8322366416985943)
Cory has opportunity: True or False?
True (0.8283842201397164)
Cory has no opportunity: True or False?
False (0.5136684743338078)
David is guilty: True or False?
True (0.884837803442546)
David is not guilty: True or False?
True (0.9019206778000431)
David has mean: True or False?
True (0.9036349079321685)
David has no mean: True or False?
True (0.7394224480813394)
David has motive: True or False?
True (0.9563089618154458)
David has no motive: True or False?
True (0.7975568155246964)
David has opportunity: True or False?
True (0.8467044802440825)
David has no opportunity: True or False?
False (0.5698526542706361)
Mark is guilty: True or False?
True (0.8484706895507578)
Mark is not guilty: True or False?
True (0.7759445334082792)
Mark has mean: True or False?
True (0.9190632712053527)
Mark has no mean: True or False?
True (0.6592954931819778)
Mark has motive: True or False?
True (0.9481545078856665)
Mark has no motive: True or False?
True (0.6884684608108543)
Mark has opportunity: True or False?
True (0.802555560073231)
Mark has no opportunity: True or False?
False (0.6104534234357184)
String is guilty: True or False?
True (0.8247443993706964)
String is not guilty: True or False?
True (0.7997552678397243)
String has mean: True or False?
True (0.8734309071535719)
String has no mean: True or False?
True (0.5983121871760707)
String has motive: True or False?
True (0.9472835653937188)
String has no motive: True or False?
True (0.833595691674723)
String has opportunity: True or False?
True (0.8565725156795254)
String has no opportunity: True or False?
True (0.5273165068094335)
### Cory
- mean: False (0.29665429172132307)
- motive: False (0.16776335830140565)
- opportunity: False (0.0)

### David
- mean: True (0.9036349079321685)
- motive: True (0.9563089618154458)
- opportunity: True (0.8467044802440825)

### Mark
- mean: False (0.3407045068180222)
- motive: False (0.31153153918914567)
- opportunity: False (0.0)

### String
- mean: False (0.4016878128239293)
- motive: False (0.16640430832527697)
- opportunity: False (0.47268349319056646)

The culprit is David.
In fact, it is David.
## 5minutemystery-the-mystery-of-the-leprechauns-trophy
Barry is guilty: True or False?
True (0.9274947665741009)
Barry is not guilty: True or False?
True (0.9455001349615358)
Barry has mean: True or False?
True (0.7556369876990674)
Barry has no mean: True or False?
False (0.5964331434971528)
Barry has motive: True or False?
True (0.9105453462677353)
Barry has no motive: True or False?
True (0.7859664553110391)
Barry has opportunity: True or False?
True (0.875361437979977)
Barry has no opportunity: True or False?
True (0.5525396910980834)
Casey is guilty: True or False?
True (0.9019206778000431)
Casey is not guilty: True or False?
True (0.9102267057681164)
Casey has mean: True or False?
True (0.6477981763584071)
Casey has no mean: True or False?
False (0.8272706865691472)
Casey has motive: True or False?
True (0.927099763868178)
Casey has no motive: True or False?
True (0.5992506238662876)
Casey has opportunity: True or False?
True (0.8868131040663721)
Casey has no opportunity: True or False?
False (0.678326898500563)
Mr. Carswell is guilty: True or False?
True (0.8677098176365254)
Mr. Carswell is not guilty: True or False?
True (0.7859664553110391)
Mr. Carswell has mean: True or False?
True (0.7225270177274575)
Mr. Carswell has no mean: True or False?
False (0.6095241816115718)
Mr. Carswell has motive: True or False?
True (0.7826624547920057)
Mr. Carswell has no motive: True or False?
True (0.6984322578436808)
Map:  24%|██▎       | 48/203 [28:29<1:33:28, 36.18s/ examples]Map:  24%|██▍       | 49/203 [29:04<1:32:15, 35.95s/ examples]Map:  25%|██▍       | 50/203 [29:31<1:25:01, 33.34s/ examples]Mr. Carswell has opportunity: True or False?
True (0.6451199006197486)
Mr. Carswell has no opportunity: True or False?
False (0.6039318499573872)
Tony is guilty: True or False?
True (0.7994423454932595)
Tony is not guilty: True or False?
True (0.811377348522662)
Tony has mean: True or False?
False (0.6619228707202935)
Tony has no mean: True or False?
False (0.881410902208909)
Tony has motive: True or False?
True (0.7862948177096581)
Tony has no motive: True or False?
False (0.525368812147771)
Tony has opportunity: True or False?
True (0.5506073202694327)
Tony has no opportunity: True or False?
False (0.6504672743423094)
### Barry
- mean: False (0.0)
- motive: False (0.21403354468896085)
- opportunity: False (0.44746030890191657)

### Casey
- mean: True (0.6477981763584071)
- motive: True (0.927099763868178)
- opportunity: True (0.8868131040663721)

### Mr. Carswell
- mean: False (0.0)
- motive: False (0.3015677421563192)
- opportunity: False (0.0)

### Tony
- mean: False (0.6619228707202935)
- motive: False (0.0)
- opportunity: False (0.0)

The culprit is Casey.
In fact, it is Tony.
## 5minutemystery-the-mysterious-chicken
Ed is guilty: True or False?
True (0.8294919722593475)
Ed is not guilty: True or False?
True (0.8883720049821552)
Ed has mean: True or False?
True (0.8656789607733094)
Ed has no mean: True or False?
True (0.6566582306092376)
Ed has motive: True or False?
True (0.9629528509146777)
Ed has no motive: True or False?
True (0.8710367026584496)
Ed has opportunity: True or False?
True (0.8349459127213729)
Ed has no opportunity: True or False?
True (0.6540113633452196)
Ed's mother is guilty: True or False?
True (0.7759445334082792)
Ed's mother is not guilty: True or False?
True (0.8727816933272936)
Ed's mother has mean: True or False?
False (0.503906199448032)
Ed's mother has no mean: True or False?
True (0.5717666110200305)
Ed's mother has motive: True or False?
True (0.9196425103002197)
Ed's mother has no motive: True or False?
True (0.7697732451157533)
Ed's mother has opportunity: True or False?
True (0.6757646168022439)
Ed's mother has no opportunity: True or False?
False (0.6783269591477166)
Ed’s Husky is guilty: True or False?
True (0.8873999116020591)
Ed’s Husky is not guilty: True or False?
True (0.862930180750016)
Ed’s Husky has mean: True or False?
True (0.842345065078002)
Ed’s Husky has no mean: True or False?
True (0.7178038242127955)
Ed’s Husky has motive: True or False?
True (0.9289262900494157)
Ed’s Husky has no motive: True or False?
True (0.91321325132378)
Ed’s Husky has opportunity: True or False?
True (0.8652240590801695)
Ed’s Husky has no opportunity: True or False?
True (0.769080279275001)
Zeke is guilty: True or False?
True (0.9187722208906307)
Zeke is not guilty: True or False?
True (0.9284088027271398)
Zeke has mean: True or False?
True (0.875361437979977)
Zeke has no mean: True or False?
True (0.7025300310583819)
Zeke has motive: True or False?
True (0.9529258022651363)
Zeke has no motive: True or False?
True (0.8852351930010195)
Zeke has opportunity: True or False?
True (0.9113376724203427)
Zeke has no opportunity: True or False?
True (0.7287482572006113)
### Ed
- mean: False (0.34334176939076244)
- motive: False (0.12896329734155043)
- opportunity: False (0.3459886366547804)

### Ed's mother
- mean: True (0.0)
- motive: True (0.9196425103002197)
- opportunity: True (0.6757646168022439)

### Ed’s Husky
- mean: False (0.28219617578720446)
- motive: False (0.08678674867622005)
- opportunity: False (0.230919720724999)

### Zeke
- mean: False (0.29746996894161815)
- motive: False (0.1147648069989805)
- opportunity: False (0.2712517427993887)

The culprit is Ed's mother.
In fact, it is Ed.
## 5minutemystery-the-late-night-horror-show
Andrew is guilty: True or False?
False (0.6020615685826383)
Andrew is not guilty: True or False?
True (0.5097643762740132)
Andrew has mean: True or False?
True (0.5243946792389143)
Andrew has no mean: True or False?
False (0.7505527730327083)
Andrew has motive: True or False?
True (0.7446563307563252)
Andrew has no motive: True or False?
False (0.6306849143569856)
Andrew has opportunity: True or False?
False (0.5486734987923966)
Andrew has no opportunity: True or False?
False (0.8933094122075369)
David is guilty: True or False?
True (0.5736784476125245)
David is not guilty: True or False?
True (0.7074046739492601)
David has mean: True or False?
True (0.7599387683150569)
David has no mean: True or False?
False (0.5117165908639297)
David has motive: True or False?
True (0.8891444205417208)
David has no motive: True or False?
True (0.646013666311734)
David has opportunity: True or False?
True (0.8454326959560526)
David has no opportunity: True or False?
True (0.5727227727404994)
Dennis is guilty: True or False?
True (0.5312093941731293)
Dennis is not guilty: True or False?
True (0.6469064338453809)
Dennis has mean: True or False?
True (0.7033457711626864)
Dennis has no mean: True or False?
False (0.5983121871760707)
Dennis has motive: True or False?
True (0.6766198919456847)
Dennis has no motive: True or False?
True (0.6460137433225688)
Dennis has opportunity: True or False?
True (0.7041600870830834)
Dennis has no opportunity: True or False?
False (0.5097643762740132)
Matthew is guilty: True or False?
True (0.5370414382302919)
Matthew is not guilty: True or False?
True (0.7033457711626864)
Matthew has mean: True or False?
True (0.8013146490010521)
Matthew has no mean: True or False?
False (0.5563995964631269)
Matthew has motive: True or False?
True (0.8519527857346616)
Matthew has no motive: True or False?
True (0.6095241816115718)
Matthew has opportunity: True or False?
True (0.833324548637899)
Matthew has no opportunity: True or False?
True (0.5185461538431656)
### Andrew
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.5486734987923966)

### David
- mean: False (0.0)
- motive: False (0.35398633368826604)
- opportunity: False (0.42727722725950057)

### Dennis
- mean: True (0.7033457711626864)
- motive: True (0.6766198919456847)
- opportunity: True (0.7041600870830834)

### Matthew
- mean: False (0.0)
- motive: False (0.39047581838842815)
- opportunity: False (0.4814538461568344)

The culprit is Dennis.
In fact, it is David.
## 5minutemystery-making-partner
Dan Cartman is guilty: True or False?
True (0.7985012549449481)
Dan Cartman is not guilty: True or False?
True (0.811974341286875)
Dan Cartman has mean: True or False?
True (0.9049869771631355)
Dan Cartman has no mean: True or False?
True (0.7620701143808404)
Dan Cartman has motive: True or False?
True (0.8255897087847518)
Dan Cartman has no motive: True or False?
True (0.7302898714065358)
Dan Cartman has opportunity: True or False?
True (0.7756047866813147)
Dan Cartman has no opportunity: True or False?
False (0.5755879969637064)
Jill is guilty: True or False?
False (0.5292633777076584)
Jill is not guilty: True or False?
True (0.6099324002798076)
Jill has mean: True or False?
True (0.8546421464778325)
Jill has no mean: True or False?
True (0.6513548405484016)
Jill has motive: True or False?
True (0.7221353097845661)
Jill has no motive: True or False?
False (0.5491570693307823)
Jill has opportunity: True or False?
False (0.5525396910980834)
Jill has no opportunity: True or False?
False (0.8755743533923891)
Mike Creighton is guilty: True or False?
True (0.71582149676272)
Mike Creighton is not guilty: True or False?
True (0.7450275926376607)
Mike Creighton has mean: True or False?
True (0.6909763109505791)
Mike Creighton has no mean: True or False?
True (0.6834194581047349)
Mike Creighton has motive: True or False?
True (0.5893619100975267)
Mike Creighton has no motive: True or False?
True (0.7802654492179112)
Mike Creighton has opportunity: True or False?
True (0.5302364729224919)
Mike Creighton has no opportunity: True or False?
False (0.785637679813794)
Mrs. Krantz is guilty: True or False?
True (0.7829945121976718)
Mrs. Krantz is not guilty: True or False?
True (0.766293592214635)
Mrs. Krantz has mean: True or False?
True (0.7836574849371717)
Mrs. Krantz has no mean: True or False?
True (0.6584175136252488)
Mrs. Krantz has motive: True or False?
True (0.7154240000492645)
Map:  25%|██▌       | 51/203 [30:18<1:34:50, 37.44s/ examples]Map:  26%|██▌       | 52/203 [30:55<1:33:40, 37.22s/ examples]Map:  26%|██▌       | 53/203 [31:34<1:34:15, 37.70s/ examples]Mrs. Krantz has no motive: True or False?
True (0.6562178198679722)
Mrs. Krantz has opportunity: True or False?
True (0.6817267588564826)
Mrs. Krantz has no opportunity: True or False?
False (0.8155265480299457)
### Dan Cartman
- mean: False (0.23792988561915962)
- motive: False (0.2697101285934642)
- opportunity: False (0.0)

### Jill
- mean: False (0.34864515945159835)
- motive: False (0.0)
- opportunity: False (0.5525396910980834)

### Mike Creighton
- mean: False (0.3165805418952651)
- motive: False (0.2197345507820888)
- opportunity: False (0.0)

### Mrs. Krantz
- mean: True (0.7836574849371717)
- motive: True (0.7154240000492645)
- opportunity: True (0.6817267588564826)

The culprit is Mrs. Krantz.
In fact, it is Mike Creighton.
## 5minutemystery-no-retreat-from-death
Amanda Kent is guilty: True or False?
False (0.5185462156586879)
Amanda Kent is not guilty: True or False?
True (0.5841525082971981)
Amanda Kent has mean: True or False?
True (0.8376200175313318)
Amanda Kent has no mean: True or False?
False (0.7468781552484828)
Amanda Kent has motive: True or False?
True (0.5350984235603058)
Amanda Kent has no motive: True or False?
False (0.5448013654847448)
Amanda Kent has opportunity: True or False?
False (0.6288633913849659)
Amanda Kent has no opportunity: True or False?
False (0.7627776774954688)
Craig Willis is guilty: True or False?
True (0.7272012283179254)
Craig Willis is not guilty: True or False?
True (0.7476159279883341)
Craig Willis has mean: True or False?
True (0.8499711693725173)
Craig Willis has no mean: True or False?
False (0.6288633913849659)
Craig Willis has motive: True or False?
True (0.6774740084332073)
Craig Willis has no motive: True or False?
True (0.5535053004623279)
Craig Willis has opportunity: True or False?
True (0.5869964306477841)
Craig Willis has no opportunity: True or False?
False (0.6477981763584071)
Niles Anderson is guilty: True or False?
True (0.6315943123389512)
Niles Anderson is not guilty: True or False?
True (0.6808786440630326)
Niles Anderson has mean: True or False?
True (0.7937461674149602)
Niles Anderson has no mean: True or False?
False (0.6791787167336184)
Niles Anderson has motive: True or False?
True (0.6224593484250324)
Niles Anderson has no motive: True or False?
False (0.5467381591701916)
Niles Anderson has opportunity: True or False?
False (0.5136684743338078)
Niles Anderson has no opportunity: True or False?
False (0.6575384693006662)
Stephanie Clark is guilty: True or False?
False (0.5583269696343842)
Stephanie Clark is not guilty: True or False?
True (0.51464427676968)
Stephanie Clark has mean: True or False?
True (0.5992506238662876)
Stephanie Clark has no mean: True or False?
False (0.832781310996106)
Stephanie Clark has motive: True or False?
False (0.6076631662366868)
Stephanie Clark has no motive: True or False?
False (0.6187804294217345)
Stephanie Clark has opportunity: True or False?
False (0.8122724274380432)
Stephanie Clark has no opportunity: True or False?
False (0.8438950825214144)
### Amanda Kent
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.6288633913849659)

### Craig Willis
- mean: True (0.8499711693725173)
- motive: True (0.6774740084332073)
- opportunity: True (0.5869964306477841)

### Niles Anderson
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.5136684743338078)

### Stephanie Clark
- mean: False (0.0)
- motive: False (0.6076631662366868)
- opportunity: False (0.8122724274380432)

The culprit is Craig Willis.
In fact, it is Niles Anderson.
## 5minutemystery-a-monster-of-a-mystery
Donald is guilty: True or False?
True (0.8044059309478723)
Donald is not guilty: True or False?
True (0.8378854414608077)
Donald has mean: True or False?
True (0.8762112821835625)
Donald has no mean: True or False?
True (0.5496406401666291)
Donald has motive: True or False?
True (0.8764230069135861)
Donald has no motive: True or False?
False (0.5321819753403337)
Donald has opportunity: True or False?
True (0.705785027818136)
Donald has no opportunity: True or False?
False (0.745398395394548)
Linda is guilty: True or False?
True (0.7431679939957333)
Linda is not guilty: True or False?
True (0.7732163648437078)
Linda has mean: True or False?
True (0.9102267057681164)
Linda has no mean: True or False?
True (0.5043944168862934)
Linda has motive: True or False?
True (0.8770562402180104)
Linda has no motive: True or False?
False (0.5836780245455975)
Linda has opportunity: True or False?
True (0.6274948163226559)
Linda has no opportunity: True or False?
False (0.814643384779728)
Randy is guilty: True or False?
True (0.6884683992569801)
Randy is not guilty: True or False?
True (0.7193836000532381)
Randy has mean: True or False?
True (0.9268353022276509)
Randy has no mean: True or False?
True (0.5964331079469681)
Randy has motive: True or False?
True (0.9403530352223053)
Randy has no motive: True or False?
False (0.5515736950589613)
Randy has opportunity: True or False?
True (0.8022458575739914)
Randy has no opportunity: True or False?
False (0.7170118721569225)
Wendell is guilty: True or False?
True (0.5156199352405011)
Wendell is not guilty: True or False?
False (0.5515736950589613)
Wendell has mean: True or False?
True (0.7859664553110391)
Wendell has no mean: True or False?
False (0.6113820047705449)
Wendell has motive: True or False?
True (0.6901415551283886)
Wendell has no motive: True or False?
False (0.7333564224770464)
Wendell has opportunity: True or False?
False (0.5292634408007735)
Wendell has no opportunity: True or False?
False (0.8683809699466569)
### Donald
- mean: False (0.45035935983337094)
- motive: False (0.0)
- opportunity: False (0.0)

### Linda
- mean: False (0.4956055831137066)
- motive: False (0.0)
- opportunity: False (0.0)

### Randy
- mean: True (0.9268353022276509)
- motive: True (0.9403530352223053)
- opportunity: True (0.8022458575739914)

### Wendell
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.5292634408007735)

The culprit is Randy.
In fact, it is Linda.
## 5minutemystery-chow-baby
Beryl Hives is guilty: True or False?
False (0.5204963827162634)
Beryl Hives is not guilty: True or False?
False (0.6224593484250324)
Beryl Hives has mean: True or False?
True (0.6976088896786037)
Beryl Hives has no mean: True or False?
False (0.702530072932436)
Beryl Hives has motive: True or False?
True (0.6988435356735703)
Beryl Hives has no motive: True or False?
False (0.5563995964631269)
Beryl Hives has opportunity: True or False?
False (0.6261242000979097)
Beryl Hives has no opportunity: True or False?
False (0.8116760258690822)
Dawn de Jong is guilty: True or False?
True (0.5331543669186894)
Dawn de Jong is not guilty: True or False?
False (0.5292634408007735)
Dawn de Jong has mean: True or False?
True (0.5321819753403337)
Dawn de Jong has no mean: True or False?
False (0.7853085971692302)
Dawn de Jong has motive: True or False?
True (0.5568816117266226)
Dawn de Jong has no motive: True or False?
False (0.7570766705324253)
Dawn de Jong has opportunity: True or False?
False (0.7272012283179254)
Dawn de Jong has no opportunity: True or False?
False (0.9277570247163465)
Konrad Pushkin is guilty: True or False?
True (0.7178038242127955)
Konrad Pushkin is not guilty: True or False?
True (0.6270381219830087)
Konrad Pushkin has mean: True or False?
True (0.5078118305218892)
Konrad Pushkin has no mean: True or False?
False (0.7905303264811482)
Konrad Pushkin has motive: True or False?
True (0.7352616086060775)
Konrad Pushkin has no motive: True or False?
False (0.6095241271158658)
Konrad Pushkin has opportunity: True or False?
False (0.5888891269161294)
Konrad Pushkin has no opportunity: True or False?
False (0.8719117627136385)
Pete Stampkowski is guilty: True or False?
True (0.7170118721569225)
Pete Stampkowski is not guilty: True or False?
True (0.6155501549781407)
Pete Stampkowski has mean: True or False?
True (0.6893056096647525)
Pete Stampkowski has no mean: True or False?
False (0.705785027818136)
Pete Stampkowski has motive: True or False?
True (0.8207569718385453)
Pete Stampkowski has no motive: True or False?
True (0.5097643762740132)
Pete Stampkowski has opportunity: True or False?
True (0.5156199352405011)Map:  27%|██▋       | 54/203 [32:15<1:36:31, 38.87s/ examples]Map:  27%|██▋       | 55/203 [33:09<1:46:30, 43.18s/ examples]Map:  28%|██▊       | 56/203 [33:58<1:50:16, 45.01s/ examples]
Pete Stampkowski has no opportunity: True or False?
False (0.824179109557089)
### Beryl Hives
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.6261242000979097)

### Dawn de Jong
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.7272012283179254)

### Konrad Pushkin
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.5888891269161294)

### Pete Stampkowski
- mean: True (0.6893056096647525)
- motive: True (0.8207569718385453)
- opportunity: True (0.5156199352405011)

The culprit is Pete Stampkowski.
In fact, it is Beryl Hives.
## 5minutemystery-the-mystery-of-the-frowning-clown
Bumbo is guilty: True or False?
True (0.6992544513448877)
Bumbo is not guilty: True or False?
True (0.7559974119430289)
Bumbo has mean: True or False?
True (0.8193157317863493)
Bumbo has no mean: True or False?
True (0.7549149897594328)
Bumbo has motive: True or False?
True (0.8883720049821552)
Bumbo has no motive: True or False?
True (0.708212608228071)
Bumbo has opportunity: True or False?
True (0.7721872989468889)
Bumbo has no opportunity: True or False?
False (0.5243946792389143)
Dusty is guilty: True or False?
True (0.7859664553110391)
Dusty is not guilty: True or False?
True (0.842345065078002)
Dusty has mean: True or False?
True (0.7924642605907138)
Dusty has no mean: True or False?
True (0.7563575572780217)
Dusty has motive: True or False?
True (0.8940517282497483)
Dusty has no motive: True or False?
True (0.5506073202694327)
Dusty has opportunity: True or False?
True (0.8104789202520752)
Dusty has no opportunity: True or False?
False (0.6901416168318547)
Mr. Green is guilty: True or False?
True (0.8428632044363634)
Mr. Green is not guilty: True or False?
True (0.7843190438750585)
Mr. Green has mean: True or False?
True (0.9081302297583123)
Mr. Green has no mean: True or False?
True (0.8261514357843124)
Mr. Green has motive: True or False?
True (0.9312751898083738)
Mr. Green has no motive: True or False?
True (0.8095772283237919)
Mr. Green has opportunity: True or False?
True (0.8040984260198152)
Mr. Green has no opportunity: True or False?
True (0.5263427467960875)
Stage Manager is guilty: True or False?
True (0.7627776774954688)
Stage Manager is not guilty: True or False?
True (0.7045668426043505)
Stage Manager has mean: True or False?
True (0.8454326455643386)
Stage Manager has no mean: True or False?
True (0.6343168082332088)
Stage Manager has motive: True or False?
True (0.8050197941712954)
Stage Manager has no motive: True or False?
True (0.6206216296838327)
Stage Manager has opportunity: True or False?
True (0.7364006034245382)
Stage Manager has no opportunity: True or False?
False (0.6893056096647525)
### Bumbo
- mean: False (0.24508501024056717)
- motive: False (0.29178739177192903)
- opportunity: False (0.0)

### Dusty
- mean: True (0.7924642605907138)
- motive: True (0.8940517282497483)
- opportunity: True (0.8104789202520752)

### Mr. Green
- mean: False (0.17384856421568762)
- motive: False (0.19042277167620814)
- opportunity: False (0.4736572532039125)

### Stage Manager
- mean: False (0.3656831917667912)
- motive: False (0.3793783703161673)
- opportunity: False (0.0)

The culprit is Dusty.
In fact, it is Stage Manager.
## 5minutemystery-the-strangest-sport-of-all
Ernie is guilty: True or False?
True (0.9246877442701001)
Ernie is not guilty: True or False?
True (0.9216402157401415)
Ernie has mean: True or False?
True (0.8951566249612815)
Ernie has no mean: True or False?
True (0.8757870204368676)
Ernie has motive: True or False?
True (0.9322068701708559)
Ernie has no motive: True or False?
True (0.8227594449669557)
Ernie has opportunity: True or False?
True (0.9012274173198201)
Ernie has no opportunity: True or False?
False (0.5048826258478675)
Gordon is guilty: True or False?
True (0.9481545078856665)
Gordon is not guilty: True or False?
True (0.9394706502722077)
Gordon has mean: True or False?
True (0.9233161821369215)
Gordon has no mean: True or False?
True (0.9086179121100144)
Gordon has motive: True or False?
True (0.9733929040540585)
Gordon has no motive: True or False?
True (0.9362850185952675)
Gordon has opportunity: True or False?
True (0.9324532728823121)
Gordon has no opportunity: True or False?
True (0.642432441257838)
Jesse is guilty: True or False?
True (0.9335520893498362)
Jesse is not guilty: True or False?
True (0.935346481802689)
Jesse has mean: True or False?
True (0.869271276026005)
Jesse has no mean: True or False?
True (0.8868131040663721)
Jesse has motive: True or False?
True (0.9210741501882456)
Jesse has no motive: True or False?
True (0.8902942539348153)
Jesse has opportunity: True or False?
True (0.8929365260632085)
Jesse has no opportunity: True or False?
True (0.5185461538431656)
Mac is guilty: True or False?
True (0.9677167542009312)
Mac is not guilty: True or False?
True (0.9575167905174621)
Mac has mean: True or False?
True (0.8951566849862127)
Mac has no mean: True or False?
True (0.7505527730327083)
Mac has motive: True or False?
True (0.9529258022651363)
Mac has no motive: True or False?
True (0.9422947179693436)
Mac has opportunity: True or False?
True (0.8933094122075369)
Mac has no opportunity: True or False?
True (0.7154240000492645)
### Ernie
- mean: True (0.8951566249612815)
- motive: True (0.9322068701708559)
- opportunity: True (0.9012274173198201)

### Gordon
- mean: False (0.09138208788998559)
- motive: False (0.06371498140473253)
- opportunity: False (0.35756755874216195)

### Jesse
- mean: False (0.11318689593362785)
- motive: False (0.10970574606518468)
- opportunity: False (0.4814538461568344)

### Mac
- mean: False (0.2494472269672917)
- motive: False (0.05770528203065639)
- opportunity: False (0.28457599995073546)

The culprit is Ernie.
In fact, it is Jesse.
## 5minutemystery-who-stole-storimons-wallet
Danny is guilty: True or False?
True (0.8875949368741688)
Danny is not guilty: True or False?
True (0.9259027265283752)
Danny has mean: True or False?
True (0.8998277786460391)
Danny has no mean: True or False?
True (0.8459424357871997)
Danny has motive: True or False?
True (0.9314625284362855)
Danny has no motive: True or False?
True (0.6224592927728324)
Danny has opportunity: True or False?
True (0.8349459127213729)
Danny has no opportunity: True or False?
False (0.6242935037467142)
Mick is guilty: True or False?
True (0.7634837587244478)
Mick is not guilty: True or False?
True (0.784649255215384)
Mick has mean: True or False?
True (0.9284088027271398)
Mick has no mean: True or False?
True (0.7853085971692302)
Mick has motive: True or False?
True (0.8244619332958376)
Mick has no motive: True or False?
False (0.6039318499573872)
Mick has opportunity: True or False?
True (0.8047130138702729)
Mick has no opportunity: True or False?
False (0.7690802105138688)
Mr. Storimon is guilty: True or False?
True (0.9177460685312047)
Mr. Storimon is not guilty: True or False?
True (0.873646672673131)
Mr. Storimon has mean: True or False?
True (0.9001793304600783)
Mr. Storimon has no mean: True or False?
True (0.7563574896543893)
Mr. Storimon has motive: True or False?
True (0.9174506641307638)
Mr. Storimon has no motive: True or False?
True (0.7333564224770464)
Mr. Storimon has opportunity: True or False?
True (0.81197440178368)
Mr. Storimon has no opportunity: True or False?
False (0.5078118910577802)
Policeman is guilty: True or False?
True (0.7641883982873323)
Policeman is not guilty: True or False?
True (0.6334102859975052)
Policeman has mean: True or False?
True (0.7498207054286419)
Policeman has no mean: True or False?
False (0.5822535180679596)
Policeman has motive: True or False?
True (0.8333246107254184)
Policeman has no motive: True or False?
True (0.6419837397014914)
Policeman has opportunity: True or False?
True (0.6996649413792725)
Policeman has no opportunity: True or False?
False (0.733738122727274)
### Danny
- mean: False (0.15405756421280026)
- motive: False (0.3775407072271676)
- opportunity: False (0.0)

### Mick
- mean: True (0.9284088027271398)
- motive: True (0.8244619332958376)
- opportunity: True (0.8047130138702729)

### Mr. Storimon
- mean: False (0.24364251034561069)
- motive: False (0.26664357752295365)
- opportunity: False (0.0)

Map:  28%|██▊       | 57/203 [34:47<1:52:32, 46.25s/ examples]Map:  29%|██▊       | 58/203 [35:36<1:53:30, 46.97s/ examples]Map:  29%|██▉       | 59/203 [36:08<1:42:11, 42.58s/ examples]### Policeman
- mean: False (0.0)
- motive: False (0.35801626029850864)
- opportunity: False (0.0)

The culprit is Mick.
In fact, it is Mr. Storimon.
## 5minutemystery-miles-archer-solves-a-case
Arnold Grossmecker is guilty: True or False?
True (0.8519527857346616)
Arnold Grossmecker is not guilty: True or False?
True (0.7879312564609259)
Arnold Grossmecker has mean: True or False?
True (0.8407825844829613)
Arnold Grossmecker has no mean: True or False?
True (0.5926666351772785)
Arnold Grossmecker has motive: True or False?
True (0.8591918406281239)
Arnold Grossmecker has no motive: True or False?
True (0.6424325178417575)
Arnold Grossmecker has opportunity: True or False?
True (0.6825737331070684)
Arnold Grossmecker has no opportunity: True or False?
False (0.7017130830397807)
Brigid Jellicoe is guilty: True or False?
True (0.8929365260632085)
Brigid Jellicoe is not guilty: True or False?
True (0.8778961263000082)
Brigid Jellicoe has mean: True or False?
True (0.905989824801558)
Brigid Jellicoe has no mean: True or False?
True (0.7356416038392981)
Brigid Jellicoe has motive: True or False?
True (0.8428631416381634)
Brigid Jellicoe has no motive: True or False?
True (0.7065955344877805)
Brigid Jellicoe has opportunity: True or False?
True (0.7962924854830264)
Brigid Jellicoe has no opportunity: True or False?
False (0.5107405249783342)
Quinton Jesselton is guilty: True or False?
True (0.8751481831208795)
Quinton Jesselton is not guilty: True or False?
True (0.8294920340613177)
Quinton Jesselton has mean: True or False?
True (0.911809923444246)
Quinton Jesselton has no mean: True or False?
True (0.7911764307711107)
Quinton Jesselton has motive: True or False?
True (0.8762112821835625)
Quinton Jesselton has no motive: True or False?
True (0.6011253583932805)
Quinton Jesselton has opportunity: True or False?
True (0.7240905804783984)
Quinton Jesselton has no opportunity: True or False?
True (0.5525396910980834)
Sandra O’Malley is guilty: True or False?
True (0.8062431836477579)
Sandra O’Malley is not guilty: True or False?
True (0.8278281049441929)
Sandra O’Malley has mean: True or False?
True (0.9337940192482527)
Sandra O’Malley has no mean: True or False?
True (0.8158201638039532)
Sandra O’Malley has motive: True or False?
True (0.8000678954040312)
Sandra O’Malley has no motive: True or False?
True (0.7669924589170153)
Sandra O’Malley has opportunity: True or False?
True (0.6557770400181139)
Sandra O’Malley has no opportunity: True or False?
True (0.5214711377329961)
### Arnold Grossmecker
- mean: True (0.8407825844829613)
- motive: True (0.8591918406281239)
- opportunity: True (0.6825737331070684)

### Brigid Jellicoe
- mean: False (0.2643583961607019)
- motive: False (0.29340446551221955)
- opportunity: False (0.0)

### Quinton Jesselton
- mean: False (0.20882356922888934)
- motive: False (0.3988746416067195)
- opportunity: False (0.44746030890191657)

### Sandra O’Malley
- mean: False (0.18417983619604683)
- motive: False (0.23300754108298471)
- opportunity: False (0.47852886226700386)

The culprit is Arnold Grossmecker.
In fact, it is Quinton Jesselton.
## 5minutemystery-murder-in-the-early-morning
Constance is guilty: True or False?
True (0.8107787408238168)
Constance is not guilty: True or False?
True (0.8098781635062345)
Constance has mean: True or False?
True (0.9319595674053855)
Constance has no mean: True or False?
True (0.5765419579552815)
Constance has motive: True or False?
True (0.7669925046333297)
Constance has no motive: True or False?
True (0.8397339530959691)
Constance has opportunity: True or False?
True (0.8338664756137771)
Constance has no opportunity: True or False?
False (0.5841525779336078)
John is guilty: True or False?
True (0.6522414018725713)
John is not guilty: True or False?
True (0.7225270177274575)
John has mean: True or False?
True (0.8305941261447712)
John has no mean: True or False?
False (0.6169357925086439)
John has motive: True or False?
True (0.6662796746479285)
John has no motive: True or False?
True (0.7570767382203575)
John has opportunity: True or False?
True (0.7962924854830264)
John has no opportunity: True or False?
False (0.5592900581575188)
Nancy is guilty: True or False?
True (0.6206215556999736)
Nancy is not guilty: True or False?
True (0.6825737331070684)
Nancy has mean: True or False?
True (0.7356416038392981)
Nancy has no mean: True or False?
False (0.5813030995752883)
Nancy has motive: True or False?
True (0.6800292740030767)
Nancy has no motive: True or False?
True (0.7527403228571042)
Nancy has opportunity: True or False?
True (0.6680145240815963)
Nancy has no opportunity: True or False?
True (0.5331543669186894)
Vernon is guilty: True or False?
True (0.8241790481509624)
Vernon is not guilty: True or False?
True (0.7911763836133219)
Vernon has mean: True or False?
True (0.8951566249612815)
Vernon has no mean: True or False?
False (0.6001883144765984)
Vernon has motive: True or False?
True (0.705785027818136)
Vernon has no motive: True or False?
True (0.7563575572780217)
Vernon has opportunity: True or False?
True (0.802555560073231)
Vernon has no opportunity: True or False?
False (0.6029970803636248)
### Constance
- mean: False (0.4234580420447185)
- motive: False (0.1602660469040309)
- opportunity: False (0.0)

### John
- mean: False (0.0)
- motive: False (0.24292326177964252)
- opportunity: False (0.0)

### Nancy
- mean: False (0.0)
- motive: False (0.24725967714289576)
- opportunity: False (0.46684563308131055)

### Vernon
- mean: True (0.8951566249612815)
- motive: True (0.705785027818136)
- opportunity: True (0.802555560073231)

The culprit is Vernon.
In fact, it is Vernon.
## 5minutemystery-raiding-cane
Brent Pearson is guilty: True or False?
False (0.5535053004623279)
Brent Pearson is not guilty: True or False?
False (0.7813306496768853)
Brent Pearson has mean: True or False?
True (0.5399537807786099)
Brent Pearson has no mean: True or False?
False (0.8013146490010521)
Brent Pearson has motive: True or False?
False (0.5784481782924303)
Brent Pearson has no motive: True or False?
False (0.7988152492192591)
Brent Pearson has opportunity: True or False?
False (0.8591917766133458)
Brent Pearson has no opportunity: True or False?
False (0.9216401608061056)
Frank Weiss is guilty: True or False?
True (0.8679338697256817)
Frank Weiss is not guilty: True or False?
True (0.5746334908651781)
Frank Weiss has mean: True or False?
True (0.8606036289596553)
Frank Weiss has no mean: True or False?
True (0.6477981763584071)
Frank Weiss has motive: True or False?
True (0.8659058819563623)
Frank Weiss has no motive: True or False?
False (0.5669777909748143)
Frank Weiss has opportunity: True or False?
True (0.5640984675176304)
Frank Weiss has no opportunity: True or False?
False (0.8428631416381634)
Michael Weiss is guilty: True or False?
True (0.6976089520497016)
Michael Weiss is not guilty: True or False?
False (0.6451199006197486)
Michael Weiss has mean: True or False?
True (0.8732148436000907)
Michael Weiss has no mean: True or False?
False (0.5774953314585229)
Michael Weiss has motive: True or False?
True (0.6992543888266708)
Michael Weiss has no motive: True or False?
False (0.6749080895533367)
Michael Weiss has opportunity: True or False?
False (0.6495786332146115)
Michael Weiss has no opportunity: True or False?
False (0.8665847814067802)
Ronald Weiss is guilty: True or False?
True (0.6325027218909103)
Ronald Weiss is not guilty: True or False?
False (0.6397360437814448)
Ronald Weiss has mean: True or False?
True (0.8723474190177988)
Ronald Weiss has no mean: True or False?
True (0.5640984675176304)
Ronald Weiss has motive: True or False?
True (0.6680145240815963)
Ronald Weiss has no motive: True or False?
False (0.7074046739492601)
Ronald Weiss has opportunity: True or False?
False (0.6513548405484016)
Ronald Weiss has no opportunity: True or False?
False (0.9193533657123177)
### Brent Pearson
- mean: False (0.0)
- motive: False (0.5784481782924303)
- opportunity: False (0.8591917766133458)

### Frank Weiss
- mean: True (0.8606036289596553)
- motive: True (0.8659058819563623)
- opportunity: True (0.5640984675176304)

### Michael Weiss
- mean: False (0.0)
Map:  30%|██▉       | 60/203 [36:43<1:35:51, 40.22s/ examples]Map:  30%|███       | 61/203 [37:30<1:40:11, 42.33s/ examples]Map:  31%|███       | 62/203 [38:19<1:44:03, 44.28s/ examples]- motive: False (0.0)
- opportunity: False (0.6495786332146115)

### Ronald Weiss
- mean: False (0.4359015324823696)
- motive: False (0.0)
- opportunity: False (0.6513548405484016)

The culprit is Frank Weiss.
In fact, it is Frank Weiss.
## 5minutemystery-the-missing-dagger
Chris Palmer is guilty: True or False?
True (0.9167081124681512)
Chris Palmer is not guilty: True or False?
True (0.8807970862580315)
Chris Palmer has mean: True or False?
True (0.8656789607733094)
Chris Palmer has no mean: True or False?
True (0.6370308391245257)
Chris Palmer has motive: True or False?
True (0.9376689781587124)
Chris Palmer has no motive: True or False?
True (0.8370879250561812)
Chris Palmer has opportunity: True or False?
True (0.7898827135821628)
Chris Palmer has no opportunity: True or False?
True (0.5156199352405011)
Matthew Light is guilty: True or False?
True (0.8534247816107388)
Matthew Light is not guilty: True or False?
True (0.8360198082076468)
Matthew Light has mean: True or False?
True (0.7745833916423246)
Matthew Light has no mean: True or False?
True (0.7453983509653428)
Matthew Light has motive: True or False?
True (0.920217993899809)
Matthew Light has no motive: True or False?
True (0.797556874947312)
Matthew Light has opportunity: True or False?
True (0.8454326455643386)
Matthew Light has no opportunity: True or False?
True (0.6783269591477166)
Mitchell Land is guilty: True or False?
True (0.9012274173198201)
Mitchell Land is not guilty: True or False?
True (0.8899121304559661)
Mitchell Land has mean: True or False?
True (0.8524448242555318)
Mitchell Land has no mean: True or False?
True (0.5698526542706361)
Mitchell Land has motive: True or False?
True (0.9631613481972502)
Mitchell Land has no motive: True or False?
True (0.7563575572780217)
Mitchell Land has opportunity: True or False?
True (0.708212608228071)
Mitchell Land has no opportunity: True or False?
False (0.589834510337428)
Paul Benham is guilty: True or False?
True (0.8727816933272936)
Paul Benham is not guilty: True or False?
True (0.8193157928301305)
Paul Benham has mean: True or False?
True (0.726425644352388)
Paul Benham has no mean: True or False?
False (0.5409238326546766)
Paul Benham has motive: True or False?
True (0.873646620599733)
Paul Benham has no motive: True or False?
True (0.6909763109505791)
Paul Benham has opportunity: True or False?
True (0.6918097672776748)
Paul Benham has no opportunity: True or False?
False (0.6048658333578858)
Russell Smith is guilty: True or False?
True (0.7648916137833577)
Russell Smith is not guilty: True or False?
True (0.7416740115009234)
Russell Smith has mean: True or False?
True (0.8244619332958376)
Russell Smith has no mean: True or False?
True (0.7364006034245382)
Russell Smith has motive: True or False?
True (0.869271276026005)
Russell Smith has no motive: True or False?
True (0.5321820387813727)
Russell Smith has opportunity: True or False?
True (0.621540893468236)
Russell Smith has no opportunity: True or False?
False (0.673191669892235)
### Chris Palmer
- mean: False (0.36296916087547426)
- motive: False (0.16291207494381876)
- opportunity: False (0.4843800647594989)

### Matthew Light
- mean: False (0.2546016490346572)
- motive: False (0.20244312505268802)
- opportunity: False (0.32167304085228343)

### Mitchell Land
- mean: False (0.43014734572936386)
- motive: False (0.24364244272197833)
- opportunity: False (0.0)

### Paul Benham
- mean: True (0.726425644352388)
- motive: True (0.873646620599733)
- opportunity: True (0.6918097672776748)

### Russell Smith
- mean: False (0.26359939657546183)
- motive: False (0.4678179612186273)
- opportunity: False (0.0)

The culprit is Paul Benham.
In fact, it is Paul Benham.
## 5minutemystery-mystery-of-the-bratty-kid
Angelita is guilty: True or False?
True (0.8887587777822111)
Angelita is not guilty: True or False?
True (0.7918210572836727)
Angelita has mean: True or False?
True (0.847967740521315)
Angelita has no mean: True or False?
True (0.8558511727823209)
Angelita has motive: True or False?
True (0.8656789607733094)
Angelita has no motive: True or False?
True (0.6766198919456847)
Angelita has opportunity: True or False?
True (0.8887587777822111)
Angelita has no opportunity: True or False?
False (0.595492552580428)
Emily is guilty: True or False?
True (0.8906751877407573)
Emily is not guilty: True or False?
True (0.8803863464576128)
Emily has mean: True or False?
True (0.9238675252821831)
Emily has no mean: True or False?
True (0.9572777759716213)
Emily has motive: True or False?
True (0.8902942539348153)
Emily has no motive: True or False?
True (0.7853085971692302)
Emily has opportunity: True or False?
True (0.9127478016020363)
Emily has no opportunity: True or False?
False (0.5302364729224919)
Jessica is guilty: True or False?
True (0.8181563669811865)
Jessica is not guilty: True or False?
True (0.8013146490010521)
Jessica has mean: True or False?
True (0.7931058945535956)
Jessica has no mean: True or False?
True (0.7431679939957333)
Jessica has motive: True or False?
True (0.8198933606225757)
Jessica has no motive: True or False?
True (0.740174341079517)
Jessica has opportunity: True or False?
True (0.8539127714046447)
Jessica has no opportunity: True or False?
False (0.5467381591701916)
Percy Wellington is guilty: True or False?
True (0.9576753972844966)
Percy Wellington is not guilty: True or False?
True (0.9226219081780128)
Percy Wellington has mean: True or False?
True (0.9360516072812131)
Percy Wellington has no mean: True or False?
True (0.9639160647221925)
Percy Wellington has motive: True or False?
True (0.9489172681310486)
Percy Wellington has no motive: True or False?
True (0.8305941261447712)
Percy Wellington has opportunity: True or False?
True (0.9606574760904091)
Percy Wellington has no opportunity: True or False?
True (0.8181563669811865)
### Angelita
- mean: False (0.14414882721767908)
- motive: False (0.3233801080543153)
- opportunity: False (0.0)

### Emily
- mean: True (0.9238675252821831)
- motive: True (0.8902942539348153)
- opportunity: True (0.9127478016020363)

### Jessica
- mean: False (0.2568320060042667)
- motive: False (0.25982565892048304)
- opportunity: False (0.0)

### Percy Wellington
- mean: False (0.03608393527780751)
- motive: False (0.16940587385522876)
- opportunity: False (0.18184363301881346)

The culprit is Emily.
In fact, it is Angelita.
## 5minutemystery-the-card-shark
The cowboy is guilty: True or False?
True (0.8519527857346616)
The cowboy is not guilty: True or False?
True (0.8289388437432279)
The cowboy has mean: True or False?
True (0.7146280500737092)
The cowboy has no mean: True or False?
True (0.6315943123389512)
The cowboy has motive: True or False?
True (0.7752646804088963)
The cowboy has no motive: True or False?
True (0.7476159279883341)
The cowboy has opportunity: True or False?
True (0.8056321690561029)
The cowboy has no opportunity: True or False?
True (0.7114308541703346)
The gunslinger is guilty: True or False?
True (0.9216402157401415)
The gunslinger is not guilty: True or False?
True (0.8872045854516336)
The gunslinger has mean: True or False?
True (0.8615382357584752)
The gunslinger has no mean: True or False?
True (0.8104789202520752)
The gunslinger has motive: True or False?
True (0.8872045854516336)
The gunslinger has no motive: True or False?
True (0.8499711693725173)
The gunslinger has opportunity: True or False?
True (0.8770561879413864)
The gunslinger has no opportunity: True or False?
True (0.7739005566220397)
The lady is guilty: True or False?
True (0.8098781635062345)
The lady is not guilty: True or False?
True (0.8233283740192667)
The lady has mean: True or False?
True (0.7697732451157533)
The lady has no mean: True or False?
True (0.7931058945535956)
The lady has motive: True or False?
True (0.8868131040663721)
The lady has no motive: True or False?
True (0.8056321690561029)
The lady has opportunity: True or False?
True (0.8272706865691472)
The lady has no opportunity: True or False?
True (0.6451199006197486)
The sheriff is guilty: True or False?
True (0.8433798528114077)
The sheriff is not guilty: True or False?
True (0.7725306828324007)
The sheriff has mean: True or False?
Map:  31%|███       | 63/203 [38:51<1:34:56, 40.69s/ examples]Map:  32%|███▏      | 64/203 [39:19<1:25:21, 36.85s/ examples]Map:  32%|███▏      | 65/203 [39:57<1:25:43, 37.27s/ examples]True (0.743912876509037)
The sheriff has no mean: True or False?
True (0.6325027218909103)
The sheriff has motive: True or False?
True (0.776622945813876)
The sheriff has no motive: True or False?
True (0.6636689235052821)
The sheriff has opportunity: True or False?
True (0.8233283740192667)
The sheriff has no opportunity: True or False?
True (0.700075275973927)
### The cowboy
- mean: True (0.7146280500737092)
- motive: True (0.7752646804088963)
- opportunity: True (0.8056321690561029)

### The gunslinger
- mean: False (0.18952107974792476)
- motive: False (0.15002883062748273)
- opportunity: False (0.22609944337796029)

### The lady
- mean: False (0.2068941054464044)
- motive: False (0.1943678309438971)
- opportunity: False (0.35488009938025145)

### The sheriff
- mean: False (0.3674972781090897)
- motive: False (0.33633107649471794)
- opportunity: False (0.29992472402607295)

The culprit is The cowboy.
In fact, it is The sheriff.
## 5minutemystery-department-store-murder
Ed Puckett is guilty: True or False?
True (0.6343168649455533)
Ed Puckett is not guilty: True or False?
True (0.5573635130218721)
Ed Puckett has mean: True or False?
True (0.5117165908639297)
Ed Puckett has no mean: True or False?
False (0.7178037814283548)
Ed Puckett has motive: True or False?
True (0.7233094544266295)
Ed Puckett has no motive: True or False?
True (0.5457699766832048)
Ed Puckett has opportunity: True or False?
True (0.6783269591477166)
Ed Puckett has no opportunity: True or False?
False (0.5370414382302919)
Gene Roberts is guilty: True or False?
True (0.6842640081724978)
Gene Roberts is not guilty: True or False?
True (0.5029296229885981)
Gene Roberts has mean: True or False?
False (0.5418937216067536)
Gene Roberts has no mean: True or False?
False (0.7424217332471881)
Gene Roberts has motive: True or False?
True (0.6504672161860058)
Gene Roberts has no motive: True or False?
True (0.621540893468236)
Gene Roberts has opportunity: True or False?
True (0.555435228101316)
Gene Roberts has no opportunity: True or False?
False (0.6706082735718226)
George Whitley is guilty: True or False?
True (0.5583270361921496)
George Whitley is not guilty: True or False?
True (0.5389832197022594)
George Whitley has mean: True or False?
False (0.5592900581575188)
George Whitley has no mean: True or False?
False (0.7348812183274223)
George Whitley has motive: True or False?
True (0.5350984235603058)
George Whitley has no motive: True or False?
True (0.5156199352405011)
George Whitley has opportunity: True or False?
False (0.7498207054286419)
George Whitley has no opportunity: True or False?
False (0.6959583025067009)
Justin Tanner is guilty: True or False?
True (0.5650587803792624)
Justin Tanner is not guilty: True or False?
False (0.5496406401666291)
Justin Tanner has mean: True or False?
True (0.5068355091660127)
Justin Tanner has no mean: True or False?
False (0.767689835247798)
Justin Tanner has motive: True or False?
True (0.6011253583932805)
Justin Tanner has no motive: True or False?
True (0.5019531141001669)
Justin Tanner has opportunity: True or False?
False (0.5592900581575188)
Justin Tanner has no opportunity: True or False?
False (0.6601723415572317)
### Ed Puckett
- mean: True (0.5117165908639297)
- motive: True (0.7233094544266295)
- opportunity: True (0.6783269591477166)

### Gene Roberts
- mean: False (0.5418937216067536)
- motive: False (0.37845910653176396)
- opportunity: False (0.0)

### George Whitley
- mean: False (0.5592900581575188)
- motive: False (0.4843800647594989)
- opportunity: False (0.7498207054286419)

### Justin Tanner
- mean: False (0.0)
- motive: False (0.49804688589983315)
- opportunity: False (0.5592900581575188)

The culprit is Ed Puckett.
In fact, it is Justin Tanner.
## 5minutemystery-the-candy-store-mystery
Brianna Cates is guilty: True or False?
False (0.5640984675176304)
Brianna Cates is not guilty: True or False?
False (0.6757646168022439)
Brianna Cates has mean: True or False?
True (0.5717666110200305)
Brianna Cates has no mean: True or False?
False (0.591723272524637)
Brianna Cates has motive: True or False?
True (0.779321849347754)
Brianna Cates has no motive: True or False?
True (0.566977858563838)
Brianna Cates has opportunity: True or False?
True (0.64779823427608)
Brianna Cates has no opportunity: True or False?
False (0.5602526707659626)
Emilee Johnson is guilty: True or False?
False (0.6057990946577705)
Emilee Johnson is not guilty: True or False?
False (0.6067314814064781)
Emilee Johnson has mean: True or False?
True (0.6095241271158658)
Emilee Johnson has no mean: True or False?
True (0.5117165908639297)
Emilee Johnson has motive: True or False?
True (0.7931059536445917)
Emilee Johnson has no motive: True or False?
True (0.6095241816115718)
Emilee Johnson has opportunity: True or False?
True (0.5822535180679596)
Emilee Johnson has no opportunity: True or False?
False (0.5380124470448935)
Justin Cates is guilty: True or False?
False (0.5669777909748143)
Justin Cates is not guilty: True or False?
False (0.7017130830397807)
Justin Cates has mean: True or False?
False (0.5185462156586879)
Justin Cates has no mean: True or False?
False (0.5583269696343842)
Justin Cates has motive: True or False?
True (0.8068526417769779)
Justin Cates has no motive: True or False?
False (0.5156199352405011)
Justin Cates has opportunity: True or False?
True (0.5107405858633529)
Justin Cates has no opportunity: True or False?
False (0.6279512069990912)
Olivia (Livvie) Johnson is guilty: True or False?
False (0.5370414382302919)
Olivia (Livvie) Johnson is not guilty: True or False?
False (0.6959583025067009)
Olivia (Livvie) Johnson has mean: True or False?
False (0.6297746298200823)
Olivia (Livvie) Johnson has no mean: True or False?
True (0.5097643762740132)
Olivia (Livvie) Johnson has motive: True or False?
True (0.7520125537161032)
Olivia (Livvie) Johnson has no motive: True or False?
True (0.5409238326546766)
Olivia (Livvie) Johnson has opportunity: True or False?
True (0.6513548405484016)
Olivia (Livvie) Johnson has no opportunity: True or False?
True (0.5515736950589613)
Trevor Cates is guilty: True or False?
False (0.5822535180679596)
Trevor Cates is not guilty: True or False?
False (0.5755879969637064)
Trevor Cates has mean: True or False?
True (0.6020616403539744)
Trevor Cates has no mean: True or False?
True (0.6206215556999736)
Trevor Cates has motive: True or False?
True (0.6504672161860058)
Trevor Cates has no motive: True or False?
True (0.5185461538431656)
Trevor Cates has opportunity: True or False?
True (0.5107405249783342)
Trevor Cates has no opportunity: True or False?
False (0.6160122877297346)
### Brianna Cates
- mean: False (0.0)
- motive: False (0.433022141436162)
- opportunity: False (0.0)

### Emilee Johnson
- mean: False (0.48828340913607027)
- motive: False (0.39047581838842815)
- opportunity: False (0.0)

### Justin Cates
- mean: True (0.4416730303656158)
- motive: True (0.8068526417769779)
- opportunity: True (0.5107405858633529)

### Olivia (Livvie) Johnson
- mean: False (0.6297746298200823)
- motive: False (0.4590761673453234)
- opportunity: False (0.44842630494103874)

### Trevor Cates
- mean: False (0.37937844430002643)
- motive: False (0.4814538461568344)
- opportunity: False (0.0)

The culprit is Justin Cates.
In fact, it is Justin Cates.
## 5minutemystery-for-the-birds
Billy Mumms is guilty: True or False?
True (0.9456006304504523)
Billy Mumms is not guilty: True or False?
True (0.9123581072962114)
Billy Mumms has mean: True or False?
True (0.776622945813876)
Billy Mumms has no mean: True or False?
True (0.6379334932841956)
Billy Mumms has motive: True or False?
True (1.4706562349249974)
Billy Mumms has no motive: True or False?
True (0.6482437163885266)
Billy Mumms has opportunity: True or False?
True (0.761006053879754)
Billy Mumms has no opportunity: True or False?
True (0.5034179144599427)
Cheryl Judson is guilty: True or False?
True (0.862930180750016)
Cheryl Judson is not guilty: True or False?
False (0.9725407553741882)
Cheryl Judson has mean: True or False?
True (0.7809967375818414)
Cheryl Judson has no mean: True or False?
True (0.6808786440630326)
Cheryl Judson has motive: True or False?
Map:  33%|███▎      | 66/203 [40:42<1:30:13, 39.51s/ examples]Map:  33%|███▎      | 67/203 [41:17<1:26:20, 38.09s/ examples]Map:  33%|███▎      | 68/203 [42:01<1:29:59, 39.99s/ examples]True (2.272887661768761)
Cheryl Judson has no motive: True or False?
False (0.45581836876730714)
Cheryl Judson has opportunity: True or False?
False (0.43382908131769415)
Cheryl Judson has no opportunity: True or False?
False (0.6592954931819778)
Stan Mifflin is guilty: True or False?
True (0.9222025890552223)
Stan Mifflin is not guilty: True or False?
True (0.9038048413863352)
Stan Mifflin has mean: True or False?
True (0.8003801084788502)
Stan Mifflin has no mean: True or False?
True (0.6723316913929156)
Stan Mifflin has motive: True or False?
True (0.9238675252821831)
Stan Mifflin has no motive: True or False?
True (0.784649255215384)
Stan Mifflin has opportunity: True or False?
True (0.7969253675907205)
Stan Mifflin has no opportunity: True or False?
True (0.6876299924560524)
Tor Hansen is guilty: True or False?
True (0.9504569764036419)
Tor Hansen is not guilty: True or False?
True (1.8090556492125005)
Tor Hansen has mean: True or False?
True (0.7721872299079675)
Tor Hansen has no mean: True or False?
True (0.6884683992569801)
Tor Hansen has motive: True or False?
True (7.849831281233191)
Tor Hansen has no motive: True or False?
True (0.8083669082173469)
Tor Hansen has opportunity: True or False?
True (0.7819973291046377)
Tor Hansen has no opportunity: True or False?
False (0.6808785831877406)
### Billy Mumms
- mean: False (0.3620665067158044)
- motive: False (0.3517562836114734)
- opportunity: False (0.49658208554005734)

### Cheryl Judson
- mean: False (0.31912135593696744)
- motive: False (0.0)
- opportunity: False (0.43382908131769415)

### Stan Mifflin
- mean: False (0.3276683086070844)
- motive: False (0.21535074478461602)
- opportunity: False (0.3123700075439476)

### Tor Hansen
- mean: True (0.7721872299079675)
- motive: True (7.849831281233191)
- opportunity: True (0.7819973291046377)

The culprit is Tor Hansen.
In fact, it is Cheryl Judson.
## 5minutemystery-the-zoo-job
Cindy is guilty: True or False?
True (0.6662796150778861)
Cindy is not guilty: True or False?
True (0.6522414018725713)
Cindy has mean: True or False?
True (0.7885832152749314)
Cindy has no mean: True or False?
False (0.6001883144765984)
Cindy has motive: True or False?
True (0.869271276026005)
Cindy has no motive: True or False?
False (0.5428632463719839)
Cindy has opportunity: True or False?
True (0.6388353131709135)
Cindy has no opportunity: True or False?
False (0.8647679145346777)
Henry is guilty: True or False?
True (0.6566582306092376)
Henry is not guilty: True or False?
True (0.6619228707202935)
Henry has mean: True or False?
True (0.7416740115009234)
Henry has no mean: True or False?
False (0.6749081498948247)
Henry has motive: True or False?
True (0.8828325273478573)
Henry has no motive: True or False?
False (0.5009765603034438)
Henry has opportunity: True or False?
True (0.5631377056275331)
Henry has no opportunity: True or False?
False (0.8509647293237851)
Leonard is guilty: True or False?
True (0.642432441257838)
Leonard is not guilty: True or False?
True (0.6926419789019715)
Leonard has mean: True or False?
True (0.8582439976623328)
Leonard has no mean: True or False?
True (0.5107405249783342)
Leonard has motive: True or False?
True (0.8272706865691472)
Leonard has no motive: True or False?
False (0.6757646168022439)
Leonard has opportunity: True or False?
True (0.5583270361921496)
Leonard has no opportunity: True or False?
False (0.861538171568877)
Tom is guilty: True or False?
False (0.5136684743338078)
Tom is not guilty: True or False?
True (0.5679366075542497)
Tom has mean: True or False?
True (0.7272012283179254)
Tom has no mean: True or False?
False (0.7090191197769757)
Tom has motive: True or False?
True (0.7846493136763113)
Tom has no motive: True or False?
False (0.5765418892261284)
Tom has opportunity: True or False?
False (0.5360700410935405)
Tom has no opportunity: True or False?
False (0.8013146490010521)
### Cindy
- mean: True (0.7885832152749314)
- motive: True (0.869271276026005)
- opportunity: True (0.6388353131709135)

### Henry
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.0)

### Leonard
- mean: False (0.4892594750216658)
- motive: False (0.0)
- opportunity: False (0.0)

### Tom
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.5360700410935405)

The culprit is Cindy.
In fact, it is Cindy.
## 5minutemystery-did-the-vicar-solve-the-mystery
Elmer Tydings is guilty: True or False?
True (0.9377830065075011)
Elmer Tydings is not guilty: True or False?
True (0.9393038120802789)
Elmer Tydings has mean: True or False?
True (0.9425067301242699)
Elmer Tydings has no mean: True or False?
True (0.7252596042773647)
Elmer Tydings has motive: True or False?
True (0.9167080509980843)
Elmer Tydings has no motive: True or False?
True (0.871911710743649)
Elmer Tydings has opportunity: True or False?
True (0.9511421913058572)
Elmer Tydings has no opportunity: True or False?
True (0.6791786560103119)
John Stubbs is guilty: True or False?
True (0.8946054590684968)
John Stubbs is not guilty: True or False?
True (0.9078854924000437)
John Stubbs has mean: True or False?
True (0.897695304229796)
John Stubbs has no mean: True or False?
True (0.7613611200983542)
John Stubbs has motive: True or False?
True (0.842085543919308)
John Stubbs has no motive: True or False?
True (0.8705973031072073)
John Stubbs has opportunity: True or False?
True (0.8314170225049837)
John Stubbs has no opportunity: True or False?
True (0.6334102859975052)
Katherine Tydings is guilty: True or False?
True (0.8820219652716884)
Katherine Tydings is not guilty: True or False?
True (0.9071478234767817)
Katherine Tydings has mean: True or False?
True (0.8086723099497763)
Katherine Tydings has no mean: True or False?
True (0.7209580003592615)
Katherine Tydings has motive: True or False?
True (0.8426043397677332)
Katherine Tydings has no motive: True or False?
True (0.8608377628023384)
Katherine Tydings has opportunity: True or False?
True (0.8710367026584496)
Katherine Tydings has no opportunity: True or False?
True (0.6597340764477)
Louise Stubbs is guilty: True or False?
True (0.8822251029233062)
Louise Stubbs is not guilty: True or False?
True (0.9118884802226345)
Louise Stubbs has mean: True or False?
True (0.8918110736745599)
Louise Stubbs has no mean: True or False?
True (0.8712559403160255)
Louise Stubbs has motive: True or False?
True (0.8474634858439474)
Louise Stubbs has no motive: True or False?
True (0.9041439284393449)
Louise Stubbs has opportunity: True or False?
True (0.8502200840158227)
Louise Stubbs has no opportunity: True or False?
True (0.7185944237486072)
### Elmer Tydings
- mean: False (0.2747403957226353)
- motive: False (0.12808828925635096)
- opportunity: False (0.3208213439896881)

### John Stubbs
- mean: False (0.23863887990164578)
- motive: False (0.1294026968927927)
- opportunity: False (0.36658971400249485)

### Katherine Tydings
- mean: False (0.2790419996407385)
- motive: False (0.13916223719766163)
- opportunity: False (0.3402659235523)

### Louise Stubbs
- mean: True (0.8918110736745599)
- motive: True (0.8474634858439474)
- opportunity: True (0.8502200840158227)

The culprit is Louise Stubbs.
In fact, it is Katherine Tydings.
## 5minutemystery-who-scratched-the-porsche
Colonel Greenerbaum is guilty: True or False?
True (0.8267117710471246)
Colonel Greenerbaum is not guilty: True or False?
True (0.7655933544531522)
Colonel Greenerbaum has mean: True or False?
True (0.8606036289596553)
Colonel Greenerbaum has no mean: True or False?
True (0.855126793018422)
Colonel Greenerbaum has motive: True or False?
True (0.8122724274380432)
Colonel Greenerbaum has no motive: True or False?
True (0.7711548223101617)
Colonel Greenerbaum has opportunity: True or False?
True (0.6288633913849659)
Colonel Greenerbaum has no opportunity: True or False?
False (0.5029296229885981)
Fido is guilty: True or False?
False (0.6294825245063967)
Fido is not guilty: True or False?
True (0.862930245043327)
Fido has mean: True or False?
True (0.8984105603938967)
Fido has no mean: True or False?
True (0.8221890958162477)
Fido has motive: True or False?
False (1.0711799654134986)
Fido has no motive: True or False?
True (0.8044058710149623)
Map:  34%|███▍      | 69/203 [42:47<1:33:23, 41.81s/ examples]Map:  34%|███▍      | 70/203 [43:23<1:28:55, 40.12s/ examples]Map:  35%|███▍      | 71/203 [43:55<1:22:46, 37.62s/ examples]Fido has opportunity: True or False?
False (1.2194432145551726)
Fido has no opportunity: True or False?
False (0.3890169404341139)
Malcolm is guilty: True or False?
True (0.6834194581047349)
Malcolm is not guilty: True or False?
True (0.7697732451157533)
Malcolm has mean: True or False?
True (0.7634837587244478)
Malcolm has no mean: True or False?
True (0.6370307821695329)
Malcolm has motive: True or False?
True (0.8294920340613177)
Malcolm has no motive: True or False?
True (0.5048826258478675)
Malcolm has opportunity: True or False?
True (0.5195212821349473)
Malcolm has no opportunity: True or False?
False (0.7620701143808404)
Roxie is guilty: True or False?
True (0.6132366084149281)
Roxie is not guilty: True or False?
True (0.6592954931819778)
Roxie has mean: True or False?
True (0.7527403228571042)
Roxie has no mean: True or False?
True (0.7209580003592615)
Roxie has motive: True or False?
True (0.8360196960886609)
Roxie has no motive: True or False?
False (0.555435228101316)
Roxie has opportunity: True or False?
True (0.5888891269161294)
Roxie has no opportunity: True or False?
False (0.7201714538416826)
### Colonel Greenerbaum
- mean: False (0.14487320698157802)
- motive: False (0.22884517768983825)
- opportunity: False (0.0)

### Fido
- mean: False (0.17781090418375234)
- motive: False (1.0711799654134986)
- opportunity: False (1.2194432145551726)

### Malcolm
- mean: False (0.3629692178304671)
- motive: False (0.49511737415213253)
- opportunity: False (0.0)

### Roxie
- mean: True (0.7527403228571042)
- motive: True (0.8360196960886609)
- opportunity: True (0.5888891269161294)

The culprit is Roxie.
In fact, it is Colonel Greenerbaum.
## 5minutemystery-the-thief-in-the-night-mystery
Jon Shaw is guilty: True or False?
True (0.8591918406281239)
Jon Shaw is not guilty: True or False?
True (0.8433797899747144)
Jon Shaw has mean: True or False?
True (0.8019357965963964)
Jon Shaw has no mean: True or False?
False (0.7074046739492601)
Jon Shaw has motive: True or False?
True (0.7972412725773819)
Jon Shaw has no motive: True or False?
True (0.5926665645259142)
Jon Shaw has opportunity: True or False?
False (0.5987815071974216)
Jon Shaw has no opportunity: True or False?
False (0.6710395833592795)
Max Reinke is guilty: True or False?
True (0.8172829725974129)
Max Reinke is not guilty: True or False?
True (0.8300437877296776)
Max Reinke has mean: True or False?
False (0.7786493288700866)
Max Reinke has no mean: True or False?
False (0.7895584060718701)
Max Reinke has motive: True or False?
True (0.7310585348819939)
Max Reinke has no motive: True or False?
True (0.6796041154763541)
Max Reinke has opportunity: True or False?
False (0.7102264820691382)
Max Reinke has no opportunity: True or False?
False (0.7538293096563191)
Todd Summers is guilty: True or False?
True (0.8633916342942395)
Todd Summers is not guilty: True or False?
True (0.8774768149941248)
Todd Summers has mean: True or False?
True (0.7683857617837733)
Todd Summers has no mean: True or False?
True (0.5612147992901458)
Todd Summers has motive: True or False?
True (0.8161134110084781)
Todd Summers has no motive: True or False?
True (0.7379142672364736)
Todd Summers has opportunity: True or False?
True (0.5631377056275331)
Todd Summers has no opportunity: True or False?
False (0.6197014353942354)
Zac Coulson is guilty: True or False?
True (0.9395815725100197)
Zac Coulson is not guilty: True or False?
True (0.9122800266337535)
Zac Coulson has mean: True or False?
True (0.6415346823638186)
Zac Coulson has no mean: True or False?
True (0.5602526707659626)
Zac Coulson has motive: True or False?
True (0.8679338050595715)
Zac Coulson has no motive: True or False?
True (0.8181563669811865)
Zac Coulson has opportunity: True or False?
True (0.6279512069990912)
Zac Coulson has no opportunity: True or False?
False (0.6575384693006662)
### Jon Shaw
- mean: True (0.8019357965963964)
- motive: True (0.7972412725773819)
- opportunity: True (0.3289604166407205)

### Max Reinke
- mean: False (0.7786493288700866)
- motive: False (0.32039588452364587)
- opportunity: False (0.7102264820691382)

### Todd Summers
- mean: False (0.43878520070985416)
- motive: False (0.2620857327635264)
- opportunity: False (0.0)

### Zac Coulson
- mean: False (0.43974732923403737)
- motive: False (0.18184363301881346)
- opportunity: False (0.0)

The culprit is Jon Shaw.
In fact, it is Zac Coulson.
## 5minutemystery-ladies-at-table
Alice is guilty: True or False?
True (0.6388352560545881)
Alice is not guilty: True or False?
True (0.6876299924560524)
Alice has mean: True or False?
True (0.8062431235779619)
Alice has no mean: True or False?
False (0.5234203246639862)
Alice has motive: True or False?
True (0.6636689235052821)
Alice has no motive: True or False?
True (0.6206215556999736)
Alice has opportunity: True or False?
True (0.6706082735718226)
Alice has no opportunity: True or False?
False (0.5813030649269245)
Frances is guilty: True or False?
False (0.5126925663186335)
Frances is not guilty: True or False?
True (0.5841525082971981)
Frances has mean: True or False?
True (0.8158201638039532)
Frances has no mean: True or False?
True (0.5477060024984176)
Frances has motive: True or False?
True (0.7424217332471881)
Frances has no motive: True or False?
True (0.5992506595844092)
Frances has opportunity: True or False?
False (0.5592900581575188)
Frances has no opportunity: True or False?
False (0.7325918054337844)
Leona is guilty: True or False?
True (0.5535053004623279)
Leona is not guilty: True or False?
True (0.6029970803636248)
Leona has mean: True or False?
True (0.7839884107482739)
Leona has no mean: True or False?
False (0.5350984235603058)
Leona has motive: True or False?
True (0.6469064338453809)
Leona has no motive: True or False?
True (0.5282900215677746)
Leona has opportunity: True or False?
True (0.525368812147771)
Leona has no opportunity: True or False?
False (0.6361271113853048)
Mary is guilty: True or False?
False (0.6610481693322063)
Mary is not guilty: True or False?
True (0.5312093941731293)
Mary has mean: True or False?
True (0.7577943897558946)
Mary has no mean: True or False?
False (0.644225125126315)
Mary has motive: True or False?
True (0.5273165696704634)
Mary has no motive: True or False?
True (0.5136684130997575)
Mary has opportunity: True or False?
False (0.6306849143569856)
Mary has no opportunity: True or False?
False (0.6513548405484016)
Ruth is guilty: True or False?
True (0.6048657973050737)
Ruth is not guilty: True or False?
True (0.8019358443954961)
Ruth has mean: True or False?
True (0.9041439284393449)
Ruth has no mean: True or False?
True (0.7617158298609953)
Ruth has motive: True or False?
True (0.8386797935187188)
Ruth has no motive: True or False?
True (0.7498206607358464)
Ruth has opportunity: True or False?
True (0.8181563669811865)
Ruth has no opportunity: True or False?
True (0.5669777909748143)
### Alice
- mean: True (0.8062431235779619)
- motive: True (0.6636689235052821)
- opportunity: True (0.6706082735718226)

### Frances
- mean: False (0.4522939975015824)
- motive: False (0.40074934041559085)
- opportunity: False (0.5592900581575188)

### Leona
- mean: False (0.0)
- motive: False (0.4717099784322254)
- opportunity: False (0.0)

### Mary
- mean: False (0.0)
- motive: False (0.4863315869002425)
- opportunity: False (0.6306849143569856)

### Ruth
- mean: False (0.23828417013900471)
- motive: False (0.2501793392641536)
- opportunity: False (0.43302220902518573)

The culprit is Alice.
In fact, it is Leona.
## 5minutemystery-the-diamond-necklace
Abby Grant is guilty: True or False?
True (0.9246876822649571)
Abby Grant is not guilty: True or False?
True (0.9337940192482527)
Abby Grant has mean: True or False?
True (0.776622945813876)
Abby Grant has no mean: True or False?
True (0.6379334932841956)
Abby Grant has motive: True or False?
True (0.9056565771882901)
Abby Grant has no motive: True or False?
True (0.8852351930010195)
Abby Grant has opportunity: True or False?
True (0.904313027820426)
Abby Grant has no opportunity: True or False?
True (0.8300437258865985)
Colonel Barrow is guilty: True or False?
True (0.9425596581002386)
Colonel Barrow is not guilty: True or False?
Map:  35%|███▌      | 72/203 [44:31<1:21:05, 37.14s/ examples]Map:  36%|███▌      | 73/203 [45:06<1:18:45, 36.35s/ examples]True (0.9519526969616549)
Colonel Barrow has mean: True or False?
True (0.9415467969679381)
Colonel Barrow has no mean: True or False?
True (0.6491338587652001)
Colonel Barrow has motive: True or False?
True (0.9151287648632792)
Colonel Barrow has no motive: True or False?
True (0.8524448242555318)
Colonel Barrow has opportunity: True or False?
True (0.9284088027271398)
Colonel Barrow has no opportunity: True or False?
True (0.8668104417201673)
Fiona Duncan is guilty: True or False?
True (0.921357630313903)
Fiona Duncan is not guilty: True or False?
False (1.2176123599793751)
Fiona Duncan has mean: True or False?
True (0.9187722824991111)
Fiona Duncan has no mean: True or False?
False (1.0456076263702099)
Fiona Duncan has motive: True or False?
True (0.8987665204865408)
Fiona Duncan has no motive: True or False?
True (0.8971559437869847)
Fiona Duncan has opportunity: True or False?
False (0.867271773267888)
Fiona Duncan has no opportunity: True or False?
False (3.3593556879645794)
Harold Duncan is guilty: True or False?
True (0.9430336353172679)
Harold Duncan is not guilty: True or False?
True (0.9435560124549824)
Harold Duncan has mean: True or False?
True (0.9257686153543061)
Harold Duncan has no mean: True or False?
True (0.6379335503198971)
Harold Duncan has motive: True or False?
True (0.9170801638253802)
Harold Duncan has no motive: True or False?
True (0.8482193926289605)
Harold Duncan has opportunity: True or False?
True (0.878314250659373)
Harold Duncan has no opportunity: True or False?
True (0.6428810349192753)
Maurice Eades is guilty: True or False?
True (0.8172829725974129)
Maurice Eades is not guilty: True or False?
True (0.7862948177096581)
Maurice Eades has mean: True or False?
True (0.874934615163517)
Maurice Eades has no mean: True or False?
False (0.7416740115009234)
Maurice Eades has motive: True or False?
True (0.7118317540033398)
Maurice Eades has no motive: True or False?
True (0.615087818987177)
Maurice Eades has opportunity: True or False?
True (0.7348812840309261)
Maurice Eades has no opportunity: True or False?
False (0.6397360437814448)
### Abby Grant
- mean: False (0.3620665067158044)
- motive: False (0.1147648069989805)
- opportunity: False (0.16995627411340153)

### Colonel Barrow
- mean: False (0.35086614123479987)
- motive: False (0.1475551757444682)
- opportunity: False (0.1331895582798327)

### Fiona Duncan
- mean: False (0.0)
- motive: False (0.10284405621301529)
- opportunity: False (0.867271773267888)

### Harold Duncan
- mean: False (0.36206644968010293)
- motive: False (0.1517806073710395)
- opportunity: False (0.3571189650807247)

### Maurice Eades
- mean: True (0.874934615163517)
- motive: True (0.7118317540033398)
- opportunity: True (0.7348812840309261)

The culprit is Maurice Eades.
In fact, it is Fiona Duncan.
## 5minutemystery-rhyming-presidents-mystery
George Bush is guilty: True or False?
True (0.8826303480425456)
George Bush is not guilty: True or False?
True (0.860369148541484)
George Bush has mean: True or False?
True (0.883437276390578)
George Bush has no mean: True or False?
True (0.733738122727274)
George Bush has motive: True or False?
True (0.8787311338092536)
George Bush has no motive: True or False?
True (0.8607207584614007)
George Bush has opportunity: True or False?
True (0.7627776774954688)
George Bush has no opportunity: True or False?
False (0.44985263935249425)
Gerald Ford is guilty: True or False?
True (0.8446654650893471)
Gerald Ford is not guilty: True or False?
False (0.543278126686496)
Gerald Ford has mean: True or False?
True (0.7962924854830264)
Gerald Ford has no mean: True or False?
False (0.5841552937600593)
Gerald Ford has motive: True or False?
False (0.8711530453124382)
Gerald Ford has no motive: True or False?
False (1.2922565011311467)
Gerald Ford has opportunity: True or False?
False (1.0412860786207854)
Gerald Ford has no opportunity: True or False?
False (0.8298881061894612)
John Quincy Adams is guilty: True or False?
True (0.8613050536634502)
John Quincy Adams is not guilty: True or False?
True (0.8472108208062923)
John Quincy Adams has mean: True or False?
True (0.7490872087035162)
John Quincy Adams has no mean: True or False?
True (0.7302898714065358)
John Quincy Adams has motive: True or False?
True (0.8181564157471076)
John Quincy Adams has no motive: True or False?
True (0.7252596691206291)
John Quincy Adams has opportunity: True or False?
True (0.7494540906858582)
John Quincy Adams has no opportunity: True or False?
True (0.6557770400181139)
Richard Nixon is guilty: True or False?
True (0.8640812064457842)
Richard Nixon is not guilty: True or False?
True (0.8305941261447712)
Richard Nixon has mean: True or False?
True (0.7813305798204846)
Richard Nixon has no mean: True or False?
True (0.5535053004623279)
Richard Nixon has motive: True or False?
True (0.8092759828926619)
Richard Nixon has no motive: True or False?
False (0.4085073252175706)
Richard Nixon has opportunity: True or False?
True (0.6808786440630326)
Richard Nixon has no opportunity: True or False?
True (0.5973730125048408)
### George Bush
- mean: False (0.266261877272726)
- motive: False (0.13927924153859927)
- opportunity: False (0.0)

### Gerald Ford
- mean: True (0.7962924854830264)
- motive: True (0.0)
- opportunity: True (0.17011189381053882)

### John Quincy Adams
- mean: False (0.2697101285934642)
- motive: False (0.2747403308793709)
- opportunity: False (0.3442229599818861)

### Richard Nixon
- mean: False (0.44649469953767207)
- motive: False (0.0)
- opportunity: False (0.40262698749515924)

The culprit is Gerald Ford.
In fact, it is Gerald Ford.
## 5minutemystery-the-white-house-ghosts
Andrew Jackson is guilty: True or False?
True (0.9823724633578762)
Andrew Jackson is not guilty: True or False?
True (0.9728823298761804)
Andrew Jackson has mean: True or False?
True (0.9190632712053527)
Andrew Jackson has no mean: True or False?
True (0.8670358119601653)
Andrew Jackson has motive: True or False?
True (0.9707016952697487)
Andrew Jackson has no motive: True or False?
True (0.9710056184023123)
Andrew Jackson has opportunity: True or False?
True (0.9481545078856665)
Andrew Jackson has no opportunity: True or False?
True (0.9034646765933593)
Calvin Coolidge is guilty: True or False?
True (0.9716717007848752)
Calvin Coolidge is not guilty: True or False?
True (0.96621972227362)
Calvin Coolidge has mean: True or False?
True (0.934872446722342)
Calvin Coolidge has no mean: True or False?
True (0.8978744762836591)
Calvin Coolidge has motive: True or False?
True (0.9789554468203624)
Calvin Coolidge has no motive: True or False?
True (0.962883113150675)
Calvin Coolidge has opportunity: True or False?
True (0.9445871723447916)
Calvin Coolidge has no opportunity: True or False?
True (0.8553686139061228)
John Adams is guilty: True or False?
True (0.9672250166644973)
John Adams is not guilty: True or False?
True (0.965608894574138)
John Adams has mean: True or False?
True (0.9509603994010378)
John Adams has no mean: True or False?
True (0.8681575656976329)
John Adams has motive: True or False?
True (0.9553191057869168)
John Adams has no motive: True or False?
True (0.9343951361750445)
John Adams has opportunity: True or False?
True (0.8891444205417208)
John Adams has no opportunity: True or False?
True (0.7549149897594328)
William Howard Taft is guilty: True or False?
True (0.9554855815192022)
William Howard Taft is not guilty: True or False?
True (0.945901275404696)
William Howard Taft has mean: True or False?
True (0.9317114347547434)
William Howard Taft has no mean: True or False?
True (0.832781373043151)
William Howard Taft has motive: True or False?
True (0.9496343151593544)
William Howard Taft has no motive: True or False?
True (0.9438413381297024)
William Howard Taft has opportunity: True or False?
True (0.9183338305905581)
William Howard Taft has no opportunity: True or False?
True (0.8570517947007738)
### Andrew Jackson
- mean: True (0.9190632712053527)
- motive: True (0.9707016952697487)
- opportunity: True (0.9481545078856665)

### Calvin Coolidge
- mean: False (0.10212552371634087)
- motive: False (0.037116886849325015)
- opportunity: False (0.14463138609387716)

### John Adams
Map:  36%|███▋      | 74/203 [45:43<1:18:46, 36.64s/ examples]Map:  37%|███▋      | 75/203 [46:23<1:20:37, 37.79s/ examples]Map:  37%|███▋      | 76/203 [47:03<1:21:23, 38.45s/ examples]- mean: False (0.13184243430236708)
- motive: False (0.06560486382495545)
- opportunity: False (0.24508501024056717)

### William Howard Taft
- mean: False (0.16721862695684897)
- motive: False (0.05615866187029761)
- opportunity: False (0.14294820529922625)

The culprit is Andrew Jackson.
In fact, it is Calvin Coolidge.
## 5minutemystery-mr-patrick-and-the-graveyard-mystery
Grave no.1 is guilty: True or False?
True (0.9686788908454032)
Grave no.1 is not guilty: True or False?
True (0.9268352400785028)
Grave no.1 has mean: True or False?
True (0.9753900767342161)
Grave no.1 has no mean: True or False?
True (0.9082930704920021)
Grave no.1 has motive: True or False?
True (0.9425066704353817)
Grave no.1 has no motive: True or False?
True (0.9496693599006181)
Grave no.1 has opportunity: True or False?
True (0.9572778330298248)
Grave no.1 has no opportunity: True or False?
True (0.9276259554905466)
Grave no.2 is guilty: True or False?
True (0.9529258022651363)
Grave no.2 is not guilty: True or False?
True (0.878314250659373)
Grave no.2 has mean: True or False?
True (0.9680204387474981)
Grave no.2 has no mean: True or False?
True (0.9008791478232747)
Grave no.2 has motive: True or False?
True (0.9246876822649571)
Grave no.2 has no motive: True or False?
True (0.8868131040663721)
Grave no.2 has opportunity: True or False?
True (0.9394706502722077)
Grave no.2 has no opportunity: True or False?
True (0.892187358563457)
Grave no.3 is guilty: True or False?
True (0.9479621664653681)
Grave no.3 is not guilty: True or False?
True (0.8558511727823209)
Grave no.3 has mean: True or False?
True (0.9752018447706344)
Grave no.3 has no mean: True or False?
True (0.9230391966311572)
Grave no.3 has motive: True or False?
True (0.9469902528343473)
Grave no.3 has no motive: True or False?
True (0.8697146199790504)
Grave no.3 has opportunity: True or False?
True (0.948346255948953)
Grave no.3 has no opportunity: True or False?
True (0.8774768149941248)
Grave no.4 is guilty: True or False?
True (0.9594593035226332)
Grave no.4 is not guilty: True or False?
True (0.8816148581338575)
Grave no.4 has mean: True or False?
True (0.9755769367349482)
Grave no.4 has no mean: True or False?
True (0.9346342066470359)
Grave no.4 has motive: True or False?
True (0.9190632712053527)
Grave no.4 has no motive: True or False?
True (0.8799743689174987)
Grave no.4 has opportunity: True or False?
True (0.9433475737015985)
Grave no.4 has no opportunity: True or False?
True (0.8933093589621482)
Grave no.5 is guilty: True or False?
True (0.9729338284788606)
Grave no.5 is not guilty: True or False?
True (0.9039745373919651)
Grave no.5 has mean: True or False?
True (0.9773707989989006)
Grave no.5 has no mean: True or False?
True (0.9012274173198201)
Grave no.5 has motive: True or False?
True (0.8887587777822111)
Grave no.5 has no motive: True or False?
True (0.8344069148356309)
Grave no.5 has opportunity: True or False?
True (0.9139841191734227)
Grave no.5 has no opportunity: True or False?
True (0.832781310996106)
### Grave no.1
- mean: True (0.9753900767342161)
- motive: True (0.9425066704353817)
- opportunity: True (0.9572778330298248)

### Grave no.2
- mean: False (0.09912085217672528)
- motive: False (0.11318689593362785)
- opportunity: False (0.10781264143654301)

### Grave no.3
- mean: False (0.07696080336884281)
- motive: False (0.13028538002094958)
- opportunity: False (0.12252318500587522)

### Grave no.4
- mean: False (0.06536579335296411)
- motive: False (0.1200256310825013)
- opportunity: False (0.10669064103785175)

### Grave no.5
- mean: False (0.09877258268017985)
- motive: False (0.1655930851643691)
- opportunity: False (0.16721868900389403)

The culprit is Grave no.1.
In fact, it is Grave no.4.
## 5minutemystery-lockbox-100
Edward Frates is guilty: True or False?
True (0.7106282704218558)
Edward Frates is not guilty: True or False?
True (0.7641883982873323)
Edward Frates has mean: True or False?
True (0.7994423454932595)
Edward Frates has no mean: True or False?
True (0.6178585826183487)
Edward Frates has motive: True or False?
True (0.6808786440630326)
Edward Frates has no motive: True or False?
True (0.7570767382203575)
Edward Frates has opportunity: True or False?
True (0.6934729802503211)
Edward Frates has no opportunity: True or False?
True (0.5774954003013352)
James Madigan is guilty: True or False?
True (0.740174341079517)
James Madigan is not guilty: True or False?
True (0.8062431235779619)
James Madigan has mean: True or False?
True (0.7512834059294674)
James Madigan has no mean: True or False?
False (0.5009765603034438)
James Madigan has motive: True or False?
True (0.5992506595844092)
James Madigan has no motive: True or False?
True (0.8386797310322072)
James Madigan has opportunity: True or False?
True (0.644225125126315)
James Madigan has no opportunity: True or False?
True (0.673191669892235)
Peter Zielny is guilty: True or False?
True (0.7193836000532381)
Peter Zielny is not guilty: True or False?
True (0.8261514850267767)
Peter Zielny has mean: True or False?
True (0.7371581892031299)
Peter Zielny has no mean: True or False?
False (0.6557770400181139)
Peter Zielny has motive: True or False?
True (0.743912876509037)
Peter Zielny has no motive: True or False?
True (0.7090191197769757)
Peter Zielny has opportunity: True or False?
True (0.5992506595844092)
Peter Zielny has no opportunity: True or False?
False (0.5438324636094939)
Ronald Finch is guilty: True or False?
True (0.8175745039697023)
Ronald Finch is not guilty: True or False?
True (0.8311430831606665)
Ronald Finch has mean: True or False?
True (0.9039745373919651)
Ronald Finch has no mean: True or False?
True (0.6379335503198971)
Ronald Finch has motive: True or False?
True (0.8134607635851566)
Ronald Finch has no motive: True or False?
True (0.7924642605907138)
Ronald Finch has opportunity: True or False?
True (0.7937462383814009)
Ronald Finch has no opportunity: True or False?
True (0.6160122877297346)
Russell Winwood is guilty: True or False?
True (0.8944211616820568)
Russell Winwood is not guilty: True or False?
True (0.9184802773231918)
Russell Winwood has mean: True or False?
True (0.9537942396657707)
Russell Winwood has no mean: True or False?
True (0.8305941261447712)
Russell Winwood has motive: True or False?
True (0.9227612629515897)
Russell Winwood has no motive: True or False?
True (0.8423451152856819)
Russell Winwood has opportunity: True or False?
True (0.9329437018480795)
Russell Winwood has no opportunity: True or False?
True (0.7981867775042927)
### Edward Frates
- mean: False (0.3821414173816513)
- motive: False (0.24292326177964252)
- opportunity: False (0.42250459969866483)

### James Madigan
- mean: False (0.0)
- motive: False (0.16132026896779283)
- opportunity: False (0.326808330107765)

### Peter Zielny
- mean: True (0.7371581892031299)
- motive: True (0.743912876509037)
- opportunity: True (0.5992506595844092)

### Ronald Finch
- mean: False (0.36206644968010293)
- motive: False (0.20753573940928616)
- opportunity: False (0.3839877122702654)

### Russell Winwood
- mean: False (0.16940587385522876)
- motive: False (0.1576548847143181)
- opportunity: False (0.20181322249570732)

The culprit is Peter Zielny.
In fact, it is Russell Winwood.
## 5minutemystery-mystery-at-the-detectives-office
Joe the janitor is guilty: True or False?
True (0.9007918816809537)
Joe the janitor is not guilty: True or False?
True (0.9197146907380594)
Joe the janitor has mean: True or False?
True (0.8665848330592597)
Joe the janitor has no mean: True or False?
True (0.7602949226623019)
Joe the janitor has motive: True or False?
True (0.9352283459368647)
Joe the janitor has no motive: True or False?
True (0.7534666630720156)
Joe the janitor has opportunity: True or False?
True (0.9585765591512942)
Joe the janitor has no opportunity: True or False?
True (0.720171518230031)
Larry is guilty: True or False?
True (0.8198933606225757)
Larry is not guilty: True or False?
True (0.7655933544531522)
Larry has mean: True or False?
True (0.7570766705324253)
Larry has no mean: True or False?
True (0.6057990946577705)
Larry has motive: True or False?
True (0.8187367896794966)
Larry has no motive: True or False?
Map:  38%|███▊      | 77/203 [47:50<1:25:44, 40.83s/ examples]Map:  38%|███▊      | 78/203 [48:35<1:27:32, 42.02s/ examples]False (0.5078118305218892)
Larry has opportunity: True or False?
True (0.580352087772514)
Larry has no opportunity: True or False?
False (0.8116760258690822)
Mr. Jorgensen is guilty: True or False?
True (0.811974341286875)
Mr. Jorgensen is not guilty: True or False?
True (0.7409249009267298)
Mr. Jorgensen has mean: True or False?
True (0.7956581141325956)
Mr. Jorgensen has no mean: True or False?
True (0.7082125449089324)
Mr. Jorgensen has motive: True or False?
True (0.8169912043042492)
Mr. Jorgensen has no motive: True or False?
True (0.6817267588564826)
Mr. Jorgensen has opportunity: True or False?
True (0.612309626324874)
Mr. Jorgensen has no opportunity: True or False?
False (0.6740504382339836)
the building manager is guilty: True or False?
True (0.8778961263000082)
the building manager is not guilty: True or False?
True (0.8971558836279927)
the building manager has mean: True or False?
True (0.6566582306092376)
the building manager has no mean: True or False?
True (0.5156199352405011)
the building manager has motive: True or False?
True (0.7882573622725895)
the building manager has no motive: True or False?
True (0.8128672807499561)
the building manager has opportunity: True or False?
True (0.6951311179371613)
the building manager has no opportunity: True or False?
True (0.5727227727404994)
### Joe the janitor
- mean: False (0.23970507733769808)
- motive: False (0.2465333369279844)
- opportunity: False (0.279828481769969)

### Larry
- mean: True (0.7570766705324253)
- motive: True (0.8187367896794966)
- opportunity: True (0.580352087772514)

### Mr. Jorgensen
- mean: False (0.2917874550910676)
- motive: False (0.3182732411435174)
- opportunity: False (0.0)

### the building manager
- mean: False (0.4843800647594989)
- motive: False (0.18713271925004393)
- opportunity: False (0.42727722725950057)

The culprit is Larry.
In fact, it is the building manager.
## 5minutemystery-the-secret-in-the-old-trunk
Dennis Boyles is guilty: True or False?
True (0.7711548682745724)
Dennis Boyles is not guilty: True or False?
True (0.7117075978887988)
Dennis Boyles has mean: True or False?
True (0.8875948773562923)
Dennis Boyles has no mean: True or False?
False (0.6976089520497016)
Dennis Boyles has motive: True or False?
True (0.6575384105121485)
Dennis Boyles has no motive: True or False?
True (0.571766542860143)
Dennis Boyles has opportunity: True or False?
False (0.6791786560103119)
Dennis Boyles has no opportunity: True or False?
False (0.72758848510157)
George Boyles is guilty: True or False?
True (0.7947037743192802)
George Boyles is not guilty: True or False?
False (0.28082901588333525)
George Boyles has mean: True or False?
True (0.8283842201397164)
George Boyles has no mean: True or False?
False (0.6980207435948766)
George Boyles has motive: True or False?
True (0.7310586002437232)
George Boyles has no motive: True or False?
True (0.6113819501087365)
George Boyles has opportunity: True or False?
False (0.7217432334405754)
George Boyles has no opportunity: True or False?
False (0.6352224318508648)
John Boyles is guilty: True or False?
True (0.8303191093049147)
John Boyles is not guilty: True or False?
True (0.7106282704218558)
John Boyles has mean: True or False?
True (0.8354835531737983)
John Boyles has no mean: True or False?
False (0.5832033700118571)
John Boyles has motive: True or False?
True (0.7512834059294674)
John Boyles has no motive: True or False?
True (0.6610482284345209)
John Boyles has opportunity: True or False?
False (0.6774740084332073)
John Boyles has no opportunity: True or False?
False (0.6329566242340383)
Patricia (Trish) Boyles Sykes is guilty: True or False?
True (0.7745833916423246)
Patricia (Trish) Boyles Sykes is not guilty: True or False?
True (0.7122322217365102)
Patricia (Trish) Boyles Sykes has mean: True or False?
True (0.8596637847360897)
Patricia (Trish) Boyles Sykes has no mean: True or False?
True (0.5917232019857303)
Patricia (Trish) Boyles Sykes has motive: True or False?
True (0.673191669892235)
Patricia (Trish) Boyles Sykes has no motive: True or False?
True (0.7577943220037995)
Patricia (Trish) Boyles Sykes has opportunity: True or False?
True (0.5755880655791468)
Patricia (Trish) Boyles Sykes has no opportunity: True or False?
True (0.5156199352405011)
Patrick Boyles is guilty: True or False?
True (0.7086160238002551)
Patrick Boyles is not guilty: True or False?
True (0.6079520676700437)
Patrick Boyles has mean: True or False?
True (0.7786493288700866)
Patrick Boyles has no mean: True or False?
False (0.7490872087035162)
Patrick Boyles has motive: True or False?
True (0.5755879969637064)
Patrick Boyles has no motive: True or False?
False (0.5907791930117218)
Patrick Boyles has opportunity: True or False?
False (0.7704647687904915)
Patrick Boyles has no opportunity: True or False?
False (0.7352616086060775)
### Dennis Boyles
- mean: False (0.0)
- motive: False (0.42823345713985705)
- opportunity: False (0.6791786560103119)

### George Boyles
- mean: False (0.0)
- motive: False (0.3886180498912635)
- opportunity: False (0.7217432334405754)

### John Boyles
- mean: False (0.0)
- motive: False (0.33895177156547907)
- opportunity: False (0.6774740084332073)

### Patricia (Trish) Boyles Sykes
- mean: False (0.40827679801426975)
- motive: False (0.24220567799620052)
- opportunity: False (0.4843800647594989)

### Patrick Boyles
- mean: True (0.7786493288700866)
- motive: True (0.5755879969637064)
- opportunity: True (0.2647383913939225)

The culprit is Patrick Boyles.
In fact, it is Patrick Boyles.
## 5minutemystery-the-restless-ghost
Casey McCormick is guilty: True or False?
True (0.9210741501882456)
Casey McCormick is not guilty: True or False?
True (0.8762113474663927)
Casey McCormick has mean: True or False?
True (0.7154240000492645)
Casey McCormick has no mean: True or False?
False (0.6540113633452196)
Casey McCormick has motive: True or False?
True (0.8376200175313318)
Casey McCormick has no motive: True or False?
True (0.5794004215835179)
Casey McCormick has opportunity: True or False?
False (0.6279512069990912)
Casey McCormick has no opportunity: True or False?
False (0.7981867775042927)
Connie McCormick is guilty: True or False?
True (0.815232454829111)
Connie McCormick is not guilty: True or False?
True (0.7680380401429294)
Connie McCormick has mean: True or False?
True (0.814643384779728)
Connie McCormick has no mean: True or False?
True (0.5078118305218892)
Connie McCormick has motive: True or False?
True (0.847967740521315)
Connie McCormick has no motive: True or False?
False (0.5592900581575188)
Connie McCormick has opportunity: True or False?
False (0.6984322578436808)
Connie McCormick has no opportunity: True or False?
False (0.7431679939957333)
Ellen McCormick is guilty: True or False?
True (0.7287482572006113)
Ellen McCormick is not guilty: True or False?
True (0.6697448487720212)
Ellen McCormick has mean: True or False?
True (0.6671476389322356)
Ellen McCormick has no mean: True or False?
False (0.6334102859975052)
Ellen McCormick has motive: True or False?
True (0.6984323202883935)
Ellen McCormick has no motive: True or False?
False (0.5660185351323219)
Ellen McCormick has opportunity: True or False?
False (0.7520125537161032)
Ellen McCormick has no opportunity: True or False?
False (0.7356416038392981)
Michael McCormick, Jr. is guilty: True or False?
True (0.9078038309924442)
Michael McCormick, Jr. is not guilty: True or False?
True (0.8805918761155977)
Michael McCormick, Jr. has mean: True or False?
True (0.9388007508488514)
Michael McCormick, Jr. has no mean: True or False?
True (0.7461389980806673)
Michael McCormick, Jr. has motive: True or False?
True (0.9430336353172679)
Michael McCormick, Jr. has no motive: True or False?
True (0.7563574896543893)
Michael McCormick, Jr. has opportunity: True or False?
True (0.7138307093362539)
Michael McCormick, Jr. has no opportunity: True or False?
True (0.6909763109505791)
The ghost of Mike McCormick, Sr. is guilty: True or False?
True (0.8587185689177256)
The ghost of Mike McCormick, Sr. is not guilty: True or False?
True (0.8572908002249056)
The ghost of Mike McCormick, Sr. has mean: True or False?
True (0.8534248451958423)
Map:  39%|███▉      | 79/203 [49:21<1:29:41, 43.40s/ examples]Map:  39%|███▉      | 80/203 [49:52<1:20:57, 39.50s/ examples]Map:  40%|███▉      | 81/203 [51:24<1:52:49, 55.49s/ examples]The ghost of Mike McCormick, Sr. has no mean: True or False?
True (0.6557770400181139)
The ghost of Mike McCormick, Sr. has motive: True or False?
True (0.8638516611889259)
The ghost of Mike McCormick, Sr. has no motive: True or False?
True (0.7806625377756776)
The ghost of Mike McCormick, Sr. has opportunity: True or False?
True (0.6934729802503211)
The ghost of Mike McCormick, Sr. has no opportunity: True or False?
True (0.6627964381792564)
### Casey McCormick
- mean: False (0.0)
- motive: False (0.4205995784164821)
- opportunity: False (0.6279512069990912)

### Connie McCormick
- mean: False (0.49218816947811084)
- motive: False (0.0)
- opportunity: False (0.6984322578436808)

### Ellen McCormick
- mean: True (0.6671476389322356)
- motive: True (0.6984323202883935)
- opportunity: True (0.2643583961607019)

### Michael McCormick, Jr.
- mean: False (0.2538610019193327)
- motive: False (0.24364251034561069)
- opportunity: False (0.3090236890494209)

### The ghost of Mike McCormick, Sr.
- mean: False (0.3442229599818861)
- motive: False (0.21933746222432238)
- opportunity: False (0.3372035618207436)

The culprit is Ellen McCormick.
In fact, it is Casey McCormick.
## 5minutemystery-the-secret-friend
Bill Baker is guilty: True or False?
True (0.8152325155686644)
Bill Baker is not guilty: True or False?
True (0.8392075831473667)
Bill Baker has mean: True or False?
True (0.9640516654033661)
Bill Baker has no mean: True or False?
True (0.9038048413863352)
Bill Baker has motive: True or False?
True (0.8169911556077801)
Bill Baker has no motive: True or False?
True (0.702530072932436)
Bill Baker has opportunity: True or False?
True (0.7461389980806673)
Bill Baker has no opportunity: True or False?
True (0.5794004215835179)
Harold Coker is guilty: True or False?
True (0.9152045868398637)
Harold Coker is not guilty: True or False?
True (0.9063219998220023)
Harold Coker has mean: True or False?
True (0.9362850185952675)
Harold Coker has no mean: True or False?
True (0.8499711693725173)
Harold Coker has motive: True or False?
True (0.9121235591541035)
Harold Coker has no motive: True or False?
True (0.8086723099497763)
Harold Coker has opportunity: True or False?
True (0.9213575753967104)
Harold Coker has no opportunity: True or False?
True (0.7648916137833577)
Lyn Baker is guilty: True or False?
True (0.8238958672039278)
Lyn Baker is not guilty: True or False?
True (0.8044059309478723)
Lyn Baker has mean: True or False?
True (0.9509603994010378)
Lyn Baker has no mean: True or False?
True (0.8701565822173906)
Lyn Baker has motive: True or False?
True (0.9322068701708559)
Lyn Baker has no motive: True or False?
True (0.802555560073231)
Lyn Baker has opportunity: True or False?
True (0.8423451152856819)
Lyn Baker has no opportunity: True or False?
True (0.5370413742099674)
Midge Coker is guilty: True or False?
True (0.8875949368741688)
Midge Coker is not guilty: True or False?
True (0.8615382357584752)
Midge Coker has mean: True or False?
True (0.952397347230678)
Midge Coker has no mean: True or False?
True (0.9244151684978138)
Midge Coker has motive: True or False?
True (0.8568122940392877)
Midge Coker has no motive: True or False?
True (0.7490872087035162)
Midge Coker has opportunity: True or False?
True (0.8044059309478723)
Midge Coker has no opportunity: True or False?
True (0.5592900581575188)
### Bill Baker
- mean: True (0.9640516654033661)
- motive: True (0.8169911556077801)
- opportunity: True (0.7461389980806673)

### Harold Coker
- mean: False (0.15002883062748273)
- motive: False (0.19132769005022365)
- opportunity: False (0.23510838621664232)

### Lyn Baker
- mean: False (0.12984341778260944)
- motive: False (0.19744443992676897)
- opportunity: False (0.46295862579003255)

### Midge Coker
- mean: False (0.0755848315021862)
- motive: False (0.2509127912964838)
- opportunity: False (0.44070994184248125)

The culprit is Bill Baker.
In fact, it is Midge Coker.
## 5minutemystery-the-cross-homestead-mystery
Journal entry of Edith is guilty: True or False?
True (0.5973730125048408)
Journal entry of Edith is not guilty: True or False?
False (0.5983121871760707)
Journal entry of Edith has mean: True or False?
True (0.7563575572780217)
Journal entry of Edith has no mean: True or False?
True (0.5126925663186335)
Journal entry of Edith has motive: True or False?
True (0.5679366075542497)
Journal entry of Edith has no motive: True or False?
False (0.5851012033999957)
Journal entry of Edith has opportunity: True or False?
True (0.5448014304301324)
Journal entry of Edith has no opportunity: True or False?
False (0.6934729182490079)
Journal entry of Leonard is guilty: True or False?
False (0.6531269509188588)
Journal entry of Leonard is not guilty: True or False?
False (0.8423451152856819)
Journal entry of Leonard has mean: True or False?
True (0.8068526417769779)
Journal entry of Leonard has no mean: True or False?
True (0.5535053004623279)
Journal entry of Leonard has motive: True or False?
True (0.5869964306477841)
Journal entry of Leonard has no motive: True or False?
False (0.6469064916833258)
Journal entry of Leonard has opportunity: True or False?
True (0.5917232019857303)
Journal entry of Leonard has no opportunity: True or False?
False (0.7049732238008671)
Journal entry of Susie is guilty: True or False?
False (0.6842640081724978)
Journal entry of Susie is not guilty: True or False?
False (0.8019358443954961)
Journal entry of Susie has mean: True or False?
True (0.7732163648437078)
Journal entry of Susie has no mean: True or False?
True (0.5019531141001669)
Journal entry of Susie has motive: True or False?
True (0.5964331079469681)
Journal entry of Susie has no motive: True or False?
False (0.6388352560545881)
Journal entry of Susie has opportunity: True or False?
True (0.5438325284393795)
Journal entry of Susie has no opportunity: True or False?
False (0.7534666630720156)
Journal entry of Victor is guilty: True or False?
False (0.5263427467960875)
Journal entry of Victor is not guilty: True or False?
False (0.685107355950278)
Journal entry of Victor has mean: True or False?
True (0.8514594452543962)
Journal entry of Victor has no mean: True or False?
True (0.6619228707202935)
Journal entry of Victor has motive: True or False?
True (0.7025300310583819)
Journal entry of Victor has no motive: True or False?
False (0.5087881523495457)
Journal entry of Victor has opportunity: True or False?
True (0.6876299924560524)
Journal entry of Victor has no opportunity: True or False?
False (0.6001883860246252)
Journal entry of Wilbur is guilty: True or False?
False (0.5841525779336078)
Journal entry of Wilbur is not guilty: True or False?
False (0.7272012283179254)
Journal entry of Wilbur has mean: True or False?
True (0.7655933544531522)
Journal entry of Wilbur has no mean: True or False?
True (0.5573635130218721)
Journal entry of Wilbur has motive: True or False?
True (0.5312093625105829)
Journal entry of Wilbur has no motive: True or False?
False (0.5794004215835179)
Journal entry of Wilbur has opportunity: True or False?
True (0.5341265295318852)
Journal entry of Wilbur has no opportunity: True or False?
False (0.6791786560103119)
### Journal entry of Edith
- mean: False (0.48730743368136653)
- motive: False (0.0)
- opportunity: False (0.0)

### Journal entry of Leonard
- mean: False (0.44649469953767207)
- motive: False (0.0)
- opportunity: False (0.0)

### Journal entry of Susie
- mean: True (0.7732163648437078)
- motive: True (0.5964331079469681)
- opportunity: True (0.5438325284393795)

### Journal entry of Victor
- mean: False (0.33807712927970646)
- motive: False (0.0)
- opportunity: False (0.0)

### Journal entry of Wilbur
- mean: False (0.44263648697812785)
- motive: False (0.0)
- opportunity: False (0.0)

The culprit is Journal entry of Susie.
In fact, it is Journal entry of Leonard.
## 5minutemystery-is-it-a-wonderful-life
Dr. Gilchrest is guilty: True or False?
True (0.9122799654606127)
Dr. Gilchrest is not guilty: True or False?
False (0.46541615458717167)
Dr. Gilchrest has mean: True or False?
True (0.9181873182746905)
Dr. Gilchrest has no mean: True or False?
False (0.7405897166498082)
Dr. Gilchrest has motive: True or False?
Map:  40%|████      | 82/203 [52:00<1:39:45, 49.47s/ examples]Map:  41%|████      | 83/203 [52:43<1:35:09, 47.58s/ examples]Map:  41%|████▏     | 84/203 [53:13<1:24:00, 42.35s/ examples]True (0.884439109617765)
Dr. Gilchrest has no motive: True or False?
True (0.9551939353146309)
Dr. Gilchrest has opportunity: True or False?
True (0.8820219652716884)
Dr. Gilchrest has no opportunity: True or False?
True (0.8787311861857122)
Jonathan Cartright is guilty: True or False?
True (0.9147487268823872)
Jonathan Cartright is not guilty: True or False?
True (0.9192084645335399)
Jonathan Cartright has mean: True or False?
True (0.8980534699860239)
Jonathan Cartright has no mean: True or False?
True (0.8092759828926619)
Jonathan Cartright has motive: True or False?
True (0.8931230927421242)
Jonathan Cartright has no motive: True or False?
True (0.9158089188126235)
Jonathan Cartright has opportunity: True or False?
True (0.8314170225049837)
Jonathan Cartright has no opportunity: True or False?
True (0.7978719483468593)
Miser James Cartright (suicide) is guilty: True or False?
True (0.8482193926289605)
Miser James Cartright (suicide) is not guilty: True or False?
True (0.7997552678397243)
Miser James Cartright (suicide) has mean: True or False?
True (0.81197440178368)
Miser James Cartright (suicide) has no mean: True or False?
True (0.767341307978324)
Miser James Cartright (suicide) has motive: True or False?
True (0.869271276026005)
Miser James Cartright (suicide) has no motive: True or False?
True (0.8405209771392761)
Miser James Cartright (suicide) has opportunity: True or False?
True (0.8250265073476026)
Miser James Cartright (suicide) has no opportunity: True or False?
True (0.8529354946829077)
Moira Laurie is guilty: True or False?
True (0.9121235591541035)
Moira Laurie is not guilty: True or False?
True (0.9128255278379087)
Moira Laurie has mean: True or False?
True (0.8701565822173906)
Moira Laurie has no mean: True or False?
True (0.8224744844528368)
Moira Laurie has motive: True or False?
True (0.8719117627136385)
Moira Laurie has no motive: True or False?
True (0.9341553473346962)
Moira Laurie has opportunity: True or False?
True (0.8877896676652527)
Moira Laurie has no opportunity: True or False?
True (0.8591918406281239)
### Dr. Gilchrest
- mean: True (0.9181873182746905)
- motive: True (0.884439109617765)
- opportunity: True (0.8820219652716884)

### Jonathan Cartright
- mean: False (0.1907240171073381)
- motive: False (0.0841910811873765)
- opportunity: False (0.20212805165314074)

### Miser James Cartright (suicide)
- mean: False (0.232658692021676)
- motive: False (0.1594790228607239)
- opportunity: False (0.14706450531709225)

### Moira Laurie
- mean: False (0.17752551554716323)
- motive: False (0.06584465266530382)
- opportunity: False (0.14080815937187607)

The culprit is Dr. Gilchrest.
In fact, it is Moira Laurie.
## 5minutemystery-lestrade-solves-a-case
Archibald Hopkins is guilty: True or False?
True (0.8652240590801695)
Archibald Hopkins is not guilty: True or False?
True (0.8633916342942395)
Archibald Hopkins has mean: True or False?
True (0.9066531685310133)
Archibald Hopkins has no mean: True or False?
True (0.8519528492100928)
Archibald Hopkins has motive: True or False?
True (0.8914335992201801)
Archibald Hopkins has no motive: True or False?
True (0.7416740115009234)
Archibald Hopkins has opportunity: True or False?
True (0.8261514850267767)
Archibald Hopkins has no opportunity: True or False?
True (0.555435228101316)
Countess Mannerley is guilty: True or False?
True (0.7937461674149602)
Countess Mannerley is not guilty: True or False?
True (0.8692713407917644)
Countess Mannerley has mean: True or False?
True (0.8987665204865408)
Countess Mannerley has no mean: True or False?
True (0.7424216889954057)
Countess Mannerley has motive: True or False?
True (0.7431679939957333)
Countess Mannerley has no motive: True or False?
True (0.5879430860094185)
Countess Mannerley has opportunity: True or False?
True (0.6504672161860058)
Countess Mannerley has no opportunity: True or False?
False (0.6791787167336184)
Loralie Courtney is guilty: True or False?
True (0.8086723099497763)
Loralie Courtney is not guilty: True or False?
True (0.8250265073476026)
Loralie Courtney has mean: True or False?
True (0.9124361266596831)
Loralie Courtney has no mean: True or False?
True (0.784649255215384)
Loralie Courtney has motive: True or False?
True (0.767689835247798)
Loralie Courtney has no motive: True or False?
True (0.5409238971378262)
Loralie Courtney has opportunity: True or False?
True (0.7704647687904915)
Loralie Courtney has no opportunity: True or False?
False (0.591723272524637)
Robert Bannington is guilty: True or False?
True (0.8665847814067802)
Robert Bannington is not guilty: True or False?
True (0.8316905440184192)
Robert Bannington has mean: True or False?
True (0.9136765013387816)
Robert Bannington has no mean: True or False?
True (0.8688268116310761)
Robert Bannington has motive: True or False?
True (0.8755743533923891)
Robert Bannington has no motive: True or False?
True (0.7033457082786769)
Robert Bannington has opportunity: True or False?
True (0.8727816933272936)
Robert Bannington has no opportunity: True or False?
False (0.5321820387813727)
### Archibald Hopkins
- mean: False (0.14804715078990716)
- motive: False (0.2583259884990766)
- opportunity: False (0.44456477189868404)

### Countess Mannerley
- mean: False (0.2575783110045943)
- motive: False (0.41205691399058153)
- opportunity: False (0.0)

### Loralie Courtney
- mean: False (0.21535074478461602)
- motive: False (0.4590761028621738)
- opportunity: False (0.0)

### Robert Bannington
- mean: True (0.9136765013387816)
- motive: True (0.8755743533923891)
- opportunity: True (0.8727816933272936)

The culprit is Robert Bannington.
In fact, it is Robert Bannington.
## 5minutemystery-whole-stole-the-new-years-kiss
Danny is guilty: True or False?
True (0.7826625131049049)
Danny is not guilty: True or False?
True (0.8688267468984366)
Danny has mean: True or False?
True (0.8951566249612815)
Danny has no mean: True or False?
True (0.7745833916423246)
Danny has motive: True or False?
True (0.9690910565174785)
Danny has no motive: True or False?
True (0.8031737798924701)
Danny has opportunity: True or False?
True (0.8803863464576128)
Danny has no opportunity: True or False?
True (0.612309626324874)
Jeremy is guilty: True or False?
True (0.5321819753403337)
Jeremy is not guilty: True or False?
True (0.51464427676968)
Jeremy has mean: True or False?
True (0.8856315007226893)
Jeremy has no mean: True or False?
True (0.7348812840309261)
Jeremy has motive: True or False?
True (0.9599877610290866)
Jeremy has no motive: True or False?
True (0.6252093370817647)
Jeremy has opportunity: True or False?
True (0.7648916137833577)
Jeremy has no opportunity: True or False?
False (0.686790355176806)
RJ is guilty: True or False?
True (0.8992984268798617)
RJ is not guilty: True or False?
True (0.9130583993174167)
RJ has mean: True or False?
True (0.8955226517597132)
RJ has no mean: True or False?
True (0.8519528492100928)
RJ has motive: True or False?
True (0.9689150454184371)
RJ has no motive: True or False?
True (0.9260365949489886)
RJ has opportunity: True or False?
True (0.9010534302227574)
RJ has no opportunity: True or False?
True (0.5477060024984176)
Reese is guilty: True or False?
True (0.8104789202520752)
Reese is not guilty: True or False?
True (0.8679338050595715)
Reese has mean: True or False?
True (0.7981867775042927)
Reese has no mean: True or False?
True (0.7988152492192591)
Reese has motive: True or False?
True (0.9793540239608529)
Reese has no motive: True or False?
True (0.7025300310583819)
Reese has opportunity: True or False?
True (0.8745065279415651)
Reese has no opportunity: True or False?
False (0.5983121515138864)
### Danny
- mean: False (0.2254166083576754)
- motive: False (0.19682622010752993)
- opportunity: False (0.38769037367512604)

### Jeremy
- mean: False (0.2651187159690739)
- motive: False (0.37479066291823526)
- opportunity: False (0.0)

### RJ
- mean: False (0.14804715078990716)
- motive: False (0.0739634050510114)
- opportunity: False (0.4522939975015824)

### Reese
- mean: True (0.7981867775042927)
- motive: True (0.9793540239608529)
- opportunity: True (0.8745065279415651)

The culprit is Reese.
In fact, it is RJ.
Map:  42%|████▏     | 85/203 [53:51<1:20:52, 41.12s/ examples]Map:  42%|████▏     | 86/203 [54:23<1:14:21, 38.13s/ examples]## 5minutemystery-the-new-years-eve-mystery
Juanita Wade is guilty: True or False?
True (0.8670357473609658)
Juanita Wade is not guilty: True or False?
True (0.9102267057681164)
Juanita Wade has mean: True or False?
True (0.941654207327861)
Juanita Wade has no mean: True or False?
True (0.8000678954040312)
Juanita Wade has motive: True or False?
True (0.9241418261705818)
Juanita Wade has no motive: True or False?
True (0.9276260107813639)
Juanita Wade has opportunity: True or False?
True (0.9431384818142104)
Juanita Wade has no opportunity: True or False?
True (0.9334307932218529)
Mary Beth Sloan is guilty: True or False?
True (0.779321849347754)
Mary Beth Sloan is not guilty: True or False?
True (0.85729086409805)
Mary Beth Sloan has mean: True or False?
True (0.9577544910931239)
Mary Beth Sloan has no mean: True or False?
True (0.7634837587244478)
Mary Beth Sloan has motive: True or False?
True (0.9076402191395381)
Mary Beth Sloan has no motive: True or False?
True (0.8413047772878592)
Mary Beth Sloan has opportunity: True or False?
True (0.8762113474663927)
Mary Beth Sloan has no opportunity: True or False?
True (0.8795611817678315)
Noel King is guilty: True or False?
True (0.8812066389307215)
Noel King is not guilty: True or False?
True (0.9114953293645017)
Noel King has mean: True or False?
True (0.9566342225308191)
Noel King has no mean: True or False?
True (0.8464508054137014)
Noel King has motive: True or False?
True (0.9281487460975983)
Noel King has no motive: True or False?
True (0.8906751877407573)
Noel King has opportunity: True or False?
True (0.9396923783210908)
Noel King has no opportunity: True or False?
True (0.9355823382423648)
Roy Wade is guilty: True or False?
True (0.8844391689240307)
Roy Wade is not guilty: True or False?
True (0.9280183890155084)
Roy Wade has mean: True or False?
True (0.9383503780077049)
Roy Wade has no mean: True or False?
True (0.7240905804783984)
Roy Wade has motive: True or False?
True (0.883638264557296)
Roy Wade has no motive: True or False?
True (0.8879840376027315)
Roy Wade has opportunity: True or False?
True (0.927887794449634)
Roy Wade has no opportunity: True or False?
True (0.8807970337584357)
Theresa King is guilty: True or False?
True (0.9302050495103452)
Theresa King is not guilty: True or False?
True (0.9482504742145513)
Theresa King has mean: True or False?
True (0.9322068076615162)
Theresa King has no mean: True or False?
True (0.8998277786460391)
Theresa King has motive: True or False?
True (0.9396923783210908)
Theresa King has no motive: True or False?
True (0.9549004429672318)
Theresa King has opportunity: True or False?
True (0.9399133323582882)
Theresa King has no opportunity: True or False?
True (0.9641867858895684)
### Juanita Wade
- mean: False (0.19993210459596877)
- motive: False (0.07237398921863614)
- opportunity: False (0.06656920677814715)

### Mary Beth Sloan
- mean: False (0.23651624127555215)
- motive: False (0.15869522271214076)
- opportunity: False (0.12043881823216851)

### Noel King
- mean: False (0.15354919458629857)
- motive: False (0.10932481225924273)
- opportunity: False (0.06441766175763519)

### Roy Wade
- mean: False (0.27590941952160164)
- motive: False (0.11201596239726852)
- opportunity: False (0.11920296624156435)

### Theresa King
- mean: True (0.9322068076615162)
- motive: True (0.9396923783210908)
- opportunity: True (0.9399133323582882)

The culprit is Theresa King.
In fact, it is Mary Beth Sloan.
## 5minutemystery-the-twelfth-night-mystery
Balthasar is guilty: True or False?
True (0.8701565303520181)
Balthasar is not guilty: True or False?
True (0.9277570247163465)
Balthasar has mean: True or False?
True (0.9605096001181298)
Balthasar has no mean: True or False?
True (0.9339146041314464)
Balthasar has motive: True or False?
True (0.9207183689158278)
Balthasar has no motive: True or False?
True (0.8923751117531873)
Balthasar has opportunity: True or False?
True (0.8388118129178417)
Balthasar has no opportunity: True or False?
True (0.7302898714065358)
Caspar is guilty: True or False?
True (0.794384956668203)
Caspar is not guilty: True or False?
True (0.8723473540228537)
Caspar has mean: True or False?
True (0.911809984585868)
Caspar has no mean: True or False?
True (0.8469578019965)
Caspar has motive: True or False?
True (0.9368651509033574)
Caspar has no motive: True or False?
True (0.9022657265573043)
Caspar has opportunity: True or False?
True (0.9217811254507657)
Caspar has no opportunity: True or False?
True (0.7233094544266295)
Dad is guilty: True or False?
True (0.9703525306286271)
Dad is not guilty: True or False?
True (0.9820998904020126)
Dad has mean: True or False?
True (0.9460510011104621)
Dad has no mean: True or False?
True (0.9615337835163564)
Dad has motive: True or False?
True (0.9678081855801772)
Dad has no motive: True or False?
True (0.9815243480003819)
Dad has opportunity: True or False?
True (0.9606574760904091)
Dad has no opportunity: True or False?
True (0.9294403817764149)
Melchoir is guilty: True or False?
True (0.9017477662022706)
Melchoir is not guilty: True or False?
True (0.9354645001658318)
Melchoir has mean: True or False?
True (0.9324532728823121)
Melchoir has no mean: True or False?
True (0.8477157967479009)
Melchoir has motive: True or False?
True (0.9588086006815989)
Melchoir has no motive: True or False?
True (0.9220623362560066)
Melchoir has opportunity: True or False?
True (0.9408984174410038)
Melchoir has no opportunity: True or False?
True (0.7947037743192802)
### Balthasar
- mean: False (0.06608539586855355)
- motive: False (0.10762488824681271)
- opportunity: False (0.2697101285934642)

### Caspar
- mean: False (0.15304219800350005)
- motive: False (0.0977342734426957)
- opportunity: False (0.27669054557337047)

### Dad
- mean: True (0.9460510011104621)
- motive: True (0.9678081855801772)
- opportunity: True (0.9606574760904091)

### Melchoir
- mean: False (0.15228420325209913)
- motive: False (0.07793766374399336)
- opportunity: False (0.2052962256807198)

The culprit is Dad.
In fact, it is Caspar.
## 5minutemystery-sugar-lands-candy-crook
King Ted is guilty: True or False?
True (1.894016958997008)
King Ted is not guilty: True or False?
True (2.1083839024195745)
King Ted has mean: True or False?
True (1.405571817019633)
King Ted has no mean: True or False?
True (1.5617991396656214)
King Ted has motive: True or False?
True (1.6973194813725263)
King Ted has no motive: True or False?
True (0.9383574601758671)
King Ted has opportunity: True or False?
True (0.9054425934549756)
King Ted has no opportunity: True or False?
True (1.285785906737175)
Lancelot is guilty: True or False?
True (0.9167826786944403)
Lancelot is not guilty: True or False?
True (0.9337335830729522)
Lancelot has mean: True or False?
True (0.9139841191734227)
Lancelot has no mean: True or False?
True (0.907434332757697)
Lancelot has motive: True or False?
True (0.8594279851904003)
Lancelot has no motive: True or False?
True (0.8184467585979083)
Lancelot has opportunity: True or False?
True (0.8893367679552574)
Lancelot has no opportunity: True or False?
True (0.8341368378998062)
Pride is guilty: True or False?
True (1.0596613849072436)
Pride is not guilty: True or False?
True (1.5554796655144447)
Pride has mean: True or False?
True (1.2278680406317655)
Pride has no mean: True or False?
True (1.5769205083673918)
Pride has motive: True or False?
True (1.2808118266097692)
Pride has no motive: True or False?
True (1.6244790388262262)
Pride has opportunity: True or False?
True (0.9274290236011148)
Pride has no opportunity: True or False?
True (1.6599298120488488)
Rupert is guilty: True or False?
True (0.9307735574385115)
Rupert is not guilty: True or False?
True (1.3915557994956593)
Rupert has mean: True or False?
True (2.8285572852899734)
Rupert has no mean: True or False?
True (0.8971559437869847)
Rupert has motive: True or False?
True (0.9203612781944561)
Rupert has no motive: True or False?
True (0.9078854315215794)
Rupert has opportunity: True or False?
True (0.8399966422759665)
Rupert has no opportunity: True or False?
True (0.8467045433284847)
### King Ted
- mean: False (0.0)
- motive: False (0.061642539824132925)
Map:  43%|████▎     | 87/203 [55:05<1:15:56, 39.28s/ examples]Map:  43%|████▎     | 88/203 [56:06<1:27:58, 45.90s/ examples]Map:  44%|████▍     | 89/203 [57:07<1:36:03, 50.56s/ examples]- opportunity: False (0.0)

### Lancelot
- mean: False (0.09256566724230297)
- motive: False (0.18155324140209173)
- opportunity: False (0.1658631621001938)

### Pride
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.0)

### Rupert
- mean: True (2.8285572852899734)
- motive: True (0.9203612781944561)
- opportunity: True (0.8399966422759665)

The culprit is Rupert.
In fact, it is King Ted.
## 5minutemystery-what-the-dickensa-christmas-eve-mystery
Fagin is guilty: True or False?
False (2.979449943812823)
Fagin is not guilty: True or False?
False (2.5936930297109377)
Fagin has mean: True or False?
True (0.9121236203167563)
Fagin has no mean: True or False?
False (0.5847760518670571)
Fagin has motive: True or False?
True (0.8563323578093363)
Fagin has no motive: True or False?
False (0.6085086472546027)
Fagin has opportunity: True or False?
True (0.7898827135821628)
Fagin has no opportunity: True or False?
False (0.6113820047705449)
Nancy is guilty: True or False?
True (0.642432441257838)
Nancy is not guilty: True or False?
True (0.6714705301843162)
Nancy has mean: True or False?
True (0.6279512069990912)
Nancy has no mean: True or False?
False (0.5019531141001669)
Nancy has motive: True or False?
True (0.8333246107254184)
Nancy has no motive: True or False?
True (0.7279754274224494)
Nancy has opportunity: True or False?
True (0.7606506998655483)
Nancy has no opportunity: True or False?
True (0.5224458497983033)
Oliver Twist is guilty: True or False?
True (0.5926665645259142)
Oliver Twist is not guilty: True or False?
True (0.5312093625105829)
Oliver Twist has mean: True or False?
True (0.7634837587244478)
Oliver Twist has no mean: True or False?
False (0.60859406896259)
Oliver Twist has motive: True or False?
True (0.8169911556077801)
Oliver Twist has no motive: True or False?
False (0.5669777909748143)
Oliver Twist has opportunity: True or False?
True (0.5370413742099674)
Oliver Twist has no opportunity: True or False?
False (0.6926419789019715)
The Artful Dodger is guilty: True or False?
True (0.5563995964631269)
The Artful Dodger is not guilty: True or False?
True (0.5746334908651781)
The Artful Dodger has mean: True or False?
True (0.6934729802503211)
The Artful Dodger has no mean: True or False?
False (0.5992506595844092)
The Artful Dodger has motive: True or False?
True (0.6757646168022439)
The Artful Dodger has no motive: True or False?
False (0.5195212821349473)
The Artful Dodger has opportunity: True or False?
True (0.5409238971378262)
The Artful Dodger has no opportunity: True or False?
False (0.6315943123389512)
The Rich Gentleman is guilty: True or False?
True (0.7138307731576955)
The Rich Gentleman is not guilty: True or False?
True (0.7017130830397807)
The Rich Gentleman has mean: True or False?
True (0.8484706263347676)
The Rich Gentleman has no mean: True or False?
True (0.7461389980806673)
The Rich Gentleman has motive: True or False?
True (0.8459424357871997)
The Rich Gentleman has no motive: True or False?
True (0.6688802830862913)
The Rich Gentleman has opportunity: True or False?
True (0.6343168082332088)
The Rich Gentleman has no opportunity: True or False?
True (0.5331543669186894)
### Fagin
- mean: True (0.9121236203167563)
- motive: True (0.8563323578093363)
- opportunity: True (0.7898827135821628)

### Nancy
- mean: False (0.0)
- motive: False (0.27202457257755064)
- opportunity: False (0.47755415020169667)

### Oliver Twist
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.0)

### The Artful Dodger
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.0)

### The Rich Gentleman
- mean: False (0.2538610019193327)
- motive: False (0.3311197169137087)
- opportunity: False (0.46684563308131055)

The culprit is Fagin.
In fact, it is The Rich Gentleman.
## 5minutemystery-the-secret-santa-mystery
Al Busby is guilty: True or False?
True (0.8534248451958423)
Al Busby is not guilty: True or False?
True (0.8122724274380432)
Al Busby has mean: True or False?
True (0.7745833916423246)
Al Busby has no mean: True or False?
False (0.6361271113853048)
Al Busby has motive: True or False?
True (0.7394224480813394)
Al Busby has no motive: True or False?
True (0.6627964974378784)
Al Busby has opportunity: True or False?
False (0.6397360437814448)
Al Busby has no opportunity: True or False?
False (0.8187367896794966)
Bob (Bobby) Key is guilty: True or False?
True (0.893681109060862)
Bob (Bobby) Key is not guilty: True or False?
True (0.879146760693242)
Bob (Bobby) Key has mean: True or False?
True (0.6315943123389512)
Bob (Bobby) Key has no mean: True or False?
False (0.5669777909748143)
Bob (Bobby) Key has motive: True or False?
True (0.7453983509653428)
Bob (Bobby) Key has no motive: True or False?
True (0.5592900581575188)
Bob (Bobby) Key has opportunity: True or False?
True (0.7106282704218558)
Bob (Bobby) Key has no opportunity: True or False?
False (0.6757646168022439)
Chuck Daughtry is guilty: True or False?
True (0.8558511727823209)
Chuck Daughtry is not guilty: True or False?
True (0.8539127714046447)
Chuck Daughtry has mean: True or False?
True (0.8080671968507699)
Chuck Daughtry has no mean: True or False?
True (0.7333563569098757)
Chuck Daughtry has motive: True or False?
True (0.7585105966624085)
Chuck Daughtry has no motive: True or False?
True (0.6992544513448877)
Chuck Daughtry has opportunity: True or False?
True (0.5573634465789677)
Chuck Daughtry has no opportunity: True or False?
False (0.6315943123389512)
Jeff Reynolds is guilty: True or False?
True (0.878314250659373)
Jeff Reynolds is not guilty: True or False?
True (0.8479678036998373)
Jeff Reynolds has mean: True or False?
True (0.7272012283179254)
Jeff Reynolds has no mean: True or False?
True (0.5360700410935405)
Jeff Reynolds has motive: True or False?
True (0.7853085386591824)
Jeff Reynolds has no motive: True or False?
True (0.6918097672776748)
Jeff Reynolds has opportunity: True or False?
True (0.5832033700118571)
Jeff Reynolds has no opportunity: True or False?
False (0.7049732238008671)
Jim Dockery is guilty: True or False?
True (0.8499711693725173)
Jim Dockery is not guilty: True or False?
True (0.8311430831606665)
Jim Dockery has mean: True or False?
True (0.5888891269161294)
Jim Dockery has no mean: True or False?
False (0.7193836643711469)
Jim Dockery has motive: True or False?
True (0.6297745735138451)
Jim Dockery has no motive: True or False?
False (0.5360700410935405)
Jim Dockery has opportunity: True or False?
False (0.644225125126315)
Jim Dockery has no opportunity: True or False?
False (0.7956581141325956)
### Al Busby
- mean: False (0.0)
- motive: False (0.3372035025621216)
- opportunity: False (0.6397360437814448)

### Bob (Bobby) Key
- mean: True (0.6315943123389512)
- motive: True (0.7453983509653428)
- opportunity: True (0.7106282704218558)

### Chuck Daughtry
- mean: False (0.26664364309012434)
- motive: False (0.30074554865511227)
- opportunity: False (0.0)

### Jeff Reynolds
- mean: False (0.4639299589064595)
- motive: False (0.30819023272232515)
- opportunity: False (0.0)

### Jim Dockery
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.644225125126315)

The culprit is Bob (Bobby) Key.
In fact, it is Jim Dockery.
## 5minutemystery-the-silly-santa-mystery
Mr. Corrigan is guilty: True or False?
True (0.8441522053247883)
Mr. Corrigan is not guilty: True or False?
True (0.8630456978394889)
Mr. Corrigan has mean: True or False?
True (0.7337380571259766)
Mr. Corrigan has no mean: True or False?
True (0.5712882946833332)
Mr. Corrigan has motive: True or False?
False (0.4462024450672553)
Mr. Corrigan has no motive: True or False?
True (0.6356748948466111)
Mr. Corrigan has opportunity: True or False?
True (0.7074046739492601)
Mr. Corrigan has no opportunity: True or False?
False (0.5770187573434935)
Mrs. Martin is guilty: True or False?
True (0.9170058398600052)
Mrs. Martin is not guilty: True or False?
True (0.9225172426683277)
Mrs. Martin has mean: True or False?
True (0.8322367037050584)
Mrs. Martin has no mean: True or False?
True (0.708212608228071)
Mrs. Martin has motive: True or False?
True (0.84619676525883)
Mrs. Martin has no motive: True or False?
True (0.7620701143808404)Map:  44%|████▍     | 90/203 [57:58<1:35:08, 50.52s/ examples]Map:  45%|████▍     | 91/203 [58:35<1:26:54, 46.56s/ examples]Map:  45%|████▌     | 92/203 [59:11<1:20:18, 43.41s/ examples]
Mrs. Martin has opportunity: True or False?
True (0.8528129435683355)
Mrs. Martin has no opportunity: True or False?
True (0.60859406896259)
Santa Claus is guilty: True or False?
True (0.8775817123105901)
Santa Claus is not guilty: True or False?
True (0.8907702541910382)
Santa Claus has mean: True or False?
True (0.5258557890702972)
Santa Claus has no mean: True or False?
True (0.5083000145505756)
Santa Claus has motive: True or False?
True (0.779321849347754)
Santa Claus has no motive: True or False?
True (0.720171518230031)
Santa Claus has opportunity: True or False?
True (0.7588681623522538)
Santa Claus has no opportunity: True or False?
True (0.5664982807903216)
The photographer is guilty: True or False?
True (0.6951311179371613)
The photographer is not guilty: True or False?
True (0.8083699316700075)
The photographer has mean: True or False?
True (0.6757645563841816)
The photographer has no mean: True or False?
True (0.5224458497983033)
The photographer has motive: True or False?
True (0.7501869182201083)
The photographer has no motive: True or False?
True (0.6535692217898651)
The photographer has opportunity: True or False?
True (1.0680877473509556)
The photographer has no opportunity: True or False?
False (0.4949171477551284)
### Mr. Corrigan
- mean: False (0.4287117053166668)
- motive: False (0.4462024450672553)
- opportunity: False (0.0)

### Mrs. Martin
- mean: False (0.29178739177192903)
- motive: False (0.23792988561915962)
- opportunity: False (0.39140593103740995)

### Santa Claus
- mean: False (0.4916999854494244)
- motive: False (0.279828481769969)
- opportunity: False (0.4335017192096784)

### The photographer
- mean: True (0.6757645563841816)
- motive: True (0.7501869182201083)
- opportunity: True (1.0680877473509556)

The culprit is The photographer.
In fact, it is The photographer.
## 5minutemystery-sky-jack
Clem Duster is guilty: True or False?
True (0.8354835531737983)
Clem Duster is not guilty: True or False?
True (0.745398395394548)
Clem Duster has mean: True or False?
True (0.8044059309478723)
Clem Duster has no mean: True or False?
True (0.6315943123389512)
Clem Duster has motive: True or False?
True (0.8294919722593475)
Clem Duster has no motive: True or False?
True (0.8158201638039532)
Clem Duster has opportunity: True or False?
True (0.725648573585541)
Clem Duster has no opportunity: True or False?
True (0.6252093370817647)
Cliff Snelling is guilty: True or False?
True (0.8311430212356835)
Cliff Snelling is not guilty: True or False?
True (0.7424217332471881)
Cliff Snelling has mean: True or False?
True (0.8338664756137771)
Cliff Snelling has no mean: True or False?
True (0.6160122877297346)
Cliff Snelling has motive: True or False?
True (0.8665847814067802)
Cliff Snelling has no motive: True or False?
True (0.795340359502468)
Cliff Snelling has opportunity: True or False?
True (0.7620701143808404)
Cliff Snelling has no opportunity: True or False?
True (0.5535053004623279)
David Loftkiss is guilty: True or False?
True (0.811078188867804)
David Loftkiss is not guilty: True or False?
True (0.6654105788791005)
David Loftkiss has mean: True or False?
True (0.8360197583769845)
David Loftkiss has no mean: True or False?
True (0.5926665645259142)
David Loftkiss has motive: True or False?
True (0.8946054590684968)
David Loftkiss has no motive: True or False?
True (0.7078087894899847)
David Loftkiss has opportunity: True or False?
True (0.7008947664177184)
David Loftkiss has no opportunity: True or False?
False (0.525368812147771)
Tom Jenks is guilty: True or False?
True (0.8181563669811865)
Tom Jenks is not guilty: True or False?
True (0.7233095190955371)
Tom Jenks has mean: True or False?
True (0.811078188867804)
Tom Jenks has no mean: True or False?
True (0.5370414382302919)
Tom Jenks has motive: True or False?
True (0.8181563669811865)
Tom Jenks has no motive: True or False?
True (0.7416740115009234)
Tom Jenks has opportunity: True or False?
True (0.644225125126315)
Tom Jenks has no opportunity: True or False?
False (0.5774954003013352)
### Clem Duster
- mean: False (0.36840568766104875)
- motive: False (0.18417983619604683)
- opportunity: False (0.37479066291823526)

### Cliff Snelling
- mean: False (0.3839877122702654)
- motive: False (0.20465964049753205)
- opportunity: False (0.44649469953767207)

### David Loftkiss
- mean: False (0.40733343547408585)
- motive: False (0.2921912105100153)
- opportunity: False (0.0)

### Tom Jenks
- mean: True (0.811078188867804)
- motive: True (0.8181563669811865)
- opportunity: True (0.644225125126315)

The culprit is Tom Jenks.
In fact, it is Tom Jenks.
## 5minutemystery-dr-watson-and-the-thwarted-engagement
Georgette Pelham is guilty: True or False?
True (0.7527403228571042)
Georgette Pelham is not guilty: True or False?
True (0.7154240000492645)
Georgette Pelham has mean: True or False?
True (0.5851012033999957)
Georgette Pelham has no mean: True or False?
False (0.5660185688696566)
Georgette Pelham has motive: True or False?
False (0.6039318499573872)
Georgette Pelham has no motive: True or False?
False (0.5964331079469681)
Georgette Pelham has opportunity: True or False?
False (0.6934729182490079)
Georgette Pelham has no opportunity: True or False?
False (0.8392075331266983)
Reverend Marvin Ingalls is guilty: True or False?
True (0.8006919661398397)
Reverend Marvin Ingalls is not guilty: True or False?
True (0.7333564224770464)
Reverend Marvin Ingalls has mean: True or False?
True (0.8056321690561029)
Reverend Marvin Ingalls has no mean: True or False?
True (0.5126925663186335)
Reverend Marvin Ingalls has motive: True or False?
True (0.7264255794048772)
Reverend Marvin Ingalls has no motive: True or False?
True (0.5926665645259142)
Reverend Marvin Ingalls has opportunity: True or False?
False (0.5621765360769869)
Reverend Marvin Ingalls has no opportunity: True or False?
False (0.7627776774954688)
Sheila Ingalls is guilty: True or False?
True (0.7468781552484828)
Sheila Ingalls is not guilty: True or False?
True (0.743912876509037)
Sheila Ingalls has mean: True or False?
True (0.8283842201397164)
Sheila Ingalls has no mean: True or False?
True (0.5535053004623279)
Sheila Ingalls has motive: True or False?
True (0.6749080895533367)
Sheila Ingalls has no motive: True or False?
False (0.5282900215677746)
Sheila Ingalls has opportunity: True or False?
False (0.5350984235603058)
Sheila Ingalls has no opportunity: True or False?
False (0.7772998201448375)
Wallace Anders is guilty: True or False?
True (0.8413047772878592)
Wallace Anders is not guilty: True or False?
True (0.8213308436294358)
Wallace Anders has mean: True or False?
True (0.7017130830397807)
Wallace Anders has no mean: True or False?
True (0.6315943123389512)
Wallace Anders has motive: True or False?
True (0.6996649413792725)
Wallace Anders has no motive: True or False?
True (0.5486734660889085)
Wallace Anders has opportunity: True or False?
True (0.5832033352502285)
Wallace Anders has no opportunity: True or False?
False (0.7461389980806673)
### Georgette Pelham
- mean: False (0.0)
- motive: False (0.6039318499573872)
- opportunity: False (0.6934729182490079)

### Reverend Marvin Ingalls
- mean: False (0.48730743368136653)
- motive: False (0.40733343547408585)
- opportunity: False (0.5621765360769869)

### Sheila Ingalls
- mean: False (0.44649469953767207)
- motive: False (0.0)
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
Big George Ratcliffe is not guilty: True or False?
True (0.7833262669301256)
Big George Ratcliffe has mean: True or False?
True (0.9403530352223053)
Big George Ratcliffe has no mean: True or False?
True (0.7025300310583819)
Big George Ratcliffe has motive: True or False?
True (0.8895288719962232)
Big George Ratcliffe has no motive: True or False?
True (0.8104788598666923)
Big George Ratcliffe has opportunity: True or False?
True (0.8701565822173906)
Map:  46%|████▌     | 93/203 [59:47<1:15:37, 41.25s/ examples]Map:  46%|████▋     | 94/203 [1:00:25<1:12:48, 40.08s/ examples]Big George Ratcliffe has no opportunity: True or False?
True (0.8204694405411458)
Chester Morris is guilty: True or False?
True (0.9063219998220023)
Chester Morris is not guilty: True or False?
True (0.8344068526674736)
Chester Morris has mean: True or False?
True (0.9152045868398637)
Chester Morris has no mean: True or False?
True (0.6645403391983984)
Chester Morris has motive: True or False?
True (0.8951566249612815)
Chester Morris has no motive: True or False?
True (0.8438951328214825)
Chester Morris has opportunity: True or False?
True (0.832781310996106)
Chester Morris has no opportunity: True or False?
True (0.7981867775042927)
Joe Franklin is guilty: True or False?
True (0.9286679635448885)
Joe Franklin is not guilty: True or False?
True (0.8474634858439474)
Joe Franklin has mean: True or False?
True (0.9314625284362855)
Joe Franklin has no mean: True or False?
True (0.7256486384635821)
Joe Franklin has motive: True or False?
True (0.9511421913058572)
Joe Franklin has no motive: True or False?
True (0.8705973031072073)
Joe Franklin has opportunity: True or False?
True (0.9010534302227574)
Joe Franklin has no opportunity: True or False?
True (0.8275496386126701)
Slim Jameson is guilty: True or False?
True (0.9235923286659299)
Slim Jameson is not guilty: True or False?
True (0.8524448242555318)
Slim Jameson has mean: True or False?
True (0.927099763868178)
Slim Jameson has no mean: True or False?
True (0.7325918054337844)
Slim Jameson has motive: True or False?
True (0.9031234959323464)
Slim Jameson has no motive: True or False?
True (0.8770561879413864)
Slim Jameson has opportunity: True or False?
True (0.8193157317863493)
Slim Jameson has no opportunity: True or False?
True (0.7969254269662895)
### Big George Ratcliffe
- mean: False (0.29746996894161815)
- motive: False (0.18952114013330768)
- opportunity: False (0.1795305594588542)

### Chester Morris
- mean: False (0.3354596608016016)
- motive: False (0.15610486717851746)
- opportunity: False (0.20181322249570732)

### Joe Franklin
- mean: False (0.2743513615364179)
- motive: False (0.1294026968927927)
- opportunity: False (0.17245036138732994)

### Slim Jameson
- mean: True (0.927099763868178)
- motive: True (0.9031234959323464)
- opportunity: True (0.8193157317863493)

The culprit is Slim Jameson.
In fact, it is Slim Jameson.
## 5minutemystery-the-mystery-of-the-american-raid
Admiral Taro is guilty: True or False?
False (0.5175709123121337)
Admiral Taro is not guilty: True or False?
False (0.729905005312225)
Admiral Taro has mean: True or False?
True (0.7752647497229632)
Admiral Taro has no mean: True or False?
False (0.7541915688671895)
Admiral Taro has motive: True or False?
True (0.6918097672776748)
Admiral Taro has no motive: True or False?
False (0.6610481693322063)
Admiral Taro has opportunity: True or False?
True (0.5219585151310108)
Admiral Taro has no opportunity: True or False?
False (0.6469064916833258)
Gina is guilty: True or False?
True (0.6714705301843162)
Gina is not guilty: True or False?
True (0.8175745039697023)
Gina has mean: True or False?
True (0.7853085971692302)
Gina has no mean: True or False?
False (0.5185462156586879)
Gina has motive: True or False?
True (0.7908535601223919)
Gina has no motive: True or False?
True (0.621540893468236)
Gina has opportunity: True or False?
True (0.8134608241927087)
Gina has no opportunity: True or False?
True (0.6361271113853048)
Kira is guilty: True or False?
True (0.6039318499573872)
Kira is not guilty: True or False?
True (0.7302898714065358)
Kira has mean: True or False?
True (0.5621765360769869)
Kira has no mean: True or False?
False (0.685107355950278)
Kira has motive: True or False?
True (0.8247443993706964)
Kira has no motive: True or False?
False (0.6433292707767855)
Kira has opportunity: True or False?
True (0.8464508054137014)
Kira has no opportunity: True or False?
True (0.5087881523495457)
The Emperor is guilty: True or False?
True (0.9170058945178141)
The Emperor is not guilty: True or False?
True (0.9340350654042096)
The Emperor has mean: True or False?
True (0.8984105603938967)
The Emperor has no mean: True or False?
True (0.8499711693725173)
The Emperor has motive: True or False?
True (0.7606506998655483)
The Emperor has no motive: True or False?
True (0.7627776774954688)
The Emperor has opportunity: True or False?
True (0.7275885284692245)
The Emperor has no opportunity: True or False?
True (0.7041600870830834)
### Admiral Taro
- mean: True (0.7752647497229632)
- motive: True (0.6918097672776748)
- opportunity: True (0.5219585151310108)

### Gina
- mean: False (0.0)
- motive: False (0.37845910653176396)
- opportunity: False (0.36387288861469524)

### Kira
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.49121184765045434)

### The Emperor
- mean: False (0.15002883062748273)
- motive: False (0.23722232250453124)
- opportunity: False (0.2958399129169166)

The culprit is Admiral Taro.
In fact, it is Admiral Taro.
## 5minutemystery-the-missing-ornament-mystery
Jackie Hadley is guilty: True or False?
True (0.9014011626580862)
Jackie Hadley is not guilty: True or False?
True (0.6880493654830329)
Jackie Hadley has mean: True or False?
True (0.9731388097113137)
Jackie Hadley has no mean: True or False?
True (0.6976089520497016)
Jackie Hadley has motive: True or False?
True (0.9589241138134527)
Jackie Hadley has no motive: True or False?
True (0.745398395394548)
Jackie Hadley has opportunity: True or False?
True (0.8649961307471897)
Jackie Hadley has no opportunity: True or False?
True (0.7053792507760227)
Lennie Hadley is guilty: True or False?
True (0.952397407545942)
Lennie Hadley is not guilty: True or False?
True (0.8543993851297865)
Lennie Hadley has mean: True or False?
True (0.9575961815839735)
Lennie Hadley has no mean: True or False?
True (0.7229183995281547)
Lennie Hadley has motive: True or False?
True (0.9799765949220004)
Lennie Hadley has no motive: True or False?
True (0.7606506998655483)
Lennie Hadley has opportunity: True or False?
True (0.9291837815043049)
Lennie Hadley has no opportunity: True or False?
True (0.7620700689579233)
Mike Hadley is guilty: True or False?
True (0.947962222968318)
Mike Hadley is not guilty: True or False?
True (0.8227594449669557)
Mike Hadley has mean: True or False?
True (0.9777987599607383)
Mike Hadley has no mean: True or False?
True (0.7697732451157533)
Mike Hadley has motive: True or False?
True (0.9819792515812888)
Mike Hadley has no motive: True or False?
True (0.7725306828324007)
Mike Hadley has opportunity: True or False?
True (0.9413853274043543)
Mike Hadley has no opportunity: True or False?
True (0.7476159279883341)
Sandy Hadley is guilty: True or False?
True (0.920789721359066)
Sandy Hadley is not guilty: True or False?
True (0.6486889055472267)
Sandy Hadley has mean: True or False?
True (0.8895288719962232)
Sandy Hadley has no mean: True or False?
True (0.5650587803792624)
Sandy Hadley has motive: True or False?
True (0.971019387667922)
Sandy Hadley has no motive: True or False?
True (0.7025300310583819)
Sandy Hadley has opportunity: True or False?
True (0.8137569459807168)
Sandy Hadley has no opportunity: True or False?
True (0.5506073202694327)
Tommy Hadley is guilty: True or False?
True (0.954477967000386)
Tommy Hadley is not guilty: True or False?
True (0.8253083182831968)
Tommy Hadley has mean: True or False?
True (0.9667888295116236)
Tommy Hadley has no mean: True or False?
True (0.6662796746479285)
Tommy Hadley has motive: True or False?
True (0.9912208913804552)
Tommy Hadley has no motive: True or False?
True (0.8122723669190336)
Tommy Hadley has opportunity: True or False?
True (0.9774139529645163)
Tommy Hadley has no opportunity: True or False?
True (0.9390248079664695)
### Jackie Hadley
- mean: False (0.30239104795029836)
- motive: False (0.254601604605452)
- opportunity: False (0.2946207492239773)

### Lennie Hadley
- mean: False (0.27708160047184527)
- motive: False (0.23934930013445166)
- opportunity: False (0.23792993104207671)

### Mike Hadley
- mean: False (0.2302267548842467)
- motive: False (0.22746931716759933)
- opportunity: False (0.2523840720116659)

### Sandy Hadley
- mean: False (0.4349412196207376)
Map:  47%|████▋     | 95/203 [1:01:03<1:11:14, 39.58s/ examples]Map:  47%|████▋     | 96/203 [1:01:41<1:09:25, 38.93s/ examples]Map:  48%|████▊     | 97/203 [1:02:10<1:03:40, 36.04s/ examples]- motive: False (0.29746996894161815)
- opportunity: False (0.4493926797305673)

### Tommy Hadley
- mean: True (0.9667888295116236)
- motive: True (0.9912208913804552)
- opportunity: True (0.9774139529645163)

The culprit is Tommy Hadley.
In fact, it is Lennie Hadley.
## 5minutemystery-the-pilgrim-thanksgiving-puzzle
John Alden is guilty: True or False?
True (0.878314250659373)
John Alden is not guilty: True or False?
True (0.8799743689174987)
John Alden has mean: True or False?
True (0.9026095892260383)
John Alden has no mean: True or False?
True (0.5282900845448565)
John Alden has motive: True or False?
True (0.7839884808423031)
John Alden has no motive: True or False?
True (0.6361271113853048)
John Alden has opportunity: True or False?
False (0.5660185688696566)
John Alden has no opportunity: True or False?
False (0.7379143332111532)
Miles Standish is guilty: True or False?
True (0.9295683483415352)
Miles Standish is not guilty: True or False?
True (0.9196425651151865)
Miles Standish has mean: True or False?
True (0.8563323578093363)
Miles Standish has no mean: True or False?
False (0.5156199352405011)
Miles Standish has motive: True or False?
True (0.8289387819824735)
Miles Standish has no motive: True or False?
True (0.7725306828324007)
Miles Standish has opportunity: True or False?
True (0.6825736720802238)
Miles Standish has no opportunity: True or False?
False (0.5544704821687028)
Priscilla Mulllins is guilty: True or False?
True (0.8376200175313318)
Priscilla Mulllins is not guilty: True or False?
True (0.7599387683150569)
Priscilla Mulllins has mean: True or False?
True (0.9043130884593419)
Priscilla Mulllins has no mean: True or False?
True (0.7082125449089324)
Priscilla Mulllins has motive: True or False?
True (0.6406358487498992)
Priscilla Mulllins has no motive: True or False?
True (0.5612147992901458)
Priscilla Mulllins has opportunity: True or False?
True (0.5224457875179084)
Priscilla Mulllins has no opportunity: True or False?
False (0.7911764307711107)
William Bradford is guilty: True or False?
True (0.7233095190955371)
William Bradford is not guilty: True or False?
True (0.7431679939957333)
William Bradford has mean: True or False?
True (0.8080671968507699)
William Bradford has no mean: True or False?
False (0.5428632463719839)
William Bradford has motive: True or False?
True (0.6288633913849659)
William Bradford has no motive: True or False?
True (0.5126925663186335)
William Bradford has opportunity: True or False?
False (0.6967841871600284)
William Bradford has no opportunity: True or False?
False (0.776622945813876)
### John Alden
- mean: False (0.4717099154551435)
- motive: False (0.36387288861469524)
- opportunity: False (0.5660185688696566)

### Miles Standish
- mean: True (0.8563323578093363)
- motive: True (0.8289387819824735)
- opportunity: True (0.6825736720802238)

### Priscilla Mulllins
- mean: False (0.2917874550910676)
- motive: False (0.43878520070985416)
- opportunity: False (0.0)

### William Bradford
- mean: False (0.0)
- motive: False (0.48730743368136653)
- opportunity: False (0.6967841871600284)

The culprit is Miles Standish.
In fact, it is John Alden.
## 5minutemystery-the-disappearing-turkey
Darby is guilty: True or False?
True (0.7490872087035162)
Darby is not guilty: True or False?
True (0.8210441512234701)
Darby has mean: True or False?
True (0.6406358487498992)
Darby has no mean: True or False?
False (0.7074046739492601)
Darby has motive: True or False?
True (0.8278281666221954)
Darby has no motive: True or False?
True (0.6297745735138451)
Darby has opportunity: True or False?
True (0.6662796746479285)
Darby has no opportunity: True or False?
False (0.7017130830397807)
Father is guilty: True or False?
True (0.9615337835163564)
Father is not guilty: True or False?
True (0.9803186062785318)
Father has mean: True or False?
True (0.77729988964086)
Father has no mean: True or False?
True (0.8543993851297865)
Father has motive: True or False?
True (0.9099069836112468)
Father has no motive: True or False?
True (0.927887794449634)
Father has opportunity: True or False?
True (0.6584175136252488)
Father has no opportunity: True or False?
False (0.5917232019857303)
Greg is guilty: True or False?
True (0.8998277786460391)
Greg is not guilty: True or False?
True (0.9381240005131491)
Greg has mean: True or False?
True (0.7859664553110391)
Greg has no mean: True or False?
True (0.7711548223101617)
Greg has motive: True or False?
True (0.9046505126460354)
Greg has no motive: True or False?
True (0.794384956668203)
Greg has opportunity: True or False?
True (0.7655933544531522)
Greg has no opportunity: True or False?
False (0.5457699766832048)
Uncle Larry is guilty: True or False?
True (0.9299510095943111)
Uncle Larry is not guilty: True or False?
True (0.9405717864730483)
Uncle Larry has mean: True or False?
True (0.8661325012437474)
Uncle Larry has no mean: True or False?
True (0.7898827135821628)
Uncle Larry has motive: True or False?
True (0.911809923444246)
Uncle Larry has no motive: True or False?
True (0.9294403817764149)
Uncle Larry has opportunity: True or False?
True (0.8255897087847518)
Uncle Larry has no opportunity: True or False?
True (0.5380124470448935)
### Darby
- mean: True (0.6406358487498992)
- motive: True (0.8278281666221954)
- opportunity: True (0.6662796746479285)

### Father
- mean: False (0.14560061487021347)
- motive: False (0.07211220555036602)
- opportunity: False (0.0)

### Greg
- mean: False (0.22884517768983825)
- motive: False (0.20561504333179703)
- opportunity: False (0.0)

### Uncle Larry
- mean: False (0.21011728641783722)
- motive: False (0.07055961822358514)
- opportunity: False (0.4619875529551065)

The culprit is Darby.
In fact, it is Father.
## 5minutemystery-a-thanksgiving-mystery-poem
Libby is guilty: True or False?
True (0.9217811254507657)
Libby is not guilty: True or False?
True (0.9307106123564625)
Libby has mean: True or False?
True (0.8697145551802641)
Libby has no mean: True or False?
True (0.8633916342942395)
Libby has motive: True or False?
True (0.9197868083117009)
Libby has no motive: True or False?
True (0.9048188910591489)
Libby has opportunity: True or False?
True (0.8710367026584496)
Libby has no opportunity: True or False?
True (0.8244619332958376)
Rusty is guilty: True or False?
True (0.8866169426295919)
Rusty is not guilty: True or False?
True (1.1820830931532942)
Rusty has mean: True or False?
True (1.357561222574218)
Rusty has no mean: True or False?
True (1.2211543163108616)
Rusty has motive: True or False?
True (1.3169100678433772)
Rusty has no motive: True or False?
True (0.833324548637899)
Rusty has opportunity: True or False?
True (0.7962924854830264)
Rusty has no opportunity: True or False?
True (0.7585105966624085)
Tiny is guilty: True or False?
True (1.582669490054393)
Tiny is not guilty: True or False?
True (2.1356244393478088)
Tiny has mean: True or False?
True (1.156026542411078)
Tiny has no mean: True or False?
True (1.289058518190761)
Tiny has motive: True or False?
True (1.3789815370569487)
Tiny has no motive: True or False?
True (0.8961499146099512)
Tiny has opportunity: True or False?
True (0.7969253675907205)
Tiny has no opportunity: True or False?
True (0.7669925046333297)
Tom is guilty: True or False?
True (0.8517062701455038)
Tom is not guilty: True or False?
True (0.8608377628023384)
Tom has mean: True or False?
True (0.7122322217365102)
Tom has no mean: True or False?
True (0.7556369876990674)
Tom has motive: True or False?
True (0.8071567377359422)
Tom has no motive: True or False?
True (0.8000678954040312)
Tom has opportunity: True or False?
True (0.7302898714065358)
Tom has no opportunity: True or False?
True (0.7333563569098757)
### Libby
- mean: False (0.13660836570576051)
- motive: False (0.09518110894085108)
- opportunity: False (0.1755380667041624)

### Rusty
- mean: True (1.357561222574218)
- motive: True (1.3169100678433772)
- opportunity: True (0.7962924854830264)

### Tiny
- mean: False (0.0)
- motive: False (0.10385008539004881)
- opportunity: False (0.23300749536667031)

### Tom
- mean: False (0.2443630123009326)
- motive: False (0.19993210459596877)
- opportunity: False (0.26664364309012434)

Map:  48%|████▊     | 98/203 [1:02:44<1:02:00, 35.43s/ examples]Map:  49%|████▉     | 99/203 [1:03:18<1:00:33, 34.94s/ examples]Map:  49%|████▉     | 100/203 [1:03:48<57:34, 33.54s/ examples] Map:  50%|████▉     | 101/203 [1:04:19<55:36, 32.71s/ examples]The culprit is Rusty.
In fact, it is Rusty.
## 5minutemystery-turkey-cull
Beaker is guilty: True or False?
True (0.8062431235779619)
Beaker is not guilty: True or False?
True (0.7786493288700866)
Beaker has mean: True or False?
True (0.7669924589170153)
Beaker has no mean: True or False?
True (0.5204963206682631)
Beaker has motive: True or False?
True (0.9491062747098069)
Beaker has no motive: True or False?
True (0.8134608241927087)
Beaker has opportunity: True or False?
True (0.7008948290825966)
Beaker has no opportunity: True or False?
True (0.5486734660889085)
Beau is guilty: True or False?
True (0.8204693794114111)
Beau is not guilty: True or False?
True (0.8591918406281239)
Beau has mean: True or False?
True (0.8778961263000082)
Beau has no mean: True or False?
True (0.7446563751413027)
Beau has motive: True or False?
True (0.9545627850600183)
Beau has no motive: True or False?
True (0.8428631416381634)
Beau has opportunity: True or False?
True (0.8895288719962232)
Beau has no opportunity: True or False?
True (0.6984322578436808)
Leaf is guilty: True or False?
True (0.8697145551802641)
Leaf is not guilty: True or False?
True (0.8098781635062345)
Leaf has mean: True or False?
True (0.8074606715677252)
Leaf has no mean: True or False?
False (0.5009765603034438)
Leaf has motive: True or False?
True (0.8638516611889259)
Leaf has no motive: True or False?
True (0.7549149897594328)
Leaf has opportunity: True or False?
True (0.7766228995235426)
Leaf has no opportunity: True or False?
True (0.566977858563838)
Red is guilty: True or False?
True (0.7549149897594328)
Red is not guilty: True or False?
True (0.6610482284345209)
Red has mean: True or False?
True (0.8397339530959691)
Red has no mean: True or False?
True (0.5486734987923966)
Red has motive: True or False?
True (0.9170058945178141)
Red has no motive: True or False?
True (0.7872777601997338)
Red has opportunity: True or False?
True (0.7185943809170431)
Red has no opportunity: True or False?
True (0.5009765603034438)
### Beaker
- mean: False (0.4795036793317369)
- motive: False (0.1865391758072913)
- opportunity: False (0.45132653391109145)

### Beau
- mean: False (0.2553436248586973)
- motive: False (0.15713685836183655)
- opportunity: False (0.3015677421563192)

### Leaf
- mean: True (0.8074606715677252)
- motive: True (0.8638516611889259)
- opportunity: True (0.7766228995235426)

### Red
- mean: False (0.4513265012076034)
- motive: False (0.21272223980026617)
- opportunity: False (0.49902343969655616)

The culprit is Leaf.
In fact, it is Beau.
## 5minutemystery-a-turkey-day-struggle
Aunt Rachel is guilty: True or False?
True (0.686790355176806)
Aunt Rachel is not guilty: True or False?
True (0.6834194581047349)
Aunt Rachel has mean: True or False?
True (0.7527403228571042)
Aunt Rachel has no mean: True or False?
True (0.5350984235603058)
Aunt Rachel has motive: True or False?
True (0.7826624547920057)
Aunt Rachel has no motive: True or False?
True (0.6504672743423094)
Aunt Rachel has opportunity: True or False?
True (0.5273165068094335)
Aunt Rachel has no opportunity: True or False?
False (0.6774740084332073)
Chris is guilty: True or False?
True (0.740174341079517)
Chris is not guilty: True or False?
True (0.802555560073231)
Chris has mean: True or False?
True (0.9099069836112468)
Chris has no mean: True or False?
True (0.7826624547920057)
Chris has motive: True or False?
True (0.9294403817764149)
Chris has no motive: True or False?
True (0.7577943897558946)
Chris has opportunity: True or False?
True (0.844921525814193)
Chris has no opportunity: True or False?
False (0.5019531141001669)
Diane is guilty: True or False?
True (0.7185943809170431)
Diane is not guilty: True or False?
True (0.7364006034245382)
Diane has mean: True or False?
True (0.8238958672039278)
Diane has no mean: True or False?
True (0.6057990946577705)
Diane has motive: True or False?
True (0.8933094122075369)
Diane has no motive: True or False?
True (0.7833262085677729)
Diane has opportunity: True or False?
True (0.7041601500399041)
Diane has no opportunity: True or False?
False (0.6095241816115718)
Jack the Dog is guilty: True or False?
True (0.8250265073476026)
Jack the Dog is not guilty: True or False?
True (0.7981867775042927)
Jack the Dog has mean: True or False?
True (0.8652240590801695)
Jack the Dog has no mean: True or False?
True (0.7431679939957333)
Jack the Dog has motive: True or False?
True (0.9193533657123177)
Jack the Dog has no motive: True or False?
True (0.6169358476670045)
Jack the Dog has opportunity: True or False?
True (0.8227594449669557)
Jack the Dog has no opportunity: True or False?
True (0.6095241271158658)
### Aunt Rachel
- mean: False (0.4649015764396942)
- motive: False (0.34953272565769056)
- opportunity: False (0.0)

### Chris
- mean: False (0.2173375452079943)
- motive: False (0.24220561024410536)
- opportunity: False (0.0)

### Diane
- mean: True (0.8238958672039278)
- motive: True (0.8933094122075369)
- opportunity: True (0.7041601500399041)

### Jack the Dog
- mean: False (0.2568320060042667)
- motive: False (0.3830641523329955)
- opportunity: False (0.3904758728841342)

The culprit is Diane.
In fact, it is Chris.
## 5minutemystery-the-missing-briefcase
Porter 1 is guilty: True or False?
True (0.8006919661398397)
Porter 1 is not guilty: True or False?
True (0.7599387683150569)
Porter 1 has mean: True or False?
True (0.861071588244826)
Porter 1 has no mean: True or False?
True (0.6575384693006662)
Porter 1 has motive: True or False?
True (0.8697145551802641)
Porter 1 has no motive: True or False?
True (0.7364006034245382)
Porter 1 has opportunity: True or False?
True (0.8227595062673136)
Porter 1 has no opportunity: True or False?
True (0.7599387683150569)
Porter 2 is guilty: True or False?
True (0.8000678954040312)
Porter 2 is not guilty: True or False?
True (0.7662936378892937)
Porter 2 has mean: True or False?
True (0.8665847814067802)
Porter 2 has no mean: True or False?
True (0.6808786440630326)
Porter 2 has motive: True or False?
True (0.9329437018480795)
Porter 2 has no motive: True or False?
True (0.64779823427608)
Porter 2 has opportunity: True or False?
True (0.925499741040984)
Porter 2 has no opportunity: True or False?
True (0.7541915239138703)
Porter 3 is guilty: True or False?
True (0.8294920340613177)
Porter 3 is not guilty: True or False?
True (0.7648916137833577)
Porter 3 has mean: True or False?
True (0.9001793304600783)
Porter 3 has no mean: True or False?
True (0.7725306828324007)
Porter 3 has motive: True or False?
True (0.9422947179693436)
Porter 3 has no motive: True or False?
True (0.7379143332111532)
Porter 3 has opportunity: True or False?
True (0.9485372300670596)
Porter 3 has no opportunity: True or False?
True (0.7806624796117883)
Porter 4 is guilty: True or False?
True (0.8745065279415651)
Porter 4 is not guilty: True or False?
True (0.8092759828926619)
Porter 4 has mean: True or False?
True (0.8984105603938967)
Porter 4 has no mean: True or False?
True (0.6901415551283886)
Porter 4 has motive: True or False?
True (0.8944211616820568)
Porter 4 has no motive: True or False?
True (0.6636689828419103)
Porter 4 has opportunity: True or False?
True (0.9105454073245608)
Porter 4 has no opportunity: True or False?
True (0.7348812840309261)
### Porter 1
- mean: True (0.861071588244826)
- motive: True (0.8697145551802641)
- opportunity: True (0.8227595062673136)

### Porter 2
- mean: False (0.31912135593696744)
- motive: False (0.35220176572392004)
- opportunity: False (0.24580847608612966)

### Porter 3
- mean: False (0.22746931716759933)
- motive: False (0.2620856667888468)
- opportunity: False (0.21933752038821175)

### Porter 4
- mean: False (0.3098584448716114)
- motive: False (0.33633101715808966)
- opportunity: False (0.2651187159690739)

The culprit is Porter 1.
In fact, it is Porter 3.
## 5minutemystery-everythings-not-just-ducky
Bethany is guilty: True or False?
True (0.9425067301242699)
Bethany is not guilty: True or False?
True (0.9155072554665495)
Bethany has mean: True or False?
True (0.9433475737015985)
Bethany has no mean: True or False?
True (0.7962924261546153)
Bethany has motive: True or False?
True (0.9698426136593115)
Map:  50%|█████     | 102/203 [1:04:58<58:37, 34.82s/ examples]Map:  51%|█████     | 103/203 [1:05:30<56:12, 33.72s/ examples]Map:  51%|█████     | 104/203 [1:06:02<55:00, 33.34s/ examples]Bethany has no motive: True or False?
True (0.8766343647921183)
Bethany has opportunity: True or False?
True (0.8670357473609658)
Bethany has no opportunity: True or False?
True (0.6460137433225688)
Connor is guilty: True or False?
True (0.9039744767757508)
Connor is not guilty: True or False?
True (0.8947894610946939)
Connor has mean: True or False?
True (0.94948238112973)
Connor has no mean: True or False?
True (0.8294919722593475)
Connor has motive: True or False?
True (0.9736947425622681)
Connor has no motive: True or False?
True (0.8344068526674736)
Connor has opportunity: True or False?
True (0.9284088027271398)
Connor has no opportunity: True or False?
True (0.5650587130190106)
Emma is guilty: True or False?
True (0.8757869551856522)
Emma is not guilty: True or False?
True (0.8584814679672361)
Emma has mean: True or False?
True (0.9181872635464632)
Emma has no mean: True or False?
True (0.7217432334405754)
Emma has motive: True or False?
True (0.911809984585868)
Emma has no motive: True or False?
True (0.8031737798924701)
Emma has opportunity: True or False?
True (0.8776866221669275)
Emma has no opportunity: True or False?
True (0.6270381219830087)
Tim is guilty: True or False?
True (0.8086723099497763)
Tim is not guilty: True or False?
True (0.8352149074858963)
Tim has mean: True or False?
True (0.947769104959166)
Tim has no mean: True or False?
True (0.8169911556077801)
Tim has motive: True or False?
True (0.9540517932883525)
Tim has no motive: True or False?
True (0.7985011954519707)
Tim has opportunity: True or False?
True (0.8881781721623143)
Tim has no opportunity: True or False?
True (0.7527403228571042)
### Bethany
- mean: True (0.9433475737015985)
- motive: True (0.9698426136593115)
- opportunity: True (0.8670357473609658)

### Connor
- mean: False (0.17050802774065255)
- motive: False (0.1655931473325264)
- opportunity: False (0.43494128698098944)

### Emma
- mean: False (0.27825676655942455)
- motive: False (0.19682622010752993)
- opportunity: False (0.3729618780169913)

### Tim
- mean: False (0.18300884439221987)
- motive: False (0.20149880454802926)
- opportunity: False (0.24725967714289576)

The culprit is Bethany.
In fact, it is Bethany.
## 5minutemystery-a-darkened-veterans-day
Colonel Abraham is guilty: True or False?
True (0.9158089188126235)
Colonel Abraham is not guilty: True or False?
True (0.8947894610946939)
Colonel Abraham has mean: True or False?
True (0.8272706865691472)
Colonel Abraham has no mean: True or False?
True (0.5029296229885981)
Colonel Abraham has motive: True or False?
True (0.94620036983)
Colonel Abraham has no motive: True or False?
True (0.8740772044235984)
Colonel Abraham has opportunity: True or False?
True (0.8852351930010195)
Colonel Abraham has no opportunity: True or False?
True (0.6029970803636248)
Frank Thompson is guilty: True or False?
True (0.9479621664653681)
Frank Thompson is not guilty: True or False?
True (0.9309620852900756)
Frank Thompson has mean: True or False?
True (0.9145963197706802)
Frank Thompson has no mean: True or False?
True (0.7793217912837537)
Frank Thompson has motive: True or False?
True (0.963230549923961)
Frank Thompson has no motive: True or False?
True (0.9162595863469921)
Frank Thompson has opportunity: True or False?
True (0.865678909174824)
Frank Thompson has no opportunity: True or False?
True (0.7962924261546153)
Mr. Landry is guilty: True or False?
True (0.7505527730327083)
Mr. Landry is not guilty: True or False?
True (0.7988152492192591)
Mr. Landry has mean: True or False?
True (0.7209580648179327)
Mr. Landry has no mean: True or False?
True (0.5068355091660127)
Mr. Landry has motive: True or False?
True (0.8514594452543962)
Mr. Landry has no motive: True or False?
True (0.8914335992201801)
Mr. Landry has opportunity: True or False?
True (0.7898827135821628)
Mr. Landry has no opportunity: True or False?
True (0.6001883144765984)
Ryan Smith is guilty: True or False?
True (0.9063219998220023)
Ryan Smith is not guilty: True or False?
True (0.8803862939824989)
Ryan Smith has mean: True or False?
True (0.8799743689174987)
Ryan Smith has no mean: True or False?
True (0.6370307821695329)
Ryan Smith has motive: True or False?
True (0.8933094122075369)
Ryan Smith has no motive: True or False?
True (0.8812065732757132)
Ryan Smith has opportunity: True or False?
True (0.7819973291046377)
Ryan Smith has no opportunity: True or False?
True (0.6934729802503211)
### Colonel Abraham
- mean: False (0.4970703770114019)
- motive: False (0.12592279557640162)
- opportunity: False (0.39700291963637524)

### Frank Thompson
- mean: False (0.22067820871624633)
- motive: False (0.08374041365300788)
- opportunity: False (0.20370757384538474)

### Mr. Landry
- mean: True (0.7209580648179327)
- motive: True (0.8514594452543962)
- opportunity: True (0.7898827135821628)

### Ryan Smith
- mean: False (0.3629692178304671)
- motive: False (0.11879342672428683)
- opportunity: False (0.3065270197496789)

The culprit is Mr. Landry.
In fact, it is Colonel Abraham.
## 5minutemystery-the-missing-ring
Fingers Ferguson is guilty: True or False?
False (0.7492284470473839)
Fingers Ferguson is not guilty: True or False?
True (0.8832359325217328)
Fingers Ferguson has mean: True or False?
True (0.8795611817678315)
Fingers Ferguson has no mean: True or False?
True (0.7627776774954688)
Fingers Ferguson has motive: True or False?
False (0.6148266936950935)
Fingers Ferguson has no motive: True or False?
True (0.8006919661398397)
Fingers Ferguson has opportunity: True or False?
False (0.8116560574095553)
Fingers Ferguson has no opportunity: True or False?
False (0.9153912570383818)
Joe Morgan is guilty: True or False?
True (0.8092759828926619)
Joe Morgan is not guilty: True or False?
True (0.8181563669811865)
Joe Morgan has mean: True or False?
True (0.9066531685310133)
Joe Morgan has no mean: True or False?
True (0.6067314814064781)
Joe Morgan has motive: True or False?
True (0.770464837675413)
Joe Morgan has no motive: True or False?
True (0.6766198919456847)
Joe Morgan has opportunity: True or False?
True (0.7333563569098757)
Joe Morgan has no opportunity: True or False?
False (0.7193836000532381)
Manuel Garcia is guilty: True or False?
True (0.5107405249783342)
Manuel Garcia is not guilty: True or False?
True (0.5039061393777357)
Manuel Garcia has mean: True or False?
True (0.621540893468236)
Manuel Garcia has no mean: True or False?
False (0.8019358443954961)
Manuel Garcia has motive: True or False?
False (0.597373048111048)
Manuel Garcia has no motive: True or False?
False (0.6132365353114321)
Manuel Garcia has opportunity: True or False?
False (0.740174341079517)
Manuel Garcia has no opportunity: True or False?
False (0.8852351930010195)
Mr. Bridges is guilty: True or False?
True (0.6095241816115718)
Mr. Bridges is not guilty: True or False?
True (0.6169358476670045)
Mr. Bridges has mean: True or False?
True (0.7905303264811482)
Mr. Bridges has no mean: True or False?
False (0.5983121871760707)
Mr. Bridges has motive: True or False?
True (0.6688802830862913)
Mr. Bridges has no motive: True or False?
True (0.6575384105121485)
Mr. Bridges has opportunity: True or False?
True (0.5185461538431656)
Mr. Bridges has no opportunity: True or False?
False (0.7853085971692302)
### Fingers Ferguson
- mean: False (0.23722232250453124)
- motive: False (0.6148266936950935)
- opportunity: False (0.8116560574095553)

### Joe Morgan
- mean: False (0.39326851859352185)
- motive: False (0.3233801080543153)
- opportunity: False (0.0)

### Manuel Garcia
- mean: False (0.0)
- motive: False (0.597373048111048)
- opportunity: False (0.740174341079517)

### Mr. Bridges
- mean: True (0.7905303264811482)
- motive: True (0.6688802830862913)
- opportunity: True (0.5185461538431656)

The culprit is Mr. Bridges.
In fact, it is Joe Morgan.
## 5minutemystery-brass-keyboard-mystery
April Key #4 is guilty: True or False?
True (0.7613611200983542)
April Key #4 is not guilty: True or False?
True (0.5563995964631269)
April Key #4 has mean: True or False?
True (0.7098244343353132)
April Key #4 has no mean: True or False?
False (0.5126925663186335)
April Key #4 has motive: True or False?
True (0.7634837587244478)
Map:  52%|█████▏    | 105/203 [1:06:52<1:02:49, 38.46s/ examples]Map:  52%|█████▏    | 106/203 [1:07:29<1:01:06, 37.80s/ examples]April Key #4 has no motive: True or False?
False (0.6984322578436808)
April Key #4 has opportunity: True or False?
True (0.7233094544266295)
April Key #4 has no opportunity: True or False?
False (0.8543993851297865)
Denise Key #6 is guilty: True or False?
True (0.7541915688671895)
Denise Key #6 is not guilty: True or False?
True (0.5645787058071989)
Denise Key #6 has mean: True or False?
True (0.7049732238008671)
Denise Key #6 has no mean: True or False?
False (0.7833262085677729)
Denise Key #6 has motive: True or False?
True (0.6178585826183487)
Denise Key #6 has no motive: True or False?
False (0.8104789202520752)
Denise Key #6 has opportunity: True or False?
True (0.5185462156586879)
Denise Key #6 has no opportunity: True or False?
False (0.8311430212356835)
Harold Key #1 is guilty: True or False?
True (0.7756047866813147)
Harold Key #1 is not guilty: True or False?
True (0.705379313841845)
Harold Key #1 has mean: True or False?
True (0.6884683992569801)
Harold Key #1 has no mean: True or False?
False (0.6774740084332073)
Harold Key #1 has motive: True or False?
True (0.6688802830862913)
Harold Key #1 has no motive: True or False?
False (0.6288633913849659)
Harold Key #1 has opportunity: True or False?
True (0.5428632463719839)
Harold Key #1 has no opportunity: True or False?
False (0.6636689828419103)
Kirsten Key #5 is guilty: True or False?
True (0.5195212821349473)
Kirsten Key #5 is not guilty: True or False?
False (0.5760650031750064)
Kirsten Key #5 has mean: True or False?
False (0.5964331079469681)
Kirsten Key #5 has no mean: True or False?
False (0.9315871016884913)
Kirsten Key #5 has motive: True or False?
False (0.6884684608108543)
Kirsten Key #5 has no motive: True or False?
False (0.8456877416951625)
Kirsten Key #5 has opportunity: True or False?
False (0.8665847814067802)
Kirsten Key #5 has no opportunity: True or False?
False (0.8799743689174987)
Robert (Buddy) Key #3 is guilty: True or False?
True (0.7412996266976789)
Robert (Buddy) Key #3 is not guilty: True or False?
False (0.5626571839060285)
Robert (Buddy) Key #3 has mean: True or False?
True (0.8250265073476026)
Robert (Buddy) Key #3 has no mean: True or False?
False (0.7662936378892937)
Robert (Buddy) Key #3 has motive: True or False?
True (0.5156198737738186)
Robert (Buddy) Key #3 has no motive: True or False?
False (0.8502200840158227)
Robert (Buddy) Key #3 has opportunity: True or False?
True (0.5423785259821196)
Robert (Buddy) Key #3 has no opportunity: True or False?
False (0.8967949154286139)
### April Key #4
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.0)

### Denise Key #6
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.0)

### Harold Key #1
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.0)

### Kirsten Key #5
- mean: False (0.5964331079469681)
- motive: False (0.6884684608108543)
- opportunity: False (0.8665847814067802)

### Robert (Buddy) Key #3
- mean: True (0.8250265073476026)
- motive: True (0.5156198737738186)
- opportunity: True (0.5423785259821196)

The culprit is Robert (Buddy) Key #3.
In fact, it is April Key #4.
## 5minutemystery-the-curse-of-the-unlucky-streak
Coach Williams is guilty: True or False?
True (0.8031737798924701)
Coach Williams is not guilty: True or False?
True (0.7233094544266295)
Coach Williams has mean: True or False?
True (0.7345005213790038)
Coach Williams has no mean: True or False?
False (0.6095241271158658)
Coach Williams has motive: True or False?
True (0.8517062701455038)
Coach Williams has no motive: True or False?
True (0.7728736896481636)
Coach Williams has opportunity: True or False?
True (0.6592954931819778)
Coach Williams has no opportunity: True or False?
False (0.6757646168022439)
Joe is guilty: True or False?
True (0.5869964306477841)
Joe is not guilty: True or False?
True (0.5784481782924303)
Joe has mean: True or False?
True (0.8568122429692968)
Joe has no mean: True or False?
False (0.5869964306477841)
Joe has motive: True or False?
True (0.861071588244826)
Joe has no motive: True or False?
True (0.5486734987923966)
Joe has opportunity: True or False?
True (0.7178038242127955)
Joe has no opportunity: True or False?
False (0.7431679939957333)
Mrs. Williams is guilty: True or False?
True (0.8957052808276003)
Mrs. Williams is not guilty: True or False?
True (0.8303191711685114)
Mrs. Williams has mean: True or False?
True (0.8645393849369172)
Mrs. Williams has no mean: True or False?
True (0.5165954111147137)
Mrs. Williams has motive: True or False?
True (0.9485372300670596)
Mrs. Williams has no motive: True or False?
True (0.811078188867804)
Mrs. Williams has opportunity: True or False?
True (0.8261514850267767)
Mrs. Williams has no opportunity: True or False?
False (0.5087881523495457)
Roderick is guilty: True or False?
True (0.6834194581047349)
Roderick is not guilty: True or False?
True (0.5399537164111071)
Roderick has mean: True or False?
True (0.60859406896259)
Roderick has no mean: True or False?
False (0.6783269591477166)
Roderick has motive: True or False?
True (0.7711548223101617)
Roderick has no motive: True or False?
True (0.5034179144599427)
Roderick has opportunity: True or False?
True (0.6343168082332088)
Roderick has no opportunity: True or False?
False (0.803173839733582)
### Coach Williams
- mean: False (0.0)
- motive: False (0.2271263103518364)
- opportunity: False (0.0)

### Joe
- mean: True (0.8568122429692968)
- motive: True (0.861071588244826)
- opportunity: True (0.7178038242127955)

### Mrs. Williams
- mean: False (0.48340458888528626)
- motive: False (0.18892181113219597)
- opportunity: False (0.0)

### Roderick
- mean: False (0.0)
- motive: False (0.49658208554005734)
- opportunity: False (0.0)

The culprit is Joe.
In fact, it is Joe.
## 5minutemystery-halloween-2008
Bride is guilty: True or False?
True (0.9124361266596831)
Bride is not guilty: True or False?
True (0.917524634492174)
Bride has mean: True or False?
True (0.8558511727823209)
Bride has no mean: True or False?
True (1.0124585808829667)
Bride has motive: True or False?
True (0.8620035048683017)
Bride has no motive: True or False?
True (0.8928431309470957)
Bride has opportunity: True or False?
True (0.9171543708147702)
Bride has no opportunity: True or False?
True (0.8737544452204027)
Groom is guilty: True or False?
True (0.9169315082548071)
Groom is not guilty: True or False?
True (1.0720792967693575)
Groom has mean: True or False?
True (0.8559715712342816)
Groom has no mean: True or False?
True (1.4136467600752023)
Groom has motive: True or False?
True (0.901737077061468)
Groom has no motive: True or False?
True (0.8885656020494875)
Groom has opportunity: True or False?
True (0.8912444703721882)
Groom has no opportunity: True or False?
True (0.9534652915134475)
Indian Chief is guilty: True or False?
True (0.9178196797655932)
Indian Chief is not guilty: True or False?
True (0.920217993899809)
Indian Chief has mean: True or False?
True (0.9014011626580862)
Indian Chief has no mean: True or False?
True (0.9020932932190145)
Indian Chief has motive: True or False?
True (0.9083743698340163)
Indian Chief has no motive: True or False?
True (0.906900823774748)
Indian Chief has opportunity: True or False?
True (0.9326375756581993)
Indian Chief has no opportunity: True or False?
True (0.894973220907352)
Wealthy Woman is guilty: True or False?
True (0.9480103258576807)
Wealthy Woman is not guilty: True or False?
True (0.9487513288936312)
Wealthy Woman has mean: True or False?
True (0.9243469854582533)
Wealthy Woman has no mean: True or False?
True (0.9292480357050936)
Wealthy Woman has motive: True or False?
True (0.9390807169043887)
Wealthy Woman has no motive: True or False?
True (0.9400236029887878)
Wealthy Woman has opportunity: True or False?
True (0.9355233894679749)
Wealthy Woman has no opportunity: True or False?
True (0.9739624429369509)
### Bride
- mean: True (0.8558511727823209)
- motive: True (0.8620035048683017)
- opportunity: True (0.9171543708147702)

### Groom
- mean: False (0.0)
- motive: False (0.11143439795051246)
- opportunity: False (0.0465347084865525)

### Indian Chief
- mean: False (0.09790670678098545)
- motive: False (0.09309917622525199)
Map:  53%|█████▎    | 107/203 [1:08:22<1:08:09, 42.60s/ examples]Map:  53%|█████▎    | 108/203 [1:08:56<1:02:54, 39.73s/ examples]Map:  54%|█████▎    | 109/203 [1:09:36<1:02:46, 40.07s/ examples]- opportunity: False (0.10502677909264801)

### Wealthy Woman
- mean: False (0.07075196429490638)
- motive: False (0.05997639701121216)
- opportunity: False (0.02603755706304911)

The culprit is Bride.
In fact, it is Groom.
## 5minutemystery-the-trick-or-treat-mystery
Dorothy is guilty: True or False?
True (0.8386797935187188)
Dorothy is not guilty: True or False?
True (0.8577681165234065)
Dorothy has mean: True or False?
True (0.7718435616326055)
Dorothy has no mean: True or False?
True (0.627038178044588)
Dorothy has motive: True or False?
True (0.8860265005470086)
Dorothy has no motive: True or False?
True (0.7570766705324253)
Dorothy has opportunity: True or False?
True (0.920789721359066)
Dorothy has no opportunity: True or False?
True (0.6206216296838327)
Superman is guilty: True or False?
True (0.8958875533219306)
Superman is not guilty: True or False?
True (0.8944211616820568)
Superman has mean: True or False?
True (0.8413048399699521)
Superman has no mean: True or False?
True (0.704566905597538)
Superman has motive: True or False?
True (0.9410069597342015)
Superman has no motive: True or False?
True (0.832781310996106)
Superman has opportunity: True or False?
True (0.8221891570741111)
Superman has no opportunity: True or False?
True (0.6680145240815963)
The Ghost is guilty: True or False?
True (0.8128672807499561)
The Ghost is not guilty: True or False?
True (0.7634837587244478)
The Ghost has mean: True or False?
True (0.8056321690561029)
The Ghost has no mean: True or False?
True (0.7074047371961694)
The Ghost has motive: True or False?
True (0.8386797935187188)
The Ghost has no motive: True or False?
True (0.6575384693006662)
The Ghost has opportunity: True or False?
True (0.8227594449669557)
The Ghost has no opportunity: True or False?
True (0.6680145838067516)
The Lion is guilty: True or False?
True (0.7333563569098757)
The Lion is not guilty: True or False?
True (0.6951311179371613)
The Lion has mean: True or False?
True (0.779321849347754)
The Lion has no mean: True or False?
True (0.7209580648179327)
The Lion has motive: True or False?
True (0.8514594452543962)
The Lion has no motive: True or False?
True (0.6297746298200823)
The Lion has opportunity: True or False?
True (0.8397339530959691)
The Lion has no opportunity: True or False?
True (0.5621764690603255)
The Witch is guilty: True or False?
True (0.7669925046333297)
The Witch is not guilty: True or False?
True (0.6976088896786037)
The Witch has mean: True or False?
True (0.7937461674149602)
The Witch has no mean: True or False?
True (0.6984323202883935)
The Witch has motive: True or False?
True (0.8727817583545995)
The Witch has no motive: True or False?
True (0.7193836000532381)
The Witch has opportunity: True or False?
True (0.8428631416381634)
The Witch has no opportunity: True or False?
True (0.6029971163050526)
### Dorothy
- mean: False (0.37296182195541205)
- motive: False (0.24292332946757467)
- opportunity: False (0.3793783703161673)

### Superman
- mean: False (0.295433094402462)
- motive: False (0.16721868900389403)
- opportunity: False (0.33198547591840366)

### The Ghost
- mean: True (0.8056321690561029)
- motive: True (0.8386797935187188)
- opportunity: True (0.8227594449669557)

### The Lion
- mean: False (0.2790419351820673)
- motive: False (0.37022537017991775)
- opportunity: False (0.4378235309396745)

### The Witch
- mean: False (0.3015676797116065)
- motive: False (0.2806163999467619)
- opportunity: False (0.3970028836949474)

The culprit is The Ghost.
In fact, it is The Witch.
## 5minutemystery-house-of-the-rising-pumpkin
Curtis is guilty: True or False?
True (0.7981867775042927)
Curtis is not guilty: True or False?
True (0.7711548223101617)
Curtis has mean: True or False?
True (0.7711548682745724)
Curtis has no mean: True or False?
True (0.7348812840309261)
Curtis has motive: True or False?
True (0.9463988549853353)
Curtis has no motive: True or False?
True (0.7697732451157533)
Curtis has opportunity: True or False?
True (0.7779753136455794)
Curtis has no opportunity: True or False?
False (0.591723272524637)
Dabney is guilty: True or False?
True (0.9216402157401415)
Dabney is not guilty: True or False?
True (0.9209319968384807)
Dabney has mean: True or False?
True (0.905989824801558)
Dabney has no mean: True or False?
True (0.8617710443758085)
Dabney has motive: True or False?
True (0.9645224799532249)
Dabney has no motive: True or False?
True (0.8472108208062923)
Dabney has opportunity: True or False?
True (0.8984105001507761)
Dabney has no opportunity: True or False?
True (0.6930575925553026)
Kim is guilty: True or False?
True (0.8601343603168419)
Kim is not guilty: True or False?
True (0.8652240590801695)
Kim has mean: True or False?
True (0.9299510095943111)
Kim has no mean: True or False?
True (0.8221891570741111)
Kim has motive: True or False?
True (0.9580694433457548)
Kim has no motive: True or False?
True (0.8198932995357624)
Kim has opportunity: True or False?
True (0.9122799654606127)
Kim has no opportunity: True or False?
True (0.6261242000979097)
Mary is guilty: True or False?
True (0.884837803442546)
Mary is not guilty: True or False?
True (0.8951566249612815)
Mary has mean: True or False?
True (0.8638516611889259)
Mary has no mean: True or False?
True (0.6388353131709135)
Mary has motive: True or False?
True (0.9477691649813238)
Mary has no motive: True or False?
True (0.7914989614633984)
Mary has opportunity: True or False?
True (0.8716934900924195)
Mary has no opportunity: True or False?
True (0.705785027818136)
### Curtis
- mean: True (0.7711548682745724)
- motive: True (0.9463988549853353)
- opportunity: True (0.7779753136455794)

### Dabney
- mean: False (0.13822895562419146)
- motive: False (0.1527891791937077)
- opportunity: False (0.30694240744469736)

### Kim
- mean: False (0.1778108429258889)
- motive: False (0.1801067004642376)
- opportunity: False (0.3738757999020903)

### Mary
- mean: False (0.36116468682908653)
- motive: False (0.20850103853660162)
- opportunity: False (0.294214972181864)

The culprit is Curtis.
In fact, it is Kim.
## 5minutemystery-the-secret-of-the-scarecrows-mask
Charles Kincaid is guilty: True or False?
True (0.9124361266596831)
Charles Kincaid is not guilty: True or False?
True (0.8868131040663721)
Charles Kincaid has mean: True or False?
True (0.7898827724330132)
Charles Kincaid has no mean: True or False?
True (0.6178585826183487)
Charles Kincaid has motive: True or False?
True (0.7975568155246964)
Charles Kincaid has no motive: True or False?
True (0.6893056096647525)
Charles Kincaid has opportunity: True or False?
True (0.6104534962074417)
Charles Kincaid has no opportunity: True or False?
False (0.6104534962074417)
Chester is guilty: True or False?
True (0.8591917766133458)
Chester is not guilty: True or False?
True (0.9139841191734227)
Chester has mean: True or False?
True (0.8624675215861032)
Chester has no mean: True or False?
False (0.503906199448032)
Chester has motive: True or False?
True (0.8204694405411458)
Chester has no motive: True or False?
True (0.6029970803636248)
Chester has opportunity: True or False?
False (0.5360700410935405)
Chester has no opportunity: True or False?
False (0.7248702601920561)
Mr. Winfrey is guilty: True or False?
True (0.9155072554665495)
Mr. Winfrey is not guilty: True or False?
True (0.9355822824773136)
Mr. Winfrey has mean: True or False?
True (0.8349459127213729)
Mr. Winfrey has no mean: True or False?
True (0.7065954713132195)
Mr. Winfrey has motive: True or False?
True (0.7606506998655483)
Mr. Winfrey has no motive: True or False?
True (0.873646672673131)
Mr. Winfrey has opportunity: True or False?
True (0.7154240000492645)
Mr. Winfrey has no opportunity: True or False?
True (0.6415346823638186)
Mrs. Winfrey is guilty: True or False?
True (0.8795611817678315)
Mrs. Winfrey is not guilty: True or False?
True (0.9145963197706802)
Mrs. Winfrey has mean: True or False?
True (0.8338664756137771)
Mrs. Winfrey has no mean: True or False?
True (0.7752646804088963)
Mrs. Winfrey has motive: True or False?
True (0.7655933544531522)
Mrs. Winfrey has no motive: True or False?
True (0.8714748565614324)
Mrs. Winfrey has opportunity: True or False?
Map:  54%|█████▍    | 110/203 [1:10:09<58:48, 37.94s/ examples]  Map:  55%|█████▍    | 111/203 [1:10:44<56:47, 37.04s/ examples]Map:  55%|█████▌    | 112/203 [1:11:10<51:01, 33.65s/ examples]True (0.8074606715677252)
Mrs. Winfrey has no opportunity: True or False?
True (0.6566582306092376)
### Charles Kincaid
- mean: False (0.3821414173816513)
- motive: False (0.3106943903352475)
- opportunity: False (0.0)

### Chester
- mean: True (0.8624675215861032)
- motive: True (0.8204694405411458)
- opportunity: True (0.27512973980794386)

### Mr. Winfrey
- mean: False (0.29340452868678046)
- motive: False (0.126353327326869)
- opportunity: False (0.3584653176361814)

### Mrs. Winfrey
- mean: False (0.2247353195911037)
- motive: False (0.12852514343856758)
- opportunity: False (0.34334176939076244)

The culprit is Chester.
In fact, it is Chester.
## 5minutemystery-the-scarecrow-slasher
Annie is guilty: True or False?
False (0.5525396910980834)
Annie is not guilty: True or False?
False (0.5068354487465153)
Annie has mean: True or False?
True (0.6206216296838327)
Annie has no mean: True or False?
False (0.7185944237486072)
Annie has motive: True or False?
True (0.7122321792841629)
Annie has no motive: True or False?
False (0.6076631662366868)
Annie has opportunity: True or False?
True (0.6984323202883935)
Annie has no opportunity: True or False?
False (0.7468781552484828)
Mr. Forbes is guilty: True or False?
True (0.7697732451157533)
Mr. Forbes is not guilty: True or False?
True (0.7386690954574974)
Mr. Forbes has mean: True or False?
True (0.8454326959560526)
Mr. Forbes has no mean: True or False?
False (0.5370414382302919)
Mr. Forbes has motive: True or False?
True (0.7975568155246964)
Mr. Forbes has no motive: True or False?
True (0.6504672161860058)
Mr. Forbes has opportunity: True or False?
True (0.6645402797838648)
Mr. Forbes has no opportunity: True or False?
False (0.685107355950278)
Mrs. Avery is guilty: True or False?
True (0.7752646804088963)
Mrs. Avery is not guilty: True or False?
True (0.7114308965749192)
Mrs. Avery has mean: True or False?
True (0.7333564224770464)
Mrs. Avery has no mean: True or False?
False (0.6504672743423094)
Mrs. Avery has motive: True or False?
True (0.7541915239138703)
Mrs. Avery has no motive: True or False?
True (0.5370414382302919)
Mrs. Avery has opportunity: True or False?
True (0.6477981763584071)
Mrs. Avery has no opportunity: True or False?
False (0.6893056096647525)
Philips is guilty: True or False?
True (0.6967842494573921)
Philips is not guilty: True or False?
True (0.7106282704218558)
Philips has mean: True or False?
False (0.5165954726976894)
Philips has no mean: True or False?
False (0.6808785831877406)
Philips has motive: True or False?
True (0.6406358487498992)
Philips has no motive: True or False?
True (0.591723272524637)
Philips has opportunity: True or False?
True (0.5068355091660127)
Philips has no opportunity: True or False?
False (0.5448014304301324)
### Annie
- mean: True (0.6206216296838327)
- motive: True (0.7122321792841629)
- opportunity: True (0.6984323202883935)

### Mr. Forbes
- mean: False (0.0)
- motive: False (0.3495327838139942)
- opportunity: False (0.0)

### Mrs. Avery
- mean: False (0.0)
- motive: False (0.46295856176970807)
- opportunity: False (0.0)

### Philips
- mean: False (0.5165954726976894)
- motive: False (0.40827672747536303)
- opportunity: False (0.0)

The culprit is Annie.
In fact, it is Philips.
## 5minutemystery-the-golden-ruse
Miss Jones is guilty: True or False?
True (0.6575384105121485)
Miss Jones is not guilty: True or False?
True (0.6197014353942354)
Miss Jones has mean: True or False?
True (0.8652240590801695)
Miss Jones has no mean: True or False?
False (0.5195213440667139)
Miss Jones has motive: True or False?
True (0.7711548682745724)
Miss Jones has no motive: True or False?
True (0.6791787167336184)
Miss Jones has opportunity: True or False?
True (0.5563995964631269)
Miss Jones has no opportunity: True or False?
False (0.5418937216067536)
Miss. Pendlebury is guilty: True or False?
True (0.7209580648179327)
Miss. Pendlebury is not guilty: True or False?
True (0.7356416038392981)
Miss. Pendlebury has mean: True or False?
True (0.867485409735739)
Miss. Pendlebury has no mean: True or False?
True (0.685107355950278)
Miss. Pendlebury has motive: True or False?
True (0.7859663967519771)
Miss. Pendlebury has no motive: True or False?
True (0.7534666630720156)
Miss. Pendlebury has opportunity: True or False?
True (0.7130321332210621)
Miss. Pendlebury has no opportunity: True or False?
True (0.5926666351772785)
Mr. Horgan is guilty: True or False?
True (0.8080671968507699)
Mr. Horgan is not guilty: True or False?
True (0.832781373043151)
Mr. Horgan has mean: True or False?
True (0.9046505126460354)
Mr. Horgan has no mean: True or False?
True (0.6876299924560524)
Mr. Horgan has motive: True or False?
True (0.8740772044235984)
Mr. Horgan has no motive: True or False?
True (0.8679338697256817)
Mr. Horgan has opportunity: True or False?
True (0.7962924261546153)
Mr. Horgan has no opportunity: True or False?
True (0.6397360437814448)
Mr. Reese is guilty: True or False?
True (0.7033457711626864)
Mr. Reese is not guilty: True or False?
True (0.8459424357871997)
Mr. Reese has mean: True or False?
True (0.9502265454272235)
Mr. Reese has no mean: True or False?
True (0.7512833387594996)
Mr. Reese has motive: True or False?
True (0.8474634858439474)
Mr. Reese has no motive: True or False?
True (0.794384956668203)
Mr. Reese has opportunity: True or False?
True (0.7217432334405754)
Mr. Reese has no opportunity: True or False?
True (0.6522414018725713)
### Miss Jones
- mean: True (0.8652240590801695)
- motive: True (0.7711548682745724)
- opportunity: True (0.5563995964631269)

### Miss. Pendlebury
- mean: False (0.31489264404972195)
- motive: False (0.2465333369279844)
- opportunity: False (0.40733336482272153)

### Mr. Horgan
- mean: False (0.3123700075439476)
- motive: False (0.13206613027431835)
- opportunity: False (0.3602639562185552)

### Mr. Reese
- mean: False (0.2487166612405004)
- motive: False (0.20561504333179703)
- opportunity: False (0.3477585981274287)

The culprit is Miss Jones.
In fact, it is Mr. Horgan.
## 5minutemystery-hound-of-the-buskerville
Balloon Twister is guilty: True or False?
True (0.9548162209309636)
Balloon Twister is not guilty: True or False?
True (0.8980534699860239)
Balloon Twister has mean: True or False?
True (0.96920782287766)
Balloon Twister has no mean: True or False?
True (0.9053223122169206)
Balloon Twister has motive: True or False?
True (0.9366337094376229)
Balloon Twister has no motive: True or False?
True (0.8601343603168419)
Balloon Twister has opportunity: True or False?
True (0.8584814679672361)
Balloon Twister has no opportunity: True or False?
True (0.8164064229895683)
Living Statue is guilty: True or False?
True (0.9015746123467522)
Living Statue is not guilty: True or False?
True (0.8006919661398397)
Living Statue has mean: True or False?
True (0.9478657243703977)
Living Statue has no mean: True or False?
True (0.8524448242555318)
Living Statue has motive: True or False?
True (0.8624675215861032)
Living Statue has no motive: True or False?
True (0.7704647687904915)
Living Statue has opportunity: True or False?
True (0.7446563307563252)
Living Statue has no opportunity: True or False?
True (0.5583270361921496)
Mime is guilty: True or False?
True (0.8906751877407573)
Mime is not guilty: True or False?
True (0.8433798528114077)
Mime has mean: True or False?
True (0.9066531685310133)
Mime has no mean: True or False?
True (0.7882573622725895)
Mime has motive: True or False?
True (0.8816149238192855)
Mime has no motive: True or False?
True (0.8122723669190336)
Mime has opportunity: True or False?
True (0.8255897087847518)
Mime has no opportunity: True or False?
True (0.6610482284345209)
Stilt-Walker is guilty: True or False?
True (0.9263036859044167)
Stilt-Walker is not guilty: True or False?
True (0.8647679145346777)
Stilt-Walker has mean: True or False?
True (0.9346342066470359)
Stilt-Walker has no mean: True or False?
True (0.8250265688168699)
Stilt-Walker has motive: True or False?
True (0.9073122118500465)
Stilt-Walker has no motive: True or False?
True (0.7950222460539826)
Stilt-Walker has opportunity: True or False?
True (0.802555560073231)
Stilt-Walker has no opportunity: True or False?
Map:  56%|█████▌    | 113/203 [1:11:49<52:50, 35.23s/ examples]Map:  56%|█████▌    | 114/203 [1:12:25<52:27, 35.37s/ examples]Map:  57%|█████▋    | 115/203 [1:12:57<50:31, 34.45s/ examples]True (0.6029970803636248)
### Balloon Twister
- mean: True (0.96920782287766)
- motive: True (0.9366337094376229)
- opportunity: True (0.8584814679672361)

### Living Statue
- mean: False (0.1475551757444682)
- motive: False (0.22953523120950847)
- opportunity: False (0.44167296380785037)

### Mime
- mean: False (0.21174263772741053)
- motive: False (0.1877276330809664)
- opportunity: False (0.33895177156547907)

### Stilt-Walker
- mean: False (0.17497343118313013)
- motive: False (0.20497775394601736)
- opportunity: False (0.39700291963637524)

The culprit is Balloon Twister.
In fact, it is Stilt-Walker.
## 5minutemystery-moriarty-picks-a-murderer-part-two
Hansom Cab Driver is guilty: True or False?
True (0.7885832152749314)
Hansom Cab Driver is not guilty: True or False?
True (0.6808786440630326)
Hansom Cab Driver has mean: True or False?
True (0.802555560073231)
Hansom Cab Driver has no mean: True or False?
True (0.6706082735718226)
Hansom Cab Driver has motive: True or False?
True (0.944073857204818)
Hansom Cab Driver has no motive: True or False?
True (0.8822251029233062)
Hansom Cab Driver has opportunity: True or False?
True (0.9044818892710186)
Hansom Cab Driver has no opportunity: True or False?
True (0.6504672161860058)
Policeman is guilty: True or False?
True (0.6842640081724978)
Policeman is not guilty: True or False?
True (0.5486734987923966)
Policeman has mean: True or False?
True (0.5794003525136094)
Policeman has no mean: True or False?
False (0.6959583025067009)
Policeman has motive: True or False?
True (0.9206470837359207)
Policeman has no motive: True or False?
True (0.8354835531737983)
Policeman has opportunity: True or False?
True (0.9095862487848758)
Policeman has no opportunity: True or False?
True (0.7174080489207124)
Theater Usher is guilty: True or False?
True (0.893681109060862)
Theater Usher is not guilty: True or False?
True (0.862699090112503)
Theater Usher has mean: True or False?
True (0.7895583472451868)
Theater Usher has no mean: True or False?
True (0.5156199352405011)
Theater Usher has motive: True or False?
True (0.907803776883121)
Theater Usher has no motive: True or False?
True (0.8410438847419)
Theater Usher has opportunity: True or False?
True (0.7655933544531522)
Theater Usher has no opportunity: True or False?
True (0.5141563432579597)
Ticket Seller is guilty: True or False?
True (0.8494723435042196)
Ticket Seller is not guilty: True or False?
True (0.814643384779728)
Ticket Seller has mean: True or False?
True (0.8556100696922833)
Ticket Seller has no mean: True or False?
True (0.7318258918270596)
Ticket Seller has motive: True or False?
True (0.9464977993639099)
Ticket Seller has no motive: True or False?
True (0.9064877041303855)
Ticket Seller has opportunity: True or False?
True (0.8966140148346177)
Ticket Seller has no opportunity: True or False?
True (1.4576762696608656)
### Hansom Cab Driver
- mean: False (0.3293917264281774)
- motive: False (0.11777489707669375)
- opportunity: False (0.3495327838139942)

### Policeman
- mean: True (0.5794003525136094)
- motive: True (0.9206470837359207)
- opportunity: True (0.9095862487848758)

### Theater Usher
- mean: False (0.4843800647594989)
- motive: False (0.15895611525810005)
- opportunity: False (0.48584365674204033)

### Ticket Seller
- mean: False (0.2681741081729404)
- motive: False (0.09351229586961451)
- opportunity: False (0.0)

The culprit is Policeman.
In fact, it is Theater Usher.
## 5minutemystery-the-scent-of-a-thief
Betty is guilty: True or False?
True (0.7879311977554747)
Betty is not guilty: True or False?
True (0.6469064338453809)
Betty has mean: True or False?
True (0.725648573585541)
Betty has no mean: True or False?
False (0.5438324636094939)
Betty has motive: True or False?
True (0.7371581892031299)
Betty has no motive: True or False?
True (0.5813030649269245)
Betty has opportunity: True or False?
True (0.5486734660889085)
Betty has no opportunity: True or False?
False (0.7718434926244166)
Darlene is guilty: True or False?
True (0.8407825844829613)
Darlene is not guilty: True or False?
True (0.7520125537161032)
Darlene has mean: True or False?
True (0.7641883982873323)
Darlene has no mean: True or False?
False (0.5515736950589613)
Darlene has motive: True or False?
True (0.7386690954574974)
Darlene has no motive: True or False?
False (0.5136684743338078)
Darlene has opportunity: True or False?
True (0.612309626324874)
Darlene has no opportunity: True or False?
False (0.7592254214399092)
Mr. Danby is guilty: True or False?
True (0.7924642605907138)
Mr. Danby is not guilty: True or False?
True (0.6791787167336184)
Mr. Danby has mean: True or False?
True (0.6706082735718226)
Mr. Danby has no mean: True or False?
False (0.5409238971378262)
Mr. Danby has motive: True or False?
True (0.6601724005812412)
Mr. Danby has no motive: True or False?
True (0.6039318499573872)
Mr. Danby has opportunity: True or False?
True (0.6680145240815963)
Mr. Danby has no opportunity: True or False?
False (0.816406362162552)
Mr. Harrison is guilty: True or False?
True (0.8428631416381634)
Mr. Harrison is not guilty: True or False?
True (0.7409249450892966)
Mr. Harrison has mean: True or False?
True (0.7697732451157533)
Mr. Harrison has no mean: True or False?
True (0.5515736950589613)
Mr. Harrison has motive: True or False?
True (0.6766198919456847)
Mr. Harrison has no motive: True or False?
True (0.6504672743423094)
Mr. Harrison has opportunity: True or False?
True (0.6370307821695329)
Mr. Harrison has no opportunity: True or False?
False (0.784649255215384)
### Betty
- mean: False (0.0)
- motive: False (0.4186969350730755)
- opportunity: False (0.0)

### Darlene
- mean: True (0.7641883982873323)
- motive: True (0.7386690954574974)
- opportunity: True (0.612309626324874)

### Mr. Danby
- mean: False (0.0)
- motive: False (0.39606815004261275)
- opportunity: False (0.0)

### Mr. Harrison
- mean: False (0.44842630494103874)
- motive: False (0.34953272565769056)
- opportunity: False (0.0)

The culprit is Darlene.
In fact, it is Mr. Harrison.
## 5minutemystery-moriarty-picks-a-murderer-part-one
Ed the Bludgeoner is guilty: True or False?
True (0.7872777601997338)
Ed the Bludgeoner is not guilty: True or False?
True (0.700075275973927)
Ed the Bludgeoner has mean: True or False?
True (0.6076631662366868)
Ed the Bludgeoner has no mean: True or False?
False (0.7074046739492601)
Ed the Bludgeoner has motive: True or False?
True (0.7739006258141444)
Ed the Bludgeoner has no motive: True or False?
False (0.5078118305218892)
Ed the Bludgeoner has opportunity: True or False?
True (0.7505527730327083)
Ed the Bludgeoner has no opportunity: True or False?
True (0.5068355091660127)
Fastidious Fred Fielder is guilty: True or False?
True (0.727201163301072)
Fastidious Fred Fielder is not guilty: True or False?
True (0.6197014353942354)
Fastidious Fred Fielder has mean: True or False?
True (0.7885832152749314)
Fastidious Fred Fielder has no mean: True or False?
False (0.6909762697651828)
Fastidious Fred Fielder has motive: True or False?
True (0.731825826396729)
Fastidious Fred Fielder has no motive: True or False?
True (0.6671476985798853)
Fastidious Fred Fielder has opportunity: True or False?
True (0.6723316913929156)
Fastidious Fred Fielder has no opportunity: True or False?
True (0.6215409675616889)
Herman Houlihan is guilty: True or False?
True (0.8062431235779619)
Herman Houlihan is not guilty: True or False?
True (0.6095241271158658)
Herman Houlihan has mean: True or False?
True (0.589834510337428)
Herman Houlihan has no mean: True or False?
False (0.7098243920264812)
Herman Houlihan has motive: True or False?
True (0.7527403228571042)
Herman Houlihan has no motive: True or False?
True (0.5165954726976894)
Herman Houlihan has opportunity: True or False?
True (0.6029970803636248)
Herman Houlihan has no opportunity: True or False?
False (0.7049732238008671)
Morris the Ascot Dandy is guilty: True or False?
True (0.7490872087035162)
Morris the Ascot Dandy is not guilty: True or False?
True (0.60859406896259)
Morris the Ascot Dandy has mean: True or False?
True (0.740174341079517)
Morris the Ascot Dandy has no mean: True or False?
False (0.6469064338453809)
Map:  57%|█████▋    | 116/203 [1:13:33<50:46, 35.02s/ examples]Map:  58%|█████▊    | 117/203 [1:14:12<51:42, 36.08s/ examples]Map:  58%|█████▊    | 118/203 [1:14:42<48:27, 34.21s/ examples]Morris the Ascot Dandy has motive: True or False?
True (0.7318258918270596)
Morris the Ascot Dandy has no motive: True or False?
True (0.5794004215835179)
Morris the Ascot Dandy has opportunity: True or False?
True (0.7240905804783984)
Morris the Ascot Dandy has no opportunity: True or False?
False (0.6057990224408951)
### Ed the Bludgeoner
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.4931644908339873)

### Fastidious Fred Fielder
- mean: False (0.0)
- motive: False (0.3328523014201147)
- opportunity: False (0.37845903243831114)

### Herman Houlihan
- mean: False (0.0)
- motive: False (0.48340452730231065)
- opportunity: False (0.0)

### Morris the Ascot Dandy
- mean: True (0.740174341079517)
- motive: True (0.7318258918270596)
- opportunity: True (0.7240905804783984)

The culprit is Morris the Ascot Dandy.
In fact, it is Fastidious Fred Fielder.
## 5minutemystery-the-geneva-summit-goldfish-mystery
Ermina Glandon is guilty: True or False?
True (0.5097643762740132)
Ermina Glandon is not guilty: True or False?
False (0.5457699766832048)
Ermina Glandon has mean: True or False?
True (0.875361437979977)
Ermina Glandon has no mean: True or False?
True (0.5263427467960875)
Ermina Glandon has motive: True or False?
True (0.5983121871760707)
Ermina Glandon has no motive: True or False?
False (0.615087818987177)
Ermina Glandon has opportunity: True or False?
False (0.64779823427608)
Ermina Glandon has no opportunity: True or False?
False (0.815232454829111)
George Adams is guilty: True or False?
True (0.644225125126315)
George Adams is not guilty: True or False?
True (0.5370414382302919)
George Adams has mean: True or False?
True (0.8745065279415651)
George Adams has no mean: True or False?
True (0.5273165068094335)
George Adams has motive: True or False?
True (0.7233094544266295)
George Adams has no motive: True or False?
False (0.5380124470448935)
George Adams has opportunity: True or False?
False (0.5243946167262008)
George Adams has no opportunity: True or False?
False (0.7264255794048772)
Matthew O'Leary is guilty: True or False?
True (0.5467381591701916)
Matthew O'Leary is not guilty: True or False?
False (0.5722447820960327)
Matthew O'Leary has mean: True or False?
True (0.9543079730970608)
Matthew O'Leary has no mean: True or False?
True (0.6352224318508648)
Matthew O'Leary has motive: True or False?
True (0.6224592927728324)
Matthew O'Leary has no motive: True or False?
False (0.8116760258690822)
Matthew O'Leary has opportunity: True or False?
True (0.8050197941712954)
Matthew O'Leary has no opportunity: True or False?
False (0.8582439976623328)
Prince Rahim is guilty: True or False?
True (0.6531268925247615)
Prince Rahim is not guilty: True or False?
True (0.6740504382339836)
Prince Rahim has mean: True or False?
True (0.6680145240815963)
Prince Rahim has no mean: True or False?
False (0.5380124470448935)
Prince Rahim has motive: True or False?
True (0.5583270361921496)
Prince Rahim has no motive: True or False?
False (0.5263427467960875)
Prince Rahim has opportunity: True or False?
False (0.6397360437814448)
Prince Rahim has no opportunity: True or False?
False (0.6706082735718226)
Ronald Reagan is guilty: True or False?
True (0.644225125126315)
Ronald Reagan is not guilty: True or False?
True (0.757435727300218)
Ronald Reagan has mean: True or False?
True (0.8966140749572745)
Ronald Reagan has no mean: True or False?
True (0.7082125449089324)
Ronald Reagan has motive: True or False?
True (0.5204963206682631)
Ronald Reagan has no motive: True or False?
False (0.5612147992901458)
Ronald Reagan has opportunity: True or False?
True (0.5612147992901458)
Ronald Reagan has no opportunity: True or False?
False (0.844921525814193)
### Ermina Glandon
- mean: False (0.4736572532039125)
- motive: False (0.0)
- opportunity: False (0.64779823427608)

### George Adams
- mean: False (0.47268349319056646)
- motive: False (0.0)
- opportunity: False (0.5243946167262008)

### Matthew O'Leary
- mean: True (0.9543079730970608)
- motive: True (0.6224592927728324)
- opportunity: True (0.8050197941712954)

### Prince Rahim
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.6397360437814448)

### Ronald Reagan
- mean: False (0.2917874550910676)
- motive: False (0.0)
- opportunity: False (0.0)

The culprit is Matthew O'Leary.
In fact, it is Ronald Reagan.
## 5minutemystery-a-straw-stuffed-mystery
Bill Albertson is guilty: True or False?
True (0.6513548405484016)
Bill Albertson is not guilty: True or False?
True (0.5660185351323219)
Bill Albertson has mean: True or False?
True (0.5832033352502285)
Bill Albertson has no mean: True or False?
False (0.615087855649269)
Bill Albertson has motive: True or False?
True (0.8688267468984366)
Bill Albertson has no motive: True or False?
False (0.5214711377329961)
Bill Albertson has opportunity: True or False?
True (0.5563995964631269)
Bill Albertson has no opportunity: True or False?
False (0.6379335503198971)
Mr. Fletcher is guilty: True or False?
True (0.5888891620166576)
Mr. Fletcher is not guilty: True or False?
True (0.5525396910980834)
Mr. Fletcher has mean: True or False?
False (0.642432441257838)
Mr. Fletcher has no mean: True or False?
False (0.8092759828926619)
Mr. Fletcher has motive: True or False?
True (0.769080279275001)
Mr. Fletcher has no motive: True or False?
True (0.5409238326546766)
Mr. Fletcher has opportunity: True or False?
True (0.6522414018725713)
Mr. Fletcher has no opportunity: True or False?
False (0.7325918054337844)
Professor Surenie is guilty: True or False?
True (0.5936093435000638)
Professor Surenie is not guilty: True or False?
True (0.5660185351323219)
Professor Surenie has mean: True or False?
False (0.5917232019857303)
Professor Surenie has no mean: True or False?
False (0.7476159279883341)
Professor Surenie has motive: True or False?
True (0.8227595062673136)
Professor Surenie has no motive: True or False?
True (0.5736783792247284)
Professor Surenie has opportunity: True or False?
False (0.5204963206682631)
Professor Surenie has no opportunity: True or False?
False (0.6206215556999736)
Rachel Beaton is guilty: True or False?
False (0.5058591351869154)
Rachel Beaton is not guilty: True or False?
False (0.5156199352405011)
Rachel Beaton has mean: True or False?
True (0.525368812147771)
Rachel Beaton has no mean: True or False?
False (0.6671476985798853)
Rachel Beaton has motive: True or False?
True (0.7170118721569225)
Rachel Beaton has no motive: True or False?
True (0.5292633777076584)
Rachel Beaton has opportunity: True or False?
False (0.6774740084332073)
Rachel Beaton has no opportunity: True or False?
False (0.6825737331070684)
### Bill Albertson
- mean: True (0.5832033352502285)
- motive: True (0.8688267468984366)
- opportunity: True (0.5563995964631269)

### Mr. Fletcher
- mean: False (0.642432441257838)
- motive: False (0.4590761673453234)
- opportunity: False (0.0)

### Professor Surenie
- mean: False (0.5917232019857303)
- motive: False (0.4263216207752716)
- opportunity: False (0.5204963206682631)

### Rachel Beaton
- mean: False (0.0)
- motive: False (0.4707366222923416)
- opportunity: False (0.6774740084332073)

The culprit is Bill Albertson.
In fact, it is Mr. Fletcher.
## 5minutemystery-ask-marthathe-shoplifter
Jane Croydon is guilty: True or False?
True (0.8019357965963964)
Jane Croydon is not guilty: True or False?
True (0.6976088896786037)
Jane Croydon has mean: True or False?
True (0.7310585348819939)
Jane Croydon has no mean: True or False?
True (0.6274947415194492)
Jane Croydon has motive: True or False?
True (0.770464837675413)
Jane Croydon has no motive: True or False?
True (0.5535053004623279)
Jane Croydon has opportunity: True or False?
False (0.5631377056275331)
Jane Croydon has no opportunity: True or False?
False (0.701713020301745)
Johnny Martin is guilty: True or False?
True (0.9024378096057211)
Johnny Martin is not guilty: True or False?
True (0.862930245043327)
Johnny Martin has mean: True or False?
True (0.7826625131049049)
Johnny Martin has no mean: True or False?
True (0.7950222460539826)
Johnny Martin has motive: True or False?
True (0.8526903338256402)
Johnny Martin has no motive: True or False?
Map:  59%|█████▊    | 119/203 [1:15:23<50:51, 36.33s/ examples]Map:  59%|█████▉    | 120/203 [1:15:55<48:33, 35.11s/ examples]Map:  60%|█████▉    | 121/203 [1:16:31<48:26, 35.44s/ examples]True (0.6343168082332088)
Johnny Martin has opportunity: True or False?
True (0.816406362162552)
Johnny Martin has no opportunity: True or False?
True (0.6325027218909103)
Martha Hampden is guilty: True or False?
True (0.776283919986686)
Martha Hampden is not guilty: True or False?
True (0.7728736896481636)
Martha Hampden has mean: True or False?
True (0.7648916137833577)
Martha Hampden has no mean: True or False?
True (0.708212608228071)
Martha Hampden has motive: True or False?
True (0.6719012932095527)
Martha Hampden has no motive: True or False?
False (0.5438325284393795)
Martha Hampden has opportunity: True or False?
False (0.5248817856312722)
Martha Hampden has no opportunity: True or False?
False (0.6951311179371613)
Steve Kravitz is guilty: True or False?
True (0.8774768149941248)
Steve Kravitz is not guilty: True or False?
True (0.8620035048683017)
Steve Kravitz has mean: True or False?
True (0.64779823427608)
Steve Kravitz has no mean: True or False?
True (0.5438324636094939)
Steve Kravitz has motive: True or False?
True (0.7869504648517817)
Steve Kravitz has no motive: True or False?
True (0.6011253583932805)
Steve Kravitz has opportunity: True or False?
True (0.5278033071427191)
Steve Kravitz has no opportunity: True or False?
False (0.7166154443253638)
### Jane Croydon
- mean: False (0.3725052584805508)
- motive: False (0.44649469953767207)
- opportunity: False (0.5631377056275331)

### Johnny Martin
- mean: False (0.20497775394601736)
- motive: False (0.3656831917667912)
- opportunity: False (0.3674972781090897)

### Martha Hampden
- mean: True (0.7648916137833577)
- motive: True (0.6719012932095527)
- opportunity: True (0.3048688820628387)

### Steve Kravitz
- mean: False (0.4561675363905061)
- motive: False (0.3988746416067195)
- opportunity: False (0.0)

The culprit is Martha Hampden.
In fact, it is Johnny Martin.
## 5minutemystery-the-hanging-figure
Daisy Morris is guilty: True or False?
True (0.6627964974378784)
Daisy Morris is not guilty: True or False?
True (0.627038178044588)
Daisy Morris has mean: True or False?
True (0.5477060677900649)
Daisy Morris has no mean: True or False?
False (0.5746334908651781)
Daisy Morris has motive: True or False?
True (0.7248703250005105)
Daisy Morris has no motive: True or False?
True (0.5039061393777357)
Daisy Morris has opportunity: True or False?
True (0.5214711377329961)
Daisy Morris has no opportunity: True or False?
False (0.7225270177274575)
Dale Clark is guilty: True or False?
True (0.6334102859975052)
Dale Clark is not guilty: True or False?
True (0.6451199006197486)
Dale Clark has mean: True or False?
True (0.8615382357584752)
Dale Clark has no mean: True or False?
True (0.5341265295318852)
Dale Clark has motive: True or False?
True (0.65489470935198)
Dale Clark has no motive: True or False?
False (0.5563995964631269)
Dale Clark has opportunity: True or False?
False (0.5224457875179084)
Dale Clark has no opportunity: True or False?
False (0.7739006258141444)
Iain Potts is guilty: True or False?
True (0.5583270361921496)
Iain Potts is not guilty: True or False?
True (0.6352223750575562)
Iain Potts has mean: True or False?
True (0.8255897087847518)
Iain Potts has no mean: True or False?
False (0.5399537164111071)
Iain Potts has motive: True or False?
True (0.7648916137833577)
Iain Potts has no motive: True or False?
False (0.5087881220234095)
Iain Potts has opportunity: True or False?
False (0.5917232019857303)
Iain Potts has no opportunity: True or False?
False (0.8238958672039278)
Lucy Smith is guilty: True or False?
True (0.740174341079517)
Lucy Smith is not guilty: True or False?
True (0.6783269591477166)
Lucy Smith has mean: True or False?
True (0.7745833916423246)
Lucy Smith has no mean: True or False?
False (0.580352087772514)
Lucy Smith has motive: True or False?
True (0.7872777601997338)
Lucy Smith has no motive: True or False?
False (0.5273165696704634)
Lucy Smith has opportunity: True or False?
True (0.5535053004623279)
Lucy Smith has no opportunity: True or False?
False (0.7154240000492645)
### Daisy Morris
- mean: False (0.0)
- motive: False (0.49609386062226435)
- opportunity: False (0.0)

### Dale Clark
- mean: False (0.4658734704681148)
- motive: False (0.0)
- opportunity: False (0.5224457875179084)

### Iain Potts
- mean: False (0.0)
- motive: False (0.0)
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
Coach Roster is not guilty: True or False?
True (0.8962513214730718)
Coach Roster has mean: True or False?
True (0.7386690294153369)
Coach Roster has no mean: True or False?
False (0.5822535180679596)
Coach Roster has motive: True or False?
True (0.8037906314112822)
Coach Roster has no motive: True or False?
True (0.8233284353620131)
Coach Roster has opportunity: True or False?
True (0.7356416476869558)
Coach Roster has no opportunity: True or False?
True (0.7310585348819939)
Eddie is guilty: True or False?
True (0.6206215556999736)
Eddie is not guilty: True or False?
True (0.6976089520497016)
Eddie has mean: True or False?
False (0.5039061393777357)
Eddie has no mean: True or False?
False (0.6671476389322356)
Eddie has motive: True or False?
False (0.615087855649269)
Eddie has no motive: True or False?
False (0.7534666630720156)
Eddie has opportunity: True or False?
False (0.570809902165233)
Eddie has no opportunity: True or False?
False (0.8300437877296776)
Eddie's Mom is guilty: True or False?
True (0.791821116278941)
Eddie's Mom is not guilty: True or False?
True (0.7512834059294674)
Eddie's Mom has mean: True or False?
False (0.6215409675616889)
Eddie's Mom has no mean: True or False?
False (0.6749080895533367)
Eddie's Mom has motive: True or False?
True (0.7937461674149602)
Eddie's Mom has no motive: True or False?
False (0.6584175136252488)
Eddie's Mom has opportunity: True or False?
False (0.5204963206682631)
Eddie's Mom has no opportunity: True or False?
False (0.72951977676791)
Marissa is guilty: True or False?
True (0.6141626144170799)
Marissa is not guilty: True or False?
True (0.7017130830397807)
Marissa has mean: True or False?
False (0.5117165908639297)
Marissa has no mean: True or False?
False (0.8227595062673136)
Marissa has motive: True or False?
False (0.591723272524637)
Marissa has no motive: True or False?
False (0.7310585348819939)
Marissa has opportunity: True or False?
False (0.6654105193867614)
Marissa has no opportunity: True or False?
False (0.8474634858439474)
### Coach Roster
- mean: False (0.0)
- motive: False (0.17667156463798694)
- opportunity: False (0.2689414651180061)

### Eddie
- mean: False (0.5039061393777357)
- motive: False (0.615087855649269)
- opportunity: False (0.570809902165233)

### Eddie's Mom
- mean: True (0.3250919104466633)
- motive: True (0.7937461674149602)
- opportunity: True (0.27048022323209)

### Marissa
- mean: False (0.5117165908639297)
- motive: False (0.591723272524637)
- opportunity: False (0.6654105193867614)

The culprit is Eddie's Mom.
In fact, it is Eddie's Mom.
## 5minutemystery-ask-marthathe-case-of-the-missing-canary
Alex Johnston is guilty: True or False?
True (0.591723272524637)
Alex Johnston is not guilty: True or False?
True (0.5282900845448565)
Alex Johnston has mean: True or False?
True (0.5926666351772785)
Alex Johnston has no mean: True or False?
False (0.6859494535376744)
Alex Johnston has motive: True or False?
True (0.7599387683150569)
Alex Johnston has no motive: True or False?
True (0.5019531141001669)
Alex Johnston has opportunity: True or False?
True (0.5583269696343842)
Alex Johnston has no opportunity: True or False?
False (0.8031737798924701)
Jimmy Carstairs is guilty: True or False?
True (0.5360699771890155)
Jimmy Carstairs is not guilty: True or False?
True (0.5165954726976894)
Jimmy Carstairs has mean: True or False?
True (0.7962924261546153)
Jimmy Carstairs has no mean: True or False?
True (0.5350984235603058)
Jimmy Carstairs has motive: True or False?
True (0.7325918709325988)
Map:  60%|██████    | 122/203 [1:17:04<46:49, 34.68s/ examples]Map:  61%|██████    | 123/203 [1:17:38<45:49, 34.37s/ examples]Map:  61%|██████    | 124/203 [1:18:30<52:06, 39.58s/ examples]Jimmy Carstairs has no motive: True or False?
False (0.5282900845448565)
Jimmy Carstairs has opportunity: True or False?
True (0.6379335503198971)
Jimmy Carstairs has no opportunity: True or False?
False (0.7217432334405754)
Lydia Carstairs is guilty: True or False?
False (0.5068355091660127)
Lydia Carstairs is not guilty: True or False?
False (0.5312093941731293)
Lydia Carstairs has mean: True or False?
True (0.6619228707202935)
Lydia Carstairs has no mean: True or False?
False (0.5243946792389143)
Lydia Carstairs has motive: True or False?
True (0.7082125449089324)
Lydia Carstairs has no motive: True or False?
True (0.5418937216067536)
Lydia Carstairs has opportunity: True or False?
True (0.5708098341193941)
Lydia Carstairs has no opportunity: True or False?
False (0.8128672807499561)
Sarabelle is guilty: True or False?
True (0.6671476389322356)
Sarabelle is not guilty: True or False?
True (0.6774740084332073)
Sarabelle has mean: True or False?
True (0.6893056096647525)
Sarabelle has no mean: True or False?
True (0.514644215419305)
Sarabelle has motive: True or False?
True (0.8294920340613177)
Sarabelle has no motive: True or False?
True (0.7114308965749192)
Sarabelle has opportunity: True or False?
True (0.5869964306477841)
Sarabelle has no opportunity: True or False?
False (0.6522414018725713)
### Alex Johnston
- mean: True (0.5926666351772785)
- motive: True (0.7599387683150569)
- opportunity: True (0.5583269696343842)

### Jimmy Carstairs
- mean: False (0.4649015764396942)
- motive: False (0.0)
- opportunity: False (0.0)

### Lydia Carstairs
- mean: False (0.0)
- motive: False (0.45810627839324636)
- opportunity: False (0.0)

### Sarabelle
- mean: False (0.48535578458069495)
- motive: False (0.2885691034250808)
- opportunity: False (0.0)

The culprit is Alex Johnston.
In fact, it is Alex Johnston.
## 5minutemystery-register-robbery
Dan is guilty: True or False?
True (0.7969253675907205)
Dan is not guilty: True or False?
True (0.7082125449089324)
Dan has mean: True or False?
True (0.7146279861809854)
Dan has no mean: True or False?
True (0.5058591351869154)
Dan has motive: True or False?
True (0.7839884107482739)
Dan has no motive: True or False?
False (0.6242935037467142)
Dan has opportunity: True or False?
True (0.5360700410935405)
Dan has no opportunity: True or False?
False (0.8397339530959691)
David is guilty: True or False?
True (0.7793217912837537)
David is not guilty: True or False?
True (0.6791786560103119)
David has mean: True or False?
True (0.7033457082786769)
David has no mean: True or False?
True (0.5087881523495457)
David has motive: True or False?
True (0.784649255215384)
David has no motive: True or False?
False (0.5350984235603058)
David has opportunity: True or False?
True (0.5822535180679596)
David has no opportunity: True or False?
False (0.7318258918270596)
Robert is guilty: True or False?
True (0.8740772044235984)
Robert is not guilty: True or False?
True (0.7620701143808404)
Robert has mean: True or False?
True (0.7409249450892966)
Robert has no mean: True or False?
True (0.5292633777076584)
Robert has motive: True or False?
True (0.8727816933272936)
Robert has no motive: True or False?
False (0.5907791930117218)
Robert has opportunity: True or False?
True (0.6531268925247615)
Robert has no opportunity: True or False?
False (0.8289387819824735)
Teresa is guilty: True or False?
True (0.7527403228571042)
Teresa is not guilty: True or False?
True (0.5708098341193941)
Teresa has mean: True or False?
True (0.6522414018725713)
Teresa has no mean: True or False?
False (0.5467381591701916)
Teresa has motive: True or False?
True (0.8606036289596553)
Teresa has no motive: True or False?
False (0.6540113633452196)
Teresa has opportunity: True or False?
True (0.5418937216067536)
Teresa has no opportunity: True or False?
False (0.8824278139880716)
### Dan
- mean: False (0.4941408648130846)
- motive: False (0.0)
- opportunity: False (0.0)

### David
- mean: False (0.49121184765045434)
- motive: False (0.0)
- opportunity: False (0.0)

### Robert
- mean: False (0.4707366222923416)
- motive: False (0.0)
- opportunity: False (0.0)

### Teresa
- mean: True (0.6522414018725713)
- motive: True (0.8606036289596553)
- opportunity: True (0.5418937216067536)

The culprit is Teresa.
In fact, it is David.
## 5minutemystery-mr-patrick-back-in-class
CSA currency is guilty: True or False?
True (0.8723473540228537)
CSA currency is not guilty: True or False?
True (0.9184802773231918)
CSA currency has mean: True or False?
True (0.9029524325377104)
CSA currency has no mean: True or False?
True (0.8745065279415651)
CSA currency has motive: True or False?
True (0.8745065279415651)
CSA currency has no motive: True or False?
True (0.927887794449634)
CSA currency has opportunity: True or False?
True (0.8370879250561812)
CSA currency has no opportunity: True or False?
True (0.8316906059841959)
Diamond necklace is guilty: True or False?
True (0.6001883860246252)
Diamond necklace is not guilty: True or False?
True (0.5746334908651781)
Diamond necklace has mean: True or False?
True (0.7662936378892937)
Diamond necklace has no mean: True or False?
True (0.6242935037467142)
Diamond necklace has motive: True or False?
True (0.6592954931819778)
Diamond necklace has no motive: True or False?
False (0.5078118910577802)
Diamond necklace has opportunity: True or False?
True (0.5234203246639862)
Diamond necklace has no opportunity: True or False?
False (0.51464427676968)
Gold money clip is guilty: True or False?
True (0.8134607635851566)
Gold money clip is not guilty: True or False?
True (0.8044059309478723)
Gold money clip has mean: True or False?
True (0.8504686406728537)
Gold money clip has no mean: True or False?
True (0.6619228707202935)
Gold money clip has motive: True or False?
True (0.7356416476869558)
Gold money clip has no motive: True or False?
True (0.6575384105121485)
Gold money clip has opportunity: True or False?
True (0.6757646168022439)
Gold money clip has no opportunity: True or False?
True (0.5331544304756466)
Jewel encrusted pistol is guilty: True or False?
True (0.7520125537161032)
Jewel encrusted pistol is not guilty: True or False?
True (0.7379143332111532)
Jewel encrusted pistol has mean: True or False?
True (0.7490872087035162)
Jewel encrusted pistol has no mean: True or False?
True (0.7146280926688615)
Jewel encrusted pistol has motive: True or False?
True (0.7461389980806673)
Jewel encrusted pistol has no motive: True or False?
True (0.6011253583932805)
Jewel encrusted pistol has opportunity: True or False?
True (0.6800292740030767)
Jewel encrusted pistol has no opportunity: True or False?
True (0.5669777909748143)
Lithograph photo is guilty: True or False?
True (0.7534666630720156)
Lithograph photo is not guilty: True or False?
True (0.7779753136455794)
Lithograph photo has mean: True or False?
True (0.8349459127213729)
Lithograph photo has no mean: True or False?
True (0.7049732238008671)
Lithograph photo has motive: True or False?
True (0.7585105966624085)
Lithograph photo has no motive: True or False?
True (0.5107405249783342)
Lithograph photo has opportunity: True or False?
True (0.7826625131049049)
Lithograph photo has no opportunity: True or False?
True (0.595492552580428)
### CSA currency
- mean: False (0.12549347205843486)
- motive: False (0.07211220555036602)
- opportunity: False (0.16830939401580414)

### Diamond necklace
- mean: True (0.7662936378892937)
- motive: True (0.6592954931819778)
- opportunity: True (0.5234203246639862)

### Gold money clip
- mean: False (0.33807712927970646)
- motive: False (0.34246158948785155)
- opportunity: False (0.4668455695243534)

### Jewel encrusted pistol
- mean: False (0.2853719073311385)
- motive: False (0.3988746416067195)
- opportunity: False (0.43302220902518573)

### Lithograph photo
- mean: False (0.29502677619913287)
- motive: False (0.4892594750216658)
- opportunity: False (0.404507447419572)

The culprit is Diamond necklace.
In fact, it is Lithograph photo.
## 5minutemystery-ask-marthathe-blackmailer
Horace Sage is guilty: True or False?
True (0.9010534302227574)
Horace Sage is not guilty: True or False?
True (0.8584814679672361)
Horace Sage has mean: True or False?
Map:  62%|██████▏   | 125/203 [1:19:08<50:58, 39.21s/ examples]Map:  62%|██████▏   | 126/203 [1:19:51<51:33, 40.18s/ examples]True (0.7806624796117883)
Horace Sage has no mean: True or False?
True (0.6610481693322063)
Horace Sage has motive: True or False?
True (0.900179384114949)
Horace Sage has no motive: True or False?
True (0.7641883982873323)
Horace Sage has opportunity: True or False?
True (0.7742421642081551)
Horace Sage has no opportunity: True or False?
True (0.581778392154428)
Martin Amberton is guilty: True or False?
True (0.8812066389307215)
Martin Amberton is not guilty: True or False?
True (0.8040984260198152)
Martin Amberton has mean: True or False?
True (0.8095772283237919)
Martin Amberton has no mean: True or False?
True (0.5568816117266226)
Martin Amberton has motive: True or False?
True (0.8107787408238168)
Martin Amberton has no motive: True or False?
True (0.5631377056275331)
Martin Amberton has opportunity: True or False?
True (0.8185918283825985)
Martin Amberton has no opportunity: True or False?
False (0.5794004215835179)
Mary Devers is guilty: True or False?
True (0.6169357925086439)
Mary Devers is not guilty: True or False?
True (0.5822535180679596)
Mary Devers has mean: True or False?
True (0.7146280500737092)
Mary Devers has no mean: True or False?
False (0.6504672743423094)
Mary Devers has motive: True or False?
True (0.591723272524637)
Mary Devers has no motive: True or False?
False (0.5679366075542497)
Mary Devers has opportunity: True or False?
True (0.5765419579552815)
Mary Devers has no opportunity: True or False?
False (0.7364006034245382)
Susan Royster is guilty: True or False?
True (0.8074606715677252)
Susan Royster is not guilty: True or False?
True (0.7527403228571042)
Susan Royster has mean: True or False?
True (0.9017477662022706)
Susan Royster has no mean: True or False?
True (0.6658452726989639)
Susan Royster has motive: True or False?
True (0.7424217332471881)
Susan Royster has no motive: True or False?
True (0.7142295345107396)
Susan Royster has opportunity: True or False?
True (0.729905005312225)
Susan Royster has no opportunity: True or False?
False (0.5087881523495457)
### Horace Sage
- mean: False (0.33895183066779366)
- motive: False (0.23581160171266768)
- opportunity: False (0.41822160784557205)

### Martin Amberton
- mean: False (0.44311838827337735)
- motive: False (0.43686229437246693)
- opportunity: False (0.0)

### Mary Devers
- mean: True (0.7146280500737092)
- motive: True (0.591723272524637)
- opportunity: True (0.5765419579552815)

### Susan Royster
- mean: False (0.3341547273010361)
- motive: False (0.28577046548926044)
- opportunity: False (0.0)

The culprit is Mary Devers.
In fact, it is Mary Devers.
## 5minutemystery-a-dream-of-old-salem
Abigail Thorpe is guilty: True or False?
True (0.8670357473609658)
Abigail Thorpe is not guilty: True or False?
True (0.8636218294491105)
Abigail Thorpe has mean: True or False?
True (0.8068526417769779)
Abigail Thorpe has no mean: True or False?
True (0.767689835247798)
Abigail Thorpe has motive: True or False?
True (0.7728736896481636)
Abigail Thorpe has no motive: True or False?
True (0.6947170558884102)
Abigail Thorpe has opportunity: True or False?
True (0.5983121871760707)
Abigail Thorpe has no opportunity: True or False?
False (0.5727227727404994)
Adam Browne is guilty: True or False?
True (0.8418256009501243)
Adam Browne is not guilty: True or False?
True (0.883638264557296)
Adam Browne has mean: True or False?
True (0.7676898810056793)
Adam Browne has no mean: True or False?
True (0.7588681623522538)
Adam Browne has motive: True or False?
True (0.7989721855047863)
Adam Browne has no motive: True or False?
True (0.7512834059294674)
Adam Browne has opportunity: True or False?
True (0.7680379714749807)
Adam Browne has no opportunity: True or False?
False (0.5774954003013352)
Goodwife Browne is guilty: True or False?
True (0.8615382357584752)
Goodwife Browne is not guilty: True or False?
True (0.884439109617765)
Goodwife Browne has mean: True or False?
True (0.8933093589621482)
Goodwife Browne has no mean: True or False?
True (0.8638516611889259)
Goodwife Browne has motive: True or False?
True (0.8596637847360897)
Goodwife Browne has no motive: True or False?
True (0.8134607635851566)
Goodwife Browne has opportunity: True or False?
True (0.8785228180531032)
Goodwife Browne has no opportunity: True or False?
True (0.7229183995281547)
Sarah Goodwin is guilty: True or False?
True (0.5717666110200305)
Sarah Goodwin is not guilty: True or False?
True (0.6627964974378784)
Sarah Goodwin has mean: True or False?
True (0.8305940642606888)
Sarah Goodwin has no mean: True or False?
True (0.6297745735138451)
Sarah Goodwin has motive: True or False?
True (0.7382918489137783)
Sarah Goodwin has no motive: True or False?
False (0.5525396910980834)
Sarah Goodwin has opportunity: True or False?
True (0.525368812147771)
Sarah Goodwin has no opportunity: True or False?
False (0.7498207054286419)
### Abigail Thorpe
- mean: False (0.232310164752202)
- motive: False (0.30528294411158985)
- opportunity: False (0.0)

### Adam Browne
- mean: False (0.24113183764774615)
- motive: False (0.2487165940705326)
- opportunity: False (0.0)

### Goodwife Browne
- mean: False (0.13614833881107413)
- motive: False (0.18653923641484338)
- opportunity: False (0.27708160047184527)

### Sarah Goodwin
- mean: True (0.8305940642606888)
- motive: True (0.7382918489137783)
- opportunity: True (0.525368812147771)

The culprit is Sarah Goodwin.
In fact, it is Adam Browne.
## 5minutemystery-the-antique-clock-mystery
The grandfather clock (stopped at 10:10 p.m.) is guilty: True or False?
True (0.6279512069990912)
The grandfather clock (stopped at 10:10 p.m.) is not guilty: True or False?
True (0.6224592927728324)
The grandfather clock (stopped at 10:10 p.m.) has mean: True or False?
True (0.8283841584202847)
The grandfather clock (stopped at 10:10 p.m.) has no mean: True or False?
True (0.8365545874520802)
The grandfather clock (stopped at 10:10 p.m.) has motive: True or False?
True (0.878314250659373)
The grandfather clock (stopped at 10:10 p.m.) has no motive: True or False?
True (0.7017130830397807)
The grandfather clock (stopped at 10:10 p.m.) has opportunity: True or False?
True (0.8140528237853677)
The grandfather clock (stopped at 10:10 p.m.) has no opportunity: True or False?
True (0.7683857617837733)
The mantle clock (stopped at 10:59 p.m.) is guilty: True or False?
True (0.6757646168022439)
The mantle clock (stopped at 10:59 p.m.) is not guilty: True or False?
True (0.5698526542706361)
The mantle clock (stopped at 10:59 p.m.) has mean: True or False?
True (0.7333563569098757)
The mantle clock (stopped at 10:59 p.m.) has no mean: True or False?
True (0.705785027818136)
The mantle clock (stopped at 10:59 p.m.) has motive: True or False?
True (0.8019358443954961)
The mantle clock (stopped at 10:59 p.m.) has no motive: True or False?
True (0.6654105193867614)
The mantle clock (stopped at 10:59 p.m.) has opportunity: True or False?
True (0.7859664553110391)
The mantle clock (stopped at 10:59 p.m.) has no opportunity: True or False?
True (0.7779753136455794)
The pocket watch (stopped at 3:18 a.m.) is guilty: True or False?
True (0.6926419789019715)
The pocket watch (stopped at 3:18 a.m.) is not guilty: True or False?
True (0.6749080895533367)
The pocket watch (stopped at 3:18 a.m.) has mean: True or False?
True (0.874934615163517)
The pocket watch (stopped at 3:18 a.m.) has no mean: True or False?
True (0.6876299924560524)
The pocket watch (stopped at 3:18 a.m.) has motive: True or False?
True (0.844921525814193)
The pocket watch (stopped at 3:18 a.m.) has no motive: True or False?
True (0.702530072932436)
The pocket watch (stopped at 3:18 a.m.) has opportunity: True or False?
True (0.854884620116169)
The pocket watch (stopped at 3:18 a.m.) has no opportunity: True or False?
True (0.8529354946829077)
The wall clock (stopped at 2:01 a.m.) is guilty: True or False?
True (0.7098243920264812)
The wall clock (stopped at 2:01 a.m.) is not guilty: True or False?
True (0.6522414018725713)
The wall clock (stopped at 2:01 a.m.) has mean: True or False?
True (0.7620701143808404)
The wall clock (stopped at 2:01 a.m.) has no mean: True or False?
True (0.7170118721569225)
Map:  63%|██████▎   | 127/203 [1:20:33<51:54, 40.98s/ examples]Map:  63%|██████▎   | 128/203 [1:21:17<52:23, 41.91s/ examples]Map:  64%|██████▎   | 129/203 [1:22:05<53:53, 43.69s/ examples]The wall clock (stopped at 2:01 a.m.) has motive: True or False?
True (0.8489722037469682)
The wall clock (stopped at 2:01 a.m.) has no motive: True or False?
True (0.725648573585541)
The wall clock (stopped at 2:01 a.m.) has opportunity: True or False?
True (0.8278281666221954)
The wall clock (stopped at 2:01 a.m.) has no opportunity: True or False?
True (0.8386797935187188)
The wristwatch (stopped at 5:22 p.m.) is guilty: True or False?
True (0.5224458497983033)
The wristwatch (stopped at 5:22 p.m.) is not guilty: True or False?
False (0.5224457875179084)
The wristwatch (stopped at 5:22 p.m.) has mean: True or False?
True (0.784649255215384)
The wristwatch (stopped at 5:22 p.m.) has no mean: True or False?
True (0.5467381591701916)
The wristwatch (stopped at 5:22 p.m.) has motive: True or False?
True (0.7264255794048772)
The wristwatch (stopped at 5:22 p.m.) has no motive: True or False?
True (0.5679366075542497)
The wristwatch (stopped at 5:22 p.m.) has opportunity: True or False?
True (0.7325918709325988)
The wristwatch (stopped at 5:22 p.m.) has no opportunity: True or False?
True (0.7240905804783984)
### The grandfather clock (stopped at 10:10 p.m.)
- mean: False (0.16344541254791978)
- motive: False (0.29828691696021925)
- opportunity: False (0.23161423821622673)

### The mantle clock (stopped at 10:59 p.m.)
- mean: True (0.7333563569098757)
- motive: True (0.8019358443954961)
- opportunity: True (0.7859664553110391)

### The pocket watch (stopped at 3:18 a.m.)
- mean: False (0.3123700075439476)
- motive: False (0.29746992706756403)
- opportunity: False (0.14706450531709225)

### The wall clock (stopped at 2:01 a.m.)
- mean: False (0.2829881278430775)
- motive: False (0.274351426414459)
- opportunity: False (0.1613202064812812)

### The wristwatch (stopped at 5:22 p.m.)
- mean: False (0.45326184082980836)
- motive: False (0.4320633924457503)
- opportunity: False (0.27590941952160164)

The culprit is The mantle clock (stopped at 10:59 p.m.).
In fact, it is The mantle clock (stopped at 10:59 p.m.).
## 5minutemystery-ask-marthathe-perjurer
Horace Osamway is guilty: True or False?
True (0.9472835653937188)
Horace Osamway is not guilty: True or False?
True (0.9253649712078899)
Horace Osamway has mean: True or False?
True (0.8140527631337082)
Horace Osamway has no mean: True or False?
True (0.7279754274224494)
Horace Osamway has motive: True or False?
True (0.8770562402180104)
Horace Osamway has no motive: True or False?
True (0.8047130138702729)
Horace Osamway has opportunity: True or False?
True (0.8253083182831968)
Horace Osamway has no opportunity: True or False?
True (0.645566946242049)
John Eberley is guilty: True or False?
True (0.9122799654606127)
John Eberley is not guilty: True or False?
True (0.9103861443438126)
John Eberley has mean: True or False?
True (0.8370879250561812)
John Eberley has no mean: True or False?
True (0.7379142672364736)
John Eberley has motive: True or False?
True (0.8101787517928931)
John Eberley has no motive: True or False?
True (0.7624240410769517)
John Eberley has opportunity: True or False?
True (0.6693127155643409)
John Eberley has no opportunity: True or False?
True (0.5375269636724329)
Martha Cranston is guilty: True or False?
True (0.8213309048233545)
Martha Cranston is not guilty: True or False?
True (0.7479842962504842)
Martha Cranston has mean: True or False?
True (0.7505527730327083)
Martha Cranston has no mean: True or False?
True (0.5048826258478675)
Martha Cranston has motive: True or False?
True (0.6256667878365441)
Martha Cranston has no motive: True or False?
True (0.51464427676968)
Martha Cranston has opportunity: True or False?
True (0.5907791930117218)
Martha Cranston has no opportunity: True or False?
False (0.7759445334082792)
Mildred Greene is guilty: True or False?
True (0.8887587777822111)
Mildred Greene is not guilty: True or False?
True (0.8368214319827847)
Mildred Greene has mean: True or False?
True (0.7879311977554747)
Mildred Greene has no mean: True or False?
True (0.5224458497983033)
Mildred Greene has motive: True or False?
True (0.7225270177274575)
Mildred Greene has no motive: True or False?
True (0.638384519849353)
Mildred Greene has opportunity: True or False?
True (0.7786493288700866)
Mildred Greene has no opportunity: True or False?
False (0.5029296829424847)
### Horace Osamway
- mean: False (0.27202457257755064)
- motive: False (0.19528698612972706)
- opportunity: False (0.354433053757951)

### John Eberley
- mean: False (0.2620857327635264)
- motive: False (0.23757595892304828)
- opportunity: False (0.4624730363275671)

### Martha Cranston
- mean: True (0.7505527730327083)
- motive: True (0.6256667878365441)
- opportunity: True (0.5907791930117218)

### Mildred Greene
- mean: False (0.47755415020169667)
- motive: False (0.36161548015064704)
- opportunity: False (0.0)

The culprit is Martha Cranston.
In fact, it is John Eberley.
## 5minutemystery-ask-marthathe-embezzler
Joan Carstairs is guilty: True or False?
True (0.8647679660788636)
Joan Carstairs is not guilty: True or False?
True (0.785637679813794)
Joan Carstairs has mean: True or False?
True (0.84440905415483)
Joan Carstairs has no mean: True or False?
True (0.8244619332958376)
Joan Carstairs has motive: True or False?
True (0.8778961263000082)
Joan Carstairs has no motive: True or False?
True (0.7185944237486072)
Joan Carstairs has opportunity: True or False?
True (0.8426043397677332)
Joan Carstairs has no opportunity: True or False?
False (0.5907791930117218)
Les Nolting is guilty: True or False?
True (0.8591918406281239)
Les Nolting is not guilty: True or False?
True (0.7229183995281547)
Les Nolting has mean: True or False?
True (0.8795611817678315)
Les Nolting has no mean: True or False?
True (0.7570766705324253)
Les Nolting has motive: True or False?
True (0.8665847814067802)
Les Nolting has no motive: True or False?
True (0.7756047866813147)
Les Nolting has opportunity: True or False?
True (0.8051730422074252)
Les Nolting has no opportunity: True or False?
True (0.5751108029857721)
Paul Brassard is guilty: True or False?
True (0.908941745727715)
Paul Brassard is not guilty: True or False?
True (0.7776377832420203)
Paul Brassard has mean: True or False?
True (0.9074763054739992)
Paul Brassard has no mean: True or False?
True (0.7538293096563191)
Paul Brassard has motive: True or False?
True (0.8819203351368529)
Paul Brassard has no motive: True or False?
True (0.7690802105138688)
Paul Brassard has opportunity: True or False?
True (0.7796575431744809)
Paul Brassard has no opportunity: True or False?
True (0.5636181674054062)
Sarah Kimble is guilty: True or False?
True (0.8056321690561029)
Sarah Kimble is not guilty: True or False?
True (0.7490872087035162)
Sarah Kimble has mean: True or False?
True (0.8980535302052036)
Sarah Kimble has no mean: True or False?
True (0.7759445334082792)
Sarah Kimble has motive: True or False?
True (0.8994751578343994)
Sarah Kimble has no motive: True or False?
True (0.6980207435948766)
Sarah Kimble has opportunity: True or False?
True (0.7966091010940959)
Sarah Kimble has no opportunity: True or False?
True (0.5331543669186894)
### Joan Carstairs
- mean: True (0.84440905415483)
- motive: True (0.8778961263000082)
- opportunity: True (0.8426043397677332)

### Les Nolting
- mean: False (0.24292332946757467)
- motive: False (0.22439521331868528)
- opportunity: False (0.4248891970142279)

### Paul Brassard
- mean: False (0.2461706903436809)
- motive: False (0.23091978948613123)
- opportunity: False (0.43638183259459384)

### Sarah Kimble
- mean: False (0.22405546659172082)
- motive: False (0.30197925640512335)
- opportunity: False (0.46684563308131055)

The culprit is Joan Carstairs.
In fact, it is Sarah Kimble.
## 5minutemystery-the-backyard-slumber-party
Justin Scott is guilty: True or False?
True (0.8316905440184192)
Justin Scott is not guilty: True or False?
True (0.7613611200983542)
Justin Scott has mean: True or False?
True (0.8710367026584496)
Justin Scott has no mean: True or False?
True (0.6697447888921682)
Justin Scott has motive: True or False?
True (0.7950222460539826)
Justin Scott has no motive: True or False?
True (0.5869964306477841)
Map:  64%|██████▍   | 130/203 [1:22:41<50:06, 41.19s/ examples]Map:  65%|██████▍   | 131/203 [1:23:26<50:58, 42.48s/ examples]Map:  65%|██████▌   | 132/203 [1:24:00<47:22, 40.03s/ examples]Justin Scott has opportunity: True or False?
True (0.6315943123389512)
Justin Scott has no opportunity: True or False?
False (0.5907791930117218)
Martin Simmons is guilty: True or False?
True (0.7859664553110391)
Martin Simmons is not guilty: True or False?
True (0.6178585826183487)
Martin Simmons has mean: True or False?
True (0.6141626144170799)
Martin Simmons has no mean: True or False?
False (0.6270381219830087)
Martin Simmons has motive: True or False?
True (0.6934729182490079)
Martin Simmons has no motive: True or False?
False (0.5660185688696566)
Martin Simmons has opportunity: True or False?
False (0.6627964381792564)
Martin Simmons has no opportunity: True or False?
False (0.816406362162552)
Stephen Kennelly is guilty: True or False?
True (0.621540893468236)
Stephen Kennelly is not guilty: True or False?
False (0.5058590748838109)
Stephen Kennelly has mean: True or False?
False (0.5039061393777357)
Stephen Kennelly has no mean: True or False?
False (0.8204694405411458)
Stephen Kennelly has motive: True or False?
True (0.6749080895533367)
Stephen Kennelly has no motive: True or False?
False (0.6343168649455533)
Stephen Kennelly has opportunity: True or False?
False (0.7446563307563252)
Stephen Kennelly has no opportunity: True or False?
False (0.9039744767757508)
Trevor Sutherland is guilty: True or False?
True (0.5360700410935405)
Trevor Sutherland is not guilty: True or False?
False (0.6132365353114321)
Trevor Sutherland has mean: True or False?
True (0.5312093941731293)
Trevor Sutherland has no mean: True or False?
False (0.7098243920264812)
Trevor Sutherland has motive: True or False?
True (0.642432441257838)
Trevor Sutherland has no motive: True or False?
False (0.6334102859975052)
Trevor Sutherland has opportunity: True or False?
False (0.6592954931819778)
Trevor Sutherland has no opportunity: True or False?
False (0.9196425651151865)
### Justin Scott
- mean: False (0.33025521110783185)
- motive: False (0.41300356935221594)
- opportunity: False (0.0)

### Martin Simmons
- mean: True (0.6141626144170799)
- motive: True (0.6934729182490079)
- opportunity: True (0.18359363783744798)

### Stephen Kennelly
- mean: False (0.5039061393777357)
- motive: False (0.0)
- opportunity: False (0.7446563307563252)

### Trevor Sutherland
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.6592954931819778)

The culprit is Martin Simmons.
In fact, it is Trevor Sutherland.
## 5minutemystery-the-rock-star-mystery
Gorg is guilty: True or False?
True (0.944176853162527)
Gorg is not guilty: True or False?
True (0.9170058945178141)
Gorg has mean: True or False?
True (0.9399133323582882)
Gorg has no mean: True or False?
True (0.9152046482091156)
Gorg has motive: True or False?
True (0.9752960797421999)
Gorg has no motive: True or False?
True (0.8714748565614324)
Gorg has opportunity: True or False?
True (0.9252299038987163)
Gorg has no opportunity: True or False?
True (0.8587185689177256)
Stu is guilty: True or False?
True (0.8587185689177256)
Stu is not guilty: True or False?
True (0.85729086409805)
Stu has mean: True or False?
True (0.7937461674149602)
Stu has no mean: True or False?
True (0.7049732238008671)
Stu has motive: True or False?
True (0.8341368378998062)
Stu has no motive: True or False?
True (0.7279754274224494)
Stu has opportunity: True or False?
True (0.5983121871760707)
Stu has no opportunity: True or False?
True (0.5515736950589613)
The Neighborhood Burgler is guilty: True or False?
True (0.942081869103903)
The Neighborhood Burgler is not guilty: True or False?
True (0.8587185689177256)
The Neighborhood Burgler has mean: True or False?
True (0.941654147692963)
The Neighborhood Burgler has no mean: True or False?
True (0.9012274173198201)
The Neighborhood Burgler has motive: True or False?
True (0.9442796704001448)
The Neighborhood Burgler has no motive: True or False?
True (0.7606506318580792)
The Neighborhood Burgler has opportunity: True or False?
True (0.9095862487848758)
The Neighborhood Burgler has no opportunity: True or False?
True (0.7599387683150569)
Tina is guilty: True or False?
True (0.8504685773080045)
Tina is not guilty: True or False?
True (0.8697145551802641)
Tina has mean: True or False?
True (0.8723474190177988)
Tina has no mean: True or False?
True (0.8370879250561812)
Tina has motive: True or False?
True (0.8610715240899957)
Tina has no motive: True or False?
True (0.8000678954040312)
Tina has opportunity: True or False?
True (0.7318258918270596)
Tina has no opportunity: True or False?
True (0.6169358476670045)
### Gorg
- mean: False (0.08479535179088438)
- motive: False (0.12852514343856758)
- opportunity: False (0.14128143108227442)

### Stu
- mean: False (0.29502677619913287)
- motive: False (0.27202457257755064)
- opportunity: False (0.44842630494103874)

### The Neighborhood Burgler
- mean: False (0.09877258268017985)
- motive: False (0.23934936814192076)
- opportunity: False (0.2400612316849431)

### Tina
- mean: True (0.8723474190177988)
- motive: True (0.8610715240899957)
- opportunity: True (0.7318258918270596)

The culprit is Tina.
In fact, it is Tina.
## 5minutemystery-ask-marthathe-arsonist
Keen Observer is guilty: True or False?
True (0.5784481782924303)
Keen Observer is not guilty: True or False?
False (0.5263427467960875)
Keen Observer has mean: True or False?
True (0.9193533657123177)
Keen Observer has no mean: True or False?
True (0.6141626144170799)
Keen Observer has motive: True or False?
True (0.6959583025067009)
Keen Observer has no motive: True or False?
False (0.5888891620166576)
Keen Observer has opportunity: True or False?
True (0.6901415551283886)
Keen Observer has no opportunity: True or False?
True (0.5832033700118571)
Minding My Own Business is guilty: True or False?
True (0.6297746298200823)
Minding My Own Business is not guilty: True or False?
True (0.5350984235603058)
Minding My Own Business has mean: True or False?
True (0.981944620412271)
Minding My Own Business has no mean: True or False?
True (0.8534247816107388)
Minding My Own Business has motive: True or False?
True (0.5765420266844429)
Minding My Own Business has no motive: True or False?
True (0.7279754274224494)
Minding My Own Business has opportunity: True or False?
True (0.7786493288700866)
Minding My Own Business has no opportunity: True or False?
True (0.5078118305218892)
Scared Stiff is guilty: True or False?
True (0.6197015092684077)
Scared Stiff is not guilty: True or False?
True (0.49999999904767284)
Scared Stiff has mean: True or False?
True (0.9076402191395381)
Scared Stiff has no mean: True or False?
False (0.5078118305218892)
Scared Stiff has motive: True or False?
True (0.621540893468236)
Scared Stiff has no motive: True or False?
False (0.5457699116223576)
Scared Stiff has opportunity: True or False?
True (0.7000752133823226)
Scared Stiff has no opportunity: True or False?
False (0.5448013654847448)
Watchful Waiter is guilty: True or False?
True (0.6104534962074417)
Watchful Waiter is not guilty: True or False?
True (0.5389832197022594)
Watchful Waiter has mean: True or False?
True (0.9314625284362855)
Watchful Waiter has no mean: True or False?
True (0.5312093941731293)
Watchful Waiter has motive: True or False?
True (0.6731917300802632)
Watchful Waiter has no motive: True or False?
True (0.6540113633452196)
Watchful Waiter has opportunity: True or False?
True (0.7341195403199204)
Watchful Waiter has no opportunity: True or False?
True (0.6104534962074417)
### Keen Observer
- mean: False (0.38583738558292013)
- motive: False (0.0)
- opportunity: False (0.41679662998814293)

### Minding My Own Business
- mean: False (0.14657521838926124)
- motive: False (0.27202457257755064)
- opportunity: False (0.49218816947811084)

### Scared Stiff
- mean: True (0.9076402191395381)
- motive: True (0.621540893468236)
- opportunity: True (0.7000752133823226)

### Watchful Waiter
- mean: False (0.4687906058268707)
- motive: False (0.3459886366547804)
- opportunity: False (0.3895465037925583)

The culprit is Scared Stiff.
In fact, it is Watchful Waiter.
## 5minutemystery-fatal-computer-crash
Alex Redoff is guilty: True or False?
True (0.9099070446252667)
Alex Redoff is not guilty: True or False?
Map:  66%|██████▌   | 133/203 [1:24:43<47:36, 40.81s/ examples]Map:  66%|██████▌   | 134/203 [1:25:25<47:08, 40.99s/ examples]True (0.8705973031072073)
Alex Redoff has mean: True or False?
True (0.7248703250005105)
Alex Redoff has no mean: True or False?
True (0.5292633777076584)
Alex Redoff has motive: True or False?
True (0.7483522884503825)
Alex Redoff has no motive: True or False?
True (0.7732163648437078)
Alex Redoff has opportunity: True or False?
True (0.7570766705324253)
Alex Redoff has no opportunity: True or False?
True (0.5860491337676195)
Cheryl Compton is guilty: True or False?
True (0.842345065078002)
Cheryl Compton is not guilty: True or False?
True (0.7683857617837733)
Cheryl Compton has mean: True or False?
True (0.8807970862580315)
Cheryl Compton has no mean: True or False?
True (0.6901415551283886)
Cheryl Compton has motive: True or False?
True (0.7074046739492601)
Cheryl Compton has no motive: True or False?
True (0.5936092727363199)
Cheryl Compton has opportunity: True or False?
True (0.720171518230031)
Cheryl Compton has no opportunity: True or False?
False (0.5660185351323219)
Claire Denninger is guilty: True or False?
True (0.8661325012437474)
Claire Denninger is not guilty: True or False?
True (0.8615382357584752)
Claire Denninger has mean: True or False?
True (0.9022656660556747)
Claire Denninger has no mean: True or False?
True (0.726425644352388)
Claire Denninger has motive: True or False?
True (0.8381505623254643)
Claire Denninger has no motive: True or False?
True (0.6706082735718226)
Claire Denninger has opportunity: True or False?
True (0.7669924589170153)
Claire Denninger has no opportunity: True or False?
False (0.5841525082971981)
Natalie Sampson is guilty: True or False?
True (0.776622945813876)
Natalie Sampson is not guilty: True or False?
True (0.6388352560545881)
Natalie Sampson has mean: True or False?
True (0.7468781997658912)
Natalie Sampson has no mean: True or False?
True (0.5907791930117218)
Natalie Sampson has motive: True or False?
True (0.6575384105121485)
Natalie Sampson has no motive: True or False?
True (0.5068355091660127)
Natalie Sampson has opportunity: True or False?
True (0.5765419579552815)
Natalie Sampson has no opportunity: True or False?
False (0.5945512478395265)
### Alex Redoff
- mean: False (0.4707366222923416)
- motive: False (0.22678363515629218)
- opportunity: False (0.41395086623238053)

### Cheryl Compton
- mean: True (0.8807970862580315)
- motive: True (0.7074046739492601)
- opportunity: True (0.720171518230031)

### Claire Denninger
- mean: False (0.273574355647612)
- motive: False (0.3293917264281774)
- opportunity: False (0.0)

### Natalie Sampson
- mean: False (0.40922080698827823)
- motive: False (0.4931644908339873)
- opportunity: False (0.0)

The culprit is Cheryl Compton.
In fact, it is Natalie Sampson.
## 5minutemystery-the-rob-club-murder-mystery
Al Gibson is guilty: True or False?
True (0.9029524325377104)
Al Gibson is not guilty: True or False?
True (0.9008791478232747)
Al Gibson has mean: True or False?
True (0.9429286143036572)
Al Gibson has no mean: True or False?
True (0.9066531077351827)
Al Gibson has motive: True or False?
True (0.9205042693180057)
Al Gibson has no motive: True or False?
True (0.8474634858439474)
Al Gibson has opportunity: True or False?
True (0.8582439976623328)
Al Gibson has no opportunity: True or False?
True (0.6662796746479285)
Johnny Woodward is guilty: True or False?
True (0.9076402191395381)
Johnny Woodward is not guilty: True or False?
True (0.8615382357584752)
Johnny Woodward has mean: True or False?
True (0.9518632280135741)
Johnny Woodward has no mean: True or False?
True (0.8891444205417208)
Johnny Woodward has motive: True or False?
True (0.9511422515416323)
Johnny Woodward has no motive: True or False?
True (0.8757870204368676)
Johnny Woodward has opportunity: True or False?
True (0.9401335713518422)
Johnny Woodward has no opportunity: True or False?
True (0.7806624796117883)
Ray Shields is guilty: True or False?
True (0.7931059536445917)
Ray Shields is not guilty: True or False?
True (0.7669925046333297)
Ray Shields has mean: True or False?
True (0.8175744430556572)
Ray Shields has no mean: True or False?
True (0.6680145838067516)
Ray Shields has motive: True or False?
True (0.8056321690561029)
Ray Shields has no motive: True or False?
True (0.6513548405484016)
Ray Shields has opportunity: True or False?
True (0.8006919661398397)
Ray Shields has no opportunity: True or False?
True (0.615087855649269)
Tim Acord is guilty: True or False?
True (0.7745833916423246)
Tim Acord is not guilty: True or False?
True (0.7549149897594328)
Tim Acord has mean: True or False?
True (0.9019206778000431)
Tim Acord has no mean: True or False?
True (0.8723473540228537)
Tim Acord has motive: True or False?
True (0.8193157928301305)
Tim Acord has no motive: True or False?
True (0.6486889055472267)
Tim Acord has opportunity: True or False?
True (0.7975568155246964)
Tim Acord has no opportunity: True or False?
True (0.5097643762740132)
Watson Treadway is guilty: True or False?
True (0.8596637206861489)
Watson Treadway is not guilty: True or False?
True (0.8221891570741111)
Watson Treadway has mean: True or False?
True (0.8799743689174987)
Watson Treadway has no mean: True or False?
True (0.7049732238008671)
Watson Treadway has motive: True or False?
True (0.8962513815714083)
Watson Treadway has no motive: True or False?
True (0.7732163648437078)
Watson Treadway has opportunity: True or False?
True (0.9155072008980665)
Watson Treadway has no opportunity: True or False?
True (0.776622945813876)
### Al Gibson
- mean: True (0.9429286143036572)
- motive: True (0.9205042693180057)
- opportunity: True (0.8582439976623328)

### Johnny Woodward
- mean: False (0.11085557945827917)
- motive: False (0.12421297956313238)
- opportunity: False (0.21933752038821175)

### Ray Shields
- mean: False (0.3319854161932484)
- motive: False (0.34864515945159835)
- opportunity: False (0.38491214435073096)

### Tim Acord
- mean: False (0.12765264597714632)
- motive: False (0.3513110944527733)
- opportunity: False (0.49023562372598684)

### Watson Treadway
- mean: False (0.29502677619913287)
- motive: False (0.22678363515629218)
- opportunity: False (0.22337705418612397)

The culprit is Al Gibson.
In fact, it is Johnny Woodward.
## 5minutemystery-ask-marthathe-litterer
Concerned Neighbor is guilty: True or False?
True (0.6486889055472267)
Concerned Neighbor is not guilty: True or False?
True (0.5263427467960875)
Concerned Neighbor has mean: True or False?
True (0.9238675252821831)
Concerned Neighbor has no mean: True or False?
True (0.7386690954574974)
Concerned Neighbor has motive: True or False?
True (0.8333246107254184)
Concerned Neighbor has no motive: True or False?
True (0.5936092727363199)
Concerned Neighbor has opportunity: True or False?
True (0.7697732451157533)
Concerned Neighbor has no opportunity: True or False?
False (0.5302364729224919)
Confused Commuter is guilty: True or False?
True (0.7711548682745724)
Confused Commuter is not guilty: True or False?
True (0.6020615685826383)
Confused Commuter has mean: True or False?
True (0.9435559526996434)
Confused Commuter has no mean: True or False?
True (0.6842640081724978)
Confused Commuter has motive: True or False?
True (0.8187367896794966)
Confused Commuter has no motive: True or False?
True (0.5794003525136094)
Confused Commuter has opportunity: True or False?
True (0.6379334932841956)
Confused Commuter has no opportunity: True or False?
False (0.5409238971378262)
Perplexed Dog Walker is guilty: True or False?
True (0.7431679939957333)
Perplexed Dog Walker is not guilty: True or False?
True (0.5350983597716067)
Perplexed Dog Walker has mean: True or False?
True (0.9603611244019274)
Perplexed Dog Walker has no mean: True or False?
True (0.8316905440184192)
Perplexed Dog Walker has motive: True or False?
True (0.8778961263000082)
Perplexed Dog Walker has no motive: True or False?
False (0.5418937216067536)
Perplexed Dog Walker has opportunity: True or False?
True (0.7704647687904915)
Perplexed Dog Walker has no opportunity: True or False?
False (0.6504672743423094)
Smug in Suburbia is guilty: True or False?
True (0.6817267588564826)
Smug in Suburbia is not guilty: True or False?
False (0.5214711998972037)
Map:  67%|██████▋   | 135/203 [1:26:01<44:47, 39.53s/ examples]Map:  67%|██████▋   | 136/203 [1:26:40<44:04, 39.47s/ examples]Map:  67%|██████▋   | 137/203 [1:27:16<42:26, 38.58s/ examples]Smug in Suburbia has mean: True or False?
True (0.8745065279415651)
Smug in Suburbia has no mean: True or False?
True (0.6370307821695329)
Smug in Suburbia has motive: True or False?
True (0.8418256009501243)
Smug in Suburbia has no motive: True or False?
False (0.6132365353114321)
Smug in Suburbia has opportunity: True or False?
True (0.5214711377329961)
Smug in Suburbia has no opportunity: True or False?
False (0.6918097672776748)
### Concerned Neighbor
- mean: False (0.26133090454250263)
- motive: False (0.4063907272636801)
- opportunity: False (0.0)

### Confused Commuter
- mean: False (0.3157359918275022)
- motive: False (0.42059964748639056)
- opportunity: False (0.0)

### Perplexed Dog Walker
- mean: True (0.9603611244019274)
- motive: True (0.8778961263000082)
- opportunity: True (0.7704647687904915)

### Smug in Suburbia
- mean: False (0.3629692178304671)
- motive: False (0.0)
- opportunity: False (0.0)

The culprit is Perplexed Dog Walker.
In fact, it is Smug in Suburbia.
## 5minutemystery-drama-queen
Alfred Cooper is guilty: True or False?
True (0.6252092625510083)
Alfred Cooper is not guilty: True or False?
True (0.5954925880745511)
Alfred Cooper has mean: True or False?
True (0.7431679939957333)
Alfred Cooper has no mean: True or False?
False (0.6433292707767855)
Alfred Cooper has motive: True or False?
True (0.6918097672776748)
Alfred Cooper has no motive: True or False?
False (0.6566582893190611)
Alfred Cooper has opportunity: True or False?
True (0.525368812147771)
Alfred Cooper has no opportunity: True or False?
False (0.7348812840309261)
Isabelle Rogers is guilty: True or False?
True (0.6315943123389512)
Isabelle Rogers is not guilty: True or False?
False (0.6113819501087365)
Isabelle Rogers has mean: True or False?
True (0.6270381219830087)
Isabelle Rogers has no mean: True or False?
False (0.7641883982873323)
Isabelle Rogers has motive: True or False?
True (0.6076632024562351)
Isabelle Rogers has no motive: True or False?
False (0.6817267588564826)
Isabelle Rogers has opportunity: True or False?
False (0.7162185953247016)
Isabelle Rogers has no opportunity: True or False?
False (0.8233283740192667)
James Fennimore is guilty: True or False?
True (0.5698526542706361)
James Fennimore is not guilty: True or False?
False (0.5068355091660127)
James Fennimore has mean: True or False?
True (0.7739006258141444)
James Fennimore has no mean: True or False?
False (0.5973730125048408)
James Fennimore has motive: True or False?
True (0.7839884808423031)
James Fennimore has no motive: True or False?
False (0.7017130830397807)
James Fennimore has opportunity: True or False?
False (0.6893056096647525)
James Fennimore has no opportunity: True or False?
False (0.7931059536445917)
Madge Anderson is guilty: True or False?
True (0.5136684743338078)
Madge Anderson is not guilty: True or False?
False (0.5117165908639297)
Madge Anderson has mean: True or False?
True (0.6388353131709135)
Madge Anderson has no mean: True or False?
False (0.6048658333578858)
Madge Anderson has motive: True or False?
True (0.5973730125048408)
Madge Anderson has no motive: True or False?
False (0.6859494535376744)
Madge Anderson has opportunity: True or False?
False (0.7170118721569225)
Madge Anderson has no opportunity: True or False?
False (0.8606036289596553)
### Alfred Cooper
- mean: True (0.7431679939957333)
- motive: True (0.6918097672776748)
- opportunity: True (0.525368812147771)

### Isabelle Rogers
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.7162185953247016)

### James Fennimore
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.6893056096647525)

### Madge Anderson
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.7170118721569225)

The culprit is Alfred Cooper.
In fact, it is James Fennimore.
## 5minutemystery-the-gourmet-mystery
Antoine is guilty: True or False?
True (0.8877896081343184)
Antoine is not guilty: True or False?
True (0.8236122680985841)
Antoine has mean: True or False?
True (0.814643384779728)
Antoine has no mean: True or False?
True (0.5457699116223576)
Antoine has motive: True or False?
True (0.8519527857346616)
Antoine has no motive: True or False?
True (0.7356416476869558)
Antoine has opportunity: True or False?
True (0.6976089520497016)
Antoine has no opportunity: True or False?
True (0.6132365353114321)
Georges Monceau is guilty: True or False?
True (0.9391922928557355)
Georges Monceau is not guilty: True or False?
False (0.9213746891252907)
Georges Monceau has mean: True or False?
True (0.84619676525883)
Georges Monceau has no mean: True or False?
True (0.5486734987923966)
Georges Monceau has motive: True or False?
True (0.8807970337584357)
Georges Monceau has no motive: True or False?
True (0.7461389980806673)
Georges Monceau has opportunity: True or False?
True (0.795181328342443)
Georges Monceau has no opportunity: True or False?
True (0.6437773011339297)
Sally Horvats is guilty: True or False?
True (0.9201462264331123)
Sally Horvats is not guilty: True or False?
False (1.2036770197503404)
Sally Horvats has mean: True or False?
True (0.8104789202520752)
Sally Horvats has no mean: True or False?
False (0.503906199448032)
Sally Horvats has motive: True or False?
True (0.9280183890155084)
Sally Horvats has no motive: True or False?
True (0.8221890958162477)
Sally Horvats has opportunity: True or False?
True (0.7735586847891339)
Sally Horvats has no opportunity: True or False?
True (0.7142295770821385)
Sam Wheeler is guilty: True or False?
False (0.6390576676453745)
Sam Wheeler is not guilty: True or False?
False (1.3018174695125186)
Sam Wheeler has mean: True or False?
True (0.7412996266976789)
Sam Wheeler has no mean: True or False?
False (0.6034645359500814)
Sam Wheeler has motive: True or False?
True (0.7325918054337844)
Sam Wheeler has no motive: True or False?
True (0.7037530630234264)
Sam Wheeler has opportunity: True or False?
True (0.615087855649269)
Sam Wheeler has no opportunity: True or False?
False (0.5112285687489156)
### Antoine
- mean: False (0.45423008837764245)
- motive: False (0.26435835231304416)
- opportunity: False (0.3867634646885679)

### Georges Monceau
- mean: False (0.4513265012076034)
- motive: False (0.2538610019193327)
- opportunity: False (0.3562226988660703)

### Sally Horvats
- mean: False (0.0)
- motive: False (0.17781090418375234)
- opportunity: False (0.2857704229178615)

### Sam Wheeler
- mean: True (0.7412996266976789)
- motive: True (0.7325918054337844)
- opportunity: True (0.615087855649269)

The culprit is Sam Wheeler.
In fact, it is Sally Horvats.
## 5minutemystery-the-potter-book-mystery
Alfred is guilty: True or False?
True (0.9229003224709645)
Alfred is not guilty: True or False?
True (0.9586153014523353)
Alfred has mean: True or False?
True (0.5107405249783342)
Alfred has no mean: True or False?
True (0.5321820387813727)
Alfred has motive: True or False?
True (0.8507168263103924)
Alfred has no motive: True or False?
True (0.7371581232960549)
Alfred has opportunity: True or False?
True (0.7520125537161032)
Alfred has no opportunity: True or False?
False (0.6370308391245257)
Ann is guilty: True or False?
True (0.8521990171094214)
Ann is not guilty: True or False?
True (0.9489172681310486)
Ann has mean: True or False?
True (0.7217432334405754)
Ann has no mean: True or False?
True (0.7118316903606244)
Ann has motive: True or False?
True (0.884439109617765)
Ann has no motive: True or False?
True (0.7697732451157533)
Ann has opportunity: True or False?
True (0.7694269364202454)
Ann has no opportunity: True or False?
False (0.6575384105121485)
Rusty is guilty: True or False?
True (0.9165588616316169)
Rusty is not guilty: True or False?
True (0.9529258022651363)
Rusty has mean: True or False?
True (0.8428631416381634)
Rusty has no mean: True or False?
True (0.8037905715242155)
Rusty has motive: True or False?
True (0.9430860272459268)
Rusty has no motive: True or False?
True (0.823044124016779)
Rusty has opportunity: True or False?
True (0.878314250659373)
Rusty has no opportunity: True or False?
False (0.5717666110200305)
Uncle Ezra is guilty: True or False?
True (0.9545627850600183)
Uncle Ezra is not guilty: True or False?
Map:  68%|██████▊   | 138/203 [1:28:05<45:00, 41.55s/ examples]Map:  68%|██████▊   | 139/203 [1:28:43<43:11, 40.49s/ examples]Map:  69%|██████▉   | 140/203 [1:29:21<41:49, 39.83s/ examples]True (0.9523087127556139)
Uncle Ezra has mean: True or False?
True (0.8582439976623328)
Uncle Ezra has no mean: True or False?
True (0.84260427698882)
Uncle Ezra has motive: True or False?
True (0.9171543708147702)
Uncle Ezra has no motive: True or False?
True (0.743912876509037)
Uncle Ezra has opportunity: True or False?
True (0.9099069836112468)
Uncle Ezra has no opportunity: True or False?
True (0.6242935037467142)
### Alfred
- mean: False (0.4678179612186273)
- motive: False (0.2628418767039451)
- opportunity: False (0.0)

### Ann
- mean: True (0.7217432334405754)
- motive: True (0.884439109617765)
- opportunity: True (0.7694269364202454)

### Rusty
- mean: False (0.1962094284757845)
- motive: False (0.17695587598322104)
- opportunity: False (0.0)

### Uncle Ezra
- mean: False (0.15739572301118)
- motive: False (0.25608712349096296)
- opportunity: False (0.3757064962532858)

The culprit is Ann.
In fact, it is Uncle Ezra.
## 5minutemystery-death-in-the-office
Cynthia Peck is guilty: True or False?
True (0.6926419789019715)
Cynthia Peck is not guilty: True or False?
True (0.7853085971692302)
Cynthia Peck has mean: True or False?
True (0.8514594452543962)
Cynthia Peck has no mean: True or False?
True (0.5544704821687028)
Cynthia Peck has motive: True or False?
True (0.7648916137833577)
Cynthia Peck has no motive: True or False?
True (0.6252092625510083)
Cynthia Peck has opportunity: True or False?
True (0.6749081498948247)
Cynthia Peck has no opportunity: True or False?
False (0.6469064338453809)
Josh Kesler is guilty: True or False?
True (0.784649255215384)
Josh Kesler is not guilty: True or False?
True (0.8128673413132903)
Josh Kesler has mean: True or False?
True (0.7799928701983835)
Josh Kesler has no mean: True or False?
True (0.589834510337428)
Josh Kesler has motive: True or False?
True (0.7752646804088963)
Josh Kesler has no motive: True or False?
True (0.6645403391983984)
Josh Kesler has opportunity: True or False?
True (0.6791787167336184)
Josh Kesler has no opportunity: True or False?
False (0.5126925663186335)
Megan Brewer is guilty: True or False?
True (0.595492552580428)
Megan Brewer is not guilty: True or False?
True (0.6834194581047349)
Megan Brewer has mean: True or False?
True (0.64779823427608)
Megan Brewer has no mean: True or False?
False (0.6261242000979097)
Megan Brewer has motive: True or False?
True (0.5399537164111071)
Megan Brewer has no motive: True or False?
True (0.5312093625105829)
Megan Brewer has opportunity: True or False?
True (0.5087881523495457)
Megan Brewer has no opportunity: True or False?
False (0.6918097672776748)
Steve Ledbetter is guilty: True or False?
True (0.7839884107482739)
Steve Ledbetter is not guilty: True or False?
True (0.8006920257960423)
Steve Ledbetter has mean: True or False?
True (0.9082930704920021)
Steve Ledbetter has no mean: True or False?
True (0.5058591351869154)
Steve Ledbetter has motive: True or False?
True (0.6424325178417575)
Steve Ledbetter has no motive: True or False?
True (0.685107355950278)
Steve Ledbetter has opportunity: True or False?
True (0.591723272524637)
Steve Ledbetter has no opportunity: True or False?
False (0.555435161888281)
### Cynthia Peck
- mean: False (0.44552951783129724)
- motive: False (0.3747907374489917)
- opportunity: False (0.0)

### Josh Kesler
- mean: False (0.41016548966257205)
- motive: False (0.3354596608016016)
- opportunity: False (0.0)

### Megan Brewer
- mean: True (0.64779823427608)
- motive: True (0.5399537164111071)
- opportunity: True (0.5087881523495457)

### Steve Ledbetter
- mean: False (0.4941408648130846)
- motive: False (0.31489264404972195)
- opportunity: False (0.0)

The culprit is Megan Brewer.
In fact, it is Megan Brewer.
## 5minutemystery-chief-inspector-japp-solves-a-case
Alan Harrison is guilty: True or False?
True (0.8438951328214825)
Alan Harrison is not guilty: True or False?
True (0.8407826471261478)
Alan Harrison has mean: True or False?
True (0.6067314814064781)
Alan Harrison has no mean: True or False?
True (0.6662796150778861)
Alan Harrison has motive: True or False?
True (0.7704647687904915)
Alan Harrison has no motive: True or False?
True (0.6774739680526108)
Alan Harrison has opportunity: True or False?
True (0.6934729802503211)
Alan Harrison has no opportunity: True or False?
False (0.5341265295318852)
Evelyn Johnston is guilty: True or False?
True (0.7786493288700866)
Evelyn Johnston is not guilty: True or False?
True (0.7490872087035162)
Evelyn Johnston has mean: True or False?
True (0.5679366075542497)
Evelyn Johnston has no mean: True or False?
True (0.5660185351323219)
Evelyn Johnston has motive: True or False?
True (0.5936092727363199)
Evelyn Johnston has no motive: True or False?
True (0.5602526707659626)
Evelyn Johnston has opportunity: True or False?
True (0.6178585826183487)
Evelyn Johnston has no opportunity: True or False?
False (0.5954925880745511)
George Smythe is guilty: True or False?
True (0.8852352523606669)
George Smythe is not guilty: True or False?
True (0.8705972382426559)
George Smythe has mean: True or False?
True (0.6242935781683038)
George Smythe has no mean: True or False?
True (0.6926419789019715)
George Smythe has motive: True or False?
True (0.7302898278778687)
George Smythe has no motive: True or False?
True (0.6951311179371613)
George Smythe has opportunity: True or False?
True (0.6783269591477166)
George Smythe has no opportunity: True or False?
True (0.5156199352405011)
Herbert Grosvenor is guilty: True or False?
True (0.9173026661190045)
Herbert Grosvenor is not guilty: True or False?
True (0.8883720049821552)
Herbert Grosvenor has mean: True or False?
True (0.5477060024984176)
Herbert Grosvenor has no mean: True or False?
True (0.6306849143569856)
Herbert Grosvenor has motive: True or False?
True (0.8098781635062345)
Herbert Grosvenor has no motive: True or False?
True (0.8074606715677252)
Herbert Grosvenor has opportunity: True or False?
True (0.7563574896543893)
Herbert Grosvenor has no opportunity: True or False?
True (0.6270381219830087)
### Alan Harrison
- mean: False (0.33372038492211387)
- motive: False (0.32252603194738916)
- opportunity: False (0.0)

### Evelyn Johnston
- mean: True (0.5679366075542497)
- motive: True (0.5936092727363199)
- opportunity: True (0.6178585826183487)

### George Smythe
- mean: False (0.30735802109802846)
- motive: False (0.3048688820628387)
- opportunity: False (0.4843800647594989)

### Herbert Grosvenor
- mean: False (0.3693150856430144)
- motive: False (0.19253932843227484)
- opportunity: False (0.3729618780169913)

The culprit is Evelyn Johnston.
In fact, it is Alan Harrison.
## 5minutemystery-who-stole-the-cavemans-dinner
Dinosaur is guilty: True or False?
True (0.8169911556077801)
Dinosaur is not guilty: True or False?
True (0.7397985526059343)
Dinosaur has mean: True or False?
True (0.6370307821695329)
Dinosaur has no mean: True or False?
True (0.5660185351323219)
Dinosaur has motive: True or False?
True (0.89010334411601)
Dinosaur has no motive: True or False?
True (0.7375364390581655)
Dinosaur has opportunity: True or False?
True (0.6627964381792564)
Dinosaur has no opportunity: True or False?
True (0.5389832197022594)
Droo is guilty: True or False?
True (0.9247556906264367)
Droo is not guilty: True or False?
True (0.8841393606706147)
Droo has mean: True or False?
True (0.7994422859301654)
Droo has no mean: True or False?
True (0.7409249450892966)
Droo has motive: True or False?
True (0.9687528016079104)
Droo has no motive: True or False?
True (0.6787529571884303)
Droo has opportunity: True or False?
True (0.9223425402045055)
Droo has no opportunity: True or False?
True (0.6808786440630326)
Father is guilty: True or False?
False (0.8231134325685282)
Father is not guilty: True or False?
False (1.332912172340777)
Father has mean: True or False?
False (0.3059238951257538)
Father has no mean: True or False?
False (0.9530712609029113)
Father has motive: True or False?
False (0.5304191471149083)
Father has no motive: True or False?
False (1.029726966621629)
Father has opportunity: True or False?
False (0.3641133616723893)
Father has no opportunity: True or False?
False (1.0001669292882562)
Monkeys is guilty: True or False?
Map:  69%|██████▉   | 141/203 [1:30:09<43:41, 42.29s/ examples]Map:  70%|██████▉   | 142/203 [1:30:37<38:32, 37.91s/ examples]Map:  70%|███████   | 143/203 [1:31:38<44:55, 44.93s/ examples]True (0.6187804294217345)
Monkeys is not guilty: True or False?
False (0.5234203246639862)
Monkeys has mean: True or False?
False (0.5282900845448565)
Monkeys has no mean: True or False?
False (0.5832033352502285)
Monkeys has motive: True or False?
True (0.6160122877297346)
Monkeys has no motive: True or False?
True (0.5341265295318852)
Monkeys has opportunity: True or False?
False (0.5428633110863297)
Monkeys has no opportunity: True or False?
False (0.6971967177605096)
### Dinosaur
- mean: False (0.4339814648676781)
- motive: False (0.26246356094183454)
- opportunity: False (0.4610167802977406)

### Droo
- mean: False (0.2590750549107034)
- motive: False (0.3212470428115697)
- opportunity: False (0.31912135593696744)

### Father
- mean: False (0.3059238951257538)
- motive: False (0.5304191471149083)
- opportunity: False (0.3641133616723893)

### Monkeys
- mean: True (0.4167966647497715)
- motive: True (0.6160122877297346)
- opportunity: True (0.3028032822394904)

The culprit is Monkeys.
In fact, it is Dinosaur.
## 5minutemystery-the-stolen-car-mystery
David Kelly is guilty: True or False?
True (0.6783269591477166)
David Kelly is not guilty: True or False?
True (0.7209580648179327)
David Kelly has mean: True or False?
True (0.867485409735739)
David Kelly has no mean: True or False?
True (0.6334102104891195)
David Kelly has motive: True or False?
True (0.7138307731576955)
David Kelly has no motive: True or False?
True (0.7826625131049049)
David Kelly has opportunity: True or False?
True (0.7348812840309261)
David Kelly has no opportunity: True or False?
True (0.5631377056275331)
Donna Allen is guilty: True or False?
True (0.6113819501087365)
Donna Allen is not guilty: True or False?
True (0.6627964974378784)
Donna Allen has mean: True or False?
True (0.8438951328214825)
Donna Allen has no mean: True or False?
True (0.6288633913849659)
Donna Allen has motive: True or False?
True (0.5907791930117218)
Donna Allen has no motive: True or False?
True (0.6513548405484016)
Donna Allen has opportunity: True or False?
True (0.5727227727404994)
Donna Allen has no opportunity: True or False?
False (0.5068355091660127)
Larry Roberts is guilty: True or False?
True (0.5973730125048408)
Larry Roberts is not guilty: True or False?
True (0.6610481693322063)
Larry Roberts has mean: True or False?
True (0.7468781997658912)
Larry Roberts has no mean: True or False?
True (0.5602526707659626)
Larry Roberts has motive: True or False?
True (0.5907792634380938)
Larry Roberts has no motive: True or False?
True (0.6783269591477166)
Larry Roberts has opportunity: True or False?
True (0.5117165908639297)
Larry Roberts has no opportunity: True or False?
False (0.621540893468236)
Nancy Lee is guilty: True or False?
True (0.5746335251160043)
Nancy Lee is not guilty: True or False?
True (0.6714705702070799)
Nancy Lee has mean: True or False?
True (0.745398395394548)
Nancy Lee has no mean: True or False?
True (0.6104534234357184)
Nancy Lee has motive: True or False?
True (0.8122724274380432)
Nancy Lee has no motive: True or False?
True (0.7975568155246964)
Nancy Lee has opportunity: True or False?
True (0.6540113633452196)
Nancy Lee has no opportunity: True or False?
True (0.550607385906944)
### David Kelly
- mean: False (0.3665897895108805)
- motive: False (0.21733748689509513)
- opportunity: False (0.43686229437246693)

### Donna Allen
- mean: False (0.37113660861503406)
- motive: False (0.34864515945159835)
- opportunity: False (0.0)

### Larry Roberts
- mean: True (0.7468781997658912)
- motive: True (0.5907792634380938)
- opportunity: True (0.5117165908639297)

### Nancy Lee
- mean: False (0.3895465765642816)
- motive: False (0.20244318447530363)
- opportunity: False (0.449392614093056)

The culprit is Larry Roberts.
In fact, it is Donna Allen.
## 5minutemystery-the-straw-hat-theater-mysteriesfinal-curtain
Arthur Glendon is guilty: True or False?
True (0.946497859305556)
Arthur Glendon is not guilty: True or False?
True (0.9343951361750445)
Arthur Glendon has mean: True or False?
True (0.6636689235052821)
Arthur Glendon has no mean: True or False?
True (0.5486734987923966)
Arthur Glendon has motive: True or False?
True (0.9343951361750445)
Arthur Glendon has no motive: True or False?
True (0.9020933537090856)
Arthur Glendon has opportunity: True or False?
True (0.9155072008980665)
Arthur Glendon has no opportunity: True or False?
True (0.7061904069041735)
Josh Whitehead is guilty: True or False?
True (0.9084556087677383)
Josh Whitehead is not guilty: True or False?
True (0.8966140749572745)
Josh Whitehead has mean: True or False?
True (0.8433798528114077)
Josh Whitehead has no mean: True or False?
True (0.7885831565209055)
Josh Whitehead has motive: True or False?
True (0.9156581770494915)
Josh Whitehead has no motive: True or False?
True (0.8840392847025188)
Josh Whitehead has opportunity: True or False?
True (0.9309620852900756)
Josh Whitehead has no opportunity: True or False?
True (0.7739005566220397)
Linda Eberlie is guilty: True or False?
True (0.8818185984511544)
Linda Eberlie is not guilty: True or False?
True (0.8563323578093363)
Linda Eberlie has mean: True or False?
True (0.8187367896794966)
Linda Eberlie has no mean: True or False?
True (0.8213308436294358)
Linda Eberlie has motive: True or False?
True (0.9219218506394821)
Linda Eberlie has no motive: True or False?
True (0.8883720049821552)
Linda Eberlie has opportunity: True or False?
True (0.9390248079664695)
Linda Eberlie has no opportunity: True or False?
True (0.8037905715242155)
Sam Watson is guilty: True or False?
True (0.8985886567144342)
Sam Watson is not guilty: True or False?
True (0.8469578019965)
Sam Watson has mean: True or False?
True (0.8175744430556572)
Sam Watson has no mean: True or False?
True (0.597373048111048)
Sam Watson has motive: True or False?
True (0.8803863464576128)
Sam Watson has no motive: True or False?
True (0.7697732451157533)
Sam Watson has opportunity: True or False?
True (0.9144436110210817)
Sam Watson has no opportunity: True or False?
True (0.5486734987923966)
Stella Marlowe is guilty: True or False?
True (0.8158201638039532)
Stella Marlowe is not guilty: True or False?
True (0.8392075331266983)
Stella Marlowe has mean: True or False?
True (0.5583269696343842)
Stella Marlowe has no mean: True or False?
True (0.5087881523495457)
Stella Marlowe has motive: True or False?
True (0.7683857617837733)
Stella Marlowe has no motive: True or False?
True (0.6406358487498992)
Stella Marlowe has opportunity: True or False?
True (0.8074606715677252)
Stella Marlowe has no opportunity: True or False?
True (0.5185462156586879)
### Arthur Glendon
- mean: False (0.4513265012076034)
- motive: False (0.09790664629091439)
- opportunity: False (0.29380959309582655)

### Josh Whitehead
- mean: False (0.2114168434790945)
- motive: False (0.1159607152974812)
- opportunity: False (0.22609944337796029)

### Linda Eberlie
- mean: True (0.8187367896794966)
- motive: True (0.9219218506394821)
- opportunity: True (0.9390248079664695)

### Sam Watson
- mean: False (0.40262695188895203)
- motive: False (0.2302267548842467)
- opportunity: False (0.4513265012076034)

### Stella Marlowe
- mean: False (0.49121184765045434)
- motive: False (0.3593641512501008)
- opportunity: False (0.48145378434131214)

The culprit is Linda Eberlie.
In fact, it is Linda Eberlie.
## 5minutemystery-itheft
Lea Thompson is guilty: True or False?
True (0.5486734987923966)
Lea Thompson is not guilty: True or False?
True (0.6636689235052821)
Lea Thompson has mean: True or False?
True (0.5428633110863297)
Lea Thompson has no mean: True or False?
False (0.6451199006197486)
Lea Thompson has motive: True or False?
True (0.5992506595844092)
Lea Thompson has no motive: True or False?
True (0.5813030649269245)
Lea Thompson has opportunity: True or False?
False (0.784649255215384)
Lea Thompson has no opportunity: True or False?
False (0.8031737798924701)
Rachel Vermeer is guilty: True or False?
True (0.5774953314585229)
Rachel Vermeer is not guilty: True or False?
True (0.5794003525136094)
Rachel Vermeer has mean: True or False?
True (0.6531268925247615)
Rachel Vermeer has no mean: True or False?
True (0.5755879969637064)
Map:  71%|███████   | 144/203 [1:32:08<39:42, 40.38s/ examples]Map:  71%|███████▏  | 145/203 [1:32:39<36:24, 37.67s/ examples]Map:  72%|███████▏  | 146/203 [1:33:15<35:20, 37.20s/ examples]Rachel Vermeer has motive: True or False?
True (0.7956580548514487)
Rachel Vermeer has no motive: True or False?
True (0.6334102859975052)
Rachel Vermeer has opportunity: True or False?
False (0.550607385906944)
Rachel Vermeer has no opportunity: True or False?
False (0.7154240000492645)
Shawn Ramos is guilty: True or False?
True (0.6876299924560524)
Shawn Ramos is not guilty: True or False?
True (0.6918097672776748)
Shawn Ramos has mean: True or False?
True (0.5841525082971981)
Shawn Ramos has no mean: True or False?
False (0.673191669892235)
Shawn Ramos has motive: True or False?
True (0.6934729802503211)
Shawn Ramos has no motive: True or False?
True (0.5888891269161294)
Shawn Ramos has opportunity: True or False?
False (0.6723316913929156)
Shawn Ramos has no opportunity: True or False?
False (0.7302898714065358)
Shay Dulaney is guilty: True or False?
True (0.6645403391983984)
Shay Dulaney is not guilty: True or False?
True (0.6851073967858599)
Shay Dulaney has mean: True or False?
True (0.6197014353942354)
Shay Dulaney has no mean: True or False?
False (0.6619228707202935)
Shay Dulaney has motive: True or False?
True (0.745398395394548)
Shay Dulaney has no motive: True or False?
True (0.5224457875179084)
Shay Dulaney has opportunity: True or False?
False (0.6601723415572317)
Shay Dulaney has no opportunity: True or False?
False (0.7333563569098757)
### Lea Thompson
- mean: False (0.0)
- motive: False (0.4186969350730755)
- opportunity: False (0.784649255215384)

### Rachel Vermeer
- mean: False (0.42441200303629356)
- motive: False (0.36658971400249485)
- opportunity: False (0.550607385906944)

### Shawn Ramos
- mean: True (0.5841525082971981)
- motive: True (0.6934729802503211)
- opportunity: True (0.2697101285934642)

### Shay Dulaney
- mean: False (0.0)
- motive: False (0.4775542124820916)
- opportunity: False (0.6601723415572317)

The culprit is Shawn Ramos.
In fact, it is Rachel Vermeer.
## 5minutemystery-the-punch-with-a-punch
Carole is guilty: True or False?
True (0.7017130830397807)
Carole is not guilty: True or False?
True (0.8092759225969047)
Carole has mean: True or False?
True (0.8464508054137014)
Carole has no mean: True or False?
True (0.7356416476869558)
Carole has motive: True or False?
True (0.9372107968415931)
Carole has no motive: True or False?
True (0.8080671968507699)
Carole has opportunity: True or False?
True (0.7613611200983542)
Carole has no opportunity: True or False?
True (0.5650587803792624)
Dan is guilty: True or False?
True (0.6943026818003076)
Dan is not guilty: True or False?
True (0.7549149897594328)
Dan has mean: True or False?
True (0.7074046739492601)
Dan has no mean: True or False?
False (0.6197014353942354)
Dan has motive: True or False?
True (0.9465966835599983)
Dan has no motive: True or False?
True (0.6513548987840652)
Dan has opportunity: True or False?
True (0.7599387683150569)
Dan has no opportunity: True or False?
False (0.6057990946577705)
Diane is guilty: True or False?
True (0.7541915688671895)
Diane is not guilty: True or False?
True (0.8519528492100928)
Diane has mean: True or False?
True (0.8484706263347676)
Diane has no mean: True or False?
True (0.6592954931819778)
Diane has motive: True or False?
True (0.9658995287662642)
Diane has no motive: True or False?
True (0.8402590129647053)
Diane has opportunity: True or False?
True (0.8131642285412432)
Diane has no opportunity: True or False?
False (0.6592954931819778)
Principal Whittenmeyer is guilty: True or False?
True (0.5370413742099674)
Principal Whittenmeyer is not guilty: True or False?
True (0.5650587803792624)
Principal Whittenmeyer has mean: True or False?
True (0.702530072932436)
Principal Whittenmeyer has no mean: True or False?
False (0.6876299924560524)
Principal Whittenmeyer has motive: True or False?
True (0.8745065930973813)
Principal Whittenmeyer has no motive: True or False?
False (0.589834510337428)
Principal Whittenmeyer has opportunity: True or False?
False (0.5746334908651781)
Principal Whittenmeyer has no opportunity: True or False?
False (0.7279754274224494)
### Carole
- mean: False (0.26435835231304416)
- motive: False (0.1919328031492301)
- opportunity: False (0.4349412196207376)

### Dan
- mean: False (0.0)
- motive: False (0.34864510121593484)
- opportunity: False (0.0)

### Diane
- mean: False (0.3407045068180222)
- motive: False (0.1597409870352947)
- opportunity: False (0.0)

### Principal Whittenmeyer
- mean: True (0.702530072932436)
- motive: True (0.8745065930973813)
- opportunity: True (0.27202457257755064)

The culprit is Principal Whittenmeyer.
In fact, it is Carole.
## 5minutemystery-the-straw-hat-theater-mysteriesbox-office-nightmare
Basil Carmody is guilty: True or False?
True (0.7905303264811482)
Basil Carmody is not guilty: True or False?
True (0.7074046739492601)
Basil Carmody has mean: True or False?
True (0.9207896596153058)
Basil Carmody has no mean: True or False?
True (0.5698526542706361)
Basil Carmody has motive: True or False?
True (0.8092759828926619)
Basil Carmody has no motive: True or False?
False (0.5312093941731293)
Basil Carmody has opportunity: True or False?
True (0.6531268925247615)
Basil Carmody has no opportunity: True or False?
False (0.6976088896786037)
John Franklin is guilty: True or False?
True (0.8652240590801695)
John Franklin is not guilty: True or False?
True (0.8037905715242155)
John Franklin has mean: True or False?
True (0.8086723099497763)
John Franklin has no mean: True or False?
True (0.5282900845448565)
John Franklin has motive: True or False?
True (0.8386797935187188)
John Franklin has no motive: True or False?
True (0.555435161888281)
John Franklin has opportunity: True or False?
True (0.6976088896786037)
John Franklin has no opportunity: True or False?
False (0.5370413742099674)
Lawrence Blake is guilty: True or False?
True (0.8464508054137014)
Lawrence Blake is not guilty: True or False?
True (0.7872777601997338)
Lawrence Blake has mean: True or False?
True (0.7122321792841629)
Lawrence Blake has no mean: True or False?
False (0.6288633913849659)
Lawrence Blake has motive: True or False?
True (0.646013666311734)
Lawrence Blake has no motive: True or False?
False (0.5515736950589613)
Lawrence Blake has opportunity: True or False?
False (0.5009765603034438)
Lawrence Blake has no opportunity: True or False?
False (0.7461389980806673)
Martha Gilmont is guilty: True or False?
True (0.6206215556999736)
Martha Gilmont is not guilty: True or False?
False (0.5224457875179084)
Martha Gilmont has mean: True or False?
True (0.5477060024984176)
Martha Gilmont has no mean: True or False?
False (0.8092759828926619)
Martha Gilmont has motive: True or False?
True (0.5350984235603058)
Martha Gilmont has no motive: True or False?
False (0.7683857617837733)
Martha Gilmont has opportunity: True or False?
False (0.7779753136455794)
Martha Gilmont has no opportunity: True or False?
False (0.8740772044235984)
### Basil Carmody
- mean: False (0.43014734572936386)
- motive: False (0.0)
- opportunity: False (0.0)

### John Franklin
- mean: False (0.4717099154551435)
- motive: False (0.444564838111719)
- opportunity: False (0.0)

### Lawrence Blake
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.5009765603034438)

### Martha Gilmont
- mean: True (0.5477060024984176)
- motive: True (0.5350984235603058)
- opportunity: True (0.12592279557640162)

The culprit is Martha Gilmont.
In fact, it is John Franklin.
## 5minutemystery-the-waffle-man-mystery
Larry is guilty: True or False?
True (0.816406362162552)
Larry is not guilty: True or False?
True (0.7749242151945704)
Larry has mean: True or False?
True (0.8529354311342636)
Larry has no mean: True or False?
True (0.6233768569026616)
Larry has motive: True or False?
True (0.8856314413364714)
Larry has no motive: True or False?
True (0.5331543669186894)
Larry has opportunity: True or False?
True (0.7341195403199204)
Larry has no opportunity: True or False?
False (0.6909763109505791)
The Old Man is guilty: True or False?
True (0.7962924261546153)
The Old Man is not guilty: True or False?
True (0.7833262085677729)
The Old Man has mean: True or False?
True (0.8936811689868521)
The Old Man has no mean: True or False?
Map:  72%|███████▏  | 147/203 [1:34:02<37:20, 40.01s/ examples]Map:  73%|███████▎  | 148/203 [1:34:40<35:59, 39.26s/ examples]True (0.7745833916423246)
The Old Man has motive: True or False?
True (0.785637679813794)
The Old Man has no motive: True or False?
True (0.6930576545194829)
The Old Man has opportunity: True or False?
True (0.6451199006197486)
The Old Man has no opportunity: True or False?
False (0.6315942370470465)
The Waffle Man is guilty: True or False?
True (0.7049732238008671)
The Waffle Man is not guilty: True or False?
True (0.6540113048720497)
The Waffle Man has mean: True or False?
True (0.8402589628813668)
The Waffle Man has no mean: True or False?
True (0.6984323202883935)
The Waffle Man has motive: True or False?
True (0.7759445334082792)
The Waffle Man has no motive: True or False?
True (0.6334102859975052)
The Waffle Man has opportunity: True or False?
True (0.6697448487720212)
The Waffle Man has no opportunity: True or False?
True (0.5136684743338078)
Vera is guilty: True or False?
True (0.7468781997658912)
Vera is not guilty: True or False?
True (0.854884683810039)
Vera has mean: True or False?
True (0.7704647687904915)
Vera has no mean: True or False?
True (0.5679366075542497)
Vera has motive: True or False?
True (0.8877896081343184)
Vera has no motive: True or False?
True (0.6495786332146115)
Vera has opportunity: True or False?
True (0.7333563569098757)
Vera has no opportunity: True or False?
False (0.5399537164111071)
### Larry
- mean: False (0.37662314309733835)
- motive: False (0.46684563308131055)
- opportunity: False (0.0)

### The Old Man
- mean: True (0.8936811689868521)
- motive: True (0.785637679813794)
- opportunity: True (0.6451199006197486)

### The Waffle Man
- mean: False (0.3015676797116065)
- motive: False (0.36658971400249485)
- opportunity: False (0.4863315256661922)

### Vera
- mean: False (0.4320633924457503)
- motive: False (0.3504213667853885)
- opportunity: False (0.0)

The culprit is The Old Man.
In fact, it is Vera.
## 5minutemystery-the-sunday-school-tithe-mystery
Doc Bentson is guilty: True or False?
True (0.8278281666221954)
Doc Bentson is not guilty: True or False?
True (0.8633915828320894)
Doc Bentson has mean: True or False?
True (0.816406362162552)
Doc Bentson has no mean: True or False?
True (0.5563995964631269)
Doc Bentson has motive: True or False?
True (0.7371581232960549)
Doc Bentson has no motive: True or False?
True (0.6774740084332073)
Doc Bentson has opportunity: True or False?
True (0.5263427467960875)
Doc Bentson has no opportunity: True or False?
False (0.6187804294217345)
Ellie Wilson is guilty: True or False?
True (0.6325027218909103)
Ellie Wilson is not guilty: True or False?
True (0.6388352560545881)
Ellie Wilson has mean: True or False?
True (0.8349459127213729)
Ellie Wilson has no mean: True or False?
True (0.5438324636094939)
Ellie Wilson has motive: True or False?
True (0.6187804294217345)
Ellie Wilson has no motive: True or False?
True (0.6352224318508648)
Ellie Wilson has opportunity: True or False?
False (0.5243946792389143)
Ellie Wilson has no opportunity: True or False?
False (0.5888891269161294)
James Gant is guilty: True or False?
True (0.7371581232960549)
James Gant is not guilty: True or False?
True (0.7570767382203575)
James Gant has mean: True or False?
True (0.8879840376027315)
James Gant has no mean: True or False?
False (0.5496406074054949)
James Gant has motive: True or False?
True (0.7209580648179327)
James Gant has no motive: True or False?
True (0.5573635130218721)
James Gant has opportunity: True or False?
False (0.5097643762740132)
James Gant has no opportunity: True or False?
False (0.6808785831877406)
Judy Gant is guilty: True or False?
True (0.615087818987177)
Judy Gant is not guilty: True or False?
True (0.595492552580428)
Judy Gant has mean: True or False?
True (0.8484706895507578)
Judy Gant has no mean: True or False?
True (0.5496406074054949)
Judy Gant has motive: True or False?
True (0.6766198919456847)
Judy Gant has no motive: True or False?
True (0.5755879969637064)
Judy Gant has opportunity: True or False?
False (0.5409238326546766)
Judy Gant has no opportunity: True or False?
False (0.6671476389322356)
Waylon Marsh is guilty: True or False?
True (0.7287483223557857)
Waylon Marsh is not guilty: True or False?
True (0.7606506318580792)
Waylon Marsh has mean: True or False?
True (0.8872045854516336)
Waylon Marsh has no mean: True or False?
True (0.7541915239138703)
Waylon Marsh has motive: True or False?
True (0.5525396910980834)
Waylon Marsh has no motive: True or False?
False (0.5621765360769869)
Waylon Marsh has opportunity: True or False?
True (0.6680145240815963)
Waylon Marsh has no opportunity: True or False?
False (0.5573635130218721)
### Doc Bentson
- mean: False (0.44360040353687313)
- motive: False (0.32252599156679274)
- opportunity: False (0.0)

### Ellie Wilson
- mean: False (0.4561675363905061)
- motive: False (0.3647775681491352)
- opportunity: False (0.5243946792389143)

### James Gant
- mean: False (0.0)
- motive: False (0.44263648697812785)
- opportunity: False (0.5097643762740132)

### Judy Gant
- mean: False (0.4503593925945051)
- motive: False (0.42441200303629356)
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
Alice Cartwright is not guilty: True or False?
True (0.5273165068094335)
Alice Cartwright has mean: True or False?
True (0.6834194581047349)
Alice Cartwright has no mean: True or False?
False (0.6943026818003076)
Alice Cartwright has motive: True or False?
True (0.7008948290825966)
Alice Cartwright has no motive: True or False?
False (0.686790355176806)
Alice Cartwright has opportunity: True or False?
False (0.6270381219830087)
Alice Cartwright has no opportunity: True or False?
False (0.8311430831606665)
Arthur Glendon is guilty: True or False?
True (0.7956580548514487)
Arthur Glendon is not guilty: True or False?
True (0.9666144932745312)
Arthur Glendon has mean: True or False?
True (0.8591918406281239)
Arthur Glendon has no mean: True or False?
False (0.6566582893190611)
Arthur Glendon has motive: True or False?
True (0.8864203688833437)
Arthur Glendon has no motive: True or False?
True (0.5087881220234095)
Arthur Glendon has opportunity: True or False?
False (0.5559174351137421)
Arthur Glendon has no opportunity: True or False?
False (0.7659436444086731)
Janice Starling is guilty: True or False?
False (0.5650587803792624)
Janice Starling is not guilty: True or False?
False (0.6169358476670045)
Janice Starling has mean: True or False?
True (0.8615382357584752)
Janice Starling has no mean: True or False?
False (0.6943026818003076)
Janice Starling has motive: True or False?
True (0.5832033352502285)
Janice Starling has no motive: True or False?
False (0.7201714538416826)
Janice Starling has opportunity: True or False?
False (0.7512834059294674)
Janice Starling has no opportunity: True or False?
False (0.8454326455643386)
Sandra Buckingham is guilty: True or False?
False (0.5983121871760707)
Sandra Buckingham is not guilty: True or False?
False (0.6749080895533367)
Sandra Buckingham has mean: True or False?
True (0.6680145240815963)
Sandra Buckingham has no mean: True or False?
False (0.7386690294153369)
Sandra Buckingham has motive: True or False?
True (0.5832033700118571)
Sandra Buckingham has no motive: True or False?
False (0.7082125449089324)
Sandra Buckingham has opportunity: True or False?
False (0.8807970862580315)
Sandra Buckingham has no opportunity: True or False?
False (0.8344069148356309)
### Alice Cartwright
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.6270381219830087)

### Arthur Glendon
- mean: False (0.0)
- motive: False (0.4912118779765905)
- opportunity: False (0.5559174351137421)

### Janice Starling
- mean: True (0.8615382357584752)
- motive: True (0.5832033352502285)
- opportunity: True (0.15456735443566139)

### Sandra Buckingham
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.8807970862580315)

The culprit is Janice Starling.
In fact, it is Arthur Glendon.Map:  73%|███████▎  | 149/203 [1:35:21<35:50, 39.83s/ examples]Map:  74%|███████▍  | 150/203 [1:35:48<31:59, 36.21s/ examples]Map:  74%|███████▍  | 151/203 [1:36:27<31:57, 36.88s/ examples]Map:  75%|███████▍  | 152/203 [1:37:09<32:39, 38.42s/ examples]
## 5minutemystery-the-anonymous-bank-robber
Edward Cantrell is guilty: True or False?
True (0.7325918709325988)
Edward Cantrell is not guilty: True or False?
True (0.7130321757210903)
Edward Cantrell has mean: True or False?
True (0.6710395233636681)
Edward Cantrell has no mean: True or False?
False (0.6714705702070799)
Edward Cantrell has motive: True or False?
False (0.5983121871760707)
Edward Cantrell has no motive: True or False?
True (0.5243946792389143)
Edward Cantrell has opportunity: True or False?
False (0.7033457082786769)
Edward Cantrell has no opportunity: True or False?
False (0.5926666351772785)
Larry Brooks is guilty: True or False?
True (0.6766198919456847)
Larry Brooks is not guilty: True or False?
True (0.7704647687904915)
Larry Brooks has mean: True or False?
True (0.5165954726976894)
Larry Brooks has no mean: True or False?
False (0.7130321332210621)
Larry Brooks has motive: True or False?
False (0.6522414018725713)
Larry Brooks has no motive: True or False?
True (0.5860491337676195)
Larry Brooks has opportunity: True or False?
False (0.867485409735739)
Larry Brooks has no opportunity: True or False?
False (0.8187367896794966)
Lester Barton is guilty: True or False?
True (0.8062431235779619)
Lester Barton is not guilty: True or False?
True (0.8402590129647053)
Lester Barton has mean: True or False?
True (0.7371581232960549)
Lester Barton has no mean: True or False?
False (0.6976088896786037)
Lester Barton has motive: True or False?
False (0.5009765603034438)
Lester Barton has no motive: True or False?
True (0.6926419789019715)
Lester Barton has opportunity: True or False?
False (0.7424217332471881)
Lester Barton has no opportunity: True or False?
False (0.5907791930117218)
Oscar Jordan is guilty: True or False?
True (0.8086723099497763)
Oscar Jordan is not guilty: True or False?
True (0.84440905415483)
Oscar Jordan has mean: True or False?
True (0.6619228707202935)
Oscar Jordan has no mean: True or False?
False (0.5869964306477841)
Oscar Jordan has motive: True or False?
True (0.6601723415572317)
Oscar Jordan has no motive: True or False?
True (0.7634837587244478)
Oscar Jordan has opportunity: True or False?
False (0.5602526707659626)
Oscar Jordan has no opportunity: True or False?
True (0.589834510337428)
### Edward Cantrell
- mean: False (0.0)
- motive: False (0.5983121871760707)
- opportunity: False (0.7033457082786769)

### Larry Brooks
- mean: False (0.0)
- motive: False (0.6522414018725713)
- opportunity: False (0.867485409735739)

### Lester Barton
- mean: True (0.7371581232960549)
- motive: True (0.0)
- opportunity: True (0.40922080698827823)

### Oscar Jordan
- mean: False (0.0)
- motive: False (0.23651624127555215)
- opportunity: False (0.5602526707659626)

The culprit is Lester Barton.
In fact, it is Lester Barton.
## 5minutemystery-the-house-of-lies
Debra is guilty: True or False?
True (0.5486734987923966)
Debra is not guilty: True or False?
True (0.7017130830397807)
Debra has mean: True or False?
True (0.7956581141325956)
Debra has no mean: True or False?
True (0.5774953314585229)
Debra has motive: True or False?
True (0.7924642605907138)
Debra has no motive: True or False?
False (0.5568816117266226)
Debra has opportunity: True or False?
True (0.6636689828419103)
Debra has no opportunity: True or False?
False (0.644225125126315)
Luke is guilty: True or False?
False (0.5360700410935405)
Luke is not guilty: True or False?
False (0.5312093941731293)
Luke has mean: True or False?
True (0.6076632024562351)
Luke has no mean: True or False?
False (0.7318258918270596)
Luke has motive: True or False?
True (0.7189891821820716)
Luke has no motive: True or False?
False (0.7314423961079403)
Luke has opportunity: True or False?
True (0.6178585273774891)
Luke has no opportunity: True or False?
False (0.8960695891821668)
Olivia is guilty: True or False?
True (0.6020615685826383)
Olivia is not guilty: True or False?
True (0.5832033352502285)
Olivia has mean: True or False?
True (0.6757646168022439)
Olivia has no mean: True or False?
False (0.5869964306477841)
Olivia has motive: True or False?
True (0.8679338697256817)
Olivia has no motive: True or False?
False (0.5048826258478675)
Olivia has opportunity: True or False?
True (0.7549149897594328)
Olivia has no opportunity: True or False?
False (0.621540893468236)
The Butler is guilty: True or False?
True (0.9008791478232747)
The Butler is not guilty: True or False?
True (0.8494724067948436)
The Butler has mean: True or False?
True (0.8322366416985943)
The Butler has no mean: True or False?
True (0.6370307821695329)
The Butler has motive: True or False?
True (0.795340359502468)
The Butler has no motive: True or False?
True (0.5822535180679596)
The Butler has opportunity: True or False?
True (0.7655933544531522)
The Butler has no opportunity: True or False?
True (0.6020615685826383)
### Debra
- mean: False (0.42250466854147706)
- motive: False (0.0)
- opportunity: False (0.0)

### Luke
- mean: True (0.6076632024562351)
- motive: True (0.7189891821820716)
- opportunity: True (0.6178585273774891)

### Olivia
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.0)

### The Butler
- mean: False (0.3629692178304671)
- motive: False (0.41774648193204045)
- opportunity: False (0.39793843141736174)

The culprit is Luke.
In fact, it is The Butler.
## 5minutemystery-the-straw-hat-theater-mysterieson-stage
Grace Upshaw is guilty: True or False?
True (0.8984105603938967)
Grace Upshaw is not guilty: True or False?
True (0.8631610889096435)
Grace Upshaw has mean: True or False?
True (0.7341194746845218)
Grace Upshaw has no mean: True or False?
False (0.64063590602721)
Grace Upshaw has motive: True or False?
True (0.8365545874520802)
Grace Upshaw has no motive: True or False?
True (0.6601723415572317)
Grace Upshaw has opportunity: True or False?
True (0.5945512478395265)
Grace Upshaw has no opportunity: True or False?
False (0.6169358476670045)
Linda Grant is guilty: True or False?
True (0.8474634858439474)
Linda Grant is not guilty: True or False?
True (0.8059378226074421)
Linda Grant has mean: True or False?
True (0.7333563569098757)
Linda Grant has no mean: True or False?
False (0.5467381591701916)
Linda Grant has motive: True or False?
True (0.6667138235236917)
Linda Grant has no motive: True or False?
True (0.5592900581575188)
Linda Grant has opportunity: True or False?
False (0.5784481782924303)
Linda Grant has no opportunity: True or False?
False (0.7697732451157533)
Molly Trumbull is guilty: True or False?
True (0.7394224480813394)
Molly Trumbull is not guilty: True or False?
True (0.6081287294536162)
Molly Trumbull has mean: True or False?
True (0.6909762697651828)
Molly Trumbull has no mean: True or False?
False (0.8107787408238168)
Molly Trumbull has motive: True or False?
True (0.5539879783000323)
Molly Trumbull has no motive: True or False?
False (0.6901415551283886)
Molly Trumbull has opportunity: True or False?
False (0.6897237229704902)
Molly Trumbull has no opportunity: True or False?
False (0.8931231526306965)
Samantha Powers is guilty: True or False?
True (0.873646620599733)
Samantha Powers is not guilty: True or False?
True (0.7803278530774741)
Samantha Powers has mean: True or False?
True (0.8193157317863493)
Samantha Powers has no mean: True or False?
False (0.7279754274224494)
Samantha Powers has motive: True or False?
True (0.621540893468236)
Samantha Powers has no motive: True or False?
True (0.6428809774412343)
Samantha Powers has opportunity: True or False?
False (0.6085939964125278)
Samantha Powers has no opportunity: True or False?
False (0.7876046283319926)
### Grace Upshaw
- mean: False (0.0)
- motive: False (0.3398276584427683)
- opportunity: False (0.0)

### Linda Grant
- mean: False (0.0)
- motive: False (0.44070994184248125)
- opportunity: False (0.5784481782924303)

### Molly Trumbull
- mean: True (0.6909762697651828)
- motive: True (0.5539879783000323)
- opportunity: True (0.10687684736930347)

### Samantha Powers
- mean: False (0.0)
- motive: False (0.3571190225587657)
- opportunity: False (0.6085939964125278)

The culprit is Molly Trumbull.
In fact, it is Grace Upshaw.
## 5minutemystery-canada-day
Map:  75%|███████▌  | 153/203 [1:37:42<30:46, 36.92s/ examples]Map:  76%|███████▌  | 154/203 [1:38:20<30:23, 37.22s/ examples]Little black-haired girl is guilty: True or False?
False (0.5009765603034438)
Little black-haired girl is not guilty: True or False?
True (0.6557770400181139)
Little black-haired girl has mean: True or False?
False (0.5515737608116735)
Little black-haired girl has no mean: True or False?
True (0.6834195192071987)
Little black-haired girl has motive: True or False?
True (0.7279754274224494)
Little black-haired girl has no motive: True or False?
True (0.5879430860094185)
Little black-haired girl has opportunity: True or False?
False (0.6951311179371613)
Little black-haired girl has no opportunity: True or False?
False (0.811078188867804)
Redheaded woman is guilty: True or False?
True (0.6252092625510083)
Redheaded woman is not guilty: True or False?
True (0.6967842494573921)
Redheaded woman has mean: True or False?
True (0.5563995964631269)
Redheaded woman has no mean: True or False?
True (0.705785027818136)
Redheaded woman has motive: True or False?
True (0.8238959285889558)
Redheaded woman has no motive: True or False?
True (0.7233095190955371)
Redheaded woman has opportunity: True or False?
True (0.570809902165233)
Redheaded woman has no opportunity: True or False?
False (0.8193157928301305)
Stocky blonde man is guilty: True or False?
True (0.6943026818003076)
Stocky blonde man is not guilty: True or False?
True (0.7074047371961694)
Stocky blonde man has mean: True or False?
True (0.5312093941731293)
Stocky blonde man has no mean: True or False?
False (0.5869964306477841)
Stocky blonde man has motive: True or False?
True (0.7033457082786769)
Stocky blonde man has no motive: True or False?
True (0.6619228707202935)
Stocky blonde man has opportunity: True or False?
False (0.7364006034245382)
Stocky blonde man has no opportunity: True or False?
False (0.7937461674149602)
Tall bald man is guilty: True or False?
True (0.5813030995752883)
Tall bald man is not guilty: True or False?
True (0.6020615685826383)
Tall bald man has mean: True or False?
False (0.525368812147771)
Tall bald man has no mean: True or False?
False (0.5496406401666291)
Tall bald man has motive: True or False?
True (0.7041600870830834)
Tall bald man has no motive: True or False?
True (0.6104534962074417)
Tall bald man has opportunity: True or False?
False (0.7570767382203575)
Tall bald man has no opportunity: True or False?
False (0.7988153087356352)
### Little black-haired girl
- mean: False (0.5515737608116735)
- motive: False (0.41205691399058153)
- opportunity: False (0.6951311179371613)

### Redheaded woman
- mean: True (0.5563995964631269)
- motive: True (0.8238959285889558)
- opportunity: True (0.570809902165233)

### Stocky blonde man
- mean: False (0.0)
- motive: False (0.33807712927970646)
- opportunity: False (0.7364006034245382)

### Tall bald man
- mean: False (0.525368812147771)
- motive: False (0.3895465037925583)
- opportunity: False (0.7570767382203575)

The culprit is Redheaded woman.
In fact, it is Tall bald man.
## 5minutemystery-the-missing-communion-set
Allison Jordan is guilty: True or False?
True (0.6469064338453809)
Allison Jordan is not guilty: True or False?
True (0.6627964381792564)
Allison Jordan has mean: True or False?
True (0.6791786560103119)
Allison Jordan has no mean: True or False?
False (0.6926419789019715)
Allison Jordan has motive: True or False?
True (0.65489470935198)
Allison Jordan has no motive: True or False?
False (0.6842640081724978)
Allison Jordan has opportunity: True or False?
False (0.6817267994905651)
Allison Jordan has no opportunity: True or False?
False (0.7950222460539826)
Heather Guse is guilty: True or False?
True (0.6197014353942354)
Heather Guse is not guilty: True or False?
True (0.5813030649269245)
Heather Guse has mean: True or False?
True (0.8031737798924701)
Heather Guse has no mean: True or False?
True (0.5612147992901458)
Heather Guse has motive: True or False?
True (0.8386797310322072)
Heather Guse has no motive: True or False?
True (0.6270381219830087)
Heather Guse has opportunity: True or False?
False (0.8365545251239088)
Heather Guse has no opportunity: True or False?
False (0.7956581141325956)
Janelle Herbst is guilty: True or False?
False (0.503906199448032)
Janelle Herbst is not guilty: True or False?
False (0.5448014304301324)
Janelle Herbst has mean: True or False?
True (0.776622945813876)
Janelle Herbst has no mean: True or False?
True (0.5945512478395265)
Janelle Herbst has motive: True or False?
True (0.7386690294153369)
Janelle Herbst has no motive: True or False?
False (0.5888891269161294)
Janelle Herbst has opportunity: True or False?
False (0.7520125537161032)
Janelle Herbst has no opportunity: True or False?
False (0.8037905715242155)
Josh Darvin is guilty: True or False?
True (0.8187367896794966)
Josh Darvin is not guilty: True or False?
True (0.708212608228071)
Josh Darvin has mean: True or False?
True (0.6976088896786037)
Josh Darvin has no mean: True or False?
True (0.5117165908639297)
Josh Darvin has motive: True or False?
True (0.8499711693725173)
Josh Darvin has no motive: True or False?
True (0.5477060024984176)
Josh Darvin has opportunity: True or False?
False (0.6433293282949071)
Josh Darvin has no opportunity: True or False?
False (0.7401742969616896)
Justin Paul is guilty: True or False?
True (0.7090191197769757)
Justin Paul is not guilty: True or False?
True (0.6132365353114321)
Justin Paul has mean: True or False?
True (0.6001883144765984)
Justin Paul has no mean: True or False?
False (0.648688963544537)
Justin Paul has motive: True or False?
True (0.814643384779728)
Justin Paul has no motive: True or False?
False (0.5448013654847448)
Justin Paul has opportunity: True or False?
False (0.7570766705324253)
Justin Paul has no opportunity: True or False?
False (0.7931059536445917)
### Allison Jordan
- mean: True (0.6791786560103119)
- motive: True (0.65489470935198)
- opportunity: True (0.20497775394601736)

### Heather Guse
- mean: False (0.43878520070985416)
- motive: False (0.3729618780169913)
- opportunity: False (0.8365545251239088)

### Janelle Herbst
- mean: False (0.4054487521604735)
- motive: False (0.0)
- opportunity: False (0.7520125537161032)

### Josh Darvin
- mean: False (0.48828340913607027)
- motive: False (0.4522939975015824)
- opportunity: False (0.6433293282949071)

### Justin Paul
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.7570766705324253)

The culprit is Allison Jordan.
In fact, it is Josh Darvin.
## 5minutemystery-who-stole-super-bowl-sunday
Aunt Mary is guilty: True or False?
True (0.7879311977554747)
Aunt Mary is not guilty: True or False?
True (0.7872777601997338)
Aunt Mary has mean: True or False?
True (0.8311430212356835)
Aunt Mary has no mean: True or False?
True (0.5515736950589613)
Aunt Mary has motive: True or False?
True (0.8204694405411458)
Aunt Mary has no motive: True or False?
True (0.7981867775042927)
Aunt Mary has opportunity: True or False?
True (0.5428632463719839)
Aunt Mary has no opportunity: True or False?
False (0.6522414018725713)
Phil is guilty: True or False?
True (0.9246876822649571)
Phil is not guilty: True or False?
True (0.9241418261705818)
Phil has mean: True or False?
True (0.8006920257960423)
Phil has no mean: True or False?
False (0.5097643762740132)
Phil has motive: True or False?
True (0.8062431235779619)
Phil has no motive: True or False?
True (0.7248702601920561)
Phil has opportunity: True or False?
True (0.720171518230031)
Phil has no opportunity: True or False?
False (0.5563995964631269)
Rick is guilty: True or False?
True (0.8885655424665229)
Rick is not guilty: True or False?
True (0.8870089652491843)
Rick has mean: True or False?
True (0.7704647687904915)
Rick has no mean: True or False?
False (0.5321820387813727)
Rick has motive: True or False?
True (0.8300437258865985)
Rick has no motive: True or False?
True (0.705785027818136)
Rick has opportunity: True or False?
True (0.6415346823638186)
Rick has no opportunity: True or False?
False (0.6279512069990912)
Uncle Charlie is guilty: True or False?
True (0.9709643714595256)
Uncle Charlie is not guilty: True or False?
True (0.9790757889289493)
Uncle Charlie has mean: True or False?
True (0.9019206778000431)
Uncle Charlie has no mean: True or False?Map:  76%|███████▋  | 155/203 [1:38:52<28:22, 35.46s/ examples]Map:  77%|███████▋  | 156/203 [1:39:23<26:45, 34.15s/ examples]Map:  77%|███████▋  | 157/203 [1:39:58<26:30, 34.58s/ examples]
True (0.8459424357871997)
Uncle Charlie has motive: True or False?
True (0.9235923286659299)
Uncle Charlie has no motive: True or False?
True (0.861071588244826)
Uncle Charlie has opportunity: True or False?
True (0.8966140749572745)
Uncle Charlie has no opportunity: True or False?
True (0.720171518230031)
### Aunt Mary
- mean: False (0.44842630494103874)
- motive: False (0.20181322249570732)
- opportunity: False (0.0)

### Phil
- mean: True (0.8006920257960423)
- motive: True (0.8062431235779619)
- opportunity: True (0.720171518230031)

### Rick
- mean: False (0.0)
- motive: False (0.294214972181864)
- opportunity: False (0.0)

### Uncle Charlie
- mean: False (0.15405756421280026)
- motive: False (0.138928411755174)
- opportunity: False (0.279828481769969)

The culprit is Phil.
In fact, it is Aunt Mary.
## 5minutemystery-the-cocktail-conundrum
Ian Fairbank is guilty: True or False?
True (0.8019358443954961)
Ian Fairbank is not guilty: True or False?
True (0.636127168259503)
Ian Fairbank has mean: True or False?
True (0.8489722037469682)
Ian Fairbank has no mean: True or False?
True (0.5640984675176304)
Ian Fairbank has motive: True or False?
True (0.875361437979977)
Ian Fairbank has no motive: True or False?
True (0.6334102859975052)
Ian Fairbank has opportunity: True or False?
True (0.897695304229796)
Ian Fairbank has no opportunity: True or False?
True (0.5698526542706361)
Mr. Fairbank is guilty: True or False?
True (0.842345065078002)
Mr. Fairbank is not guilty: True or False?
True (0.7641883982873323)
Mr. Fairbank has mean: True or False?
True (0.8438950825214144)
Mr. Fairbank has no mean: True or False?
False (0.5156198737738186)
Mr. Fairbank has motive: True or False?
True (0.8216173055802608)
Mr. Fairbank has no motive: True or False?
True (0.8227595062673136)
Mr. Fairbank has opportunity: True or False?
True (0.8601343090488404)
Mr. Fairbank has no opportunity: True or False?
True (0.6959583025067009)
Mr. Lewis Rhys is guilty: True or False?
True (0.7461389980806673)
Mr. Lewis Rhys is not guilty: True or False?
True (0.6334102859975052)
Mr. Lewis Rhys has mean: True or False?
True (0.9066531077351827)
Mr. Lewis Rhys has no mean: True or False?
True (0.6575384105121485)
Mr. Lewis Rhys has motive: True or False?
True (0.789233749534095)
Mr. Lewis Rhys has no motive: True or False?
True (0.6934729182490079)
Mr. Lewis Rhys has opportunity: True or False?
True (0.8134607635851566)
Mr. Lewis Rhys has no opportunity: True or False?
True (0.566977858563838)
Mrs. Fairbank is guilty: True or False?
True (0.9190632712053527)
Mrs. Fairbank is not guilty: True or False?
True (0.8244618718686391)
Mrs. Fairbank has mean: True or False?
True (0.9431384818142104)
Mrs. Fairbank has no mean: True or False?
True (0.726425644352388)
Mrs. Fairbank has motive: True or False?
True (0.9456006903352807)
Mrs. Fairbank has no motive: True or False?
True (0.8122723669190336)
Mrs. Fairbank has opportunity: True or False?
True (0.9317114347547434)
Mrs. Fairbank has no opportunity: True or False?
True (0.8652240590801695)
### Ian Fairbank
- mean: False (0.4359015324823696)
- motive: False (0.36658971400249485)
- opportunity: False (0.43014734572936386)

### Mr. Fairbank
- mean: True (0.8438950825214144)
- motive: True (0.8216173055802608)
- opportunity: True (0.8601343090488404)

### Mr. Lewis Rhys
- mean: False (0.34246158948785155)
- motive: False (0.3065270817509921)
- opportunity: False (0.433022141436162)

### Mrs. Fairbank
- mean: False (0.273574355647612)
- motive: False (0.1877276330809664)
- opportunity: False (0.13477594091983047)

The culprit is Mr. Fairbank.
In fact, it is Mrs. Fairbank.
## 5minutemystery-the-gypsys-secret-numbers
Great Marchelli is guilty: True or False?
True (0.9577545517476556)
Great Marchelli is not guilty: True or False?
True (0.9621431229853287)
Great Marchelli has mean: True or False?
True (0.9322068701708559)
Great Marchelli has no mean: True or False?
True (0.9079670935046645)
Great Marchelli has motive: True or False?
True (0.966726005782453)
Great Marchelli has no motive: True or False?
True (0.9549004429672318)
Great Marchelli has opportunity: True or False?
True (0.958769975577766)
Great Marchelli has no opportunity: True or False?
True (0.9391365661970741)
Lorenzo is guilty: True or False?
True (0.924823579961238)
Lorenzo is not guilty: True or False?
True (0.9545204053129497)
Lorenzo has mean: True or False?
True (0.8407825844829613)
Lorenzo has no mean: True or False?
True (0.7348812840309261)
Lorenzo has motive: True or False?
True (0.9456006903352807)
Lorenzo has no motive: True or False?
True (0.9296962009164971)
Lorenzo has opportunity: True or False?
True (0.940735282281303)
Lorenzo has no opportunity: True or False?
False (0.4200705867645463)
Ringmaster is guilty: True or False?
True (0.9324532728823121)
Ringmaster is not guilty: True or False?
True (0.9299510719523877)
Ringmaster has mean: True or False?
True (0.9007046239919082)
Ringmaster has no mean: True or False?
True (0.7687331368312712)
Ringmaster has motive: True or False?
True (0.9717254050158363)
Ringmaster has no motive: True or False?
True (0.9552356617277232)
Ringmaster has opportunity: True or False?
True (0.9546474221708894)
Ringmaster has no opportunity: True or False?
True (0.942612469657282)
Sheriff is guilty: True or False?
True (0.9100670238942131)
Sheriff is not guilty: True or False?
True (0.9228308210322659)
Sheriff has mean: True or False?
True (0.8860265599597172)
Sheriff has no mean: True or False?
True (0.8338664134858856)
Sheriff has motive: True or False?
True (0.9522199623739209)
Sheriff has no motive: True or False?
True (0.944893063704541)
Sheriff has opportunity: True or False?
True (0.9493885642537184)
Sheriff has no opportunity: True or False?
True (0.9528381834886748)
### Great Marchelli
- mean: False (0.09203290649533546)
- motive: False (0.045099557032768245)
- opportunity: False (0.060863433802925915)

### Lorenzo
- mean: True (0.8407825844829613)
- motive: True (0.9456006903352807)
- opportunity: True (0.940735282281303)

### Ringmaster
- mean: False (0.2312668631687288)
- motive: False (0.04476433827227677)
- opportunity: False (0.05738753034271804)

### Sheriff
- mean: False (0.16613358651411436)
- motive: False (0.05510693629545904)
- opportunity: False (0.04716181651132523)

The culprit is Lorenzo.
In fact, it is Sheriff.
## 5minutemystery-its-gone
Abe is guilty: True or False?
True (0.8244619332958376)
Abe is not guilty: True or False?
True (0.9149009617112335)
Abe has mean: True or False?
True (0.9224823751318276)
Abe has no mean: True or False?
True (0.7592253761865491)
Abe has motive: True or False?
True (0.8799743689174987)
Abe has no motive: True or False?
True (0.8269914342149828)
Abe has opportunity: True or False?
True (0.7680380401429294)
Abe has no opportunity: True or False?
True (0.6370307821695329)
Lance is guilty: True or False?
True (0.8741846653426761)
Lance is not guilty: True or False?
True (0.9062390341149371)
Lance has mean: True or False?
True (0.7846493136763113)
Lance has no mean: True or False?
True (0.7520125537161032)
Lance has motive: True or False?
True (0.9189178954169608)
Lance has no motive: True or False?
True (0.8384153298109808)
Lance has opportunity: True or False?
True (0.8474634858439474)
Lance has no opportunity: True or False?
True (0.6627964974378784)
The Amazing Andrew is guilty: True or False?
True (0.8940516749601143)
The Amazing Andrew is not guilty: True or False?
True (0.8781053402372203)
The Amazing Andrew has mean: True or False?
True (0.8958875533219306)
The Amazing Andrew has no mean: True or False?
True (0.7969253675907205)
The Amazing Andrew has motive: True or False?
True (0.9328213936074807)
The Amazing Andrew has no motive: True or False?
True (0.8474634353311888)
The Amazing Andrew has opportunity: True or False?
True (0.7563575572780217)
The Amazing Andrew has no opportunity: True or False?
True (0.6522414018725713)
Zora the Magnificent is guilty: True or False?
True (0.8241790481509624)
Zora the Magnificent is not guilty: True or False?
True (0.8184467585979083)
Zora the Magnificent has mean: True or False?
True (0.769080279275001)
Map:  78%|███████▊  | 158/203 [1:40:39<27:20, 36.45s/ examples]Map:  78%|███████▊  | 159/203 [1:41:16<26:43, 36.44s/ examples]Map:  79%|███████▉  | 160/203 [1:41:34<22:20, 31.18s/ examples]Zora the Magnificent has no mean: True or False?
True (0.7704647687904915)
Zora the Magnificent has motive: True or False?
True (0.9095863097773887)
Zora the Magnificent has no motive: True or False?
True (0.8227594449669557)
Zora the Magnificent has opportunity: True or False?
True (0.7585106418731645)
Zora the Magnificent has no opportunity: True or False?
False (0.5380124470448935)
### Abe
- mean: False (0.24077462381345094)
- motive: False (0.17300856578501722)
- opportunity: False (0.3629692178304671)

### Lance
- mean: False (0.2479874462838968)
- motive: False (0.16158467018901923)
- opportunity: False (0.3372035025621216)

### The Amazing Andrew
- mean: False (0.20307463240927948)
- motive: False (0.15253656466881116)
- opportunity: False (0.3477585981274287)

### Zora the Magnificent
- mean: True (0.769080279275001)
- motive: True (0.9095863097773887)
- opportunity: True (0.7585106418731645)

The culprit is Zora the Magnificent.
In fact, it is The Amazing Andrew.
## 5minutemystery-the-misers-hoard
Bob Parsons is guilty: True or False?
True (0.9735944874605075)
Bob Parsons is not guilty: True or False?
True (0.9291838438109349)
Bob Parsons has mean: True or False?
True (0.9564718616162037)
Bob Parsons has no mean: True or False?
True (0.740174341079517)
Bob Parsons has motive: True or False?
True (0.9536650199751218)
Bob Parsons has no motive: True or False?
True (0.9455000750830757)
Bob Parsons has opportunity: True or False?
True (0.7898827135821628)
Bob Parsons has no opportunity: True or False?
True (0.673191669892235)
John Entwhistle III is guilty: True or False?
True (0.9299510095943111)
John Entwhistle III is not guilty: True or False?
True (0.8816149238192855)
John Entwhistle III has mean: True or False?
True (0.8879840376027315)
John Entwhistle III has no mean: True or False?
True (0.7641884666111024)
John Entwhistle III has motive: True or False?
True (0.9579909444975866)
John Entwhistle III has no motive: True or False?
True (0.9224823132745662)
John Entwhistle III has opportunity: True or False?
True (0.7098244343353132)
John Entwhistle III has no opportunity: True or False?
True (0.5964331079469681)
Sam Greenway is guilty: True or False?
True (0.9515039936355008)
Sam Greenway is not guilty: True or False?
True (0.9073122726900733)
Sam Greenway has mean: True or False?
True (0.91789335161495)
Sam Greenway has no mean: True or False?
True (0.7527403228571042)
Sam Greenway has motive: True or False?
True (0.9173766997328059)
Sam Greenway has no motive: True or False?
True (0.8352149074858963)
Sam Greenway has opportunity: True or False?
True (0.8181563669811865)
Sam Greenway has no opportunity: True or False?
True (0.648688963544537)
Sarah Parsons is guilty: True or False?
True (0.958769975577766)
Sarah Parsons is not guilty: True or False?
True (0.8893367679552574)
Sarah Parsons has mean: True or False?
True (0.9173026661190045)
Sarah Parsons has no mean: True or False?
True (0.5214711377329961)
Sarah Parsons has motive: True or False?
True (0.9231777821690265)
Sarah Parsons has no motive: True or False?
True (0.859427933964502)
Sarah Parsons has opportunity: True or False?
True (0.6992543888266708)
Sarah Parsons has no opportunity: True or False?
True (0.5794004215835179)
### Bob Parsons
- mean: False (0.25982565892048304)
- motive: False (0.05449992491692435)
- opportunity: False (0.326808330107765)

### John Entwhistle III
- mean: True (0.8879840376027315)
- motive: True (0.9579909444975866)
- opportunity: True (0.7098244343353132)

### Sam Greenway
- mean: False (0.24725967714289576)
- motive: False (0.16478509251410367)
- opportunity: False (0.351311036455463)

### Sarah Parsons
- mean: False (0.47852886226700386)
- motive: False (0.140572066035498)
- opportunity: False (0.4205995784164821)

The culprit is John Entwhistle III.
In fact, it is Sarah Parsons.
## 5minutemystery-the-cornfield-caper
Austin is guilty: True or False?
True (0.7409249009267298)
Austin is not guilty: True or False?
True (0.7739006258141444)
Austin has mean: True or False?
True (0.854884620116169)
Austin has no mean: True or False?
True (0.6851073967858599)
Austin has motive: True or False?
True (0.7074046739492601)
Austin has no motive: True or False?
True (0.7592254214399092)
Austin has opportunity: True or False?
True (0.6113819501087365)
Austin has no opportunity: True or False?
False (0.5418937862055231)
Billy is guilty: True or False?
True (0.621540893468236)
Billy is not guilty: True or False?
True (0.6619228115397798)
Billy has mean: True or False?
True (0.8175745039697023)
Billy has no mean: True or False?
True (0.5688948754232768)
Billy has motive: True or False?
True (0.8104788598666923)
Billy has no motive: True or False?
True (0.7606506998655483)
Billy has opportunity: True or False?
True (0.7994423454932595)
Billy has no opportunity: True or False?
True (0.6584175136252488)
Nick is guilty: True or False?
False (0.5185461538431656)
Nick is not guilty: True or False?
True (0.5321820387813727)
Nick has mean: True or False?
True (0.7859664553110391)
Nick has no mean: True or False?
True (0.6048657973050737)
Nick has motive: True or False?
True (0.7527403228571042)
Nick has no motive: True or False?
True (0.7371581892031299)
Nick has opportunity: True or False?
True (0.678326898500563)
Nick has no opportunity: True or False?
True (0.5869963606723607)
### Austin
- mean: True (0.854884620116169)
- motive: True (0.7074046739492601)
- opportunity: True (0.6113819501087365)

### Billy
- mean: False (0.43110512457672323)
- motive: False (0.23934930013445166)
- opportunity: False (0.3415824863747512)

### Nick
- mean: False (0.3951342026949263)
- motive: False (0.2628418107968701)
- opportunity: False (0.4130036393276393)

The culprit is Austin.
In fact, it is Billy.
## 5minutemystery-a-stolen-future
Donna Blake is guilty: True or False?
True (0.789233749534095)
Donna Blake is not guilty: True or False?
True (0.7078087894899847)
Donna Blake has mean: True or False?
True (0.8198933606225757)
Donna Blake has no mean: True or False?
False (0.6531269509188588)
Donna Blake has motive: True or False?
True (0.7394224480813394)
Donna Blake has no motive: True or False?
True (0.6001883860246252)
Donna Blake has opportunity: True or False?
True (0.7534666630720156)
Donna Blake has no opportunity: True or False?
False (0.5563995964631269)
George Wilson is guilty: True or False?
True (0.7498207054286419)
George Wilson is not guilty: True or False?
True (0.5151320592438547)
George Wilson has mean: True or False?
True (0.7098243920264812)
George Wilson has no mean: True or False?
False (0.8238958672039278)
George Wilson has motive: True or False?
True (0.8322366416985943)
George Wilson has no motive: True or False?
False (0.6306849143569856)
George Wilson has opportunity: True or False?
True (0.7008947664177184)
George Wilson has no opportunity: True or False?
False (0.8638516611889259)
Jeffery Sharp is guilty: True or False?
True (0.8526903338256402)
Jeffery Sharp is not guilty: True or False?
True (0.7174080489207124)
Jeffery Sharp has mean: True or False?
True (0.6379334932841956)
Jeffery Sharp has no mean: True or False?
False (0.7341195403199204)
Jeffery Sharp has motive: True or False?
True (0.816406362162552)
Jeffery Sharp has no motive: True or False?
True (0.7178038242127955)
Jeffery Sharp has opportunity: True or False?
True (0.7786492592534148)
Jeffery Sharp has no opportunity: True or False?
True (0.5029296229885981)
Pete Thompson is guilty: True or False?
True (0.9012274173198201)
Pete Thompson is not guilty: True or False?
True (0.7898827135821628)
Pete Thompson has mean: True or False?
True (0.7853085971692302)
Pete Thompson has no mean: True or False?
False (0.5592899914849522)
Pete Thompson has motive: True or False?
True (0.7662936378892937)
Pete Thompson has no motive: True or False?
True (0.6297746298200823)
Pete Thompson has opportunity: True or False?
True (0.7879311977554747)
Pete Thompson has no opportunity: True or False?
True (0.6020616403539744)
### Donna Blake
- mean: False (0.0)
- motive: False (0.3998116139753748)
- opportunity: False (0.0)

### George Wilson
- mean: True (0.7098243920264812)
Map:  79%|███████▉  | 161/203 [1:42:09<22:35, 32.27s/ examples]Map:  80%|███████▉  | 162/203 [1:43:00<25:53, 37.88s/ examples]Map:  80%|████████  | 163/203 [1:43:46<26:47, 40.19s/ examples]- motive: True (0.8322366416985943)
- opportunity: True (0.7008947664177184)

### Jeffery Sharp
- mean: False (0.0)
- motive: False (0.28219617578720446)
- opportunity: False (0.4970703770114019)

### Pete Thompson
- mean: False (0.0)
- motive: False (0.37022537017991775)
- opportunity: False (0.39793835964602564)

The culprit is George Wilson.
In fact, it is Jeffery Sharp.
## 5minutemystery-the-dirty-half-dozen
Bethany Knight is guilty: True or False?
True (0.8227594449669557)
Bethany Knight is not guilty: True or False?
True (0.7879311977554747)
Bethany Knight has mean: True or False?
True (0.9193534273597669)
Bethany Knight has no mean: True or False?
True (0.7138307093362539)
Bethany Knight has motive: True or False?
True (0.8910549899564296)
Bethany Knight has no motive: True or False?
True (0.7098243285632378)
Bethany Knight has opportunity: True or False?
True (0.7217431689117048)
Bethany Knight has no opportunity: True or False?
True (0.6067315356525022)
Joe Clark is guilty: True or False?
True (0.8902942539348153)
Joe Clark is not guilty: True or False?
True (0.8316905440184192)
Joe Clark has mean: True or False?
True (0.9358173616900589)
Joe Clark has no mean: True or False?
True (0.8370879250561812)
Joe Clark has motive: True or False?
True (0.9405717864730483)
Joe Clark has no motive: True or False?
True (0.7570767382203575)
Joe Clark has opportunity: True or False?
True (0.8056321690561029)
Joe Clark has no opportunity: True or False?
True (0.6419836823036749)
Sherry Fogle is guilty: True or False?
True (0.8050197941712954)
Sherry Fogle is not guilty: True or False?
True (0.7240905157396584)
Sherry Fogle has mean: True or False?
True (0.8860265599597172)
Sherry Fogle has no mean: True or False?
True (0.7130321332210621)
Sherry Fogle has motive: True or False?
True (0.8479678036998373)
Sherry Fogle has no motive: True or False?
True (0.6039318499573872)
Sherry Fogle has opportunity: True or False?
False (0.5048826860345702)
Sherry Fogle has no opportunity: True or False?
True (0.5175708506128766)
Tonya Muse is guilty: True or False?
True (0.5822535180679596)
Tonya Muse is not guilty: True or False?
True (1.8181954195282923)
Tonya Muse has mean: True or False?
True (0.7872777601997338)
Tonya Muse has no mean: True or False?
False (0.5097643762740132)
Tonya Muse has motive: True or False?
True (0.7697732451157533)
Tonya Muse has no motive: True or False?
True (0.7025667346245409)
Tonya Muse has opportunity: True or False?
False (0.6671476389322356)
Tonya Muse has no opportunity: True or False?
True (1.1321932026986181)
Wayne Clark is guilty: True or False?
True (0.9329437018480795)
Wayne Clark is not guilty: True or False?
True (0.9038048413863352)
Wayne Clark has mean: True or False?
True (0.9489172681310486)
Wayne Clark has no mean: True or False?
True (0.8238958672039278)
Wayne Clark has motive: True or False?
True (0.9580694433457548)
Wayne Clark has no motive: True or False?
True (0.8529354946829077)
Wayne Clark has opportunity: True or False?
True (0.8665847814067802)
Wayne Clark has no opportunity: True or False?
True (0.6901415551283886)
### Bethany Knight
- mean: True (0.9193534273597669)
- motive: True (0.8910549899564296)
- opportunity: True (0.7217431689117048)

### Joe Clark
- mean: False (0.16291207494381876)
- motive: False (0.24292326177964252)
- opportunity: False (0.35801631769632514)

### Sherry Fogle
- mean: False (0.28696786677893793)
- motive: False (0.39606815004261275)
- opportunity: False (0.5048826860345702)

### Tonya Muse
- mean: False (0.0)
- motive: False (0.2974332653754591)
- opportunity: False (0.6671476389322356)

### Wayne Clark
- mean: False (0.17610413279607218)
- motive: False (0.14706450531709225)
- opportunity: False (0.3098584448716114)

The culprit is Bethany Knight.
In fact, it is Wayne Clark.
## 5minutemystery-a-porsche-of-course
Amy Golden is guilty: True or False?
True (0.5428632463719839)
Amy Golden is not guilty: True or False?
True (0.5068355091660127)
Amy Golden has mean: True or False?
False (0.5660185351323219)
Amy Golden has no mean: True or False?
False (0.8973360043541736)
Amy Golden has motive: True or False?
False (0.5068355091660127)
Amy Golden has no motive: True or False?
False (0.6370308391245257)
Amy Golden has opportunity: True or False?
False (0.8181563669811865)
Amy Golden has no opportunity: True or False?
False (0.8688267468984366)
Frankie Cole is guilty: True or False?
True (0.7697732451157533)
Frankie Cole is not guilty: True or False?
True (0.7461389980806673)
Frankie Cole has mean: True or False?
True (0.7505527730327083)
Frankie Cole has no mean: True or False?
False (0.5399537164111071)
Frankie Cole has motive: True or False?
True (0.7563575572780217)
Frankie Cole has no motive: True or False?
False (0.5477060024984176)
Frankie Cole has opportunity: True or False?
True (0.6654105788791005)
Frankie Cole has no opportunity: True or False?
False (0.6132366084149281)
Jeremy Steele is guilty: True or False?
True (0.5907791930117218)
Jeremy Steele is not guilty: True or False?
True (0.5350984235603058)
Jeremy Steele has mean: True or False?
True (0.5888891269161294)
Jeremy Steele has no mean: True or False?
False (0.7563575572780217)
Jeremy Steele has motive: True or False?
True (0.5746334908651781)
Jeremy Steele has no motive: True or False?
False (0.6901415551283886)
Jeremy Steele has opportunity: True or False?
False (0.5973730125048408)
Jeremy Steele has no opportunity: True or False?
False (0.8887587777822111)
Lionel Jacobs is guilty: True or False?
True (0.6926419789019715)
Lionel Jacobs is not guilty: True or False?
True (0.6095241816115718)
Lionel Jacobs has mean: True or False?
True (0.5136684743338078)
Lionel Jacobs has no mean: True or False?
False (0.8534247816107388)
Lionel Jacobs has motive: True or False?
False (0.5273165068094335)
Lionel Jacobs has no motive: True or False?
False (0.7585105966624085)
Lionel Jacobs has opportunity: True or False?
False (0.5477060024984176)
Lionel Jacobs has no opportunity: True or False?
False (0.8267118326419537)
Susan Barker is guilty: True or False?
True (0.6671476985798853)
Susan Barker is not guilty: True or False?
True (0.5983121871760707)
Susan Barker has mean: True or False?
False (0.5097643762740132)
Susan Barker has no mean: True or False?
False (0.6984323202883935)
Susan Barker has motive: True or False?
True (0.51464427676968)
Susan Barker has no motive: True or False?
False (0.5983121871760707)
Susan Barker has opportunity: True or False?
True (0.5698526542706361)
Susan Barker has no opportunity: True or False?
False (0.7325918054337844)
### Amy Golden
- mean: False (0.5660185351323219)
- motive: False (0.5068355091660127)
- opportunity: False (0.8181563669811865)

### Frankie Cole
- mean: True (0.7505527730327083)
- motive: True (0.7563575572780217)
- opportunity: True (0.6654105788791005)

### Jeremy Steele
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.5973730125048408)

### Lionel Jacobs
- mean: False (0.0)
- motive: False (0.5273165068094335)
- opportunity: False (0.5477060024984176)

### Susan Barker
- mean: False (0.5097643762740132)
- motive: False (0.0)
- opportunity: False (0.0)

The culprit is Frankie Cole.
In fact, it is Frankie Cole.
## 5minutemystery-the-mystery-of-the-missing-story
Alex Rebmevon is guilty: True or False?
True (0.9407897579933674)
Alex Rebmevon is not guilty: True or False?
True (0.9216402157401415)
Alex Rebmevon has mean: True or False?
True (0.8489722037469682)
Alex Rebmevon has no mean: True or False?
True (0.5515736950589613)
Alex Rebmevon has motive: True or False?
True (0.8951566249612815)
Alex Rebmevon has no motive: True or False?
True (0.8925625120974553)
Alex Rebmevon has opportunity: True or False?
True (0.6876299924560524)
Alex Rebmevon has no opportunity: True or False?
False (0.5107405249783342)
Amy is guilty: True or False?
True (0.7520125537161032)
Amy is not guilty: True or False?
True (0.769080279275001)
Amy has mean: True or False?
True (0.6224593484250324)
Amy has no mean: True or False?
False (0.5879430860094185)
Amy has motive: True or False?
True (0.7162185953247016)
Amy has no motive: True or False?
True (0.6566582893190611)
Map:  81%|████████  | 164/203 [1:44:21<25:13, 38.82s/ examples]Map:  81%|████████▏ | 165/203 [1:44:51<22:47, 35.98s/ examples]Map:  82%|████████▏ | 166/203 [1:45:25<21:49, 35.39s/ examples]Amy has opportunity: True or False?
True (0.6270381219830087)
Amy has no opportunity: True or False?
False (0.6697448487720212)
Lucy is guilty: True or False?
True (0.6842640693504702)
Lucy is not guilty: True or False?
True (0.7476159279883341)
Lucy has mean: True or False?
False (0.6693127155643409)
Lucy has no mean: True or False?
False (0.7708100054796322)
Lucy has motive: True or False?
True (0.6570984669319457)
Lucy has no motive: True or False?
True (0.5274521469155076)
Lucy has opportunity: True or False?
False (0.5131804871639641)
Lucy has no opportunity: True or False?
False (0.817865615286059)
Sarah is guilty: True or False?
True (0.6288633913849659)
Sarah is not guilty: True or False?
True (0.7130321332210621)
Sarah has mean: True or False?
False (0.5331543669186894)
Sarah has no mean: True or False?
False (0.5107405858633529)
Sarah has motive: True or False?
True (0.8565725156795254)
Sarah has no motive: True or False?
True (0.7648916137833577)
Sarah has opportunity: True or False?
True (0.6160122877297346)
Sarah has no opportunity: True or False?
False (0.7130321332210621)
### Alex Rebmevon
- mean: False (0.44842630494103874)
- motive: False (0.1074374879025447)
- opportunity: False (0.0)

### Amy
- mean: True (0.6224593484250324)
- motive: True (0.7162185953247016)
- opportunity: True (0.6270381219830087)

### Lucy
- mean: False (0.6693127155643409)
- motive: False (0.47254785308449243)
- opportunity: False (0.5131804871639641)

### Sarah
- mean: False (0.5331543669186894)
- motive: False (0.23510838621664232)
- opportunity: False (0.0)

The culprit is Amy.
In fact, it is Lucy.
## 5minutemystery-the-case-of-the-missing-friend
Billy Friend is guilty: True or False?
True (0.6020615685826383)
Billy Friend is not guilty: True or False?
True (0.7446563307563252)
Billy Friend has mean: True or False?
True (0.811078188867804)
Billy Friend has no mean: True or False?
True (0.6076631662366868)
Billy Friend has motive: True or False?
True (0.7752647497229632)
Billy Friend has no motive: True or False?
True (0.8098781635062345)
Billy Friend has opportunity: True or False?
True (0.5612147992901458)
Billy Friend has no opportunity: True or False?
True (0.5185461538431656)
Diana Scott is guilty: True or False?
True (0.5936092727363199)
Diana Scott is not guilty: True or False?
True (0.7839884808423031)
Diana Scott has mean: True or False?
True (0.7333563569098757)
Diana Scott has no mean: True or False?
True (0.5282900845448565)
Diana Scott has motive: True or False?
True (0.6397360437814448)
Diana Scott has no motive: True or False?
True (0.7759445334082792)
Diana Scott has opportunity: True or False?
True (0.5195213440667139)
Diana Scott has no opportunity: True or False?
False (0.5428632463719839)
Harrell Garner is guilty: True or False?
True (0.5879430860094185)
Harrell Garner is not guilty: True or False?
True (0.6791787167336184)
Harrell Garner has mean: True or False?
True (0.615087855649269)
Harrell Garner has no mean: True or False?
False (0.5486734660889085)
Harrell Garner has motive: True or False?
True (0.5879431210535583)
Harrell Garner has no motive: True or False?
True (0.6076631662366868)
Harrell Garner has opportunity: True or False?
True (0.503906199448032)
Harrell Garner has no opportunity: True or False?
False (0.7033457082786769)
Susan Allen is guilty: True or False?
False (0.646013666311734)
Susan Allen is not guilty: True or False?
True (0.5467381591701916)
Susan Allen has mean: True or False?
True (0.642432441257838)
Susan Allen has no mean: True or False?
False (0.5165954111147137)
Susan Allen has motive: True or False?
True (0.6477981763584071)
Susan Allen has no motive: True or False?
True (0.6206216296838327)
Susan Allen has opportunity: True or False?
False (0.6706082735718226)
Susan Allen has no opportunity: True or False?
False (0.7154240000492645)
### Billy Friend
- mean: False (0.3923368337633132)
- motive: False (0.19012183649376546)
- opportunity: False (0.4814538461568344)

### Diana Scott
- mean: False (0.4717099154551435)
- motive: False (0.22405546659172082)
- opportunity: False (0.0)

### Harrell Garner
- mean: True (0.615087855649269)
- motive: True (0.5879431210535583)
- opportunity: True (0.503906199448032)

### Susan Allen
- mean: False (0.0)
- motive: False (0.3793783703161673)
- opportunity: False (0.6706082735718226)

The culprit is Harrell Garner.
In fact, it is Diana Scott.
## 5minutemystery-sweat-it-out
Chris Henderson is guilty: True or False?
True (0.7905303264811482)
Chris Henderson is not guilty: True or False?
True (0.8062431235779619)
Chris Henderson has mean: True or False?
True (0.85729086409805)
Chris Henderson has no mean: True or False?
True (0.6731917300802632)
Chris Henderson has motive: True or False?
True (0.720171518230031)
Chris Henderson has no motive: True or False?
True (0.6187804294217345)
Chris Henderson has opportunity: True or False?
False (0.6187804294217345)
Chris Henderson has no opportunity: True or False?
False (0.7090191197769757)
Dave Perkins is guilty: True or False?
True (0.8864204283224634)
Dave Perkins is not guilty: True or False?
True (0.9029524930853913)
Dave Perkins has mean: True or False?
True (0.8438951328214825)
Dave Perkins has no mean: True or False?
True (0.6315942370470465)
Dave Perkins has motive: True or False?
True (0.8241790481509624)
Dave Perkins has no motive: True or False?
True (0.7552761500547527)
Dave Perkins has opportunity: True or False?
True (0.5945512478395265)
Dave Perkins has no opportunity: True or False?
False (0.6486889055472267)
Larry Douglas is guilty: True or False?
True (0.8526902830013373)
Larry Douglas is not guilty: True or False?
True (0.8504685773080045)
Larry Douglas has mean: True or False?
True (0.7386690954574974)
Larry Douglas has no mean: True or False?
True (0.5068355091660127)
Larry Douglas has motive: True or False?
True (0.6706082735718226)
Larry Douglas has no motive: True or False?
True (0.5477060024984176)
Larry Douglas has opportunity: True or False?
False (0.5399537164111071)
Larry Douglas has no opportunity: True or False?
False (0.6671476389322356)
Nathan Elliott is guilty: True or False?
True (0.8392075331266983)
Nathan Elliott is not guilty: True or False?
True (0.8272706865691472)
Nathan Elliott has mean: True or False?
True (0.8828325273478573)
Nathan Elliott has no mean: True or False?
True (0.5486734660889085)
Nathan Elliott has motive: True or False?
True (0.7409249009267298)
Nathan Elliott has no motive: True or False?
True (0.6370308391245257)
Nathan Elliott has opportunity: True or False?
True (0.5302364729224919)
Nathan Elliott has no opportunity: True or False?
False (0.7209580003592615)
### Chris Henderson
- mean: False (0.32680826991973677)
- motive: False (0.3812195705782655)
- opportunity: False (0.6187804294217345)

### Dave Perkins
- mean: True (0.8438951328214825)
- motive: True (0.8241790481509624)
- opportunity: True (0.5945512478395265)

### Larry Douglas
- mean: False (0.4931644908339873)
- motive: False (0.4522939975015824)
- opportunity: False (0.5399537164111071)

### Nathan Elliott
- mean: False (0.45132653391109145)
- motive: False (0.36296916087547426)
- opportunity: False (0.0)

The culprit is Dave Perkins.
In fact, it is Chris Henderson.
## 5minutemystery-mystery-of-the-missing-heart
Eric Winter is guilty: True or False?
True (0.8927496657814362)
Eric Winter is not guilty: True or False?
True (0.844921525814193)
Eric Winter has mean: True or False?
True (0.8674854614419002)
Eric Winter has no mean: True or False?
True (0.6610482284345209)
Eric Winter has motive: True or False?
True (0.8862236142219189)
Eric Winter has no motive: True or False?
False (0.5973730125048408)
Eric Winter has opportunity: True or False?
False (0.51464427676968)
Eric Winter has no opportunity: True or False?
False (0.6566582893190611)
Jenny Jackson is guilty: True or False?
True (0.7718435616326055)
Jenny Jackson is not guilty: True or False?
True (0.7098244343353132)
Jenny Jackson has mean: True or False?
True (0.821044090050916)
Jenny Jackson has no mean: True or False?
False (0.6141626144170799)
Jenny Jackson has motive: True or False?
True (0.8681575656976329)
Map:  82%|████████▏ | 167/203 [1:46:03<21:49, 36.37s/ examples]Map:  83%|████████▎ | 168/203 [1:46:41<21:21, 36.63s/ examples]Jenny Jackson has no motive: True or False?
True (0.5107405858633529)
Jenny Jackson has opportunity: True or False?
True (0.6288633913849659)
Jenny Jackson has no opportunity: True or False?
False (0.6749081498948247)
Jimmy Jackson is guilty: True or False?
True (0.875574405580689)
Jimmy Jackson is not guilty: True or False?
True (0.8022459173459678)
Jimmy Jackson has mean: True or False?
True (0.7826624547920057)
Jimmy Jackson has no mean: True or False?
False (0.5302364729224919)
Jimmy Jackson has motive: True or False?
True (0.8985886567144342)
Jimmy Jackson has no motive: True or False?
False (0.5755879969637064)
Jimmy Jackson has opportunity: True or False?
True (0.7498206607358464)
Jimmy Jackson has no opportunity: True or False?
False (0.5515737608116735)
Wendy LaRue is guilty: True or False?
True (0.8155265480299457)
Wendy LaRue is not guilty: True or False?
True (0.743912876509037)
Wendy LaRue has mean: True or False?
True (0.862930245043327)
Wendy LaRue has no mean: True or False?
False (0.5631377056275331)
Wendy LaRue has motive: True or False?
True (0.814643384779728)
Wendy LaRue has no motive: True or False?
True (0.5903069265873606)
Wendy LaRue has opportunity: True or False?
False (0.5009765603034438)
Wendy LaRue has no opportunity: True or False?
False (0.5736783792247284)
### Eric Winter
- mean: False (0.33895177156547907)
- motive: False (0.0)
- opportunity: False (0.51464427676968)

### Jenny Jackson
- mean: False (0.0)
- motive: False (0.4892594141366471)
- opportunity: False (0.0)

### Jimmy Jackson
- mean: True (0.7826624547920057)
- motive: True (0.8985886567144342)
- opportunity: True (0.7498206607358464)

### Wendy LaRue
- mean: False (0.0)
- motive: False (0.4096930734126394)
- opportunity: False (0.5009765603034438)

The culprit is Jimmy Jackson.
In fact, it is Eric Winter.
## 5minutemystery-stealing-second-base
Coach Joe Morgan is guilty: True or False?
True (0.8631610245991334)
Coach Joe Morgan is not guilty: True or False?
True (0.8757869551856522)
Coach Joe Morgan has mean: True or False?
True (0.7505527730327083)
Coach Joe Morgan has no mean: True or False?
False (0.6774740084332073)
Coach Joe Morgan has motive: True or False?
True (0.5321819753403337)
Coach Joe Morgan has no motive: True or False?
True (0.7318258918270596)
Coach Joe Morgan has opportunity: True or False?
True (0.5087881220234095)
Coach Joe Morgan has no opportunity: True or False?
False (0.615087818987177)
Mary Thornton is guilty: True or False?
True (0.8828325273478573)
Mary Thornton is not guilty: True or False?
True (0.878939158433705)
Mary Thornton has mean: True or False?
True (0.770464837675413)
Mary Thornton has no mean: True or False?
False (0.6379334932841956)
Mary Thornton has motive: True or False?
True (0.7937461674149602)
Mary Thornton has no motive: True or False?
False (0.5273165696704634)
Mary Thornton has opportunity: True or False?
True (0.6029970803636248)
Mary Thornton has no opportunity: True or False?
False (0.6288633913849659)
Randy Newsom is guilty: True or False?
True (0.9103861443438126)
Randy Newsom is not guilty: True or False?
True (0.8992099203330682)
Randy Newsom has mean: True or False?
True (0.9082930095862076)
Randy Newsom has no mean: True or False?
False (0.6001883860246252)
Randy Newsom has motive: True or False?
True (0.8261514850267767)
Randy Newsom has no motive: True or False?
True (0.5832033352502285)
Randy Newsom has opportunity: True or False?
False (0.514644215419305)
Randy Newsom has no opportunity: True or False?
False (0.7256486384635821)
Shorty Gilstrap is guilty: True or False?
True (0.9036349079321685)
Shorty Gilstrap is not guilty: True or False?
True (0.8850366506597954)
Shorty Gilstrap has mean: True or False?
True (0.893681109060862)
Shorty Gilstrap has no mean: True or False?
False (0.5195213440667139)
Shorty Gilstrap has motive: True or False?
True (0.8074606715677252)
Shorty Gilstrap has no motive: True or False?
True (0.6067314814064781)
Shorty Gilstrap has opportunity: True or False?
True (0.5650587803792624)
Shorty Gilstrap has no opportunity: True or False?
False (0.6169357925086439)
### Coach Joe Morgan
- mean: False (0.0)
- motive: False (0.2681741081729404)
- opportunity: False (0.0)

### Mary Thornton
- mean: True (0.770464837675413)
- motive: True (0.7937461674149602)
- opportunity: True (0.6029970803636248)

### Randy Newsom
- mean: False (0.0)
- motive: False (0.4167966647497715)
- opportunity: False (0.514644215419305)

### Shorty Gilstrap
- mean: False (0.0)
- motive: False (0.39326851859352185)
- opportunity: False (0.0)

The culprit is Mary Thornton.
In fact, it is Mary Thornton.
## 5minutemystery-murder-in-the-old-house
Bathroom is guilty: True or False?
True (0.8386797935187188)
Bathroom is not guilty: True or False?
True (1.2448884804419427)
Bathroom has mean: True or False?
True (0.6141625595066657)
Bathroom has no mean: True or False?
True (0.7299235824947253)
Bathroom has motive: True or False?
True (0.642432441257838)
Bathroom has no motive: True or False?
True (0.7431679939957333)
Bathroom has opportunity: True or False?
True (0.6085939964125278)
Bathroom has no opportunity: True or False?
True (0.5292633777076584)
Bedroom of daughter, Anita Jensen is guilty: True or False?
True (0.6834194581047349)
Bedroom of daughter, Anita Jensen is not guilty: True or False?
True (0.6187804294217345)
Bedroom of daughter, Anita Jensen has mean: True or False?
True (0.7146280500737092)
Bedroom of daughter, Anita Jensen has no mean: True or False?
True (0.6884683992569801)
Bedroom of daughter, Anita Jensen has motive: True or False?
True (0.6645402797838648)
Bedroom of daughter, Anita Jensen has no motive: True or False?
True (0.5851012033999957)
Bedroom of daughter, Anita Jensen has opportunity: True or False?
True (0.5973730125048408)
Bedroom of daughter, Anita Jensen has no opportunity: True or False?
True (0.5350984235603058)
Bedroom of oldest son, Harry Jensen is guilty: True or False?
False (0.5039061393777357)
Bedroom of oldest son, Harry Jensen is not guilty: True or False?
False (0.5992506595844092)
Bedroom of oldest son, Harry Jensen has mean: True or False?
True (0.6522414018725713)
Bedroom of oldest son, Harry Jensen has no mean: True or False?
True (0.5717666110200305)
Bedroom of oldest son, Harry Jensen has motive: True or False?
False (0.5525396581641524)
Bedroom of oldest son, Harry Jensen has no motive: True or False?
False (0.5650587803792624)
Bedroom of oldest son, Harry Jensen has opportunity: True or False?
False (0.5936092727363199)
Bedroom of oldest son, Harry Jensen has no opportunity: True or False?
False (0.627038178044588)
Bedroom of youngest son, Edward Jensen is guilty: True or False?
True (0.6169357925086439)
Bedroom of youngest son, Edward Jensen is not guilty: True or False?
False (0.5019531141001669)
Bedroom of youngest son, Edward Jensen has mean: True or False?
True (0.7697733139388475)
Bedroom of youngest son, Edward Jensen has no mean: True or False?
True (0.6918097672776748)
Bedroom of youngest son, Edward Jensen has motive: True or False?
True (0.570809902165233)
Bedroom of youngest son, Edward Jensen has no motive: True or False?
True (0.525368812147771)
Bedroom of youngest son, Edward Jensen has opportunity: True or False?
True (0.5650587803792624)
Bedroom of youngest son, Edward Jensen has no opportunity: True or False?
False (0.5078118910577802)
Master bedroom of Earl and Mildrid Jensen is guilty: True or False?
True (0.5727227727404994)
Master bedroom of Earl and Mildrid Jensen is not guilty: True or False?
False (0.5448014304301324)
Master bedroom of Earl and Mildrid Jensen has mean: True or False?
True (0.7725306828324007)
Master bedroom of Earl and Mildrid Jensen has no mean: True or False?
True (0.7041601500399041)
Master bedroom of Earl and Mildrid Jensen has motive: True or False?
True (0.6918097672776748)
Master bedroom of Earl and Mildrid Jensen has no motive: True or False?
True (0.6825737331070684)
Master bedroom of Earl and Mildrid Jensen has opportunity: True or False?
True (0.686790355176806)
Master bedroom of Earl and Mildrid Jensen has no opportunity: True or False?
True (0.6540113633452196)
### Bathroom
Map:  83%|████████▎ | 169/203 [1:47:21<21:24, 37.78s/ examples]Map:  84%|████████▎ | 170/203 [1:47:57<20:23, 37.08s/ examples]Map:  84%|████████▍ | 171/203 [1:48:30<19:06, 35.84s/ examples]- mean: False (0.27007641750527467)
- motive: False (0.2568320060042667)
- opportunity: False (0.4707366222923416)

### Bedroom of daughter, Anita Jensen
- mean: False (0.3115316007430199)
- motive: False (0.4148987966000043)
- opportunity: False (0.4649015764396942)

### Bedroom of oldest son, Harry Jensen
- mean: False (0.42823338897996954)
- motive: False (0.5525396581641524)
- opportunity: False (0.5936092727363199)

### Bedroom of youngest son, Edward Jensen
- mean: True (0.7697733139388475)
- motive: True (0.570809902165233)
- opportunity: True (0.5650587803792624)

### Master bedroom of Earl and Mildrid Jensen
- mean: False (0.29583984996009594)
- motive: False (0.31742626689293163)
- opportunity: False (0.3459886366547804)

The culprit is Bedroom of youngest son, Edward Jensen.
In fact, it is Bathroom.
## 5minutemystery-the-chess-mystery
Father is guilty: True or False?
True (0.9443823686645129)
Father is not guilty: True or False?
True (0.9471859326465281)
Father has mean: True or False?
True (0.7819973291046377)
Father has no mean: True or False?
True (0.6842640081724978)
Father has motive: True or False?
True (0.9076402191395381)
Father has no motive: True or False?
True (0.9026095892260383)
Father has opportunity: True or False?
True (0.6451199006197486)
Father has no opportunity: True or False?
True (0.6424325178417575)
Greg is guilty: True or False?
True (0.873646620599733)
Greg is not guilty: True or False?
True (0.9111797236708432)
Greg has mean: True or False?
True (0.7994422859301654)
Greg has no mean: True or False?
True (0.5214711377329961)
Greg has motive: True or False?
True (0.8998277786460391)
Greg has no motive: True or False?
True (0.8300437258865985)
Greg has opportunity: True or False?
True (0.7379143332111532)
Greg has no opportunity: True or False?
True (0.5126925663186335)
Tina is guilty: True or False?
True (0.7779752672746386)
Tina is not guilty: True or False?
True (0.8710367026584496)
Tina has mean: True or False?
True (0.7379142672364736)
Tina has no mean: True or False?
False (0.5506073202694327)
Tina has motive: True or False?
True (0.7512834059294674)
Tina has no motive: True or False?
True (0.7049732238008671)
Tina has opportunity: True or False?
True (0.6723316913929156)
Tina has no opportunity: True or False?
False (0.6680145240815963)
Uncle Larry is guilty: True or False?
True (0.9392480858026054)
Uncle Larry is not guilty: True or False?
True (0.9378969089655451)
Uncle Larry has mean: True or False?
True (0.794384956668203)
Uncle Larry has no mean: True or False?
True (0.6252093370817647)
Uncle Larry has motive: True or False?
True (0.847967740521315)
Uncle Larry has no motive: True or False?
True (0.8647679145346777)
Uncle Larry has opportunity: True or False?
True (0.6959583025067009)
Uncle Larry has no opportunity: True or False?
False (0.5078118305218892)
### Father
- mean: False (0.3157359918275022)
- motive: False (0.09739041077396171)
- opportunity: False (0.3575674821582425)

### Greg
- mean: False (0.47852886226700386)
- motive: False (0.16995627411340153)
- opportunity: False (0.48730743368136653)

### Tina
- mean: True (0.7379142672364736)
- motive: True (0.7512834059294674)
- opportunity: True (0.6723316913929156)

### Uncle Larry
- mean: False (0.37479066291823526)
- motive: False (0.13523208546532228)
- opportunity: False (0.0)

The culprit is Tina.
In fact, it is Greg.
## 5minutemystery-lost-stolen-and-found
John Beddington is guilty: True or False?
True (0.8125700297166154)
John Beddington is not guilty: True or False?
True (0.8031737798924701)
John Beddington has mean: True or False?
True (0.9456006304504523)
John Beddington has no mean: True or False?
True (0.8410438847419)
John Beddington has motive: True or False?
True (0.7490872087035162)
John Beddington has no motive: True or False?
True (0.7570766705324253)
John Beddington has opportunity: True or False?
True (0.8418256636710214)
John Beddington has no opportunity: True or False?
True (0.5185461538431656)
Louisa Perry is guilty: True or False?
True (0.6297746298200823)
Louisa Perry is not guilty: True or False?
True (0.7122321792841629)
Louisa Perry has mean: True or False?
True (0.8899121304559661)
Louisa Perry has no mean: True or False?
True (0.5631377056275331)
Louisa Perry has motive: True or False?
True (0.6575384693006662)
Louisa Perry has no motive: True or False?
True (0.5039061393777357)
Louisa Perry has opportunity: True or False?
True (0.6039318499573872)
Louisa Perry has no opportunity: True or False?
False (0.6893056096647525)
Mary Ingram is guilty: True or False?
True (0.5535053004623279)
Mary Ingram is not guilty: True or False?
True (0.5964331079469681)
Mary Ingram has mean: True or False?
True (0.8175745039697023)
Mary Ingram has no mean: True or False?
False (0.5195213440667139)
Mary Ingram has motive: True or False?
True (0.7416740115009234)
Mary Ingram has no motive: True or False?
False (0.580352018589158)
Mary Ingram has opportunity: True or False?
True (0.6029970803636248)
Mary Ingram has no opportunity: True or False?
False (0.6774739680526108)
Sarah Upton is guilty: True or False?
True (0.615087818987177)
Sarah Upton is not guilty: True or False?
True (0.6256668624218418)
Sarah Upton has mean: True or False?
True (0.8633916342942395)
Sarah Upton has no mean: True or False?
True (0.5350983597716067)
Sarah Upton has motive: True or False?
True (0.612309626324874)
Sarah Upton has no motive: True or False?
True (0.5467381591701916)
Sarah Upton has opportunity: True or False?
True (0.5794004215835179)
Sarah Upton has no opportunity: True or False?
False (0.6495786332146115)
### John Beddington
- mean: False (0.15895611525810005)
- motive: False (0.24292332946757467)
- opportunity: False (0.4814538461568344)

### Louisa Perry
- mean: False (0.43686229437246693)
- motive: False (0.49609386062226435)
- opportunity: False (0.0)

### Mary Ingram
- mean: True (0.8175745039697023)
- motive: True (0.7416740115009234)
- opportunity: True (0.6029970803636248)

### Sarah Upton
- mean: False (0.4649016402283933)
- motive: False (0.45326184082980836)
- opportunity: False (0.0)

The culprit is Mary Ingram.
In fact, it is Louisa Perry.
## 5minutemystery-the-chocolate-cupcake-caper
Geraldine is guilty: True or False?
False (0.6662796746479285)
Geraldine is not guilty: True or False?
True (0.5263427467960875)
Geraldine has mean: True or False?
True (0.7348812840309261)
Geraldine has no mean: True or False?
False (0.65489470935198)
Geraldine has motive: True or False?
True (0.7094219376364089)
Geraldine has no motive: True or False?
True (0.7065955344877805)
Geraldine has opportunity: True or False?
True (0.6020615685826383)
Geraldine has no opportunity: True or False?
False (0.5282900845448565)
Julianna is guilty: True or False?
True (0.6926419789019715)
Julianna is not guilty: True or False?
True (0.7065954713132195)
Julianna has mean: True or False?
True (0.9210740952879496)
Julianna has no mean: True or False?
True (0.6943026818003076)
Julianna has motive: True or False?
True (0.9492946258008691)
Julianna has no motive: True or False?
True (0.7846493136763113)
Julianna has opportunity: True or False?
True (0.7371581892031299)
Julianna has no opportunity: True or False?
True (0.7310585348819939)
Luis is guilty: True or False?
True (0.6141626144170799)
Luis is not guilty: True or False?
True (0.7356416476869558)
Luis has mean: True or False?
True (0.8080671968507699)
Luis has no mean: True or False?
True (0.5185461538431656)
Luis has motive: True or False?
True (0.8868131040663721)
Luis has no motive: True or False?
True (0.6680145240815963)
Luis has opportunity: True or False?
True (0.7905303264811482)
Luis has no opportunity: True or False?
False (0.5926665645259142)
Mr. Bento is guilty: True or False?
False (0.6095241271158658)
Mr. Bento is not guilty: True or False?
True (0.5009765603034438)
Mr. Bento has mean: True or False?
True (0.8227594449669557)
Mr. Bento has no mean: True or False?
False (0.5907791930117218)
Mr. Bento has motive: True or False?
True (0.8360197583769845)
Mr. Bento has no motive: True or False?
True (0.7386690294153369)
Mr. Bento has opportunity: True or False?
True (0.589834510337428)
Map:  85%|████████▍ | 172/203 [1:49:02<18:00, 34.84s/ examples]Map:  85%|████████▌ | 173/203 [1:49:39<17:42, 35.43s/ examples]Map:  86%|████████▌ | 174/203 [1:50:14<17:07, 35.44s/ examples]Mr. Bento has no opportunity: True or False?
False (0.6992543888266708)
### Geraldine
- mean: False (0.0)
- motive: False (0.29340446551221955)
- opportunity: False (0.0)

### Julianna
- mean: False (0.30569731819969237)
- motive: False (0.2153506863236887)
- opportunity: False (0.2689414651180061)

### Luis
- mean: False (0.4814538461568344)
- motive: False (0.33198547591840366)
- opportunity: False (0.0)

### Mr. Bento
- mean: True (0.8227594449669557)
- motive: True (0.8360197583769845)
- opportunity: True (0.589834510337428)

The culprit is Mr. Bento.
In fact, it is Geraldine.
## 5minutemystery-dead-mans-island
Grandpa is guilty: True or False?
True (0.8244619332958376)
Grandpa is not guilty: True or False?
True (0.726425644352388)
Grandpa has mean: True or False?
True (0.8397340156610265)
Grandpa has no mean: True or False?
False (0.6325027218909103)
Grandpa has motive: True or False?
True (0.9382373082603129)
Grandpa has no motive: True or False?
True (0.7424217332471881)
Grandpa has opportunity: True or False?
False (0.5009765005823875)
Grandpa has no opportunity: True or False?
False (0.6242935781683038)
Grandpa's grandfather is guilty: True or False?
True (0.6610481693322063)
Grandpa's grandfather is not guilty: True or False?
True (0.5102524605032837)
Grandpa's grandfather has mean: True or False?
True (0.7185943809170431)
Grandpa's grandfather has no mean: True or False?
False (0.8221891570741111)
Grandpa's grandfather has motive: True or False?
True (0.9509603391767795)
Grandpa's grandfather has no motive: True or False?
False (0.5341265295318852)
Grandpa's grandfather has opportunity: True or False?
False (0.6800292740030767)
Grandpa's grandfather has no opportunity: True or False?
False (0.7918210572836727)
Lisa is guilty: True or False?
False (0.5312093941731293)
Lisa is not guilty: True or False?
False (0.7627776320303776)
Lisa has mean: True or False?
False (0.6252093370817647)
Lisa has no mean: True or False?
False (0.8958875533219306)
Lisa has motive: True or False?
True (0.7174080061598618)
Lisa has no motive: True or False?
False (0.5592899914849522)
Lisa has opportunity: True or False?
False (0.5506073202694327)
Lisa has no opportunity: True or False?
False (0.7520125537161032)
Mike is guilty: True or False?
True (0.7416740115009234)
Mike is not guilty: True or False?
True (0.5964331434971528)
Mike has mean: True or False?
True (0.627038178044588)
Mike has no mean: True or False?
False (0.816406362162552)
Mike has motive: True or False?
True (0.8615382357584752)
Mike has no motive: True or False?
False (0.5112285687489156)
Mike has opportunity: True or False?
True (0.7468781552484828)
Mike has no opportunity: True or False?
True (0.5268296530347192)
### Grandpa
- mean: False (0.0)
- motive: False (0.2575782667528119)
- opportunity: False (0.5009765005823875)

### Grandpa's grandfather
- mean: True (0.7185943809170431)
- motive: True (0.9509603391767795)
- opportunity: True (0.2081789427163273)

### Lisa
- mean: False (0.6252093370817647)
- motive: False (0.0)
- opportunity: False (0.5506073202694327)

### Mike
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.4731703469652808)

The culprit is Grandpa's grandfather.
In fact, it is Lisa.
## 5minutemystery-who-stole-the-rock-of-ages
Denise Hurst is guilty: True or False?
True (0.7745833916423246)
Denise Hurst is not guilty: True or False?
True (0.8705973031072073)
Denise Hurst has mean: True or False?
True (0.8615382357584752)
Denise Hurst has no mean: True or False?
False (0.5350984235603058)
Denise Hurst has motive: True or False?
True (0.5602526707659626)
Denise Hurst has no motive: True or False?
True (0.6433292707767855)
Denise Hurst has opportunity: True or False?
False (0.5107405858633529)
Denise Hurst has no opportunity: True or False?
False (0.6315943123389512)
Jim Gaigon is guilty: True or False?
True (0.8272706865691472)
Jim Gaigon is not guilty: True or False?
True (0.8519528492100928)
Jim Gaigon has mean: True or False?
True (0.7287483223557857)
Jim Gaigon has no mean: True or False?
False (0.6160122877297346)
Jim Gaigon has motive: True or False?
True (0.6297745735138451)
Jim Gaigon has no motive: True or False?
True (0.6859494535376744)
Jim Gaigon has opportunity: True or False?
False (0.5253688747766175)
Jim Gaigon has no opportunity: True or False?
False (0.64779823427608)
Juan Carde is guilty: True or False?
True (0.858718632897247)
Juan Carde is not guilty: True or False?
True (0.9107043724734579)
Juan Carde has mean: True or False?
True (0.9178934131644976)
Juan Carde has no mean: True or False?
True (0.6740504382339836)
Juan Carde has motive: True or False?
True (0.779321849347754)
Juan Carde has no motive: True or False?
True (0.7008948290825966)
Juan Carde has opportunity: True or False?
True (0.7106282704218558)
Juan Carde has no opportunity: True or False?
False (0.5107405249783342)
Skye Smith is guilty: True or False?
True (0.6415346823638186)
Skye Smith is not guilty: True or False?
True (0.7931059536445917)
Skye Smith has mean: True or False?
True (0.6984323202883935)
Skye Smith has no mean: True or False?
False (0.5841525779336078)
Skye Smith has motive: True or False?
False (0.5097644370426659)
Skye Smith has no motive: True or False?
False (0.5983121871760707)
Skye Smith has opportunity: True or False?
False (0.6486889055472267)
Skye Smith has no opportunity: True or False?
False (0.7364006034245382)
### Denise Hurst
- mean: True (0.8615382357584752)
- motive: True (0.5602526707659626)
- opportunity: True (0.36840568766104875)

### Jim Gaigon
- mean: False (0.0)
- motive: False (0.31405054646232555)
- opportunity: False (0.5253688747766175)

### Juan Carde
- mean: False (0.3259495617660164)
- motive: False (0.2991051709174034)
- opportunity: False (0.0)

### Skye Smith
- mean: False (0.0)
- motive: False (0.5097644370426659)
- opportunity: False (0.6486889055472267)

The culprit is Denise Hurst.
In fact, it is Juan Carde.
## 5minutemystery-all-washed-up
Captain Kildare is guilty: True or False?
True (0.8423451152856819)
Captain Kildare is not guilty: True or False?
True (0.8591917766133458)
Captain Kildare has mean: True or False?
True (0.9359345468898206)
Captain Kildare has no mean: True or False?
True (0.8866168897831055)
Captain Kildare has motive: True or False?
True (0.9164093141890854)
Captain Kildare has no motive: True or False?
True (0.5515737608116735)
Captain Kildare has opportunity: True or False?
True (0.8560919228396967)
Captain Kildare has no opportunity: True or False?
True (0.6486889055472267)
Latrisha Lanigan is guilty: True or False?
True (0.7394224480813394)
Latrisha Lanigan is not guilty: True or False?
True (0.6926419789019715)
Latrisha Lanigan has mean: True or False?
True (0.7468781997658912)
Latrisha Lanigan has no mean: True or False?
True (0.6406358487498992)
Latrisha Lanigan has motive: True or False?
True (0.8710366507406179)
Latrisha Lanigan has no motive: True or False?
False (0.621540893468236)
Latrisha Lanigan has opportunity: True or False?
True (0.685107355950278)
Latrisha Lanigan has no opportunity: True or False?
True (0.5331543669186894)
Mark Colson is guilty: True or False?
True (0.7839884808423031)
Mark Colson is not guilty: True or False?
True (0.6909762697651828)
Mark Colson has mean: True or False?
True (0.7950222460539826)
Mark Colson has no mean: True or False?
True (0.5869964306477841)
Mark Colson has motive: True or False?
True (0.8086723099497763)
Mark Colson has no motive: True or False?
False (0.5765419579552815)
Mark Colson has opportunity: True or False?
True (0.615087855649269)
Mark Colson has no opportunity: True or False?
False (0.5794004215835179)
Marvin Fishback is guilty: True or False?
True (0.6315943123389512)
Marvin Fishback is not guilty: True or False?
True (0.5945513187155627)
Marvin Fishback has mean: True or False?
True (0.6104534962074417)
Marvin Fishback has no mean: True or False?
False (0.5573635130218721)
Marvin Fishback has motive: True or False?
True (0.6495786332146115)
Marvin Fishback has no motive: True or False?
False (0.6343168082332088)
Marvin Fishback has opportunity: True or False?
False (0.5736784476125245)
Map:  86%|████████▌ | 175/203 [1:50:49<16:26, 35.23s/ examples]Map:  87%|████████▋ | 176/203 [1:51:20<15:18, 34.03s/ examples]Map:  87%|████████▋ | 177/203 [1:51:54<14:43, 33.99s/ examples]Map:  88%|████████▊ | 178/203 [1:52:32<14:39, 35.18s/ examples]Marvin Fishback has no opportunity: True or False?
False (0.6783269591477166)
### Captain Kildare
- mean: False (0.11338311021689451)
- motive: False (0.44842623918832647)
- opportunity: False (0.3513110944527733)

### Latrisha Lanigan
- mean: False (0.3593641512501008)
- motive: False (0.0)
- opportunity: False (0.46684563308131055)

### Mark Colson
- mean: True (0.7950222460539826)
- motive: True (0.8086723099497763)
- opportunity: True (0.615087855649269)

### Marvin Fishback
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.5736784476125245)

The culprit is Mark Colson.
In fact, it is Mark Colson.
## 5minutemystery-the-hidden-messenger
Jean is guilty: True or False?
True (0.8444089912414552)
Jean is not guilty: True or False?
True (0.8446654650893471)
Jean has mean: True or False?
True (0.9063219998220023)
Jean has no mean: True or False?
True (0.6697448487720212)
Jean has motive: True or False?
True (0.9479621664653681)
Jean has no motive: True or False?
True (0.7468781552484828)
Jean has opportunity: True or False?
True (0.8740772565226612)
Jean has no opportunity: True or False?
True (0.7225270177274575)
Marie is guilty: True or False?
True (0.6001883860246252)
Marie is not guilty: True or False?
True (0.6160122877297346)
Marie has mean: True or False?
True (0.7599387683150569)
Marie has no mean: True or False?
False (0.5563995964631269)
Marie has motive: True or False?
True (0.7541915239138703)
Marie has no motive: True or False?
True (0.5165954111147137)
Marie has opportunity: True or False?
True (0.5727227727404994)
Marie has no opportunity: True or False?
False (0.648688963544537)
Molly is guilty: True or False?
True (0.6817267994905651)
Molly is not guilty: True or False?
True (0.7283620328527746)
Molly has mean: True or False?
True (0.7394224480813394)
Molly has no mean: True or False?
False (0.5655386901212957)
Molly has motive: True or False?
True (0.8267118326419537)
Molly has no motive: True or False?
True (0.6169357925086439)
Molly has opportunity: True or False?
True (0.8025555002781843)
Molly has no opportunity: True or False?
False (0.5214711377329961)
Smith is guilty: True or False?
True (0.7033457082786769)
Smith is not guilty: True or False?
True (0.6918097672776748)
Smith has mean: True or False?
True (0.7074046739492601)
Smith has no mean: True or False?
False (0.5841525779336078)
Smith has motive: True or False?
True (0.7885831565209055)
Smith has no motive: True or False?
True (0.5360700410935405)
Smith has opportunity: True or False?
True (0.7468781552484828)
Smith has no opportunity: True or False?
False (0.60859406896259)
### Jean
- mean: False (0.33025515122797877)
- motive: False (0.2531218447515172)
- opportunity: False (0.27747298227254247)

### Marie
- mean: False (0.0)
- motive: False (0.48340458888528626)
- opportunity: False (0.0)

### Molly
- mean: False (0.0)
- motive: False (0.38306420749135606)
- opportunity: False (0.0)

### Smith
- mean: True (0.7074046739492601)
- motive: True (0.7885831565209055)
- opportunity: True (0.7468781552484828)

The culprit is Smith.
In fact, it is Smith.
## 5minutemystery-the-disappearing-dollhouse
Julia is guilty: True or False?
True (0.7356416476869558)
Julia is not guilty: True or False?
True (0.7074047371961694)
Julia has mean: True or False?
True (0.7806625377756776)
Julia has no mean: True or False?
False (0.5765419579552815)
Julia has motive: True or False?
True (0.8238958672039278)
Julia has no motive: True or False?
True (0.6224593484250324)
Julia has opportunity: True or False?
True (0.7130321332210621)
Julia has no opportunity: True or False?
False (0.6901415551283886)
Kyle is guilty: True or False?
True (0.5879431210535583)
Kyle is not guilty: True or False?
True (0.6706083335288773)
Kyle has mean: True or False?
True (0.7662937064012869)
Kyle has no mean: True or False?
False (0.5573634465789677)
Kyle has motive: True or False?
True (0.6029971163050526)
Kyle has no motive: True or False?
True (0.49999999904767284)
Kyle has opportunity: True or False?
True (0.5583269696343842)
Kyle has no opportunity: True or False?
False (0.7648916137833577)
Lucius is guilty: True or False?
True (0.673191669892235)
Lucius is not guilty: True or False?
True (0.7130321332210621)
Lucius has mean: True or False?
True (0.642432441257838)
Lucius has no mean: True or False?
False (0.8727816933272936)
Lucius has motive: True or False?
True (0.642432441257838)
Lucius has no motive: True or False?
False (0.580352087772514)
Lucius has opportunity: True or False?
False (0.5418937216067536)
Lucius has no opportunity: True or False?
False (0.8433797899747144)
Reg is guilty: True or False?
True (0.6270381219830087)
Reg is not guilty: True or False?
True (0.6601723415572317)
Reg has mean: True or False?
True (0.5755879969637064)
Reg has no mean: True or False?
False (0.7819972591886313)
Reg has motive: True or False?
True (0.5832033352502285)
Reg has no motive: True or False?
False (0.5612147992901458)
Reg has opportunity: True or False?
False (0.5292633777076584)
Reg has no opportunity: True or False?
False (0.789233749534095)
### Julia
- mean: True (0.7806625377756776)
- motive: True (0.8238958672039278)
- opportunity: True (0.7130321332210621)

### Kyle
- mean: False (0.0)
- motive: False (0.5000000009523271)
- opportunity: False (0.0)

### Lucius
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.5418937216067536)

### Reg
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.5292633777076584)

The culprit is Julia.
In fact, it is Reg.
## 5minutemystery-a-bear-a-dog-and-a-mystery
Mom is guilty: True or False?
False (0.5765419579552815)
Mom is not guilty: True or False?
True (0.5263427467960875)
Mom has mean: True or False?
False (0.615087818987177)
Mom has no mean: True or False?
False (0.8244619332958376)
Mom has motive: True or False?
False (0.6766198919456847)
Mom has no motive: True or False?
False (0.7879311977554747)
Mom has opportunity: True or False?
False (0.8474634858439474)
Mom has no opportunity: True or False?
False (0.941654147692963)
Old Mugger is guilty: True or False?
False (0.7468781552484828)
Old Mugger is not guilty: True or False?
False (0.7859664553110391)
Old Mugger has mean: True or False?
True (0.6067314814064781)
Old Mugger has no mean: True or False?
False (0.7711548682745724)
Old Mugger has motive: True or False?
False (0.5282900215677746)
Old Mugger has no motive: True or False?
False (0.7556369876990674)
Old Mugger has opportunity: True or False?
False (0.8050197941712954)
Old Mugger has no opportunity: True or False?
False (0.883638205304735)
Orville is guilty: True or False?
True (0.595492552580428)
Orville is not guilty: True or False?
True (0.51464427676968)
Orville has mean: True or False?
True (0.5983121871760707)
Orville has no mean: True or False?
False (0.7225270177274575)
Orville has motive: True or False?
True (0.7563575572780217)
Orville has no motive: True or False?
False (0.7752646804088963)
Orville has opportunity: True or False?
False (0.5964331434971528)
Orville has no opportunity: True or False?
False (0.8349459127213729)
Taylor is guilty: True or False?
True (0.5631377056275331)
Taylor is not guilty: True or False?
True (0.5175709123121337)
Taylor has mean: True or False?
True (0.5438325284393795)
Taylor has no mean: True or False?
False (0.8122723669190336)
Taylor has motive: True or False?
True (0.6749080895533367)
Taylor has no motive: True or False?
False (0.811078188867804)
Taylor has opportunity: True or False?
True (0.5234203246639862)
Taylor has no opportunity: True or False?
False (0.8469578650997759)
### Mom
- mean: False (0.615087818987177)
- motive: False (0.6766198919456847)
- opportunity: False (0.8474634858439474)

### Old Mugger
- mean: False (0.0)
- motive: False (0.5282900215677746)
- opportunity: False (0.8050197941712954)

### Orville
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.5964331434971528)

### Taylor
- mean: True (0.5438325284393795)
- motive: True (0.6749080895533367)
- opportunity: True (0.5234203246639862)

The culprit is Taylor.
In fact, it is Taylor.
## 5minutemystery-the-mystery-of-the-talented-cat
Edith is guilty: True or False?
Map:  88%|████████▊ | 179/203 [1:53:10<14:24, 36.03s/ examples]Map:  89%|████████▊ | 180/203 [1:53:52<14:29, 37.80s/ examples]True (0.7739005566220397)
Edith is not guilty: True or False?
True (0.8701565303520181)
Edith has mean: True or False?
True (0.7648916137833577)
Edith has no mean: True or False?
False (0.5292633777076584)
Edith has motive: True or False?
True (0.7645401872124011)
Edith has no motive: True or False?
True (0.6302298800836272)
Edith has opportunity: True or False?
True (0.6192410564568527)
Edith has no opportunity: True or False?
False (0.6706082136147734)
Joshua Sellers is guilty: True or False?
True (0.8778961263000082)
Joshua Sellers is not guilty: True or False?
True (0.8322366416985943)
Joshua Sellers has mean: True or False?
True (0.8969755785184792)
Joshua Sellers has no mean: True or False?
True (0.6540113633452196)
Joshua Sellers has motive: True or False?
True (0.8077641180140109)
Joshua Sellers has no motive: True or False?
True (0.7074046739492601)
Joshua Sellers has opportunity: True or False?
True (0.6406358487498992)
Joshua Sellers has no opportunity: True or False?
True (0.5822535180679596)
Muggles is guilty: True or False?
True (0.8494724067948436)
Muggles is not guilty: True or False?
True (0.8762112821835625)
Muggles has mean: True or False?
True (0.8494724067948436)
Muggles has no mean: True or False?
True (0.7549149897594328)
Muggles has motive: True or False?
True (0.8316905440184192)
Muggles has no motive: True or False?
True (0.7911764307711107)
Muggles has opportunity: True or False?
True (0.7310585348819939)
Muggles has no opportunity: True or False?
True (0.5563995964631269)
Rick is guilty: True or False?
True (0.6584174547581384)
Rick is not guilty: True or False?
True (0.6714705702070799)
Rick has mean: True or False?
True (0.7074047371961694)
Rick has no mean: True or False?
False (0.6252093370817647)
Rick has motive: True or False?
True (0.5282900215677746)
Rick has no motive: True or False?
False (0.5467381591701916)
Rick has opportunity: True or False?
False (0.6206216296838327)
Rick has no opportunity: True or False?
False (0.8534247816107388)
### Edith
- mean: True (0.7648916137833577)
- motive: True (0.7645401872124011)
- opportunity: True (0.6192410564568527)

### Joshua Sellers
- mean: False (0.3459886366547804)
- motive: False (0.2925953260507399)
- opportunity: False (0.41774648193204045)

### Muggles
- mean: False (0.24508501024056717)
- motive: False (0.20882356922888934)
- opportunity: False (0.44360040353687313)

### Rick
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.6206216296838327)

The culprit is Edith.
In fact, it is Edith.
## 5minutemystery-the-haunted-portrait
Jonathan Ingersoll is guilty: True or False?
True (0.8509646659219744)
Jonathan Ingersoll is not guilty: True or False?
True (0.7739006258141444)
Jonathan Ingersoll has mean: True or False?
True (0.8980534699860239)
Jonathan Ingersoll has no mean: True or False?
True (0.8311430212356835)
Jonathan Ingersoll has motive: True or False?
True (0.8294919722593475)
Jonathan Ingersoll has no motive: True or False?
True (0.7704647687904915)
Jonathan Ingersoll has opportunity: True or False?
True (0.7826624547920057)
Jonathan Ingersoll has no opportunity: True or False?
True (0.6451199006197486)
Lucille Cameron is guilty: True or False?
True (0.8344069148356309)
Lucille Cameron is not guilty: True or False?
True (0.8006920257960423)
Lucille Cameron has mean: True or False?
True (0.9362850185952675)
Lucille Cameron has no mean: True or False?
True (0.9121235591541035)
Lucille Cameron has motive: True or False?
True (0.8795611817678315)
Lucille Cameron has no motive: True or False?
True (0.7806624796117883)
Lucille Cameron has opportunity: True or False?
True (0.8643104392003704)
Lucille Cameron has no opportunity: True or False?
True (0.6926419789019715)
Marion Montgomery is guilty: True or False?
True (0.8216173055802608)
Marion Montgomery is not guilty: True or False?
True (0.7490872087035162)
Marion Montgomery has mean: True or False?
True (0.8261514850267767)
Marion Montgomery has no mean: True or False?
True (0.7570766705324253)
Marion Montgomery has motive: True or False?
True (0.8204694405411458)
Marion Montgomery has no motive: True or False?
True (0.7520125537161032)
Marion Montgomery has opportunity: True or False?
True (0.7988152492192591)
Marion Montgomery has no opportunity: True or False?
True (0.6132365353114321)
Teddy Auchinlech is guilty: True or False?
True (0.7461389980806673)
Teddy Auchinlech is not guilty: True or False?
True (0.6926419789019715)
Teddy Auchinlech has mean: True or False?
True (0.8587185689177256)
Teddy Auchinlech has no mean: True or False?
True (0.8300437877296776)
Teddy Auchinlech has motive: True or False?
True (0.8122723669190336)
Teddy Auchinlech has no motive: True or False?
True (0.7178037814283548)
Teddy Auchinlech has opportunity: True or False?
True (0.7732163648437078)
Teddy Auchinlech has no opportunity: True or False?
True (0.6495786332146115)
### Jonathan Ingersoll
- mean: False (0.1688569787643165)
- motive: False (0.22953523120950847)
- opportunity: False (0.35488009938025145)

### Lucille Cameron
- mean: False (0.08787644084589652)
- motive: False (0.21933752038821175)
- opportunity: False (0.30735802109802846)

### Marion Montgomery
- mean: False (0.24292332946757467)
- motive: False (0.2479874462838968)
- opportunity: False (0.3867634646885679)

### Teddy Auchinlech
- mean: True (0.8587185689177256)
- motive: True (0.8122723669190336)
- opportunity: True (0.7732163648437078)

The culprit is Teddy Auchinlech.
In fact, it is Jonathan Ingersoll.
## 5minutemystery-the-classic-automobile-mystery
Gary Riggs is guilty: True or False?
True (0.8068525816617738)
Gary Riggs is not guilty: True or False?
True (0.6834195192071987)
Gary Riggs has mean: True or False?
True (0.6261242000979097)
Gary Riggs has no mean: True or False?
False (0.874934615163517)
Gary Riggs has motive: True or False?
True (0.5679366075542497)
Gary Riggs has no motive: True or False?
True (0.5573635130218721)
Gary Riggs has opportunity: True or False?
False (0.7431679939957333)
Gary Riggs has no opportunity: True or False?
False (0.7505527730327083)
Gerald "Doc" McCroy is guilty: True or False?
True (0.5755879969637064)
Gerald "Doc" McCroy is not guilty: True or False?
True (0.5126925663186335)
Gerald "Doc" McCroy has mean: True or False?
False (0.5708098341193941)
Gerald "Doc" McCroy has no mean: True or False?
False (0.878314250659373)
Gerald "Doc" McCroy has motive: True or False?
True (0.5679366075542497)
Gerald "Doc" McCroy has no motive: True or False?
False (0.5058591351869154)
Gerald "Doc" McCroy has opportunity: True or False?
False (0.7975568155246964)
Gerald "Doc" McCroy has no opportunity: True or False?
False (0.7341195403199204)
Mike Benson is guilty: True or False?
True (0.6160122877297346)
Mike Benson is not guilty: True or False?
True (0.5467381591701916)
Mike Benson has mean: True or False?
True (0.6104534962074417)
Mike Benson has no mean: True or False?
False (0.8705973031072073)
Mike Benson has motive: True or False?
False (0.5165954111147137)
Mike Benson has no motive: True or False?
True (0.5879430860094185)
Mike Benson has opportunity: True or False?
False (0.8444089912414552)
Mike Benson has no opportunity: True or False?
False (0.8244619332958376)
Tommy Flowers is guilty: True or False?
True (0.5851011336505011)
Tommy Flowers is not guilty: True or False?
False (0.5660185351323219)
Tommy Flowers has mean: True or False?
True (0.7178037814283548)
Tommy Flowers has no mean: True or False?
False (0.8925625719484378)
Tommy Flowers has motive: True or False?
True (0.6279512069990912)
Tommy Flowers has no motive: True or False?
False (0.6242935037467142)
Tommy Flowers has opportunity: True or False?
False (0.7431679939957333)
Tommy Flowers has no opportunity: True or False?
False (0.6808786440630326)
### Gary Riggs
- mean: False (0.0)
- motive: False (0.44263648697812785)
- opportunity: False (0.7431679939957333)

### Gerald "Doc" McCroy
- mean: False (0.5708098341193941)
- motive: False (0.0)
- opportunity: False (0.7975568155246964)

### Mike Benson
- mean: False (0.0)
- motive: False (0.5165954111147137)
- opportunity: False (0.8444089912414552)

### Tommy Flowers
Map:  89%|████████▉ | 181/203 [1:54:22<13:01, 35.53s/ examples]Map:  90%|████████▉ | 182/203 [1:55:05<13:13, 37.76s/ examples]Map:  90%|█████████ | 183/203 [1:55:51<13:22, 40.14s/ examples]- mean: True (0.7178037814283548)
- motive: True (0.6279512069990912)
- opportunity: True (0.31912135593696744)

The culprit is Tommy Flowers.
In fact, it is Gerald "Doc" McCroy.
## 5minutemystery-rocks-and-feathers
Barley is guilty: True or False?
True (0.8464508054137014)
Barley is not guilty: True or False?
True (0.8577681165234065)
Barley has mean: True or False?
True (0.9073122118500465)
Barley has no mean: True or False?
True (0.7416740115009234)
Barley has motive: True or False?
True (0.8362873170845201)
Barley has no motive: True or False?
True (0.7318258918270596)
Barley has opportunity: True or False?
True (0.8233283740192667)
Barley has no opportunity: True or False?
True (0.6215409675616889)
Bertha is guilty: True or False?
True (0.9116528030198908)
Bertha is not guilty: True or False?
True (0.9138304573134544)
Bertha has mean: True or False?
True (0.8534247816107388)
Bertha has no mean: True or False?
True (0.8407826471261478)
Bertha has motive: True or False?
True (0.9223425402045055)
Bertha has no motive: True or False?
True (0.7846493136763113)
Bertha has opportunity: True or False?
True (0.862930245043327)
Bertha has no opportunity: True or False?
True (0.7641883982873323)
Joseph is guilty: True or False?
True (0.8596637847360897)
Joseph is not guilty: True or False?
True (0.8283841584202847)
Joseph has mean: True or False?
True (0.8652240590801695)
Joseph has no mean: True or False?
True (0.6361271113853048)
Joseph has motive: True or False?
True (0.8727816933272936)
Joseph has no motive: True or False?
True (0.6783269591477166)
Joseph has opportunity: True or False?
True (0.7981867775042927)
Joseph has no opportunity: True or False?
True (0.6817267588564826)
Tom is guilty: True or False?
True (0.8322366416985943)
Tom is not guilty: True or False?
True (0.8370879250561812)
Tom has mean: True or False?
True (0.8647679145346777)
Tom has no mean: True or False?
True (0.6909762697651828)
Tom has motive: True or False?
True (0.8652240590801695)
Tom has no motive: True or False?
True (0.6714705702070799)
Tom has opportunity: True or False?
True (0.8068525816617738)
Tom has no opportunity: True or False?
True (0.7498207054286419)
### Barley
- mean: False (0.2583259884990766)
- motive: False (0.2681741081729404)
- opportunity: False (0.37845903243831114)

### Bertha
- mean: True (0.8534247816107388)
- motive: True (0.9223425402045055)
- opportunity: True (0.862930245043327)

### Joseph
- mean: False (0.36387288861469524)
- motive: False (0.32167304085228343)
- opportunity: False (0.3182732411435174)

### Tom
- mean: False (0.3090237302348172)
- motive: False (0.3285294297929201)
- opportunity: False (0.2501792945713581)

The culprit is Bertha.
In fact, it is Tom.
## 5minutemystery-who-is-telling-the-truth
Bill Flowers is guilty: True or False?
True (0.8998277786460391)
Bill Flowers is not guilty: True or False?
True (0.9460011721384068)
Bill Flowers has mean: True or False?
True (0.9730365275631271)
Bill Flowers has no mean: True or False?
True (0.9076402191395381)
Bill Flowers has motive: True or False?
True (0.8860265599597172)
Bill Flowers has no motive: True or False?
True (0.8966140148346177)
Bill Flowers has opportunity: True or False?
True (0.854884620116169)
Bill Flowers has no opportunity: True or False?
True (0.8484706263347676)
Jane Neal is guilty: True or False?
True (0.8883720049821552)
Jane Neal is not guilty: True or False?
True (0.941654147692963)
Jane Neal has mean: True or False?
True (0.9606574760904091)
Jane Neal has no mean: True or False?
True (0.8980535302052036)
Jane Neal has motive: True or False?
True (0.8727817583545995)
Jane Neal has no motive: True or False?
True (0.8998277786460391)
Jane Neal has opportunity: True or False?
True (0.844921525814193)
Jane Neal has no opportunity: True or False?
True (0.832781373043151)
Jimmy Smith is guilty: True or False?
True (0.955152093302995)
Jimmy Smith is not guilty: True or False?
True (0.9667888295116236)
Jimmy Smith has mean: True or False?
True (0.9661560069290531)
Jimmy Smith has no mean: True or False?
True (0.9022657265573043)
Jimmy Smith has motive: True or False?
True (0.8955226517597132)
Jimmy Smith has no motive: True or False?
True (0.9102267057681164)
Jimmy Smith has opportunity: True or False?
True (0.9139841191734227)
Jimmy Smith has no opportunity: True or False?
True (0.8848377441095496)
Larry Gerard is guilty: True or False?
True (0.9273633336539081)
Larry Gerard is not guilty: True or False?
True (0.9615337835163564)
Larry Gerard has mean: True or False?
True (0.9532750830575984)
Larry Gerard has no mean: True or False?
True (0.878314250659373)
Larry Gerard has motive: True or False?
True (0.8423451152856819)
Larry Gerard has no motive: True or False?
True (0.8799743689174987)
Larry Gerard has opportunity: True or False?
True (0.8392075831473667)
Larry Gerard has no opportunity: True or False?
True (0.8311430212356835)
Paula Newsome is guilty: True or False?
True (0.9260365949489886)
Paula Newsome is not guilty: True or False?
True (0.9491062747098069)
Paula Newsome has mean: True or False?
True (0.971563935671788)
Paula Newsome has no mean: True or False?
True (0.8140527631337082)
Paula Newsome has motive: True or False?
True (0.8489722037469682)
Paula Newsome has no motive: True or False?
True (0.8955227118091885)
Paula Newsome has opportunity: True or False?
True (0.8807970337584357)
Paula Newsome has no opportunity: True or False?
True (0.8820220178442959)
### Bill Flowers
- mean: False (0.09235978086046193)
- motive: False (0.10338598516538233)
- opportunity: False (0.15152937366523245)

### Jane Neal
- mean: False (0.10194646979479638)
- motive: False (0.10017222135396087)
- opportunity: False (0.16721862695684897)

### Jimmy Smith
- mean: False (0.0977342734426957)
- motive: False (0.08977329423188363)
- opportunity: False (0.11516225589045037)

### Larry Gerard
- mean: True (0.9532750830575984)
- motive: True (0.8423451152856819)
- opportunity: True (0.8392075831473667)

### Paula Newsome
- mean: False (0.18594723686629178)
- motive: False (0.10447728819081148)
- opportunity: False (0.1179779821557041)

The culprit is Larry Gerard.
In fact, it is Paula Newsome.
## 5minutemystery-ask-marthathe-identity-thief
Grace Means is guilty: True or False?
True (0.874934615163517)
Grace Means is not guilty: True or False?
True (0.7889086034411039)
Grace Means has mean: True or False?
True (0.9324533354081785)
Grace Means has no mean: True or False?
True (0.862930245043327)
Grace Means has motive: True or False?
True (0.9149009617112335)
Grace Means has no motive: True or False?
True (0.8050197941712954)
Grace Means has opportunity: True or False?
True (0.8056321690561029)
Grace Means has no opportunity: True or False?
True (0.700075275973927)
Joan Colthrop is guilty: True or False?
True (0.8910549302065384)
Joan Colthrop is not guilty: True or False?
True (0.77729988964086)
Joan Colthrop has mean: True or False?
True (0.9447913165152162)
Joan Colthrop has no mean: True or False?
True (0.8289388437432279)
Joan Colthrop has motive: True or False?
True (0.8770561879413864)
Joan Colthrop has no motive: True or False?
True (0.6001883144765984)
Joan Colthrop has opportunity: True or False?
True (0.6697448487720212)
Joan Colthrop has no opportunity: True or False?
False (0.5573635130218721)
Laura Parsons is guilty: True or False?
True (0.9181872635464632)
Laura Parsons is not guilty: True or False?
True (0.8916224825491823)
Laura Parsons has mean: True or False?
True (0.9284088027271398)
Laura Parsons has no mean: True or False?
True (0.8514593818157263)
Laura Parsons has motive: True or False?
True (0.8068526417769779)
Laura Parsons has no motive: True or False?
True (0.6575384105121485)
Laura Parsons has opportunity: True or False?
True (0.686790293772966)
Laura Parsons has no opportunity: True or False?
True (0.6859494535376744)
Maybelle Johnson is guilty: True or False?
True (0.8397339530959691)
Maybelle Johnson is not guilty: True or False?
True (0.7806624796117883)
Maybelle Johnson has mean: True or False?
True (0.8514594452543962)
Maybelle Johnson has no mean: True or False?
True (0.6808786440630326)
Maybelle Johnson has motive: True or False?
Map:  91%|█████████ | 184/203 [1:56:26<12:12, 38.56s/ examples]Map:  91%|█████████ | 185/203 [1:57:05<11:36, 38.68s/ examples]Map:  92%|█████████▏| 186/203 [1:57:33<10:03, 35.48s/ examples]True (0.8633915828320894)
Maybelle Johnson has no motive: True or False?
False (0.5273165068094335)
Maybelle Johnson has opportunity: True or False?
True (0.6067314814064781)
Maybelle Johnson has no opportunity: True or False?
True (0.5175709123121337)
### Grace Means
- mean: False (0.13706975495667295)
- motive: False (0.19498020582870457)
- opportunity: False (0.29992472402607295)

### Joan Colthrop
- mean: False (0.1710611562567721)
- motive: False (0.3998116855234016)
- opportunity: False (0.0)

### Laura Parsons
- mean: False (0.14854061818427367)
- motive: False (0.34246158948785155)
- opportunity: False (0.31405054646232555)

### Maybelle Johnson
- mean: True (0.8514594452543962)
- motive: True (0.8633915828320894)
- opportunity: True (0.6067314814064781)

The culprit is Maybelle Johnson.
In fact, it is Joan Colthrop.
## 5minutemystery-ask-marthathe-pickpocket
Johnny Anderson is guilty: True or False?
True (0.7994422859301654)
Johnny Anderson is not guilty: True or False?
True (0.7468781552484828)
Johnny Anderson has mean: True or False?
True (0.8092759828926619)
Johnny Anderson has no mean: True or False?
True (0.6893056096647525)
Johnny Anderson has motive: True or False?
True (0.8013146490010521)
Johnny Anderson has no motive: True or False?
False (0.5350984235603058)
Johnny Anderson has opportunity: True or False?
True (0.7534666630720156)
Johnny Anderson has no opportunity: True or False?
True (0.6011253583932805)
Morris Emerson is guilty: True or False?
True (0.8402589628813668)
Morris Emerson is not guilty: True or False?
True (0.8433797899747144)
Morris Emerson has mean: True or False?
True (0.7669925046333297)
Morris Emerson has no mean: True or False?
True (0.7520125537161032)
Morris Emerson has motive: True or False?
True (0.7905303264811482)
Morris Emerson has no motive: True or False?
True (0.5428632463719839)
Morris Emerson has opportunity: True or False?
True (0.6884683992569801)
Morris Emerson has no opportunity: True or False?
False (0.6504672743423094)
Sarah Browne is guilty: True or False?
True (0.7799929399351836)
Sarah Browne is not guilty: True or False?
True (0.7424217332471881)
Sarah Browne has mean: True or False?
True (0.8652240590801695)
Sarah Browne has no mean: True or False?
True (0.7371581232960549)
Sarah Browne has motive: True or False?
True (0.726425644352388)
Sarah Browne has no motive: True or False?
False (0.6297746298200823)
Sarah Browne has opportunity: True or False?
True (0.6306849143569856)
Sarah Browne has no opportunity: True or False?
False (0.6406358487498992)
Tom Blankenship is guilty: True or False?
True (0.7981867775042927)
Tom Blankenship is not guilty: True or False?
True (0.7898827724330132)
Tom Blankenship has mean: True or False?
True (0.8092759828926619)
Tom Blankenship has no mean: True or False?
True (0.6361271113853048)
Tom Blankenship has motive: True or False?
True (0.811078188867804)
Tom Blankenship has no motive: True or False?
True (0.49999999904767284)
Tom Blankenship has opportunity: True or False?
True (0.6697448487720212)
Tom Blankenship has no opportunity: True or False?
True (0.5048826258478675)
### Johnny Anderson
- mean: False (0.3106943903352475)
- motive: False (0.0)
- opportunity: False (0.3988746416067195)

### Morris Emerson
- mean: False (0.2479874462838968)
- motive: False (0.4571367536280161)
- opportunity: False (0.0)

### Sarah Browne
- mean: True (0.8652240590801695)
- motive: True (0.726425644352388)
- opportunity: True (0.6306849143569856)

### Tom Blankenship
- mean: False (0.36387288861469524)
- motive: False (0.5000000009523271)
- opportunity: False (0.49511737415213253)

The culprit is Sarah Browne.
In fact, it is Tom Blankenship.
## 5minutemystery-diamond-deception
Horace is guilty: True or False?
True (0.6680145240815963)
Horace is not guilty: True or False?
True (0.6261242000979097)
Horace has mean: True or False?
True (0.8524448242555318)
Horace has no mean: True or False?
True (0.5573635130218721)
Horace has motive: True or False?
True (0.6984323202883935)
Horace has no motive: True or False?
True (0.7527403228571042)
Horace has opportunity: True or False?
True (0.708212608228071)
Horace has no opportunity: True or False?
False (0.5428632463719839)
Jake is guilty: True or False?
True (0.5679366075542497)
Jake is not guilty: True or False?
False (0.5312093941731293)
Jake has mean: True or False?
True (0.8056321690561029)
Jake has no mean: True or False?
True (0.5224458497983033)
Jake has motive: True or False?
True (0.7348812183274223)
Jake has no motive: True or False?
True (0.6783269591477166)
Jake has opportunity: True or False?
True (0.7394224480813394)
Jake has no opportunity: True or False?
False (0.5784481782924303)
John is guilty: True or False?
True (0.6566582306092376)
John is not guilty: True or False?
True (0.6714705702070799)
John has mean: True or False?
True (0.8820219652716884)
John has no mean: True or False?
True (0.580352018589158)
John has motive: True or False?
True (0.8444089912414552)
John has no motive: True or False?
True (0.7138307093362539)
John has opportunity: True or False?
True (0.8092759828926619)
John has no opportunity: True or False?
True (0.5688948754232768)
Lewis is guilty: True or False?
True (0.6740504984987916)
Lewis is not guilty: True or False?
True (0.5983121871760707)
Lewis has mean: True or False?
True (0.8860265599597172)
Lewis has no mean: True or False?
True (0.5860490988363701)
Lewis has motive: True or False?
True (0.7453983509653428)
Lewis has no motive: True or False?
True (0.7648916137833577)
Lewis has opportunity: True or False?
True (0.7409249009267298)
Lewis has no opportunity: True or False?
True (0.5563995964631269)
### Horace
- mean: False (0.44263648697812785)
- motive: False (0.24725967714289576)
- opportunity: False (0.0)

### Jake
- mean: True (0.8056321690561029)
- motive: True (0.7348812183274223)
- opportunity: True (0.7394224480813394)

### John
- mean: False (0.41964798141084203)
- motive: False (0.2861692906637461)
- opportunity: False (0.43110512457672323)

### Lewis
- mean: False (0.41395090116362987)
- motive: False (0.23510838621664232)
- opportunity: False (0.44360040353687313)

The culprit is Jake.
In fact, it is Lewis.
## 5minutemystery-where-is-matthew
Andy's bedroom is guilty: True or False?
True (0.5592900581575188)
Andy's bedroom is not guilty: True or False?
False (0.5195213440667139)
Andy's bedroom has mean: True or False?
True (0.8787311338092536)
Andy's bedroom has no mean: True or False?
True (0.5583270361921496)
Andy's bedroom has motive: True or False?
True (0.8158201638039532)
Andy's bedroom has no motive: True or False?
True (0.5282900215677746)
Andy's bedroom has opportunity: True or False?
True (0.5650587130190106)
Andy's bedroom has no opportunity: True or False?
False (0.6187804294217345)
Matthew's bedroom is guilty: True or False?
True (0.6343168082332088)
Matthew's bedroom is not guilty: True or False?
True (0.6774740084332073)
Matthew's bedroom has mean: True or False?
True (0.9142907234091052)
Matthew's bedroom has no mean: True or False?
True (0.7786492592534148)
Matthew's bedroom has motive: True or False?
True (0.8606036289596553)
Matthew's bedroom has no motive: True or False?
True (0.589834510337428)
Matthew's bedroom has opportunity: True or False?
True (0.784649255215384)
Matthew's bedroom has no opportunity: True or False?
True (0.60859406896259)
The garage is guilty: True or False?
True (0.7577943897558946)
The garage is not guilty: True or False?
True (0.7563575572780217)
The garage has mean: True or False?
True (0.8044059309478723)
The garage has no mean: True or False?
True (0.6224593484250324)
The garage has motive: True or False?
True (0.7170118721569225)
The garage has no motive: True or False?
True (0.615087855649269)
The garage has opportunity: True or False?
True (0.7416740115009234)
The garage has no opportunity: True or False?
True (0.5156199352405011)
The hall closet is guilty: True or False?
True (0.5224458497983033)
The hall closet is not guilty: True or False?
True (0.6834194581047349)
The hall closet has mean: True or False?
True (0.7813306496768853)
The hall closet has no mean: True or False?
True (0.6610481693322063)
Map:  92%|█████████▏| 187/203 [1:58:06<09:16, 34.81s/ examples]Map:  93%|█████████▎| 188/203 [1:58:42<08:48, 35.25s/ examples]Map:  93%|█████████▎| 189/203 [1:59:38<09:40, 41.43s/ examples]The hall closet has motive: True or False?
True (0.7937461674149602)
The hall closet has no motive: True or False?
False (0.5087881523495457)
The hall closet has opportunity: True or False?
True (0.7527403228571042)
The hall closet has no opportunity: True or False?
False (0.5736784476125245)
The tree house is guilty: True or False?
True (0.5535053004623279)
The tree house is not guilty: True or False?
True (0.6306849143569856)
The tree house has mean: True or False?
True (0.8244619332958376)
The tree house has no mean: True or False?
True (0.6197014353942354)
The tree house has motive: True or False?
True (0.8044059309478723)
The tree house has no motive: True or False?
False (0.5087881220234095)
The tree house has opportunity: True or False?
True (0.6645403391983984)
The tree house has no opportunity: True or False?
False (0.6325027218909103)
### Andy's bedroom
- mean: False (0.44167296380785037)
- motive: False (0.4717099784322254)
- opportunity: False (0.0)

### Matthew's bedroom
- mean: False (0.22135074074658523)
- motive: False (0.41016548966257205)
- opportunity: False (0.39140593103740995)

### The garage
- mean: False (0.37754065157496763)
- motive: False (0.38491214435073096)
- opportunity: False (0.4843800647594989)

### The hall closet
- mean: True (0.7813306496768853)
- motive: True (0.7937461674149602)
- opportunity: True (0.7527403228571042)

### The tree house
- mean: False (0.3802985646057646)
- motive: False (0.0)
- opportunity: False (0.0)

The culprit is The hall closet.
In fact, it is The tree house.
## 5minutemystery-the-mysterious-gift
CIndy is guilty: True or False?
True (0.7394223819718238)
CIndy is not guilty: True or False?
True (0.6901415551283886)
CIndy has mean: True or False?
True (0.7813306496768853)
CIndy has no mean: True or False?
True (0.5360700410935405)
CIndy has motive: True or False?
True (0.72951977676791)
CIndy has no motive: True or False?
True (0.6325027972911149)
CIndy has opportunity: True or False?
True (0.5156198737738186)
CIndy has no opportunity: True or False?
False (0.589834510337428)
Josie's mother is guilty: True or False?
False (0.6297746298200823)
Josie's mother is not guilty: True or False?
False (0.7424216889954057)
Josie's mother has mean: True or False?
False (0.8994750975198919)
Josie's mother has no mean: True or False?
False (0.9355823382423648)
Josie's mother has motive: True or False?
True (0.595492552580428)
Josie's mother has no motive: True or False?
False (0.9056565771882901)
Josie's mother has opportunity: True or False?
False (0.8074606715677252)
Josie's mother has no opportunity: True or False?
False (0.9577545517476556)
Lester is guilty: True or False?
True (0.8122724274380432)
Lester is not guilty: True or False?
True (0.7732163648437078)
Lester has mean: True or False?
True (0.8365545874520802)
Lester has no mean: True or False?
False (0.5486734987923966)
Lester has motive: True or False?
True (0.6992544513448877)
Lester has no motive: True or False?
False (0.5097643762740132)
Lester has opportunity: True or False?
False (0.5097644370426659)
Lester has no opportunity: True or False?
False (0.7806624796117883)
Lorraine is guilty: True or False?
True (0.6361271113853048)
Lorraine is not guilty: True or False?
True (0.638384519849353)
Lorraine has mean: True or False?
True (0.7154240000492645)
Lorraine has no mean: True or False?
False (0.5688948754232768)
Lorraine has motive: True or False?
True (0.7065955344877805)
Lorraine has no motive: True or False?
False (0.6197014353942354)
Lorraine has opportunity: True or False?
False (0.5964331434971528)
Lorraine has no opportunity: True or False?
False (0.7606506998655483)
### CIndy
- mean: False (0.4639299589064595)
- motive: False (0.3674972027088851)
- opportunity: False (0.0)

### Josie's mother
- mean: False (0.8994750975198919)
- motive: False (0.0)
- opportunity: False (0.8074606715677252)

### Lester
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.5097644370426659)

### Lorraine
- mean: True (0.7154240000492645)
- motive: True (0.7065955344877805)
- opportunity: True (0.23934930013445166)

The culprit is Lorraine.
In fact, it is Lorraine.
## 5minutemystery-perry-mason-and-the-high-school-crush-murder
Morris Ingalls is guilty: True or False?
True (0.9364013693337395)
Morris Ingalls is not guilty: True or False?
True (0.8955227118091885)
Morris Ingalls has mean: True or False?
True (0.8062431235779619)
Morris Ingalls has no mean: True or False?
True (0.8464508684792033)
Morris Ingalls has motive: True or False?
True (0.9394706502722077)
Morris Ingalls has no motive: True or False?
True (0.7708100054796322)
Morris Ingalls has opportunity: True or False?
True (0.8982321647536474)
Morris Ingalls has no opportunity: True or False?
True (0.7759445334082792)
Randolph Johnson is guilty: True or False?
True (0.8640812064457842)
Randolph Johnson is not guilty: True or False?
True (0.7541915688671895)
Randolph Johnson has mean: True or False?
True (0.8840392847025188)
Randolph Johnson has no mean: True or False?
True (0.7287482572006113)
Randolph Johnson has motive: True or False?
True (0.8454326455643386)
Randolph Johnson has no motive: True or False?
True (0.5860490988363701)
Randolph Johnson has opportunity: True or False?
True (0.8360197583769845)
Randolph Johnson has no opportunity: True or False?
True (0.5389832197022594)
Sarah Conrad is guilty: True or False?
True (0.7969253675907205)
Sarah Conrad is not guilty: True or False?
True (0.7446563751413027)
Sarah Conrad has mean: True or False?
True (0.6893056096647525)
Sarah Conrad has no mean: True or False?
True (0.6325027218909103)
Sarah Conrad has motive: True or False?
True (0.8267117710471246)
Sarah Conrad has no motive: True or False?
True (0.5860491337676195)
Sarah Conrad has opportunity: True or False?
True (0.8278281666221954)
Sarah Conrad has no opportunity: True or False?
False (0.580352018589158)
Tom Gooding is guilty: True or False?
True (0.9309620852900756)
Tom Gooding is not guilty: True or False?
True (0.8797679608387514)
Tom Gooding has mean: True or False?
True (0.9121235591541035)
Tom Gooding has no mean: True or False?
True (0.7431679939957333)
Tom Gooding has motive: True or False?
True (0.8893367679552574)
Tom Gooding has no motive: True or False?
True (0.7683857617837733)
Tom Gooding has opportunity: True or False?
True (0.9094255002859922)
Tom Gooding has no opportunity: True or False?
True (0.7000752133823226)
### Morris Ingalls
- mean: False (0.15354913152079674)
- motive: False (0.2291899945203678)
- opportunity: False (0.22405546659172082)

### Randolph Johnson
- mean: False (0.2712517427993887)
- motive: False (0.41395090116362987)
- opportunity: False (0.4610167802977406)

### Sarah Conrad
- mean: True (0.6893056096647525)
- motive: True (0.8267117710471246)
- opportunity: True (0.8278281666221954)

### Tom Gooding
- mean: False (0.2568320060042667)
- motive: False (0.23161423821622673)
- opportunity: False (0.2999247866176774)

The culprit is Sarah Conrad.
In fact, it is Morris Ingalls.
## 5minutemystery-who-stole-super-tuesday
Barry is guilty: True or False?
True (0.8803862939824989)
Barry is not guilty: True or False?
True (0.8683809052472352)
Barry has mean: True or False?
True (0.9032942081209032)
Barry has no mean: True or False?
False (0.6306849143569856)
Barry has motive: True or False?
True (0.9335520893498362)
Barry has no motive: True or False?
True (0.705785027818136)
Barry has opportunity: True or False?
True (0.809577288641998)
Barry has no opportunity: True or False?
False (0.7613610520273686)
Ricky Churrelo is guilty: True or False?
True (0.7680380401429294)
Ricky Churrelo is not guilty: True or False?
False (0.5141564045501756)
Ricky Churrelo has mean: True or False?
False (0.6169357925086439)
Ricky Churrelo has no mean: True or False?
False (0.7937461674149602)
Ricky Churrelo has motive: True or False?
True (0.6992543888266708)
Ricky Churrelo has no motive: True or False?
True (0.5486734987923966)
Ricky Churrelo has opportunity: True or False?
False (0.7592253761865491)
Ricky Churrelo has no opportunity: True or False?
False (0.9044819499212575)
Simon Knowles is guilty: True or False?
Map:  94%|█████████▎| 190/203 [2:00:16<08:43, 40.26s/ examples]Map:  94%|█████████▍| 191/203 [2:00:44<07:19, 36.60s/ examples]Map:  95%|█████████▍| 192/203 [2:01:12<06:13, 33.98s/ examples]True (0.9298236969789664)
Simon Knowles is not guilty: True or False?
True (0.7789858009240295)
Simon Knowles has mean: True or False?
True (0.5525396910980834)
Simon Knowles has no mean: True or False?
False (0.7325918709325988)
Simon Knowles has motive: True or False?
True (0.8143482752411424)
Simon Knowles has no motive: True or False?
True (0.7178037814283548)
Simon Knowles has opportunity: True or False?
False (0.7325918709325988)
Simon Knowles has no opportunity: True or False?
False (0.8670357473609658)
Xavier Ericksen is guilty: True or False?
True (0.8258708137274083)
Xavier Ericksen is not guilty: True or False?
True (0.5058591351869154)
Xavier Ericksen has mean: True or False?
False (0.7371581892031299)
Xavier Ericksen has no mean: True or False?
False (0.8216173667955227)
Xavier Ericksen has motive: True or False?
True (0.5122046514309807)
Xavier Ericksen has no motive: True or False?
False (0.5746334908651781)
Xavier Ericksen has opportunity: True or False?
False (0.8509646659219744)
Xavier Ericksen has no opportunity: True or False?
False (0.9571578507101896)
### Barry
- mean: True (0.9032942081209032)
- motive: True (0.9335520893498362)
- opportunity: True (0.809577288641998)

### Ricky Churrelo
- mean: False (0.6169357925086439)
- motive: False (0.4513265012076034)
- opportunity: False (0.7592253761865491)

### Simon Knowles
- mean: False (0.0)
- motive: False (0.28219621857164523)
- opportunity: False (0.7325918709325988)

### Xavier Ericksen
- mean: False (0.7371581892031299)
- motive: False (0.0)
- opportunity: False (0.8509646659219744)

The culprit is Barry.
In fact, it is Simon Knowles.
## 5minutemystery-the-missing-son
Caleb is guilty: True or False?
True (0.8071567978738078)
Caleb is not guilty: True or False?
True (0.8818185984511544)
Caleb has mean: True or False?
True (0.9178934131644976)
Caleb has no mean: True or False?
True (0.7185944237486072)
Caleb has motive: True or False?
True (0.9536218061663073)
Caleb has no motive: True or False?
True (0.6706082735718226)
Caleb has opportunity: True or False?
True (0.8563323578093363)
Caleb has no opportunity: True or False?
False (0.6909763109505791)
Conner is guilty: True or False?
True (0.7272012283179254)
Conner is not guilty: True or False?
True (0.7476159279883341)
Conner has mean: True or False?
True (0.934155284694701)
Conner has no mean: True or False?
True (0.767689835247798)
Conner has motive: True or False?
True (0.9515039936355008)
Conner has no motive: True or False?
False (0.5341265295318852)
Conner has opportunity: True or False?
True (0.9076402191395381)
Conner has no opportunity: True or False?
False (0.7106283339569771)
Jordan is guilty: True or False?
True (0.7559974119430289)
Jordan is not guilty: True or False?
True (0.8125700297166154)
Jordan has mean: True or False?
True (0.8365545874520802)
Jordan has no mean: True or False?
False (0.5746334908651781)
Jordan has motive: True or False?
True (0.9046505665674094)
Jordan has no motive: True or False?
True (0.6714705301843162)
Jordan has opportunity: True or False?
True (0.5755880655791468)
Jordan has no opportunity: True or False?
False (0.7833262085677729)
Kyle is guilty: True or False?
True (0.7997552678397243)
Kyle is not guilty: True or False?
True (0.7981867775042927)
Kyle has mean: True or False?
True (0.8454326455643386)
Kyle has no mean: True or False?
True (0.5243946792389143)
Kyle has motive: True or False?
True (0.9008791478232747)
Kyle has no motive: True or False?
True (0.5832033352502285)
Kyle has opportunity: True or False?
True (0.7302898278778687)
Kyle has no opportunity: True or False?
False (0.7264255794048772)
### Caleb
- mean: False (0.28140557625139284)
- motive: False (0.3293917264281774)
- opportunity: False (0.0)

### Conner
- mean: True (0.934155284694701)
- motive: True (0.9515039936355008)
- opportunity: True (0.9076402191395381)

### Jordan
- mean: False (0.0)
- motive: False (0.32852946981568376)
- opportunity: False (0.0)

### Kyle
- mean: False (0.47560532076108575)
- motive: False (0.4167966647497715)
- opportunity: False (0.0)

The culprit is Conner.
In fact, it is Caleb.
## 5minutemystery-the-stolen-cupcake
Angelica is guilty: True or False?
True (0.5185461538431656)
Angelica is not guilty: True or False?
False (0.6242935037467142)
Angelica has mean: True or False?
False (0.6926419789019715)
Angelica has no mean: True or False?
False (0.8688268116310761)
Angelica has motive: True or False?
True (0.720171518230031)
Angelica has no motive: True or False?
True (0.5389832197022594)
Angelica has opportunity: True or False?
False (0.5312093625105829)
Angelica has no opportunity: True or False?
False (0.8169911556077801)
Caedon is guilty: True or False?
True (0.6057990946577705)
Caedon is not guilty: True or False?
False (0.5263427467960875)
Caedon has mean: True or False?
True (0.5660185351323219)
Caedon has no mean: True or False?
False (0.8365545874520802)
Caedon has motive: True or False?
True (0.7613611200983542)
Caedon has no motive: True or False?
True (0.591723272524637)
Caedon has opportunity: True or False?
False (0.5097643762740132)
Caedon has no opportunity: True or False?
False (0.8210441512234701)
Ross is guilty: True or False?
True (0.5813030649269245)
Ross is not guilty: True or False?
True (0.5389831554504565)
Ross has mean: True or False?
True (0.612309626324874)
Ross has no mean: True or False?
False (0.5774954003013352)
Ross has motive: True or False?
True (0.8539127077831877)
Ross has no motive: True or False?
True (0.5964331079469681)
Ross has opportunity: True or False?
True (0.6513548405484016)
Ross has no opportunity: True or False?
False (0.6918097672776748)
Tony is guilty: True or False?
False (0.7541915239138703)
Tony is not guilty: True or False?
False (0.8086723099497763)
Tony has mean: True or False?
False (0.7620701143808404)
Tony has no mean: True or False?
False (0.8433797899747144)
Tony has motive: True or False?
True (0.5888891269161294)
Tony has no motive: True or False?
False (0.6688802830862913)
Tony has opportunity: True or False?
False (0.5631377056275331)
Tony has no opportunity: True or False?
False (0.8624675215861032)
### Angelica
- mean: False (0.6926419789019715)
- motive: False (0.4610167802977406)
- opportunity: False (0.5312093625105829)

### Caedon
- mean: False (0.0)
- motive: False (0.40827672747536303)
- opportunity: False (0.5097643762740132)

### Ross
- mean: True (0.612309626324874)
- motive: True (0.8539127077831877)
- opportunity: True (0.6513548405484016)

### Tony
- mean: False (0.7620701143808404)
- motive: False (0.0)
- opportunity: False (0.5631377056275331)

The culprit is Ross.
In fact, it is Caedon.
## 5minutemystery-school-trip
Beth is guilty: True or False?
False (0.7476159279883341)
Beth is not guilty: True or False?
True (0.6270381219830087)
Beth has mean: True or False?
True (0.7577943897558946)
Beth has no mean: True or False?
False (0.7690802105138688)
Beth has motive: True or False?
True (0.7527403228571042)
Beth has no motive: True or False?
True (0.5860490988363701)
Beth has opportunity: True or False?
False (0.6749080895533367)
Beth has no opportunity: True or False?
False (0.7468781552484828)
Damon is guilty: True or False?
True (0.5879430860094185)
Damon is not guilty: True or False?
True (0.8601343603168419)
Damon has mean: True or False?
True (0.8289388437432279)
Damon has no mean: True or False?
False (0.5107405249783342)
Damon has motive: True or False?
True (0.6424325178417575)
Damon has no motive: True or False?
True (0.6451199006197486)
Damon has opportunity: True or False?
True (0.6714705702070799)
Damon has no opportunity: True or False?
False (0.5350984235603058)
Leo is guilty: True or False?
False (0.5467381591701916)
Leo is not guilty: True or False?
True (0.8272706249326802)
Leo has mean: True or False?
True (0.6943026818003076)
Leo has no mean: True or False?
False (0.6740504382339836)
Leo has motive: True or False?
True (0.8795611817678315)
Leo has no motive: True or False?
True (0.7209580648179327)
Leo has opportunity: True or False?
True (0.7556369876990674)
Leo has no opportunity: True or False?
True (0.6160122877297346)
Mr. Michael's is guilty: True or False?
Map:  95%|█████████▌| 193/203 [2:01:49<05:49, 34.93s/ examples]Map:  96%|█████████▌| 194/203 [2:02:30<05:31, 36.85s/ examples]False (0.642432441257838)
Mr. Michael's is not guilty: True or False?
True (0.5640984675176304)
Mr. Michael's has mean: True or False?
True (0.7931058945535956)
Mr. Michael's has no mean: True or False?
False (0.7641883982873323)
Mr. Michael's has motive: True or False?
False (0.6076631662366868)
Mr. Michael's has no motive: True or False?
False (0.6791787167336184)
Mr. Michael's has opportunity: True or False?
False (0.7704647687904915)
Mr. Michael's has no opportunity: True or False?
False (0.8944211616820568)
The Seniors is guilty: True or False?
True (0.5389832197022594)
The Seniors is not guilty: True or False?
True (0.8086723099497763)
The Seniors has mean: True or False?
True (0.5784481782924303)
The Seniors has no mean: True or False?
False (0.7348812840309261)
The Seniors has motive: True or False?
True (0.5370413742099674)
The Seniors has no motive: True or False?
True (0.5234203246639862)
The Seniors has opportunity: True or False?
False (0.842345065078002)
The Seniors has no opportunity: True or False?
False (0.7732163648437078)
### Beth
- mean: False (0.0)
- motive: False (0.41395090116362987)
- opportunity: False (0.6749080895533367)

### Damon
- mean: True (0.8289388437432279)
- motive: True (0.6424325178417575)
- opportunity: True (0.6714705702070799)

### Leo
- mean: False (0.0)
- motive: False (0.2790419351820673)
- opportunity: False (0.3839877122702654)

### Mr. Michael's
- mean: False (0.0)
- motive: False (0.6076631662366868)
- opportunity: False (0.7704647687904915)

### The Seniors
- mean: False (0.0)
- motive: False (0.47657967533601375)
- opportunity: False (0.842345065078002)

The culprit is Damon.
In fact, it is The Seniors.
## 5minutemystery-arsonist-attack
Jade Foster is guilty: True or False?
True (0.9449946880768697)
Jade Foster is not guilty: True or False?
True (0.9532750262379774)
Jade Foster has mean: True or False?
True (0.9302051049548884)
Jade Foster has no mean: True or False?
True (0.8774768149941248)
Jade Foster has motive: True or False?
True (0.9082930095862076)
Jade Foster has no motive: True or False?
True (0.9537943000694998)
Jade Foster has opportunity: True or False?
True (0.8534247816107388)
Jade Foster has no opportunity: True or False?
True (0.8647679145346777)
Jock Matt is guilty: True or False?
True (0.9331876642092066)
Jock Matt is not guilty: True or False?
True (0.9567959908103164)
Jock Matt has mean: True or False?
True (0.9346342066470359)
Jock Matt has no mean: True or False?
True (0.832781310996106)
Jock Matt has motive: True or False?
True (0.865678909174824)
Jock Matt has no motive: True or False?
True (0.9385759220258869)
Jock Matt has opportunity: True or False?
True (0.8638516611889259)
Jock Matt has no opportunity: True or False?
True (0.7641883982873323)
Madelyn Reader is guilty: True or False?
True (0.9567959302164903)
Madelyn Reader is not guilty: True or False?
True (0.9548162813994148)
Madelyn Reader has mean: True or False?
True (0.9341553473346962)
Madelyn Reader has no mean: True or False?
True (0.862930180750016)
Madelyn Reader has motive: True or False?
True (0.9367495172436676)
Madelyn Reader has no motive: True or False?
True (0.9524858586686383)
Madelyn Reader has opportunity: True or False?
True (0.7505527730327083)
Madelyn Reader has no opportunity: True or False?
True (0.8563324216110711)
Max Crabgrass is guilty: True or False?
True (0.9252299038987163)
Max Crabgrass is not guilty: True or False?
True (0.948346255948953)
Max Crabgrass has mean: True or False?
True (0.9381240005131491)
Max Crabgrass has no mean: True or False?
True (0.8994751578343994)
Max Crabgrass has motive: True or False?
True (0.9056565771882901)
Max Crabgrass has no motive: True or False?
True (0.9355823382423648)
Max Crabgrass has opportunity: True or False?
True (0.8856314413364714)
Max Crabgrass has no opportunity: True or False?
True (0.8433797899747144)
Security Guard is guilty: True or False?
True (0.9543079126608008)
Security Guard is not guilty: True or False?
True (0.9541373270174538)
Security Guard has mean: True or False?
True (0.9273632783787477)
Security Guard has no mean: True or False?
True (0.7924642605907138)
Security Guard has motive: True or False?
True (0.9276260107813639)
Security Guard has no motive: True or False?
True (0.9544780238917078)
Security Guard has opportunity: True or False?
True (0.8397339530959691)
Security Guard has no opportunity: True or False?
True (0.8529354311342636)
### Jade Foster
- mean: False (0.12252318500587522)
- motive: False (0.046205699930500166)
- opportunity: False (0.13523208546532228)

### Jock Matt
- mean: False (0.16721868900389403)
- motive: False (0.06142407797411309)
- opportunity: False (0.23581160171266768)

### Madelyn Reader
- mean: True (0.9341553473346962)
- motive: True (0.9367495172436676)
- opportunity: True (0.7505527730327083)

### Max Crabgrass
- mean: False (0.10052484216560065)
- motive: False (0.06441766175763519)
- opportunity: False (0.1566202100252856)

### Security Guard
- mean: False (0.20753573940928616)
- motive: False (0.04552197610829223)
- opportunity: False (0.14706456886573638)

The culprit is Madelyn Reader.
In fact, it is Jade Foster.
## 5minutemystery-investigation-sabotager
Emma is guilty: True or False?
True (0.9149009617112335)
Emma is not guilty: True or False?
True (0.9001793304600783)
Emma has mean: True or False?
True (0.9073122118500465)
Emma has no mean: True or False?
True (0.7461389980806673)
Emma has motive: True or False?
True (0.9333093737798925)
Emma has no motive: True or False?
True (0.874934615163517)
Emma has opportunity: True or False?
True (0.9084555478510448)
Emma has no opportunity: True or False?
True (0.7424217332471881)
Mary is guilty: True or False?
True (0.942400812874096)
Mary is not guilty: True or False?
True (0.8860265599597172)
Mary has mean: True or False?
True (0.9114953904850286)
Mary has no mean: True or False?
True (0.8019358443954961)
Mary has motive: True or False?
True (0.9465966835599983)
Mary has no motive: True or False?
True (0.8787311338092536)
Mary has opportunity: True or False?
True (0.9529258022651363)
Mary has no opportunity: True or False?
True (0.8732148436000907)
Peter is guilty: True or False?
True (0.9187722824991111)
Peter is not guilty: True or False?
True (0.8872045854516336)
Peter has mean: True or False?
True (0.8294920340613177)
Peter has no mean: True or False?
True (0.555435228101316)
Peter has motive: True or False?
True (0.8824278665848695)
Peter has no motive: True or False?
True (0.8376199551237796)
Peter has opportunity: True or False?
True (0.8918110736745599)
Peter has no opportunity: True or False?
True (0.5698526542706361)
Tim is guilty: True or False?
True (0.8643104392003704)
Tim is not guilty: True or False?
True (0.8181563669811865)
Tim has mean: True or False?
True (0.8991213421091365)
Tim has no mean: True or False?
True (0.6233768569026616)
Tim has motive: True or False?
True (0.884837803442546)
Tim has no motive: True or False?
True (0.8349459127213729)
Tim has opportunity: True or False?
True (0.8250265688168699)
Tim has no opportunity: True or False?
True (0.685107355950278)
Valerie is guilty: True or False?
True (0.873646620599733)
Valerie is not guilty: True or False?
True (0.8807970862580315)
Valerie has mean: True or False?
True (0.9343951361750445)
Valerie has no mean: True or False?
True (0.5973730125048408)
Valerie has motive: True or False?
True (0.9392481417861557)
Valerie has no motive: True or False?
True (0.8697146199790504)
Valerie has opportunity: True or False?
True (0.8960695891821668)
Valerie has no opportunity: True or False?
True (0.5992506238662876)
### Emma
- mean: False (0.2538610019193327)
- motive: False (0.125065384836483)
- opportunity: False (0.2575782667528119)

### Mary
- mean: True (0.9114953904850286)
- motive: True (0.9465966835599983)
- opportunity: True (0.9529258022651363)

### Peter
- mean: False (0.44456477189868404)
- motive: False (0.16238004487622038)
- opportunity: False (0.43014734572936386)

### Tim
- mean: False (0.37662314309733835)
- motive: False (0.16505408727862714)
- opportunity: False (0.31489264404972195)

### Valerie
- mean: False (0.40262698749515924)
Map:  96%|█████████▌| 195/203 [2:03:05<04:49, 36.20s/ examples]Map:  97%|█████████▋| 196/203 [2:03:36<04:03, 34.74s/ examples]Map:  97%|█████████▋| 197/203 [2:04:15<03:35, 35.84s/ examples]- motive: False (0.13028538002094958)
- opportunity: False (0.4007493761337124)

The culprit is Mary.
In fact, it is Emma.
## 5minutemystery-the-presidential-smear-campaint-a-jacelyn-drew-mystery
Brittany is guilty: True or False?
True (0.8255897087847518)
Brittany is not guilty: True or False?
True (0.8620035048683017)
Brittany has mean: True or False?
True (0.8013146490010521)
Brittany has no mean: True or False?
True (0.6766198919456847)
Brittany has motive: True or False?
True (0.84440905415483)
Brittany has no motive: True or False?
True (0.7669924589170153)
Brittany has opportunity: True or False?
True (0.5907792634380938)
Brittany has no opportunity: True or False?
False (0.5097643762740132)
Isis is guilty: True or False?
True (0.9446893339351747)
Isis is not guilty: True or False?
True (0.9491062747098069)
Isis has mean: True or False?
True (0.7498207054286419)
Isis has no mean: True or False?
True (0.7178038242127955)
Isis has motive: True or False?
True (0.905989824801558)
Isis has no motive: True or False?
True (0.9518632280135741)
Isis has opportunity: True or False?
True (0.6513548405484016)
Isis has no opportunity: True or False?
True (0.6469064338453809)
Marie is guilty: True or False?
True (0.7017130830397807)
Marie is not guilty: True or False?
True (0.866132552869269)
Marie has mean: True or False?
True (0.7178038242127955)
Marie has no mean: True or False?
True (0.5765419579552815)
Marie has motive: True or False?
True (0.7931059536445917)
Marie has no motive: True or False?
True (0.7592254214399092)
Marie has opportunity: True or False?
True (0.6242935781683038)
Marie has no opportunity: True or False?
False (0.570809902165233)
Norma is guilty: True or False?
True (0.8056321690561029)
Norma is not guilty: True or False?
True (0.8665847814067802)
Norma has mean: True or False?
True (0.60859406896259)
Norma has no mean: True or False?
True (0.5428633110863297)
Norma has motive: True or False?
True (0.8267117710471246)
Norma has no motive: True or False?
True (0.7662936378892937)
Norma has opportunity: True or False?
True (0.5822535180679596)
Norma has no opportunity: True or False?
False (0.6169357925086439)
### Brittany
- mean: False (0.3233801080543153)
- motive: False (0.23300754108298471)
- opportunity: False (0.0)

### Isis
- mean: False (0.28219617578720446)
- motive: False (0.04813677198642585)
- opportunity: False (0.35309356615461907)

### Marie
- mean: False (0.4234580420447185)
- motive: False (0.24077457856009077)
- opportunity: False (0.0)

### Norma
- mean: True (0.60859406896259)
- motive: True (0.8267117710471246)
- opportunity: True (0.5822535180679596)

The culprit is Norma.
In fact, it is Isis.
## 5minutemystery-the-sunday-mystery
Jack Jackson is guilty: True or False?
True (0.8740772044235984)
Jack Jackson is not guilty: True or False?
True (0.8497219730709873)
Jack Jackson has mean: True or False?
True (0.8601343090488404)
Jack Jackson has no mean: True or False?
False (0.5669777909748143)
Jack Jackson has motive: True or False?
True (0.779321849347754)
Jack Jackson has no motive: True or False?
True (0.5631377056275331)
Jack Jackson has opportunity: True or False?
False (0.525368812147771)
Jack Jackson has no opportunity: True or False?
False (0.6984323202883935)
Jimmy Jackson is guilty: True or False?
True (0.8322366416985943)
Jimmy Jackson is not guilty: True or False?
True (0.7898827135821628)
Jimmy Jackson has mean: True or False?
True (0.8624675215861032)
Jimmy Jackson has no mean: True or False?
False (0.5860490988363701)
Jimmy Jackson has motive: True or False?
True (0.8128672807499561)
Jimmy Jackson has no motive: True or False?
True (0.5467381591701916)
Jimmy Jackson has opportunity: True or False?
True (0.5302364729224919)
Jimmy Jackson has no opportunity: True or False?
False (0.5973730125048408)
Jon Jackson is guilty: True or False?
True (0.8553685501761973)
Jon Jackson is not guilty: True or False?
True (0.8594279851904003)
Jon Jackson has mean: True or False?
True (0.9022656660556747)
Jon Jackson has no mean: True or False?
False (0.5312093625105829)
Jon Jackson has motive: True or False?
True (0.8940516749601143)
Jon Jackson has no motive: True or False?
True (0.6469064916833258)
Jon Jackson has opportunity: True or False?
True (0.6714705702070799)
Jon Jackson has no opportunity: True or False?
False (0.5746334908651781)
Maria Jackson is guilty: True or False?
True (0.8016254254291421)
Maria Jackson is not guilty: True or False?
True (0.814643384779728)
Maria Jackson has mean: True or False?
True (0.8840392847025188)
Maria Jackson has no mean: True or False?
False (0.5078118305218892)
Maria Jackson has motive: True or False?
True (0.879146760693242)
Maria Jackson has no motive: True or False?
True (0.5039061393777357)
Maria Jackson has opportunity: True or False?
True (0.6557770400181139)
Maria Jackson has no opportunity: True or False?
False (0.6297746298200823)
Spot is guilty: True or False?
True (0.6783269591477166)
Spot is not guilty: True or False?
True (0.7272012283179254)
Spot has mean: True or False?
True (0.8692713407917644)
Spot has no mean: True or False?
True (0.5535053004623279)
Spot has motive: True or False?
True (0.7937462383814009)
Spot has no motive: True or False?
True (0.7490872087035162)
Spot has opportunity: True or False?
True (0.5869964306477841)
Spot has no opportunity: True or False?
False (0.6575384693006662)
### Jack Jackson
- mean: False (0.0)
- motive: False (0.43686229437246693)
- opportunity: False (0.525368812147771)

### Jimmy Jackson
- mean: False (0.0)
- motive: False (0.45326184082980836)
- opportunity: False (0.0)

### Jon Jackson
- mean: True (0.9022656660556747)
- motive: True (0.8940516749601143)
- opportunity: True (0.6714705702070799)

### Maria Jackson
- mean: False (0.0)
- motive: False (0.49609386062226435)
- opportunity: False (0.0)

### Spot
- mean: False (0.44649469953767207)
- motive: False (0.2509127912964838)
- opportunity: False (0.0)

The culprit is Jon Jackson.
In fact, it is Spot.
## 5minutemystery-the-mystery-of-heritage
Jack Anderson is guilty: True or False?
True (0.9564311500981832)
Jack Anderson is not guilty: True or False?
True (0.9592307208025933)
Jack Anderson has mean: True or False?
True (0.8850366506597954)
Jack Anderson has no mean: True or False?
True (0.6270381219830087)
Jack Anderson has motive: True or False?
True (0.9381240005131491)
Jack Anderson has no motive: True or False?
True (0.794384956668203)
Jack Anderson has opportunity: True or False?
True (0.911809984585868)
Jack Anderson has no opportunity: True or False?
True (0.7348812840309261)
Jessica Anderson is guilty: True or False?
True (0.9310874934413855)
Jessica Anderson is not guilty: True or False?
True (0.8906751877407573)
Jessica Anderson has mean: True or False?
True (0.9029524325377104)
Jessica Anderson has no mean: True or False?
True (0.6654105193867614)
Jessica Anderson has motive: True or False?
True (0.8828325273478573)
Jessica Anderson has no motive: True or False?
True (0.7394224480813394)
Jessica Anderson has opportunity: True or False?
True (0.8221891570741111)
Jessica Anderson has no opportunity: True or False?
True (0.7178037814283548)
Martha Anderson is guilty: True or False?
True (0.9354645628936168)
Martha Anderson is not guilty: True or False?
True (0.9159593578192197)
Martha Anderson has mean: True or False?
True (0.8670358119601653)
Martha Anderson has no mean: True or False?
False (0.5525396910980834)
Martha Anderson has motive: True or False?
True (0.9099069836112468)
Martha Anderson has no motive: True or False?
True (0.6415346823638186)
Martha Anderson has opportunity: True or False?
True (0.8080671968507699)
Martha Anderson has no opportunity: True or False?
True (0.5841525779336078)
Mrs. Neil is guilty: True or False?
True (0.9553191057869168)
Mrs. Neil is not guilty: True or False?
True (0.854884620116169)
Mrs. Neil has mean: True or False?
True (0.9537942396657707)
Mrs. Neil has no mean: True or False?
True (0.8316905440184192)
Mrs. Neil has motive: True or False?
True (0.969324171790829)
Mrs. Neil has no motive: True or False?
True (0.7620701143808404)
Mrs. Neil has opportunity: True or False?
True (0.9553191057869168)
Map:  98%|█████████▊| 198/203 [2:04:41<02:45, 33.08s/ examples]Map:  98%|█████████▊| 199/203 [2:05:02<01:57, 29.40s/ examples]Map:  99%|█████████▊| 200/203 [2:05:38<01:34, 31.48s/ examples]Map:  99%|█████████▉| 201/203 [2:06:07<01:00, 30.49s/ examples]Mrs. Neil has no opportunity: True or False?
True (0.6740504382339836)
### Jack Anderson
- mean: False (0.3729618780169913)
- motive: False (0.20561504333179703)
- opportunity: False (0.2651187159690739)

### Jessica Anderson
- mean: False (0.33458948061323857)
- motive: False (0.2605775519186606)
- opportunity: False (0.28219621857164523)

### Martha Anderson
- mean: True (0.8670358119601653)
- motive: True (0.9099069836112468)
- opportunity: True (0.8080671968507699)

### Mrs. Neil
- mean: False (0.16830945598158076)
- motive: False (0.23792988561915962)
- opportunity: False (0.3259495617660164)

The culprit is Martha Anderson.
In fact, it is Jessica Anderson.
## 5minutemystery-murder-of-the-actor
Bruce Whittingley is guilty: True or False?
True (0.8714748565614324)
Bruce Whittingley is not guilty: True or False?
True (0.8848377441095496)
Bruce Whittingley has mean: True or False?
True (0.8300437877296776)
Bruce Whittingley has no mean: True or False?
False (0.5350984235603058)
Bruce Whittingley has motive: True or False?
True (0.7017130830397807)
Bruce Whittingley has no motive: True or False?
True (0.8670357473609658)
Bruce Whittingley has opportunity: True or False?
True (0.65489470935198)
Bruce Whittingley has no opportunity: True or False?
True (0.6513548405484016)
Marie Carloette is guilty: True or False?
True (0.759938723019178)
Marie Carloette is not guilty: True or False?
True (0.8204693794114111)
Marie Carloette has mean: True or False?
True (0.7911763836133219)
Marie Carloette has no mean: True or False?
False (0.5078118305218892)
Marie Carloette has motive: True or False?
True (0.8354834909254251)
Marie Carloette has no motive: True or False?
True (0.8006920257960423)
Marie Carloette has opportunity: True or False?
True (0.8283841584202847)
Marie Carloette has no opportunity: True or False?
True (0.6859494535376744)
Mario Marcino is guilty: True or False?
True (0.9079670935046645)
Mario Marcino is not guilty: True or False?
True (0.8991214023999228)
Mario Marcino has mean: True or False?
True (0.7988153087356352)
Mario Marcino has no mean: True or False?
True (0.5765418892261284)
Mario Marcino has motive: True or False?
True (0.7950222460539826)
Mario Marcino has no motive: True or False?
True (0.8832359917473193)
Mario Marcino has opportunity: True or False?
True (0.7310585348819939)
Mario Marcino has no opportunity: True or False?
True (0.7853085971692302)
### Bruce Whittingley
- mean: True (0.8300437877296776)
- motive: True (0.7017130830397807)
- opportunity: True (0.65489470935198)

### Marie Carloette
- mean: False (0.0)
- motive: False (0.19930797420395774)
- opportunity: False (0.31405054646232555)

### Mario Marcino
- mean: False (0.42345811077387163)
- motive: False (0.11676400825268074)
- opportunity: False (0.21469140283076982)

The culprit is Bruce Whittingley.
In fact, it is Marie Carloette.
## 5minutemystery-another-hotel-murder
Dianne Shelby is guilty: True or False?
True (0.7994423454932595)
Dianne Shelby is not guilty: True or False?
True (0.7209580648179327)
Dianne Shelby has mean: True or False?
True (0.8227594449669557)
Dianne Shelby has no mean: True or False?
False (0.5448014304301324)
Dianne Shelby has motive: True or False?
True (0.7154240000492645)
Dianne Shelby has no motive: True or False?
True (0.6884684608108543)
Dianne Shelby has opportunity: True or False?
True (0.6800292132037243)
Dianne Shelby has no opportunity: True or False?
True (0.6627964974378784)
James Castro is guilty: True or False?
True (0.8620035048683017)
James Castro is not guilty: True or False?
True (0.821044090050916)
James Castro has mean: True or False?
True (0.8918110138739693)
James Castro has no mean: True or False?
False (0.5380124470448935)
James Castro has motive: True or False?
True (0.8370879250561812)
James Castro has no motive: True or False?
True (0.7170118721569225)
James Castro has opportunity: True or False?
True (0.847967740521315)
James Castro has no opportunity: True or False?
True (0.6654105788791005)
Kevin King is guilty: True or False?
True (0.9102267057681164)
Kevin King is not guilty: True or False?
True (0.8638516611889259)
Kevin King has mean: True or False?
True (0.9639160647221925)
Kevin King has no mean: True or False?
True (0.6242935037467142)
Kevin King has motive: True or False?
True (0.7613610520273686)
Kevin King has no motive: True or False?
True (0.7302898714065358)
Kevin King has opportunity: True or False?
True (0.776622945813876)
Kevin King has no opportunity: True or False?
True (0.6169357925086439)
Roger Shelby is guilty: True or False?
True (0.8969755785184792)
Roger Shelby is not guilty: True or False?
True (0.8311430212356835)
Roger Shelby has mean: True or False?
True (0.8407825844829613)
Roger Shelby has no mean: True or False?
False (0.5234203246639862)
Roger Shelby has motive: True or False?
True (0.702530072932436)
Roger Shelby has no motive: True or False?
True (0.6943027438758075)
Roger Shelby has opportunity: True or False?
True (0.7017130830397807)
Roger Shelby has no opportunity: True or False?
True (0.5486734987923966)
### Dianne Shelby
- mean: True (0.8227594449669557)
- motive: True (0.7154240000492645)
- opportunity: True (0.6800292132037243)

### James Castro
- mean: False (0.0)
- motive: False (0.2829881278430775)
- opportunity: False (0.3345894211208995)

### Kevin King
- mean: False (0.3757064962532858)
- motive: False (0.2697101285934642)
- opportunity: False (0.38306420749135606)

### Roger Shelby
- mean: False (0.0)
- motive: False (0.3056972561241925)
- opportunity: False (0.4513265012076034)

The culprit is Dianne Shelby.
In fact, it is James Castro.
## 5minutemystery-the-missing-book
Brad is guilty: True or False?
True (0.5117165908639297)
Brad is not guilty: True or False?
True (0.5869964306477841)
Brad has mean: True or False?
True (0.7505527730327083)
Brad has no mean: True or False?
False (0.5907792634380938)
Brad has motive: True or False?
True (0.6048658333578858)
Brad has no motive: True or False?
False (0.5185461538431656)
Brad has opportunity: True or False?
True (0.5860491337676195)
Brad has no opportunity: True or False?
True (0.5350984235603058)
Fred is guilty: True or False?
True (0.7424216889954057)
Fred is not guilty: True or False?
True (0.7527403228571042)
Fred has mean: True or False?
True (0.7799928701983835)
Fred has no mean: True or False?
False (0.5094371206509557)
Fred has motive: True or False?
True (0.8086723702005608)
Fred has no motive: True or False?
True (0.6132366084149281)
Fred has opportunity: True or False?
True (0.6825737331070684)
Fred has no opportunity: True or False?
True (0.5794003525136094)
Mrs. Dunwoodee is guilty: True or False?
True (0.700075275973927)
Mrs. Dunwoodee is not guilty: True or False?
True (0.7371581232960549)
Mrs. Dunwoodee has mean: True or False?
True (0.5973730125048408)
Mrs. Dunwoodee has no mean: True or False?
False (0.5860491337676195)
Mrs. Dunwoodee has motive: True or False?
True (0.7233094544266295)
Mrs. Dunwoodee has no motive: True or False?
True (0.5869964306477841)
Mrs. Dunwoodee has opportunity: True or False?
True (0.7732163648437078)
Mrs. Dunwoodee has no opportunity: True or False?
True (0.6723316913929156)
Ricky is guilty: True or False?
True (0.5592900581575188)
Ricky is not guilty: True or False?
True (0.5879430860094185)
Ricky has mean: True or False?
True (0.7577943897558946)
Ricky has no mean: True or False?
False (0.5204963206682631)
Ricky has motive: True or False?
True (0.6206216296838327)
Ricky has no motive: True or False?
True (0.5389832197022594)
Ricky has opportunity: True or False?
True (0.6252093370817647)
Ricky has no opportunity: True or False?
False (0.5195212821349473)
### Brad
- mean: True (0.7505527730327083)
- motive: True (0.6048658333578858)
- opportunity: True (0.5860491337676195)

### Fred
- mean: False (0.0)
- motive: False (0.3867633915850719)
- opportunity: False (0.42059964748639056)

### Mrs. Dunwoodee
- mean: False (0.0)
- motive: False (0.41300356935221594)
- opportunity: False (0.3276683086070844)

### Ricky
- mean: False (0.0)
- motive: False (0.4610167802977406)
- opportunity: False (0.0)

The culprit is Brad.
In fact, it is Fred.
Map: 100%|█████████▉| 202/203 [2:06:40<00:31, 31.53s/ examples]Map: 100%|██████████| 203/203 [2:07:23<00:00, 34.97s/ examples]Map: 100%|██████████| 203/203 [2:07:24<00:00, 37.66s/ examples]
## 5minutemystery-the-necklace
Aunt Mary is guilty: True or False?
True (0.7826624547920057)
Aunt Mary is not guilty: True or False?
True (0.9005298052062833)
Aunt Mary has mean: True or False?
True (0.7969253675907205)
Aunt Mary has no mean: True or False?
True (0.5185461538431656)
Aunt Mary has motive: True or False?
True (0.8013146490010521)
Aunt Mary has no motive: True or False?
True (0.7872777601997338)
Aunt Mary has opportunity: True or False?
True (0.6584175136252488)
Aunt Mary has no opportunity: True or False?
False (0.5107405858633529)
Dad is guilty: True or False?
True (0.9233161821369215)
Dad is not guilty: True or False?
True (0.9626731268425771)
Dad has mean: True or False?
True (0.8864203688833437)
Dad has no mean: True or False?
True (0.8098781635062345)
Dad has motive: True or False?
True (0.8868131040663721)
Dad has no motive: True or False?
True (0.8895288123486662)
Dad has opportunity: True or False?
True (0.7512833387594996)
Dad has no opportunity: True or False?
True (0.5926665645259142)
Mom is guilty: True or False?
True (0.8509647293237851)
Mom is not guilty: True or False?
True (0.9289263523387795)
Mom has mean: True or False?
True (0.8433798528114077)
Mom has no mean: True or False?
True (0.6783269591477166)
Mom has motive: True or False?
True (0.8484706263347676)
Mom has no motive: True or False?
True (0.8019357965963964)
Mom has opportunity: True or False?
True (0.6132366084149281)
Mom has no opportunity: True or False?
False (0.6039318499573872)
Uncle Henry is guilty: True or False?
True (0.8504686406728537)
Uncle Henry is not guilty: True or False?
True (0.9095863097773887)
Uncle Henry has mean: True or False?
True (0.7409249009267298)
Uncle Henry has no mean: True or False?
True (0.5282900845448565)
Uncle Henry has motive: True or False?
True (0.8444089912414552)
Uncle Henry has no motive: True or False?
True (0.8333246107254184)
Uncle Henry has opportunity: True or False?
True (0.7655932860037753)
Uncle Henry has no opportunity: True or False?
True (0.6206216296838327)
Uncle John is guilty: True or False?
True (0.8204694405411458)
Uncle John is not guilty: True or False?
True (0.8820219652716884)
Uncle John has mean: True or False?
True (0.7483522884503825)
Uncle John has no mean: True or False?
False (0.5009765603034438)
Uncle John has motive: True or False?
True (0.7924642605907138)
Uncle John has no motive: True or False?
True (0.8250265073476026)
Uncle John has opportunity: True or False?
True (0.7256486384635821)
Uncle John has no opportunity: True or False?
True (0.6020615685826383)
### Aunt Mary
- mean: False (0.4814538461568344)
- motive: False (0.21272223980026617)
- opportunity: False (0.0)

### Dad
- mean: False (0.19012183649376546)
- motive: False (0.11047118765133379)
- opportunity: False (0.40733343547408585)

### Mom
- mean: False (0.32167304085228343)
- motive: False (0.19806420340360364)
- opportunity: False (0.0)

### Uncle Henry
- mean: False (0.4717099154551435)
- motive: False (0.1666753892745816)
- opportunity: False (0.3793783703161673)

### Uncle John
- mean: True (0.7483522884503825)
- motive: True (0.7924642605907138)
- opportunity: True (0.7256486384635821)

The culprit is Uncle John.
In fact, it is Dad.
## 5minutemystery-the-purloined-wallet
Bill Buchanan is guilty: True or False?
True (0.9599877610290866)
Bill Buchanan is not guilty: True or False?
True (0.943711818036405)
Bill Buchanan has mean: True or False?
True (0.8519527857346616)
Bill Buchanan has no mean: True or False?
True (0.6224592927728324)
Bill Buchanan has motive: True or False?
True (0.844921525814193)
Bill Buchanan has no motive: True or False?
True (0.8534247816107388)
Bill Buchanan has opportunity: True or False?
True (0.8807970337584357)
Bill Buchanan has no opportunity: True or False?
True (0.7826625131049049)
Carson Thomson is guilty: True or False?
True (0.9509148001014369)
Carson Thomson is not guilty: True or False?
True (0.9484418035658785)
Carson Thomson has mean: True or False?
True (0.8596637847360897)
Carson Thomson has no mean: True or False?
True (0.6654105788791005)
Carson Thomson has motive: True or False?
True (0.854884683810039)
Carson Thomson has no motive: True or False?
True (0.9240047343914451)
Carson Thomson has opportunity: True or False?
True (0.8221890958162477)
Carson Thomson has no opportunity: True or False?
True (0.7859664553110391)
Cooper is guilty: True or False?
True (0.921357630313903)
Cooper is not guilty: True or False?
True (0.9004423045512396)
Cooper has mean: True or False?
True (0.5312093941731293)
Cooper has no mean: True or False?
False (0.6992543888266708)
Cooper has motive: True or False?
True (0.7356416476869558)
Cooper has no motive: True or False?
True (0.8233283740192667)
Cooper has opportunity: True or False?
True (0.8357518369388613)
Cooper has no opportunity: True or False?
True (0.6001883144765984)
David Nader is guilty: True or False?
True (0.9019206173215508)
David Nader is not guilty: True or False?
True (0.8980534699860239)
David Nader has mean: True or False?
True (0.7272012283179254)
David Nader has no mean: True or False?
False (0.65489470935198)
David Nader has motive: True or False?
True (0.869271276026005)
David Nader has no motive: True or False?
True (0.8708171827875996)
David Nader has opportunity: True or False?
True (0.8128672807499561)
David Nader has no opportunity: True or False?
True (0.673191669892235)
Vincent Garcia is guilty: True or False?
True (0.9467446218678568)
Vincent Garcia is not guilty: True or False?
True (0.9399684678073418)
Vincent Garcia has mean: True or False?
True (0.8207569718385453)
Vincent Garcia has no mean: True or False?
False (0.5195213440667139)
Vincent Garcia has motive: True or False?
True (0.8624675215861032)
Vincent Garcia has no motive: True or False?
True (0.9031234959323464)
Vincent Garcia has opportunity: True or False?
True (0.8514594452543962)
Vincent Garcia has no opportunity: True or False?
True (0.7978720077929541)
### Bill Buchanan
- mean: False (0.3775407072271676)
- motive: False (0.14657521838926124)
- opportunity: False (0.21733748689509513)

### Carson Thomson
- mean: False (0.3345894211208995)
- motive: False (0.07599526560855485)
- opportunity: False (0.21403354468896085)

### Cooper
- mean: False (0.0)
- motive: False (0.17667162598073327)
- opportunity: False (0.3998116855234016)

### David Nader
- mean: False (0.0)
- motive: False (0.12918281721240044)
- opportunity: False (0.326808330107765)

### Vincent Garcia
- mean: True (0.8207569718385453)
- motive: True (0.8624675215861032)
- opportunity: True (0.8514594452543962)

The culprit is Vincent Garcia.
In fact, it is David Nader.
Solved 41 out of 203.
