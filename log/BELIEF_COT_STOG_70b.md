nohup: ignoring input
/home/sraja/mambaforge/envs/llm-mysteries/lib/python3.10/site-packages/transformers/models/auto/auto_factory.py:472: FutureWarning: The `use_auth_token` argument is deprecated and will be removed in v5 of Transformers. Please use `token` instead.
  warnings.warn(
Loading checkpoint shards:   0%|          | 0/15 [00:00<?, ?it/s]Loading checkpoint shards:   7%|▋         | 1/15 [00:01<00:24,  1.73s/it]Loading checkpoint shards:  13%|█▎        | 2/15 [00:03<00:21,  1.67s/it]Loading checkpoint shards:  20%|██        | 3/15 [00:04<00:19,  1.63s/it]Loading checkpoint shards:  27%|██▋       | 4/15 [00:06<00:18,  1.70s/it]Loading checkpoint shards:  33%|███▎      | 5/15 [00:08<00:18,  1.82s/it]Loading checkpoint shards:  40%|████      | 6/15 [00:10<00:16,  1.82s/it]Loading checkpoint shards:  47%|████▋     | 7/15 [00:12<00:14,  1.79s/it]Loading checkpoint shards:  53%|█████▎    | 8/15 [00:14<00:12,  1.81s/it]Loading checkpoint shards:  60%|██████    | 9/15 [00:15<00:10,  1.79s/it]Loading checkpoint shards:  67%|██████▋   | 10/15 [00:17<00:08,  1.76s/it]Loading checkpoint shards:  73%|███████▎  | 11/15 [00:19<00:06,  1.74s/it]Loading checkpoint shards:  80%|████████  | 12/15 [00:21<00:05,  1.76s/it]Loading checkpoint shards:  87%|████████▋ | 13/15 [00:22<00:03,  1.73s/it]Loading checkpoint shards:  93%|█████████▎| 14/15 [00:24<00:01,  1.69s/it]Loading checkpoint shards: 100%|██████████| 15/15 [00:24<00:00,  1.23s/it]Loading checkpoint shards: 100%|██████████| 15/15 [00:24<00:00,  1.64s/it]
/home/sraja/mambaforge/envs/llm-mysteries/lib/python3.10/site-packages/dill/_dill.py:412: PicklingWarning: Cannot locate reference to <class '_ctypes.PyCFuncPtrType'>.
  StockPickler.save(self, obj, save_persistent_id)
/home/sraja/mambaforge/envs/llm-mysteries/lib/python3.10/site-packages/dill/_dill.py:412: PicklingWarning: Cannot pickle <class '_ctypes.PyCFuncPtrType'>: _ctypes.PyCFuncPtrType has recursive self-references that trigger a RecursionError.
  StockPickler.save(self, obj, save_persistent_id)
Parameter 'function'=<function processCase at 0x7eff74156950> of the transform datasets.arrow_dataset.Dataset._map_single couldn't be hashed properly, a random hash was used instead. Make sure your transforms and parameters are serializable with pickle or dill for the dataset fingerprinting and caching to work. If you reuse this transform, the caching mechanism will consider it to be different from the previous calls and recompute everything. This warning is only showed once. Subsequent hashing failures won't be showed.
Map:   0%|          | 0/203 [00:00<?, ? examples/s]Map:   0%|          | 1/203 [01:00<3:23:35, 60.47s/ examples]Map:   1%|          | 2/203 [01:51<3:04:13, 54.99s/ examples]Map:   1%|▏         | 3/203 [02:48<3:06:20, 55.90s/ examples]Map:   2%|▏         | 4/203 [03:39<2:58:37, 53.86s/ examples]## 5minutemystery-who-let-the-frogs-out
Kyle Kravetsky is guilty: True or False?
True (0.8812066389307215)
Kyle Kravetsky has mean: True or False?
True (0.873646672673131)
Kyle Kravetsky has motive: True or False?
True (0.9708540445899615)
Kyle Kravetsky has opportunity: True or False?
True (0.8444089912414552)
Marnie Pepper is guilty: True or False?
True (0.9392480858026054)
Marnie Pepper has mean: True or False?
True (0.8875949368741688)
Marnie Pepper has motive: True or False?
True (0.9723097678630687)
Marnie Pepper has opportunity: True or False?
True (0.8710367026584496)
Matilda Robbens is guilty: True or False?
True (0.9467937951644804)
Matilda Robbens has mean: True or False?
True (0.7711548682745724)
Matilda Robbens has motive: True or False?
True (0.9802430864191416)
Matilda Robbens has opportunity: True or False?
True (0.85729086409805)
Sergio Ramos is guilty: True or False?
True (0.9628131975124238)
Sergio Ramos has mean: True or False?
True (0.9005298052062833)
Sergio Ramos has motive: True or False?
True (0.9647224545627199)
Sergio Ramos has opportunity: True or False?
True (0.9403530352223053)
### Kyle Kravetsky
- mean: False (0.126353327326869)
- motive: False (0.029145955410038504)
- opportunity: False (0.1555910087585448)

### Marnie Pepper
- mean: False (0.1124050631258312)
- motive: False (0.027690232136931336)
- opportunity: False (0.12896329734155043)

### Matilda Robbens
- mean: False (0.22884513172542764)
- motive: False (0.019756913580858404)
- opportunity: False (0.14270913590195)

### Sergio Ramos
- mean: True (0.9005298052062833)
- motive: True (0.9647224545627199)
- opportunity: True (0.9403530352223053)

The culprit is Sergio Ramos.
In fact, it is Matilda Robbens.
## 5minutemystery-uncle-buck-field-trip
Collin is guilty: True or False?
True (0.9390248079664695)
Collin has mean: True or False?
True (0.7988152492192591)
Collin has motive: True or False?
True (0.9796676048170913)
Collin has opportunity: True or False?
True (0.981021999947924)
Erica is guilty: True or False?
True (0.8951566249612815)
Erica has mean: True or False?
True (0.7217432334405754)
Erica has motive: True or False?
True (0.9733929040540585)
Erica has opportunity: True or False?
True (0.9339146041314464)
Rory is guilty: True or False?
True (0.9346342066470359)
Rory has mean: True or False?
True (0.8175744430556572)
Rory has motive: True or False?
True (0.9669764642537568)
Rory has opportunity: True or False?
True (0.9629528509146777)
Rusty is guilty: True or False?
True (0.9424007531919156)
Rusty has mean: True or False?
True (0.8140528237853677)
Rusty has motive: True or False?
True (0.9773275249708122)
Rusty has opportunity: True or False?
True (0.9522199020698944)
### Collin
- mean: True (0.7988152492192591)
- motive: True (0.9796676048170913)
- opportunity: True (0.981021999947924)

### Erica
- mean: False (0.27825676655942455)
- motive: False (0.02660709594594146)
- opportunity: False (0.06608539586855355)

### Rory
- mean: False (0.18242555694434281)
- motive: False (0.03302353574624317)
- opportunity: False (0.03704714908532225)

### Rusty
- mean: False (0.1859471762146323)
- motive: False (0.02267247502918779)
- opportunity: False (0.047780097930105625)

The culprit is Collin.
In fact, it is Rory.
## 5minutemystery-mystery-of-the-white-hats
Captain Stark is guilty: True or False?
True (0.9500415344497218)
Captain Stark has mean: True or False?
True (0.9127478016020363)
Captain Stark has motive: True or False?
True (0.9621076000160501)
Captain Stark has opportunity: True or False?
True (0.8795611817678315)
Chet is guilty: True or False?
True (0.9437636147996928)
Chet has mean: True or False?
True (0.8638517255508926)
Chet has motive: True or False?
True (0.9695556762577888)
Chet has opportunity: True or False?
True (0.8872045854516336)
Doug is guilty: True or False?
True (0.8980535302052036)
Doug has mean: True or False?
True (0.7074047371961694)
Doug has motive: True or False?
True (0.9599126594957205)
Doug has opportunity: True or False?
True (0.72951977676791)
Ernie is guilty: True or False?
True (0.8044059309478723)
Ernie has mean: True or False?
True (0.8140528237853677)
Ernie has motive: True or False?
True (0.8918110736745599)
Ernie has opportunity: True or False?
True (0.7662936378892937)
### Captain Stark
- mean: True (0.9127478016020363)
- motive: True (0.9621076000160501)
- opportunity: True (0.8795611817678315)

### Chet
- mean: False (0.13614827444910738)
- motive: False (0.030444323742211177)
- opportunity: False (0.11279541454836639)

### Doug
- mean: False (0.29259526280383064)
- motive: False (0.040087340504279534)
- opportunity: False (0.27048022323209)

### Ernie
- mean: False (0.1859471762146323)
- motive: False (0.10818892632544008)
- opportunity: False (0.23370636211070628)

The culprit is Captain Stark.
In fact, it is Chet.
## 5minutemystery-the-missing-popcorn
Private First Class Dicky Mosier is guilty: True or False?
True (0.9647224545627199)
Private First Class Dicky Mosier has mean: True or False?
True (0.9635062220717456)
Private First Class Dicky Mosier has motive: True or False?
True (0.9865458604248776)
Private First Class Dicky Mosier has opportunity: True or False?
True (0.9707432981083896)
Private Joe Locke is guilty: True or False?
True (0.9145963197706802)
Private Joe Locke has mean: True or False?
True (0.8951566249612815)
Private Joe Locke has motive: True or False?
True (0.9686195851543489)
Private Joe Locke has opportunity: True or False?
True (0.9418684262191025)
Specialist Fifth Class Ron Henson is guilty: True or False?
True (0.9449946880768697)
Specialist Fifth Class Ron Henson has mean: True or False?
True (0.9460011122282159)
Specialist Fifth Class Ron Henson has motive: True or False?
True (0.9795897010514905)
Specialist Fifth Class Ron Henson has opportunity: True or False?
True (0.9536218061663073)
Specialist Fourth Class Patrick Macnamara is guilty: True or False?
True (0.9401336308904421)
Specialist Fourth Class Patrick Macnamara has mean: True or False?
True (0.913058338092082)
Specialist Fourth Class Patrick Macnamara has motive: True or False?
True (0.9548162813994148)
Specialist Fourth Class Patrick Macnamara has opportunity: True or False?
True (0.8906751877407573)
### Private First Class Dicky Mosier
- mean: True (0.9635062220717456)
- motive: True (0.9865458604248776)
- opportunity: True (0.9707432981083896)

### Private Joe Locke
- mean: False (0.10484337503871854)
- motive: False (0.03138041484565113)
- opportunity: False (0.058131573780897505)

### Specialist Fifth Class Ron Henson
- mean: False (0.053998887771784077)
- motive: False (0.020410298948509542)
- opportunity: False (0.04637819383369268)

### Specialist Fourth Class Patrick Macnamara
- mean: False (0.08694166190791797)
- motive: False (0.04518371860058523)
- opportunity: False (0.10932481225924273)

The culprit is Private First Class Dicky Mosier.
In fact, it is Private Joe Locke.
## 5minutemystery-mystery-on-the-moor
Jack MacGinnis is guilty: True or False?
True (0.8633915828320894)
Jack MacGinnis has mean: True or False?
True (0.8838389494391541)
Jack MacGinnis has motive: True or False?
True (0.9444848881002107)
Jack MacGinnis has opportunity: True or False?
True (0.8433797899747144)
James Macready is guilty: True or False?
True (0.9476239083642972)
James Macready has mean: True or False?
True (0.9284088027271398)
James Macready has motive: True or False?
True (0.9641867858895684)
James Macready has opportunity: True or False?
True (0.9466953276900992)
Samuel Doone is guilty: True or False?
True (0.9372107968415931)
Samuel Doone has mean: True or False?
True (0.8210441512234701)
Samuel Doone has motive: True or False?
True (0.9594592463344039)
Samuel Doone has opportunity: True or False?
True (0.869271276026005)
Tom Jenkins is guilty: True or False?
True (0.9238675252821831)
Tom Jenkins has mean: True or False?
True (0.8822250371924163)
Tom Jenkins has motive: True or False?
True (0.9718859200238344)
Tom Jenkins has opportunity: True or False?
True (0.9224823132745662)
### Jack MacGinnis
- mean: False (0.11616105056084591)
- motive: False (0.055515111899789304)
- opportunity: False (0.1566202100252856)

Map:   2%|▏         | 5/203 [04:49<3:17:30, 59.85s/ examples]Map:   3%|▎         | 6/203 [06:30<4:02:09, 73.75s/ examples]Map:   3%|▎         | 7/203 [07:58<4:15:37, 78.25s/ examples]Map:   4%|▍         | 8/203 [09:03<4:01:27, 74.29s/ examples]Map:   4%|▍         | 9/203 [10:03<3:45:07, 69.62s/ examples]### James Macready
- mean: True (0.9284088027271398)
- motive: True (0.9641867858895684)
- opportunity: True (0.9466953276900992)

### Samuel Doone
- mean: False (0.17895584877652992)
- motive: False (0.04054075366559606)
- opportunity: False (0.13072872397399504)

### Tom Jenkins
- mean: False (0.1177749628075837)
- motive: False (0.02811407997616555)
- opportunity: False (0.0775176867254338)

The culprit is James Macready.
In fact, it is James Macready.
## 5minutemystery-who-stole-curious-george
Dexter is guilty: True or False?
True (0.8305941261447712)
Dexter has mean: True or False?
True (0.7988152492192591)
Dexter has motive: True or False?
True (0.9575961815839735)
Dexter has opportunity: True or False?
True (0.9531007408873468)
Mr. Ferguson is guilty: True or False?
True (0.854884620116169)
Mr. Ferguson has mean: True or False?
True (0.8895288123486662)
Mr. Ferguson has motive: True or False?
True (0.9655764090471975)
Mr. Ferguson has opportunity: True or False?
True (0.9127477403975288)
Mrs. Yee is guilty: True or False?
True (0.6187803740984554)
Mrs. Yee has mean: True or False?
True (0.6800292132037243)
Mrs. Yee has motive: True or False?
True (0.941654147692963)
Mrs. Yee has opportunity: True or False?
True (0.7779753136455794)
Skyler is guilty: True or False?
True (0.9374402785760423)
Skyler has mean: True or False?
True (0.8701565822173906)
Skyler has motive: True or False?
True (0.9789956218205105)
Skyler has opportunity: True or False?
True (0.9181872635464632)
### Dexter
- mean: False (0.20118475078074094)
- motive: False (0.04240381841602647)
- opportunity: False (0.04689925911265325)

### Mr. Ferguson
- mean: False (0.11047118765133379)
- motive: False (0.03442359095280245)
- opportunity: False (0.08725225960247118)

### Mrs. Yee
- mean: False (0.31997078679627566)
- motive: False (0.05834585230703704)
- opportunity: False (0.22202468635442063)

### Skyler
- mean: True (0.8701565822173906)
- motive: True (0.9789956218205105)
- opportunity: True (0.9181872635464632)

The culprit is Skyler.
In fact, it is Dexter.
## 5minutemystery-the-saxophones-ghost
Building Manager is guilty: True or False?
True (0.9894906286737151)
Building Manager has mean: True or False?
True (0.905989824801558)
Building Manager has motive: True or False?
True (0.9889064429708829)
Building Manager has opportunity: True or False?
True (0.9648551350350516)
Eric is guilty: True or False?
True (0.988038897570479)
Eric has mean: True or False?
True (0.7898827135821628)
Eric has motive: True or False?
True (0.9929609300067086)
Eric has opportunity: True or False?
True (0.9520419225082909)
Lenny is guilty: True or False?
True (0.9944773316650645)
Lenny has mean: True or False?
True (0.8423451152856819)
Lenny has motive: True or False?
True (0.9898106456437191)
Lenny has opportunity: True or False?
True (0.960804880888677)
Red is guilty: True or False?
True (0.9870296120305199)
Red has mean: True or False?
True (0.873646620599733)
Red has motive: True or False?
True (0.9859904643821331)
Red has opportunity: True or False?
True (0.9385759849623091)
### Building Manager
- mean: True (0.905989824801558)
- motive: True (0.9889064429708829)
- opportunity: True (0.9648551350350516)

### Eric
- mean: False (0.21011728641783722)
- motive: False (0.0070390699932914025)
- opportunity: False (0.047958077491709106)

### Lenny
- mean: False (0.1576548847143181)
- motive: False (0.010189354356280877)
- opportunity: False (0.03919511911132301)

### Red
- mean: False (0.12635337940026703)
- motive: False (0.014009535617866886)
- opportunity: False (0.061424015037690904)

The culprit is Building Manager.
In fact, it is Building Manager.
## 5minutemystery-who-shot-mom
Dad is guilty: True or False?
True (0.8944211616820568)
Dad has mean: True or False?
True (0.8879840376027315)
Dad has motive: True or False?
True (0.9693821664094352)
Dad has opportunity: True or False?
True (0.9488224997202508)
Randy is guilty: True or False?
True (0.9177460069915372)
Randy has mean: True or False?
True (0.8509647293237851)
Randy has motive: True or False?
True (0.990839004835608)
Randy has opportunity: True or False?
True (0.9672868242254096)
Roger is guilty: True or False?
True (0.8647679145346777)
Roger has mean: True or False?
True (0.7786493288700866)
Roger has motive: True or False?
True (0.9884696011429079)
Roger has opportunity: True or False?
True (0.9740426532811326)
Rory is guilty: True or False?
True (0.9237300750192418)
Rory has mean: True or False?
True (0.8856314413364714)
Rory has motive: True or False?
True (0.9897513984446356)
Rory has opportunity: True or False?
True (0.976310552041449)
### Dad
- mean: False (0.11201596239726852)
- motive: False (0.030617833590564802)
- opportunity: False (0.05117750027974921)

### Randy
- mean: False (0.14903527067621491)
- motive: False (0.00916099516439195)
- opportunity: False (0.03271317577459043)

### Roger
- mean: False (0.22135067112991336)
- motive: False (0.011530398857092061)
- opportunity: False (0.025957346718867402)

### Rory
- mean: True (0.8856314413364714)
- motive: True (0.9897513984446356)
- opportunity: True (0.976310552041449)

The culprit is Rory.
In fact, it is Randy.
## 5minutemystery-finding-the-flower-fund
James Faust is guilty: True or False?
True (0.9008790874146224)
James Faust has mean: True or False?
True (0.9354645628936168)
James Faust has motive: True or False?
True (0.9181873182746905)
James Faust has opportunity: True or False?
True (0.8795611817678315)
Justin Thorn is guilty: True or False?
True (0.904313027820426)
Justin Thorn has mean: True or False?
True (0.7049732238008671)
Justin Thorn has motive: True or False?
True (0.8854335555838845)
Justin Thorn has opportunity: True or False?
True (0.9564718616162037)
Lincoln Smith is guilty: True or False?
True (0.8679338697256817)
Lincoln Smith has mean: True or False?
True (0.7599387683150569)
Lincoln Smith has motive: True or False?
False (1.6827630606855486)
Lincoln Smith has opportunity: True or False?
True (0.9100670238942131)
Linda Hinton is guilty: True or False?
True (0.8539127077831877)
Linda Hinton has mean: True or False?
True (0.8140528237853677)
Linda Hinton has motive: True or False?
True (0.8349459127213729)
Linda Hinton has opportunity: True or False?
True (0.8198932995357624)
### James Faust
- mean: True (0.9354645628936168)
- motive: True (0.9181873182746905)
- opportunity: True (0.8795611817678315)

### Justin Thorn
- mean: False (0.29502677619913287)
- motive: False (0.11456644441611552)
- opportunity: False (0.04352813838379632)

### Lincoln Smith
- mean: False (0.2400612316849431)
- motive: False (1.6827630606855486)
- opportunity: False (0.08993297610578688)

### Linda Hinton
- mean: False (0.1859471762146323)
- motive: False (0.16505408727862714)
- opportunity: False (0.1801067004642376)

The culprit is James Faust.
In fact, it is Lincoln Smith.
## 5minutemystery-map-of-the-traitor
Benjamin is guilty: True or False?
True (0.9531007408873468)
Benjamin has mean: True or False?
True (0.7839884808423031)
Benjamin has motive: True or False?
True (0.9399133323582882)
Benjamin has opportunity: True or False?
True (0.9244152304846833)
Edward is guilty: True or False?
True (0.9759464267558225)
Edward has mean: True or False?
True (0.7386690954574974)
Edward has motive: True or False?
True (0.9758545755283039)
Edward has opportunity: True or False?
True (0.9355823382423648)
Jonathan is guilty: True or False?
True (0.9716717007848752)
Jonathan has mean: True or False?
True (0.9196425103002197)
Jonathan has motive: True or False?
True (0.9808393129553152)
Jonathan has opportunity: True or False?
True (0.9505947242503305)
Lucius is guilty: True or False?
True (0.9648551925449009)
Lucius has mean: True or False?
True (0.9309620852900756)
Lucius has motive: True or False?
True (0.9718859797630299)
Lucius has opportunity: True or False?
True (0.9196425651151865)
### Benjamin
- mean: False (0.2160115191576969)
- motive: False (0.06008666764171178)
- opportunity: False (0.07558476951531667)

### Edward
- mean: False (0.26133090454250263)
- motive: False (0.024145424471696098)
- opportunity: False (0.06441766175763519)

### Jonathan
Map:   5%|▍         | 10/203 [11:15<3:46:50, 70.52s/ examples]Map:   5%|▌         | 11/203 [12:31<3:50:25, 72.01s/ examples]Map:   6%|▌         | 12/203 [14:38<4:42:22, 88.70s/ examples]Map:   6%|▋         | 13/203 [15:58<4:32:31, 86.06s/ examples]Map:   7%|▋         | 14/203 [17:25<4:32:16, 86.44s/ examples]- mean: True (0.9196425103002197)
- motive: True (0.9808393129553152)
- opportunity: True (0.9505947242503305)

### Lucius
- mean: False (0.06903791470992438)
- motive: False (0.028114020236970072)
- opportunity: False (0.0803574348848135)

The culprit is Jonathan.
In fact, it is Jonathan.
## 5minutemystery-the-crusaders-robe
Captain Fosters is guilty: True or False?
True (0.9851575496109519)
Captain Fosters has mean: True or False?
True (0.9594592463344039)
Captain Fosters has motive: True or False?
True (0.9946255086819855)
Captain Fosters has opportunity: True or False?
True (0.9739437102411692)
Godefroi is guilty: True or False?
True (0.9623205675054309)
Godefroi has mean: True or False?
True (0.963368656065788)
Godefroi has motive: True or False?
True (0.9852430220637501)
Godefroi has opportunity: True or False?
True (0.972309708097824)
Morgan Grant is guilty: True or False?
True (0.9590009457171959)
Morgan Grant has mean: True or False?
True (0.8204694405411458)
Morgan Grant has motive: True or False?
True (0.9876400824622509)
Morgan Grant has opportunity: True or False?
True (0.9559813152103319)
Sir Francis Walters is guilty: True or False?
True (0.9666631825345839)
Sir Francis Walters has mean: True or False?
True (0.9291837815043049)
Sir Francis Walters has motive: True or False?
True (0.9902350305140533)
Sir Francis Walters has opportunity: True or False?
True (0.893681109060862)
### Captain Fosters
- mean: True (0.9594592463344039)
- motive: True (0.9946255086819855)
- opportunity: True (0.9739437102411692)

### Godefroi
- mean: False (0.03663134393421197)
- motive: False (0.01475697793624986)
- opportunity: False (0.02769029190217598)

### Morgan Grant
- mean: False (0.1795305594588542)
- motive: False (0.012359917537749121)
- opportunity: False (0.04401868478966808)

### Sir Francis Walters
- mean: False (0.07081621849569508)
- motive: False (0.00976496948594674)
- opportunity: False (0.10631889093913804)

The culprit is Captain Fosters.
In fact, it is Godefroi.
## 5minutemystery-mr-patricks-history-class
Corporal Tom Patrick is guilty: True or False?
True (0.7541915239138703)
Corporal Tom Patrick has mean: True or False?
True (0.5679366075542497)
Corporal Tom Patrick has motive: True or False?
True (0.7620701143808404)
Corporal Tom Patrick has opportunity: True or False?
True (0.7905302675820512)
Pvt. Billy Calhoun is guilty: True or False?
True (0.8354835531737983)
Pvt. Billy Calhoun has mean: True or False?
True (0.7364006034245382)
Pvt. Billy Calhoun has motive: True or False?
True (0.8879840376027315)
Pvt. Billy Calhoun has opportunity: True or False?
True (0.7599387683150569)
Pvt. Jack Trueblood is guilty: True or False?
True (0.8762113474663927)
Pvt. Jack Trueblood has mean: True or False?
True (0.7541915239138703)
Pvt. Jack Trueblood has motive: True or False?
True (0.8991214023999228)
Pvt. Jack Trueblood has opportunity: True or False?
True (0.8134607635851566)
Sgt. Patrick Culpepper is guilty: True or False?
True (0.8413047772878592)
Sgt. Patrick Culpepper has mean: True or False?
True (0.7468781552484828)
Sgt. Patrick Culpepper has motive: True or False?
True (0.7599387683150569)
Sgt. Patrick Culpepper has opportunity: True or False?
True (0.7122321792841629)
### Corporal Tom Patrick
- mean: False (0.4320633924457503)
- motive: False (0.23792988561915962)
- opportunity: False (0.20946973241794875)

### Pvt. Billy Calhoun
- mean: False (0.26359939657546183)
- motive: False (0.11201596239726852)
- opportunity: False (0.2400612316849431)

### Pvt. Jack Trueblood
- mean: True (0.7541915239138703)
- motive: True (0.8991214023999228)
- opportunity: True (0.8134607635851566)

### Sgt. Patrick Culpepper
- mean: False (0.2531218447515172)
- motive: False (0.2400612316849431)
- opportunity: False (0.28776782071583706)

The culprit is Pvt. Jack Trueblood.
In fact, it is Pvt. Billy Calhoun.
## 5minutemystery-bigfoot-mystery
Burt is guilty: True or False?
True (0.9284088027271398)
Burt has mean: True or False?
True (0.7950222460539826)
Burt has motive: True or False?
True (0.959077715892926)
Burt has opportunity: True or False?
True (0.9124361878432953)
Jerry is guilty: True or False?
True (0.879146760693242)
Jerry has mean: True or False?
True (0.6197014353942354)
Jerry has motive: True or False?
True (0.9313377150989219)
Jerry has opportunity: True or False?
True (0.8013146490010521)
Leng is guilty: True or False?
True (0.9372107968415931)
Leng has mean: True or False?
True (0.8216173667955227)
Leng has motive: True or False?
True (0.9310874934413855)
Leng has opportunity: True or False?
True (0.833324548637899)
Winston is guilty: True or False?
True (0.9400235399552953)
Winston has mean: True or False?
True (0.7394224480813394)
Winston has motive: True or False?
True (0.9543079730970608)
Winston has opportunity: True or False?
True (0.9230391416137353)
### Burt
- mean: True (0.7950222460539826)
- motive: True (0.959077715892926)
- opportunity: True (0.9124361878432953)

### Jerry
- mean: False (0.3802985646057646)
- motive: False (0.06866228490107806)
- opportunity: False (0.1986853509989479)

### Leng
- mean: False (0.17838263320447734)
- motive: False (0.06891250655861447)
- opportunity: False (0.16667545136210105)

### Winston
- mean: False (0.2605775519186606)
- motive: False (0.045692026902939165)
- opportunity: False (0.07696085838626465)

The culprit is Burt.
In fact, it is Jerry.
## 5minutemystery-missing-movie-money
Billy is guilty: True or False?
True (0.966726063403815)
Billy has mean: True or False?
True (0.9237300750192418)
Billy has motive: True or False?
True (0.9691494704322867)
Billy has opportunity: True or False?
True (0.9304582506719414)
Cody is guilty: True or False?
True (0.9433475737015985)
Cody has mean: True or False?
True (0.9095862487848758)
Cody has motive: True or False?
True (0.9541373270174538)
Cody has opportunity: True or False?
True (0.8975157733960666)
Juliet is guilty: True or False?
True (0.9015745518914653)
Juliet has mean: True or False?
True (0.9798997635332343)
Juliet has motive: True or False?
True (1.2907778613313514)
Juliet has opportunity: True or False?
True (0.9358173616900589)
Tammy is guilty: True or False?
True (0.944073857204818)
Tammy has mean: True or False?
True (0.9097468291312483)
Tammy has motive: True or False?
True (0.9110214697019103)
Tammy has opportunity: True or False?
True (0.8397339530959691)
### Billy
- mean: False (0.07626992498075824)
- motive: False (0.03085052956771328)
- opportunity: False (0.06954174932805857)

### Cody
- mean: False (0.09041375121512418)
- motive: False (0.045862672982546204)
- opportunity: False (0.10248422660393341)

### Juliet
- mean: True (0.9798997635332343)
- motive: True (1.2907778613313514)
- opportunity: True (0.9358173616900589)

### Tammy
- mean: False (0.09025317086875173)
- motive: False (0.08897853029808966)
- opportunity: False (0.1602660469040309)

The culprit is Juliet.
In fact, it is Cody.
## 5minutemystery-missing-ammunition
Henry is guilty: True or False?
True (0.8899121304559661)
Henry has mean: True or False?
True (0.9161096235973493)
Henry has motive: True or False?
True (0.9565531009888748)
Henry has opportunity: True or False?
True (0.9008791478232747)
Mr. Samuel is guilty: True or False?
True (0.7994423454932595)
Mr. Samuel has mean: True or False?
True (0.8740772044235984)
Mr. Samuel has motive: True or False?
True (0.9361683754137716)
Mr. Samuel has opportunity: True or False?
True (0.8444089912414552)
Mr. Smith is guilty: True or False?
True (0.9105454073245608)
Mr. Smith has mean: True or False?
True (0.8757870204368676)
Mr. Smith has motive: True or False?
True (0.9613164671024811)
Mr. Smith has opportunity: True or False?
True (0.8647679660788636)
Young Soldier is guilty: True or False?
True (0.9730876681996075)
Young Soldier has mean: True or False?
True (0.9608048200409682)
Young Soldier has motive: True or False?
True (0.9762200121234286)
Young Soldier has opportunity: True or False?
True (0.9263037480179213)
### Henry
- mean: False (0.08389037640265073)
- motive: False (0.043446899011125195)
- opportunity: False (0.09912085217672528)

### Mr. Samuel
- mean: False (0.12592279557640162)
Map:   7%|▋         | 15/203 [18:35<4:15:33, 81.56s/ examples]Map:   8%|▊         | 16/203 [20:12<4:28:58, 86.30s/ examples]Map:   8%|▊         | 17/203 [21:30<4:19:10, 83.60s/ examples]Map:   9%|▉         | 18/203 [23:14<4:37:13, 89.91s/ examples]Map:   9%|▉         | 19/203 [24:49<4:40:14, 91.38s/ examples]- motive: False (0.06383162458622837)
- opportunity: False (0.1555910087585448)

### Mr. Smith
- mean: False (0.12421297956313238)
- motive: False (0.03868353289751891)
- opportunity: False (0.13523203392113636)

### Young Soldier
- mean: True (0.9608048200409682)
- motive: True (0.9762200121234286)
- opportunity: True (0.9263037480179213)

The culprit is Young Soldier.
In fact, it is Henry.
## 5minutemystery-the-sky-sleuths
Bug collector is guilty: True or False?
True (0.9767359492645185)
Bug collector has mean: True or False?
True (0.8652240590801695)
Bug collector has motive: True or False?
True (0.9639839524564597)
Bug collector has opportunity: True or False?
True (0.91789335161495)
Elderly man is guilty: True or False?
True (0.987350642725576)
Elderly man has mean: True or False?
True (0.9113376113103917)
Elderly man has motive: True or False?
True (0.974580348460635)
Elderly man has opportunity: True or False?
True (0.9704086780234861)
Family man is guilty: True or False?
True (0.9682614213403071)
Family man has mean: True or False?
True (0.883437276390578)
Family man has motive: True or False?
True (0.9509603391767795)
Family man has opportunity: True or False?
True (0.9281486838603771)
Motorcyclist is guilty: True or False?
True (0.9793540841590924)
Motorcyclist has mean: True or False?
True (0.9328214561580316)
Motorcyclist has motive: True or False?
True (0.975059748401155)
Motorcyclist has opportunity: True or False?
True (0.9513234509300917)
### Bug collector
- mean: False (0.13477594091983047)
- motive: False (0.036016047543540264)
- opportunity: False (0.08210664838505)

### Elderly man
- mean: False (0.0886623886896083)
- motive: False (0.025419651539364985)
- opportunity: False (0.02959132197651393)

### Family man
- mean: False (0.11656272360942199)
- motive: False (0.04903966082322053)
- opportunity: False (0.07185131613962292)

### Motorcyclist
- mean: True (0.9328214561580316)
- motive: True (0.975059748401155)
- opportunity: True (0.9513234509300917)

The culprit is Motorcyclist.
In fact, it is Bug collector.
## 5minutemystery-battle-of-the-bulge
Anderson is guilty: True or False?
True (0.9614614837165661)
Anderson has mean: True or False?
True (0.7613610520273686)
Anderson has motive: True or False?
True (0.9364014251476122)
Anderson has opportunity: True or False?
True (0.8563323578093363)
Dilworth is guilty: True or False?
True (0.9761291751471208)
Dilworth has mean: True or False?
True (0.7476159279883341)
Dilworth has motive: True or False?
True (0.9438672063066703)
Dilworth has opportunity: True or False?
True (0.8477157335881546)
Maguire is guilty: True or False?
True (0.9530133616438526)
Maguire has mean: True or False?
True (0.6723316913929156)
Maguire has motive: True or False?
True (0.9020932932190145)
Maguire has opportunity: True or False?
True (0.8050197941712954)
Siegel is guilty: True or False?
True (0.9488224997202508)
Siegel has mean: True or False?
True (0.6224593484250324)
Siegel has motive: True or False?
True (0.944279730201317)
Siegel has opportunity: True or False?
True (0.8697145551802641)
### Anderson
- mean: True (0.7613610520273686)
- motive: True (0.9364014251476122)
- opportunity: True (0.8563323578093363)

### Dilworth
- mean: False (0.2523840720116659)
- motive: False (0.056132793693329686)
- opportunity: False (0.15228426641184545)

### Maguire
- mean: False (0.3276683086070844)
- motive: False (0.09790670678098545)
- opportunity: False (0.19498020582870457)

### Siegel
- mean: False (0.37754065157496763)
- motive: False (0.05572026979868305)
- opportunity: False (0.13028544481973592)

The culprit is Anderson.
In fact, it is Dilworth.
## 5minutemystery-the-missing-button
Eliza Murray is guilty: True or False?
True (0.9532750830575984)
Eliza Murray has mean: True or False?
True (0.7461389980806673)
Eliza Murray has motive: True or False?
True (0.9616060242722225)
Eliza Murray has opportunity: True or False?
True (0.9422947179693436)
George Sanders is guilty: True or False?
True (0.9626028535101038)
George Sanders has mean: True or False?
True (0.8987665204865408)
George Sanders has motive: True or False?
True (0.9761291751471208)
George Sanders has opportunity: True or False?
True (0.9175985492877378)
Stable boy Ian is guilty: True or False?
True (0.9720986492264091)
Stable boy Ian has mean: True or False?
True (0.9346342693191454)
Stable boy Ian has motive: True or False?
True (0.9883352519517842)
Stable boy Ian has opportunity: True or False?
True (0.9783846739081675)
Thomas Murray is guilty: True or False?
True (0.925499741040984)
Thomas Murray has mean: True or False?
True (0.5631377056275331)
Thomas Murray has motive: True or False?
True (0.9425067301242699)
Thomas Murray has opportunity: True or False?
True (0.7065955344877805)
### Eliza Murray
- mean: False (0.2538610019193327)
- motive: False (0.038393975727777474)
- opportunity: False (0.05770528203065639)

### George Sanders
- mean: False (0.10123347951345918)
- motive: False (0.02387082485287917)
- opportunity: False (0.08240145071226224)

### Stable boy Ian
- mean: True (0.9346342693191454)
- motive: True (0.9883352519517842)
- opportunity: True (0.9783846739081675)

### Thomas Murray
- mean: False (0.43686229437246693)
- motive: False (0.05749326987573011)
- opportunity: False (0.29340446551221955)

The culprit is Stable boy Ian.
In fact, it is Stable boy Ian.
## 5minutemystery-the-railroad-mystery
Alvarado is guilty: True or False?
True (0.8998277183078867)
Alvarado has mean: True or False?
True (0.6531268925247615)
Alvarado has motive: True or False?
True (0.922412458454602)
Alvarado has opportunity: True or False?
True (0.8610715240899957)
The engineer is guilty: True or False?
True (0.7911764307711107)
The engineer has mean: True or False?
True (0.6123096993178739)
The engineer has motive: True or False?
True (0.6352225075752841)
The engineer has opportunity: True or False?
True (0.8504686406728537)
The mechanic is guilty: True or False?
True (0.8803862939824989)
The mechanic has mean: True or False?
True (0.7333563569098757)
The mechanic has motive: True or False?
True (0.8193157928301305)
The mechanic has opportunity: True or False?
True (0.8940517282497483)
Zebediah is guilty: True or False?
True (0.893681109060862)
Zebediah has mean: True or False?
True (0.6020615685826383)
Zebediah has motive: True or False?
True (0.8407825844829613)
Zebediah has opportunity: True or False?
True (0.7364006034245382)
### Alvarado
- mean: False (0.3468731074752385)
- motive: False (0.07758754154539804)
- opportunity: False (0.13892847591000435)

### The engineer
- mean: False (0.38769030068212607)
- motive: False (0.3647774924247159)
- opportunity: False (0.14953135932714634)

### The mechanic
- mean: True (0.7333563569098757)
- motive: True (0.8193157928301305)
- opportunity: True (0.8940517282497483)

### Zebediah
- mean: False (0.39793843141736174)
- motive: False (0.15921741551703872)
- opportunity: False (0.26359939657546183)

The culprit is The mechanic.
In fact, it is Zebediah.
## 5minutemystery-the-date
Bob is guilty: True or False?
True (0.8415653745537904)
Bob has mean: True or False?
True (0.7283620328527746)
Bob has motive: True or False?
True (0.9705206155895632)
Bob has opportunity: True or False?
True (0.8978744762836591)
Cynthia is guilty: True or False?
True (0.8994751578343994)
Cynthia has mean: True or False?
True (0.6757646168022439)
Cynthia has motive: True or False?
True (0.9666631825345839)
Cynthia has opportunity: True or False?
True (0.8895288123486662)
Diane is guilty: True or False?
True (0.8587185689177256)
Diane has mean: True or False?
True (0.7490872087035162)
Diane has motive: True or False?
True (0.9657707197858371)
Diane has opportunity: True or False?
True (0.84440905415483)
Kristin is guilty: True or False?
True (0.9012274173198201)
Kristin has mean: True or False?
True (0.8116760258690822)
Kristin has motive: True or False?
True (0.9783846739081675)
Kristin has opportunity: True or False?
True (0.9187722208906307)
### Bob
- mean: False (0.27163796714722543)
- motive: False (0.02947938441043685)
- opportunity: False (0.10212552371634087)

### Cynthia
- mean: False (0.32423538319775613)
Map:  10%|▉         | 20/203 [26:12<4:30:45, 88.77s/ examples]Map:  10%|█         | 21/203 [27:25<4:15:10, 84.12s/ examples]Map:  11%|█         | 22/203 [29:03<4:26:37, 88.38s/ examples]Map:  11%|█▏        | 23/203 [30:09<4:04:39, 81.55s/ examples]Map:  12%|█▏        | 24/203 [31:16<3:50:36, 77.30s/ examples]- motive: False (0.03333681746541606)
- opportunity: False (0.11047118765133379)

### Diane
- mean: False (0.2509127912964838)
- motive: False (0.03422928021416294)
- opportunity: False (0.15559094584516997)

### Kristin
- mean: True (0.8116760258690822)
- motive: True (0.9783846739081675)
- opportunity: True (0.9187722208906307)

The culprit is Kristin.
In fact, it is Bob.
## 5minutemystery-b-movie-murder
Angela is guilty: True or False?
True (0.9563904403130185)
Angela has mean: True or False?
True (0.8338664756137771)
Angela has motive: True or False?
True (0.9673486357359453)
Angela has opportunity: True or False?
True (0.9473810211532727)
Debbie is guilty: True or False?
True (0.9831822505619944)
Debbie has mean: True or False?
True (0.8354835531737983)
Debbie has motive: True or False?
True (0.9891186952035905)
Debbie has opportunity: True or False?
True (0.9768465751854355)
Sal is guilty: True or False?
True (0.9594593035226332)
Sal has mean: True or False?
True (0.8370879250561812)
Sal has motive: True or False?
True (0.9788343902147806)
Sal has opportunity: True or False?
True (0.9603611816439128)
Tom is guilty: True or False?
True (0.9655114412719658)
Tom has mean: True or False?
True (0.8626990386916318)
Tom has motive: True or False?
True (0.9782603970717496)
Tom has opportunity: True or False?
True (0.967471776843259)
### Angela
- mean: False (0.16613352438622286)
- motive: False (0.03265136426405468)
- opportunity: False (0.05261897884672728)

### Debbie
- mean: False (0.1645164468262017)
- motive: False (0.010881304796409474)
- opportunity: False (0.023153424814564505)

### Sal
- mean: False (0.16291207494381876)
- motive: False (0.02116560978521942)
- opportunity: False (0.03963881835608718)

### Tom
- mean: True (0.8626990386916318)
- motive: True (0.9782603970717496)
- opportunity: True (0.967471776843259)

The culprit is Tom.
In fact, it is Angela.
## 5minutemystery-the-jackie-mitchell-autographed-baseball-mystery
Dr. Edgar Newton is guilty: True or False?
True (0.9252299659402181)
Dr. Edgar Newton has mean: True or False?
True (0.8914335992201801)
Dr. Edgar Newton has motive: True or False?
True (0.9829218988549058)
Dr. Edgar Newton has opportunity: True or False?
True (0.9069831945855868)
Melinda Baker is guilty: True or False?
True (0.934872446722342)
Melinda Baker has mean: True or False?
True (0.9381240005131491)
Melinda Baker has motive: True or False?
True (0.9842154375736257)
Melinda Baker has opportunity: True or False?
True (0.8940517282497483)
Simon Plympton is guilty: True or False?
True (0.9928786157528565)
Simon Plympton has mean: True or False?
True (0.9740426532811326)
Simon Plympton has motive: True or False?
True (0.9959139822439478)
Simon Plympton has opportunity: True or False?
True (0.9710742839974638)
Susan Plympton is guilty: True or False?
True (0.9781354673766767)
Susan Plympton has mean: True or False?
True (0.8807970862580315)
Susan Plympton has motive: True or False?
True (0.9915870428475455)
Susan Plympton has opportunity: True or False?
True (0.8418256636710214)
### Dr. Edgar Newton
- mean: False (0.10856640077981994)
- motive: False (0.017078101145094227)
- opportunity: False (0.09301680541441315)

### Melinda Baker
- mean: False (0.06187599948685085)
- motive: False (0.01578456242637427)
- opportunity: False (0.10594827175025168)

### Simon Plympton
- mean: True (0.9740426532811326)
- motive: True (0.9959139822439478)
- opportunity: True (0.9710742839974638)

### Susan Plympton
- mean: False (0.11920291374196845)
- motive: False (0.008412957152454492)
- opportunity: False (0.1581743363289786)

The culprit is Simon Plympton.
In fact, it is Susan Plympton.
## 5minutemystery-the-easter-egg-mystery
Anna is guilty: True or False?
True (0.8354835531737983)
Anna has mean: True or False?
False (0.6343168082332088)
Anna has motive: True or False?
True (0.8392075831473667)
Anna has opportunity: True or False?
True (0.8820220178442959)
Cole is guilty: True or False?
True (0.8799743689174987)
Cole has mean: True or False?
False (0.685107355950278)
Cole has motive: True or False?
True (0.7613610520273686)
Cole has opportunity: True or False?
True (0.8019357965963964)
Justin is guilty: True or False?
True (0.924959242644946)
Justin has mean: True or False?
True (0.612309626324874)
Justin has motive: True or False?
True (0.9100669628694658)
Justin has opportunity: True or False?
True (0.892187358563457)
Lizzie is guilty: True or False?
True (0.9329437018480795)
Lizzie has mean: True or False?
True (0.6688802830862913)
Lizzie has motive: True or False?
True (0.8899121304559661)
Lizzie has opportunity: True or False?
True (0.8596637206861489)
Rachel is guilty: True or False?
True (0.8732148436000907)
Rachel has mean: True or False?
False (0.5496406074054949)
Rachel has motive: True or False?
True (0.7972412725773819)
Rachel has opportunity: True or False?
True (0.7106283339569771)
### Anna
- mean: False (0.6343168082332088)
- motive: False (0.16079241685263335)
- opportunity: False (0.1179779821557041)

### Cole
- mean: False (0.685107355950278)
- motive: False (0.2386389479726314)
- opportunity: False (0.19806420340360364)

### Justin
- mean: False (0.38769037367512604)
- motive: False (0.08993303713053424)
- opportunity: False (0.10781264143654301)

### Lizzie
- mean: True (0.6688802830862913)
- motive: True (0.8899121304559661)
- opportunity: True (0.8596637206861489)

### Rachel
- mean: False (0.5496406074054949)
- motive: False (0.20275872742261813)
- opportunity: False (0.2893716660430229)

The culprit is Lizzie.
In fact, it is Lizzie.
## 5minutemystery-easter-rhyme
Abbott is guilty: True or False?
True (0.6415346823638186)
Abbott has mean: True or False?
True (0.7025300310583819)
Abbott has motive: True or False?
True (0.6859494535376744)
Abbott has opportunity: True or False?
True (0.6984323202883935)
Andy is guilty: True or False?
True (0.6076631662366868)
Andy has mean: True or False?
True (0.5204963206682631)
Andy has motive: True or False?
True (0.5448013654847448)
Andy has opportunity: True or False?
True (0.6011253583932805)
Randy is guilty: True or False?
True (0.6992543888266708)
Randy has mean: True or False?
True (0.6918097054250644)
Randy has motive: True or False?
True (0.6918097672776748)
Randy has opportunity: True or False?
True (0.6540113633452196)
Speedy is guilty: True or False?
True (0.673191669892235)
Speedy has mean: True or False?
True (0.6601723415572317)
Speedy has motive: True or False?
True (0.6311396940785249)
Speedy has opportunity: True or False?
True (0.6347697233822684)
### Abbott
- mean: True (0.7025300310583819)
- motive: True (0.6859494535376744)
- opportunity: True (0.6984323202883935)

### Andy
- mean: False (0.4795036793317369)
- motive: False (0.4551986345152552)
- opportunity: False (0.3988746416067195)

### Randy
- mean: False (0.30819029457493563)
- motive: False (0.30819023272232515)
- opportunity: False (0.3459886366547804)

### Speedy
- mean: False (0.3398276584427683)
- motive: False (0.3688603059214751)
- opportunity: False (0.36523027661773155)

The culprit is Abbott.
In fact, it is Speedy.
## 5minutemystery-the-april-fool
Boston, MA is guilty: True or False?
True (0.8940517282497483)
Boston, MA has mean: True or False?
True (0.9504109622144332)
Boston, MA has motive: True or False?
True (0.948346255948953)
Boston, MA has opportunity: True or False?
True (0.9139840578860137)
Philadelphia, PA is guilty: True or False?
True (0.9529258022651363)
Philadelphia, PA has mean: True or False?
True (0.9433475737015985)
Philadelphia, PA has motive: True or False?
True (0.9629528509146777)
Philadelphia, PA has opportunity: True or False?
True (0.9268352400785028)
Pittsburgh, PA is guilty: True or False?
True (0.9515039936355008)
Pittsburgh, PA has mean: True or False?
True (0.9563089012524633)
Pittsburgh, PA has motive: True or False?
True (0.9689738746693873)
Pittsburgh, PA has opportunity: True or False?
True (0.9575961815839735)
Raleigh, NC is guilty: True or False?
True (0.92386746333204)
Raleigh, NC has mean: True or False?
True (0.9302050495103452)
Raleigh, NC has motive: True or False?
True (0.9458013187522837)
Raleigh, NC has opportunity: True or False?Map:  12%|█▏        | 25/203 [32:46<3:59:51, 80.85s/ examples]Map:  13%|█▎        | 26/203 [34:00<3:53:04, 79.01s/ examples]Map:  13%|█▎        | 27/203 [35:10<3:43:37, 76.23s/ examples]Map:  14%|█▍        | 28/203 [36:36<3:50:44, 79.11s/ examples]Map:  14%|█▍        | 29/203 [38:01<3:54:15, 80.78s/ examples]
True (0.8984105001507761)
Washington, DC is guilty: True or False?
True (0.9063219998220023)
Washington, DC has mean: True or False?
True (0.9039744767757508)
Washington, DC has motive: True or False?
True (0.9386885150411723)
Washington, DC has opportunity: True or False?
True (0.9183338853275215)
### Boston, MA
- mean: False (0.04958903778556678)
- motive: False (0.051653744051046946)
- opportunity: False (0.08601594211398633)

### Philadelphia, PA
- mean: False (0.056652426298401504)
- motive: False (0.03704714908532225)
- opportunity: False (0.07316475992149718)

### Pittsburgh, PA
- mean: True (0.9563089012524633)
- motive: True (0.9689738746693873)
- opportunity: True (0.9575961815839735)

### Raleigh, NC
- mean: False (0.06979495048965478)
- motive: False (0.05419868124771632)
- opportunity: False (0.10158949984922394)

### Washington, DC
- mean: False (0.09602552322424918)
- motive: False (0.061311484958827656)
- opportunity: False (0.08166611467247853)

The culprit is Pittsburgh, PA.
In fact, it is Washington, DC.
## 5minutemystery-green-feet
Carm is guilty: True or False?
True (0.8933094122075369)
Carm has mean: True or False?
True (0.7819973291046377)
Carm has motive: True or False?
True (0.9192084645335399)
Carm has opportunity: True or False?
True (0.8397339530959691)
Diane is guilty: True or False?
True (0.9064877041303855)
Diane has mean: True or False?
True (0.8464508054137014)
Diane has motive: True or False?
True (0.9265699426348812)
Diane has opportunity: True or False?
True (0.9142907234091052)
Jen is guilty: True or False?
True (0.9233162440500982)
Jen has mean: True or False?
True (0.8402589628813668)
Jen has motive: True or False?
True (0.9494823209990744)
Jen has opportunity: True or False?
True (0.8969755785184792)
Maureen is guilty: True or False?
True (0.8624675215861032)
Maureen has mean: True or False?
True (0.816406362162552)
Maureen has motive: True or False?
True (0.9122799654606127)
Maureen has opportunity: True or False?
True (0.911809984585868)
### Carm
- mean: False (0.2180026708953623)
- motive: False (0.08079153546646012)
- opportunity: False (0.1602660469040309)

### Diane
- mean: True (0.8464508054137014)
- motive: True (0.9265699426348812)
- opportunity: True (0.9142907234091052)

### Jen
- mean: False (0.1597410371186332)
- motive: False (0.05051767900092563)
- opportunity: False (0.1030244214815208)

### Maureen
- mean: False (0.18359363783744798)
- motive: False (0.08772003453938726)
- opportunity: False (0.08819001541413196)

The culprit is Diane.
In fact, it is Diane.
## 5minutemystery-restaurant-roulette
Atsushi Nishi is guilty: True or False?
True (0.9832144969671855)
Atsushi Nishi has mean: True or False?
True (0.9374402785760423)
Atsushi Nishi has motive: True or False?
True (0.9747251273624444)
Atsushi Nishi has opportunity: True or False?
True (0.9381240005131491)
Gianni Girodano is guilty: True or False?
True (0.928538502080124)
Gianni Girodano has mean: True or False?
True (0.802555560073231)
Gianni Girodano has motive: True or False?
True (0.8864204283224634)
Gianni Girodano has opportunity: True or False?
True (0.7074046739492601)
Jack McDonald is guilty: True or False?
True (0.9461008327071723)
Jack McDonald has mean: True or False?
True (0.9095863097773887)
Jack McDonald has motive: True or False?
True (0.9777563211328246)
Jack McDonald has opportunity: True or False?
True (0.8816148581338575)
Jean-Pierre Dubois is guilty: True or False?
True (0.9517736433770346)
Jean-Pierre Dubois has mean: True or False?
True (0.950777887812089)
Jean-Pierre Dubois has motive: True or False?
True (0.9487275499225403)
Jean-Pierre Dubois has opportunity: True or False?
True (0.8787311338092536)
### Atsushi Nishi
- mean: True (0.9374402785760423)
- motive: True (0.9747251273624444)
- opportunity: True (0.9381240005131491)

### Gianni Girodano
- mean: False (0.19744443992676897)
- motive: False (0.11357957167753663)
- opportunity: False (0.2925953260507399)

### Jack McDonald
- mean: False (0.09041369022261125)
- motive: False (0.022243678867175376)
- opportunity: False (0.11838514186614246)

### Jean-Pierre Dubois
- mean: False (0.04922211218791095)
- motive: False (0.05127245007745973)
- opportunity: False (0.1212688661907464)

The culprit is Atsushi Nishi.
In fact, it is Gianni Girodano.
## 5minutemystery-violating-the-pirate-code
Bosun Ridley is guilty: True or False?
True (0.9385759849623091)
Bosun Ridley has mean: True or False?
True (0.8261514850267767)
Bosun Ridley has motive: True or False?
True (0.9244151684978138)
Bosun Ridley has opportunity: True or False?
True (0.8868131040663721)
Mr Arbuthnot is guilty: True or False?
True (0.9745319483890362)
Mr Arbuthnot has mean: True or False?
True (0.9022656660556747)
Mr Arbuthnot has motive: True or False?
True (0.9892441036318841)
Mr Arbuthnot has opportunity: True or False?
True (0.9579122665190904)
Nehemiah is guilty: True or False?
True (0.9564718010429047)
Nehemiah has mean: True or False?
True (0.8860265005470086)
Nehemiah has motive: True or False?
True (0.9770663977543804)
Nehemiah has opportunity: True or False?
True (0.9206470837359207)
Will is guilty: True or False?
True (0.9646559343002779)
Will has mean: True or False?
True (0.9337940192482527)
Will has motive: True or False?
True (0.982724071443633)
Will has opportunity: True or False?
True (0.9637117373129486)
### Bosun Ridley
- mean: False (0.1738485149732233)
- motive: False (0.0755848315021862)
- opportunity: False (0.11318689593362785)

### Mr Arbuthnot
- mean: False (0.09773433394432529)
- motive: False (0.010755896368115914)
- opportunity: False (0.04208773348090955)

### Nehemiah
- mean: False (0.1139734994529914)
- motive: False (0.022933602245619578)
- opportunity: False (0.07935291626407925)

### Will
- mean: True (0.9337940192482527)
- motive: True (0.982724071443633)
- opportunity: True (0.9637117373129486)

The culprit is Will.
In fact, it is Bosun Ridley.
## 5minutemystery-space-station-sagittarius-six-suffers-sabotage
Cpl. Bennington is guilty: True or False?
True (0.9302050495103452)
Cpl. Bennington has mean: True or False?
True (0.8187367896794966)
Cpl. Bennington has motive: True or False?
True (0.9618933789072692)
Cpl. Bennington has opportunity: True or False?
True (0.9447913165152162)
Scrivine is guilty: True or False?
True (0.9458013187522837)
Scrivine has mean: True or False?
True (0.8415654247149972)
Scrivine has motive: True or False?
True (0.9515039936355008)
Scrivine has opportunity: True or False?
True (0.9252299659402181)
Sgt. O'Hennessey is guilty: True or False?
True (0.927887794449634)
Sgt. O'Hennessey has mean: True or False?
True (0.767689835247798)
Sgt. O'Hennessey has motive: True or False?
True (0.9559813721912603)
Sgt. O'Hennessey has opportunity: True or False?
True (0.927099763868178)
Sgt.Valance is guilty: True or False?
True (0.9736947425622681)
Sgt.Valance has mean: True or False?
True (0.8300437877296776)
Sgt.Valance has motive: True or False?
True (0.9598374351134399)
Sgt.Valance has opportunity: True or False?
True (0.9022656660556747)
### Cpl. Bennington
- mean: True (0.8187367896794966)
- motive: True (0.9618933789072692)
- opportunity: True (0.9447913165152162)

### Scrivine
- mean: False (0.15843457528500282)
- motive: False (0.048496006364499245)
- opportunity: False (0.07477003405978189)

### Sgt. O'Hennessey
- mean: False (0.232310164752202)
- motive: False (0.04401862780873966)
- opportunity: False (0.07290023613182195)

### Sgt.Valance
- mean: False (0.16995621227032243)
- motive: False (0.040162564886560115)
- opportunity: False (0.09773433394432529)

The culprit is Cpl. Bennington.
In fact, it is Sgt.Valance.
## 5minutemystery-flying-saucer-of-new-mexico
Dora is guilty: True or False?
True (0.9773275850444884)
Dora has mean: True or False?
True (0.9029524325377104)
Dora has motive: True or False?
True (0.9683812839782183)
Dora has opportunity: True or False?
True (0.8872045854516336)
Lester is guilty: True or False?
True (0.9892752166033384)
Lester has mean: True or False?
True (0.9614615446058614)
Lester has motive: True or False?
True (0.9903430339413316)
Lester has opportunity: True or False?
True (0.9565531009888748)
Map:  15%|█▍        | 30/203 [39:21<3:52:45, 80.73s/ examples]Map:  15%|█▌        | 31/203 [40:59<4:06:26, 85.97s/ examples]Map:  16%|█▌        | 32/203 [42:47<4:23:16, 92.38s/ examples]Map:  16%|█▋        | 33/203 [44:07<4:11:36, 88.81s/ examples]Map:  17%|█▋        | 34/203 [45:33<4:07:33, 87.89s/ examples]Uncle Art is guilty: True or False?
True (0.966726063403815)
Uncle Art has mean: True or False?
True (0.9274947043807324)
Uncle Art has motive: True or False?
True (0.9736947425622681)
Uncle Art has opportunity: True or False?
True (0.9329437018480795)
Zach is guilty: True or False?
True (0.96920782287766)
Zach has mean: True or False?
True (0.8951566249612815)
Zach has motive: True or False?
True (0.9606574760904091)
Zach has opportunity: True or False?
True (0.8982321647536474)
### Dora
- mean: False (0.0970475674622896)
- motive: False (0.03161871602178168)
- opportunity: False (0.11279541454836639)

### Lester
- mean: True (0.9614615446058614)
- motive: True (0.9903430339413316)
- opportunity: True (0.9565531009888748)

### Uncle Art
- mean: False (0.07250529561926755)
- motive: False (0.026305257437731933)
- opportunity: False (0.06705629815192049)

### Zach
- mean: False (0.10484337503871854)
- motive: False (0.03934252390959092)
- opportunity: False (0.10176783524635258)

The culprit is Lester.
In fact, it is Dora.
## 5minutemystery-great-musket-mystery
Lyle Day is guilty: True or False?
True (0.9532750262379774)
Lyle Day has mean: True or False?
True (0.9184802773231918)
Lyle Day has motive: True or False?
True (0.9653158197836269)
Lyle Day has opportunity: True or False?
True (0.8998277786460391)
Mary Wright is guilty: True or False?
True (0.925499741040984)
Mary Wright has mean: True or False?
True (0.9026095892260383)
Mary Wright has motive: True or False?
True (0.9537081113927965)
Mary Wright has opportunity: True or False?
True (0.9534487112250288)
Paul Revere is guilty: True or False?
True (0.9443823686645129)
Paul Revere has mean: True or False?
True (0.8973360043541736)
Paul Revere has motive: True or False?
True (0.9203612233366507)
Paul Revere has opportunity: True or False?
True (0.9237300130783155)
Stevie Brown is guilty: True or False?
True (0.9494823209990744)
Stevie Brown has mean: True or False?
True (0.9746769070949022)
Stevie Brown has motive: True or False?
True (0.9655114412719658)
Stevie Brown has opportunity: True or False?
True (0.9400235399552953)
### Lyle Day
- mean: False (0.08151972267680818)
- motive: False (0.034684180216373095)
- opportunity: False (0.10017222135396087)

### Mary Wright
- mean: False (0.09739041077396171)
- motive: False (0.04629188860720346)
- opportunity: False (0.04655128877497117)

### Paul Revere
- mean: False (0.1026639956458264)
- motive: False (0.07963877666334929)
- opportunity: False (0.07626998692168452)

### Stevie Brown
- mean: True (0.9746769070949022)
- motive: True (0.9655114412719658)
- opportunity: True (0.9400235399552953)

The culprit is Stevie Brown.
In fact, it is Lyle Day.
## 5minutemystery-true-green-a-st-patricks-day-mystery
Emily Carpenter is guilty: True or False?
True (0.8519527857346616)
Emily Carpenter has mean: True or False?
True (0.7114308541703346)
Emily Carpenter has motive: True or False?
True (0.9320833668388808)
Emily Carpenter has opportunity: True or False?
True (0.7655933544531522)
Evan Carpenter is guilty: True or False?
True (0.9041439284393449)
Evan Carpenter has mean: True or False?
True (0.6757646168022439)
Evan Carpenter has motive: True or False?
True (0.9528381834886748)
Evan Carpenter has opportunity: True or False?
True (0.8392075831473667)
Richie Harris is guilty: True or False?
True (0.8267117710471246)
Richie Harris has mean: True or False?
True (0.6967842494573921)
Richie Harris has motive: True or False?
True (0.914290668913133)
Richie Harris has opportunity: True or False?
True (0.8255897087847518)
Zachary MacDonald is guilty: True or False?
True (0.8469578650997759)
Zachary MacDonald has mean: True or False?
True (0.5879430860094185)
Zachary MacDonald has motive: True or False?
True (0.9237300750192418)
Zachary MacDonald has opportunity: True or False?
True (0.7416740115009234)
### Emily Carpenter
- mean: False (0.2885691458296654)
- motive: False (0.06791663316111918)
- opportunity: False (0.23440664554684776)

### Evan Carpenter
- mean: True (0.6757646168022439)
- motive: True (0.9528381834886748)
- opportunity: True (0.8392075831473667)

### Richie Harris
- mean: False (0.30321575054260785)
- motive: False (0.08570933108686696)
- opportunity: False (0.1744102912152482)

### Zachary MacDonald
- mean: False (0.41205691399058153)
- motive: False (0.07626992498075824)
- opportunity: False (0.2583259884990766)

The culprit is Evan Carpenter.
In fact, it is Emily Carpenter.
## 5minutemystery-st-patricks-day-pearls
Christopher is guilty: True or False?
True (0.9456006903352807)
Christopher has mean: True or False?
True (0.921357630313903)
Christopher has motive: True or False?
True (0.9825574747001844)
Christopher has opportunity: True or False?
True (0.9842760556568076)
Earl is guilty: True or False?
True (0.9158089188126235)
Earl has mean: True or False?
True (0.9405717864730483)
Earl has motive: True or False?
True (0.9750121835371013)
Earl has opportunity: True or False?
True (0.9851003883001379)
Robert is guilty: True or False?
True (0.8774767496170098)
Robert has mean: True or False?
True (0.8670357473609658)
Robert has motive: True or False?
True (0.9651191233711941)
Robert has opportunity: True or False?
True (0.9680204387474981)
Tom is guilty: True or False?
True (0.940789698413215)
Tom has mean: True or False?
True (0.9717254050158363)
Tom has motive: True or False?
True (0.9878996018169273)
Tom has opportunity: True or False?
True (0.9805806282390328)
### Christopher
- mean: False (0.07864236968609695)
- motive: False (0.017442525299815603)
- opportunity: False (0.015723944343192353)

### Earl
- mean: False (0.05942821352695171)
- motive: False (0.024987816462898715)
- opportunity: False (0.014899611699862092)

### Robert
- mean: False (0.13296425263903422)
- motive: False (0.0348808766288059)
- opportunity: False (0.0319795612525019)

### Tom
- mean: True (0.9717254050158363)
- motive: True (0.9878996018169273)
- opportunity: True (0.9805806282390328)

The culprit is Tom.
In fact, it is Tom.
## 5minutemystery-death-in-the-theatre
Helen Smith is guilty: True or False?
True (0.7364006034245382)
Helen Smith has mean: True or False?
True (0.8216173667955227)
Helen Smith has motive: True or False?
True (0.9114953293645017)
Helen Smith has opportunity: True or False?
True (0.9155072554665495)
Joanne Driscoll is guilty: True or False?
True (0.7876046283319926)
Joanne Driscoll has mean: True or False?
True (0.8701565303520181)
Joanne Driscoll has motive: True or False?
True (0.8955227118091885)
Joanne Driscoll has opportunity: True or False?
True (0.8940517282497483)
Kevin Doyle is guilty: True or False?
True (0.702530072932436)
Kevin Doyle has mean: True or False?
True (0.7950222460539826)
Kevin Doyle has motive: True or False?
True (0.8433797899747144)
Kevin Doyle has opportunity: True or False?
True (0.7676898810056793)
Sarah Jones is guilty: True or False?
True (0.8989440778839496)
Sarah Jones has mean: True or False?
True (0.8418256636710214)
Sarah Jones has motive: True or False?
True (0.9335520893498362)
Sarah Jones has opportunity: True or False?
True (0.9073122118500465)
### Helen Smith
- mean: False (0.17838263320447734)
- motive: False (0.08850467063549827)
- opportunity: False (0.08449274453345046)

### Joanne Driscoll
- mean: False (0.12984346964798188)
- motive: False (0.10447728819081148)
- opportunity: False (0.10594827175025168)

### Kevin Doyle
- mean: False (0.20497775394601736)
- motive: False (0.1566202100252856)
- opportunity: False (0.23231011899432075)

### Sarah Jones
- mean: True (0.8418256636710214)
- motive: True (0.9335520893498362)
- opportunity: True (0.9073122118500465)

The culprit is Sarah Jones.
In fact, it is Kevin Doyle.
## 5minutemystery-death-at-andersonville
Corporal Wardlow Horner is guilty: True or False?
True (0.9599126594957205)
Corporal Wardlow Horner has mean: True or False?
True (0.9149009617112335)
Corporal Wardlow Horner has motive: True or False?
True (0.9917323586955374)
Corporal Wardlow Horner has opportunity: True or False?
True (0.9660280346390409)
Private Jamie Whisenant is guilty: True or False?
True (0.9513234509300917)
Private Jamie Whisenant has mean: True or False?
Map:  17%|█▋        | 35/203 [46:37<3:45:43, 80.62s/ examples]Map:  18%|█▊        | 36/203 [47:56<3:43:43, 80.38s/ examples]Map:  18%|█▊        | 37/203 [49:01<3:29:31, 75.73s/ examples]Map:  19%|█▊        | 38/203 [49:58<3:12:14, 69.91s/ examples]Map:  19%|█▉        | 39/203 [51:19<3:20:28, 73.35s/ examples]True (0.9086179121100144)
Private Jamie Whisenant has motive: True or False?
True (0.9868280288485443)
Private Jamie Whisenant has opportunity: True or False?
True (0.9580694433457548)
Sergeant Coleman Crosby is guilty: True or False?
True (0.8852351930010195)
Sergeant Coleman Crosby has mean: True or False?
True (0.851212260635415)
Sergeant Coleman Crosby has motive: True or False?
True (0.9767802359728407)
Sergeant Coleman Crosby has opportunity: True or False?
True (0.8875948773562923)
Sergeant Josiah Thornton is guilty: True or False?
True (0.9349913039165801)
Sergeant Josiah Thornton has mean: True or False?
True (0.9161096235973493)
Sergeant Josiah Thornton has motive: True or False?
True (0.9851717948106439)
Sergeant Josiah Thornton has opportunity: True or False?
True (0.9086179121100144)
### Corporal Wardlow Horner
- mean: True (0.9149009617112335)
- motive: True (0.9917323586955374)
- opportunity: True (0.9660280346390409)

### Private Jamie Whisenant
- mean: False (0.09138208788998559)
- motive: False (0.013171971151455741)
- opportunity: False (0.041930556654245166)

### Sergeant Coleman Crosby
- mean: False (0.148787739364585)
- motive: False (0.023219764027159306)
- opportunity: False (0.11240512264370772)

### Sergeant Josiah Thornton
- mean: False (0.08389037640265073)
- motive: False (0.014828205189356125)
- opportunity: False (0.09138208788998559)

The culprit is Corporal Wardlow Horner.
In fact, it is Sergeant Josiah Thornton.
## 5minutemystery-the-big-game
Carli Antor is guilty: True or False?
True (0.893866539303124)
Carli Antor has mean: True or False?
True (0.789233749534095)
Carli Antor has motive: True or False?
True (0.943970619289785)
Carli Antor has opportunity: True or False?
True (0.945399403620829)
Chuck Jarrett is guilty: True or False?
True (0.8169911556077801)
Chuck Jarrett has mean: True or False?
True (0.6334102104891195)
Chuck Jarrett has motive: True or False?
True (0.9484418035658785)
Chuck Jarrett has opportunity: True or False?
True (0.8714748565614324)
Rich Pender is guilty: True or False?
True (0.8074605993751186)
Rich Pender has mean: True or False?
True (0.6513548405484016)
Rich Pender has motive: True or False?
True (0.942400812874096)
Rich Pender has opportunity: True or False?
True (0.9249593046682986)
Tom Barrett is guilty: True or False?
True (0.7472472734767229)
Tom Barrett has mean: True or False?
True (0.7752646804088963)
Tom Barrett has motive: True or False?
True (0.9378968460746586)
Tom Barrett has opportunity: True or False?
True (0.9567959302164903)
### Carli Antor
- mean: True (0.789233749534095)
- motive: True (0.943970619289785)
- opportunity: True (0.945399403620829)

### Chuck Jarrett
- mean: False (0.3665897895108805)
- motive: False (0.05155819643412152)
- opportunity: False (0.12852514343856758)

### Rich Pender
- mean: False (0.34864515945159835)
- motive: False (0.05759918712590395)
- opportunity: False (0.07504069533170143)

### Tom Barrett
- mean: False (0.2247353195911037)
- motive: False (0.06210315392534138)
- opportunity: False (0.04320406978350966)

The culprit is Carli Antor.
In fact, it is Tom Barrett.
## 5minutemystery-the-liberty-gun
Bob Turkle is guilty: True or False?
True (0.8568122429692968)
Bob Turkle has mean: True or False?
True (0.8402590129647053)
Bob Turkle has motive: True or False?
True (0.9079671476237222)
Bob Turkle has opportunity: True or False?
True (0.7962924261546153)
Captain Parker is guilty: True or False?
True (0.8444089912414552)
Captain Parker has mean: True or False?
True (0.8381505623254643)
Captain Parker has motive: True or False?
True (0.9418684262191025)
Captain Parker has opportunity: True or False?
True (0.8683809699466569)
Paul Rhodes is guilty: True or False?
True (0.8333246107254184)
Paul Rhodes has mean: True or False?
True (0.9036349079321685)
Paul Rhodes has motive: True or False?
True (0.9638480560973683)
Paul Rhodes has opportunity: True or False?
True (0.8887587777822111)
Tom Wise is guilty: True or False?
True (0.8879840376027315)
Tom Wise has mean: True or False?
True (0.8539127077831877)
Tom Wise has motive: True or False?
True (0.9613891248869872)
Tom Wise has opportunity: True or False?
True (0.8925625120974553)
### Bob Turkle
- mean: False (0.1597409870352947)
- motive: False (0.09203285237627779)
- opportunity: False (0.20370757384538474)

### Captain Parker
- mean: False (0.16184943767453575)
- motive: False (0.058131573780897505)
- opportunity: False (0.13161903005334308)

### Paul Rhodes
- mean: True (0.9036349079321685)
- motive: True (0.9638480560973683)
- opportunity: True (0.8887587777822111)

### Tom Wise
- mean: False (0.14608729221681227)
- motive: False (0.038610875113012755)
- opportunity: False (0.1074374879025447)

The culprit is Paul Rhodes.
In fact, it is Captain Parker.
## 5minutemystery-summer-camp
Allie is guilty: True or False?
True (0.8820219652716884)
Allie has mean: True or False?
True (0.844921525814193)
Allie has motive: True or False?
True (0.9334308488586655)
Allie has opportunity: True or False?
True (0.844921525814193)
Danny is guilty: True or False?
True (0.913058338092082)
Danny has mean: True or False?
True (0.8349459127213729)
Danny has motive: True or False?
True (0.9822537304185777)
Danny has opportunity: True or False?
True (0.9268352400785028)
Diane's campers is guilty: True or False?
True (0.9317114972308657)
Diane's campers has mean: True or False?
True (0.8333246107254184)
Diane's campers has motive: True or False?
True (0.9294403817764149)
Diane's campers has opportunity: True or False?
True (0.794384956668203)
Tom is guilty: True or False?
True (0.8947894610946939)
Tom has mean: True or False?
True (0.8812066389307215)
Tom has motive: True or False?
True (0.9769347912465448)
Tom has opportunity: True or False?
True (0.8929365260632085)
### Allie
- mean: False (0.155078474185807)
- motive: False (0.06656915114133455)
- opportunity: False (0.155078474185807)

### Danny
- mean: False (0.16505408727862714)
- motive: False (0.017746269581422336)
- opportunity: False (0.07316475992149718)

### Diane's campers
- mean: False (0.1666753892745816)
- motive: False (0.07055961822358514)
- opportunity: False (0.20561504333179703)

### Tom
- mean: True (0.8812066389307215)
- motive: True (0.9769347912465448)
- opportunity: True (0.8929365260632085)

The culprit is Tom.
In fact, it is Tom.
## 5minutemystery-mystery-at-lyndleys-fort
Bo is guilty: True or False?
True (0.9053223122169206)
Bo has mean: True or False?
True (0.5185462156586879)
Bo has motive: True or False?
True (0.8484706895507578)
Bo has opportunity: True or False?
True (0.6029971163050526)
John is guilty: True or False?
True (0.9401335713518422)
John has mean: True or False?
False (0.5708098341193941)
John has motive: True or False?
True (0.8795611817678315)
John has opportunity: True or False?
True (0.570809902165233)
John's wife is guilty: True or False?
True (0.8305941261447712)
John's wife has mean: True or False?
True (0.60859406896259)
John's wife has motive: True or False?
True (0.6306849143569856)
John's wife has opportunity: True or False?
True (0.7122321792841629)
Nathan Drew is guilty: True or False?
True (0.8519527857346616)
Nathan Drew has mean: True or False?
True (0.6242935037467142)
Nathan Drew has motive: True or False?
True (0.8370879250561812)
Nathan Drew has opportunity: True or False?
True (0.6706082735718226)
### Bo
- mean: False (0.48145378434131214)
- motive: False (0.15152931044924223)
- opportunity: False (0.3970028836949474)

### John
- mean: False (0.5708098341193941)
- motive: False (0.12043881823216851)
- opportunity: False (0.429190097834767)

### John's wife
- mean: False (0.39140593103740995)
- motive: False (0.3693150856430144)
- opportunity: False (0.28776782071583706)

### Nathan Drew
- mean: True (0.6242935037467142)
- motive: True (0.8370879250561812)
- opportunity: True (0.6706082735718226)

The culprit is Nathan Drew.
In fact, it is Nathan Drew.
## 5minutemystery-riddle-of-the-confederate-spy
Garrett is guilty: True or False?
True (0.94519740270931)
Garrett has mean: True or False?
True (0.8128672807499561)
Garrett has motive: True or False?
True (0.9589241138134527)
Map:  20%|█▉        | 40/203 [52:17<3:06:45, 68.74s/ examples]Map:  20%|██        | 41/203 [53:41<3:18:13, 73.42s/ examples]Map:  21%|██        | 42/203 [55:07<3:27:06, 77.18s/ examples]Map:  21%|██        | 43/203 [56:18<3:20:23, 75.15s/ examples]Garrett has opportunity: True or False?
True (0.8289388437432279)
McMurty is guilty: True or False?
True (0.9697853917136491)
McMurty has mean: True or False?
True (0.8407825844829613)
McMurty has motive: True or False?
True (0.9637799266082508)
McMurty has opportunity: True or False?
True (0.897695304229796)
Parker is guilty: True or False?
True (0.9485372300670596)
Parker has mean: True or False?
True (0.811078188867804)
Parker has motive: True or False?
True (0.9429285510753684)
Parker has opportunity: True or False?
True (0.9429286143036572)
Winslow is guilty: True or False?
True (0.9745318884872003)
Winslow has mean: True or False?
True (0.8987665204865408)
Winslow has motive: True or False?
True (0.9599877610290866)
Winslow has opportunity: True or False?
True (0.9238675252821831)
### Garrett
- mean: False (0.18713271925004393)
- motive: False (0.04107588618654734)
- opportunity: False (0.1710611562567721)

### McMurty
- mean: False (0.15921741551703872)
- motive: False (0.03622007339174915)
- opportunity: False (0.10230469577020396)

### Parker
- mean: False (0.18892181113219597)
- motive: False (0.05707144892463156)
- opportunity: False (0.05707138569634285)

### Winslow
- mean: True (0.8987665204865408)
- motive: True (0.9599877610290866)
- opportunity: True (0.9238675252821831)

The culprit is Winslow.
In fact, it is Parker.
## 5minutemystery-thin-ice
Hortence Lacombe is guilty: True or False?
True (0.9181873182746905)
Hortence Lacombe has mean: True or False?
True (0.612309626324874)
Hortence Lacombe has motive: True or False?
True (0.9119668603126158)
Hortence Lacombe has opportunity: True or False?
True (0.595492552580428)
Joe Tucker is guilty: True or False?
True (0.9448931235445592)
Joe Tucker has mean: True or False?
True (0.7826625131049049)
Joe Tucker has motive: True or False?
True (0.9361683754137716)
Joe Tucker has opportunity: True or False?
True (0.7655934000860735)
Mikey Chanowski is guilty: True or False?
True (0.9442796704001448)
Mikey Chanowski has mean: True or False?
True (0.7170118721569225)
Mikey Chanowski has motive: True or False?
True (0.9576753972844966)
Mikey Chanowski has opportunity: True or False?
True (0.7937461674149602)
Shea Callaghan is guilty: True or False?
True (0.9375546563206157)
Shea Callaghan has mean: True or False?
True (0.7154240000492645)
Shea Callaghan has motive: True or False?
True (0.9026095892260383)
Shea Callaghan has opportunity: True or False?
True (0.7041600870830834)
### Hortence Lacombe
- mean: False (0.38769037367512604)
- motive: False (0.08803313968738424)
- opportunity: False (0.404507447419572)

### Joe Tucker
- mean: True (0.7826625131049049)
- motive: True (0.9361683754137716)
- opportunity: True (0.7655934000860735)

### Mikey Chanowski
- mean: False (0.2829881278430775)
- motive: False (0.04232460271550342)
- opportunity: False (0.20625383258503982)

### Shea Callaghan
- mean: False (0.28457599995073546)
- motive: False (0.09739041077396171)
- opportunity: False (0.2958399129169166)

The culprit is Joe Tucker.
In fact, it is Shea Callaghan.
## 5minutemystery-flouted
Chloe Streamer is guilty: True or False?
True (0.9455001349615358)
Chloe Streamer has mean: True or False?
True (0.8766343647921183)
Chloe Streamer has motive: True or False?
True (0.9593832497641647)
Chloe Streamer has opportunity: True or False?
True (0.884439109617765)
Lyle Esposito is guilty: True or False?
True (0.9672868854836233)
Lyle Esposito has mean: True or False?
True (0.851212260635415)
Lyle Esposito has motive: True or False?
True (0.9748211501698323)
Lyle Esposito has opportunity: True or False?
True (0.9364014251476122)
Marty Nolan is guilty: True or False?
True (0.9540517932883525)
Marty Nolan has mean: True or False?
True (0.8509646659219744)
Marty Nolan has motive: True or False?
True (0.9669139993413022)
Marty Nolan has opportunity: True or False?
True (0.9489172681310486)
Susan Moorgate is guilty: True or False?
True (0.9193533657123177)
Susan Moorgate has mean: True or False?
True (0.6662796150778861)
Susan Moorgate has motive: True or False?
True (0.862930245043327)
Susan Moorgate has opportunity: True or False?
True (0.7008947664177184)
### Chloe Streamer
- mean: False (0.12336563520788169)
- motive: False (0.04061675023583533)
- opportunity: False (0.11556089038223505)

### Lyle Esposito
- mean: False (0.148787739364585)
- motive: False (0.025178849830167715)
- opportunity: False (0.06359857485238785)

### Marty Nolan
- mean: True (0.8509646659219744)
- motive: True (0.9669139993413022)
- opportunity: True (0.9489172681310486)

### Susan Moorgate
- mean: False (0.33372038492211387)
- motive: False (0.13706975495667295)
- opportunity: False (0.2991052335822816)

The culprit is Marty Nolan.
In fact, it is Marty Nolan.
## 5minutemystery-car-trouble
Mr. Carlson is guilty: True or False?
True (0.9162595863469921)
Mr. Carlson has mean: True or False?
True (0.8608377628023384)
Mr. Carlson has motive: True or False?
True (0.983862637994192)
Mr. Carlson has opportunity: True or False?
True (0.9435559526996434)
Mr. Leamington is guilty: True or False?
True (0.9296323035994176)
Mr. Leamington has mean: True or False?
True (0.9063219998220023)
Mr. Leamington has motive: True or False?
True (0.9862973096916147)
Mr. Leamington has opportunity: True or False?
True (0.930078152541638)
Mrs. Roberts is guilty: True or False?
True (0.8774768149941248)
Mrs. Roberts has mean: True or False?
True (0.8314170225049837)
Mrs. Roberts has motive: True or False?
True (0.9815950994553841)
Mrs. Roberts has opportunity: True or False?
True (0.8727816933272936)
Randy Peters is guilty: True or False?
True (0.8902941942359355)
Randy Peters has mean: True or False?
True (0.7704647687904915)
Randy Peters has motive: True or False?
True (0.974676967005652)
Randy Peters has opportunity: True or False?
True (0.9231777821690265)
### Mr. Carlson
- mean: False (0.13916223719766163)
- motive: False (0.016137362005807954)
- opportunity: False (0.05644404730035657)

### Mr. Leamington
- mean: True (0.9063219998220023)
- motive: True (0.9862973096916147)
- opportunity: True (0.930078152541638)

### Mrs. Roberts
- mean: False (0.16858297749501627)
- motive: False (0.018404900544615854)
- opportunity: False (0.1272183066727064)

### Randy Peters
- mean: False (0.22953523120950847)
- motive: False (0.025323032994348016)
- opportunity: False (0.07682221783097354)

The culprit is Mr. Leamington.
In fact, it is Randy Peters.
## 5minutemystery-mr-poes-birthday-party
Anthony is guilty: True or False?
True (0.9466953276900992)
Anthony has mean: True or False?
True (0.8638516611889259)
Anthony has motive: True or False?
True (0.9669139993413022)
Anthony has opportunity: True or False?
True (0.9284088027271398)
Connor is guilty: True or False?
True (0.9173026114435064)
Connor has mean: True or False?
True (0.8587185689177256)
Connor has motive: True or False?
True (0.9577544910931239)
Connor has opportunity: True or False?
True (0.878314250659373)
Skylar is guilty: True or False?
True (0.9692660578747095)
Skylar has mean: True or False?
True (0.905322251510331)
Skylar has motive: True or False?
True (0.9824231266498078)
Skylar has opportunity: True or False?
True (0.897695304229796)
Stephen is guilty: True or False?
True (0.9094255002859922)
Stephen has mean: True or False?
True (0.6187804294217345)
Stephen has motive: True or False?
True (0.9790757889289493)
Stephen has opportunity: True or False?
True (0.8719117627136385)
Tommy is guilty: True or False?
True (0.9074763663250294)
Tommy has mean: True or False?
True (0.950041474283655)
Tommy has motive: True or False?
True (0.9735442395649992)
Tommy has opportunity: True or False?
True (0.8469578650997759)
### Anthony
- mean: False (0.13614833881107413)
- motive: False (0.03308600065869782)
- opportunity: False (0.07159119727286023)

### Connor
- mean: False (0.14128143108227442)
- motive: False (0.04224550890687606)
- opportunity: False (0.12168574934062704)

### Skylar
- mean: True (0.905322251510331)
- motive: True (0.9824231266498078)
- opportunity: True (0.897695304229796)

### Stephen
- mean: False (0.3812195705782655)
- motive: False (0.02092421107105069)
Map:  22%|██▏       | 44/203 [57:47<3:30:15, 79.34s/ examples]Map:  22%|██▏       | 45/203 [59:07<3:29:19, 79.49s/ examples]Map:  23%|██▎       | 46/203 [1:00:32<3:32:51, 81.35s/ examples]Map:  23%|██▎       | 47/203 [1:01:53<3:30:54, 81.12s/ examples]Map:  24%|██▎       | 48/203 [1:03:10<3:26:14, 79.83s/ examples]- opportunity: False (0.12808823728636154)

### Tommy
- mean: False (0.04995852571634496)
- motive: False (0.026455760435000752)
- opportunity: False (0.1530421349002241)

The culprit is Skylar.
In fact, it is Connor.
## 5minutemystery-the-root-of-all-evil
Bryan Durell is guilty: True or False?
True (0.8128672807499561)
Bryan Durell has mean: True or False?
True (0.6967842494573921)
Bryan Durell has motive: True or False?
True (0.9319595674053855)
Bryan Durell has opportunity: True or False?
True (0.7819972591886313)
Grieve Collier is guilty: True or False?
True (0.8787311338092536)
Grieve Collier has mean: True or False?
True (0.7559974119430289)
Grieve Collier has motive: True or False?
True (0.979314505527214)
Grieve Collier has opportunity: True or False?
True (0.8563323578093363)
Jacques Bourbonne is guilty: True or False?
True (0.8297680628665619)
Jacques Bourbonne has mean: True or False?
True (0.7931058945535956)
Jacques Bourbonne has motive: True or False?
True (0.9568766339006164)
Jacques Bourbonne has opportunity: True or False?
True (0.8433797899747144)
Ruth Majick is guilty: True or False?
True (0.8122723669190336)
Ruth Majick has mean: True or False?
True (0.8433797899747144)
Ruth Majick has motive: True or False?
True (0.935346481802689)
Ruth Majick has opportunity: True or False?
True (0.8688268116310761)
### Bryan Durell
- mean: False (0.30321575054260785)
- motive: False (0.06804043259461445)
- opportunity: False (0.21800274081136872)

### Grieve Collier
- mean: False (0.24400258805697106)
- motive: False (0.020685494472786004)
- opportunity: False (0.14366764219066375)

### Jacques Bourbonne
- mean: False (0.2068941054464044)
- motive: False (0.04312336609938361)
- opportunity: False (0.1566202100252856)

### Ruth Majick
- mean: True (0.8433797899747144)
- motive: True (0.935346481802689)
- opportunity: True (0.8688268116310761)

The culprit is Ruth Majick.
In fact, it is Bryan Durell.
## 5minutemystery-get-the-lead-out
Benjamin Trodger is guilty: True or False?
True (0.9105453462677353)
Benjamin Trodger has mean: True or False?
True (0.8770561879413864)
Benjamin Trodger has motive: True or False?
True (0.9355823382423648)
Benjamin Trodger has opportunity: True or False?
True (0.9012274173198201)
Cynthia Kirwan is guilty: True or False?
True (0.9152045868398637)
Cynthia Kirwan has mean: True or False?
True (0.7627776774954688)
Cynthia Kirwan has motive: True or False?
True (0.942081869103903)
Cynthia Kirwan has opportunity: True or False?
True (0.8832359917473193)
Dan Skinner is guilty: True or False?
True (0.9420819287658885)
Dan Skinner has mean: True or False?
True (0.8352149074858963)
Dan Skinner has motive: True or False?
True (0.9627782093174002)
Dan Skinner has opportunity: True or False?
True (0.9190632712053527)
Shel Jonas is guilty: True or False?
True (0.9231777821690265)
Shel Jonas has mean: True or False?
True (0.7786493288700866)
Shel Jonas has motive: True or False?
True (0.9403530947748038)
Shel Jonas has opportunity: True or False?
True (0.8582439976623328)
### Benjamin Trodger
- mean: False (0.1229438120586136)
- motive: False (0.06441766175763519)
- opportunity: False (0.09877258268017985)

### Cynthia Kirwan
- mean: False (0.23722232250453124)
- motive: False (0.057918130896096987)
- opportunity: False (0.11676400825268074)

### Dan Skinner
- mean: True (0.8352149074858963)
- motive: True (0.9627782093174002)
- opportunity: True (0.9190632712053527)

### Shel Jonas
- mean: False (0.22135067112991336)
- motive: False (0.05964690522519622)
- opportunity: False (0.14175600233766716)

The culprit is Dan Skinner.
In fact, it is Dan Skinner.
## 5minutemystery-popping-a-wheelie
Cory is guilty: True or False?
True (0.8577681165234065)
Cory has mean: True or False?
True (0.6433292707767855)
Cory has motive: True or False?
True (0.8925625719484378)
Cory has opportunity: True or False?
True (0.7424216889954057)
David is guilty: True or False?
True (0.8692713407917644)
David has mean: True or False?
True (0.6967841871600284)
David has motive: True or False?
True (0.9237300130783155)
David has opportunity: True or False?
True (0.7520125537161032)
Mark is guilty: True or False?
True (0.9677167542009312)
Mark has mean: True or False?
True (0.8652241235443877)
Mark has motive: True or False?
True (0.9686788331076437)
Mark has opportunity: True or False?
True (0.8951566849862127)
String is guilty: True or False?
True (0.9124361878432953)
String has mean: True or False?
True (0.8727817583545995)
String has motive: True or False?
True (0.8101787517928931)
String has opportunity: True or False?
True (0.854884683810039)
### Cory
- mean: False (0.3566707292232145)
- motive: False (0.1074374280515622)
- opportunity: False (0.2575783110045943)

### David
- mean: False (0.30321581283997157)
- motive: False (0.07626998692168452)
- opportunity: False (0.2479874462838968)

### Mark
- mean: True (0.8652241235443877)
- motive: True (0.9686788331076437)
- opportunity: True (0.8951566849862127)

### String
- mean: False (0.12721824164540052)
- motive: False (0.18982124820710689)
- opportunity: False (0.14511531618996099)

The culprit is Mark.
In fact, it is David.
## 5minutemystery-the-mystery-of-the-leprechauns-trophy
Barry is guilty: True or False?
True (0.8969755785184792)
Barry has mean: True or False?
True (0.9170058398600052)
Barry has motive: True or False?
True (0.9597620378565557)
Barry has opportunity: True or False?
True (0.8732148436000907)
Casey is guilty: True or False?
True (0.8799743689174987)
Casey has mean: True or False?
True (0.892187358563457)
Casey has motive: True or False?
True (0.9094255544919778)
Casey has opportunity: True or False?
True (0.8757870204368676)
Mr. Carswell is guilty: True or False?
True (0.7333563569098757)
Mr. Carswell has mean: True or False?
True (0.8392075831473667)
Mr. Carswell has motive: True or False?
True (0.8820219652716884)
Mr. Carswell has opportunity: True or False?
True (0.7669924589170153)
Tony is guilty: True or False?
True (0.8418256636710214)
Tony has mean: True or False?
True (0.8665847814067802)
Tony has motive: True or False?
True (0.8816149238192855)
Tony has opportunity: True or False?
True (0.7106282704218558)
### Barry
- mean: True (0.9170058398600052)
- motive: True (0.9597620378565557)
- opportunity: True (0.8732148436000907)

### Casey
- mean: False (0.10781264143654301)
- motive: False (0.09057444550802218)
- opportunity: False (0.12421297956313238)

### Mr. Carswell
- mean: False (0.16079241685263335)
- motive: False (0.11797803472831159)
- opportunity: False (0.23300754108298471)

### Tony
- mean: False (0.1334152185932198)
- motive: False (0.11838507618071448)
- opportunity: False (0.28937172957814417)

The culprit is Barry.
In fact, it is Tony.
## 5minutemystery-the-mysterious-chicken
Ed is guilty: True or False?
True (0.8227595062673136)
Ed has mean: True or False?
True (0.8793541237128909)
Ed has motive: True or False?
True (0.9657060519221431)
Ed has opportunity: True or False?
True (0.9726235262544756)
Ed's mother is guilty: True or False?
True (0.580352087772514)
Ed's mother has mean: True or False?
False (0.5650587803792624)
Ed's mother has motive: True or False?
True (0.9706877478963396)
Ed's mother has opportunity: True or False?
True (0.9785492416845885)
Ed’s Husky is guilty: True or False?
True (0.644225125126315)
Ed’s Husky has mean: True or False?
False (0.6513548405484016)
Ed’s Husky has motive: True or False?
True (0.934872446722342)
Ed’s Husky has opportunity: True or False?
True (0.7453983509653428)
Zeke is guilty: True or False?
True (0.9309620852900756)
Zeke has mean: True or False?
True (0.9281487460975983)
Zeke has motive: True or False?
True (0.9931760429948333)
Zeke has opportunity: True or False?
True (0.9812389020148623)
### Ed
- mean: False (0.1206458762871091)
- motive: False (0.034293948077856906)
- opportunity: False (0.027376473745524432)

### Ed's mother
- mean: False (0.5650587803792624)
- motive: False (0.029312252103660397)
- opportunity: False (0.021450758315411544)

### Ed’s Husky
- mean: False (0.6513548405484016)
- motive: False (0.06512755327765796)
- opportunity: False (0.2546016490346572)

### Zeke
Map:  24%|██▍       | 49/203 [1:04:34<3:28:27, 81.22s/ examples]Map:  25%|██▍       | 50/203 [1:05:31<3:08:06, 73.77s/ examples]Map:  25%|██▌       | 51/203 [1:07:13<3:28:27, 82.29s/ examples]Map:  26%|██▌       | 52/203 [1:08:29<3:22:27, 80.44s/ examples]Map:  26%|██▌       | 53/203 [1:09:58<3:27:21, 82.94s/ examples]- mean: True (0.9281487460975983)
- motive: True (0.9931760429948333)
- opportunity: True (0.9812389020148623)

The culprit is Zeke.
In fact, it is Ed.
## 5minutemystery-the-late-night-horror-show
Andrew is guilty: True or False?
True (0.9319595674053855)
Andrew has mean: True or False?
True (0.8311430212356835)
Andrew has motive: True or False?
True (0.8591918406281239)
Andrew has opportunity: True or False?
True (0.7669924589170153)
David is guilty: True or False?
True (0.8723473540228537)
David has mean: True or False?
True (0.6976089520497016)
David has motive: True or False?
True (0.8958875533219306)
David has opportunity: True or False?
True (0.8381505623254643)
Dennis is guilty: True or False?
True (0.920217993899809)
Dennis has mean: True or False?
True (0.8484706895507578)
Dennis has motive: True or False?
True (0.9063219998220023)
Dennis has opportunity: True or False?
True (0.8489722037469682)
Matthew is guilty: True or False?
True (0.9351098557348285)
Matthew has mean: True or False?
True (0.8723473540228537)
Matthew has motive: True or False?
True (0.9299510095943111)
Matthew has opportunity: True or False?
True (0.879146760693242)
### Andrew
- mean: False (0.1688569787643165)
- motive: False (0.14080815937187607)
- opportunity: False (0.23300754108298471)

### David
- mean: False (0.30239104795029836)
- motive: False (0.1041124466780694)
- opportunity: False (0.16184943767453575)

### Dennis
- mean: False (0.15152931044924223)
- motive: False (0.09367800017799766)
- opportunity: False (0.15102779625303175)

### Matthew
- mean: True (0.8723473540228537)
- motive: True (0.9299510095943111)
- opportunity: True (0.879146760693242)

The culprit is Matthew.
In fact, it is David.
## 5minutemystery-making-partner
Dan Cartman is guilty: True or False?
True (0.8134608241927087)
Dan Cartman has mean: True or False?
True (0.878314250659373)
Dan Cartman has motive: True or False?
True (0.947769104959166)
Dan Cartman has opportunity: True or False?
True (0.9445872321654378)
Jill is guilty: True or False?
True (0.8826302888575707)
Jill has mean: True or False?
True (0.8221891570741111)
Jill has motive: True or False?
True (0.9403530352223053)
Jill has opportunity: True or False?
True (0.854884683810039)
Mike Creighton is guilty: True or False?
True (0.6654105788791005)
Mike Creighton has mean: True or False?
True (0.7779753136455794)
Mike Creighton has motive: True or False?
True (0.9226219081780128)
Mike Creighton has opportunity: True or False?
True (0.9032942081209032)
Mrs. Krantz is guilty: True or False?
True (0.7606506318580792)
Mrs. Krantz has mean: True or False?
True (0.7994423454932595)
Mrs. Krantz has motive: True or False?
True (0.9367495172436676)
Mrs. Krantz has opportunity: True or False?
True (0.8381505623254643)
### Dan Cartman
- mean: True (0.878314250659373)
- motive: True (0.947769104959166)
- opportunity: True (0.9445872321654378)

### Jill
- mean: False (0.1778108429258889)
- motive: False (0.05964696477769471)
- opportunity: False (0.14511531618996099)

### Mike Creighton
- mean: False (0.22202468635442063)
- motive: False (0.07737809182198718)
- opportunity: False (0.09670579187909678)

### Mrs. Krantz
- mean: False (0.20055765450674046)
- motive: False (0.06325048275633238)
- opportunity: False (0.16184943767453575)

The culprit is Dan Cartman.
In fact, it is Mike Creighton.
## 5minutemystery-no-retreat-from-death
Amanda Kent is guilty: True or False?
True (0.9307106123564625)
Amanda Kent has mean: True or False?
True (0.9804313180726916)
Amanda Kent has motive: True or False?
True (0.9868280885871353)
Amanda Kent has opportunity: True or False?
True (0.9706877478963396)
Craig Willis is guilty: True or False?
True (0.9183338853275215)
Craig Willis has mean: True or False?
True (0.9431384220853135)
Craig Willis has motive: True or False?
True (0.9891291857546544)
Craig Willis has opportunity: True or False?
True (0.9405717864730483)
Niles Anderson is guilty: True or False?
True (0.9616059669560388)
Niles Anderson has mean: True or False?
True (0.9707432981083896)
Niles Anderson has motive: True or False?
True (0.9929882285769507)
Niles Anderson has opportunity: True or False?
True (0.972727357600667)
Stephanie Clark is guilty: True or False?
True (0.9152045868398637)
Stephanie Clark has mean: True or False?
True (0.9603611244019274)
Stephanie Clark has motive: True or False?
True (0.9865199324432031)
Stephanie Clark has opportunity: True or False?
True (0.9546474221708894)
### Amanda Kent
- mean: True (0.9804313180726916)
- motive: True (0.9868280885871353)
- opportunity: True (0.9706877478963396)

### Craig Willis
- mean: False (0.05686157791468649)
- motive: False (0.010870814245345639)
- opportunity: False (0.05942821352695171)

### Niles Anderson
- mean: False (0.029256701891610448)
- motive: False (0.007011771423049318)
- opportunity: False (0.027272642399333025)

### Stephanie Clark
- mean: False (0.039638875598072554)
- motive: False (0.01348006755679687)
- opportunity: False (0.04535257782911062)

The culprit is Amanda Kent.
In fact, it is Niles Anderson.
## 5minutemystery-a-monster-of-a-mystery
Donald is guilty: True or False?
True (0.970070243275667)
Donald has mean: True or False?
True (0.9476723683039264)
Donald has motive: True or False?
True (0.9529258022651363)
Donald has opportunity: True or False?
True (0.9438672660817211)
Linda is guilty: True or False?
True (0.9428234118096998)
Linda has mean: True or False?
True (0.9331876642092066)
Linda has motive: True or False?
True (0.9753431079900657)
Linda has opportunity: True or False?
True (0.9660280346390409)
Randy is guilty: True or False?
True (0.9672868242254096)
Randy has mean: True or False?
True (0.9175984877579624)
Randy has motive: True or False?
True (0.9683812262581977)
Randy has opportunity: True or False?
True (0.9626028535101038)
Wendell is guilty: True or False?
True (0.96224969617818)
Wendell has mean: True or False?
True (0.9071478843057855)
Wendell has motive: True or False?
True (0.9658352120791275)
Wendell has opportunity: True or False?
True (0.9076402191395381)
### Donald
- mean: False (0.05232763169607357)
- motive: False (0.047074197734863654)
- opportunity: False (0.05613273391827889)

### Linda
- mean: True (0.9331876642092066)
- motive: True (0.9753431079900657)
- opportunity: True (0.9660280346390409)

### Randy
- mean: False (0.08240151224203762)
- motive: False (0.03161877374180233)
- opportunity: False (0.03739714648989623)

### Wendell
- mean: False (0.09285211569421448)
- motive: False (0.03416478792087252)
- opportunity: False (0.09235978086046193)

The culprit is Linda.
In fact, it is Linda.
## 5minutemystery-chow-baby
Beryl Hives is guilty: True or False?
True (0.8757869551856522)
Beryl Hives has mean: True or False?
True (0.6959583025067009)
Beryl Hives has motive: True or False?
True (0.9314625284362855)
Beryl Hives has opportunity: True or False?
True (0.8283842201397164)
Dawn de Jong is guilty: True or False?
True (0.7386690954574974)
Dawn de Jong has mean: True or False?
True (0.6352224318508648)
Dawn de Jong has motive: True or False?
True (0.9008791478232747)
Dawn de Jong has opportunity: True or False?
True (0.6306849143569856)
Konrad Pushkin is guilty: True or False?
True (0.9460011721384068)
Konrad Pushkin has mean: True or False?
True (0.7146280926688615)
Konrad Pushkin has motive: True or False?
True (0.9439705630247532)
Konrad Pushkin has opportunity: True or False?
True (0.8918110138739693)
Pete Stampkowski is guilty: True or False?
True (0.8984105603938967)
Pete Stampkowski has mean: True or False?
True (0.6619228115397798)
Pete Stampkowski has motive: True or False?
True (0.9575167905174621)
Pete Stampkowski has opportunity: True or False?
True (0.8864204283224634)
### Beryl Hives
- mean: False (0.3040416974932991)
- motive: False (0.06853747156371448)
- opportunity: False (0.17161577986028365)

### Dawn de Jong
- mean: False (0.3647775681491352)
- motive: False (0.09912085217672528)
- opportunity: False (0.3693150856430144)

### Konrad Pushkin
- mean: True (0.7146280926688615)
- motive: True (0.9439705630247532)
- opportunity: True (0.8918110138739693)

### Pete Stampkowski
Map:  27%|██▋       | 54/203 [1:11:22<3:27:10, 83.43s/ examples]Map:  27%|██▋       | 55/203 [1:13:25<3:54:38, 95.12s/ examples]Map:  28%|██▊       | 56/203 [1:15:22<4:09:45, 101.94s/ examples]Map:  28%|██▊       | 57/203 [1:17:05<4:08:41, 102.20s/ examples]Map:  29%|██▊       | 58/203 [1:18:51<4:09:48, 103.37s/ examples]- mean: False (0.33807718846022017)
- motive: False (0.04248320948253792)
- opportunity: False (0.11357957167753663)

The culprit is Konrad Pushkin.
In fact, it is Beryl Hives.
## 5minutemystery-the-mystery-of-the-frowning-clown
Bumbo is guilty: True or False?
True (0.9643886093607492)
Bumbo has mean: True or False?
True (0.8906751877407573)
Bumbo has motive: True or False?
True (0.9700134993465792)
Bumbo has opportunity: True or False?
True (0.9190632712053527)
Dusty is guilty: True or False?
True (0.9630224717531983)
Dusty has mean: True or False?
True (0.9089416847784234)
Dusty has motive: True or False?
True (0.9722043875229701)
Dusty has opportunity: True or False?
True (0.9270997017012965)
Mr. Green is guilty: True or False?
True (0.9579909444975866)
Mr. Green has mean: True or False?
True (0.8973359441831076)
Mr. Green has motive: True or False?
True (0.9771101479827176)
Mr. Green has opportunity: True or False?
True (0.9244151684978138)
Stage Manager is guilty: True or False?
True (0.9491062747098069)
Stage Manager has mean: True or False?
True (0.9328214561580316)
Stage Manager has motive: True or False?
True (0.9792749284948266)
Stage Manager has opportunity: True or False?
True (0.959535181008237)
### Bumbo
- mean: False (0.10932481225924273)
- motive: False (0.02998650065342079)
- opportunity: False (0.0809367287946473)

### Dusty
- mean: False (0.09105831522157659)
- motive: False (0.027795612477029885)
- opportunity: False (0.07290029829870348)

### Mr. Green
- mean: False (0.10266405581689242)
- motive: False (0.02288985201728244)
- opportunity: False (0.0755848315021862)

### Stage Manager
- mean: True (0.9328214561580316)
- motive: True (0.9792749284948266)
- opportunity: True (0.959535181008237)

The culprit is Stage Manager.
In fact, it is Stage Manager.
## 5minutemystery-the-strangest-sport-of-all
Ernie is guilty: True or False?
True (0.9190633328333496)
Ernie has mean: True or False?
True (0.8951566249612815)
Ernie has motive: True or False?
True (0.9102267057681164)
Ernie has opportunity: True or False?
True (0.9394705907755942)
Gordon is guilty: True or False?
True (0.9046505126460354)
Gordon has mean: True or False?
True (0.7534666630720156)
Gordon has motive: True or False?
True (0.8998277786460391)
Gordon has opportunity: True or False?
True (0.8591918406281239)
Jesse is guilty: True or False?
True (0.8910549302065384)
Jesse has mean: True or False?
True (0.7950222460539826)
Jesse has motive: True or False?
True (0.8770561879413864)
Jesse has opportunity: True or False?
True (0.8062431235779619)
Mac is guilty: True or False?
True (0.9307106123564625)
Mac has mean: True or False?
True (0.8820219652716884)
Mac has motive: True or False?
True (0.927887794449634)
Mac has opportunity: True or False?
True (0.8973360043541736)
### Ernie
- mean: True (0.8951566249612815)
- motive: True (0.9102267057681164)
- opportunity: True (0.9394705907755942)

### Gordon
- mean: False (0.2465333369279844)
- motive: False (0.10017222135396087)
- opportunity: False (0.14080815937187607)

### Jesse
- mean: False (0.20497775394601736)
- motive: False (0.1229438120586136)
- opportunity: False (0.1937568764220381)

### Mac
- mean: False (0.11797803472831159)
- motive: False (0.07211220555036602)
- opportunity: False (0.1026639956458264)

The culprit is Ernie.
In fact, it is Jesse.
## 5minutemystery-who-stole-storimons-wallet
Danny is guilty: True or False?
True (0.9678993227186541)
Danny has mean: True or False?
True (0.8444089912414552)
Danny has motive: True or False?
True (0.943347633443741)
Danny has opportunity: True or False?
True (0.942081869103903)
Mick is guilty: True or False?
True (0.9753431679417652)
Mick has mean: True or False?
True (0.9775000208126312)
Mick has motive: True or False?
True (0.9820482724696491)
Mick has opportunity: True or False?
True (0.9698996547102765)
Mr. Storimon is guilty: True or False?
True (0.9683812262581977)
Mr. Storimon has mean: True or False?
True (0.9598374351134399)
Mr. Storimon has motive: True or False?
True (0.9859634637885061)
Mr. Storimon has opportunity: True or False?
True (0.9759464867446064)
Policeman is guilty: True or False?
True (0.9792550794742616)
Policeman has mean: True or False?
True (0.9333093181503205)
Policeman has motive: True or False?
True (0.9764905566616159)
Policeman has opportunity: True or False?
True (0.9599126594957205)
### Danny
- mean: False (0.1555910087585448)
- motive: False (0.05665236655625905)
- opportunity: False (0.057918130896096987)

### Mick
- mean: True (0.9775000208126312)
- motive: True (0.9820482724696491)
- opportunity: True (0.9698996547102765)

### Mr. Storimon
- mean: False (0.040162564886560115)
- motive: False (0.014036536211493922)
- opportunity: False (0.02405351325539362)

### Policeman
- mean: False (0.06669068184967952)
- motive: False (0.023509443338384117)
- opportunity: False (0.040087340504279534)

The culprit is Mick.
In fact, it is Mr. Storimon.
## 5minutemystery-miles-archer-solves-a-case
Arnold Grossmecker is guilty: True or False?
True (0.9465966835599983)
Arnold Grossmecker has mean: True or False?
True (0.847967740521315)
Arnold Grossmecker has motive: True or False?
True (0.9763104920302871)
Arnold Grossmecker has opportunity: True or False?
True (0.9170058398600052)
Brigid Jellicoe is guilty: True or False?
True (0.9537942396657707)
Brigid Jellicoe has mean: True or False?
True (0.9073122118500465)
Brigid Jellicoe has motive: True or False?
True (0.9638480560973683)
Brigid Jellicoe has opportunity: True or False?
True (0.9405717864730483)
Quinton Jesselton is guilty: True or False?
True (0.9294403817764149)
Quinton Jesselton has mean: True or False?
True (0.9408984770280414)
Quinton Jesselton has motive: True or False?
True (0.9736947425622681)
Quinton Jesselton has opportunity: True or False?
True (0.8980534699860239)
Sandra O’Malley is guilty: True or False?
True (0.8365545874520802)
Sandra O’Malley has mean: True or False?
True (0.6842640693504702)
Sandra O’Malley has motive: True or False?
True (0.9422947179693436)
Sandra O’Malley has opportunity: True or False?
True (0.9193533657123177)
### Arnold Grossmecker
- mean: False (0.15203225947868504)
- motive: False (0.02368950796971292)
- opportunity: False (0.08299416013999483)

### Brigid Jellicoe
- mean: False (0.09268778814995349)
- motive: False (0.036151943902631656)
- opportunity: False (0.05942821352695171)

### Quinton Jesselton
- mean: True (0.9408984770280414)
- motive: True (0.9736947425622681)
- opportunity: True (0.8980534699860239)

### Sandra O’Malley
- mean: False (0.31573593064952976)
- motive: False (0.05770528203065639)
- opportunity: False (0.08064663428768226)

The culprit is Quinton Jesselton.
In fact, it is Quinton Jesselton.
## 5minutemystery-murder-in-the-early-morning
Constance is guilty: True or False?
True (0.8333246107254184)
Constance has mean: True or False?
True (0.9687380774673213)
Constance has motive: True or False?
True (0.9687380774673213)
Constance has opportunity: True or False?
True (0.9682614213403071)
John is guilty: True or False?
True (0.71582149676272)
John has mean: True or False?
True (0.8433797899747144)
John has motive: True or False?
True (0.9394705907755942)
John has opportunity: True or False?
True (0.9709092372014624)
Nancy is guilty: True or False?
True (0.7911764307711107)
Nancy has mean: True or False?
True (0.7885831565209055)
Nancy has motive: True or False?
True (0.9284088027271398)
Nancy has opportunity: True or False?
True (0.920789721359066)
Vernon is guilty: True or False?
True (0.7412996266976789)
Vernon has mean: True or False?
True (0.8716934900924195)
Vernon has motive: True or False?
True (0.9530133616438526)
Vernon has opportunity: True or False?
True (0.9425067301242699)
### Constance
- mean: True (0.9687380774673213)
- motive: True (0.9687380774673213)
- opportunity: True (0.9682614213403071)

### John
- mean: False (0.1566202100252856)
- motive: False (0.06052940922440575)
- opportunity: False (0.029090762798537617)

### Nancy
- mean: False (0.2114168434790945)
- motive: False (0.07159119727286023)
- opportunity: False (0.079210278640934)

### Vernon
- mean: False (0.12830650990758052)
Map:  29%|██▉       | 59/203 [1:19:56<3:40:19, 91.80s/ examples] Map:  30%|██▉       | 60/203 [1:21:07<3:23:35, 85.42s/ examples]Map:  30%|███       | 61/203 [1:22:42<3:28:53, 88.27s/ examples]Map:  31%|███       | 62/203 [1:24:22<3:35:45, 91.81s/ examples]Map:  31%|███       | 63/203 [1:25:24<3:13:47, 83.05s/ examples]- motive: False (0.04698663835614736)
- opportunity: False (0.05749326987573011)

The culprit is Constance.
In fact, it is Vernon.
## 5minutemystery-raiding-cane
Brent Pearson is guilty: True or False?
True (0.9563905008811648)
Brent Pearson has mean: True or False?
True (0.8169911556077801)
Brent Pearson has motive: True or False?
True (0.9819446807697475)
Brent Pearson has opportunity: True or False?
True (0.8887587777822111)
Frank Weiss is guilty: True or False?
True (0.9714016916045378)
Frank Weiss has mean: True or False?
True (0.8686040045586428)
Frank Weiss has motive: True or False?
True (0.9890448453517958)
Frank Weiss has opportunity: True or False?
True (0.8873999116020591)
Michael Weiss is guilty: True or False?
True (0.9565936323912209)
Michael Weiss has mean: True or False?
True (0.8203256148776867)
Michael Weiss has motive: True or False?
True (0.9808208937620218)
Michael Weiss has opportunity: True or False?
True (0.8253083182831968)
Ronald Weiss is guilty: True or False?
True (0.9680808185196469)
Ronald Weiss has mean: True or False?
True (0.8546422101536368)
Ronald Weiss has motive: True or False?
True (0.9823386069427514)
Ronald Weiss has opportunity: True or False?
True (0.8908652046764556)
### Brent Pearson
- mean: False (0.18300884439221987)
- motive: False (0.018055319230252498)
- opportunity: False (0.11124122221778887)

### Frank Weiss
- mean: True (0.8686040045586428)
- motive: True (0.9890448453517958)
- opportunity: True (0.8873999116020591)

### Michael Weiss
- mean: False (0.17967438512231326)
- motive: False (0.01917910623797825)
- opportunity: False (0.17469168171680316)

### Ronald Weiss
- mean: False (0.14535778984636316)
- motive: False (0.017661393057248564)
- opportunity: False (0.10913479532354442)

The culprit is Frank Weiss.
In fact, it is Frank Weiss.
## 5minutemystery-the-missing-dagger
Chris Palmer is guilty: True or False?
True (0.960804880888677)
Chris Palmer has mean: True or False?
True (0.936980484689786)
Chris Palmer has motive: True or False?
True (0.9721515187478543)
Chris Palmer has opportunity: True or False?
True (0.962813258487323)
Matthew Light is guilty: True or False?
True (0.9396923188104354)
Matthew Light has mean: True or False?
True (0.9046505665674094)
Matthew Light has motive: True or False?
True (0.9518632280135741)
Matthew Light has opportunity: True or False?
True (0.9351098557348285)
Mitchell Land is guilty: True or False?
True (0.9471859926317535)
Mitchell Land has mean: True or False?
True (0.9130583993174167)
Mitchell Land has motive: True or False?
True (0.9444848881002107)
Mitchell Land has opportunity: True or False?
True (0.9594593035226332)
Paul Benham is guilty: True or False?
True (0.9748211501698323)
Paul Benham has mean: True or False?
True (0.9605096001181298)
Paul Benham has motive: True or False?
True (0.972830772390074)
Paul Benham has opportunity: True or False?
True (0.9559813152103319)
Russell Smith is guilty: True or False?
True (0.9517737036527996)
Russell Smith has mean: True or False?
True (0.9610980147014194)
Russell Smith has motive: True or False?
True (0.9808393129553152)
Russell Smith has opportunity: True or False?
True (0.9634374994224176)
### Chris Palmer
- mean: False (0.06301951531021399)
- motive: False (0.027848481252145674)
- opportunity: False (0.03718674151267698)

### Matthew Light
- mean: False (0.09534943343259061)
- motive: False (0.04813677198642585)
- opportunity: False (0.06489014426517148)

### Mitchell Land
- mean: False (0.08694160068258328)
- motive: False (0.055515111899789304)
- opportunity: False (0.0405406964773668)

### Paul Benham
- mean: False (0.0394903998818702)
- motive: False (0.027169227609926017)
- opportunity: False (0.04401868478966808)

### Russell Smith
- mean: True (0.9610980147014194)
- motive: True (0.9808393129553152)
- opportunity: True (0.9634374994224176)

The culprit is Russell Smith.
In fact, it is Paul Benham.
## 5minutemystery-mystery-of-the-bratty-kid
Angelita is guilty: True or False?
True (0.8996515883738708)
Angelita has mean: True or False?
True (0.8716934900924195)
Angelita has motive: True or False?
True (0.8624674701790345)
Angelita has opportunity: True or False?
True (0.9082930704920021)
Emily is guilty: True or False?
True (0.944176853162527)
Emily has mean: True or False?
True (0.8862236142219189)
Emily has motive: True or False?
True (0.9180403984176693)
Emily has opportunity: True or False?
True (0.950041474283655)
Jessica is guilty: True or False?
True (0.9281487460975983)
Jessica has mean: True or False?
True (0.8872045854516336)
Jessica has motive: True or False?
True (0.9340350654042096)
Jessica has opportunity: True or False?
True (0.9319595118562682)
Percy Wellington is guilty: True or False?
True (0.9383503780077049)
Percy Wellington has mean: True or False?
True (0.8852352523606669)
Percy Wellington has motive: True or False?
True (0.8998277786460391)
Percy Wellington has opportunity: True or False?
True (0.9388008138003494)
### Angelita
- mean: False (0.12830650990758052)
- motive: False (0.13753252982096553)
- opportunity: False (0.09170692950799786)

### Emily
- mean: True (0.8862236142219189)
- motive: True (0.9180403984176693)
- opportunity: True (0.950041474283655)

### Jessica
- mean: False (0.11279541454836639)
- motive: False (0.06596493459579045)
- opportunity: False (0.06804048814373176)

### Percy Wellington
- mean: False (0.11476474763933309)
- motive: False (0.10017222135396087)
- opportunity: False (0.06119918619965059)

The culprit is Emily.
In fact, it is Angelita.
## 5minutemystery-the-card-shark
The cowboy is guilty: True or False?
True (0.9596865178182852)
The cowboy has mean: True or False?
True (0.8955226517597132)
The cowboy has motive: True or False?
True (0.9797840121845385)
The cowboy has opportunity: True or False?
True (0.9522199020698944)
The gunslinger is guilty: True or False?
True (0.945399403620829)
The gunslinger has mean: True or False?
True (0.919930758847437)
The gunslinger has motive: True or False?
True (0.9690910565174785)
The gunslinger has opportunity: True or False?
True (0.9584600345758558)
The lady is guilty: True or False?
True (0.9554855815192022)
The lady has mean: True or False?
True (0.8539127077831877)
The lady has motive: True or False?
True (0.9648551350350516)
The lady has opportunity: True or False?
True (0.8633915828320894)
The sheriff is guilty: True or False?
True (0.9319595674053855)
The sheriff has mean: True or False?
True (0.8740772044235984)
The sheriff has motive: True or False?
True (0.9690910565174785)
The sheriff has opportunity: True or False?
True (0.928538502080124)
### The cowboy
- mean: False (0.10447734824028676)
- motive: False (0.020215987815461522)
- opportunity: False (0.047780097930105625)

### The gunslinger
- mean: True (0.919930758847437)
- motive: True (0.9690910565174785)
- opportunity: True (0.9584600345758558)

### The lady
- mean: False (0.14608729221681227)
- motive: False (0.0351448649649484)
- opportunity: False (0.1366084171679106)

### The sheriff
- mean: False (0.12592279557640162)
- motive: False (0.03090894348252149)
- opportunity: False (0.071461497919876)

The culprit is The gunslinger.
In fact, it is The sheriff.
## 5minutemystery-department-store-murder
Ed Puckett is guilty: True or False?
True (0.9167081124681512)
Ed Puckett has mean: True or False?
True (0.6592954931819778)
Ed Puckett has motive: True or False?
True (0.9505947844514345)
Ed Puckett has opportunity: True or False?
True (0.7725306828324007)
Gene Roberts is guilty: True or False?
True (0.8031737798924701)
Gene Roberts has mean: True or False?
False (0.5019531141001669)
Gene Roberts has motive: True or False?
True (0.8879840376027315)
Gene Roberts has opportunity: True or False?
True (0.8683809699466569)
George Whitley is guilty: True or False?
True (0.8803863464576128)
George Whitley has mean: True or False?
True (0.6859494535376744)
George Whitley has motive: True or False?
True (0.8879840376027315)
George Whitley has opportunity: True or False?
True (0.6252092625510083)
Justin Tanner is guilty: True or False?
True (0.8365545874520802)
Justin Tanner has mean: True or False?
True (0.7379143332111532)
Map:  32%|███▏      | 64/203 [1:26:14<2:49:32, 73.18s/ examples]Map:  32%|███▏      | 65/203 [1:27:25<2:46:47, 72.52s/ examples]Map:  33%|███▎      | 66/203 [1:28:35<2:43:28, 71.59s/ examples]Map:  33%|███▎      | 67/203 [1:29:24<2:27:02, 64.87s/ examples]Map:  33%|███▎      | 68/203 [1:30:26<2:23:54, 63.96s/ examples]Justin Tanner has motive: True or False?
True (0.940789698413215)
Justin Tanner has opportunity: True or False?
True (0.8762112821835625)
### Ed Puckett
- mean: False (0.3407045068180222)
- motive: False (0.04940521554856547)
- opportunity: False (0.22746931716759933)

### Gene Roberts
- mean: False (0.5019531141001669)
- motive: False (0.11201596239726852)
- opportunity: False (0.13161903005334308)

### George Whitley
- mean: False (0.31405054646232555)
- motive: False (0.11201596239726852)
- opportunity: False (0.3747907374489917)

### Justin Tanner
- mean: True (0.7379143332111532)
- motive: True (0.940789698413215)
- opportunity: True (0.8762112821835625)

The culprit is Justin Tanner.
In fact, it is Justin Tanner.
## 5minutemystery-the-candy-store-mystery
Brianna Cates is guilty: True or False?
True (0.961024938565791)
Brianna Cates has mean: True or False?
True (0.9008791478232747)
Brianna Cates has motive: True or False?
True (0.9150529491683197)
Brianna Cates has opportunity: True or False?
True (0.8936811689868521)
Emilee Johnson is guilty: True or False?
True (0.9622497571173928)
Emilee Johnson has mean: True or False?
True (0.9378968460746586)
Emilee Johnson has motive: True or False?
True (0.9756234297188763)
Emilee Johnson has opportunity: True or False?
True (0.9558166865608263)
Justin Cates is guilty: True or False?
True (0.9569571625798028)
Justin Cates has mean: True or False?
True (0.9219218506394821)
Justin Cates has motive: True or False?
True (0.9312127242200585)
Justin Cates has opportunity: True or False?
True (0.944176853162527)
Olivia (Livvie) Johnson is guilty: True or False?
True (0.960804880888677)
Olivia (Livvie) Johnson has mean: True or False?
True (0.9235923286659299)
Olivia (Livvie) Johnson has motive: True or False?
True (0.9445872321654378)
Olivia (Livvie) Johnson has opportunity: True or False?
True (0.9082930704920021)
Trevor Cates is guilty: True or False?
True (0.9655115024177445)
Trevor Cates has mean: True or False?
True (0.8912444106095914)
Trevor Cates has motive: True or False?
True (0.9602122316574973)
Trevor Cates has opportunity: True or False?
True (0.854884620116169)
### Brianna Cates
- mean: False (0.09912085217672528)
- motive: False (0.0849470508316803)
- opportunity: False (0.10631883101314787)

### Emilee Johnson
- mean: True (0.9378968460746586)
- motive: True (0.9756234297188763)
- opportunity: True (0.9558166865608263)

### Justin Cates
- mean: False (0.07807814936051793)
- motive: False (0.06878727577994148)
- opportunity: False (0.055823146837473026)

### Olivia (Livvie) Johnson
- mean: False (0.07640767133407012)
- motive: False (0.05541276783456217)
- opportunity: False (0.09170692950799786)

### Trevor Cates
- mean: False (0.10875558939040864)
- motive: False (0.03978776834250275)
- opportunity: False (0.14511537988383105)

The culprit is Emilee Johnson.
In fact, it is Justin Cates.
## 5minutemystery-for-the-birds
Billy Mumms is guilty: True or False?
True (0.8778961263000082)
Billy Mumms has mean: True or False?
True (0.7655933544531522)
Billy Mumms has motive: True or False?
True (0.8244619332958376)
Billy Mumms has opportunity: True or False?
True (0.9353465445225602)
Cheryl Judson is guilty: True or False?
True (0.9326989624184171)
Cheryl Judson has mean: True or False?
True (0.7490872087035162)
Cheryl Judson has motive: True or False?
True (0.8940517282497483)
Cheryl Judson has opportunity: True or False?
True (0.9427180278987515)
Stan Mifflin is guilty: True or False?
True (0.8929365260632085)
Stan Mifflin has mean: True or False?
True (0.7662936378892937)
Stan Mifflin has motive: True or False?
True (0.934872446722342)
Stan Mifflin has opportunity: True or False?
True (0.9693242313725606)
Tor Hansen is guilty: True or False?
True (0.8198933606225757)
Tor Hansen has mean: True or False?
True (0.9946713536393796)
Tor Hansen has motive: True or False?
True (0.8272706865691472)
Tor Hansen has opportunity: True or False?
True (0.9073122118500465)
### Billy Mumms
- mean: False (0.23440664554684776)
- motive: False (0.1755380667041624)
- opportunity: False (0.06465345547743984)

### Cheryl Judson
- mean: False (0.2509127912964838)
- motive: False (0.10594827175025168)
- opportunity: False (0.057281972101248524)

### Stan Mifflin
- mean: False (0.23370636211070628)
- motive: False (0.06512755327765796)
- opportunity: False (0.03067576862743937)

### Tor Hansen
- mean: True (0.9946713536393796)
- motive: True (0.8272706865691472)
- opportunity: True (0.9073122118500465)

The culprit is Tor Hansen.
In fact, it is Cheryl Judson.
## 5minutemystery-the-zoo-job
Cindy is guilty: True or False?
True (0.883638205304735)
Cindy has mean: True or False?
True (0.8074606715677252)
Cindy has motive: True or False?
True (0.9114953293645017)
Cindy has opportunity: True or False?
True (0.7969253675907205)
Henry is guilty: True or False?
True (0.8797679608387514)
Henry has mean: True or False?
True (0.7634837587244478)
Henry has motive: True or False?
True (0.9435560124549824)
Henry has opportunity: True or False?
True (0.8300437258865985)
Leonard is guilty: True or False?
True (0.8418256636710214)
Leonard has mean: True or False?
True (0.8000678954040312)
Leonard has motive: True or False?
True (0.947962222968318)
Leonard has opportunity: True or False?
True (0.8899121304559661)
Tom is guilty: True or False?
True (0.8725647371909419)
Tom has mean: True or False?
True (0.8927496657814362)
Tom has motive: True or False?
True (0.9335520893498362)
Tom has opportunity: True or False?
True (0.8980534699860239)
### Cindy
- mean: False (0.19253932843227484)
- motive: False (0.08850467063549827)
- opportunity: False (0.20307463240927948)

### Henry
- mean: False (0.23651624127555215)
- motive: False (0.05644398754501756)
- opportunity: False (0.16995627411340153)

### Leonard
- mean: False (0.19993210459596877)
- motive: False (0.052037777031682)
- opportunity: False (0.11008786954403393)

### Tom
- mean: True (0.8927496657814362)
- motive: True (0.9335520893498362)
- opportunity: True (0.8980534699860239)

The culprit is Tom.
In fact, it is Cindy.
## 5minutemystery-did-the-vicar-solve-the-mystery
Elmer Tydings is guilty: True or False?
True (0.9820138217808033)
Elmer Tydings has mean: True or False?
True (0.9743860965141968)
Elmer Tydings has motive: True or False?
True (0.9902445073767759)
Elmer Tydings has opportunity: True or False?
True (0.9643214331583058)
John Stubbs is guilty: True or False?
True (0.9787533276905257)
John Stubbs has mean: True or False?
True (0.981021999947924)
John Stubbs has motive: True or False?
True (0.9832306498689419)
John Stubbs has opportunity: True or False?
True (0.9651190622502646)
Katherine Tydings is guilty: True or False?
True (0.9752489919994439)
Katherine Tydings has mean: True or False?
True (0.9752018447706344)
Katherine Tydings has motive: True or False?
True (0.9885914322998767)
Katherine Tydings has opportunity: True or False?
True (0.9724147321673792)
Louise Stubbs is guilty: True or False?
True (0.9606574760904091)
Louise Stubbs has mean: True or False?
True (0.9420819287658885)
Louise Stubbs has motive: True or False?
True (0.9738940592742902)
Louise Stubbs has opportunity: True or False?
True (0.9666631825345839)
### Elmer Tydings
- mean: False (0.02561390348580317)
- motive: False (0.00975549262322406)
- opportunity: False (0.03567856684169424)

### John Stubbs
- mean: False (0.01897800005207595)
- motive: False (0.01676935013105807)
- opportunity: False (0.03488093774973544)

### Katherine Tydings
- mean: True (0.9752018447706344)
- motive: True (0.9885914322998767)
- opportunity: True (0.9724147321673792)

### Louise Stubbs
- mean: False (0.05791807123411152)
- motive: False (0.02610594072570982)
- opportunity: False (0.03333681746541606)

The culprit is Katherine Tydings.
In fact, it is Katherine Tydings.
## 5minutemystery-who-scratched-the-porsche
Colonel Greenerbaum is guilty: True or False?
True (0.9113376113103917)
Colonel Greenerbaum has mean: True or False?
True (0.8840392254230673)
Colonel Greenerbaum has motive: True or False?
True (0.9452984928501705)
Colonel Greenerbaum has opportunity: True or False?
True (0.8697145551802641)
Map:  34%|███▍      | 69/203 [1:31:31<2:23:29, 64.25s/ examples]Map:  34%|███▍      | 70/203 [1:32:20<2:12:42, 59.87s/ examples]Map:  35%|███▍      | 71/203 [1:33:05<2:01:25, 55.19s/ examples]Map:  35%|███▌      | 72/203 [1:33:54<1:56:50, 53.51s/ examples]Fido is guilty: True or False?
False (0.8481214046032184)
Fido has mean: True or False?
False (2.821102743875856)
Fido has motive: True or False?
False (1.7946410176084657)
Fido has opportunity: True or False?
False (1.792952879485295)
Malcolm is guilty: True or False?
True (0.8998277786460391)
Malcolm has mean: True or False?
True (0.9353465445225602)
Malcolm has motive: True or False?
True (0.897695304229796)
Malcolm has opportunity: True or False?
True (0.9036349079321685)
Roxie is guilty: True or False?
True (0.8980535302052036)
Roxie has mean: True or False?
True (0.673191669892235)
Roxie has motive: True or False?
True (0.904313027820426)
Roxie has opportunity: True or False?
True (0.8444089912414552)
### Colonel Greenerbaum
- mean: False (0.11596077457693266)
- motive: False (0.054701507149829465)
- opportunity: False (0.13028544481973592)

### Fido
- mean: False (2.821102743875856)
- motive: False (1.7946410176084657)
- opportunity: False (1.792952879485295)

### Malcolm
- mean: True (0.9353465445225602)
- motive: True (0.897695304229796)
- opportunity: True (0.9036349079321685)

### Roxie
- mean: False (0.326808330107765)
- motive: False (0.095686972179574)
- opportunity: False (0.1555910087585448)

The culprit is Malcolm.
In fact, it is Colonel Greenerbaum.
## 5minutemystery-the-thief-in-the-night-mystery
Jon Shaw is guilty: True or False?
True (0.8697145551802641)
Jon Shaw has mean: True or False?
True (0.8381505623254643)
Jon Shaw has motive: True or False?
True (0.9318356525033217)
Jon Shaw has opportunity: True or False?
True (0.7512834059294674)
Max Reinke is guilty: True or False?
True (0.884439109617765)
Max Reinke has mean: True or False?
True (0.9324533354081785)
Max Reinke has motive: True or False?
True (0.9456006903352807)
Max Reinke has opportunity: True or False?
True (0.9471859926317535)
Todd Summers is guilty: True or False?
True (0.7348812840309261)
Todd Summers has mean: True or False?
True (0.7988152492192591)
Todd Summers has motive: True or False?
True (0.905989824801558)
Todd Summers has opportunity: True or False?
True (0.6415346823638186)
Zac Coulson is guilty: True or False?
True (0.9575961815839735)
Zac Coulson has mean: True or False?
True (0.8980534699860239)
Zac Coulson has motive: True or False?
True (0.9761291751471208)
Zac Coulson has opportunity: True or False?
True (0.8918110138739693)
### Jon Shaw
- mean: False (0.16184943767453575)
- motive: False (0.06816434749667832)
- opportunity: False (0.2487165940705326)

### Max Reinke
- mean: True (0.9324533354081785)
- motive: True (0.9456006903352807)
- opportunity: True (0.9471859926317535)

### Todd Summers
- mean: False (0.20118475078074094)
- motive: False (0.09401017519844201)
- opportunity: False (0.3584653176361814)

### Zac Coulson
- mean: False (0.10194653001397613)
- motive: False (0.02387082485287917)
- opportunity: False (0.10818898612603067)

The culprit is Max Reinke.
In fact, it is Zac Coulson.
## 5minutemystery-ladies-at-table
Alice is guilty: True or False?
True (0.779321849347754)
Alice has mean: True or False?
False (0.5431680717579583)
Alice has motive: True or False?
True (0.9167080509980843)
Alice has opportunity: True or False?
True (0.9230391416137353)
Frances is guilty: True or False?
True (0.8311430212356835)
Frances has mean: True or False?
True (0.7256486384635821)
Frances has motive: True or False?
True (0.905989824801558)
Frances has opportunity: True or False?
True (0.8925625120974553)
Leona is guilty: True or False?
True (0.8852351930010195)
Leona has mean: True or False?
True (0.847967740521315)
Leona has motive: True or False?
True (0.9319595674053855)
Leona has opportunity: True or False?
True (0.9516839395409852)
Mary is guilty: True or False?
True (0.821044090050916)
Mary has mean: True or False?
True (0.7988153087356352)
Mary has motive: True or False?
True (0.8633915828320894)
Mary has opportunity: True or False?
True (0.893681109060862)
Ruth is guilty: True or False?
True (0.7008948290825966)
Ruth has mean: True or False?
True (0.8502200206694925)
Ruth has motive: True or False?
True (0.9323301884216684)
Ruth has opportunity: True or False?
True (0.9173026661190045)
### Alice
- mean: False (0.5431680717579583)
- motive: False (0.08329194900191572)
- opportunity: False (0.07696085838626465)

### Frances
- mean: False (0.2743513615364179)
- motive: False (0.09401017519844201)
- opportunity: False (0.1074374879025447)

### Leona
- mean: True (0.847967740521315)
- motive: True (0.9319595674053855)
- opportunity: True (0.9516839395409852)

### Mary
- mean: False (0.20118469126436478)
- motive: False (0.1366084171679106)
- opportunity: False (0.10631889093913804)

### Ruth
- mean: False (0.14977997933050746)
- motive: False (0.06766981157833163)
- opportunity: False (0.08269733388099554)

The culprit is Leona.
In fact, it is Leona.
## 5minutemystery-the-diamond-necklace
Abby Grant is guilty: True or False?
True (0.9336731438527403)
Abby Grant has mean: True or False?
True (0.7859664553110391)
Abby Grant has motive: True or False?
True (0.9753900767342161)
Abby Grant has opportunity: True or False?
True (0.9572778330298248)
Colonel Barrow is guilty: True or False?
True (0.8568122940392877)
Colonel Barrow has mean: True or False?
True (0.5214711377329961)
Colonel Barrow has motive: True or False?
True (0.9787938590250385)
Colonel Barrow has opportunity: True or False?
True (0.983214557402718)
Fiona Duncan is guilty: True or False?
False (0.8554494017777171)
Fiona Duncan has mean: True or False?
False (0.9530570094344373)
Fiona Duncan has motive: True or False?
False (1.6622269950246393)
Fiona Duncan has opportunity: True or False?
False (0.9353123000985991)
Harold Duncan is guilty: True or False?
True (0.9066531077351827)
Harold Duncan has mean: True or False?
True (0.8074605993751186)
Harold Duncan has motive: True or False?
True (0.971019387667922)
Harold Duncan has opportunity: True or False?
True (0.9233161821369215)
Maurice Eades is guilty: True or False?
True (0.9276259554905466)
Maurice Eades has mean: True or False?
False (0.5312093941731293)
Maurice Eades has motive: True or False?
True (0.9819446807697475)
Maurice Eades has opportunity: True or False?
True (0.9756698013402983)
### Abby Grant
- mean: True (0.7859664553110391)
- motive: True (0.9753900767342161)
- opportunity: True (0.9572778330298248)

### Colonel Barrow
- mean: False (0.47852886226700386)
- motive: False (0.02120614097496154)
- opportunity: False (0.016785442597281985)

### Fiona Duncan
- mean: False (0.9530570094344373)
- motive: False (1.6622269950246393)
- opportunity: False (0.9353123000985991)

### Harold Duncan
- mean: False (0.1925394006248814)
- motive: False (0.02898061233207805)
- opportunity: False (0.07668381786307854)

### Maurice Eades
- mean: False (0.5312093941731293)
- motive: False (0.018055319230252498)
- opportunity: False (0.024330198659701652)

The culprit is Abby Grant.
In fact, it is Fiona Duncan.
## 5minutemystery-rhyming-presidents-mystery
George Bush is guilty: True or False?
True (0.8832359917473193)
George Bush has mean: True or False?
True (0.5860491337676195)
George Bush has motive: True or False?
True (0.9086178579521682)
George Bush has opportunity: True or False?
True (0.7379142672364736)
Gerald Ford is guilty: True or False?
True (0.8955227118091885)
Gerald Ford has mean: True or False?
True (0.7264255794048772)
Gerald Ford has motive: True or False?
True (0.9005298588820442)
Gerald Ford has opportunity: True or False?
True (0.6984322578436808)
John Quincy Adams is guilty: True or False?
True (0.8519527857346616)
John Quincy Adams has mean: True or False?
True (0.6095241271158658)
John Quincy Adams has motive: True or False?
True (0.878314250659373)
John Quincy Adams has opportunity: True or False?
True (0.6113820047705449)
Richard Nixon is guilty: True or False?
True (0.8624675215861032)
Richard Nixon has mean: True or False?
True (0.7606506318580792)
Richard Nixon has motive: True or False?
True (0.9244151684978138)
Richard Nixon has opportunity: True or False?
True (0.7745833916423246)
### George Bush
- mean: False (0.41395086623238053)
- motive: False (0.0913821420478318)
Map:  36%|███▌      | 73/203 [1:34:41<1:51:18, 51.37s/ examples]Map:  36%|███▋      | 74/203 [1:35:38<1:54:05, 53.07s/ examples]Map:  37%|███▋      | 75/203 [1:36:35<1:55:40, 54.22s/ examples]Map:  37%|███▋      | 76/203 [1:37:26<1:53:08, 53.46s/ examples]Map:  38%|███▊      | 77/203 [1:38:36<2:02:40, 58.42s/ examples]- opportunity: False (0.2620857327635264)

### Gerald Ford
- mean: False (0.2735744205951228)
- motive: False (0.09947014111795582)
- opportunity: False (0.3015677421563192)

### John Quincy Adams
- mean: False (0.3904758728841342)
- motive: False (0.12168574934062704)
- opportunity: False (0.38861799522945506)

### Richard Nixon
- mean: True (0.7606506318580792)
- motive: True (0.9244151684978138)
- opportunity: True (0.7745833916423246)

The culprit is Richard Nixon.
In fact, it is Gerald Ford.
## 5minutemystery-the-white-house-ghosts
Andrew Jackson is guilty: True or False?
True (0.8606036289596553)
Andrew Jackson has mean: True or False?
True (0.9358173616900589)
Andrew Jackson has motive: True or False?
True (0.9798997635332343)
Andrew Jackson has opportunity: True or False?
True (0.9124361266596831)
Calvin Coolidge is guilty: True or False?
True (0.9142907234091052)
Calvin Coolidge has mean: True or False?
True (0.950777887812089)
Calvin Coolidge has motive: True or False?
True (0.9694401031032759)
Calvin Coolidge has opportunity: True or False?
True (0.952041865762172)
John Adams is guilty: True or False?
True (0.9190633328333496)
John Adams has mean: True or False?
True (0.9716717007848752)
John Adams has motive: True or False?
True (0.9826908710080852)
John Adams has opportunity: True or False?
True (0.9173026661190045)
William Howard Taft is guilty: True or False?
True (0.911809984585868)
William Howard Taft has mean: True or False?
True (0.9651191233711941)
William Howard Taft has motive: True or False?
True (0.9872772696831444)
William Howard Taft has opportunity: True or False?
True (0.921357630313903)
### Andrew Jackson
- mean: False (0.06418263830994109)
- motive: False (0.02010023646676573)
- opportunity: False (0.0875638733403169)

### Calvin Coolidge
- mean: False (0.04922211218791095)
- motive: False (0.030559896896724115)
- opportunity: False (0.04795813423782802)

### John Adams
- mean: False (0.028328299215124808)
- motive: False (0.017309128991914835)
- opportunity: False (0.08269733388099554)

### William Howard Taft
- mean: True (0.9651191233711941)
- motive: True (0.9872772696831444)
- opportunity: True (0.921357630313903)

The culprit is William Howard Taft.
In fact, it is Calvin Coolidge.
## 5minutemystery-mr-patrick-and-the-graveyard-mystery
Grave no.1 is guilty: True or False?
True (0.9655115024177445)
Grave no.1 has mean: True or False?
True (0.918626370973125)
Grave no.1 has motive: True or False?
True (0.953361928704124)
Grave no.1 has opportunity: True or False?
True (0.8902942539348153)
Grave no.2 is guilty: True or False?
True (0.9652503733161137)
Grave no.2 has mean: True or False?
True (0.9486325389479346)
Grave no.2 has motive: True or False?
True (0.963368656065788)
Grave no.2 has opportunity: True or False?
True (0.9155072008980665)
Grave no.3 is guilty: True or False?
True (0.9666001797251225)
Grave no.3 has mean: True or False?
True (0.9165588616316169)
Grave no.3 has motive: True or False?
True (0.958847105894029)
Grave no.3 has opportunity: True or False?
True (0.8973360043541736)
Grave no.4 is guilty: True or False?
True (0.9747731684499236)
Grave no.4 has mean: True or False?
True (0.9099070446252667)
Grave no.4 has motive: True or False?
True (0.9708540445899615)
Grave no.4 has opportunity: True or False?
True (0.8879840376027315)
Grave no.5 is guilty: True or False?
True (0.9742394081324117)
Grave no.5 has mean: True or False?
True (0.9555685526018006)
Grave no.5 has motive: True or False?
True (0.974580348460635)
Grave no.5 has opportunity: True or False?
True (0.9376689781587124)
### Grave no.1
- mean: False (0.08137362902687495)
- motive: False (0.04663807129587605)
- opportunity: False (0.10970574606518468)

### Grave no.2
- mean: False (0.051367461052065355)
- motive: False (0.03663134393421197)
- opportunity: False (0.08449279910193352)

### Grave no.3
- mean: False (0.08344113836838307)
- motive: False (0.041152894105971005)
- opportunity: False (0.1026639956458264)

### Grave no.4
- mean: False (0.09009295537473327)
- motive: False (0.029145955410038504)
- opportunity: False (0.11201596239726852)

### Grave no.5
- mean: True (0.9555685526018006)
- motive: True (0.974580348460635)
- opportunity: True (0.9376689781587124)

The culprit is Grave no.5.
In fact, it is Grave no.4.
## 5minutemystery-lockbox-100
Edward Frates is guilty: True or False?
True (0.9291837815043049)
Edward Frates has mean: True or False?
True (0.7065955344877805)
Edward Frates has motive: True or False?
True (0.9640517228653248)
Edward Frates has opportunity: True or False?
True (0.9616780268435321)
James Madigan is guilty: True or False?
True (0.8577681165234065)
James Madigan has mean: True or False?
True (0.65489470935198)
James Madigan has motive: True or False?
True (0.958537757711882)
James Madigan has opportunity: True or False?
True (0.94948238112973)
Peter Zielny is guilty: True or False?
True (0.8397339530959691)
Peter Zielny has mean: True or False?
True (0.858244061606496)
Peter Zielny has motive: True or False?
True (0.9786310784192824)
Peter Zielny has opportunity: True or False?
True (0.9695556762577888)
Ronald Finch is guilty: True or False?
True (0.9553191057869168)
Ronald Finch has mean: True or False?
True (0.9127477403975288)
Ronald Finch has motive: True or False?
True (0.9863104819435934)
Ronald Finch has opportunity: True or False?
True (0.9874235991199588)
Russell Winwood is guilty: True or False?
True (0.911809984585868)
Russell Winwood has mean: True or False?
True (0.9114953293645017)
Russell Winwood has motive: True or False?
True (0.972362279388711)
Russell Winwood has opportunity: True or False?
True (0.9577544910931239)
### Edward Frates
- mean: False (0.29340446551221955)
- motive: False (0.03594827713467519)
- opportunity: False (0.0383219731564679)

### James Madigan
- mean: False (0.34510529064802)
- motive: False (0.04146224228811801)
- opportunity: False (0.050517618870269954)

### Peter Zielny
- mean: False (0.14175593839350398)
- motive: False (0.02136892158071757)
- opportunity: False (0.030444323742211177)

### Ronald Finch
- mean: True (0.9127477403975288)
- motive: True (0.9863104819435934)
- opportunity: True (0.9874235991199588)

### Russell Winwood
- mean: False (0.08850467063549827)
- motive: False (0.027637720611288996)
- opportunity: False (0.04224550890687606)

The culprit is Ronald Finch.
In fact, it is Russell Winwood.
## 5minutemystery-mystery-at-the-detectives-office
Joe the janitor is guilty: True or False?
True (0.9268352400785028)
Joe the janitor has mean: True or False?
True (0.9053223122169206)
Joe the janitor has motive: True or False?
True (0.9538802513450514)
Joe the janitor has opportunity: True or False?
True (0.9235923286659299)
Larry is guilty: True or False?
True (0.9100670238942131)
Larry has mean: True or False?
True (0.9643214331583058)
Larry has motive: True or False?
True (0.9718859797630299)
Larry has opportunity: True or False?
True (0.9346342066470359)
Mr. Jorgensen is guilty: True or False?
True (0.866132552869269)
Mr. Jorgensen has mean: True or False?
True (0.9392480858026054)
Mr. Jorgensen has motive: True or False?
True (0.9429286143036572)
Mr. Jorgensen has opportunity: True or False?
True (0.9053223122169206)
the building manager is guilty: True or False?
True (0.860369148541484)
the building manager has mean: True or False?
True (0.720171518230031)
the building manager has motive: True or False?
True (0.9127477403975288)
the building manager has opportunity: True or False?
True (0.8031737798924701)
### Joe the janitor
- mean: False (0.09467768778307939)
- motive: False (0.04611974865494861)
- opportunity: False (0.07640767133407012)

### Larry
- mean: True (0.9643214331583058)
- motive: True (0.9718859797630299)
- opportunity: True (0.9346342066470359)

### Mr. Jorgensen
- mean: False (0.06075191419739456)
- motive: False (0.05707138569634285)
- opportunity: False (0.09467768778307939)

### the building manager
- mean: False (0.279828481769969)
- motive: False (0.08725225960247118)
- opportunity: False (0.19682622010752993)

The culprit is Larry.
In fact, it is the building manager.
## 5minutemystery-the-secret-in-the-old-trunk
Map:  38%|███▊      | 78/203 [1:39:41<2:05:20, 60.16s/ examples]Map:  39%|███▉      | 79/203 [1:40:51<2:10:54, 63.34s/ examples]Map:  39%|███▉      | 80/203 [1:41:32<1:55:38, 56.41s/ examples]Dennis Boyles is guilty: True or False?
True (0.9105454073245608)
Dennis Boyles has mean: True or False?
True (0.9417613738325554)
Dennis Boyles has motive: True or False?
True (0.9324532728823121)
Dennis Boyles has opportunity: True or False?
True (0.8795611817678315)
George Boyles is guilty: True or False?
True (0.9268353022276509)
George Boyles has mean: True or False?
True (0.9133679254389228)
George Boyles has motive: True or False?
True (0.9329437018480795)
George Boyles has opportunity: True or False?
True (0.8272706865691472)
John Boyles is guilty: True or False?
True (0.9141375412484458)
John Boyles has mean: True or False?
True (0.8854334962109398)
John Boyles has motive: True or False?
True (0.8816148581338575)
John Boyles has opportunity: True or False?
True (0.8037905715242155)
Patricia (Trish) Boyles Sykes is guilty: True or False?
True (0.8762113474663927)
Patricia (Trish) Boyles Sykes has mean: True or False?
True (0.9281487460975983)
Patricia (Trish) Boyles Sykes has motive: True or False?
True (0.9079671476237222)
Patricia (Trish) Boyles Sykes has opportunity: True or False?
True (0.9184802773231918)
Patrick Boyles is guilty: True or False?
True (0.8787311338092536)
Patrick Boyles has mean: True or False?
True (0.9003546849431159)
Patrick Boyles has motive: True or False?
True (0.8504686406728537)
Patrick Boyles has opportunity: True or False?
True (0.7981867775042927)
### Dennis Boyles
- mean: False (0.058238626167444574)
- motive: False (0.06754672711768794)
- opportunity: False (0.12043881823216851)

### George Boyles
- mean: False (0.08663207456107724)
- motive: False (0.06705629815192049)
- opportunity: False (0.17272931343085285)

### John Boyles
- mean: False (0.11456650378906019)
- motive: False (0.11838514186614246)
- opportunity: False (0.1962094284757845)

### Patricia (Trish) Boyles Sykes
- mean: True (0.9281487460975983)
- motive: True (0.9079671476237222)
- opportunity: True (0.9184802773231918)

### Patrick Boyles
- mean: False (0.09964531505688412)
- motive: False (0.14953135932714634)
- opportunity: False (0.20181322249570732)

The culprit is Patricia (Trish) Boyles Sykes.
In fact, it is Patrick Boyles.
## 5minutemystery-the-restless-ghost
Casey McCormick is guilty: True or False?
True (0.9809125656479328)
Casey McCormick has mean: True or False?
True (0.9196425103002197)
Casey McCormick has motive: True or False?
True (0.970070243275667)
Casey McCormick has opportunity: True or False?
True (0.9418684262191025)
Connie McCormick is guilty: True or False?
True (0.9676556581517683)
Connie McCormick has mean: True or False?
True (0.7090191831682278)
Connie McCormick has motive: True or False?
True (0.9543079730970608)
Connie McCormick has opportunity: True or False?
True (0.7779753136455794)
Ellen McCormick is guilty: True or False?
True (0.9799765346854967)
Ellen McCormick has mean: True or False?
True (0.866132552869269)
Ellen McCormick has motive: True or False?
True (0.9815244083320255)
Ellen McCormick has opportunity: True or False?
True (0.874934615163517)
Michael McCormick, Jr. is guilty: True or False?
True (0.971455871280406)
Michael McCormick, Jr. has mean: True or False?
True (0.8633915828320894)
Michael McCormick, Jr. has motive: True or False?
True (0.9747251273624444)
Michael McCormick, Jr. has opportunity: True or False?
True (0.941654207327861)
The ghost of Mike McCormick, Sr. is guilty: True or False?
True (0.9210740952879496)
The ghost of Mike McCormick, Sr. has mean: True or False?
True (0.8973360043541736)
The ghost of Mike McCormick, Sr. has motive: True or False?
True (0.9237300130783155)
The ghost of Mike McCormick, Sr. has opportunity: True or False?
True (0.884439109617765)
### Casey McCormick
- mean: True (0.9196425103002197)
- motive: True (0.970070243275667)
- opportunity: True (0.9418684262191025)

### Connie McCormick
- mean: False (0.29098081683177224)
- motive: False (0.045692026902939165)
- opportunity: False (0.22202468635442063)

### Ellen McCormick
- mean: False (0.13386744713073095)
- motive: False (0.018475591667974522)
- opportunity: False (0.125065384836483)

### Michael McCormick, Jr.
- mean: False (0.1366084171679106)
- motive: False (0.025274872637555568)
- opportunity: False (0.05834579267213902)

### The ghost of Mike McCormick, Sr.
- mean: False (0.1026639956458264)
- motive: False (0.07626998692168452)
- opportunity: False (0.11556089038223505)

The culprit is Casey McCormick.
In fact, it is Casey McCormick.
## 5minutemystery-the-secret-friend
Bill Baker is guilty: True or False?
True (0.8683809699466569)
Bill Baker has mean: True or False?
False (0.5427057221656224)
Bill Baker has motive: True or False?
True (0.9246876822649571)
Bill Baker has opportunity: True or False?
True (0.8227594449669557)
Harold Coker is guilty: True or False?
True (0.9362850185952675)
Harold Coker has mean: True or False?
False (0.5757329310092021)
Harold Coker has motive: True or False?
False (1.5442224925625845)
Harold Coker has opportunity: True or False?
True (0.8438950825214144)
Lyn Baker is guilty: True or False?
True (0.8906751877407573)
Lyn Baker has mean: True or False?
True (0.678326898500563)
Lyn Baker has motive: True or False?
True (0.8820219652716884)
Lyn Baker has opportunity: True or False?
True (0.6160122877297346)
Midge Coker is guilty: True or False?
True (0.9599126594957205)
Midge Coker has mean: True or False?
True (0.8902941942359355)
Midge Coker has motive: True or False?
True (0.9662834418200392)
Midge Coker has opportunity: True or False?
True (0.9175984877579624)
### Bill Baker
- mean: False (0.5427057221656224)
- motive: False (0.07531231773504288)
- opportunity: False (0.17724055503304426)

### Harold Coker
- mean: False (0.5757329310092021)
- motive: False (1.5442224925625845)
- opportunity: False (0.15610491747858557)

### Lyn Baker
- mean: False (0.32167310149943695)
- motive: False (0.11797803472831159)
- opportunity: False (0.3839877122702654)

### Midge Coker
- mean: True (0.8902941942359355)
- motive: True (0.9662834418200392)
- opportunity: True (0.9175984877579624)

The culprit is Midge Coker.
In fact, it is Midge Coker.
## 5minutemystery-the-cross-homestead-mystery
Journal entry of Edith is guilty: True or False?
True (0.9841241829125448)
Journal entry of Edith has mean: True or False?
True (0.982724071443633)
Journal entry of Edith has motive: True or False?
True (0.9908566478287073)
Journal entry of Edith has opportunity: True or False?
True (0.9456006903352807)
Journal entry of Leonard is guilty: True or False?
True (0.9862973096916147)
Journal entry of Leonard has mean: True or False?
True (0.9866748452623849)
Journal entry of Leonard has motive: True or False?
True (0.9877822992384565)
Journal entry of Leonard has opportunity: True or False?
True (0.9647888536180752)
Journal entry of Susie is guilty: True or False?
True (0.9767580632580227)
Journal entry of Susie has mean: True or False?
True (0.9761291751471208)
Journal entry of Susie has motive: True or False?
True (0.9775857921500122)
Journal entry of Susie has opportunity: True or False?
True (0.9404625306133385)
Journal entry of Victor is guilty: True or False?
True (0.9805806866861946)
Journal entry of Victor has mean: True or False?
True (0.9787533276905257)
Journal entry of Victor has motive: True or False?
True (0.9799382085917008)
Journal entry of Victor has opportunity: True or False?
True (0.9531007408873468)
Journal entry of Wilbur is guilty: True or False?
True (0.9927742482115516)
Journal entry of Wilbur has mean: True or False?
True (0.9912717340487711)
Journal entry of Wilbur has motive: True or False?
True (0.988884985036839)
Journal entry of Wilbur has opportunity: True or False?
True (0.9785901910948728)
### Journal entry of Edith
- mean: False (0.01727592855636695)
- motive: False (0.009143352171292696)
- opportunity: False (0.054399309664719286)

### Journal entry of Leonard
- mean: False (0.013325154737615086)
- motive: False (0.012217700761543493)
- opportunity: False (0.035211146381924796)

### Journal entry of Susie
- mean: False (0.02387082485287917)
- motive: False (0.02241420784998782)
- opportunity: False (0.05953746938666149)

### Journal entry of Victor
Map:  40%|███▉      | 81/203 [1:42:39<2:01:41, 59.85s/ examples]Map:  40%|████      | 82/203 [1:43:25<1:51:48, 55.44s/ examples]Map:  41%|████      | 83/203 [1:44:28<1:55:45, 57.88s/ examples]Map:  41%|████▏     | 84/203 [1:45:08<1:44:16, 52.58s/ examples]Map:  42%|████▏     | 85/203 [1:45:59<1:42:13, 51.98s/ examples]- mean: False (0.0212466723094743)
- motive: False (0.020061791408299223)
- opportunity: False (0.04689925911265325)

### Journal entry of Wilbur
- mean: True (0.9912717340487711)
- motive: True (0.988884985036839)
- opportunity: True (0.9785901910948728)

The culprit is Journal entry of Wilbur.
In fact, it is Journal entry of Leonard.
## 5minutemystery-is-it-a-wonderful-life
Dr. Gilchrest is guilty: True or False?
True (0.7918210572836727)
Dr. Gilchrest has mean: True or False?
True (0.8910549302065384)
Dr. Gilchrest has motive: True or False?
True (0.9066531077351827)
Dr. Gilchrest has opportunity: True or False?
True (0.9216401608061056)
Jonathan Cartright is guilty: True or False?
True (0.7683857617837733)
Jonathan Cartright has mean: True or False?
True (0.9145963197706802)
Jonathan Cartright has motive: True or False?
True (0.9142907234091052)
Jonathan Cartright has opportunity: True or False?
True (0.8529354311342636)
Miser James Cartright (suicide) is guilty: True or False?
True (0.8250265688168699)
Miser James Cartright (suicide) has mean: True or False?
True (0.9326989624184171)
Miser James Cartright (suicide) has motive: True or False?
True (0.920789721359066)
Miser James Cartright (suicide) has opportunity: True or False?
True (0.832781373043151)
Moira Laurie is guilty: True or False?
True (0.8494723435042196)
Moira Laurie has mean: True or False?
True (0.9360516072812131)
Moira Laurie has motive: True or False?
True (0.9252299659402181)
Moira Laurie has opportunity: True or False?
True (0.9036349079321685)
### Dr. Gilchrest
- mean: False (0.10894506979346164)
- motive: False (0.0933468922648173)
- opportunity: False (0.07835983919389444)

### Jonathan Cartright
- mean: False (0.08540368022931977)
- motive: False (0.08570927659089478)
- opportunity: False (0.14706456886573638)

### Miser James Cartright (suicide)
- mean: False (0.0673010375815829)
- motive: False (0.079210278640934)
- opportunity: False (0.16721862695684897)

### Moira Laurie
- mean: True (0.9360516072812131)
- motive: True (0.9252299659402181)
- opportunity: True (0.9036349079321685)

The culprit is Moira Laurie.
In fact, it is Moira Laurie.
## 5minutemystery-lestrade-solves-a-case
Archibald Hopkins is guilty: True or False?
True (0.9694401626921336)
Archibald Hopkins has mean: True or False?
True (0.9187722824991111)
Archibald Hopkins has motive: True or False?
True (0.9853561522937149)
Archibald Hopkins has opportunity: True or False?
True (0.9516839395409852)
Countess Mannerley is guilty: True or False?
True (0.9520419225082909)
Countess Mannerley has mean: True or False?
True (0.9205042693180057)
Countess Mannerley has motive: True or False?
True (0.9772841927877102)
Countess Mannerley has opportunity: True or False?
True (0.958226146208407)
Loralie Courtney is guilty: True or False?
True (0.9701269272790862)
Loralie Courtney has mean: True or False?
True (0.9167080509980843)
Loralie Courtney has motive: True or False?
True (0.9834386705764392)
Loralie Courtney has opportunity: True or False?
True (0.9655115024177445)
Robert Bannington is guilty: True or False?
True (0.9690910565174785)
Robert Bannington has mean: True or False?
True (0.8852351930010195)
Robert Bannington has motive: True or False?
True (0.9655764090471975)
Robert Bannington has opportunity: True or False?
True (0.9249593046682986)
### Archibald Hopkins
- mean: False (0.08122771750088886)
- motive: False (0.014643847706285129)
- opportunity: False (0.04831606045901482)

### Countess Mannerley
- mean: False (0.07949573068199434)
- motive: False (0.02271580721228983)
- opportunity: False (0.04177385379159304)

### Loralie Courtney
- mean: True (0.9167080509980843)
- motive: True (0.9834386705764392)
- opportunity: True (0.9655115024177445)

### Robert Bannington
- mean: False (0.1147648069989805)
- motive: False (0.03442359095280245)
- opportunity: False (0.07504069533170143)

The culprit is Loralie Courtney.
In fact, it is Robert Bannington.
## 5minutemystery-whole-stole-the-new-years-kiss
Danny is guilty: True or False?
True (0.847967740521315)
Danny has mean: True or False?
True (0.7162186593596369)
Danny has motive: True or False?
True (0.9435559526996434)
Danny has opportunity: True or False?
True (0.9531007408873468)
Jeremy is guilty: True or False?
True (0.9527502639818524)
Jeremy has mean: True or False?
True (0.8902942539348153)
Jeremy has motive: True or False?
True (0.9741903536012754)
Jeremy has opportunity: True or False?
True (0.9543079730970608)
RJ is guilty: True or False?
True (0.9361683754137716)
RJ has mean: True or False?
True (0.9541373270174538)
RJ has motive: True or False?
True (0.9613890640022783)
RJ has opportunity: True or False?
True (0.8918110736745599)
Reese is guilty: True or False?
True (0.8854334962109398)
Reese has mean: True or False?
True (0.8000678477162699)
Reese has motive: True or False?
True (0.9753900767342161)
Reese has opportunity: True or False?
True (0.9633685950557156)
### Danny
- mean: False (0.2837813406403631)
- motive: False (0.05644404730035657)
- opportunity: False (0.04689925911265325)

### Jeremy
- mean: True (0.8902942539348153)
- motive: True (0.9741903536012754)
- opportunity: True (0.9543079730970608)

### RJ
- mean: False (0.045862672982546204)
- motive: False (0.038610935997721696)
- opportunity: False (0.10818892632544008)

### Reese
- mean: False (0.19993215228373007)
- motive: False (0.02460992326578393)
- opportunity: False (0.03663140494428441)

The culprit is Jeremy.
In fact, it is RJ.
## 5minutemystery-the-new-years-eve-mystery
Juanita Wade is guilty: True or False?
True (0.9751071938949272)
Juanita Wade has mean: True or False?
True (0.8732148436000907)
Juanita Wade has motive: True or False?
True (0.9730876681996075)
Juanita Wade has opportunity: True or False?
True (0.9365176577773374)
Mary Beth Sloan is guilty: True or False?
True (0.9894906286737151)
Mary Beth Sloan has mean: True or False?
True (0.9655764701970907)
Mary Beth Sloan has motive: True or False?
True (0.9944666626011286)
Mary Beth Sloan has opportunity: True or False?
True (0.9714558133771256)
Noel King is guilty: True or False?
True (0.990005791112619)
Noel King has mean: True or False?
True (0.9762200121234286)
Noel King has motive: True or False?
True (0.9929950235120173)
Noel King has opportunity: True or False?
True (0.9851575496109519)
Roy Wade is guilty: True or False?
True (0.9869543914070512)
Roy Wade has mean: True or False?
True (0.6224592927728324)
Roy Wade has motive: True or False?
True (0.9826908710080852)
Roy Wade has opportunity: True or False?
True (0.9351099114717211)
Theresa King is guilty: True or False?
True (0.9871788026482293)
Theresa King has mean: True or False?
True (0.8807970862580315)
Theresa King has motive: True or False?
True (0.9843062166752533)
Theresa King has opportunity: True or False?
True (0.950041474283655)
### Juanita Wade
- mean: False (0.12678515639990928)
- motive: False (0.02691233180039254)
- opportunity: False (0.06348234222266258)

### Mary Beth Sloan
- mean: False (0.0344235298029093)
- motive: False (0.005533337398871407)
- opportunity: False (0.02854418662287439)

### Noel King
- mean: True (0.9762200121234286)
- motive: True (0.9929950235120173)
- opportunity: True (0.9851575496109519)

### Roy Wade
- mean: False (0.3775407072271676)
- motive: False (0.017309128991914835)
- opportunity: False (0.06489008852827893)

### Theresa King
- mean: False (0.11920291374196845)
- motive: False (0.01569378332474669)
- opportunity: False (0.04995852571634496)

The culprit is Noel King.
In fact, it is Mary Beth Sloan.
## 5minutemystery-the-twelfth-night-mystery
Balthasar is guilty: True or False?
True (0.8944211616820568)
Balthasar has mean: True or False?
True (0.8294919722593475)
Balthasar has motive: True or False?
True (0.9119669214647611)
Balthasar has opportunity: True or False?
True (0.7655933544531522)
Caspar is guilty: True or False?
True (0.9155072554665495)
Caspar has mean: True or False?
True (0.7697732451157533)
Caspar has motive: True or False?
True (0.9605096001181298)
Caspar has opportunity: True or False?
True (0.8354835531737983)
Dad is guilty: True or False?
True (0.920789721359066)
Map:  42%|████▏     | 86/203 [1:46:43<1:36:27, 49.47s/ examples]Map:  43%|████▎     | 87/203 [1:47:33<1:36:28, 49.90s/ examples]Map:  43%|████▎     | 88/203 [1:48:45<1:48:03, 56.38s/ examples]Map:  44%|████▍     | 89/203 [1:50:07<2:01:29, 63.95s/ examples]Dad has mean: True or False?
True (0.8984105603938967)
Dad has motive: True or False?
True (0.9623205675054309)
Dad has opportunity: True or False?
True (0.894973220907352)
Melchoir is guilty: True or False?
True (0.9158089188126235)
Melchoir has mean: True or False?
True (0.9049869164790318)
Melchoir has motive: True or False?
True (0.9635748275768365)
Melchoir has opportunity: True or False?
True (0.9039745373919651)
### Balthasar
- mean: False (0.17050802774065255)
- motive: False (0.0880330785352389)
- opportunity: False (0.23440664554684776)

### Caspar
- mean: False (0.2302267548842467)
- motive: False (0.0394903998818702)
- opportunity: False (0.1645164468262017)

### Dad
- mean: False (0.10158943960610334)
- motive: False (0.037679432494569065)
- opportunity: False (0.10502677909264801)

### Melchoir
- mean: True (0.9049869164790318)
- motive: True (0.9635748275768365)
- opportunity: True (0.9039745373919651)

The culprit is Melchoir.
In fact, it is Caspar.
## 5minutemystery-sugar-lands-candy-crook
King Ted is guilty: True or False?
False (0.9425067301242699)
King Ted has mean: True or False?
False (0.8906751877407573)
King Ted has motive: True or False?
False (0.9392481417861557)
King Ted has opportunity: True or False?
False (0.8086723099497763)
Lancelot is guilty: True or False?
False (0.8606036289596553)
Lancelot has mean: True or False?
False (0.8464508054137014)
Lancelot has motive: True or False?
False (0.789233749534095)
Lancelot has opportunity: True or False?
False (0.6334102859975052)
Pride is guilty: True or False?
False (0.8958876133958744)
Pride has mean: True or False?
False (0.740174341079517)
Pride has motive: True or False?
False (0.8283842201397164)
Pride has opportunity: True or False?
False (0.555435228101316)
Rupert is guilty: True or False?
False (0.8803863464576128)
Rupert has mean: True or False?
False (0.8710367026584496)
Rupert has motive: True or False?
False (0.6723316913929156)
Rupert has opportunity: True or False?
True (0.5583270361921496)
### King Ted
- mean: False (0.8906751877407573)
- motive: False (0.9392481417861557)
- opportunity: False (0.8086723099497763)

### Lancelot
- mean: False (0.8464508054137014)
- motive: False (0.789233749534095)
- opportunity: False (0.6334102859975052)

### Pride
- mean: False (0.740174341079517)
- motive: False (0.8283842201397164)
- opportunity: False (0.555435228101316)

### Rupert
- mean: True (0.12896329734155043)
- motive: True (0.3276683086070844)
- opportunity: True (0.5583270361921496)

The culprit is Rupert.
In fact, it is King Ted.
## 5minutemystery-what-the-dickensa-christmas-eve-mystery
Fagin is guilty: True or False?
False (1.783197962502115)
Fagin has mean: True or False?
True (0.9405717864730483)
Fagin has motive: True or False?
False (2.308052201328324)
Fagin has opportunity: True or False?
False (2.7818942645849876)
Nancy is guilty: True or False?
True (0.9378969089655451)
Nancy has mean: True or False?
True (0.9149009617112335)
Nancy has motive: True or False?
True (0.9731387498951102)
Nancy has opportunity: True or False?
True (0.9396923783210908)
Oliver Twist is guilty: True or False?
True (0.9252299659402181)
Oliver Twist has mean: True or False?
True (0.8929365260632085)
Oliver Twist has motive: True or False?
True (0.9761291751471208)
Oliver Twist has opportunity: True or False?
True (0.9563089618154458)
The Artful Dodger is guilty: True or False?
True (0.9712384344135814)
The Artful Dodger has mean: True or False?
True (0.948346255948953)
The Artful Dodger has motive: True or False?
True (0.9866234067972167)
The Artful Dodger has opportunity: True or False?
True (0.9789956218205105)
The Rich Gentleman is guilty: True or False?
True (0.94620036983)
The Rich Gentleman has mean: True or False?
True (0.9127477403975288)
The Rich Gentleman has motive: True or False?
True (0.9826576716941837)
The Rich Gentleman has opportunity: True or False?
True (0.9664105191028597)
### Fagin
- mean: False (0.05942821352695171)
- motive: False (2.308052201328324)
- opportunity: False (2.7818942645849876)

### Nancy
- mean: False (0.08509903828876653)
- motive: False (0.026861250104889822)
- opportunity: False (0.06030762167890924)

### Oliver Twist
- mean: False (0.1070634739367915)
- motive: False (0.02387082485287917)
- opportunity: False (0.04369103818455422)

### The Artful Dodger
- mean: True (0.948346255948953)
- motive: True (0.9866234067972167)
- opportunity: True (0.9789956218205105)

### The Rich Gentleman
- mean: False (0.08725225960247118)
- motive: False (0.01734232830581628)
- opportunity: False (0.03358948089714031)

The culprit is The Artful Dodger.
In fact, it is The Rich Gentleman.
## 5minutemystery-the-secret-santa-mystery
Al Busby is guilty: True or False?
True (0.9407897579933674)
Al Busby has mean: True or False?
True (0.8858291535164952)
Al Busby has motive: True or False?
True (0.9532750262379774)
Al Busby has opportunity: True or False?
True (0.8774768149941248)
Bob (Bobby) Key is guilty: True or False?
True (0.9739932421876873)
Bob (Bobby) Key has mean: True or False?
True (0.9196425651151865)
Bob (Bobby) Key has motive: True or False?
True (0.9635748850103736)
Bob (Bobby) Key has opportunity: True or False?
True (0.9238675252821831)
Chuck Daughtry is guilty: True or False?
True (0.9449946880768697)
Chuck Daughtry has mean: True or False?
True (0.8316905440184192)
Chuck Daughtry has motive: True or False?
True (0.943970619289785)
Chuck Daughtry has opportunity: True or False?
True (0.8643104392003704)
Jeff Reynolds is guilty: True or False?
True (0.9813464881551738)
Jeff Reynolds has mean: True or False?
True (0.9775000208126312)
Jeff Reynolds has motive: True or False?
True (0.9934927819342948)
Jeff Reynolds has opportunity: True or False?
True (0.9705764057188281)
Jim Dockery is guilty: True or False?
True (0.9448931235445592)
Jim Dockery has mean: True or False?
True (0.8454326959560526)
Jim Dockery has motive: True or False?
True (0.9639160647221925)
Jim Dockery has opportunity: True or False?
True (0.8812065732757132)
### Al Busby
- mean: False (0.11417084648350484)
- motive: False (0.04672497376202256)
- opportunity: False (0.12252318500587522)

### Bob (Bobby) Key
- mean: False (0.0803574348848135)
- motive: False (0.03642511498962642)
- opportunity: False (0.07613247471781692)

### Chuck Daughtry
- mean: False (0.16830945598158076)
- motive: False (0.056029380710215015)
- opportunity: False (0.13568956079962957)

### Jeff Reynolds
- mean: True (0.9775000208126312)
- motive: True (0.9934927819342948)
- opportunity: True (0.9705764057188281)

### Jim Dockery
- mean: False (0.15456730404394736)
- motive: False (0.03608393527780751)
- opportunity: False (0.11879342672428683)

The culprit is Jeff Reynolds.
In fact, it is Jim Dockery.
## 5minutemystery-the-silly-santa-mystery
Mr. Corrigan is guilty: True or False?
True (0.6876299924560524)
Mr. Corrigan has mean: True or False?
True (0.5660185351323219)
Mr. Corrigan has motive: True or False?
True (0.9034646765933593)
Mr. Corrigan has opportunity: True or False?
True (0.7453983509653428)
Mrs. Martin is guilty: True or False?
True (0.8577680653964441)
Mrs. Martin has mean: True or False?
True (0.7348812840309261)
Mrs. Martin has motive: True or False?
True (0.9414391533604212)
Mrs. Martin has opportunity: True or False?
True (0.821044090050916)
Santa Claus is guilty: True or False?
True (0.7882573622725895)
Santa Claus has mean: True or False?
True (0.6297746298200823)
Santa Claus has motive: True or False?
True (0.8638516611889259)
Santa Claus has opportunity: True or False?
True (0.7606506998655483)
The photographer is guilty: True or False?
True (0.9020932932190145)
The photographer has mean: True or False?
True (0.7683857617837733)
The photographer has motive: True or False?
True (0.91321325132378)
The photographer has opportunity: True or False?
True (0.8785228704171453)
### Mr. Corrigan
- mean: False (0.4339814648676781)
- motive: False (0.09653532340664073)
- opportunity: False (0.2546016490346572)

### Mrs. Martin
- mean: False (0.2651187159690739)
- motive: False (0.058560846639578834)
- opportunity: False (0.17895590994908395)

### Santa Claus
Map:  44%|████▍     | 90/203 [1:51:20<2:05:36, 66.69s/ examples]Map:  45%|████▍     | 91/203 [1:52:14<1:57:38, 63.03s/ examples]Map:  45%|████▌     | 92/203 [1:53:04<1:49:21, 59.11s/ examples]Map:  46%|████▌     | 93/203 [1:53:56<1:44:18, 56.90s/ examples]Map:  46%|████▋     | 94/203 [1:54:48<1:40:59, 55.59s/ examples]- mean: False (0.37022537017991775)
- motive: False (0.13614833881107413)
- opportunity: False (0.23934930013445166)

### The photographer
- mean: True (0.7683857617837733)
- motive: True (0.91321325132378)
- opportunity: True (0.8785228704171453)

The culprit is The photographer.
In fact, it is The photographer.
## 5minutemystery-sky-jack
Clem Duster is guilty: True or False?
True (0.9531007408873468)
Clem Duster has mean: True or False?
True (0.7577943897558946)
Clem Duster has motive: True or False?
True (0.9808759696772071)
Clem Duster has opportunity: True or False?
True (0.9205042693180057)
Cliff Snelling is guilty: True or False?
True (0.9235923286659299)
Cliff Snelling has mean: True or False?
True (0.6706082735718226)
Cliff Snelling has motive: True or False?
True (0.976535319718931)
Cliff Snelling has opportunity: True or False?
True (0.8745065279415651)
David Loftkiss is guilty: True or False?
True (0.9383503780077049)
David Loftkiss has mean: True or False?
True (0.6817267994905651)
David Loftkiss has motive: True or False?
True (0.9571978443343412)
David Loftkiss has opportunity: True or False?
True (0.8198932995357624)
Tom Jenks is guilty: True or False?
True (0.9391365661970741)
Tom Jenks has mean: True or False?
True (0.7065954713132195)
Tom Jenks has motive: True or False?
True (0.9706321357771589)
Tom Jenks has opportunity: True or False?
True (0.842345065078002)
### Clem Duster
- mean: True (0.7577943897558946)
- motive: True (0.9808759696772071)
- opportunity: True (0.9205042693180057)

### Cliff Snelling
- mean: False (0.3293917264281774)
- motive: False (0.02346468028106896)
- opportunity: False (0.12549347205843486)

### David Loftkiss
- mean: False (0.31827320050943486)
- motive: False (0.042802155665658814)
- opportunity: False (0.1801067004642376)

### Tom Jenks
- mean: False (0.29340452868678046)
- motive: False (0.0293678642228411)
- opportunity: False (0.157654934921998)

The culprit is Clem Duster.
In fact, it is Tom Jenks.
## 5minutemystery-dr-watson-and-the-thwarted-engagement
Georgette Pelham is guilty: True or False?
True (0.9831822505619944)
Georgette Pelham has mean: True or False?
True (0.9652503733161137)
Georgette Pelham has motive: True or False?
True (0.9947186709118788)
Georgette Pelham has opportunity: True or False?
True (0.9622497571173928)
Reverend Marvin Ingalls is guilty: True or False?
True (0.9771973485275812)
Reverend Marvin Ingalls has mean: True or False?
True (0.9114953293645017)
Reverend Marvin Ingalls has motive: True or False?
True (0.9944478272754128)
Reverend Marvin Ingalls has opportunity: True or False?
True (0.9731388097113137)
Sheila Ingalls is guilty: True or False?
True (0.9821169963689194)
Sheila Ingalls has mean: True or False?
True (0.9529258626138675)
Sheila Ingalls has motive: True or False?
True (0.9932156800207016)
Sheila Ingalls has opportunity: True or False?
True (0.9698996547102765)
Wallace Anders is guilty: True or False?
True (0.9575961815839735)
Wallace Anders has mean: True or False?
True (0.9498557456415421)
Wallace Anders has motive: True or False?
True (0.9943085313118175)
Wallace Anders has opportunity: True or False?
True (0.9749646191773192)
### Georgette Pelham
- mean: True (0.9652503733161137)
- motive: True (0.9947186709118788)
- opportunity: True (0.9622497571173928)

### Reverend Marvin Ingalls
- mean: False (0.08850467063549827)
- motive: False (0.00555217272458719)
- opportunity: False (0.026861190288686276)

### Sheila Ingalls
- mean: False (0.04707413738613253)
- motive: False (0.006784319979298403)
- opportunity: False (0.030100345289723496)

### Wallace Anders
- mean: False (0.05014425435845793)
- motive: False (0.005691468688182488)
- opportunity: False (0.025035380822680753)

The culprit is Georgette Pelham.
In fact, it is Wallace Anders.
## 5minutemystery-shoot-out-at-splithead-canyon
Big George Ratcliffe is guilty: True or False?
True (0.9355823382423648)
Big George Ratcliffe has mean: True or False?
True (0.8734309071535719)
Big George Ratcliffe has motive: True or False?
True (0.9777138240494376)
Big George Ratcliffe has opportunity: True or False?
True (0.8582439976623328)
Chester Morris is guilty: True or False?
True (0.971019387667922)
Chester Morris has mean: True or False?
True (0.9071478843057855)
Chester Morris has motive: True or False?
True (0.9835338590325645)
Chester Morris has opportunity: True or False?
True (0.8978744762836591)
Joe Franklin is guilty: True or False?
True (0.9222025272167219)
Joe Franklin has mean: True or False?
True (0.8551267420488947)
Joe Franklin has motive: True or False?
True (0.9696132548883896)
Joe Franklin has opportunity: True or False?
True (0.8013146490010521)
Slim Jameson is guilty: True or False?
True (0.9497626419596781)
Slim Jameson has mean: True or False?
True (0.941654147692963)
Slim Jameson has motive: True or False?
True (0.9808393129553152)
Slim Jameson has opportunity: True or False?
True (0.8984105603938967)
### Big George Ratcliffe
- mean: False (0.12656909284642814)
- motive: False (0.02228617595056237)
- opportunity: False (0.14175600233766716)

### Chester Morris
- mean: False (0.09285211569421448)
- motive: False (0.016466140967435483)
- opportunity: False (0.10212552371634087)

### Joe Franklin
- mean: False (0.14487325795110528)
- motive: False (0.030386745111610436)
- opportunity: False (0.1986853509989479)

### Slim Jameson
- mean: True (0.941654147692963)
- motive: True (0.9808393129553152)
- opportunity: True (0.8984105603938967)

The culprit is Slim Jameson.
In fact, it is Slim Jameson.
## 5minutemystery-the-mystery-of-the-american-raid
Admiral Taro is guilty: True or False?
True (0.9263036859044167)
Admiral Taro has mean: True or False?
True (0.9295683483415352)
Admiral Taro has motive: True or False?
True (0.9294404371753803)
Admiral Taro has opportunity: True or False?
True (0.7138307731576955)
Gina is guilty: True or False?
True (0.9580695040202324)
Gina has mean: True or False?
True (0.7898827135821628)
Gina has motive: True or False?
True (0.9664104579001461)
Gina has opportunity: True or False?
True (0.865678909174824)
Kira is guilty: True or False?
True (0.9121235591541035)
Kira has mean: True or False?
True (0.8558511090164419)
Kira has motive: True or False?
True (0.9399133323582882)
Kira has opportunity: True or False?
True (0.8860265005470086)
The Emperor is guilty: True or False?
True (0.9599126594957205)
The Emperor has mean: True or False?
True (0.905322251510331)
The Emperor has motive: True or False?
True (0.9313377150989219)
The Emperor has opportunity: True or False?
True (0.8976952440346371)
### Admiral Taro
- mean: False (0.07043165165846477)
- motive: False (0.07055956282461973)
- opportunity: False (0.2861692268423045)

### Gina
- mean: False (0.21011728641783722)
- motive: False (0.033589542099853875)
- opportunity: False (0.13432109082517596)

### Kira
- mean: False (0.1441488909835581)
- motive: False (0.06008666764171178)
- opportunity: False (0.1139734994529914)

### The Emperor
- mean: True (0.905322251510331)
- motive: True (0.9313377150989219)
- opportunity: True (0.8976952440346371)

The culprit is The Emperor.
In fact, it is Admiral Taro.
## 5minutemystery-the-missing-ornament-mystery
Jackie Hadley is guilty: True or False?
True (0.983149946614081)
Jackie Hadley has mean: True or False?
True (0.9403530352223053)
Jackie Hadley has motive: True or False?
True (0.9946045875651337)
Jackie Hadley has opportunity: True or False?
True (0.9704646460964202)
Lennie Hadley is guilty: True or False?
True (0.991570711107413)
Lennie Hadley has mean: True or False?
True (0.9563089012524633)
Lennie Hadley has motive: True or False?
True (0.9967806339468787)
Lennie Hadley has opportunity: True or False?
True (0.9795114404088129)
Mike Hadley is guilty: True or False?
True (0.9840936058779184)
Mike Hadley has mean: True or False?
True (0.9238675252821831)
Mike Hadley has motive: True or False?
True (0.993499100107697)
Mike Hadley has opportunity: True or False?
True (0.9569571625798028)
Sandy Hadley is guilty: True or False?
True (0.9843664168051008)
Sandy Hadley has mean: True or False?
True (0.9273632783787477)
Sandy Hadley has motive: True or False?
Map:  47%|████▋     | 95/203 [1:55:38<1:36:35, 53.67s/ examples]Map:  47%|████▋     | 96/203 [1:56:30<1:35:06, 53.33s/ examples]Map:  48%|████▊     | 97/203 [1:57:10<1:26:53, 49.18s/ examples]Map:  48%|████▊     | 98/203 [1:57:56<1:24:27, 48.26s/ examples]Map:  49%|████▉     | 99/203 [1:58:41<1:22:14, 47.45s/ examples]True (0.9943799375786527)
Sandy Hadley has opportunity: True or False?
True (0.9730365275631271)
Tommy Hadley is guilty: True or False?
True (0.9935618639533421)
Tommy Hadley has mean: True or False?
True (0.9594593035226332)
Tommy Hadley has motive: True or False?
True (0.996332228175721)
Tommy Hadley has opportunity: True or False?
True (0.9815598126769862)
### Jackie Hadley
- mean: False (0.05964696477769471)
- motive: False (0.005395412434866298)
- opportunity: False (0.029535353903579753)

### Lennie Hadley
- mean: False (0.04369109874753674)
- motive: False (0.003219366053121342)
- opportunity: False (0.020488559591187117)

### Mike Hadley
- mean: False (0.07613247471781692)
- motive: False (0.006500899892302958)
- opportunity: False (0.04304283742019721)

### Sandy Hadley
- mean: False (0.07263672162125234)
- motive: False (0.005620062421347272)
- opportunity: False (0.026963472436872915)

### Tommy Hadley
- mean: True (0.9594593035226332)
- motive: True (0.996332228175721)
- opportunity: True (0.9815598126769862)

The culprit is Tommy Hadley.
In fact, it is Lennie Hadley.
## 5minutemystery-the-pilgrim-thanksgiving-puzzle
John Alden is guilty: True or False?
True (0.8914335992201801)
John Alden has mean: True or False?
True (0.7570766705324253)
John Alden has motive: True or False?
True (0.8074606715677252)
John Alden has opportunity: True or False?
True (0.6800292740030767)
Miles Standish is guilty: True or False?
True (0.7662936378892937)
Miles Standish has mean: True or False?
True (0.7918210572836727)
Miles Standish has motive: True or False?
True (0.8710367026584496)
Miles Standish has opportunity: True or False?
True (0.6270381219830087)
Priscilla Mulllins is guilty: True or False?
True (0.9312127242200585)
Priscilla Mulllins has mean: True or False?
True (0.8766343647921183)
Priscilla Mulllins has motive: True or False?
True (0.9210740952879496)
Priscilla Mulllins has opportunity: True or False?
True (0.7599387683150569)
William Bradford is guilty: True or False?
True (0.8519528492100928)
William Bradford has mean: True or False?
True (0.9066531685310133)
William Bradford has motive: True or False?
True (0.8283841584202847)
William Bradford has opportunity: True or False?
True (0.897695304229796)
### John Alden
- mean: False (0.24292332946757467)
- motive: False (0.19253932843227484)
- opportunity: False (0.31997072599692333)

### Miles Standish
- mean: False (0.2081789427163273)
- motive: False (0.12896329734155043)
- opportunity: False (0.3729618780169913)

### Priscilla Mulllins
- mean: False (0.12336563520788169)
- motive: False (0.07892590471205041)
- opportunity: False (0.2400612316849431)

### William Bradford
- mean: True (0.9066531685310133)
- motive: True (0.8283841584202847)
- opportunity: True (0.897695304229796)

The culprit is William Bradford.
In fact, it is John Alden.
## 5minutemystery-the-disappearing-turkey
Darby is guilty: True or False?
True (0.9815950994553841)
Darby has mean: True or False?
True (0.9489172681310486)
Darby has motive: True or False?
True (0.9928647279268393)
Darby has opportunity: True or False?
True (0.9630919684645517)
Father is guilty: True or False?
True (0.9828891164753333)
Father has mean: True or False?
True (0.9054895675798634)
Father has motive: True or False?
True (0.9852146509274663)
Father has opportunity: True or False?
True (0.9260366570445833)
Greg is guilty: True or False?
True (0.96716302569886)
Greg has mean: True or False?
True (0.897695304229796)
Greg has motive: True or False?
True (0.9845754507999278)
Greg has opportunity: True or False?
True (0.9494823209990744)
Uncle Larry is guilty: True or False?
True (0.9420819287658885)
Uncle Larry has mean: True or False?
True (0.8879840376027315)
Uncle Larry has motive: True or False?
True (0.9871044155030217)
Uncle Larry has opportunity: True or False?
True (0.9216402157401415)
### Darby
- mean: True (0.9489172681310486)
- motive: True (0.9928647279268393)
- opportunity: True (0.9630919684645517)

### Father
- mean: False (0.09451043242013657)
- motive: False (0.014785349072533704)
- opportunity: False (0.07396334295541673)

### Greg
- mean: False (0.10230469577020396)
- motive: False (0.01542454920007219)
- opportunity: False (0.05051767900092563)

### Uncle Larry
- mean: False (0.11201596239726852)
- motive: False (0.012895584496978252)
- opportunity: False (0.07835978425985846)

The culprit is Darby.
In fact, it is Father.
## 5minutemystery-a-thanksgiving-mystery-poem
Libby is guilty: True or False?
True (0.589834510337428)
Libby has mean: True or False?
True (1.177830223552625)
Libby has motive: True or False?
True (1.4299377878015305)
Libby has opportunity: True or False?
True (0.9261395275636995)
Rusty is guilty: True or False?
True (1.8880003495184299)
Rusty has mean: True or False?
True (3.6993957079592654)
Rusty has motive: True or False?
True (6.251786511526913)
Rusty has opportunity: True or False?
True (2.3336385978178766)
Tiny is guilty: True or False?
False (0.6645403391983984)
Tiny has mean: True or False?
True (0.7997992557378433)
Tiny has motive: True or False?
True (1.7692136510952106)
Tiny has opportunity: True or False?
True (0.9304634014996606)
Tom is guilty: True or False?
True (0.8598587236220697)
Tom has mean: True or False?
True (3.6657931659415888)
Tom has motive: True or False?
True (3.948028698268326)
Tom has opportunity: True or False?
True (2.2198909046679023)
### Libby
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.07386047243630045)

### Rusty
- mean: True (3.6993957079592654)
- motive: True (6.251786511526913)
- opportunity: True (2.3336385978178766)

### Tiny
- mean: False (0.20020074426215673)
- motive: False (0.0)
- opportunity: False (0.06953659850033944)

### Tom
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.0)

The culprit is Rusty.
In fact, it is Rusty.
## 5minutemystery-turkey-cull
Beaker is guilty: True or False?
True (0.981021941474458)
Beaker has mean: True or False?
True (2.745320506080678)
Beaker has motive: True or False?
True (0.9798226954348701)
Beaker has opportunity: True or False?
True (0.8770561879413864)
Beau is guilty: True or False?
True (1.0713009788463974)
Beau has mean: True or False?
True (3.701607113358059)
Beau has motive: True or False?
True (0.9677167542009312)
Beau has opportunity: True or False?
True (0.7819973291046377)
Leaf is guilty: True or False?
True (0.9616780268435321)
Leaf has mean: True or False?
True (0.8897206197970384)
Leaf has motive: True or False?
True (0.9773707989989006)
Leaf has opportunity: True or False?
True (0.8951566249612815)
Red is guilty: True or False?
True (0.9418684262191025)
Red has mean: True or False?
True (1.1395321828655796)
Red has motive: True or False?
True (0.9694401626921336)
Red has opportunity: True or False?
True (0.784649255215384)
### Beaker
- mean: True (2.745320506080678)
- motive: True (0.9798226954348701)
- opportunity: True (0.8770561879413864)

### Beau
- mean: False (0.0)
- motive: False (0.03228324579906883)
- opportunity: False (0.2180026708953623)

### Leaf
- mean: False (0.11027938020296157)
- motive: False (0.02262920100109944)
- opportunity: False (0.10484337503871854)

### Red
- mean: False (0.0)
- motive: False (0.030559837307866378)
- opportunity: False (0.21535074478461602)

The culprit is Beaker.
In fact, it is Beau.
## 5minutemystery-a-turkey-day-struggle
Aunt Rachel is guilty: True or False?
True (0.9529258022651363)
Aunt Rachel has mean: True or False?
True (0.9383503780077049)
Aunt Rachel has motive: True or False?
True (0.9833749535726279)
Aunt Rachel has opportunity: True or False?
True (0.9440737974166838)
Chris is guilty: True or False?
True (0.9632996920284339)
Chris has mean: True or False?
True (0.921357630313903)
Chris has motive: True or False?
True (0.9863631130002726)
Chris has opportunity: True or False?
True (0.9312127242200585)
Diane is guilty: True or False?
True (0.9560634496217031)
Diane has mean: True or False?
True (0.7826625131049049)
Diane has motive: True or False?
True (0.9713473322135262)
Diane has opportunity: True or False?
True (0.9114953293645017)
Jack the Dog is guilty: True or False?
True (0.9509603994010378)
Map:  49%|████▉     | 100/203 [1:59:22<1:17:56, 45.41s/ examples]Map:  50%|████▉     | 101/203 [2:00:03<1:14:57, 44.09s/ examples]Map:  50%|█████     | 102/203 [2:01:00<1:20:33, 47.85s/ examples]Map:  51%|█████     | 103/203 [2:01:42<1:17:12, 46.33s/ examples]Map:  51%|█████     | 104/203 [2:02:27<1:15:42, 45.89s/ examples]Jack the Dog has mean: True or False?
True (0.9180403984176693)
Jack the Dog has motive: True or False?
True (0.9680507201226971)
Jack the Dog has opportunity: True or False?
True (0.9241418261705818)
### Aunt Rachel
- mean: True (0.9383503780077049)
- motive: True (0.9833749535726279)
- opportunity: True (0.9440737974166838)

### Chris
- mean: False (0.07864236968609695)
- motive: False (0.013636886999727427)
- opportunity: False (0.06878727577994148)

### Diane
- mean: False (0.21733748689509513)
- motive: False (0.028652667786473796)
- opportunity: False (0.08850467063549827)

### Jack the Dog
- mean: False (0.08195960158233073)
- motive: False (0.031949279877302894)
- opportunity: False (0.07585817382941817)

The culprit is Aunt Rachel.
In fact, it is Chris.
## 5minutemystery-the-missing-briefcase
Porter 1 is guilty: True or False?
True (0.9384632725948482)
Porter 1 has mean: True or False?
True (0.8624675215861032)
Porter 1 has motive: True or False?
True (0.9570375696873612)
Porter 1 has opportunity: True or False?
True (0.8925625120974553)
Porter 2 is guilty: True or False?
True (0.942612469657282)
Porter 2 has mean: True or False?
True (0.8255897087847518)
Porter 2 has motive: True or False?
True (0.9676556581517683)
Porter 2 has opportunity: True or False?
True (0.9447913165152162)
Porter 3 is guilty: True or False?
True (0.955152153792717)
Porter 3 has mean: True or False?
True (0.8514594452543962)
Porter 3 has motive: True or False?
True (0.9841089245217288)
Porter 3 has opportunity: True or False?
True (0.9661559457424579)
Porter 4 is guilty: True or False?
True (0.9575167905174621)
Porter 4 has mean: True or False?
True (0.8832359917473193)
Porter 4 has motive: True or False?
True (0.9848401551103727)
Porter 4 has opportunity: True or False?
True (0.948058427656158)
### Porter 1
- mean: False (0.13753247841389682)
- motive: False (0.0429624303126388)
- opportunity: False (0.1074374879025447)

### Porter 2
- mean: False (0.1744102912152482)
- motive: False (0.03234434184823165)
- opportunity: False (0.055208683484783805)

### Porter 3
- mean: False (0.1485405547456038)
- motive: False (0.015891075478271177)
- opportunity: False (0.03384405425754211)

### Porter 4
- mean: True (0.8832359917473193)
- motive: True (0.9848401551103727)
- opportunity: True (0.948058427656158)

The culprit is Porter 4.
In fact, it is Porter 3.
## 5minutemystery-everythings-not-just-ducky
Bethany is guilty: True or False?
True (0.9155072008980665)
Bethany has mean: True or False?
True (0.7718434926244166)
Bethany has motive: True or False?
True (0.986726105374147)
Bethany has opportunity: True or False?
True (0.8423451152856819)
Connor is guilty: True or False?
True (0.9304582506719414)
Connor has mean: True or False?
True (0.7937461674149602)
Connor has motive: True or False?
True (0.9833748931272365)
Connor has opportunity: True or False?
True (0.8816149238192855)
Emma is guilty: True or False?
True (0.9249593046682986)
Emma has mean: True or False?
True (0.7641884666111024)
Emma has motive: True or False?
True (0.9796676632098326)
Emma has opportunity: True or False?
True (0.8140527631337082)
Tim is guilty: True or False?
True (0.8494724067948436)
Tim has mean: True or False?
True (0.6976088896786037)
Tim has motive: True or False?
True (0.9764456756172326)
Tim has opportunity: True or False?
True (0.8074606715677252)
### Bethany
- mean: False (0.22815650737558335)
- motive: False (0.013273894625853044)
- opportunity: False (0.1576548847143181)

### Connor
- mean: True (0.7937461674149602)
- motive: True (0.9833748931272365)
- opportunity: True (0.8816149238192855)

### Emma
- mean: False (0.2358115333888976)
- motive: False (0.020332336790167438)
- opportunity: False (0.18594723686629178)

### Tim
- mean: False (0.3023911103213963)
- motive: False (0.02355432438276739)
- opportunity: False (0.19253932843227484)

The culprit is Connor.
In fact, it is Bethany.
## 5minutemystery-a-darkened-veterans-day
Colonel Abraham is guilty: True or False?
True (0.9729852083817088)
Colonel Abraham has mean: True or False?
True (0.963368656065788)
Colonel Abraham has motive: True or False?
True (0.9927952288368657)
Colonel Abraham has opportunity: True or False?
True (0.9815244083320255)
Frank Thompson is guilty: True or False?
True (0.9713473322135262)
Frank Thompson has mean: True or False?
True (0.9546474221708894)
Frank Thompson has motive: True or False?
True (0.9873993989626895)
Frank Thompson has opportunity: True or False?
True (0.9639160647221925)
Mr. Landry is guilty: True or False?
True (0.9364014251476122)
Mr. Landry has mean: True or False?
True (0.9273633336539081)
Mr. Landry has motive: True or False?
True (0.9780727024492712)
Mr. Landry has opportunity: True or False?
True (0.9563089618154458)
Ryan Smith is guilty: True or False?
True (0.9780517227981328)
Ryan Smith has mean: True or False?
True (0.9315870392207104)
Ryan Smith has motive: True or False?
True (0.9876400824622509)
Ryan Smith has opportunity: True or False?
True (0.9671009774598767)
### Colonel Abraham
- mean: True (0.963368656065788)
- motive: True (0.9927952288368657)
- opportunity: True (0.9815244083320255)

### Frank Thompson
- mean: False (0.04535257782911062)
- motive: False (0.012600601037310533)
- opportunity: False (0.03608393527780751)

### Mr. Landry
- mean: False (0.0726366663460919)
- motive: False (0.021927297550728753)
- opportunity: False (0.04369103818455422)

### Ryan Smith
- mean: False (0.0684129607792896)
- motive: False (0.012359917537749121)
- opportunity: False (0.032899022540123335)

The culprit is Colonel Abraham.
In fact, it is Colonel Abraham.
## 5minutemystery-the-missing-ring
Fingers Ferguson is guilty: True or False?
True (0.9572777759716213)
Fingers Ferguson has mean: True or False?
False (0.6816549012710613)
Fingers Ferguson has motive: True or False?
True (0.9825240364904724)
Fingers Ferguson has opportunity: True or False?
False (1.0570191495790755)
Joe Morgan is guilty: True or False?
True (0.9226218463113949)
Joe Morgan has mean: True or False?
True (0.811078188867804)
Joe Morgan has motive: True or False?
True (0.9603611244019274)
Joe Morgan has opportunity: True or False?
True (0.9155072554665495)
Manuel Garcia is guilty: True or False?
True (0.8679338050595715)
Manuel Garcia has mean: True or False?
True (0.7185943809170431)
Manuel Garcia has motive: True or False?
True (0.9516838792709049)
Manuel Garcia has opportunity: True or False?
True (0.944176853162527)
Mr. Bridges is guilty: True or False?
True (0.9031234959323464)
Mr. Bridges has mean: True or False?
True (0.700075275973927)
Mr. Bridges has motive: True or False?
True (0.9848546984022976)
Mr. Bridges has opportunity: True or False?
True (0.9219218506394821)
### Fingers Ferguson
- mean: False (0.6816549012710613)
- motive: False (0.017475963509527626)
- opportunity: False (1.0570191495790755)

### Joe Morgan
- mean: True (0.811078188867804)
- motive: True (0.9603611244019274)
- opportunity: True (0.9155072554665495)

### Manuel Garcia
- mean: False (0.2814056190829569)
- motive: False (0.04831612072909508)
- opportunity: False (0.055823146837473026)

### Mr. Bridges
- mean: False (0.29992472402607295)
- motive: False (0.015145301597702443)
- opportunity: False (0.07807814936051793)

The culprit is Joe Morgan.
In fact, it is Joe Morgan.
## 5minutemystery-brass-keyboard-mystery
April Key #4 is guilty: True or False?
True (0.9689738169140454)
April Key #4 has mean: True or False?
True (0.8856315007226893)
April Key #4 has motive: True or False?
True (0.987829386772097)
April Key #4 has opportunity: True or False?
True (0.9458012588547495)
Denise Key #6 is guilty: True or False?
True (0.9859363436468169)
Denise Key #6 has mean: True or False?
True (0.9365176577773374)
Denise Key #6 has motive: True or False?
True (0.9918279647218875)
Denise Key #6 has opportunity: True or False?
True (0.9649873987772907)
Harold Key #1 is guilty: True or False?
True (0.9631612907883619)
Harold Key #1 has mean: True or False?
True (0.9102267057681164)
Harold Key #1 has motive: True or False?
True (0.9840016367056158)
Harold Key #1 has opportunity: True or False?
True (0.884837803442546)
Map:  52%|█████▏    | 105/203 [2:03:37<1:26:32, 52.98s/ examples]Map:  52%|█████▏    | 106/203 [2:04:29<1:25:08, 52.67s/ examples]Map:  53%|█████▎    | 107/203 [2:05:48<1:37:18, 60.82s/ examples]Map:  53%|█████▎    | 108/203 [2:06:34<1:28:58, 56.20s/ examples]Map:  54%|█████▎    | 109/203 [2:07:33<1:29:36, 57.20s/ examples]Kirsten Key #5 is guilty: True or False?
True (0.9572777759716213)
Kirsten Key #5 has mean: True or False?
True (0.867485409735739)
Kirsten Key #5 has motive: True or False?
True (0.9823893307032775)
Kirsten Key #5 has opportunity: True or False?
True (0.9346342066470359)
Robert (Buddy) Key #3 is guilty: True or False?
True (0.9733929040540585)
Robert (Buddy) Key #3 has mean: True or False?
True (0.9039745373919651)
Robert (Buddy) Key #3 has motive: True or False?
True (0.9855242965202695)
Robert (Buddy) Key #3 has opportunity: True or False?
True (0.9257686153543061)
### April Key #4
- mean: False (0.11436849927731074)
- motive: False (0.012170613227903027)
- opportunity: False (0.05419874114525047)

### Denise Key #6
- mean: True (0.9365176577773374)
- motive: True (0.9918279647218875)
- opportunity: True (0.9649873987772907)

### Harold Key #1
- mean: False (0.08977329423188363)
- motive: False (0.0159983632943842)
- opportunity: False (0.11516219655745397)

### Kirsten Key #5
- mean: False (0.13251459026426105)
- motive: False (0.017610669296722503)
- opportunity: False (0.06536579335296411)

### Robert (Buddy) Key #3
- mean: False (0.0960254626080349)
- motive: False (0.014475703479730484)
- opportunity: False (0.0742313846456939)

The culprit is Denise Key #6.
In fact, it is April Key #4.
## 5minutemystery-the-curse-of-the-unlucky-streak
Coach Williams is guilty: True or False?
True (0.8688268116310761)
Coach Williams has mean: True or False?
True (0.8751481831208795)
Coach Williams has motive: True or False?
True (0.9752253881278916)
Coach Williams has opportunity: True or False?
True (0.8951566249612815)
Joe is guilty: True or False?
True (0.8303191711685114)
Joe has mean: True or False?
True (0.918480215734292)
Joe has motive: True or False?
True (0.9495291710083491)
Joe has opportunity: True or False?
True (0.9325762415758686)
Mrs. Williams is guilty: True or False?
True (0.7745833916423246)
Mrs. Williams has mean: True or False?
True (0.7348812840309261)
Mrs. Williams has motive: True or False?
True (0.9486324788710994)
Mrs. Williams has opportunity: True or False?
True (0.8092759828926619)
Roderick is guilty: True or False?
True (0.7813305798204846)
Roderick has mean: True or False?
True (0.7394223819718238)
Roderick has motive: True or False?
True (0.8969755785184792)
Roderick has opportunity: True or False?
True (0.7732163648437078)
### Coach Williams
- mean: False (0.1248518168791205)
- motive: False (0.024774611872108387)
- opportunity: False (0.10484337503871854)

### Joe
- mean: True (0.918480215734292)
- motive: True (0.9495291710083491)
- opportunity: True (0.9325762415758686)

### Mrs. Williams
- mean: False (0.2651187159690739)
- motive: False (0.05136752112890064)
- opportunity: False (0.1907240171073381)

### Roderick
- mean: False (0.26057761802817625)
- motive: False (0.1030244214815208)
- opportunity: False (0.22678363515629218)

The culprit is Joe.
In fact, it is Joe.
## 5minutemystery-halloween-2008
Bride is guilty: True or False?
True (0.8204694405411458)
Bride has mean: True or False?
True (0.6619228707202935)
Bride has motive: True or False?
True (0.7505527059280641)
Bride has opportunity: True or False?
True (0.6279512069990912)
Groom is guilty: True or False?
True (0.9219218506394821)
Groom has mean: True or False?
True (0.8524448242555318)
Groom has motive: True or False?
True (0.7911764307711107)
Groom has opportunity: True or False?
True (0.8181563669811865)
Indian Chief is guilty: True or False?
True (0.6343168082332088)
Indian Chief has mean: True or False?
True (0.6048657973050737)
Indian Chief has motive: True or False?
True (0.6187804294217345)
Indian Chief has opportunity: True or False?
True (0.6575384105121485)
Wealthy Woman is guilty: True or False?
True (0.685107355950278)
Wealthy Woman has mean: True or False?
False (0.5360700410935405)
Wealthy Woman has motive: True or False?
True (0.5117165908639297)
Wealthy Woman has opportunity: True or False?
True (0.5234203246639862)
### Bride
- mean: False (0.33807712927970646)
- motive: False (0.2494472940719359)
- opportunity: False (0.37204879300090876)

### Groom
- mean: True (0.8524448242555318)
- motive: True (0.7911764307711107)
- opportunity: True (0.8181563669811865)

### Indian Chief
- mean: False (0.3951342026949263)
- motive: False (0.3812195705782655)
- opportunity: False (0.34246158948785155)

### Wealthy Woman
- mean: False (0.5360700410935405)
- motive: False (0.48828340913607027)
- opportunity: False (0.47657967533601375)

The culprit is Groom.
In fact, it is Groom.
## 5minutemystery-the-trick-or-treat-mystery
Dorothy is guilty: True or False?
True (0.9615338444102304)
Dorothy has mean: True or False?
True (0.802555560073231)
Dorothy has motive: True or False?
True (0.9155072554665495)
Dorothy has opportunity: True or False?
True (0.7505527730327083)
Superman is guilty: True or False?
True (0.9657060519221431)
Superman has mean: True or False?
True (0.934155284694701)
Superman has motive: True or False?
True (0.9682614213403071)
Superman has opportunity: True or False?
True (0.9408984770280414)
The Ghost is guilty: True or False?
True (0.9720455997120265)
The Ghost has mean: True or False?
True (0.7756047866813147)
The Ghost has motive: True or False?
True (0.9556514027264735)
The Ghost has opportunity: True or False?
True (0.9161096235973493)
The Lion is guilty: True or False?
True (0.9828890560598048)
The Lion has mean: True or False?
True (0.9235923286659299)
The Lion has motive: True or False?
True (0.9664105191028597)
The Lion has opportunity: True or False?
True (0.9543079730970608)
The Witch is guilty: True or False?
True (0.9638480560973683)
The Witch has mean: True or False?
True (0.854884683810039)
The Witch has motive: True or False?
True (0.9498557456415421)
The Witch has opportunity: True or False?
True (0.8762112821835625)
### Dorothy
- mean: False (0.19744443992676897)
- motive: False (0.08449274453345046)
- opportunity: False (0.2494472269672917)

### Superman
- mean: False (0.065844715305299)
- motive: False (0.03173857865969287)
- opportunity: False (0.05910152297195859)

### The Ghost
- mean: False (0.22439521331868528)
- motive: False (0.04434859727352647)
- opportunity: False (0.08389037640265073)

### The Lion
- mean: True (0.9235923286659299)
- motive: True (0.9664105191028597)
- opportunity: True (0.9543079730970608)

### The Witch
- mean: False (0.14511531618996099)
- motive: False (0.05014425435845793)
- opportunity: False (0.12378871781643752)

The culprit is The Lion.
In fact, it is The Witch.
## 5minutemystery-house-of-the-rising-pumpkin
Curtis is guilty: True or False?
True (0.9612438076473231)
Curtis has mean: True or False?
True (0.9329437644068318)
Curtis has motive: True or False?
True (0.971455871280406)
Curtis has opportunity: True or False?
True (0.9360515445140636)
Dabney is guilty: True or False?
True (0.9726234682815975)
Dabney has mean: True or False?
True (0.9094255544919778)
Dabney has motive: True or False?
True (0.9717254050158363)
Dabney has opportunity: True or False?
True (0.9193534273597669)
Kim is guilty: True or False?
True (0.9759005309632979)
Kim has mean: True or False?
True (0.8927496657814362)
Kim has motive: True or False?
True (0.9713473322135262)
Kim has opportunity: True or False?
True (0.9213575753967104)
Mary is guilty: True or False?
True (0.9549844874375936)
Mary has mean: True or False?
True (0.927887794449634)
Mary has motive: True or False?
True (0.9748211501698323)
Mary has opportunity: True or False?
True (0.8925625719484378)
### Curtis
- mean: True (0.9329437644068318)
- motive: True (0.971455871280406)
- opportunity: True (0.9360515445140636)

### Dabney
- mean: False (0.09057444550802218)
- motive: False (0.028274594984163737)
- opportunity: False (0.08064657264023312)

### Kim
- mean: False (0.10725033421856378)
- motive: False (0.028652667786473796)
- opportunity: False (0.07864242460328963)

### Mary
- mean: False (0.07211220555036602)
- motive: False (0.025178849830167715)
- opportunity: False (0.1074374280515622)

The culprit is Curtis.
In fact, it is Kim.
## 5minutemystery-the-secret-of-the-scarecrows-mask
Charles Kincaid is guilty: True or False?
Map:  54%|█████▍    | 110/203 [2:08:22<1:24:34, 54.57s/ examples]Map:  55%|█████▍    | 111/203 [2:09:17<1:23:55, 54.73s/ examples]Map:  55%|█████▌    | 112/203 [2:09:53<1:14:41, 49.24s/ examples]Map:  56%|█████▌    | 113/203 [2:10:50<1:17:06, 51.40s/ examples]True (0.9563089012524633)
Charles Kincaid has mean: True or False?
True (0.9467937951644804)
Charles Kincaid has motive: True or False?
True (0.9874962564918496)
Charles Kincaid has opportunity: True or False?
True (0.9683812262581977)
Chester is guilty: True or False?
True (0.9771973485275812)
Chester has mean: True or False?
True (0.9222025272167219)
Chester has motive: True or False?
True (0.981202900643061)
Chester has opportunity: True or False?
True (0.9518632280135741)
Mr. Winfrey is guilty: True or False?
True (0.8987665204865408)
Mr. Winfrey has mean: True or False?
True (0.8272706865691472)
Mr. Winfrey has motive: True or False?
True (0.9139841191734227)
Mr. Winfrey has opportunity: True or False?
True (0.908941745727715)
Mrs. Winfrey is guilty: True or False?
True (0.9447913165152162)
Mrs. Winfrey has mean: True or False?
True (0.8705973031072073)
Mrs. Winfrey has motive: True or False?
True (0.9544780238917078)
Mrs. Winfrey has opportunity: True or False?
True (0.9235923286659299)
### Charles Kincaid
- mean: True (0.9467937951644804)
- motive: True (0.9874962564918496)
- opportunity: True (0.9683812262581977)

### Chester
- mean: False (0.07779747278327809)
- motive: False (0.018797099356938962)
- opportunity: False (0.04813677198642585)

### Mr. Winfrey
- mean: False (0.17272931343085285)
- motive: False (0.0860158808265773)
- opportunity: False (0.09105825427228498)

### Mrs. Winfrey
- mean: False (0.1294026968927927)
- motive: False (0.04552197610829223)
- opportunity: False (0.07640767133407012)

The culprit is Charles Kincaid.
In fact, it is Chester.
## 5minutemystery-the-scarecrow-slasher
Annie is guilty: True or False?
True (0.9476723683039264)
Annie has mean: True or False?
True (0.7240905157396584)
Annie has motive: True or False?
True (0.9655114412719658)
Annie has opportunity: True or False?
True (0.854884683810039)
Mr. Forbes is guilty: True or False?
True (0.6297746298200823)
Mr. Forbes has mean: True or False?
True (0.7714994025200967)
Mr. Forbes has motive: True or False?
True (0.9081302297583123)
Mr. Forbes has opportunity: True or False?
True (0.7602949226623019)
Mrs. Avery is guilty: True or False?
True (0.9206471454701205)
Mrs. Avery has mean: True or False?
True (0.7356416476869558)
Mrs. Avery has motive: True or False?
True (0.9823216197069597)
Mrs. Avery has opportunity: True or False?
True (0.8620035048683017)
Philips is guilty: True or False?
True (0.9622497571173928)
Philips has mean: True or False?
True (0.7581526119887462)
Philips has motive: True or False?
True (0.9644556034131689)
Philips has opportunity: True or False?
True (0.9358173616900589)
### Annie
- mean: False (0.27590948426034156)
- motive: False (0.034488558728034246)
- opportunity: False (0.14511531618996099)

### Mr. Forbes
- mean: False (0.22850059747990326)
- motive: False (0.09186977024168774)
- opportunity: False (0.23970507733769808)

### Mrs. Avery
- mean: False (0.26435835231304416)
- motive: False (0.017678380293040252)
- opportunity: False (0.13799649513169832)

### Philips
- mean: True (0.7581526119887462)
- motive: True (0.9644556034131689)
- opportunity: True (0.9358173616900589)

The culprit is Philips.
In fact, it is Philips.
## 5minutemystery-the-golden-ruse
Miss Jones is guilty: True or False?
True (0.7950223052877581)
Miss Jones has mean: True or False?
True (0.9046505665674094)
Miss Jones has motive: True or False?
True (0.911809984585868)
Miss Jones has opportunity: True or False?
True (0.9127477403975288)
Miss. Pendlebury is guilty: True or False?
True (0.8984105603938967)
Miss. Pendlebury has mean: True or False?
True (0.8074606715677252)
Miss. Pendlebury has motive: True or False?
True (0.8824278665848695)
Miss. Pendlebury has opportunity: True or False?
True (0.8596637206861489)
Mr. Horgan is guilty: True or False?
True (0.8193157317863493)
Mr. Horgan has mean: True or False?
True (0.7718434926244166)
Mr. Horgan has motive: True or False?
True (0.9145963197706802)
Mr. Horgan has opportunity: True or False?
True (0.9249593046682986)
Mr. Reese is guilty: True or False?
True (0.8803863464576128)
Mr. Reese has mean: True or False?
True (0.8193157317863493)
Mr. Reese has motive: True or False?
True (0.9731898306467035)
Mr. Reese has opportunity: True or False?
True (0.9142907234091052)
### Miss Jones
- mean: True (0.9046505665674094)
- motive: True (0.911809984585868)
- opportunity: True (0.9127477403975288)

### Miss. Pendlebury
- mean: False (0.19253932843227484)
- motive: False (0.11757213341513051)
- opportunity: False (0.14033627931385106)

### Mr. Horgan
- mean: False (0.22815650737558335)
- motive: False (0.08540368022931977)
- opportunity: False (0.07504069533170143)

### Mr. Reese
- mean: False (0.1806842682136507)
- motive: False (0.026810169353296498)
- opportunity: False (0.08570927659089478)

The culprit is Miss Jones.
In fact, it is Mr. Horgan.
## 5minutemystery-hound-of-the-buskerville
Balloon Twister is guilty: True or False?
True (0.9855382441311838)
Balloon Twister has mean: True or False?
True (0.9177460685312047)
Balloon Twister has motive: True or False?
True (0.9781771902180998)
Balloon Twister has opportunity: True or False?
True (0.9800721401531428)
Living Statue is guilty: True or False?
True (0.9758545755283039)
Living Statue has mean: True or False?
True (0.8866168897831055)
Living Statue has motive: True or False?
True (0.962813258487323)
Living Statue has opportunity: True or False?
True (0.9569571625798028)
Mime is guilty: True or False?
True (0.9704086183750964)
Mime has mean: True or False?
True (0.8255897702959807)
Mime has motive: True or False?
True (0.9603983181010374)
Mime has opportunity: True or False?
True (0.9086178579521682)
Stilt-Walker is guilty: True or False?
True (0.9709643714595256)
Stilt-Walker has mean: True or False?
True (0.9199306971612747)
Stilt-Walker has motive: True or False?
True (0.9603611244019274)
Stilt-Walker has opportunity: True or False?
True (0.948346199423113)
### Balloon Twister
- mean: True (0.9177460685312047)
- motive: True (0.9781771902180998)
- opportunity: True (0.9800721401531428)

### Living Statue
- mean: False (0.11338311021689451)
- motive: False (0.03718674151267698)
- opportunity: False (0.04304283742019721)

### Mime
- mean: False (0.17441022970401932)
- motive: False (0.039601681898962626)
- opportunity: False (0.0913821420478318)

### Stilt-Walker
- mean: False (0.08006930283872526)
- motive: False (0.039638875598072554)
- opportunity: False (0.051653800576886955)

The culprit is Balloon Twister.
In fact, it is Stilt-Walker.
## 5minutemystery-moriarty-picks-a-murderer-part-two
Hansom Cab Driver is guilty: True or False?
True (0.905989824801558)
Hansom Cab Driver has mean: True or False?
True (0.5602526707659626)
Hansom Cab Driver has motive: True or False?
True (0.7662937064012869)
Hansom Cab Driver has opportunity: True or False?
True (0.8244619332958376)
Policeman is guilty: True or False?
True (0.874934615163517)
Policeman has mean: True or False?
True (0.8016254254291421)
Policeman has motive: True or False?
True (0.8587185689177256)
Policeman has opportunity: True or False?
True (0.832781310996106)
Theater Usher is guilty: True or False?
True (0.9032942081209032)
Theater Usher has mean: True or False?
True (0.5631377056275331)
Theater Usher has motive: True or False?
True (0.8128672807499561)
Theater Usher has opportunity: True or False?
True (0.8958876133958744)
Ticket Seller is guilty: True or False?
True (0.9029524930853913)
Ticket Seller has mean: True or False?
True (0.64063590602721)
Ticket Seller has motive: True or False?
True (0.7833262085677729)
Ticket Seller has opportunity: True or False?
True (0.7041601500399041)
### Hansom Cab Driver
- mean: False (0.43974732923403737)
- motive: False (0.2337062935987131)
- opportunity: False (0.1755380667041624)

### Policeman
- mean: True (0.8016254254291421)
- motive: True (0.8587185689177256)
- opportunity: True (0.832781310996106)

### Theater Usher
- mean: False (0.43686229437246693)
- motive: False (0.18713271925004393)
- opportunity: False (0.10411238660412558)

### Ticket Seller
- mean: False (0.35936409397279)
- motive: False (0.2166737914322271)
Map:  56%|█████▌    | 114/203 [2:11:39<1:15:23, 50.82s/ examples]Map:  57%|█████▋    | 115/203 [2:12:22<1:10:51, 48.31s/ examples]Map:  57%|█████▋    | 116/203 [2:13:14<1:11:51, 49.55s/ examples]Map:  58%|█████▊    | 117/203 [2:14:10<1:13:36, 51.36s/ examples]Map:  58%|█████▊    | 118/203 [2:14:52<1:08:43, 48.51s/ examples]- opportunity: False (0.29583984996009594)

The culprit is Policeman.
In fact, it is Theater Usher.
## 5minutemystery-the-scent-of-a-thief
Betty is guilty: True or False?
True (0.9781354072533421)
Betty has mean: True or False?
True (0.8514593818157263)
Betty has motive: True or False?
True (0.9815598126769862)
Betty has opportunity: True or False?
True (0.9343951361750445)
Darlene is guilty: True or False?
True (0.9724147321673792)
Darlene has mean: True or False?
True (0.8910549899564296)
Darlene has motive: True or False?
True (0.9890975956044473)
Darlene has opportunity: True or False?
True (0.9604354488383994)
Mr. Danby is guilty: True or False?
True (0.9331876642092066)
Mr. Danby has mean: True or False?
True (0.8431216460935126)
Mr. Danby has motive: True or False?
True (0.9834386705764392)
Mr. Danby has opportunity: True or False?
True (0.9505947242503305)
Mr. Harrison is guilty: True or False?
True (0.9617499703158447)
Mr. Harrison has mean: True or False?
True (0.9593831890064877)
Mr. Harrison has motive: True or False?
True (0.9946981072726756)
Mr. Harrison has opportunity: True or False?
True (0.9865975971456143)
### Betty
- mean: False (0.14854061818427367)
- motive: False (0.01844018732301378)
- opportunity: False (0.06560486382495545)

### Darlene
- mean: False (0.10894501004357038)
- motive: False (0.010902404395552678)
- opportunity: False (0.039564551161600625)

### Mr. Danby
- mean: False (0.1568783539064874)
- motive: False (0.01656132942356081)
- opportunity: False (0.049405275749669464)

### Mr. Harrison
- mean: True (0.9593831890064877)
- motive: True (0.9946981072726756)
- opportunity: True (0.9865975971456143)

The culprit is Mr. Harrison.
In fact, it is Mr. Harrison.
## 5minutemystery-moriarty-picks-a-murderer-part-one
Ed the Bludgeoner is guilty: True or False?
True (0.8679338697256817)
Ed the Bludgeoner has mean: True or False?
True (0.9019207382785395)
Ed the Bludgeoner has motive: True or False?
True (0.9164093141890854)
Ed the Bludgeoner has opportunity: True or False?
True (0.9431384818142104)
Fastidious Fred Fielder is guilty: True or False?
False (3.1005544453257916)
Fastidious Fred Fielder has mean: True or False?
False (3.296294936941234)
Fastidious Fred Fielder has motive: True or False?
False (2.056922424377871)
Fastidious Fred Fielder has opportunity: True or False?
False (3.3718678768950143)
Herman Houlihan is guilty: True or False?
True (0.6918097672776748)
Herman Houlihan has mean: True or False?
True (0.7931059536445917)
Herman Houlihan has motive: True or False?
True (0.7975568155246964)
Herman Houlihan has opportunity: True or False?
False (0.7133364983567047)
Morris the Ascot Dandy is guilty: True or False?
True (0.8955226517597132)
Morris the Ascot Dandy has mean: True or False?
True (0.9252299659402181)
Morris the Ascot Dandy has motive: True or False?
True (0.9437636745681832)
Morris the Ascot Dandy has opportunity: True or False?
True (0.9841546417437246)
### Ed the Bludgeoner
- mean: False (0.09807926172146053)
- motive: False (0.08359068581091456)
- opportunity: False (0.05686151818578955)

### Fastidious Fred Fielder
- mean: False (3.296294936941234)
- motive: False (2.056922424377871)
- opportunity: False (3.3718678768950143)

### Herman Houlihan
- mean: False (0.2068940463554083)
- motive: False (0.20244318447530363)
- opportunity: False (0.7133364983567047)

### Morris the Ascot Dandy
- mean: True (0.9252299659402181)
- motive: True (0.9437636745681832)
- opportunity: True (0.9841546417437246)

The culprit is Morris the Ascot Dandy.
In fact, it is Fastidious Fred Fielder.
## 5minutemystery-the-geneva-summit-goldfish-mystery
Ermina Glandon is guilty: True or False?
True (0.9319595674053855)
Ermina Glandon has mean: True or False?
True (0.9167081124681512)
Ermina Glandon has motive: True or False?
True (0.9690910565174785)
Ermina Glandon has opportunity: True or False?
True (0.8732147785405174)
George Adams is guilty: True or False?
True (0.9291837815043049)
George Adams has mean: True or False?
True (0.8624675215861032)
George Adams has motive: True or False?
True (0.9760835762008001)
George Adams has opportunity: True or False?
True (0.811078188867804)
Matthew O'Leary is guilty: True or False?
True (0.7563575572780217)
Matthew O'Leary has mean: True or False?
True (0.8984105603938967)
Matthew O'Leary has motive: True or False?
True (0.9246876822649571)
Matthew O'Leary has opportunity: True or False?
True (0.84440905415483)
Prince Rahim is guilty: True or False?
True (0.9583821892129424)
Prince Rahim has mean: True or False?
True (0.8175744430556572)
Prince Rahim has motive: True or False?
True (0.9777987599607383)
Prince Rahim has opportunity: True or False?
True (0.9219218506394821)
Ronald Reagan is guilty: True or False?
True (0.8272706865691472)
Ronald Reagan has mean: True or False?
True (0.5583269696343842)
Ronald Reagan has motive: True or False?
True (0.9432430869704435)
Ronald Reagan has opportunity: True or False?
True (0.8068526417769779)
### Ermina Glandon
- mean: True (0.9167081124681512)
- motive: True (0.9690910565174785)
- opportunity: True (0.8732147785405174)

### George Adams
- mean: False (0.13753247841389682)
- motive: False (0.023916423799199893)
- opportunity: False (0.18892181113219597)

### Matthew O'Leary
- mean: False (0.10158943960610334)
- motive: False (0.07531231773504288)
- opportunity: False (0.15559094584516997)

### Prince Rahim
- mean: False (0.18242555694434281)
- motive: False (0.022201240039261716)
- opportunity: False (0.07807814936051793)

### Ronald Reagan
- mean: False (0.4416730303656158)
- motive: False (0.056756913029556544)
- opportunity: False (0.1931473582230221)

The culprit is Ermina Glandon.
In fact, it is Ronald Reagan.
## 5minutemystery-a-straw-stuffed-mystery
Bill Albertson is guilty: True or False?
True (0.9843664168051008)
Bill Albertson has mean: True or False?
True (0.8596637847360897)
Bill Albertson has motive: True or False?
True (0.9850644470823064)
Bill Albertson has opportunity: True or False?
True (0.963230549923961)
Mr. Fletcher is guilty: True or False?
True (0.9386884590909785)
Mr. Fletcher has mean: True or False?
True (0.8451772989343147)
Mr. Fletcher has motive: True or False?
True (0.9869040247745934)
Mr. Fletcher has opportunity: True or False?
True (0.9527503243194666)
Professor Surenie is guilty: True or False?
True (0.9575167905174621)
Professor Surenie has mean: True or False?
True (0.787931139050028)
Professor Surenie has motive: True or False?
True (0.9730365275631271)
Professor Surenie has opportunity: True or False?
True (0.9317114972308657)
Rachel Beaton is guilty: True or False?
True (0.9773275850444884)
Rachel Beaton has mean: True or False?
True (0.873646672673131)
Rachel Beaton has motive: True or False?
True (0.9856215116934163)
Rachel Beaton has opportunity: True or False?
True (0.9435559526996434)
### Bill Albertson
- mean: True (0.8596637847360897)
- motive: True (0.9850644470823064)
- opportunity: True (0.963230549923961)

### Mr. Fletcher
- mean: False (0.1548227010656853)
- motive: False (0.01309597522540662)
- opportunity: False (0.0472496756805334)

### Professor Surenie
- mean: False (0.21206886094997202)
- motive: False (0.026963472436872915)
- opportunity: False (0.06828850276913434)

### Rachel Beaton
- mean: False (0.126353327326869)
- motive: False (0.014378488306583725)
- opportunity: False (0.05644404730035657)

The culprit is Bill Albertson.
In fact, it is Mr. Fletcher.
## 5minutemystery-ask-marthathe-shoplifter
Jane Croydon is guilty: True or False?
True (0.9855243561799379)
Jane Croydon has mean: True or False?
True (0.8438950825214144)
Jane Croydon has motive: True or False?
True (0.9832467444299942)
Jane Croydon has opportunity: True or False?
True (0.9351098557348285)
Johnny Martin is guilty: True or False?
True (0.9787533276905257)
Johnny Martin has mean: True or False?
True (0.8727816933272936)
Johnny Martin has motive: True or False?
True (0.9758085604594696)
Johnny Martin has opportunity: True or False?
True (0.9522199623739209)
Martha Hampden is guilty: True or False?
True (0.9750121835371013)
Martha Hampden has mean: True or False?
True (0.8864204283224634)
Map:  59%|█████▊    | 119/203 [2:15:53<1:13:13, 52.30s/ examples]Map:  59%|█████▉    | 120/203 [2:16:37<1:08:52, 49.79s/ examples]Map:  60%|█████▉    | 121/203 [2:17:28<1:08:31, 50.14s/ examples]Map:  60%|██████    | 122/203 [2:18:12<1:05:17, 48.36s/ examples]Map:  61%|██████    | 123/203 [2:18:56<1:02:51, 47.14s/ examples]Martha Hampden has motive: True or False?
True (0.9838781949479747)
Martha Hampden has opportunity: True or False?
True (0.9294403817764149)
Steve Kravitz is guilty: True or False?
True (0.9856353404294369)
Steve Kravitz has mean: True or False?
True (0.879146760693242)
Steve Kravitz has motive: True or False?
True (0.9680808798281443)
Steve Kravitz has opportunity: True or False?
True (0.9392480858026054)
### Jane Croydon
- mean: False (0.15610491747858557)
- motive: False (0.016753255570005843)
- opportunity: False (0.06489014426517148)

### Johnny Martin
- mean: True (0.8727816933272936)
- motive: True (0.9758085604594696)
- opportunity: True (0.9522199623739209)

### Martha Hampden
- mean: False (0.11357957167753663)
- motive: False (0.016121805052025318)
- opportunity: False (0.07055961822358514)

### Steve Kravitz
- mean: False (0.12085323930675795)
- motive: False (0.03191912017185572)
- opportunity: False (0.06075191419739456)

The culprit is Johnny Martin.
In fact, it is Johnny Martin.
## 5minutemystery-the-hanging-figure
Daisy Morris is guilty: True or False?
True (0.9563089618154458)
Daisy Morris has mean: True or False?
True (0.9322068701708559)
Daisy Morris has motive: True or False?
True (0.9543930889248589)
Daisy Morris has opportunity: True or False?
True (0.9394705907755942)
Dale Clark is guilty: True or False?
True (0.930078152541638)
Dale Clark has mean: True or False?
True (0.847967740521315)
Dale Clark has motive: True or False?
True (0.9400235399552953)
Dale Clark has opportunity: True or False?
True (0.8860265599597172)
Iain Potts is guilty: True or False?
True (0.9308364374248909)
Iain Potts has mean: True or False?
True (0.8856314413364714)
Iain Potts has motive: True or False?
True (0.9142907234091052)
Iain Potts has opportunity: True or False?
True (0.8832359917473193)
Lucy Smith is guilty: True or False?
True (0.9309620852900756)
Lucy Smith has mean: True or False?
True (0.9082930095862076)
Lucy Smith has motive: True or False?
True (0.9392480858026054)
Lucy Smith has opportunity: True or False?
True (0.905322251510331)
### Daisy Morris
- mean: True (0.9322068701708559)
- motive: True (0.9543930889248589)
- opportunity: True (0.9394705907755942)

### Dale Clark
- mean: False (0.15203225947868504)
- motive: False (0.059976460044704694)
- opportunity: False (0.11397344004028276)

### Iain Potts
- mean: False (0.11436855866352857)
- motive: False (0.08570927659089478)
- opportunity: False (0.11676400825268074)

### Lucy Smith
- mean: False (0.09170699041379238)
- motive: False (0.06075191419739456)
- opportunity: False (0.09467774848966903)

The culprit is Daisy Morris.
In fact, it is Dale Clark.
## 5minutemystery-our-quarterback-is-missing
Coach Roster is guilty: True or False?
True (0.9637117373129486)
Coach Roster has mean: True or False?
True (0.925094725346746)
Coach Roster has motive: True or False?
True (0.9738443491650812)
Coach Roster has opportunity: True or False?
True (0.9386884590909785)
Eddie is guilty: True or False?
True (0.9408984770280414)
Eddie has mean: True or False?
True (0.9097467681279717)
Eddie has motive: True or False?
True (0.9561454058699453)
Eddie has opportunity: True or False?
True (0.8688267468984366)
Eddie's Mom is guilty: True or False?
True (0.9456006304504523)
Eddie's Mom has mean: True or False?
True (0.9114953293645017)
Eddie's Mom has motive: True or False?
True (0.9673486357359453)
Eddie's Mom has opportunity: True or False?
True (0.9053223122169206)
Marissa is guilty: True or False?
True (0.9747251273624444)
Marissa has mean: True or False?
True (0.9069831945855868)
Marissa has motive: True or False?
True (0.982724130018554)
Marissa has opportunity: True or False?
True (0.9399133918829404)
### Coach Roster
- mean: True (0.925094725346746)
- motive: True (0.9738443491650812)
- opportunity: True (0.9386884590909785)

### Eddie
- mean: False (0.09025323187202827)
- motive: False (0.04385459413005466)
- opportunity: False (0.13117325310156336)

### Eddie's Mom
- mean: False (0.08850467063549827)
- motive: False (0.03265136426405468)
- opportunity: False (0.09467768778307939)

### Marissa
- mean: False (0.09301680541441315)
- motive: False (0.017275869981446035)
- opportunity: False (0.06008660811705957)

The culprit is Coach Roster.
In fact, it is Eddie's Mom.
## 5minutemystery-ask-marthathe-case-of-the-missing-canary
Alex Johnston is guilty: True or False?
True (0.9227612010756272)
Alex Johnston has mean: True or False?
True (0.8852351930010195)
Alex Johnston has motive: True or False?
True (0.9756698013402983)
Alex Johnston has opportunity: True or False?
True (0.918480215734292)
Jimmy Carstairs is guilty: True or False?
True (0.9194980842090085)
Jimmy Carstairs has mean: True or False?
True (0.8526903338256402)
Jimmy Carstairs has motive: True or False?
True (0.9528381231454964)
Jimmy Carstairs has opportunity: True or False?
True (0.9286679635448885)
Lydia Carstairs is guilty: True or False?
True (0.968441008005572)
Lydia Carstairs has mean: True or False?
True (0.9073122118500465)
Lydia Carstairs has motive: True or False?
True (0.9803562168273844)
Lydia Carstairs has opportunity: True or False?
True (0.9322068701708559)
Sarabelle is guilty: True or False?
True (0.9467937951644804)
Sarabelle has mean: True or False?
True (0.873646672673131)
Sarabelle has motive: True or False?
True (0.9563904403130185)
Sarabelle has opportunity: True or False?
True (0.8539127714046447)
### Alex Johnston
- mean: False (0.1147648069989805)
- motive: False (0.024330198659701652)
- opportunity: False (0.08151978426570805)

### Jimmy Carstairs
- mean: False (0.1473096661743598)
- motive: False (0.04716187685450357)
- opportunity: False (0.07133203645511155)

### Lydia Carstairs
- mean: True (0.9073122118500465)
- motive: True (0.9803562168273844)
- opportunity: True (0.9322068701708559)

### Sarabelle
- mean: False (0.126353327326869)
- motive: False (0.04360955968698155)
- opportunity: False (0.14608722859535528)

The culprit is Lydia Carstairs.
In fact, it is Alex Johnston.
## 5minutemystery-register-robbery
Dan is guilty: True or False?
True (0.8590535670268302)
Dan has mean: True or False?
True (0.7676898810056793)
Dan has motive: True or False?
True (0.9399133918829404)
Dan has opportunity: True or False?
True (0.84440905415483)
David is guilty: True or False?
True (0.8885655424665229)
David has mean: True or False?
True (0.7209580648179327)
David has motive: True or False?
True (0.9324532728823121)
David has opportunity: True or False?
True (0.8360197583769845)
Robert is guilty: True or False?
True (0.8923750519147751)
Robert has mean: True or False?
True (0.5907791930117218)
Robert has motive: True or False?
True (0.8914335992201801)
Robert has opportunity: True or False?
True (0.7379143332111532)
Teresa is guilty: True or False?
True (1.1983431006124314)
Teresa has mean: True or False?
True (0.6011253583932805)
Teresa has motive: True or False?
True (1.5779629867344473)
Teresa has opportunity: True or False?
True (0.7248703250005105)
### Dan
- mean: True (0.7676898810056793)
- motive: True (0.9399133918829404)
- opportunity: True (0.84440905415483)

### David
- mean: False (0.2790419351820673)
- motive: False (0.06754672711768794)
- opportunity: False (0.1639802416230155)

### Robert
- mean: False (0.40922080698827823)
- motive: False (0.10856640077981994)
- opportunity: False (0.2620856667888468)

### Teresa
- mean: False (0.3988746416067195)
- motive: False (0.0)
- opportunity: False (0.2751296749994895)

The culprit is Dan.
In fact, it is David.
## 5minutemystery-mr-patrick-back-in-class
CSA currency is guilty: True or False?
True (0.9434518224682585)
CSA currency has mean: True or False?
True (0.6671476985798853)
CSA currency has motive: True or False?
True (0.9390248079664695)
CSA currency has opportunity: True or False?
True (0.920217993899809)
Diamond necklace is guilty: True or False?
True (0.9886243938205078)
Diamond necklace has mean: True or False?
True (0.9860979323093966)
Diamond necklace has motive: True or False?
True (0.9869166012557465)
Diamond necklace has opportunity: True or False?
True (0.9815950994553841)
Gold money clip is guilty: True or False?
Map:  61%|██████    | 124/203 [2:20:11<1:13:10, 55.58s/ examples]Map:  62%|██████▏   | 125/203 [2:21:09<1:13:05, 56.22s/ examples]Map:  62%|██████▏   | 126/203 [2:22:14<1:15:30, 58.84s/ examples]Map:  63%|██████▎   | 127/203 [2:23:24<1:18:49, 62.23s/ examples]True (0.9763782033334516)
Gold money clip has mean: True or False?
True (0.9375547191885567)
Gold money clip has motive: True or False?
True (0.9745561472167436)
Gold money clip has opportunity: True or False?
True (0.9605836282984641)
Jewel encrusted pistol is guilty: True or False?
True (0.9918516877713647)
Jewel encrusted pistol has mean: True or False?
True (0.9716178782667568)
Jewel encrusted pistol has motive: True or False?
True (0.9870919588955418)
Jewel encrusted pistol has opportunity: True or False?
True (0.9717789891296182)
Lithograph photo is guilty: True or False?
True (0.9805806866861946)
Lithograph photo has mean: True or False?
True (0.9859364033314291)
Lithograph photo has motive: True or False?
True (0.9728823298761804)
Lithograph photo has opportunity: True or False?
True (0.9715639953911919)
### CSA currency
- mean: False (0.3328523014201147)
- motive: False (0.06097519203353052)
- opportunity: False (0.07978200610019104)

### Diamond necklace
- mean: True (0.9860979323093966)
- motive: True (0.9869166012557465)
- opportunity: True (0.9815950994553841)

### Gold money clip
- mean: False (0.06244528081144329)
- motive: False (0.02544385278325645)
- opportunity: False (0.03941637170153589)

### Jewel encrusted pistol
- mean: False (0.02838212173324317)
- motive: False (0.012908041104458201)
- opportunity: False (0.028221010870381757)

### Lithograph photo
- mean: False (0.014063596668570932)
- motive: False (0.027117670123819604)
- opportunity: False (0.02843600460880813)

The culprit is Diamond necklace.
In fact, it is Lithograph photo.
## 5minutemystery-ask-marthathe-blackmailer
Horace Sage is guilty: True or False?
True (0.8656789607733094)
Horace Sage has mean: True or False?
True (0.7981867775042927)
Horace Sage has motive: True or False?
True (0.913058338092082)
Horace Sage has opportunity: True or False?
True (0.8633915828320894)
Martin Amberton is guilty: True or False?
True (0.7193836000532381)
Martin Amberton has mean: True or False?
True (0.7745833916423246)
Martin Amberton has motive: True or False?
True (0.8868131040663721)
Martin Amberton has opportunity: True or False?
True (0.7233094544266295)
Mary Devers is guilty: True or False?
True (0.8158201638039532)
Mary Devers has mean: True or False?
True (0.8386797310322072)
Mary Devers has motive: True or False?
True (0.9121235591541035)
Mary Devers has opportunity: True or False?
True (0.854884620116169)
Susan Royster is guilty: True or False?
True (0.7233094544266295)
Susan Royster has mean: True or False?
True (0.7431679939957333)
Susan Royster has motive: True or False?
True (0.8840393439819743)
Susan Royster has opportunity: True or False?
True (0.7655933544531522)
### Horace Sage
- mean: False (0.20181322249570732)
- motive: False (0.08694166190791797)
- opportunity: False (0.1366084171679106)

### Martin Amberton
- mean: False (0.2254166083576754)
- motive: False (0.11318689593362785)
- opportunity: False (0.27669054557337047)

### Mary Devers
- mean: True (0.8386797310322072)
- motive: True (0.9121235591541035)
- opportunity: True (0.854884620116169)

### Susan Royster
- mean: False (0.2568320060042667)
- motive: False (0.11596065601802574)
- opportunity: False (0.23440664554684776)

The culprit is Mary Devers.
In fact, it is Mary Devers.
## 5minutemystery-a-dream-of-old-salem
Abigail Thorpe is guilty: True or False?
True (0.8187367896794966)
Abigail Thorpe has mean: True or False?
True (0.6876299924560524)
Abigail Thorpe has motive: True or False?
True (0.9284088027271398)
Abigail Thorpe has opportunity: True or False?
True (0.8991213421091365)
Adam Browne is guilty: True or False?
True (0.7839884808423031)
Adam Browne has mean: True or False?
True (0.5409238971378262)
Adam Browne has motive: True or False?
True (0.8543993214720741)
Adam Browne has opportunity: True or False?
True (0.7833262085677729)
Goodwife Browne is guilty: True or False?
True (0.8524448242555318)
Goodwife Browne has mean: True or False?
True (0.6504672743423094)
Goodwife Browne has motive: True or False?
True (0.9383503780077049)
Goodwife Browne has opportunity: True or False?
True (0.8354834909254251)
Sarah Goodwin is guilty: True or False?
True (0.8300437258865985)
Sarah Goodwin has mean: True or False?
True (0.5926666351772785)
Sarah Goodwin has motive: True or False?
True (0.8122724274380432)
Sarah Goodwin has opportunity: True or False?
True (0.7520125537161032)
### Abigail Thorpe
- mean: True (0.6876299924560524)
- motive: True (0.9284088027271398)
- opportunity: True (0.8991213421091365)

### Adam Browne
- mean: False (0.4590761028621738)
- motive: False (0.1456006785279259)
- opportunity: False (0.2166737914322271)

### Goodwife Browne
- mean: False (0.34953272565769056)
- motive: False (0.06164962199229507)
- opportunity: False (0.16451650907457493)

### Sarah Goodwin
- mean: False (0.40733336482272153)
- motive: False (0.18772757256195682)
- opportunity: False (0.2479874462838968)

The culprit is Abigail Thorpe.
In fact, it is Adam Browne.
## 5minutemystery-the-antique-clock-mystery
The grandfather clock (stopped at 10:10 p.m.) is guilty: True or False?
True (0.9527503243194666)
The grandfather clock (stopped at 10:10 p.m.) has mean: True or False?
True (0.936749461409047)
The grandfather clock (stopped at 10:10 p.m.) has motive: True or False?
True (0.9707986706740892)
The grandfather clock (stopped at 10:10 p.m.) has opportunity: True or False?
True (0.9463988549853353)
The mantle clock (stopped at 10:59 p.m.) is guilty: True or False?
True (0.9313377150989219)
The mantle clock (stopped at 10:59 p.m.) has mean: True or False?
True (0.952397347230678)
The mantle clock (stopped at 10:59 p.m.) has motive: True or False?
True (0.9688561547723137)
The mantle clock (stopped at 10:59 p.m.) has opportunity: True or False?
True (0.9227612010756272)
The pocket watch (stopped at 3:18 a.m.) is guilty: True or False?
True (0.9624620067145623)
The pocket watch (stopped at 3:18 a.m.) has mean: True or False?
True (0.9396923783210908)
The pocket watch (stopped at 3:18 a.m.) has motive: True or False?
True (0.9706321357771589)
The pocket watch (stopped at 3:18 a.m.) has opportunity: True or False?
True (0.9447913165152162)
The wall clock (stopped at 2:01 a.m.) is guilty: True or False?
True (0.9396923783210908)
The wall clock (stopped at 2:01 a.m.) has mean: True or False?
True (0.9092645024391882)
The wall clock (stopped at 2:01 a.m.) has motive: True or False?
True (0.9705206155895632)
The wall clock (stopped at 2:01 a.m.) has opportunity: True or False?
True (0.927887794449634)
The wristwatch (stopped at 5:22 p.m.) is guilty: True or False?
True (0.9273633336539081)
The wristwatch (stopped at 5:22 p.m.) has mean: True or False?
True (0.9121235591541035)
The wristwatch (stopped at 5:22 p.m.) has motive: True or False?
True (0.9299510719523877)
The wristwatch (stopped at 5:22 p.m.) has opportunity: True or False?
True (0.9063219998220023)
### The grandfather clock (stopped at 10:10 p.m.)
- mean: False (0.06325053859095298)
- motive: False (0.029201329325910796)
- opportunity: False (0.05360114501466473)

### The mantle clock (stopped at 10:59 p.m.)
- mean: False (0.04760265276932196)
- motive: False (0.031143845227686318)
- opportunity: False (0.0772387989243728)

### The pocket watch (stopped at 3:18 a.m.)
- mean: True (0.9396923783210908)
- motive: True (0.9706321357771589)
- opportunity: True (0.9447913165152162)

### The wall clock (stopped at 2:01 a.m.)
- mean: False (0.09073549756081178)
- motive: False (0.02947938441043685)
- opportunity: False (0.07211220555036602)

### The wristwatch (stopped at 5:22 p.m.)
- mean: False (0.08787644084589652)
- motive: False (0.07004892804761231)
- opportunity: False (0.09367800017799766)

The culprit is The pocket watch (stopped at 3:18 a.m.).
In fact, it is The mantle clock (stopped at 10:59 p.m.).
## 5minutemystery-ask-marthathe-perjurer
Horace Osamway is guilty: True or False?
True (0.8982321647536474)
Horace Osamway has mean: True or False?
True (0.8098781635062345)
Horace Osamway has motive: True or False?
True (0.9450961931109775)
Horace Osamway has opportunity: True or False?
True (0.9458013187522837)
Map:  63%|██████▎   | 128/203 [2:24:28<1:18:25, 62.74s/ examples]Map:  64%|██████▎   | 129/203 [2:25:43<1:22:00, 66.50s/ examples]Map:  64%|██████▍   | 130/203 [2:26:30<1:13:40, 60.55s/ examples]Map:  65%|██████▍   | 131/203 [2:27:45<1:17:42, 64.75s/ examples]John Eberley is guilty: True or False?
True (0.8622357197068287)
John Eberley has mean: True or False?
True (0.6876299924560524)
John Eberley has motive: True or False?
True (0.9031234959323464)
John Eberley has opportunity: True or False?
True (0.7570766705324253)
Martha Cranston is guilty: True or False?
True (0.8247443993706964)
Martha Cranston has mean: True or False?
True (0.591723272524637)
Martha Cranston has motive: True or False?
True (0.9087799803825275)
Martha Cranston has opportunity: True or False?
True (0.7074046739492601)
Mildred Greene is guilty: True or False?
True (0.8092759225969047)
Mildred Greene has mean: True or False?
True (0.5879431210535583)
Mildred Greene has motive: True or False?
True (0.8631610245991334)
Mildred Greene has opportunity: True or False?
True (0.7017130830397807)
### Horace Osamway
- mean: True (0.8098781635062345)
- motive: True (0.9450961931109775)
- opportunity: True (0.9458013187522837)

### John Eberley
- mean: False (0.3123700075439476)
- motive: False (0.09687650406765358)
- opportunity: False (0.24292332946757467)

### Martha Cranston
- mean: False (0.40827672747536303)
- motive: False (0.0912200196174725)
- opportunity: False (0.2925953260507399)

### Mildred Greene
- mean: False (0.4120568789464417)
- motive: False (0.13683897540086665)
- opportunity: False (0.29828691696021925)

The culprit is Horace Osamway.
In fact, it is John Eberley.
## 5minutemystery-ask-marthathe-embezzler
Joan Carstairs is guilty: True or False?
True (0.816406362162552)
Joan Carstairs has mean: True or False?
True (0.5841525779336078)
Joan Carstairs has motive: True or False?
True (0.9124361266596831)
Joan Carstairs has opportunity: True or False?
True (0.7898827135821628)
Les Nolting is guilty: True or False?
True (0.8300437877296776)
Les Nolting has mean: True or False?
True (0.705785027818136)
Les Nolting has motive: True or False?
True (0.8883720049821552)
Les Nolting has opportunity: True or False?
True (0.7975568155246964)
Paul Brassard is guilty: True or False?
True (0.8714748565614324)
Paul Brassard has mean: True or False?
True (0.7872777601997338)
Paul Brassard has motive: True or False?
True (0.9353465445225602)
Paul Brassard has opportunity: True or False?
True (0.789233749534095)
Sarah Kimble is guilty: True or False?
True (0.8278281666221954)
Sarah Kimble has mean: True or False?
True (0.7779753136455794)
Sarah Kimble has motive: True or False?
True (0.9257686153543061)
Sarah Kimble has opportunity: True or False?
True (0.7193836643711469)
### Joan Carstairs
- mean: False (0.41584742206639225)
- motive: False (0.0875638733403169)
- opportunity: False (0.21011728641783722)

### Les Nolting
- mean: False (0.294214972181864)
- motive: False (0.11162799501784482)
- opportunity: False (0.20244318447530363)

### Paul Brassard
- mean: True (0.7872777601997338)
- motive: True (0.9353465445225602)
- opportunity: True (0.789233749534095)

### Sarah Kimble
- mean: False (0.22202468635442063)
- motive: False (0.0742313846456939)
- opportunity: False (0.28061633562885313)

The culprit is Paul Brassard.
In fact, it is Sarah Kimble.
## 5minutemystery-the-backyard-slumber-party
Justin Scott is guilty: True or False?
True (0.9643214331583058)
Justin Scott has mean: True or False?
True (0.9543079730970608)
Justin Scott has motive: True or False?
True (0.9875922800954249)
Justin Scott has opportunity: True or False?
True (0.9791157846694846)
Martin Simmons is guilty: True or False?
True (0.927887794449634)
Martin Simmons has mean: True or False?
True (0.91789335161495)
Martin Simmons has motive: True or False?
True (0.9799573413335708)
Martin Simmons has opportunity: True or False?
True (0.9870296120305199)
Stephen Kennelly is guilty: True or False?
True (0.9381240005131491)
Stephen Kennelly has mean: True or False?
True (0.8803862939824989)
Stephen Kennelly has motive: True or False?
True (0.9674102673982512)
Stephen Kennelly has opportunity: True or False?
True (0.9525741334779666)
Trevor Sutherland is guilty: True or False?
True (0.9372107968415931)
Trevor Sutherland has mean: True or False?
True (0.9317114347547434)
Trevor Sutherland has motive: True or False?
True (0.9746287473052455)
Trevor Sutherland has opportunity: True or False?
True (0.9781354673766767)
### Justin Scott
- mean: True (0.9543079730970608)
- motive: True (0.9875922800954249)
- opportunity: True (0.9791157846694846)

### Martin Simmons
- mean: False (0.08210664838505)
- motive: False (0.02004265866642918)
- opportunity: False (0.012970387969480135)

### Stephen Kennelly
- mean: False (0.1196137060175011)
- motive: False (0.0325897326017488)
- opportunity: False (0.0474258665220334)

### Trevor Sutherland
- mean: False (0.06828856524525662)
- motive: False (0.025371252694754487)
- opportunity: False (0.02186453262332333)

The culprit is Justin Scott.
In fact, it is Trevor Sutherland.
## 5minutemystery-the-rock-star-mystery
Gorg is guilty: True or False?
True (0.9816655524802333)
Gorg has mean: True or False?
True (0.9460011721384068)
Gorg has motive: True or False?
True (0.9852996465775707)
Gorg has opportunity: True or False?
True (0.9514138119240159)
Stu is guilty: True or False?
True (0.9319595674053855)
Stu has mean: True or False?
True (0.9238675252821831)
Stu has motive: True or False?
True (0.9796676632098326)
Stu has opportunity: True or False?
True (0.9697281713378947)
The Neighborhood Burgler is guilty: True or False?
True (0.959912598704516)
The Neighborhood Burgler has mean: True or False?
True (0.9505029326253388)
The Neighborhood Burgler has motive: True or False?
True (0.9816655524802333)
The Neighborhood Burgler has opportunity: True or False?
True (0.9685006130461804)
Tina is guilty: True or False?
True (0.9675331712558415)
Tina has mean: True or False?
True (0.878314250659373)
Tina has motive: True or False?
True (0.9647889147180926)
Tina has opportunity: True or False?
True (0.8991214023999228)
### Gorg
- mean: False (0.05399882786159316)
- motive: False (0.014700353422429258)
- opportunity: False (0.04858618807598414)

### Stu
- mean: False (0.07613247471781692)
- motive: False (0.020332336790167438)
- opportunity: False (0.030271828662105316)

### The Neighborhood Burgler
- mean: True (0.9505029326253388)
- motive: True (0.9816655524802333)
- opportunity: True (0.9685006130461804)

### Tina
- mean: False (0.12168574934062704)
- motive: False (0.03521108528190742)
- opportunity: False (0.10087859760007722)

The culprit is The Neighborhood Burgler.
In fact, it is Tina.
## 5minutemystery-ask-marthathe-arsonist
Keen Observer is guilty: True or False?
True (0.8524448242555318)
Keen Observer has mean: True or False?
True (0.861071588244826)
Keen Observer has motive: True or False?
True (0.9319595674053855)
Keen Observer has opportunity: True or False?
True (0.9410069597342015)
Minding My Own Business is guilty: True or False?
True (0.8740772044235984)
Minding My Own Business has mean: True or False?
True (0.9133679254389228)
Minding My Own Business has motive: True or False?
True (0.9471859926317535)
Minding My Own Business has opportunity: True or False?
True (0.9567959908103164)
Scared Stiff is guilty: True or False?
True (0.8832359917473193)
Scared Stiff has mean: True or False?
True (0.9388008138003494)
Scared Stiff has motive: True or False?
True (0.9661560069290531)
Scared Stiff has opportunity: True or False?
True (0.9304582506719414)
Watchful Waiter is guilty: True or False?
True (0.8175745039697023)
Watchful Waiter has mean: True or False?
True (0.8019358443954961)
Watchful Waiter has motive: True or False?
True (0.9149009617112335)
Watchful Waiter has opportunity: True or False?
True (0.8701565303520181)
### Keen Observer
- mean: False (0.138928411755174)
- motive: False (0.06804043259461445)
- opportunity: False (0.058993040265798546)

### Minding My Own Business
- mean: False (0.08663207456107724)
- motive: False (0.052814007368246485)
- opportunity: False (0.04320400918968359)

### Scared Stiff
- mean: True (0.9388008138003494)
- motive: True (0.9661560069290531)
- opportunity: True (0.9304582506719414)

### Watchful Waiter
- mean: False (0.19806415560450386)
- motive: False (0.08509903828876653)
Map:  65%|██████▌   | 132/203 [2:28:32<1:10:29, 59.57s/ examples]Map:  66%|██████▌   | 133/203 [2:29:33<1:10:03, 60.04s/ examples]Map:  66%|██████▌   | 134/203 [2:30:29<1:07:24, 58.61s/ examples]Map:  67%|██████▋   | 135/203 [2:31:18<1:03:22, 55.92s/ examples]Map:  67%|██████▋   | 136/203 [2:32:13<1:01:58, 55.51s/ examples]- opportunity: False (0.12984346964798188)

The culprit is Scared Stiff.
In fact, it is Watchful Waiter.
## 5minutemystery-fatal-computer-crash
Alex Redoff is guilty: True or False?
True (0.9210741501882456)
Alex Redoff has mean: True or False?
True (0.9233161821369215)
Alex Redoff has motive: True or False?
True (0.9565531009888748)
Alex Redoff has opportunity: True or False?
True (0.9577545517476556)
Cheryl Compton is guilty: True or False?
True (0.9257686153543061)
Cheryl Compton has mean: True or False?
True (0.8872045854516336)
Cheryl Compton has motive: True or False?
True (0.9436599010766334)
Cheryl Compton has opportunity: True or False?
True (0.9356999401883446)
Claire Denninger is guilty: True or False?
True (0.9095863097773887)
Claire Denninger has mean: True or False?
True (0.9010534302227574)
Claire Denninger has motive: True or False?
True (0.9347534165970482)
Claire Denninger has opportunity: True or False?
True (0.9477691649813238)
Natalie Sampson is guilty: True or False?
True (0.9199306971612747)
Natalie Sampson has mean: True or False?
True (0.8895288719962232)
Natalie Sampson has motive: True or False?
True (0.9537942396657707)
Natalie Sampson has opportunity: True or False?
True (0.9466952677359475)
### Alex Redoff
- mean: True (0.9233161821369215)
- motive: True (0.9565531009888748)
- opportunity: True (0.9577545517476556)

### Cheryl Compton
- mean: False (0.11279541454836639)
- motive: False (0.056340098923366555)
- opportunity: False (0.06430005981165543)

### Claire Denninger
- mean: False (0.09894656977724259)
- motive: False (0.06524658340295175)
- opportunity: False (0.0522308350186762)

### Natalie Sampson
- mean: False (0.11047112800377679)
- motive: False (0.046205760334229296)
- opportunity: False (0.05330473226405252)

The culprit is Alex Redoff.
In fact, it is Natalie Sampson.
## 5minutemystery-the-rob-club-murder-mystery
Al Gibson is guilty: True or False?
True (0.9854684474764122)
Al Gibson has mean: True or False?
True (0.8723473540228537)
Al Gibson has motive: True or False?
True (0.9910233023598813)
Al Gibson has opportunity: True or False?
True (0.9760379793845908)
Johnny Woodward is guilty: True or False?
True (0.9873017666029376)
Johnny Woodward has mean: True or False?
True (0.9741412398478105)
Johnny Woodward has motive: True or False?
True (0.9970963000269885)
Johnny Woodward has opportunity: True or False?
True (0.9957684278724305)
Ray Shields is guilty: True or False?
True (0.9859364033314291)
Ray Shields has mean: True or False?
True (0.9596109393754703)
Ray Shields has motive: True or False?
True (0.9937949778263467)
Ray Shields has opportunity: True or False?
True (0.974580348460635)
Tim Acord is guilty: True or False?
True (0.9798997635332343)
Tim Acord has mean: True or False?
True (0.9184802773231918)
Tim Acord has motive: True or False?
True (0.9898303149898466)
Tim Acord has opportunity: True or False?
True (0.9706877478963396)
Watson Treadway is guilty: True or False?
True (0.982590972614882)
Watson Treadway has mean: True or False?
True (0.8895288719962232)
Watson Treadway has motive: True or False?
True (0.9954305886032181)
Watson Treadway has opportunity: True or False?
True (0.9632304925109479)
### Al Gibson
- mean: False (0.12765264597714632)
- motive: False (0.008976697640118658)
- opportunity: False (0.023962020615409196)

### Johnny Woodward
- mean: True (0.9741412398478105)
- motive: True (0.9970963000269885)
- opportunity: True (0.9957684278724305)

### Ray Shields
- mean: False (0.04038906062452974)
- motive: False (0.006205022173653263)
- opportunity: False (0.025419651539364985)

### Tim Acord
- mean: False (0.08151972267680818)
- motive: False (0.010169685010153362)
- opportunity: False (0.029312252103660397)

### Watson Treadway
- mean: False (0.11047112800377679)
- motive: False (0.004569411396781908)
- opportunity: False (0.036769507489052056)

The culprit is Johnny Woodward.
In fact, it is Johnny Woodward.
## 5minutemystery-ask-marthathe-litterer
Concerned Neighbor is guilty: True or False?
True (0.7394223819718238)
Concerned Neighbor has mean: True or False?
True (0.7527403228571042)
Concerned Neighbor has motive: True or False?
True (0.9095862487848758)
Concerned Neighbor has opportunity: True or False?
True (0.8116760258690822)
Confused Commuter is guilty: True or False?
True (0.9412234437340664)
Confused Commuter has mean: True or False?
True (0.934155284694701)
Confused Commuter has motive: True or False?
True (0.9539660824292815)
Confused Commuter has opportunity: True or False?
True (0.9669139993413022)
Perplexed Dog Walker is guilty: True or False?
True (0.9029524325377104)
Perplexed Dog Walker has mean: True or False?
True (0.920217993899809)
Perplexed Dog Walker has motive: True or False?
True (0.9449947479233238)
Perplexed Dog Walker has opportunity: True or False?
True (0.9590009457171959)
Smug in Suburbia is guilty: True or False?
True (0.8553685501761973)
Smug in Suburbia has mean: True or False?
True (0.8828325273478573)
Smug in Suburbia has motive: True or False?
True (0.875361437979977)
Smug in Suburbia has opportunity: True or False?
True (0.8816149238192855)
### Concerned Neighbor
- mean: False (0.24725967714289576)
- motive: False (0.09041375121512418)
- opportunity: False (0.18832397413091784)

### Confused Commuter
- mean: True (0.934155284694701)
- motive: True (0.9539660824292815)
- opportunity: True (0.9669139993413022)

### Perplexed Dog Walker
- mean: False (0.07978200610019104)
- motive: False (0.05500525207667617)
- opportunity: False (0.04099905428280415)

### Smug in Suburbia
- mean: False (0.11716747265214267)
- motive: False (0.12463856202002299)
- opportunity: False (0.11838507618071448)

The culprit is Confused Commuter.
In fact, it is Smug in Suburbia.
## 5minutemystery-drama-queen
Alfred Cooper is guilty: True or False?
True (0.8289388437432279)
Alfred Cooper has mean: True or False?
True (0.7613611200983542)
Alfred Cooper has motive: True or False?
True (0.9384632725948482)
Alfred Cooper has opportunity: True or False?
True (0.8587185689177256)
Isabelle Rogers is guilty: True or False?
True (0.9046505126460354)
Isabelle Rogers has mean: True or False?
True (0.8407825844829613)
Isabelle Rogers has motive: True or False?
True (0.9244152304846833)
Isabelle Rogers has opportunity: True or False?
True (0.8423451152856819)
James Fennimore is guilty: True or False?
True (0.925499741040984)
James Fennimore has mean: True or False?
True (0.8688267468984366)
James Fennimore has motive: True or False?
True (0.941654207327861)
James Fennimore has opportunity: True or False?
True (0.8333246107254184)
Madge Anderson is guilty: True or False?
True (0.92386746333204)
Madge Anderson has mean: True or False?
True (0.8344068526674736)
Madge Anderson has motive: True or False?
True (0.9584600345758558)
Madge Anderson has opportunity: True or False?
True (0.8204694405411458)
### Alfred Cooper
- mean: False (0.23863887990164578)
- motive: False (0.061536727405151814)
- opportunity: False (0.14128143108227442)

### Isabelle Rogers
- mean: False (0.15921741551703872)
- motive: False (0.07558476951531667)
- opportunity: False (0.1576548847143181)

### James Fennimore
- mean: True (0.8688267468984366)
- motive: True (0.941654207327861)
- opportunity: True (0.8333246107254184)

### Madge Anderson
- mean: False (0.1655931473325264)
- motive: False (0.041539965424144176)
- opportunity: False (0.1795305594588542)

The culprit is James Fennimore.
In fact, it is James Fennimore.
## 5minutemystery-the-gourmet-mystery
Antoine is guilty: True or False?
True (0.6557770400181139)
Antoine has mean: True or False?
True (0.7799928701983835)
Antoine has motive: True or False?
True (0.8966140148346177)
Antoine has opportunity: True or False?
True (0.8679338697256817)
Georges Monceau is guilty: True or False?
True (0.8134607635851566)
Georges Monceau has mean: True or False?
True (0.7287483223557857)
Georges Monceau has motive: True or False?
True (0.921357630313903)
Georges Monceau has opportunity: True or False?
True (0.8984105603938967)
Sally Horvats is guilty: True or False?
True (0.8665847814067802)
Sally Horvats has mean: True or False?
True (0.94519740270931)
Map:  67%|██████▋   | 137/203 [2:33:01<58:48, 53.47s/ examples]  Map:  68%|██████▊   | 138/203 [2:34:13<1:03:38, 58.75s/ examples]Map:  68%|██████▊   | 139/203 [2:35:11<1:02:25, 58.52s/ examples]Map:  69%|██████▉   | 140/203 [2:36:06<1:00:30, 57.63s/ examples]Map:  69%|██████▉   | 141/203 [2:37:14<1:02:42, 60.68s/ examples]Sally Horvats has motive: True or False?
True (0.9489172681310486)
Sally Horvats has opportunity: True or False?
True (0.9284088027271398)
Sam Wheeler is guilty: True or False?
True (0.816406362162552)
Sam Wheeler has mean: True or False?
True (0.8643104392003704)
Sam Wheeler has motive: True or False?
True (0.9319595674053855)
Sam Wheeler has opportunity: True or False?
True (0.9257686153543061)
### Antoine
- mean: False (0.22000712980161652)
- motive: False (0.10338598516538233)
- opportunity: False (0.13206613027431835)

### Georges Monceau
- mean: False (0.2712516776442143)
- motive: False (0.07864236968609695)
- opportunity: False (0.10158943960610334)

### Sally Horvats
- mean: True (0.94519740270931)
- motive: True (0.9489172681310486)
- opportunity: True (0.9284088027271398)

### Sam Wheeler
- mean: False (0.13568956079962957)
- motive: False (0.06804043259461445)
- opportunity: False (0.0742313846456939)

The culprit is Sally Horvats.
In fact, it is Sally Horvats.
## 5minutemystery-the-potter-book-mystery
Alfred is guilty: True or False?
True (0.9485372300670596)
Alfred has mean: True or False?
True (0.8255897087847518)
Alfred has motive: True or False?
True (0.9718859797630299)
Alfred has opportunity: True or False?
True (0.9422947179693436)
Ann is guilty: True or False?
True (0.9479621664653681)
Ann has mean: True or False?
True (0.9102267057681164)
Ann has motive: True or False?
True (0.9545627850600183)
Ann has opportunity: True or False?
True (0.9580694433457548)
Rusty is guilty: True or False?
True (0.9584600345758558)
Rusty has mean: True or False?
True (0.7931059536445917)
Rusty has motive: True or False?
True (0.9646558768023054)
Rusty has opportunity: True or False?
True (0.8940516749601143)
Uncle Ezra is guilty: True or False?
True (0.7988152492192591)
Uncle Ezra has mean: True or False?
True (0.7969253675907205)
Uncle Ezra has motive: True or False?
True (0.9308364374248909)
Uncle Ezra has opportunity: True or False?
True (0.8860265005470086)
### Alfred
- mean: False (0.1744102912152482)
- motive: False (0.028114020236970072)
- opportunity: False (0.05770528203065639)

### Ann
- mean: True (0.9102267057681164)
- motive: True (0.9545627850600183)
- opportunity: True (0.9580694433457548)

### Rusty
- mean: False (0.2068940463554083)
- motive: False (0.035344123197694644)
- opportunity: False (0.10594832503988572)

### Uncle Ezra
- mean: False (0.20307463240927948)
- motive: False (0.06916356257510914)
- opportunity: False (0.1139734994529914)

The culprit is Ann.
In fact, it is Uncle Ezra.
## 5minutemystery-death-in-the-office
Cynthia Peck is guilty: True or False?
True (0.9489645957880718)
Cynthia Peck has mean: True or False?
True (0.9305845477606799)
Cynthia Peck has motive: True or False?
True (0.9508691427698753)
Cynthia Peck has opportunity: True or False?
True (0.8774768149941248)
Josh Kesler is guilty: True or False?
True (0.9554855815192022)
Josh Kesler has mean: True or False?
True (0.9465966236120936)
Josh Kesler has motive: True or False?
True (0.9455001349615358)
Josh Kesler has opportunity: True or False?
True (0.927099763868178)
Megan Brewer is guilty: True or False?
True (0.8000678954040312)
Megan Brewer has mean: True or False?
True (0.861071588244826)
Megan Brewer has motive: True or False?
True (0.8019357965963964)
Megan Brewer has opportunity: True or False?
True (0.7725306828324007)
Steve Ledbetter is guilty: True or False?
True (0.9183339469066092)
Steve Ledbetter has mean: True or False?
True (0.9643886093607492)
Steve Ledbetter has motive: True or False?
True (0.9008791478232747)
Steve Ledbetter has opportunity: True or False?
True (0.9189178954169608)
### Cynthia Peck
- mean: False (0.06941545223932011)
- motive: False (0.04913085723012467)
- opportunity: False (0.12252318500587522)

### Josh Kesler
- mean: True (0.9465966236120936)
- motive: True (0.9455001349615358)
- opportunity: True (0.927099763868178)

### Megan Brewer
- mean: False (0.138928411755174)
- motive: False (0.19806420340360364)
- opportunity: False (0.22746931716759933)

### Steve Ledbetter
- mean: False (0.035611390639250784)
- motive: False (0.09912085217672528)
- opportunity: False (0.08108210458303922)

The culprit is Josh Kesler.
In fact, it is Megan Brewer.
## 5minutemystery-chief-inspector-japp-solves-a-case
Alan Harrison is guilty: True or False?
True (0.9558166865608263)
Alan Harrison has mean: True or False?
True (0.9304582506719414)
Alan Harrison has motive: True or False?
True (0.9564718616162037)
Alan Harrison has opportunity: True or False?
True (0.941654147692963)
Evelyn Johnston is guilty: True or False?
True (0.9534487112250288)
Evelyn Johnston has mean: True or False?
True (0.9319596298981465)
Evelyn Johnston has motive: True or False?
True (0.9505947242503305)
Evelyn Johnston has opportunity: True or False?
True (0.944176853162527)
George Smythe is guilty: True or False?
True (0.9591543064115948)
George Smythe has mean: True or False?
True (0.9241418261705818)
George Smythe has motive: True or False?
True (0.9603611816439128)
George Smythe has opportunity: True or False?
True (0.9170058945178141)
Herbert Grosvenor is guilty: True or False?
True (0.9720985894741414)
Herbert Grosvenor has mean: True or False?
True (0.9331876642092066)
Herbert Grosvenor has motive: True or False?
True (0.972727357600667)
Herbert Grosvenor has opportunity: True or False?
True (0.9580695040202324)
### Alan Harrison
- mean: False (0.06954174932805857)
- motive: False (0.04352813838379632)
- opportunity: False (0.05834585230703704)

### Evelyn Johnston
- mean: False (0.06804037010185349)
- motive: False (0.049405275749669464)
- opportunity: False (0.055823146837473026)

### George Smythe
- mean: False (0.07585817382941817)
- motive: False (0.03963881835608718)
- opportunity: False (0.08299410548218589)

### Herbert Grosvenor
- mean: True (0.9331876642092066)
- motive: True (0.972727357600667)
- opportunity: True (0.9580695040202324)

The culprit is Herbert Grosvenor.
In fact, it is Alan Harrison.
## 5minutemystery-who-stole-the-cavemans-dinner
Dinosaur is guilty: True or False?
True (0.8665847814067802)
Dinosaur has mean: True or False?
False (0.5602526707659626)
Dinosaur has motive: True or False?
True (0.8294919722593475)
Dinosaur has opportunity: True or False?
True (0.811078188867804)
Droo is guilty: True or False?
True (0.9390248079664695)
Droo has mean: True or False?
True (0.7725306828324007)
Droo has motive: True or False?
True (0.9650533199435419)
Droo has opportunity: True or False?
True (0.9309620852900756)
Father is guilty: True or False?
True (0.9365176577773374)
Father has mean: True or False?
True (0.8261514850267767)
Father has motive: True or False?
True (0.935346481802689)
Father has opportunity: True or False?
True (0.9307105568817887)
Monkeys is guilty: True or False?
True (0.9066531077351827)
Monkeys has mean: True or False?
True (0.8338664756137771)
Monkeys has motive: True or False?
True (0.9515939960119401)
Monkeys has opportunity: True or False?
True (0.9365176577773374)
### Dinosaur
- mean: False (0.5602526707659626)
- motive: False (0.17050802774065255)
- opportunity: False (0.18892181113219597)

### Droo
- mean: False (0.22746931716759933)
- motive: False (0.03494668005645807)
- opportunity: False (0.06903791470992438)

### Father
- mean: False (0.1738485149732233)
- motive: False (0.06465351819731102)
- opportunity: False (0.06928944311821128)

### Monkeys
- mean: True (0.8338664756137771)
- motive: True (0.9515939960119401)
- opportunity: True (0.9365176577773374)

The culprit is Monkeys.
In fact, it is Dinosaur.
## 5minutemystery-the-stolen-car-mystery
David Kelly is guilty: True or False?
True (0.928538502080124)
David Kelly has mean: True or False?
True (0.9020932932190145)
David Kelly has motive: True or False?
True (0.9814889431064477)
David Kelly has opportunity: True or False?
True (0.9566341655109778)
Donna Allen is guilty: True or False?
True (0.9656412588860065)
Donna Allen has mean: True or False?
True (0.9286680258169302)
Donna Allen has motive: True or False?
True (0.9806919106398481)
Donna Allen has opportunity: True or False?
True (0.9597620378565557)
Map:  70%|██████▉   | 142/203 [2:37:50<54:10, 53.29s/ examples]  Map:  70%|███████   | 143/203 [2:39:24<1:05:36, 65.60s/ examples]Map:  71%|███████   | 144/203 [2:40:08<58:10, 59.16s/ examples]  Map:  71%|███████▏  | 145/203 [2:40:55<53:35, 55.45s/ examples]Larry Roberts is guilty: True or False?
True (0.9268353022276509)
Larry Roberts has mean: True or False?
True (0.8489722037469682)
Larry Roberts has motive: True or False?
True (0.9680204387474981)
Larry Roberts has opportunity: True or False?
True (0.9498557456415421)
Nancy Lee is guilty: True or False?
True (0.9626730694627891)
Nancy Lee has mean: True or False?
True (0.913058338092082)
Nancy Lee has motive: True or False?
True (0.9822196365979101)
Nancy Lee has opportunity: True or False?
True (0.9224823751318276)
### David Kelly
- mean: False (0.09790670678098545)
- motive: False (0.018511056893552258)
- opportunity: False (0.043365834489022204)

### Donna Allen
- mean: True (0.9286680258169302)
- motive: True (0.9806919106398481)
- opportunity: True (0.9597620378565557)

### Larry Roberts
- mean: False (0.15102779625303175)
- motive: False (0.0319795612525019)
- opportunity: False (0.05014425435845793)

### Nancy Lee
- mean: False (0.08694166190791797)
- motive: False (0.017780363402089883)
- opportunity: False (0.07751762486817237)

The culprit is Donna Allen.
In fact, it is Donna Allen.
## 5minutemystery-the-straw-hat-theater-mysteriesfinal-curtain
Arthur Glendon is guilty: True or False?
True (0.8727817583545995)
Arthur Glendon has mean: True or False?
True (0.8620035048683017)
Arthur Glendon has motive: True or False?
True (0.8762113474663927)
Arthur Glendon has opportunity: True or False?
True (0.9625325207646147)
Josh Whitehead is guilty: True or False?
True (0.854884620116169)
Josh Whitehead has mean: True or False?
True (0.9294403817764149)
Josh Whitehead has motive: True or False?
True (0.908941745727715)
Josh Whitehead has opportunity: True or False?
True (0.9460011122282159)
Linda Eberlie is guilty: True or False?
True (0.9286680258169302)
Linda Eberlie has mean: True or False?
True (0.9036349079321685)
Linda Eberlie has motive: True or False?
True (0.9241418261705818)
Linda Eberlie has opportunity: True or False?
True (0.958847105894029)
Sam Watson is guilty: True or False?
True (0.9281487460975983)
Sam Watson has mean: True or False?
True (0.9291837815043049)
Sam Watson has motive: True or False?
True (0.9365176577773374)
Sam Watson has opportunity: True or False?
True (0.9716717007848752)
Stella Marlowe is guilty: True or False?
True (0.8305940642606888)
Stella Marlowe has mean: True or False?
True (0.9216401608061056)
Stella Marlowe has motive: True or False?
True (0.8499711693725173)
Stella Marlowe has opportunity: True or False?
True (0.9561454058699453)
### Arthur Glendon
- mean: False (0.13799649513169832)
- motive: False (0.12378865253360727)
- opportunity: False (0.03746747923538529)

### Josh Whitehead
- mean: False (0.07055961822358514)
- motive: False (0.09105825427228498)
- opportunity: False (0.053998887771784077)

### Linda Eberlie
- mean: False (0.0963650920678315)
- motive: False (0.07585817382941817)
- opportunity: False (0.041152894105971005)

### Sam Watson
- mean: True (0.9291837815043049)
- motive: True (0.9365176577773374)
- opportunity: True (0.9716717007848752)

### Stella Marlowe
- mean: False (0.07835983919389444)
- motive: False (0.15002883062748273)
- opportunity: False (0.04385459413005466)

The culprit is Sam Watson.
In fact, it is Linda Eberlie.
## 5minutemystery-itheft
Lea Thompson is guilty: True or False?
True (0.9374402785760423)
Lea Thompson has mean: True or False?
True (0.8677098176365254)
Lea Thompson has motive: True or False?
True (0.9639160647221925)
Lea Thompson has opportunity: True or False?
True (0.9546474221708894)
Rachel Vermeer is guilty: True or False?
True (0.9008791478232747)
Rachel Vermeer has mean: True or False?
True (0.8969755785184792)
Rachel Vermeer has motive: True or False?
True (0.9702962635848237)
Rachel Vermeer has opportunity: True or False?
True (0.9281487460975983)
Shawn Ramos is guilty: True or False?
True (0.9099070446252667)
Shawn Ramos has mean: True or False?
True (0.8539127714046447)
Shawn Ramos has motive: True or False?
True (0.9808025352018944)
Shawn Ramos has opportunity: True or False?
True (0.9435559526996434)
Shay Dulaney is guilty: True or False?
True (0.9281487460975983)
Shay Dulaney has mean: True or False?
True (0.823044124016779)
Shay Dulaney has motive: True or False?
True (0.9558166865608263)
Shay Dulaney has opportunity: True or False?
True (0.9044818892710186)
### Lea Thompson
- mean: False (0.13229018236347456)
- motive: False (0.03608393527780751)
- opportunity: False (0.04535257782911062)

### Rachel Vermeer
- mean: True (0.8969755785184792)
- motive: True (0.9702962635848237)
- opportunity: True (0.9281487460975983)

### Shawn Ramos
- mean: False (0.14608722859535528)
- motive: False (0.01919746479810558)
- opportunity: False (0.05644404730035657)

### Shay Dulaney
- mean: False (0.17695587598322104)
- motive: False (0.0441833134391737)
- opportunity: False (0.09551811072898142)

The culprit is Rachel Vermeer.
In fact, it is Rachel Vermeer.
## 5minutemystery-the-punch-with-a-punch
Carole is guilty: True or False?
True (0.7446563307563252)
Carole has mean: True or False?
False (0.5341265295318852)
Carole has motive: True or False?
True (0.8705972382426559)
Carole has opportunity: True or False?
True (0.8098781635062345)
Dan is guilty: True or False?
True (0.6901415551283886)
Dan has mean: True or False?
True (0.6113819501087365)
Dan has motive: True or False?
True (0.9319595674053855)
Dan has opportunity: True or False?
True (0.8947895144283036)
Diane is guilty: True or False?
True (0.7620701143808404)
Diane has mean: True or False?
True (0.5292634408007735)
Diane has motive: True or False?
True (0.9136765013387816)
Diane has opportunity: True or False?
True (0.8104789202520752)
Principal Whittenmeyer is guilty: True or False?
True (0.8204694405411458)
Principal Whittenmeyer has mean: True or False?
True (0.49999999904767284)
Principal Whittenmeyer has motive: True or False?
True (0.9376689781587124)
Principal Whittenmeyer has opportunity: True or False?
True (0.8272706865691472)
### Carole
- mean: False (0.5341265295318852)
- motive: False (0.1294027617573441)
- opportunity: False (0.19012183649376546)

### Dan
- mean: True (0.6113819501087365)
- motive: True (0.9319595674053855)
- opportunity: True (0.8947895144283036)

### Diane
- mean: False (0.4707365591992265)
- motive: False (0.08632349866121836)
- opportunity: False (0.18952107974792476)

### Principal Whittenmeyer
- mean: False (0.5000000009523271)
- motive: False (0.06233102184128758)
- opportunity: False (0.17272931343085285)

The culprit is Dan.
In fact, it is Carole.
## 5minutemystery-the-straw-hat-theater-mysteriesbox-office-nightmare
Basil Carmody is guilty: True or False?
True (0.9822537304185777)
Basil Carmody has mean: True or False?
True (0.9687380774673213)
Basil Carmody has motive: True or False?
True (0.990550875800996)
Basil Carmody has opportunity: True or False?
True (0.9768465751854355)
John Franklin is guilty: True or False?
True (0.9831822505619944)
John Franklin has mean: True or False?
True (0.9718859797630299)
John Franklin has motive: True or False?
True (0.9903663396202808)
John Franklin has opportunity: True or False?
True (0.970126867648015)
Lawrence Blake is guilty: True or False?
True (0.9693822259947317)
Lawrence Blake has mean: True or False?
True (0.9331876642092066)
Lawrence Blake has motive: True or False?
True (0.9897513984446356)
Lawrence Blake has opportunity: True or False?
True (0.9537942396657707)
Martha Gilmont is guilty: True or False?
True (0.9686788908454032)
Martha Gilmont has mean: True or False?
True (0.9671630869492336)
Martha Gilmont has motive: True or False?
True (0.9879926447379697)
Martha Gilmont has opportunity: True or False?
True (0.9746286873974596)
### Basil Carmody
- mean: True (0.9687380774673213)
- motive: True (0.990550875800996)
- opportunity: True (0.9768465751854355)

### John Franklin
- mean: False (0.028114020236970072)
- motive: False (0.009633660379719244)
- opportunity: False (0.029873132351984966)

### Lawrence Blake
- mean: False (0.06681233579079338)
- motive: False (0.010248601555364445)
- opportunity: False (0.046205760334229296)

### Martha Gilmont
- mean: False (0.032836913050766414)
Map:  72%|███████▏  | 146/203 [2:41:46<51:26, 54.14s/ examples]Map:  72%|███████▏  | 147/203 [2:42:55<54:39, 58.56s/ examples]Map:  73%|███████▎  | 148/203 [2:43:48<52:01, 56.76s/ examples]Map:  73%|███████▎  | 149/203 [2:44:39<49:38, 55.15s/ examples]Map:  74%|███████▍  | 150/203 [2:45:21<45:14, 51.22s/ examples]- motive: False (0.01200735526203034)
- opportunity: False (0.02537131260254044)

The culprit is Basil Carmody.
In fact, it is John Franklin.
## 5minutemystery-the-waffle-man-mystery
Larry is guilty: True or False?
True (0.9538802513450514)
Larry has mean: True or False?
True (0.9103862053899627)
Larry has motive: True or False?
True (0.9638480560973683)
Larry has opportunity: True or False?
True (0.9291837815043049)
The Old Man is guilty: True or False?
True (0.9469901928615181)
The Old Man has mean: True or False?
True (0.9309620852900756)
The Old Man has motive: True or False?
True (0.9799189575826882)
The Old Man has opportunity: True or False?
True (0.9567151656221777)
The Waffle Man is guilty: True or False?
True (0.9361683754137716)
The Waffle Man has mean: True or False?
True (0.9097467681279717)
The Waffle Man has motive: True or False?
True (0.9722307324426623)
The Waffle Man has opportunity: True or False?
True (0.9523087127556139)
Vera is guilty: True or False?
True (0.9649873987772907)
Vera has mean: True or False?
True (0.8774768149941248)
Vera has motive: True or False?
True (0.9779255993272387)
Vera has opportunity: True or False?
True (0.9566342225308191)
### Larry
- mean: False (0.08961379461003727)
- motive: False (0.036151943902631656)
- opportunity: False (0.07081621849569508)

### The Old Man
- mean: True (0.9309620852900756)
- motive: True (0.9799189575826882)
- opportunity: True (0.9567151656221777)

### The Waffle Man
- mean: False (0.09025323187202827)
- motive: False (0.027769267557337662)
- opportunity: False (0.047691287244386094)

### Vera
- mean: False (0.12252318500587522)
- motive: False (0.02207440067276134)
- opportunity: False (0.04336577746918091)

The culprit is The Old Man.
In fact, it is Vera.
## 5minutemystery-the-sunday-school-tithe-mystery
Doc Bentson is guilty: True or False?
True (0.950777887812089)
Doc Bentson has mean: True or False?
True (0.8402589628813668)
Doc Bentson has motive: True or False?
True (0.9716178782667568)
Doc Bentson has opportunity: True or False?
True (0.9324533354081785)
Ellie Wilson is guilty: True or False?
True (0.9541373270174538)
Ellie Wilson has mean: True or False?
True (0.8344069148356309)
Ellie Wilson has motive: True or False?
True (0.9742884034320242)
Ellie Wilson has opportunity: True or False?
True (0.927099763868178)
James Gant is guilty: True or False?
True (0.9515039936355008)
James Gant has mean: True or False?
True (0.8221890958162477)
James Gant has motive: True or False?
True (0.982287646116634)
James Gant has opportunity: True or False?
True (0.9082930095862076)
Judy Gant is guilty: True or False?
True (0.9369805475192257)
Judy Gant has mean: True or False?
True (0.6662796746479285)
Judy Gant has motive: True or False?
True (0.9586927300380139)
Judy Gant has opportunity: True or False?
True (0.9543079730970608)
Waylon Marsh is guilty: True or False?
True (0.966851473631521)
Waylon Marsh has mean: True or False?
True (0.9012274173198201)
Waylon Marsh has motive: True or False?
True (0.9863368269753094)
Waylon Marsh has opportunity: True or False?
True (0.952397347230678)
### Doc Bentson
- mean: False (0.1597410371186332)
- motive: False (0.02838212173324317)
- opportunity: False (0.06754666459182146)

### Ellie Wilson
- mean: False (0.1655930851643691)
- motive: False (0.025711596567975836)
- opportunity: False (0.07290023613182195)

### James Gant
- mean: False (0.17781090418375234)
- motive: False (0.017712353883366005)
- opportunity: False (0.09170699041379238)

### Judy Gant
- mean: False (0.3337203253520715)
- motive: False (0.04130726996198608)
- opportunity: False (0.045692026902939165)

### Waylon Marsh
- mean: True (0.9012274173198201)
- motive: True (0.9863368269753094)
- opportunity: True (0.952397347230678)

The culprit is Waylon Marsh.
In fact, it is Waylon Marsh.
## 5minutemystery-the-straw-hat-theater-mysteriescasting-call
Alice Cartwright is guilty: True or False?
True (0.9427180278987515)
Alice Cartwright has mean: True or False?
True (0.8037905715242155)
Alice Cartwright has motive: True or False?
True (0.941654147692963)
Alice Cartwright has opportunity: True or False?
True (0.7911763836133219)
Arthur Glendon is guilty: True or False?
True (0.9509603391767795)
Arthur Glendon has mean: True or False?
True (0.8940516749601143)
Arthur Glendon has motive: True or False?
True (0.9553191057869168)
Arthur Glendon has opportunity: True or False?
True (0.8428631416381634)
Janice Starling is guilty: True or False?
True (0.9382373082603129)
Janice Starling has mean: True or False?
True (0.9032942081209032)
Janice Starling has motive: True or False?
True (0.9618217364339323)
Janice Starling has opportunity: True or False?
True (0.776622945813876)
Sandra Buckingham is guilty: True or False?
True (0.9693242313725606)
Sandra Buckingham has mean: True or False?
True (0.866132552869269)
Sandra Buckingham has motive: True or False?
True (0.9548162813994148)
Sandra Buckingham has opportunity: True or False?
True (0.8140527631337082)
### Alice Cartwright
- mean: False (0.1962094284757845)
- motive: False (0.05834585230703704)
- opportunity: False (0.20882361638667812)

### Arthur Glendon
- mean: True (0.8940516749601143)
- motive: True (0.9553191057869168)
- opportunity: True (0.8428631416381634)

### Janice Starling
- mean: False (0.09670579187909678)
- motive: False (0.03817826356606768)
- opportunity: False (0.22337705418612397)

### Sandra Buckingham
- mean: False (0.13386744713073095)
- motive: False (0.04518371860058523)
- opportunity: False (0.18594723686629178)

The culprit is Arthur Glendon.
In fact, it is Arthur Glendon.
## 5minutemystery-the-anonymous-bank-robber
Edward Cantrell is guilty: True or False?
True (0.9886682030396517)
Edward Cantrell has mean: True or False?
True (0.9520419225082909)
Edward Cantrell has motive: True or False?
True (0.9939613341638746)
Edward Cantrell has opportunity: True or False?
True (0.9811668987645739)
Larry Brooks is guilty: True or False?
True (0.9690910565174785)
Larry Brooks has mean: True or False?
True (0.8181563669811865)
Larry Brooks has motive: True or False?
True (0.9872034791669495)
Larry Brooks has opportunity: True or False?
True (0.9715639953911919)
Lester Barton is guilty: True or False?
True (0.9908919928962941)
Lester Barton has mean: True or False?
True (0.9603611244019274)
Lester Barton has motive: True or False?
True (0.9967428446694364)
Lester Barton has opportunity: True or False?
True (0.9799765346854967)
Oscar Jordan is guilty: True or False?
True (0.9853561522937149)
Oscar Jordan has mean: True or False?
True (0.8980534699860239)
Oscar Jordan has motive: True or False?
True (0.9949199557758223)
Oscar Jordan has opportunity: True or False?
True (0.9826908710080852)
### Edward Cantrell
- mean: False (0.047958077491709106)
- motive: False (0.006038665836125445)
- opportunity: False (0.018833101235426142)

### Larry Brooks
- mean: False (0.18184363301881346)
- motive: False (0.012796520833050495)
- opportunity: False (0.02843600460880813)

### Lester Barton
- mean: True (0.9603611244019274)
- motive: True (0.9967428446694364)
- opportunity: True (0.9799765346854967)

### Oscar Jordan
- mean: False (0.10194653001397613)
- motive: False (0.005080044224177738)
- opportunity: False (0.017309128991914835)

The culprit is Lester Barton.
In fact, it is Lester Barton.
## 5minutemystery-the-house-of-lies
Debra is guilty: True or False?
True (0.9463988549853353)
Debra has mean: True or False?
True (0.948058427656158)
Debra has motive: True or False?
True (0.9644556034131689)
Debra has opportunity: True or False?
True (0.8929365260632085)
Luke is guilty: True or False?
True (0.935228290192913)
Luke has mean: True or False?
True (0.7772998201448375)
Luke has motive: True or False?
True (0.9681411371390284)
Luke has opportunity: True or False?
True (0.9181872635464632)
Olivia is guilty: True or False?
True (0.9362850185952675)
Olivia has mean: True or False?
True (0.884837803442546)
Olivia has motive: True or False?
True (0.9683812262581977)
Olivia has opportunity: True or False?
True (0.936749461409047)
The Butler is guilty: True or False?
True (0.9744347924514057)
Map:  74%|███████▍  | 151/203 [2:46:18<45:45, 52.80s/ examples]Map:  75%|███████▍  | 152/203 [2:47:19<46:58, 55.27s/ examples]Map:  75%|███████▌  | 153/203 [2:48:03<43:20, 52.01s/ examples]Map:  76%|███████▌  | 154/203 [2:48:53<42:01, 51.46s/ examples]Map:  76%|███████▋  | 155/203 [2:49:36<39:11, 49.00s/ examples]The Butler has mean: True or False?
True (0.9390248639367113)
The Butler has motive: True or False?
True (0.9746769070949022)
The Butler has opportunity: True or False?
True (0.9509603994010378)
### Debra
- mean: False (0.051941572343842)
- motive: False (0.03554439658683106)
- opportunity: False (0.1070634739367915)

### Luke
- mean: False (0.22270017985516255)
- motive: False (0.031858862860971615)
- opportunity: False (0.08181273645353682)

### Olivia
- mean: False (0.11516219655745397)
- motive: False (0.03161877374180233)
- opportunity: False (0.06325053859095298)

### The Butler
- mean: True (0.9390248639367113)
- motive: True (0.9746769070949022)
- opportunity: True (0.9509603994010378)

The culprit is The Butler.
In fact, it is The Butler.
## 5minutemystery-the-straw-hat-theater-mysterieson-stage
Grace Upshaw is guilty: True or False?
True (0.9463988549853353)
Grace Upshaw has mean: True or False?
True (0.8991214023999228)
Grace Upshaw has motive: True or False?
True (0.9791157846694846)
Grace Upshaw has opportunity: True or False?
True (0.942081869103903)
Linda Grant is guilty: True or False?
True (0.9365176577773374)
Linda Grant has mean: True or False?
True (0.8957052808276003)
Linda Grant has motive: True or False?
True (0.9802052373824002)
Linda Grant has opportunity: True or False?
True (0.9376689222692878)
Molly Trumbull is guilty: True or False?
True (0.9358173616900589)
Molly Trumbull has mean: True or False?
True (0.811078188867804)
Molly Trumbull has motive: True or False?
True (0.9615337835163564)
Molly Trumbull has opportunity: True or False?
True (0.9273632783787477)
Samantha Powers is guilty: True or False?
True (0.9433475737015985)
Samantha Powers has mean: True or False?
True (0.9181873182746905)
Samantha Powers has motive: True or False?
True (0.9819446807697475)
Samantha Powers has opportunity: True or False?
True (0.9574372776306425)
### Grace Upshaw
- mean: False (0.10087859760007722)
- motive: False (0.020884215330515432)
- opportunity: False (0.057918130896096987)

### Linda Grant
- mean: False (0.10429471917239974)
- motive: False (0.019794762617599826)
- opportunity: False (0.062331077730712225)

### Molly Trumbull
- mean: False (0.18892181113219597)
- motive: False (0.03846621648364357)
- opportunity: False (0.07263672162125234)

### Samantha Powers
- mean: True (0.9181873182746905)
- motive: True (0.9819446807697475)
- opportunity: True (0.9574372776306425)

The culprit is Samantha Powers.
In fact, it is Grace Upshaw.
## 5minutemystery-canada-day
Little black-haired girl is guilty: True or False?
True (0.9522199623739209)
Little black-haired girl has mean: True or False?
True (0.9653158197836269)
Little black-haired girl has motive: True or False?
True (0.9688561547723137)
Little black-haired girl has opportunity: True or False?
True (0.9051547640395294)
Redheaded woman is guilty: True or False?
True (0.9521309719757854)
Redheaded woman has mean: True or False?
True (0.9612438076473231)
Redheaded woman has motive: True or False?
True (0.9583042252239092)
Redheaded woman has opportunity: True or False?
True (0.8444089912414552)
Stocky blonde man is guilty: True or False?
True (0.9546474221708894)
Stocky blonde man has mean: True or False?
True (0.9302051049548884)
Stocky blonde man has motive: True or False?
True (0.9430336353172679)
Stocky blonde man has opportunity: True or False?
True (0.8947894610946939)
Tall bald man is guilty: True or False?
True (0.9178934131644976)
Tall bald man has mean: True or False?
True (0.8862236142219189)
Tall bald man has motive: True or False?
True (0.9300782079786175)
Tall bald man has opportunity: True or False?
True (0.7962924261546153)
### Little black-haired girl
- mean: True (0.9653158197836269)
- motive: True (0.9688561547723137)
- opportunity: True (0.9051547640395294)

### Redheaded woman
- mean: False (0.03875619235267691)
- motive: False (0.041695774776090766)
- opportunity: False (0.1555910087585448)

### Stocky blonde man
- mean: False (0.0697948950451116)
- motive: False (0.056966364682732085)
- opportunity: False (0.10521053890530607)

### Tall bald man
- mean: False (0.11377638577808113)
- motive: False (0.06992179202138249)
- opportunity: False (0.20370757384538474)

The culprit is Little black-haired girl.
In fact, it is Tall bald man.
## 5minutemystery-the-missing-communion-set
Allison Jordan is guilty: True or False?
True (0.854884620116169)
Allison Jordan has mean: True or False?
True (0.6723316913929156)
Allison Jordan has motive: True or False?
True (0.9196425651151865)
Allison Jordan has opportunity: True or False?
True (0.7498206607358464)
Heather Guse is guilty: True or False?
True (0.9119669214647611)
Heather Guse has mean: True or False?
True (0.7931058945535956)
Heather Guse has motive: True or False?
True (0.9616780268435321)
Heather Guse has opportunity: True or False?
True (0.8255897087847518)
Janelle Herbst is guilty: True or False?
True (0.8901032777981455)
Janelle Herbst has mean: True or False?
True (0.8216173055802608)
Janelle Herbst has motive: True or False?
True (0.9702399365512847)
Janelle Herbst has opportunity: True or False?
True (0.875361437979977)
Josh Darvin is guilty: True or False?
True (0.9309620852900756)
Josh Darvin has mean: True or False?
True (0.9105454073245608)
Josh Darvin has motive: True or False?
True (0.9833749535726279)
Josh Darvin has opportunity: True or False?
True (0.9516839395409852)
Justin Paul is guilty: True or False?
True (0.9543930284832085)
Justin Paul has mean: True or False?
True (0.9056565771882901)
Justin Paul has motive: True or False?
True (0.9907140133328187)
Justin Paul has opportunity: True or False?
True (0.9443823686645129)
### Allison Jordan
- mean: False (0.3276683086070844)
- motive: False (0.0803574348848135)
- opportunity: False (0.2501793392641536)

### Heather Guse
- mean: False (0.2068941054464044)
- motive: False (0.0383219731564679)
- opportunity: False (0.1744102912152482)

### Janelle Herbst
- mean: False (0.1783826944197392)
- motive: False (0.02976006344871529)
- opportunity: False (0.12463856202002299)

### Josh Darvin
- mean: True (0.9105454073245608)
- motive: True (0.9833749535726279)
- opportunity: True (0.9516839395409852)

### Justin Paul
- mean: False (0.09434342281170993)
- motive: False (0.009285986667181279)
- opportunity: False (0.05561763133548714)

The culprit is Josh Darvin.
In fact, it is Josh Darvin.
## 5minutemystery-who-stole-super-bowl-sunday
Aunt Mary is guilty: True or False?
True (0.9695556166618308)
Aunt Mary has mean: True or False?
True (0.9012274173198201)
Aunt Mary has motive: True or False?
True (0.966726063403815)
Aunt Mary has opportunity: True or False?
True (0.9365175949789369)
Phil is guilty: True or False?
True (0.9856353404294369)
Phil has mean: True or False?
True (0.9576754579340193)
Phil has motive: True or False?
True (0.9922594430312686)
Phil has opportunity: True or False?
True (0.9843363767844491)
Rick is guilty: True or False?
True (0.9701269272790862)
Rick has mean: True or False?
True (0.8413047772878592)
Rick has motive: True or False?
True (0.9777987599607383)
Rick has opportunity: True or False?
True (0.9562272444658398)
Uncle Charlie is guilty: True or False?
True (0.9217811254507657)
Uncle Charlie has mean: True or False?
True (0.9391365661970741)
Uncle Charlie has motive: True or False?
True (0.9843062166752533)
Uncle Charlie has opportunity: True or False?
True (0.9578334701149885)
### Aunt Mary
- mean: False (0.09877258268017985)
- motive: False (0.03327393659618505)
- opportunity: False (0.06348240502106306)

### Phil
- mean: True (0.9576754579340193)
- motive: True (0.9922594430312686)
- opportunity: True (0.9843363767844491)

### Rick
- mean: False (0.15869522271214076)
- motive: False (0.022201240039261716)
- opportunity: False (0.04377275553416016)

### Uncle Charlie
- mean: False (0.060863433802925915)
- motive: False (0.01569378332474669)
- opportunity: False (0.04216652988501146)

The culprit is Phil.
In fact, it is Aunt Mary.
## 5minutemystery-the-cocktail-conundrum
Ian Fairbank is guilty: True or False?
True (0.942612469657282)
Ian Fairbank has mean: True or False?
True (0.7225270177274575)
Map:  77%|███████▋  | 156/203 [2:50:18<36:40, 46.81s/ examples]Map:  77%|███████▋  | 157/203 [2:51:04<35:41, 46.56s/ examples]Map:  78%|███████▊  | 158/203 [2:52:01<37:15, 49.69s/ examples]Map:  78%|███████▊  | 159/203 [2:52:56<37:33, 51.23s/ examples]Map:  79%|███████▉  | 160/203 [2:53:23<31:28, 43.92s/ examples]Ian Fairbank has motive: True or False?
True (0.9747731684499236)
Ian Fairbank has opportunity: True or False?
True (0.8732148436000907)
Mr. Fairbank is guilty: True or False?
True (0.8638516611889259)
Mr. Fairbank has mean: True or False?
True (0.7439129430200341)
Mr. Fairbank has motive: True or False?
True (0.9796870954125814)
Mr. Fairbank has opportunity: True or False?
True (0.8019358443954961)
Mr. Lewis Rhys is guilty: True or False?
True (0.8927496657814362)
Mr. Lewis Rhys has mean: True or False?
True (0.7033457082786769)
Mr. Lewis Rhys has motive: True or False?
True (0.9458013187522837)
Mr. Lewis Rhys has opportunity: True or False?
True (0.7512834059294674)
Mrs. Fairbank is guilty: True or False?
True (0.9076401582775206)
Mrs. Fairbank has mean: True or False?
True (0.8365545874520802)
Mrs. Fairbank has motive: True or False?
True (0.9660279734605501)
Mrs. Fairbank has opportunity: True or False?
True (0.9606574760904091)
### Ian Fairbank
- mean: False (0.27747298227254247)
- motive: False (0.025226831550076434)
- opportunity: False (0.12678515639990928)

### Mr. Fairbank
- mean: False (0.2560870569799659)
- motive: False (0.020312904587418634)
- opportunity: False (0.19806415560450386)

### Mr. Lewis Rhys
- mean: False (0.29665429172132307)
- motive: False (0.05419868124771632)
- opportunity: False (0.2487165940705326)

### Mrs. Fairbank
- mean: True (0.8365545874520802)
- motive: True (0.9660279734605501)
- opportunity: True (0.9606574760904091)

The culprit is Mrs. Fairbank.
In fact, it is Mrs. Fairbank.
## 5minutemystery-the-gypsys-secret-numbers
Great Marchelli is guilty: True or False?
True (0.873646620599733)
Great Marchelli has mean: True or False?
True (0.9026095892260383)
Great Marchelli has motive: True or False?
True (0.9680808798281443)
Great Marchelli has opportunity: True or False?
True (0.8489722037469682)
Lorenzo is guilty: True or False?
True (0.8370879250561812)
Lorenzo has mean: True or False?
True (0.8887587777822111)
Lorenzo has motive: True or False?
True (0.9431384220853135)
Lorenzo has opportunity: True or False?
True (0.7662936378892937)
Ringmaster is guilty: True or False?
True (0.9309620852900756)
Ringmaster has mean: True or False?
True (0.8582439976623328)
Ringmaster has motive: True or False?
True (0.9687380774673213)
Ringmaster has opportunity: True or False?
True (0.8998277786460391)
Sheriff is guilty: True or False?
True (0.8633916342942395)
Sheriff has mean: True or False?
True (0.7872777601997338)
Sheriff has motive: True or False?
True (0.9001793304600783)
Sheriff has opportunity: True or False?
True (0.6513548405484016)
### Great Marchelli
- mean: False (0.09739041077396171)
- motive: False (0.03191912017185572)
- opportunity: False (0.15102779625303175)

### Lorenzo
- mean: False (0.11124122221778887)
- motive: False (0.05686157791468649)
- opportunity: False (0.23370636211070628)

### Ringmaster
- mean: True (0.8582439976623328)
- motive: True (0.9687380774673213)
- opportunity: True (0.8998277786460391)

### Sheriff
- mean: False (0.21272223980026617)
- motive: False (0.09982066953992175)
- opportunity: False (0.34864515945159835)

The culprit is Ringmaster.
In fact, it is Sheriff.
## 5minutemystery-its-gone
Abe is guilty: True or False?
True (0.9854404929374018)
Abe has mean: True or False?
True (0.9495758995187151)
Abe has motive: True or False?
True (0.9845754507999278)
Abe has opportunity: True or False?
True (0.9771538382869732)
Lance is guilty: True or False?
True (0.9848983286494055)
Lance has mean: True or False?
True (0.878314250659373)
Lance has motive: True or False?
True (0.9818404909998607)
Lance has opportunity: True or False?
True (0.9362850185952675)
The Amazing Andrew is guilty: True or False?
True (0.9832788702399727)
The Amazing Andrew has mean: True or False?
True (0.8957052808276003)
The Amazing Andrew has motive: True or False?
True (0.9903196098332093)
The Amazing Andrew has opportunity: True or False?
True (0.9784259207825959)
Zora the Magnificent is guilty: True or False?
True (0.9857180718083847)
Zora the Magnificent has mean: True or False?
True (0.9489172681310486)
Zora the Magnificent has motive: True or False?
True (0.9841850996844234)
Zora the Magnificent has opportunity: True or False?
True (0.9622497571173928)
### Abe
- mean: True (0.9495758995187151)
- motive: True (0.9845754507999278)
- opportunity: True (0.9771538382869732)

### Lance
- mean: False (0.12168574934062704)
- motive: False (0.018159509000139296)
- opportunity: False (0.06371498140473253)

### The Amazing Andrew
- mean: False (0.10429471917239974)
- motive: False (0.009680390166790676)
- opportunity: False (0.021574079217404063)

### Zora the Magnificent
- mean: False (0.0510827318689514)
- motive: False (0.01581490031557664)
- opportunity: False (0.0377502428826072)

The culprit is Abe.
In fact, it is The Amazing Andrew.
## 5minutemystery-the-misers-hoard
Bob Parsons is guilty: True or False?
True (0.909666538803496)
Bob Parsons has mean: True or False?
True (0.7704647687904915)
Bob Parsons has motive: True or False?
True (0.9690910565174785)
Bob Parsons has opportunity: True or False?
True (0.9173026114435064)
John Entwhistle III is guilty: True or False?
True (0.9670387494740702)
John Entwhistle III has mean: True or False?
True (0.9001793304600783)
John Entwhistle III has motive: True or False?
True (0.9692661174528692)
John Entwhistle III has opportunity: True or False?
True (0.9463988549853353)
Sam Greenway is guilty: True or False?
True (0.9187722824991111)
Sam Greenway has mean: True or False?
True (0.9100670238942131)
Sam Greenway has motive: True or False?
True (0.9783433085003262)
Sam Greenway has opportunity: True or False?
True (0.8899121304559661)
Sarah Parsons is guilty: True or False?
True (0.9065704359329319)
Sarah Parsons has mean: True or False?
True (0.7898827135821628)
Sarah Parsons has motive: True or False?
True (0.963368656065788)
Sarah Parsons has opportunity: True or False?
True (0.7585105966624085)
### Bob Parsons
- mean: False (0.22953523120950847)
- motive: False (0.03090894348252149)
- opportunity: False (0.08269738855649356)

### John Entwhistle III
- mean: True (0.9001793304600783)
- motive: True (0.9692661174528692)
- opportunity: True (0.9463988549853353)

### Sam Greenway
- mean: False (0.08993297610578688)
- motive: False (0.021656691499673753)
- opportunity: False (0.11008786954403393)

### Sarah Parsons
- mean: False (0.21011728641783722)
- motive: False (0.03663134393421197)
- opportunity: False (0.2414894033375915)

The culprit is John Entwhistle III.
In fact, it is Sarah Parsons.
## 5minutemystery-the-cornfield-caper
Austin is guilty: True or False?
True (0.9632304925109479)
Austin has mean: True or False?
True (0.8128672807499561)
Austin has motive: True or False?
True (0.9579909444975866)
Austin has opportunity: True or False?
True (0.9498557456415421)
Billy is guilty: True or False?
True (0.9689738169140454)
Billy has mean: True or False?
True (0.7401742969616896)
Billy has motive: True or False?
True (0.9295683483415352)
Billy has opportunity: True or False?
True (0.9001793304600783)
Nick is guilty: True or False?
True (0.972727357600667)
Nick has mean: True or False?
True (0.8469578650997759)
Nick has motive: True or False?
True (0.9515489937596097)
Nick has opportunity: True or False?
True (0.9569571019757698)
### Austin
- mean: False (0.18713271925004393)
- motive: False (0.042009055502413406)
- opportunity: False (0.05014425435845793)

### Billy
- mean: False (0.25982570303831043)
- motive: False (0.07043165165846477)
- opportunity: False (0.09982066953992175)

### Nick
- mean: True (0.8469578650997759)
- motive: True (0.9515489937596097)
- opportunity: True (0.9569571019757698)

The culprit is Nick.
In fact, it is Billy.
## 5minutemystery-a-stolen-future
Donna Blake is guilty: True or False?
True (0.9447913165152162)
Donna Blake has mean: True or False?
True (0.9437636745681832)
Donna Blake has motive: True or False?
True (0.9797452684142095)
Donna Blake has opportunity: True or False?
True (0.9289263523387795)
George Wilson is guilty: True or False?
True (0.9468920823984345)
George Wilson has mean: True or False?
True (0.9145963197706802)Map:  79%|███████▉  | 161/203 [2:54:11<31:38, 45.20s/ examples]Map:  80%|███████▉  | 162/203 [2:55:21<36:01, 52.71s/ examples]Map:  80%|████████  | 163/203 [2:56:26<37:30, 56.27s/ examples]Map:  81%|████████  | 164/203 [2:57:19<35:54, 55.25s/ examples]
George Wilson has motive: True or False?
True (0.9829546804969759)
George Wilson has opportunity: True or False?
True (0.9408984770280414)
Jeffery Sharp is guilty: True or False?
True (0.9402434229803527)
Jeffery Sharp has mean: True or False?
True (0.9509603994010378)
Jeffery Sharp has motive: True or False?
True (0.9930961729703996)
Jeffery Sharp has opportunity: True or False?
True (0.9791157846694846)
Pete Thompson is guilty: True or False?
True (0.9001793304600783)
Pete Thompson has mean: True or False?
True (0.7994422859301654)
Pete Thompson has motive: True or False?
True (0.9629527935182168)
Pete Thompson has opportunity: True or False?
True (0.9390248079664695)
### Donna Blake
- mean: False (0.05623632543181678)
- motive: False (0.020254731585790497)
- opportunity: False (0.07107364766122048)

### George Wilson
- mean: False (0.08540368022931977)
- motive: False (0.017045319503024126)
- opportunity: False (0.05910152297195859)

### Jeffery Sharp
- mean: True (0.9509603994010378)
- motive: True (0.9930961729703996)
- opportunity: True (0.9791157846694846)

### Pete Thompson
- mean: False (0.20055771406983458)
- motive: False (0.03704720648178317)
- opportunity: False (0.06097519203353052)

The culprit is Jeffery Sharp.
In fact, it is Jeffery Sharp.
## 5minutemystery-the-dirty-half-dozen
Bethany Knight is guilty: True or False?
True (0.9498556854872413)
Bethany Knight has mean: True or False?
True (0.8050197341926492)
Bethany Knight has motive: True or False?
True (0.9611709710713023)
Bethany Knight has opportunity: True or False?
True (0.8140527631337082)
Joe Clark is guilty: True or False?
True (0.9418683665706381)
Joe Clark has mean: True or False?
True (0.8776866744811284)
Joe Clark has motive: True or False?
True (0.9626028535101038)
Joe Clark has opportunity: True or False?
True (0.8344069148356309)
Sherry Fogle is guilty: True or False?
True (0.9422946582938823)
Sherry Fogle has mean: True or False?
True (0.8661325012437474)
Sherry Fogle has motive: True or False?
True (0.9742394680162697)
Sherry Fogle has opportunity: True or False?
True (0.814643384779728)
Tonya Muse is guilty: True or False?
True (1.7651923355465458)
Tonya Muse has mean: True or False?
True (0.5888891269161294)
Tonya Muse has motive: True or False?
True (0.9537943000694998)
Tonya Muse has opportunity: True or False?
True (0.6288633913849659)
Wayne Clark is guilty: True or False?
True (0.957037509078236)
Wayne Clark has mean: True or False?
True (0.8987665204865408)
Wayne Clark has motive: True or False?
True (0.9653158197836269)
Wayne Clark has opportunity: True or False?
True (0.8376199551237796)
### Bethany Knight
- mean: False (0.19498026580735084)
- motive: False (0.03882902892869766)
- opportunity: False (0.18594723686629178)

### Joe Clark
- mean: False (0.12231332551887164)
- motive: False (0.03739714648989623)
- opportunity: False (0.1655930851643691)

### Sherry Fogle
- mean: False (0.1338674987562526)
- motive: False (0.025760531983730295)
- opportunity: False (0.18535661522027203)

### Tonya Muse
- mean: False (0.4111108730838706)
- motive: False (0.046205699930500166)
- opportunity: False (0.37113660861503406)

### Wayne Clark
- mean: True (0.8987665204865408)
- motive: True (0.9653158197836269)
- opportunity: True (0.8376199551237796)

The culprit is Wayne Clark.
In fact, it is Wayne Clark.
## 5minutemystery-a-porsche-of-course
Amy Golden is guilty: True or False?
True (0.9837225082161594)
Amy Golden has mean: True or False?
True (0.9585376970077499)
Amy Golden has motive: True or False?
True (0.9902161360821735)
Amy Golden has opportunity: True or False?
True (0.9814889431064477)
Frankie Cole is guilty: True or False?
True (0.9785492416845885)
Frankie Cole has mean: True or False?
True (0.9302050495103452)
Frankie Cole has motive: True or False?
True (0.9839708801996613)
Frankie Cole has opportunity: True or False?
True (0.9750122434684597)
Jeremy Steele is guilty: True or False?
True (0.9716178782667568)
Jeremy Steele has mean: True or False?
True (0.9260365949489886)
Jeremy Steele has motive: True or False?
True (0.9764007329815675)
Jeremy Steele has opportunity: True or False?
True (0.9671630869492336)
Lionel Jacobs is guilty: True or False?
True (0.9789554468203624)
Lionel Jacobs has mean: True or False?
True (0.94620036983)
Lionel Jacobs has motive: True or False?
True (0.9774139529645163)
Lionel Jacobs has opportunity: True or False?
True (0.9678385865075065)
Susan Barker is guilty: True or False?
True (0.976580083009196)
Susan Barker has mean: True or False?
True (0.9294403817764149)
Susan Barker has motive: True or False?
True (0.9712384344135814)
Susan Barker has opportunity: True or False?
True (0.9515039936355008)
### Amy Golden
- mean: True (0.9585376970077499)
- motive: True (0.9902161360821735)
- opportunity: True (0.9814889431064477)

### Frankie Cole
- mean: False (0.06979495048965478)
- motive: False (0.01602911980033872)
- opportunity: False (0.024987756531540284)

### Jeremy Steele
- mean: False (0.0739634050510114)
- motive: False (0.023599267018432513)
- opportunity: False (0.032836913050766414)

### Lionel Jacobs
- mean: False (0.05379963017)
- motive: False (0.022586047035483725)
- opportunity: False (0.03216141349249346)

### Susan Barker
- mean: False (0.07055961822358514)
- motive: False (0.028761565586418625)
- opportunity: False (0.048496006364499245)

The culprit is Amy Golden.
In fact, it is Frankie Cole.
## 5minutemystery-the-mystery-of-the-missing-story
Alex Rebmevon is guilty: True or False?
True (0.91789335161495)
Alex Rebmevon has mean: True or False?
True (0.7041601500399041)
Alex Rebmevon has motive: True or False?
True (0.958226146208407)
Alex Rebmevon has opportunity: True or False?
True (0.8013146490010521)
Amy is guilty: True or False?
True (0.8640812064457842)
Amy has mean: True or False?
True (0.8433797899747144)
Amy has motive: True or False?
True (0.9705764057188281)
Amy has opportunity: True or False?
True (0.8413047772878592)
Lucy is guilty: True or False?
True (0.7779753136455794)
Lucy has mean: True or False?
True (0.5907792634380938)
Lucy has motive: True or False?
True (0.9615337835163564)
Lucy has opportunity: True or False?
True (0.7264255794048772)
Sarah is guilty: True or False?
True (0.8308687759814434)
Sarah has mean: True or False?
True (0.8175745039697023)
Sarah has motive: True or False?
True (0.9662834418200392)
Sarah has opportunity: True or False?
True (0.8606036289596553)
### Alex Rebmevon
- mean: False (0.29583984996009594)
- motive: False (0.04177385379159304)
- opportunity: False (0.1986853509989479)

### Amy
- mean: True (0.8433797899747144)
- motive: True (0.9705764057188281)
- opportunity: True (0.8413047772878592)

### Lucy
- mean: False (0.40922073656190616)
- motive: False (0.03846621648364357)
- opportunity: False (0.2735744205951228)

### Sarah
- mean: False (0.18242549603029767)
- motive: False (0.033716558179960776)
- opportunity: False (0.13939637104034475)

The culprit is Amy.
In fact, it is Lucy.
## 5minutemystery-the-case-of-the-missing-friend
Billy Friend is guilty: True or False?
True (0.8354835531737983)
Billy Friend has mean: True or False?
True (0.9628131975124238)
Billy Friend has motive: True or False?
False (0.6073669806570988)
Billy Friend has opportunity: True or False?
True (0.8887587777822111)
Diana Scott is guilty: True or False?
True (0.9194980294026535)
Diana Scott has mean: True or False?
True (0.9711837766333243)
Diana Scott has motive: True or False?
True (0.9482983939002998)
Diana Scott has opportunity: True or False?
True (0.8846386054372942)
Harrell Garner is guilty: True or False?
True (0.9419752942631836)
Harrell Garner has mean: True or False?
True (0.9807288650933316)
Harrell Garner has motive: True or False?
True (0.9534053189771676)
Harrell Garner has opportunity: True or False?
True (0.943970619289785)
Susan Allen is guilty: True or False?
True (0.814643384779728)
Susan Allen has mean: True or False?
True (0.9339146597970963)
Susan Allen has motive: True or False?
False (0.72520429508428)
Susan Allen has opportunity: True or False?
True (0.7799928701983835)
### Billy Friend
- mean: False (0.03718680248757622)
Map:  81%|████████▏ | 165/203 [2:58:00<32:16, 50.97s/ examples]Map:  82%|████████▏ | 166/203 [2:58:46<30:31, 49.50s/ examples]Map:  82%|████████▏ | 167/203 [2:59:41<30:47, 51.32s/ examples]Map:  83%|████████▎ | 168/203 [3:00:30<29:23, 50.40s/ examples]- motive: False (0.6073669806570988)
- opportunity: False (0.11124122221778887)

### Diana Scott
- mean: False (0.028816223366675664)
- motive: False (0.051701606099700204)
- opportunity: False (0.11536139456270578)

### Harrell Garner
- mean: True (0.9807288650933316)
- motive: True (0.9534053189771676)
- opportunity: True (0.943970619289785)

### Susan Allen
- mean: False (0.06608534020290369)
- motive: False (0.72520429508428)
- opportunity: False (0.22000712980161652)

The culprit is Harrell Garner.
In fact, it is Diana Scott.
## 5minutemystery-sweat-it-out
Chris Henderson is guilty: True or False?
True (0.9229003224709645)
Chris Henderson has mean: True or False?
True (0.9076401582775206)
Chris Henderson has motive: True or False?
True (0.9634374994224176)
Chris Henderson has opportunity: True or False?
True (0.9473810811508532)
Dave Perkins is guilty: True or False?
True (0.8665847814067802)
Dave Perkins has mean: True or False?
True (0.8840392847025188)
Dave Perkins has motive: True or False?
True (0.9658351545108645)
Dave Perkins has opportunity: True or False?
True (0.9233161821369215)
Larry Douglas is guilty: True or False?
True (0.8919993657480679)
Larry Douglas has mean: True or False?
True (0.8587185689177256)
Larry Douglas has motive: True or False?
True (0.9738194950619852)
Larry Douglas has opportunity: True or False?
True (0.9376689222692878)
Nathan Elliott is guilty: True or False?
True (0.8906751280163339)
Nathan Elliott has mean: True or False?
True (0.9537942396657707)
Nathan Elliott has motive: True or False?
True (0.9949334859556598)
Nathan Elliott has opportunity: True or False?
True (0.9727272996216001)
### Chris Henderson
- mean: False (0.09235984172247935)
- motive: False (0.03656250057758237)
- opportunity: False (0.05261891884914682)

### Dave Perkins
- mean: False (0.1159607152974812)
- motive: False (0.034164845489135454)
- opportunity: False (0.07668381786307854)

### Larry Douglas
- mean: False (0.14128143108227442)
- motive: False (0.026180504938014826)
- opportunity: False (0.062331077730712225)

### Nathan Elliott
- mean: True (0.9537942396657707)
- motive: True (0.9949334859556598)
- opportunity: True (0.9727272996216001)

The culprit is Nathan Elliott.
In fact, it is Chris Henderson.
## 5minutemystery-mystery-of-the-missing-heart
Eric Winter is guilty: True or False?
True (0.8987665204865408)
Eric Winter has mean: True or False?
True (0.8221891570741111)
Eric Winter has motive: True or False?
True (0.9846346375905863)
Eric Winter has opportunity: True or False?
True (0.9012274173198201)
Jenny Jackson is guilty: True or False?
True (0.8568122940392877)
Jenny Jackson has mean: True or False?
True (0.6662796746479285)
Jenny Jackson has motive: True or False?
True (0.919930758847437)
Jenny Jackson has opportunity: True or False?
True (0.8338664134858856)
Jimmy Jackson is guilty: True or False?
True (0.8774767496170098)
Jimmy Jackson has mean: True or False?
True (0.791821116278941)
Jimmy Jackson has motive: True or False?
True (0.9092645024391882)
Jimmy Jackson has opportunity: True or False?
True (0.8762113474663927)
Wendy LaRue is guilty: True or False?
True (0.9307105568817887)
Wendy LaRue has mean: True or False?
True (0.6477981763584071)
Wendy LaRue has motive: True or False?
True (0.9798226352078263)
Wendy LaRue has opportunity: True or False?
True (0.8587185689177256)
### Eric Winter
- mean: True (0.8221891570741111)
- motive: True (0.9846346375905863)
- opportunity: True (0.9012274173198201)

### Jenny Jackson
- mean: False (0.3337203253520715)
- motive: False (0.08006924115256298)
- opportunity: False (0.16613358651411436)

### Jimmy Jackson
- mean: False (0.20817888372105897)
- motive: False (0.09073549756081178)
- opportunity: False (0.12378865253360727)

### Wendy LaRue
- mean: False (0.3522018236415929)
- motive: False (0.02017736479217369)
- opportunity: False (0.14128143108227442)

The culprit is Eric Winter.
In fact, it is Eric Winter.
## 5minutemystery-stealing-second-base
Coach Joe Morgan is guilty: True or False?
True (0.7931058945535956)
Coach Joe Morgan has mean: True or False?
True (0.6619228707202935)
Coach Joe Morgan has motive: True or False?
True (0.9385759849623091)
Coach Joe Morgan has opportunity: True or False?
True (0.8031737798924701)
Mary Thornton is guilty: True or False?
True (0.9029524325377104)
Mary Thornton has mean: True or False?
True (0.8086723099497763)
Mary Thornton has motive: True or False?
True (0.975059748401155)
Mary Thornton has opportunity: True or False?
True (0.9403530352223053)
Randy Newsom is guilty: True or False?
True (0.9319595674053855)
Randy Newsom has mean: True or False?
True (0.7534666630720156)
Randy Newsom has motive: True or False?
True (0.9558991201960071)
Randy Newsom has opportunity: True or False?
True (0.9314624659768579)
Shorty Gilstrap is guilty: True or False?
True (0.9336731438527403)
Shorty Gilstrap has mean: True or False?
True (0.7662936378892937)
Shorty Gilstrap has motive: True or False?
True (0.9724670646029822)
Shorty Gilstrap has opportunity: True or False?
True (0.9431384220853135)
### Coach Joe Morgan
- mean: False (0.33807712927970646)
- motive: False (0.061424015037690904)
- opportunity: False (0.19682622010752993)

### Mary Thornton
- mean: True (0.8086723099497763)
- motive: True (0.975059748401155)
- opportunity: True (0.9403530352223053)

### Randy Newsom
- mean: False (0.2465333369279844)
- motive: False (0.04410087980399291)
- opportunity: False (0.06853753402314211)

### Shorty Gilstrap
- mean: False (0.23370636211070628)
- motive: False (0.027532935397017844)
- opportunity: False (0.05686157791468649)

The culprit is Mary Thornton.
In fact, it is Mary Thornton.
## 5minutemystery-murder-in-the-old-house
Bathroom is guilty: True or False?
True (0.9666001797251225)
Bathroom has mean: True or False?
True (0.9412234437340664)
Bathroom has motive: True or False?
True (0.9835338590325645)
Bathroom has opportunity: True or False?
True (0.9481545679322319)
Bedroom of daughter, Anita Jensen is guilty: True or False?
True (1.1329194703045333)
Bedroom of daughter, Anita Jensen has mean: True or False?
True (0.8803862939824989)
Bedroom of daughter, Anita Jensen has motive: True or False?
True (0.9760835762008001)
Bedroom of daughter, Anita Jensen has opportunity: True or False?
True (0.9158089188126235)
Bedroom of oldest son, Harry Jensen is guilty: True or False?
True (0.9388008138003494)
Bedroom of oldest son, Harry Jensen has mean: True or False?
True (0.918626370973125)
Bedroom of oldest son, Harry Jensen has motive: True or False?
True (0.9751071938949272)
Bedroom of oldest son, Harry Jensen has opportunity: True or False?
True (0.9385759220258869)
Bedroom of youngest son, Edward Jensen is guilty: True or False?
True (1.2674606319009032)
Bedroom of youngest son, Edward Jensen has mean: True or False?
True (0.9320833112823845)
Bedroom of youngest son, Edward Jensen has motive: True or False?
True (0.9854404929374018)
Bedroom of youngest son, Edward Jensen has opportunity: True or False?
True (0.9603611816439128)
Master bedroom of Earl and Mildrid Jensen is guilty: True or False?
True (0.9796286813551001)
Master bedroom of Earl and Mildrid Jensen has mean: True or False?
True (0.9755768767688796)
Master bedroom of Earl and Mildrid Jensen has motive: True or False?
True (0.9848983882711804)
Master bedroom of Earl and Mildrid Jensen has opportunity: True or False?
True (0.9615338444102304)
### Bathroom
- mean: False (0.05877655626593359)
- motive: False (0.016466140967435483)
- opportunity: False (0.05184543206776815)

### Bedroom of daughter, Anita Jensen
- mean: False (0.1196137060175011)
- motive: False (0.023916423799199893)
- opportunity: False (0.0841910811873765)

### Bedroom of oldest son, Harry Jensen
- mean: False (0.08137362902687495)
- motive: False (0.02489280610507283)
- opportunity: False (0.06142407797411309)

### Bedroom of youngest son, Edward Jensen
- mean: False (0.06791668871761547)
- motive: False (0.014559507062598231)
- opportunity: False (0.03963881835608718)

### Master bedroom of Earl and Mildrid Jensen
- mean: True (0.9755768767688796)
- motive: True (0.9848983882711804)
Map:  83%|████████▎ | 169/203 [3:01:25<29:20, 51.78s/ examples]Map:  84%|████████▎ | 170/203 [3:02:12<27:47, 50.52s/ examples]Map:  84%|████████▍ | 171/203 [3:02:59<26:20, 49.40s/ examples]Map:  85%|████████▍ | 172/203 [3:03:44<24:47, 47.97s/ examples]Map:  85%|████████▌ | 173/203 [3:04:34<24:24, 48.83s/ examples]- opportunity: True (0.9615338444102304)

The culprit is Master bedroom of Earl and Mildrid Jensen.
In fact, it is Bathroom.
## 5minutemystery-the-chess-mystery
Father is guilty: True or False?
True (0.9778411387040619)
Father has mean: True or False?
True (0.9212159548464016)
Father has motive: True or False?
True (0.9590009457171959)
Father has opportunity: True or False?
True (0.7924642605907138)
Greg is guilty: True or False?
True (0.9449947479233238)
Greg has mean: True or False?
True (0.8311430212356835)
Greg has motive: True or False?
True (0.9812389020148623)
Greg has opportunity: True or False?
True (0.9222025890552223)
Tina is guilty: True or False?
True (0.9479621664653681)
Tina has mean: True or False?
True (0.8175745039697023)
Tina has motive: True or False?
True (0.9591543064115948)
Tina has opportunity: True or False?
True (0.8365545251239088)
Uncle Larry is guilty: True or False?
True (0.8820219652716884)
Uncle Larry has mean: True or False?
True (0.8092759828926619)
Uncle Larry has motive: True or False?
True (0.934155284694701)
Uncle Larry has opportunity: True or False?
True (0.7759445334082792)
### Father
- mean: False (0.07878404515359838)
- motive: False (0.04099905428280415)
- opportunity: False (0.20753573940928616)

### Greg
- mean: True (0.8311430212356835)
- motive: True (0.9812389020148623)
- opportunity: True (0.9222025890552223)

### Tina
- mean: False (0.18242549603029767)
- motive: False (0.040845693588405174)
- opportunity: False (0.16344547487609118)

### Uncle Larry
- mean: False (0.1907240171073381)
- motive: False (0.065844715305299)
- opportunity: False (0.22405546659172082)

The culprit is Greg.
In fact, it is Greg.
## 5minutemystery-lost-stolen-and-found
John Beddington is guilty: True or False?
True (0.7662936378892937)
John Beddington has mean: True or False?
True (0.8895288719962232)
John Beddington has motive: True or False?
True (0.9374402785760423)
John Beddington has opportunity: True or False?
True (0.8294920340613177)
Louisa Perry is guilty: True or False?
True (0.7697732451157533)
Louisa Perry has mean: True or False?
True (0.8973360043541736)
Louisa Perry has motive: True or False?
True (0.9492946859196381)
Louisa Perry has opportunity: True or False?
True (0.8013146490010521)
Mary Ingram is guilty: True or False?
True (0.7416740778117503)
Mary Ingram has mean: True or False?
True (0.8951566249612815)
Mary Ingram has motive: True or False?
True (0.9456006903352807)
Mary Ingram has opportunity: True or False?
True (0.8665847814067802)
Sarah Upton is guilty: True or False?
True (0.875361437979977)
Sarah Upton has mean: True or False?
True (0.9038048413863352)
Sarah Upton has motive: True or False?
True (0.9535353169313603)
Sarah Upton has opportunity: True or False?
True (0.9116528030198908)
### John Beddington
- mean: False (0.11047112800377679)
- motive: False (0.06255972142395771)
- opportunity: False (0.17050796593868234)

### Louisa Perry
- mean: False (0.1026639956458264)
- motive: False (0.05070531408036194)
- opportunity: False (0.1986853509989479)

### Mary Ingram
- mean: False (0.10484337503871854)
- motive: False (0.054399309664719286)
- opportunity: False (0.1334152185932198)

### Sarah Upton
- mean: True (0.9038048413863352)
- motive: True (0.9535353169313603)
- opportunity: True (0.9116528030198908)

The culprit is Sarah Upton.
In fact, it is Louisa Perry.
## 5minutemystery-the-chocolate-cupcake-caper
Geraldine is guilty: True or False?
True (0.9322068701708559)
Geraldine has mean: True or False?
True (0.8856315007226893)
Geraldine has motive: True or False?
True (0.9818056233287176)
Geraldine has opportunity: True or False?
True (0.9612438076473231)
Julianna is guilty: True or False?
True (0.8872045854516336)
Julianna has mean: True or False?
True (0.9015745518914653)
Julianna has motive: True or False?
True (0.9798997635332343)
Julianna has opportunity: True or False?
True (0.9591543064115948)
Luis is guilty: True or False?
True (0.9171543708147702)
Luis has mean: True or False?
True (0.8426043397677332)
Luis has motive: True or False?
True (0.9843062166752533)
Luis has opportunity: True or False?
True (0.920789721359066)
Mr. Bento is guilty: True or False?
True (0.897695304229796)
Mr. Bento has mean: True or False?
True (0.8316905440184192)
Mr. Bento has motive: True or False?
True (0.9847230314726132)
Mr. Bento has opportunity: True or False?
True (0.883638205304735)
### Geraldine
- mean: False (0.11436849927731074)
- motive: False (0.01819437667128243)
- opportunity: False (0.03875619235267691)

### Julianna
- mean: True (0.9015745518914653)
- motive: True (0.9798997635332343)
- opportunity: True (0.9591543064115948)

### Luis
- mean: False (0.1573956602322668)
- motive: False (0.01569378332474669)
- opportunity: False (0.079210278640934)

### Mr. Bento
- mean: False (0.16830945598158076)
- motive: False (0.015276968527386803)
- opportunity: False (0.11636179469526498)

The culprit is Julianna.
In fact, it is Geraldine.
## 5minutemystery-dead-mans-island
Grandpa is guilty: True or False?
True (0.8534247816107388)
Grandpa has mean: True or False?
True (0.6706082735718226)
Grandpa has motive: True or False?
True (0.9558991201960071)
Grandpa has opportunity: True or False?
True (0.8050197341926492)
Grandpa's grandfather is guilty: True or False?
True (0.7162185953247016)
Grandpa's grandfather has mean: True or False?
True (0.7041601500399041)
Grandpa's grandfather has motive: True or False?
True (0.8852351930010195)
Grandpa's grandfather has opportunity: True or False?
True (0.7017130830397807)
Lisa is guilty: True or False?
True (0.7556369876990674)
Lisa has mean: True or False?
False (0.685107355950278)
Lisa has motive: True or False?
True (0.7074046739492601)
Lisa has opportunity: True or False?
True (0.6388352560545881)
Mike is guilty: True or False?
True (0.7905302675820512)
Mike has mean: True or False?
True (0.6141625595066657)
Mike has motive: True or False?
True (0.8984105603938967)
Mike has opportunity: True or False?
True (0.8807970862580315)
### Grandpa
- mean: True (0.6706082735718226)
- motive: True (0.9558991201960071)
- opportunity: True (0.8050197341926492)

### Grandpa's grandfather
- mean: False (0.29583984996009594)
- motive: False (0.1147648069989805)
- opportunity: False (0.29828691696021925)

### Lisa
- mean: False (0.685107355950278)
- motive: False (0.2925953260507399)
- opportunity: False (0.36116474394541187)

### Mike
- mean: False (0.38583744049333435)
- motive: False (0.10158943960610334)
- opportunity: False (0.11920291374196845)

The culprit is Grandpa.
In fact, it is Lisa.
## 5minutemystery-who-stole-the-rock-of-ages
Denise Hurst is guilty: True or False?
True (0.9326989068252284)
Denise Hurst has mean: True or False?
True (0.9612438076473231)
Denise Hurst has motive: True or False?
True (0.9842759969893847)
Denise Hurst has opportunity: True or False?
True (0.9467937951644804)
Jim Gaigon is guilty: True or False?
True (0.9319595674053855)
Jim Gaigon has mean: True or False?
True (0.8227594449669557)
Jim Gaigon has motive: True or False?
True (0.9571177945772992)
Jim Gaigon has opportunity: True or False?
True (0.9433475737015985)
Juan Carde is guilty: True or False?
True (0.9026096497507297)
Juan Carde has mean: True or False?
True (0.883638205304735)
Juan Carde has motive: True or False?
True (0.9596109393754703)
Juan Carde has opportunity: True or False?
True (0.9276260107813639)
Skye Smith is guilty: True or False?
True (0.9394706502722077)
Skye Smith has mean: True or False?
True (0.9529258626138675)
Skye Smith has motive: True or False?
True (0.9815244083320255)
Skye Smith has opportunity: True or False?
True (0.9492946258008691)
### Denise Hurst
- mean: True (0.9612438076473231)
- motive: True (0.9842759969893847)
- opportunity: True (0.9467937951644804)

### Jim Gaigon
- mean: False (0.17724055503304426)
- motive: False (0.042882205422700825)
- opportunity: False (0.056652426298401504)

### Juan Carde
- mean: False (0.11636179469526498)
- motive: False (0.04038906062452974)
- opportunity: False (0.07237398921863614)

### Skye Smith
- mean: False (0.04707413738613253)
- motive: False (0.018475591667974522)
Map:  86%|████████▌ | 174/203 [3:05:23<23:35, 48.81s/ examples]Map:  86%|████████▌ | 175/203 [3:06:12<22:43, 48.68s/ examples]Map:  87%|████████▋ | 176/203 [3:06:54<21:06, 46.91s/ examples]Map:  87%|████████▋ | 177/203 [3:07:46<20:53, 48.20s/ examples]Map:  88%|████████▊ | 178/203 [3:08:43<21:15, 51.02s/ examples]Map:  88%|████████▊ | 179/203 [3:09:39<21:00, 52.52s/ examples]- opportunity: False (0.050705374199130904)

The culprit is Denise Hurst.
In fact, it is Juan Carde.
## 5minutemystery-all-washed-up
Captain Kildare is guilty: True or False?
True (0.8620035048683017)
Captain Kildare has mean: True or False?
True (0.8714748565614324)
Captain Kildare has motive: True or False?
True (0.9260365949489886)
Captain Kildare has opportunity: True or False?
True (0.8441522053247883)
Latrisha Lanigan is guilty: True or False?
True (0.9489172115711736)
Latrisha Lanigan has mean: True or False?
True (0.9007045635949587)
Latrisha Lanigan has motive: True or False?
True (0.9193534273597669)
Latrisha Lanigan has opportunity: True or False?
True (0.7956581141325956)
Mark Colson is guilty: True or False?
True (0.9339146597970963)
Mark Colson has mean: True or False?
True (0.8233283740192667)
Mark Colson has motive: True or False?
True (0.9322068701708559)
Mark Colson has opportunity: True or False?
True (0.9015745518914653)
Marvin Fishback is guilty: True or False?
True (0.9493885642537184)
Marvin Fishback has mean: True or False?
True (0.9066531077351827)
Marvin Fishback has motive: True or False?
True (0.9412234437340664)
Marvin Fishback has opportunity: True or False?
True (0.9145963197706802)
### Captain Kildare
- mean: False (0.12852514343856758)
- motive: False (0.0739634050510114)
- opportunity: False (0.1558477946752117)

### Latrisha Lanigan
- mean: False (0.09929543640504135)
- motive: False (0.08064657264023312)
- opportunity: False (0.20434188586740443)

### Mark Colson
- mean: False (0.17667162598073327)
- motive: False (0.0677931298291441)
- opportunity: False (0.09842544810853471)

### Marvin Fishback
- mean: True (0.9066531077351827)
- motive: True (0.9412234437340664)
- opportunity: True (0.9145963197706802)

The culprit is Marvin Fishback.
In fact, it is Mark Colson.
## 5minutemystery-the-hidden-messenger
Jean is guilty: True or False?
True (0.9026095892260383)
Jean has mean: True or False?
True (0.879146760693242)
Jean has motive: True or False?
True (0.972151576692602)
Jean has opportunity: True or False?
True (0.8980534699860239)
Marie is guilty: True or False?
True (0.9392480858026054)
Marie has mean: True or False?
True (0.8250265688168699)
Marie has motive: True or False?
True (0.9639839524564597)
Marie has opportunity: True or False?
True (0.8558511727823209)
Molly is guilty: True or False?
True (0.9388008138003494)
Molly has mean: True or False?
True (0.8086723702005608)
Molly has motive: True or False?
True (0.9772842528587228)
Molly has opportunity: True or False?
True (0.9489172681310486)
Smith is guilty: True or False?
True (0.9494823209990744)
Smith has mean: True or False?
True (0.8037905715242155)
Smith has motive: True or False?
True (0.9756929870688384)
Smith has opportunity: True or False?
True (0.8575297062839006)
### Jean
- mean: True (0.879146760693242)
- motive: True (0.972151576692602)
- opportunity: True (0.8980534699860239)

### Marie
- mean: False (0.17497343118313013)
- motive: False (0.036016047543540264)
- opportunity: False (0.14414882721767908)

### Molly
- mean: False (0.19132762979943918)
- motive: False (0.02271574714127722)
- opportunity: False (0.0510827318689514)

### Smith
- mean: False (0.1962094284757845)
- motive: False (0.024307012931161553)
- opportunity: False (0.14247029371609943)

The culprit is Jean.
In fact, it is Smith.
## 5minutemystery-the-disappearing-dollhouse
Julia is guilty: True or False?
True (0.8727817583545995)
Julia has mean: True or False?
False (4.693134685645497)
Julia has motive: True or False?
True (0.9626730694627891)
Julia has opportunity: True or False?
True (0.9653811448171958)
Kyle is guilty: True or False?
True (0.9603611244019274)
Kyle has mean: True or False?
True (0.9121235591541035)
Kyle has motive: True or False?
True (0.988733708717463)
Kyle has opportunity: True or False?
True (0.9830200071977605)
Lucius is guilty: True or False?
True (0.9581478236979405)
Lucius has mean: True or False?
True (0.9304582506719414)
Lucius has motive: True or False?
True (0.9686195851543489)
Lucius has opportunity: True or False?
True (0.9604354488383994)
Reg is guilty: True or False?
True (0.9207896596153058)
Reg has mean: True or False?
True (0.9273633336539081)
Reg has motive: True or False?
True (0.9744833710245325)
Reg has opportunity: True or False?
True (0.9374402785760423)
### Julia
- mean: False (4.693134685645497)
- motive: False (0.03732693053721092)
- opportunity: False (0.034618855182804165)

### Kyle
- mean: True (0.9121235591541035)
- motive: True (0.988733708717463)
- opportunity: True (0.9830200071977605)

### Lucius
- mean: False (0.06954174932805857)
- motive: False (0.03138041484565113)
- opportunity: False (0.039564551161600625)

### Reg
- mean: False (0.0726366663460919)
- motive: False (0.02551662897546747)
- opportunity: False (0.06255972142395771)

The culprit is Kyle.
In fact, it is Reg.
## 5minutemystery-a-bear-a-dog-and-a-mystery
Mom is guilty: True or False?
True (0.9164093756391206)
Mom has mean: True or False?
True (0.5774954003013352)
Mom has motive: True or False?
True (0.9478657843986744)
Mom has opportunity: True or False?
True (0.745398395394548)
Old Mugger is guilty: True or False?
True (0.8980534699860239)
Old Mugger has mean: True or False?
True (0.6206215556999736)
Old Mugger has motive: True or False?
True (0.9444848881002107)
Old Mugger has opportunity: True or False?
True (0.8601343090488404)
Orville is guilty: True or False?
True (0.9456006903352807)
Orville has mean: True or False?
True (0.7209580648179327)
Orville has motive: True or False?
True (0.96716302569886)
Orville has opportunity: True or False?
True (0.9111797236708432)
Taylor is guilty: True or False?
True (0.7676898810056793)
Taylor has mean: True or False?
False (0.5087881523495457)
Taylor has motive: True or False?
True (0.8762112821835625)
Taylor has opportunity: True or False?
True (0.5282900845448565)
### Mom
- mean: False (0.42250459969866483)
- motive: False (0.052134215601325584)
- opportunity: False (0.254601604605452)

### Old Mugger
- mean: False (0.37937844430002643)
- motive: False (0.055515111899789304)
- opportunity: False (0.13986569095115964)

### Orville
- mean: True (0.7209580648179327)
- motive: True (0.96716302569886)
- opportunity: True (0.9111797236708432)

### Taylor
- mean: False (0.5087881523495457)
- motive: False (0.12378871781643752)
- opportunity: False (0.4717099154551435)

The culprit is Orville.
In fact, it is Taylor.
## 5minutemystery-the-mystery-of-the-talented-cat
Edith is guilty: True or False?
True (0.9095862487848758)
Edith has mean: True or False?
True (0.6020616403539744)
Edith has motive: True or False?
True (0.954477967000386)
Edith has opportunity: True or False?
True (0.9241418261705818)
Joshua Sellers is guilty: True or False?
True (0.7956581141325956)
Joshua Sellers has mean: True or False?
True (0.6531269509188588)
Joshua Sellers has motive: True or False?
True (0.9456006304504523)
Joshua Sellers has opportunity: True or False?
True (0.794384956668203)
Muggles is guilty: True or False?
True (0.7859664553110391)
Muggles has mean: True or False?
True (0.7577943897558946)
Muggles has motive: True or False?
True (0.8428631416381634)
Muggles has opportunity: True or False?
True (0.8558511090164419)
Rick is guilty: True or False?
True (0.9284088027271398)
Rick has mean: True or False?
True (0.5078118910577802)
Rick has motive: True or False?
True (0.9505947844514345)
Rick has opportunity: True or False?
True (0.7379143332111532)
### Edith
- mean: True (0.6020616403539744)
- motive: True (0.954477967000386)
- opportunity: True (0.9241418261705818)

### Joshua Sellers
- mean: False (0.34687304908114125)
- motive: False (0.054399369549547716)
- opportunity: False (0.20561504333179703)

### Muggles
- mean: False (0.24220561024410536)
- motive: False (0.15713685836183655)
- opportunity: False (0.1441488909835581)

### Rick
- mean: False (0.49218810894221976)
- motive: False (0.04940521554856547)
- opportunity: False (0.2620856667888468)

The culprit is Edith.
In fact, it is Edith.
## 5minutemystery-the-haunted-portrait
Jonathan Ingersoll is guilty: True or False?
True (0.8818185327505514)
Map:  89%|████████▊ | 180/203 [3:10:41<21:15, 55.45s/ examples]Map:  89%|████████▉ | 181/203 [3:11:24<18:52, 51.47s/ examples]Map:  90%|████████▉ | 182/203 [3:12:27<19:13, 54.91s/ examples]Map:  90%|█████████ | 183/203 [3:13:31<19:13, 57.66s/ examples]Jonathan Ingersoll has mean: True or False?
True (0.8128673413132903)
Jonathan Ingersoll has motive: True or False?
True (0.8622356683135765)
Jonathan Ingersoll has opportunity: True or False?
True (0.8697145551802641)
Lucille Cameron is guilty: True or False?
True (0.9392480858026054)
Lucille Cameron has mean: True or False?
True (0.7739006258141444)
Lucille Cameron has motive: True or False?
True (0.9431384818142104)
Lucille Cameron has opportunity: True or False?
True (0.955152093302995)
Marion Montgomery is guilty: True or False?
True (0.9368650880816557)
Marion Montgomery has mean: True or False?
True (0.9518632280135741)
Marion Montgomery has motive: True or False?
True (0.9289263523387795)
Marion Montgomery has opportunity: True or False?
True (0.962813258487323)
Teddy Auchinlech is guilty: True or False?
True (3.2475815027746555)
Teddy Auchinlech has mean: True or False?
True (0.794384956668203)
Teddy Auchinlech has motive: True or False?
True (1.43163262838224)
Teddy Auchinlech has opportunity: True or False?
True (1.931643529252958)
### Jonathan Ingersoll
- mean: False (0.1871326586867097)
- motive: False (0.13776433168642355)
- opportunity: False (0.13028544481973592)

### Lucille Cameron
- mean: False (0.22609937418585557)
- motive: False (0.05686151818578955)
- opportunity: False (0.044847906697005)

### Marion Montgomery
- mean: False (0.04813677198642585)
- motive: False (0.07107364766122048)
- opportunity: False (0.03718674151267698)

### Teddy Auchinlech
- mean: True (0.794384956668203)
- motive: True (1.43163262838224)
- opportunity: True (1.931643529252958)

The culprit is Teddy Auchinlech.
In fact, it is Jonathan Ingersoll.
## 5minutemystery-the-classic-automobile-mystery
Gary Riggs is guilty: True or False?
True (0.9553191057869168)
Gary Riggs has mean: True or False?
True (0.9402434229803527)
Gary Riggs has motive: True or False?
True (0.9791556598479493)
Gary Riggs has opportunity: True or False?
True (0.9326989068252284)
Gerald "Doc" McCroy is guilty: True or False?
True (0.9590009457171959)
Gerald "Doc" McCroy has mean: True or False?
True (0.892187358563457)
Gerald "Doc" McCroy has motive: True or False?
True (0.9815950994553841)
Gerald "Doc" McCroy has opportunity: True or False?
True (0.8828325273478573)
Mike Benson is guilty: True or False?
True (0.9548162209309636)
Mike Benson has mean: True or False?
True (0.8316905440184192)
Mike Benson has motive: True or False?
True (0.984486222973347)
Mike Benson has opportunity: True or False?
True (0.9618217364339323)
Tommy Flowers is guilty: True or False?
True (0.928538502080124)
Tommy Flowers has mean: True or False?
True (0.947769104959166)
Tommy Flowers has motive: True or False?
True (0.9855382441311838)
Tommy Flowers has opportunity: True or False?
True (0.9546474221708894)
### Gary Riggs
- mean: False (0.05975657701964732)
- motive: False (0.020844340152050722)
- opportunity: False (0.06730109317477162)

### Gerald "Doc" McCroy
- mean: False (0.10781264143654301)
- motive: False (0.018404900544615854)
- opportunity: False (0.11716747265214267)

### Mike Benson
- mean: False (0.16830945598158076)
- motive: False (0.01551377702665302)
- opportunity: False (0.03817826356606768)

### Tommy Flowers
- mean: True (0.947769104959166)
- motive: True (0.9855382441311838)
- opportunity: True (0.9546474221708894)

The culprit is Tommy Flowers.
In fact, it is Gerald "Doc" McCroy.
## 5minutemystery-rocks-and-feathers
Barley is guilty: True or False?
True (0.9803938269930638)
Barley has mean: True or False?
True (0.9149009003623453)
Barley has motive: True or False?
True (0.9885140654321632)
Barley has opportunity: True or False?
True (0.9563089618154458)
Bertha is guilty: True or False?
True (0.9781771902180998)
Bertha has mean: True or False?
True (0.9107043724734579)
Bertha has motive: True or False?
True (0.9860174060256517)
Bertha has opportunity: True or False?
True (0.9407897579933674)
Joseph is guilty: True or False?
True (0.9767580632580227)
Joseph has mean: True or False?
True (0.8714748565614324)
Joseph has motive: True or False?
True (0.9846050735525358)
Joseph has opportunity: True or False?
True (0.9383503780077049)
Tom is guilty: True or False?
True (0.9747251273624444)
Tom has mean: True or False?
True (0.9260365949489886)
Tom has motive: True or False?
True (0.9841241829125448)
Tom has opportunity: True or False?
True (0.9029524930853913)
### Barley
- mean: True (0.9149009003623453)
- motive: True (0.9885140654321632)
- opportunity: True (0.9563089618154458)

### Bertha
- mean: False (0.08929562752654208)
- motive: False (0.013982593974348312)
- opportunity: False (0.05921024200663261)

### Joseph
- mean: False (0.12852514343856758)
- motive: False (0.015394926447464208)
- opportunity: False (0.06164962199229507)

### Tom
- mean: False (0.0739634050510114)
- motive: False (0.015875817087455224)
- opportunity: False (0.09704750691460873)

The culprit is Barley.
In fact, it is Tom.
## 5minutemystery-who-is-telling-the-truth
Bill Flowers is guilty: True or False?
True (6.79557595610628)
Bill Flowers has mean: True or False?
True (1.3275039629265664)
Bill Flowers has motive: True or False?
True (2.7880484433212644)
Bill Flowers has opportunity: True or False?
True (1.8472763495547708)
Jane Neal is guilty: True or False?
True (6.0577882142450195)
Jane Neal has mean: True or False?
True (0.9178934131644976)
Jane Neal has motive: True or False?
True (3.8160518900271723)
Jane Neal has opportunity: True or False?
True (0.924959242644946)
Jimmy Smith is guilty: True or False?
True (2.9199808911835494)
Jimmy Smith has mean: True or False?
True (0.9105453462677353)
Jimmy Smith has motive: True or False?
True (0.9751546380646186)
Jimmy Smith has opportunity: True or False?
True (0.9492946258008691)
Larry Gerard is guilty: True or False?
True (4.445725184361779)
Larry Gerard has mean: True or False?
True (0.9621075390858402)
Larry Gerard has motive: True or False?
True (2.327079594569891)
Larry Gerard has opportunity: True or False?
True (0.9661560069290531)
Paula Newsome is guilty: True or False?
True (6.19686643615343)
Paula Newsome has mean: True or False?
True (1.101176589948744)
Paula Newsome has motive: True or False?
True (4.531693733651497)
Paula Newsome has opportunity: True or False?
True (2.1901572309810446)
### Bill Flowers
- mean: False (0.0)
- motive: False (0.0)
- opportunity: False (0.0)

### Jane Neal
- mean: False (0.08210658683550243)
- motive: False (0.0)
- opportunity: False (0.075040757355054)

### Jimmy Smith
- mean: False (0.08945465373226469)
- motive: False (0.02484536193538145)
- opportunity: False (0.050705374199130904)

### Larry Gerard
- mean: False (0.037892460914159765)
- motive: False (0.0)
- opportunity: False (0.033843993070946876)

### Paula Newsome
- mean: True (1.101176589948744)
- motive: True (4.531693733651497)
- opportunity: True (2.1901572309810446)

The culprit is Paula Newsome.
In fact, it is Paula Newsome.
## 5minutemystery-ask-marthathe-identity-thief
Grace Means is guilty: True or False?
True (0.8397339530959691)
Grace Means has mean: True or False?
True (0.5660185351323219)
Grace Means has motive: True or False?
True (0.9167081124681512)
Grace Means has opportunity: True or False?
True (0.8891443609199433)
Joan Colthrop is guilty: True or False?
True (0.6951311179371613)
Joan Colthrop has mean: True or False?
True (0.7879311977554747)
Joan Colthrop has motive: True or False?
True (0.9556514027264735)
Joan Colthrop has opportunity: True or False?
True (0.8267118326419537)
Laura Parsons is guilty: True or False?
True (0.9494823209990744)
Laura Parsons has mean: True or False?
True (0.8013146490010521)
Laura Parsons has motive: True or False?
True (0.9525741334779666)
Laura Parsons has opportunity: True or False?
True (0.8944211616820568)
Maybelle Johnson is guilty: True or False?
True (0.9246876822649571)
Maybelle Johnson has mean: True or False?
True (0.8697145551802641)
Maybelle Johnson has motive: True or False?
True (0.9618217364339323)
Maybelle Johnson has opportunity: True or False?
True (0.9427180278987515)
### Grace Means
- mean: False (0.4339814648676781)
- motive: False (0.0832918875318488)
Map:  91%|█████████ | 184/203 [3:14:18<17:16, 54.54s/ examples]Map:  91%|█████████ | 185/203 [3:15:13<16:24, 54.72s/ examples]Map:  92%|█████████▏| 186/203 [3:15:50<14:01, 49.51s/ examples]Map:  92%|█████████▏| 187/203 [3:16:32<12:34, 47.18s/ examples]Map:  93%|█████████▎| 188/203 [3:17:22<12:00, 48.02s/ examples]- opportunity: False (0.11085563908005669)

### Joan Colthrop
- mean: False (0.2120688022445253)
- motive: False (0.04434859727352647)
- opportunity: False (0.1732881673580463)

### Laura Parsons
- mean: False (0.1986853509989479)
- motive: False (0.0474258665220334)
- opportunity: False (0.10557883831794324)

### Maybelle Johnson
- mean: True (0.8697145551802641)
- motive: True (0.9618217364339323)
- opportunity: True (0.9427180278987515)

The culprit is Maybelle Johnson.
In fact, it is Joan Colthrop.
## 5minutemystery-ask-marthathe-pickpocket
Johnny Anderson is guilty: True or False?
True (0.9950659273323337)
Johnny Anderson has mean: True or False?
True (0.9820482724696491)
Johnny Anderson has motive: True or False?
True (0.9969868660453549)
Johnny Anderson has opportunity: True or False?
True (0.9918752912999942)
Morris Emerson is guilty: True or False?
True (0.9862841366970037)
Morris Emerson has mean: True or False?
True (0.9457010626376176)
Morris Emerson has motive: True or False?
True (0.9927180410162981)
Morris Emerson has opportunity: True or False?
True (0.974676967005652)
Sarah Browne is guilty: True or False?
True (0.9954527021774832)
Sarah Browne has mean: True or False?
True (0.9795506000537378)
Sarah Browne has motive: True or False?
True (0.9958418606562941)
Sarah Browne has opportunity: True or False?
True (0.9822195762235328)
Tom Blankenship is guilty: True or False?
True (0.9961344004804578)
Tom Blankenship has mean: True or False?
True (0.9811307191121953)
Tom Blankenship has motive: True or False?
True (0.9953363539243901)
Tom Blankenship has opportunity: True or False?
True (0.9900827408432981)
### Johnny Anderson
- mean: True (0.9820482724696491)
- motive: True (0.9969868660453549)
- opportunity: True (0.9918752912999942)

### Morris Emerson
- mean: False (0.05429893736238245)
- motive: False (0.007281958983701875)
- opportunity: False (0.025323032994348016)

### Sarah Browne
- mean: False (0.02044939994626216)
- motive: False (0.004158139343705902)
- opportunity: False (0.017780423776467158)

### Tom Blankenship
- mean: False (0.018869280887804707)
- motive: False (0.004663646075609873)
- opportunity: False (0.00991725915670194)

The culprit is Johnny Anderson.
In fact, it is Tom Blankenship.
## 5minutemystery-diamond-deception
Horace is guilty: True or False?
True (0.9105454073245608)
Horace has mean: True or False?
True (0.9145963810991447)
Horace has motive: True or False?
True (0.8705972382426559)
Horace has opportunity: True or False?
True (0.9445872321654378)
Jake is guilty: True or False?
True (0.9124361878432953)
Jake has mean: True or False?
True (0.8444089912414552)
Jake has motive: True or False?
True (0.9170058945178141)
Jake has opportunity: True or False?
True (0.8534247816107388)
John is guilty: True or False?
True (0.9127477403975288)
John has mean: True or False?
True (0.8955226517597132)
John has motive: True or False?
True (0.9192084097444476)
John has opportunity: True or False?
True (0.9405717864730483)
Lewis is guilty: True or False?
True (0.8509646659219744)
Lewis has mean: True or False?
True (0.6876299924560524)
Lewis has motive: True or False?
False (1.0923348003492868)
Lewis has opportunity: True or False?
True (0.9567959302164903)
### Horace
- mean: False (0.08540361890085535)
- motive: False (0.1294027617573441)
- opportunity: False (0.05541276783456217)

### Jake
- mean: False (0.1555910087585448)
- motive: False (0.08299410548218589)
- opportunity: False (0.14657521838926124)

### John
- mean: True (0.8955226517597132)
- motive: True (0.9192084097444476)
- opportunity: True (0.9405717864730483)

### Lewis
- mean: False (0.3123700075439476)
- motive: False (1.0923348003492868)
- opportunity: False (0.04320406978350966)

The culprit is John.
In fact, it is Lewis.
## 5minutemystery-where-is-matthew
Andy's bedroom is guilty: True or False?
True (0.9513234509300917)
Andy's bedroom has mean: True or False?
True (0.9235923286659299)
Andy's bedroom has motive: True or False?
True (0.9710193279819936)
Andy's bedroom has opportunity: True or False?
True (0.875361437979977)
Matthew's bedroom is guilty: True or False?
True (0.9709092372014624)
Matthew's bedroom has mean: True or False?
True (0.9656413200400066)
Matthew's bedroom has motive: True or False?
True (0.9907320139497646)
Matthew's bedroom has opportunity: True or False?
True (0.9644556034131689)
The garage is guilty: True or False?
True (0.9053223122169206)
The garage has mean: True or False?
True (0.9139841191734227)
The garage has motive: True or False?
True (0.9613890640022783)
The garage has opportunity: True or False?
True (0.9697853917136491)
The hall closet is guilty: True or False?
True (0.8929365260632085)
The hall closet has mean: True or False?
True (0.9102267057681164)
The hall closet has motive: True or False?
True (0.9164093756391206)
The hall closet has opportunity: True or False?
True (0.8933094122075369)
The tree house is guilty: True or False?
True (0.8305941261447712)
The tree house has mean: True or False?
True (0.8799743689174987)
The tree house has motive: True or False?
True (0.920789721359066)
The tree house has opportunity: True or False?
True (0.9099069836112468)
### Andy's bedroom
- mean: False (0.07640767133407012)
- motive: False (0.02898067201800636)
- opportunity: False (0.12463856202002299)

### Matthew's bedroom
- mean: True (0.9656413200400066)
- motive: True (0.9907320139497646)
- opportunity: True (0.9644556034131689)

### The garage
- mean: False (0.0860158808265773)
- motive: False (0.038610935997721696)
- opportunity: False (0.03021460828635092)

### The hall closet
- mean: False (0.08977329423188363)
- motive: False (0.08359062436087938)
- opportunity: False (0.1066905877924631)

### The tree house
- mean: False (0.1200256310825013)
- motive: False (0.079210278640934)
- opportunity: False (0.09009301638875322)

The culprit is Matthew's bedroom.
In fact, it is The tree house.
## 5minutemystery-the-mysterious-gift
CIndy is guilty: True or False?
True (0.8987665204865408)
CIndy has mean: True or False?
True (0.8116760258690822)
CIndy has motive: True or False?
True (0.9445872321654378)
CIndy has opportunity: True or False?
True (0.9447913165152162)
Josie's mother is guilty: True or False?
True (0.49999999904767284)
Josie's mother has mean: True or False?
True (0.8494723435042196)
Josie's mother has motive: True or False?
True (0.9029524325377104)
Josie's mother has opportunity: True or False?
True (0.8459424988148251)
Lester is guilty: True or False?
True (0.8134607635851566)
Lester has mean: True or False?
True (0.6451199006197486)
Lester has motive: True or False?
True (0.9378969089655451)
Lester has opportunity: True or False?
True (0.8832359917473193)
Lorraine is guilty: True or False?
True (0.6934729182490079)
Lorraine has mean: True or False?
True (0.5907791930117218)
Lorraine has motive: True or False?
True (0.8951566249612815)
Lorraine has opportunity: True or False?
True (0.8294920340613177)
### CIndy
- mean: True (0.8116760258690822)
- motive: True (0.9445872321654378)
- opportunity: True (0.9447913165152162)

### Josie's mother
- mean: False (0.15052765649578037)
- motive: False (0.0970475674622896)
- opportunity: False (0.15405750118517492)

### Lester
- mean: False (0.35488009938025145)
- motive: False (0.06210309103445488)
- opportunity: False (0.11676400825268074)

### Lorraine
- mean: False (0.40922080698827823)
- motive: False (0.10484337503871854)
- opportunity: False (0.17050796593868234)

The culprit is CIndy.
In fact, it is Lorraine.
## 5minutemystery-perry-mason-and-the-high-school-crush-murder
Morris Ingalls is guilty: True or False?
True (0.9641867858895684)
Morris Ingalls has mean: True or False?
True (0.9184802773231918)
Morris Ingalls has motive: True or False?
True (0.9692661174528692)
Morris Ingalls has opportunity: True or False?
True (0.926967620306882)
Randolph Johnson is guilty: True or False?
True (0.9366336466314406)
Randolph Johnson has mean: True or False?
True (0.9048188910591489)
Randolph Johnson has motive: True or False?
True (0.9506863937012171)
Randolph Johnson has opportunity: True or False?
True (0.875361437979977)
Map:  93%|█████████▎| 189/203 [3:18:43<13:28, 57.74s/ examples]Map:  94%|█████████▎| 190/203 [3:19:38<12:20, 56.93s/ examples]Map:  94%|█████████▍| 191/203 [3:20:15<10:12, 51.00s/ examples]Map:  95%|█████████▍| 192/203 [3:20:52<08:37, 47.01s/ examples]Map:  95%|█████████▌| 193/203 [3:21:45<08:06, 48.70s/ examples]Sarah Conrad is guilty: True or False?
True (0.9569571625798028)
Sarah Conrad has mean: True or False?
True (0.8723474190177988)
Sarah Conrad has motive: True or False?
True (0.9598374351134399)
Sarah Conrad has opportunity: True or False?
True (0.9178934131644976)
Tom Gooding is guilty: True or False?
True (0.9481545078856665)
Tom Gooding has mean: True or False?
True (0.9132133125595024)
Tom Gooding has motive: True or False?
True (0.9706043010821588)
Tom Gooding has opportunity: True or False?
True (0.9398029451247769)
### Morris Ingalls
- mean: False (0.08151972267680818)
- motive: False (0.03073388254713083)
- opportunity: False (0.07303237969311804)

### Randolph Johnson
- mean: False (0.09518110894085108)
- motive: False (0.0493136062987829)
- opportunity: False (0.12463856202002299)

### Sarah Conrad
- mean: False (0.12765258098220122)
- motive: False (0.040162564886560115)
- opportunity: False (0.08210658683550243)

### Tom Gooding
- mean: True (0.9132133125595024)
- motive: True (0.9706043010821588)
- opportunity: True (0.9398029451247769)

The culprit is Tom Gooding.
In fact, it is Morris Ingalls.
## 5minutemystery-who-stole-super-tuesday
Barry is guilty: True or False?
True (0.7766228995235426)
Barry has mean: True or False?
True (0.9026095892260383)
Barry has motive: True or False?
True (0.8278281049441929)
Barry has opportunity: True or False?
True (0.7683857159844143)
Ricky Churrelo is guilty: True or False?
True (0.8080671968507699)
Ricky Churrelo has mean: True or False?
True (0.8175745039697023)
Ricky Churrelo has motive: True or False?
True (0.8840392847025188)
Ricky Churrelo has opportunity: True or False?
True (0.7718434926244166)
Simon Knowles is guilty: True or False?
True (0.8316905440184192)
Simon Knowles has mean: True or False?
True (0.8267118326419537)
Simon Knowles has motive: True or False?
True (0.9168570665458525)
Simon Knowles has opportunity: True or False?
True (0.7468781997658912)
Xavier Ericksen is guilty: True or False?
True (0.7911764307711107)
Xavier Ericksen has mean: True or False?
True (0.8494724067948436)
Xavier Ericksen has motive: True or False?
True (0.8947895144283036)
Xavier Ericksen has opportunity: True or False?
True (0.7592254214399092)
### Barry
- mean: False (0.09739041077396171)
- motive: False (0.1721718950558071)
- opportunity: False (0.2316142840155857)

### Ricky Churrelo
- mean: False (0.18242549603029767)
- motive: False (0.1159607152974812)
- opportunity: False (0.22815650737558335)

### Simon Knowles
- mean: False (0.1732881673580463)
- motive: False (0.08314293345414747)
- opportunity: False (0.2531218002341088)

### Xavier Ericksen
- mean: True (0.8494724067948436)
- motive: True (0.8947895144283036)
- opportunity: True (0.7592254214399092)

The culprit is Xavier Ericksen.
In fact, it is Simon Knowles.
## 5minutemystery-the-missing-son
Caleb is guilty: True or False?
True (0.84619676525883)
Caleb has mean: True or False?
True (0.9066531077351827)
Caleb has motive: True or False?
True (0.9678993227186541)
Caleb has opportunity: True or False?
True (0.7872777601997338)
Conner is guilty: True or False?
True (0.9337940192482527)
Conner has mean: True or False?
True (0.9637799266082508)
Conner has motive: True or False?
True (0.9858821037649884)
Conner has opportunity: True or False?
True (0.9111797236708432)
Jordan is guilty: True or False?
True (0.8464508054137014)
Jordan has mean: True or False?
True (0.6513548405484016)
Jordan has motive: True or False?
True (0.962813258487323)
Jordan has opportunity: True or False?
True (0.9099069836112468)
Kyle is guilty: True or False?
True (0.9368651509033574)
Kyle has mean: True or False?
True (0.944176853162527)
Kyle has motive: True or False?
True (0.9837849137206752)
Kyle has opportunity: True or False?
True (0.9658995863383641)
### Caleb
- mean: False (0.0933468922648173)
- motive: False (0.03210067728134591)
- opportunity: False (0.21272223980026617)

### Conner
- mean: False (0.03622007339174915)
- motive: False (0.014117896235011584)
- opportunity: False (0.08882027632915679)

### Jordan
- mean: False (0.34864515945159835)
- motive: False (0.03718674151267698)
- opportunity: False (0.09009301638875322)

### Kyle
- mean: True (0.944176853162527)
- motive: True (0.9837849137206752)
- opportunity: True (0.9658995863383641)

The culprit is Kyle.
In fact, it is Caleb.
## 5minutemystery-the-stolen-cupcake
Angelica is guilty: True or False?
True (0.925499741040984)
Angelica has mean: True or False?
True (0.8086723099497763)
Angelica has motive: True or False?
True (0.9563089618154458)
Angelica has opportunity: True or False?
True (0.9339146597970963)
Caedon is guilty: True or False?
True (0.9336731438527403)
Caedon has mean: True or False?
True (0.8764230069135861)
Caedon has motive: True or False?
True (0.9733929040540585)
Caedon has opportunity: True or False?
True (0.9007046239919082)
Ross is guilty: True or False?
True (0.925499741040984)
Ross has mean: True or False?
True (0.7360212909517942)
Ross has motive: True or False?
True (0.9797065261759322)
Ross has opportunity: True or False?
True (0.9388008138003494)
Tony is guilty: True or False?
True (0.8910549899564296)
Tony has mean: True or False?
True (0.7049732238008671)
Tony has motive: True or False?
True (0.9732915161502819)
Tony has opportunity: True or False?
True (0.925499741040984)
### Angelica
- mean: False (0.19132769005022365)
- motive: False (0.04369103818455422)
- opportunity: False (0.06608534020290369)

### Caedon
- mean: True (0.8764230069135861)
- motive: True (0.9733929040540585)
- opportunity: True (0.9007046239919082)

### Ross
- mean: False (0.26397870904820575)
- motive: False (0.020293473824067765)
- opportunity: False (0.06119918619965059)

### Tony
- mean: False (0.29502677619913287)
- motive: False (0.026708483849718134)
- opportunity: False (0.07450025895901602)

The culprit is Caedon.
In fact, it is Caedon.
## 5minutemystery-school-trip
Beth is guilty: True or False?
True (0.8856314413364714)
Beth has mean: True or False?
True (0.60859406896259)
Beth has motive: True or False?
True (0.9412234437340664)
Beth has opportunity: True or False?
True (0.7732163648437078)
Damon is guilty: True or False?
True (0.8727817583545995)
Damon has mean: True or False?
True (0.7981867775042927)
Damon has motive: True or False?
True (0.8512123240556729)
Damon has opportunity: True or False?
True (0.6951311179371613)
Leo is guilty: True or False?
True (0.905989824801558)
Leo has mean: True or False?
True (0.8710367026584496)
Leo has motive: True or False?
True (0.962391318570921)
Leo has opportunity: True or False?
True (0.9390248079664695)
Mr. Michael's is guilty: True or False?
True (0.811078188867804)
Mr. Michael's has mean: True or False?
True (0.8727817583545995)
Mr. Michael's has motive: True or False?
True (0.9244151684978138)
Mr. Michael's has opportunity: True or False?
True (0.8122723669190336)
The Seniors is guilty: True or False?
True (0.5525396910980834)
The Seniors has mean: True or False?
True (0.7806625377756776)
The Seniors has motive: True or False?
True (0.7786493288700866)
The Seniors has opportunity: True or False?
False (0.5302364729224919)
### Beth
- mean: False (0.39140593103740995)
- motive: False (0.05877655626593359)
- opportunity: False (0.22678363515629218)

### Damon
- mean: False (0.20181322249570732)
- motive: False (0.14878767594432707)
- opportunity: False (0.3048688820628387)

### Leo
- mean: True (0.8710367026584496)
- motive: True (0.962391318570921)
- opportunity: True (0.9390248079664695)

### Mr. Michael's
- mean: False (0.12721824164540052)
- motive: False (0.0755848315021862)
- opportunity: False (0.1877276330809664)

### The Seniors
- mean: False (0.21933746222432238)
- motive: False (0.22135067112991336)
- opportunity: False (0.5302364729224919)

The culprit is Leo.
In fact, it is The Seniors.
## 5minutemystery-arsonist-attack
Jade Foster is guilty: True or False?
True (0.8734308550930344)
Jade Foster has mean: True or False?
True (0.7348812840309261)
Jade Foster has motive: True or False?
True (0.7225270177274575)
Jade Foster has opportunity: True or False?
True (0.8322366416985943)
Jock Matt is guilty: True or False?
Map:  96%|█████████▌| 194/203 [3:22:47<07:53, 52.64s/ examples]Map:  96%|█████████▌| 195/203 [3:23:32<06:42, 50.36s/ examples]Map:  97%|█████████▋| 196/203 [3:24:15<05:37, 48.26s/ examples]Map:  97%|█████████▋| 197/203 [3:25:03<04:48, 48.10s/ examples]True (0.8558511727823209)
Jock Matt has mean: True or False?
False (0.5136684130997575)
Jock Matt has motive: True or False?
True (0.7799928701983835)
Jock Matt has opportunity: True or False?
True (0.7853085971692302)
Madelyn Reader is guilty: True or False?
True (0.8661325012437474)
Madelyn Reader has mean: True or False?
True (0.550607385906944)
Madelyn Reader has motive: True or False?
True (0.7634837587244478)
Madelyn Reader has opportunity: True or False?
True (0.8056321690561029)
Max Crabgrass is guilty: True or False?
True (1.2484914190047414)
Max Crabgrass has mean: True or False?
True (0.7185943809170431)
Max Crabgrass has motive: True or False?
True (0.8826302888575707)
Max Crabgrass has opportunity: True or False?
True (0.9008791478232747)
Security Guard is guilty: True or False?
True (0.9289263523387795)
Security Guard has mean: True or False?
True (0.8958876133958744)
Security Guard has motive: True or False?
True (0.9161096235973493)
Security Guard has opportunity: True or False?
True (0.9136765013387816)
### Jade Foster
- mean: False (0.2651187159690739)
- motive: False (0.27747298227254247)
- opportunity: False (0.16776335830140565)

### Jock Matt
- mean: False (0.5136684130997575)
- motive: False (0.22000712980161652)
- opportunity: False (0.21469140283076982)

### Madelyn Reader
- mean: False (0.449392614093056)
- motive: False (0.23651624127555215)
- opportunity: False (0.1943678309438971)

### Max Crabgrass
- mean: False (0.2814056190829569)
- motive: False (0.11736971114242933)
- opportunity: False (0.09912085217672528)

### Security Guard
- mean: True (0.8958876133958744)
- motive: True (0.9161096235973493)
- opportunity: True (0.9136765013387816)

The culprit is Security Guard.
In fact, it is Jade Foster.
## 5minutemystery-investigation-sabotager
Emma is guilty: True or False?
True (0.9658995287662642)
Emma has mean: True or False?
True (0.8803863464576128)
Emma has motive: True or False?
True (0.9326989068252284)
Emma has opportunity: True or False?
True (0.9447913165152162)
Mary is guilty: True or False?
True (0.9263036859044167)
Mary has mean: True or False?
True (0.8812065732757132)
Mary has motive: True or False?
True (0.934872446722342)
Mary has opportunity: True or False?
True (0.9682614213403071)
Peter is guilty: True or False?
True (0.8719117627136385)
Peter has mean: True or False?
True (0.8289387819824735)
Peter has motive: True or False?
True (0.9190633328333496)
Peter has opportunity: True or False?
True (0.9289263523387795)
Tim is guilty: True or False?
True (0.9369805475192257)
Tim has mean: True or False?
True (0.9729852083817088)
Tim has motive: True or False?
True (0.9602867377475474)
Tim has opportunity: True or False?
True (0.9012274173198201)
Valerie is guilty: True or False?
True (0.814643384779728)
Valerie has mean: True or False?
True (0.8376199551237796)
Valerie has motive: True or False?
True (0.7122321792841629)
Valerie has opportunity: True or False?
True (0.943347633443741)
### Emma
- mean: False (0.11961365354238718)
- motive: False (0.06730109317477162)
- opportunity: False (0.055208683484783805)

### Mary
- mean: False (0.11879342672428683)
- motive: False (0.06512755327765796)
- opportunity: False (0.03173857865969287)

### Peter
- mean: False (0.1710612180175265)
- motive: False (0.08093666716665038)
- opportunity: False (0.07107364766122048)

### Tim
- mean: True (0.9729852083817088)
- motive: True (0.9602867377475474)
- opportunity: True (0.9012274173198201)

### Valerie
- mean: False (0.16238004487622038)
- motive: False (0.28776782071583706)
- opportunity: False (0.05665236655625905)

The culprit is Tim.
In fact, it is Emma.
## 5minutemystery-the-presidential-smear-campaint-a-jacelyn-drew-mystery
Brittany is guilty: True or False?
True (0.9336731438527403)
Brittany has mean: True or False?
True (0.8563324216110711)
Brittany has motive: True or False?
True (0.9425067301242699)
Brittany has opportunity: True or False?
True (0.9516838792709049)
Isis is guilty: True or False?
True (0.9682013404912752)
Isis has mean: True or False?
True (0.8816149238192855)
Isis has motive: True or False?
True (0.9673486357359453)
Isis has opportunity: True or False?
True (0.943451882217003)
Marie is guilty: True or False?
True (0.9515039936355008)
Marie has mean: True or False?
True (0.8745065930973813)
Marie has motive: True or False?
True (0.9429286143036572)
Marie has opportunity: True or False?
True (0.962813258487323)
Norma is guilty: True or False?
True (0.9240047963507929)
Norma has mean: True or False?
True (0.7885832152749314)
Norma has motive: True or False?
True (0.9261703516148618)
Norma has opportunity: True or False?
True (0.9583821892129424)
### Brittany
- mean: False (0.14366757838892885)
- motive: False (0.05749326987573011)
- opportunity: False (0.04831612072909508)

### Isis
- mean: True (0.8816149238192855)
- motive: True (0.9673486357359453)
- opportunity: True (0.943451882217003)

### Marie
- mean: False (0.12549340690261868)
- motive: False (0.05707138569634285)
- opportunity: False (0.03718674151267698)

### Norma
- mean: False (0.21141678472506864)
- motive: False (0.07382964838513817)
- opportunity: False (0.04161781078705762)

The culprit is Isis.
In fact, it is Isis.
## 5minutemystery-the-sunday-mystery
Jack Jackson is guilty: True or False?
True (0.7853085971692302)
Jack Jackson has mean: True or False?
True (0.8134608241927087)
Jack Jackson has motive: True or False?
True (0.9799765949220004)
Jack Jackson has opportunity: True or False?
True (0.9681411371390284)
Jimmy Jackson is guilty: True or False?
True (0.8104789202520752)
Jimmy Jackson has mean: True or False?
False (0.6584175136252488)
Jimmy Jackson has motive: True or False?
True (0.9680204387474981)
Jimmy Jackson has opportunity: True or False?
True (0.9076402191395381)
Jon Jackson is guilty: True or False?
True (0.9196425103002197)
Jon Jackson has mean: True or False?
True (0.595492552580428)
Jon Jackson has motive: True or False?
True (0.958847105894029)
Jon Jackson has opportunity: True or False?
True (0.9005298052062833)
Maria Jackson is guilty: True or False?
True (0.8080671968507699)
Maria Jackson has mean: True or False?
True (0.7950222460539826)
Maria Jackson has motive: True or False?
True (0.9683213832701327)
Maria Jackson has opportunity: True or False?
True (0.929696145502287)
Spot is guilty: True or False?
True (0.8910549899564296)
Spot has mean: True or False?
False (0.5992506595844092)
Spot has motive: True or False?
False (0.6463158311908145)
Spot has opportunity: True or False?
True (0.9549844874375936)
### Jack Jackson
- mean: True (0.8134608241927087)
- motive: True (0.9799765949220004)
- opportunity: True (0.9681411371390284)

### Jimmy Jackson
- mean: False (0.6584175136252488)
- motive: False (0.0319795612525019)
- opportunity: False (0.09235978086046193)

### Jon Jackson
- mean: False (0.404507447419572)
- motive: False (0.041152894105971005)
- opportunity: False (0.09947019479371666)

### Maria Jackson
- mean: False (0.20497775394601736)
- motive: False (0.03167861672986727)
- opportunity: False (0.07030385449771304)

### Spot
- mean: False (0.5992506595844092)
- motive: False (0.6463158311908145)
- opportunity: False (0.045015512562406435)

The culprit is Jack Jackson.
In fact, it is Spot.
## 5minutemystery-the-mystery-of-heritage
Jack Anderson is guilty: True or False?
True (0.9651848090355489)
Jack Anderson has mean: True or False?
True (0.7866228249849953)
Jack Anderson has motive: True or False?
True (0.9564719186263709)
Jack Anderson has opportunity: True or False?
True (0.8638516611889259)
Jessica Anderson is guilty: True or False?
True (0.9757623676279906)
Jessica Anderson has mean: True or False?
True (0.8098781635062345)
Jessica Anderson has motive: True or False?
True (0.9774139529645163)
Jessica Anderson has opportunity: True or False?
True (0.9573576465213919)
Martha Anderson is guilty: True or False?
True (0.9734434487527764)
Martha Anderson has mean: True or False?
True (0.9105454073245608)
Martha Anderson has motive: True or False?
True (0.9843664168051008)
Martha Anderson has opportunity: True or False?
True (0.9614615446058614)
Mrs. Neil is guilty: True or False?
Map:  98%|█████████▊| 198/203 [3:25:37<03:39, 43.95s/ examples]Map:  98%|█████████▊| 199/203 [3:26:04<02:34, 38.64s/ examples]Map:  99%|█████████▊| 200/203 [3:26:53<02:05, 41.76s/ examples]Map:  99%|█████████▉| 201/203 [3:27:30<01:20, 40.49s/ examples]Map: 100%|█████████▉| 202/203 [3:28:19<00:43, 43.14s/ examples]True (0.9625325207646147)
Mrs. Neil has mean: True or False?
True (0.927887794449634)
Mrs. Neil has motive: True or False?
True (0.982590972614882)
Mrs. Neil has opportunity: True or False?
True (0.9824568029810573)
### Jack Anderson
- mean: False (0.21337717501500475)
- motive: False (0.04352808137362907)
- opportunity: False (0.13614833881107413)

### Jessica Anderson
- mean: False (0.19012183649376546)
- motive: False (0.022586047035483725)
- opportunity: False (0.04264235347860812)

### Martha Anderson
- mean: False (0.0894545926754392)
- motive: False (0.01563358319489916)
- opportunity: False (0.03853845539413858)

### Mrs. Neil
- mean: True (0.927887794449634)
- motive: True (0.982590972614882)
- opportunity: True (0.9824568029810573)

The culprit is Mrs. Neil.
In fact, it is Jessica Anderson.
## 5minutemystery-murder-of-the-actor
Bruce Whittingley is guilty: True or False?
True (0.986151396974789)
Bruce Whittingley has mean: True or False?
True (0.8080671968507699)
Bruce Whittingley has motive: True or False?
True (0.9558166865608263)
Bruce Whittingley has opportunity: True or False?
True (0.9498557456415421)
Marie Carloette is guilty: True or False?
True (0.9846050735525358)
Marie Carloette has mean: True or False?
True (0.9730365275631271)
Marie Carloette has motive: True or False?
True (0.9729338284788606)
Marie Carloette has opportunity: True or False?
True (0.9642542005689824)
Mario Marcino is guilty: True or False?
True (0.9863368866841652)
Mario Marcino has mean: True or False?
True (0.9473810211532727)
Mario Marcino has motive: True or False?
True (0.9862576727459876)
Mario Marcino has opportunity: True or False?
True (0.9797840705842182)
### Bruce Whittingley
- mean: False (0.1919328031492301)
- motive: False (0.0441833134391737)
- opportunity: False (0.05014425435845793)

### Marie Carloette
- mean: False (0.026963472436872915)
- motive: False (0.027066171521139437)
- opportunity: False (0.03574579943101763)

### Mario Marcino
- mean: True (0.9473810211532727)
- motive: True (0.9862576727459876)
- opportunity: True (0.9797840705842182)

The culprit is Mario Marcino.
In fact, it is Marie Carloette.
## 5minutemystery-another-hotel-murder
Dianne Shelby is guilty: True or False?
True (0.8919052512911346)
Dianne Shelby has mean: True or False?
True (0.7866228835929651)
Dianne Shelby has motive: True or False?
True (0.9525520223134187)
Dianne Shelby has opportunity: True or False?
True (0.864539320523716)
James Castro is guilty: True or False?
True (1.0058063062603522)
James Castro has mean: True or False?
True (0.860369148541484)
James Castro has motive: True or False?
True (0.9067357195193472)
James Castro has opportunity: True or False?
True (0.892187358563457)
Kevin King is guilty: True or False?
True (0.9458512675695098)
Kevin King has mean: True or False?
True (0.9064877041303855)
Kevin King has motive: True or False?
True (0.9545415629477866)
Kevin King has opportunity: True or False?
True (0.9515490540211475)
Roger Shelby is guilty: True or False?
True (0.8488469713350262)
Roger Shelby has mean: True or False?
True (0.7704647687904915)
Roger Shelby has motive: True or False?
True (0.9137535101236324)
Roger Shelby has opportunity: True or False?
True (0.8881781721623143)
### Dianne Shelby
- mean: False (0.21337711640703494)
- motive: False (0.047447977686581266)
- opportunity: False (0.13546067947628404)

### James Castro
- mean: False (0.13963085145851595)
- motive: False (0.09326428048065283)
- opportunity: False (0.10781264143654301)

### Kevin King
- mean: True (0.9064877041303855)
- motive: True (0.9545415629477866)
- opportunity: True (0.9515490540211475)

### Roger Shelby
- mean: False (0.22953523120950847)
- motive: False (0.08624648987636763)
- opportunity: False (0.11182182783768568)

The culprit is Kevin King.
In fact, it is James Castro.
## 5minutemystery-the-missing-book
Brad is guilty: True or False?
True (0.955152093302995)
Brad has mean: True or False?
True (0.9319595674053855)
Brad has motive: True or False?
True (0.9369805475192257)
Brad has opportunity: True or False?
True (0.9832788702399727)
Fred is guilty: True or False?
True (0.9656413200400066)
Fred has mean: True or False?
True (0.9475755109125973)
Fred has motive: True or False?
False (0.7665304747562915)
Fred has opportunity: True or False?
False (0.6321309950802387)
Mrs. Dunwoodee is guilty: True or False?
True (0.9693242313725606)
Mrs. Dunwoodee has mean: True or False?
True (0.9167080509980843)
Mrs. Dunwoodee has motive: True or False?
True (0.9384632725948482)
Mrs. Dunwoodee has opportunity: True or False?
True (0.9458012588547495)
Ricky is guilty: True or False?
True (0.9698996547102765)
Ricky has mean: True or False?
True (0.9031234421019929)
Ricky has motive: True or False?
True (0.9639160647221925)
Ricky has opportunity: True or False?
True (0.9571978443343412)
### Brad
- mean: True (0.9319595674053855)
- motive: True (0.9369805475192257)
- opportunity: True (0.9832788702399727)

### Fred
- mean: False (0.052424489087402715)
- motive: False (0.7665304747562915)
- opportunity: False (0.6321309950802387)

### Mrs. Dunwoodee
- mean: False (0.08329194900191572)
- motive: False (0.061536727405151814)
- opportunity: False (0.05419874114525047)

### Ricky
- mean: False (0.09687655789800709)
- motive: False (0.03608393527780751)
- opportunity: False (0.042802155665658814)

The culprit is Brad.
In fact, it is Fred.
## 5minutemystery-the-necklace
Aunt Mary is guilty: True or False?
True (0.9675331712558415)
Aunt Mary has mean: True or False?
True (0.9008791478232747)
Aunt Mary has motive: True or False?
True (0.9318356525033217)
Aunt Mary has opportunity: True or False?
True (0.9527502639818524)
Dad is guilty: True or False?
True (0.9902538653604824)
Dad has mean: True or False?
True (0.9237300750192418)
Dad has motive: True or False?
True (0.985057294041011)
Dad has opportunity: True or False?
True (0.9354645628936168)
Mom is guilty: True or False?
True (0.9853984116501415)
Mom has mean: True or False?
True (0.8824278665848695)
Mom has motive: True or False?
True (0.9817357655259503)
Mom has opportunity: True or False?
True (0.9214990117475544)
Uncle Henry is guilty: True or False?
True (0.9630224717531983)
Uncle Henry has mean: True or False?
True (0.9543079730970608)
Uncle Henry has motive: True or False?
True (0.9696132548883896)
Uncle Henry has opportunity: True or False?
True (0.9739436503754907)
Uncle John is guilty: True or False?
True (0.9678385865075065)
Uncle John has mean: True or False?
True (0.9658351545108645)
Uncle John has motive: True or False?
True (0.972204327764203)
Uncle John has opportunity: True or False?
True (0.9762653119462512)
### Aunt Mary
- mean: False (0.09912085217672528)
- motive: False (0.06816434749667832)
- opportunity: False (0.04724973601814764)

### Dad
- mean: False (0.07626992498075824)
- motive: False (0.014942705958989055)
- opportunity: False (0.06453543710638321)

### Mom
- mean: False (0.11757213341513051)
- motive: False (0.01826423447404968)
- opportunity: False (0.07850098825244556)

### Uncle Henry
- mean: False (0.045692026902939165)
- motive: False (0.030386745111610436)
- opportunity: False (0.026056349624509312)

### Uncle John
- mean: True (0.9658351545108645)
- motive: True (0.972204327764203)
- opportunity: True (0.9762653119462512)

The culprit is Uncle John.
In fact, it is Dad.
## 5minutemystery-the-purloined-wallet
Bill Buchanan is guilty: True or False?
True (0.9022657265573043)
Bill Buchanan has mean: True or False?
True (0.9014011626580862)
Bill Buchanan has motive: True or False?
True (1.469602350642461)
Bill Buchanan has opportunity: True or False?
True (0.9082930095862076)
Carson Thomson is guilty: True or False?
True (0.9372107409794781)
Carson Thomson has mean: True or False?
True (0.9353465445225602)
Carson Thomson has motive: True or False?
True (0.8467044802440825)
Carson Thomson has opportunity: True or False?
True (0.9095862487848758)
Cooper is guilty: True or False?
True (0.874934615163517)
Cooper has mean: True or False?
True (0.5964331434971528)
Cooper has motive: True or False?
True (0.85729086409805)
Cooper has opportunity: True or False?
True (0.9541373270174538)
Map: 100%|██████████| 203/203 [3:29:16<00:00, 47.25s/ examples]Map: 100%|██████████| 203/203 [3:29:16<00:00, 61.86s/ examples]
David Nader is guilty: True or False?
True (0.8643104392003704)
David Nader has mean: True or False?
True (0.8944211616820568)
David Nader has motive: True or False?
True (0.8050197941712954)
David Nader has opportunity: True or False?
True (0.9666631213158693)
Vincent Garcia is guilty: True or False?
True (0.8812066389307215)
Vincent Garcia has mean: True or False?
True (0.9079670935046645)
Vincent Garcia has motive: True or False?
True (0.8524448242555318)
Vincent Garcia has opportunity: True or False?
True (0.9233162440500982)
### Bill Buchanan
- mean: True (0.9014011626580862)
- motive: True (1.469602350642461)
- opportunity: True (0.9082930095862076)

### Carson Thomson
- mean: False (0.06465345547743984)
- motive: False (0.1532955197559175)
- opportunity: False (0.09041375121512418)

### Cooper
- mean: False (0.4035668565028472)
- motive: False (0.14270913590195)
- opportunity: False (0.045862672982546204)

### David Nader
- mean: False (0.10557883831794324)
- motive: False (0.19498020582870457)
- opportunity: False (0.03333687868413071)

### Vincent Garcia
- mean: False (0.09203290649533546)
- motive: False (0.1475551757444682)
- opportunity: False (0.07668375594990184)

The culprit is Bill Buchanan.
In fact, it is David Nader.
Solved 52 out of 203.
