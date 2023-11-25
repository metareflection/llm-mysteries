## This run represents modified prompts to see how the performance of llama2 70b will be
Updated the prompts in `markers.py` to be:
- preambule = 'Here is a mystery story. Your role is to find who is the culprit. Make sure to analyze the story in detail and construct a timeline of main events that occur in the story'
- postambule = 'Now, think step-by-step on who the culprit is using your constructed timeline. Can you tell me who is the culprit?'

============= OUTPUT STARTS HERE=========
nohup: ignoring input
/home/sraja/mambaforge/envs/llm-mysteries/lib/python3.10/site-packages/transformers/models/auto/auto_factory.py:472: FutureWarning: The `use_auth_token` argument is deprecated and will be removed in v5 of Transformers. Please use `token` instead.
  warnings.warn(

Loading checkpoint shards:   0%|          | 0/15 [00:00<?, ?it/s]
Loading checkpoint shards:   7%|▋         | 1/15 [00:01<00:24,  1.77s/it]
Loading checkpoint shards:  13%|█▎        | 2/15 [00:03<00:21,  1.67s/it]
Loading checkpoint shards:  20%|██        | 3/15 [00:04<00:19,  1.59s/it]
Loading checkpoint shards:  27%|██▋       | 4/15 [00:06<00:18,  1.66s/it]
Loading checkpoint shards:  33%|███▎      | 5/15 [00:08<00:18,  1.81s/it]
Loading checkpoint shards:  40%|████      | 6/15 [00:10<00:16,  1.82s/it]
Loading checkpoint shards:  47%|████▋     | 7/15 [00:12<00:14,  1.79s/it]
Loading checkpoint shards:  53%|█████▎    | 8/15 [00:14<00:12,  1.80s/it]
Loading checkpoint shards:  60%|██████    | 9/15 [00:15<00:10,  1.77s/it]
Loading checkpoint shards:  67%|██████▋   | 10/15 [00:17<00:08,  1.74s/it]
Loading checkpoint shards:  73%|███████▎  | 11/15 [00:19<00:06,  1.74s/it]
Loading checkpoint shards:  80%|████████  | 12/15 [00:21<00:05,  1.76s/it]
Loading checkpoint shards:  87%|████████▋ | 13/15 [00:22<00:03,  1.73s/it]
Loading checkpoint shards:  93%|█████████▎| 14/15 [00:24<00:01,  1.70s/it]
Loading checkpoint shards: 100%|██████████| 15/15 [00:24<00:00,  1.23s/it]
Loading checkpoint shards: 100%|██████████| 15/15 [00:24<00:00,  1.63s/it]
/home/sraja/mambaforge/envs/llm-mysteries/lib/python3.10/site-packages/dill/_dill.py:412: PicklingWarning: Cannot locate reference to <class '_ctypes.PyCFuncPtrType'>.
  StockPickler.save(self, obj, save_persistent_id)
/home/sraja/mambaforge/envs/llm-mysteries/lib/python3.10/site-packages/dill/_dill.py:412: PicklingWarning: Cannot pickle <class '_ctypes.PyCFuncPtrType'>: _ctypes.PyCFuncPtrType has recursive self-references that trigger a RecursionError.
  StockPickler.save(self, obj, save_persistent_id)
Parameter 'function'=<function processCase at 0x7f8e680f35b0> of the transform datasets.arrow_dataset.Dataset._map_single couldn't be hashed properly, a random hash was used instead. Make sure your transforms and parameters are serializable with pickle or dill for the dataset fingerprinting and caching to work. If you reuse this transform, the caching mechanism will consider it to be different from the previous calls and recompute everything. This warning is only showed once. Subsequent hashing failures won't be showed.

Map:   0%|          | 0/203 [00:00<?, ? examples/s]
Map:   0%|          | 1/203 [01:17<4:22:14, 77.89s/ examples]
Map:   1%|          | 2/203 [02:20<3:50:05, 68.68s/ examples]
Map:   1%|▏         | 3/203 [03:30<3:51:08, 69.34s/ examples]## 5minutemystery-who-let-the-frogs-out
Kyle Kravetsky is guilty: True or False?
True (0.8812066389307215)
Kyle Kravetsky is not guilty: True or False?
True (0.8883720049821552)
Kyle Kravetsky has mean: True or False?
True (0.873646672673131)
Kyle Kravetsky has no mean: True or False?
True (0.7170118721569225)
Kyle Kravetsky has motive: True or False?
True (0.9708540445899615)
Kyle Kravetsky has no motive: True or False?
True (0.7931059536445917)
Kyle Kravetsky has opportunity: True or False?
True (0.8444089912414552)
Kyle Kravetsky has no opportunity: True or False?
True (0.6252092625510083)
Marnie Pepper is guilty: True or False?
True (0.9392480858026054)
Marnie Pepper is not guilty: True or False?
True (0.9590010064506653)
Marnie Pepper has mean: True or False?
True (0.8875949368741688)
Marnie Pepper has no mean: True or False?
True (0.8122724274380432)
Marnie Pepper has motive: True or False?
True (0.9723097678630687)
Marnie Pepper has no motive: True or False?
True (0.9127477403975288)
Marnie Pepper has opportunity: True or False?
True (0.8710367026584496)
Marnie Pepper has no opportunity: True or False?
True (0.6918097672776748)
Matilda Robbens is guilty: True or False?
True (0.9467937951644804)
Matilda Robbens is not guilty: True or False?
True (0.9095863097773887)
Matilda Robbens has mean: True or False?
True (0.7711548682745724)
Matilda Robbens has no mean: True or False?
True (0.7446563751413027)
Matilda Robbens has motive: True or False?
True (0.9802430864191416)
Matilda Robbens has no motive: True or False?
True (0.8175744430556572)
Matilda Robbens has opportunity: True or False?
True (0.85729086409805)
Matilda Robbens has no opportunity: True or False?
True (0.6325027218909103)
Sergio Ramos is guilty: True or False?
True (0.9628131975124238)
Sergio Ramos is not guilty: True or False?
True (0.9435559526996434)
Sergio Ramos has mean: True or False?
True (0.9005298052062833)
Sergio Ramos has no mean: True or False?
True (0.8068526417769779)
Sergio Ramos has motive: True or False?
True (0.9647224545627199)
Sergio Ramos has no motive: True or False?
True (0.8991214023999228)
Sergio Ramos has opportunity: True or False?
True (0.9403530352223053)
Sergio Ramos has no opportunity: True or False?
True (0.7431679939957333)
### Kyle Kravetsky
- mean: False (0.2829881278430775)
- motive: False (0.2068940463554083)
- opportunity: False (0.3747907374489917)

### Marnie Pepper
- mean: True (0.8875949368741688)
- motive: True (0.9723097678630687)
- opportunity: True (0.8710367026584496)

### Matilda Robbens
- mean: False (0.2553436248586973)
- motive: False (0.18242555694434281)
- opportunity: False (0.3674972781090897)

### Sergio Ramos
- mean: False (0.1931473582230221)
- motive: False (0.10087859760007722)
- opportunity: False (0.2568320060042667)

The culprit is Marnie Pepper.
In fact, it is Matilda Robbens.
## 5minutemystery-uncle-buck-field-trip
Collin is guilty: True or False?
True (0.9390248079664695)
Collin is not guilty: True or False?
True (0.9552356617277232)
Collin has mean: True or False?
True (0.7988152492192591)
Collin has no mean: True or False?
True (0.9281487460975983)
Collin has motive: True or False?
True (0.9796676048170913)
Collin has no motive: True or False?
True (0.9465966835599983)
Collin has opportunity: True or False?
True (0.981021999947924)
Collin has no opportunity: True or False?
True (0.9651191233711941)
Erica is guilty: True or False?
True (0.8951566249612815)
Erica is not guilty: True or False?
True (0.8987665204865408)
Erica has mean: True or False?
True (0.7217432334405754)
Erica has no mean: True or False?
True (0.8244619332958376)
Erica has motive: True or False?
True (0.9733929040540585)
Erica has no motive: True or False?
True (0.9102267057681164)
Erica has opportunity: True or False?
True (0.9339146041314464)
Erica has no opportunity: True or False?
True (0.8787311338092536)
Rory is guilty: True or False?
True (0.9346342066470359)
Rory is not guilty: True or False?
True (0.9490118621693758)
Rory has mean: True or False?
True (0.8175744430556572)
Rory has no mean: True or False?
True (0.9108630396247971)
Rory has motive: True or False?
True (0.9669764642537568)
Rory has no motive: True or False?
True (0.8683809699466569)
Rory has opportunity: True or False?
True (0.9629528509146777)
Rory has no opportunity: True or False?
True (0.9082930095862076)
Rusty is guilty: True or False?
True (0.9424007531919156)
Rusty is not guilty: True or False?
True (0.9515039936355008)
Rusty has mean: True or False?
True (0.8140528237853677)
Rusty has no mean: True or False?
True (0.9127477403975288)
Rusty has motive: True or False?
True (0.9773275249708122)
Rusty has no motive: True or False?
True (0.8899121304559661)
Rusty has opportunity: True or False?
True (0.9522199020698944)
Rusty has no opportunity: True or False?
True (0.878314250659373)
### Collin
- mean: True (0.7988152492192591)
- motive: True (0.9796676048170913)
- opportunity: True (0.981021999947924)

### Erica
- mean: True (0.7217432334405754)
- motive: False (0.08977329423188363)
- opportunity: False (0.1212688661907464)

### Rory
- mean: True (0.8175744430556572)
- motive: False (0.13161903005334308)
- opportunity: False (0.09170699041379238)

### Rusty
- mean: True (0.8140528237853677)
- motive: False (0.11008786954403393)
- opportunity: False (0.12168574934062704)

The culprit is Collin.
In fact, it is Rory.
## 5minutemystery-mystery-of-the-white-hats
Captain Stark is guilty: True or False?
True (0.9500415344497218)
Captain Stark is not guilty: True or False?
True (0.9541373270174538)
Captain Stark has mean: True or False?
True (0.9127478016020363)
Captain Stark has no mean: True or False?
True (0.7386690954574974)
Captain Stark has motive: True or False?
True (0.9621076000160501)
Captain Stark has no motive: True or False?
True (0.8316905440184192)
Captain Stark has opportunity: True or False?
True (0.8795611817678315)
Captain Stark has no opportunity: True or False?
True (0.7025300310583819)
Chet is guilty: True or False?
True (0.9437636147996928)
Chet is not guilty: True or False?
True (0.9422946582938823)
Chet has mean: True or False?
True (0.8638517255508926)
Chet has no mean: True or False?
False (0.5185461538431656)
Chet has motive: True or False?
True (0.9695556762577888)
Chet has no motive: True or False?
True (0.8638516611889259)
Chet has opportunity: True or False?
True (0.8872045854516336)
Chet has no opportunity: True or False?
True (0.6141626144170799)
Doug is guilty: True or False?
True (0.8980535302052036)
Doug is not guilty: True or False?
True (0.9334308488586655)
Doug has mean: True or False?
True (0.7074047371961694)
Doug has no mean: True or False?
False (0.6076631662366868)
Doug has motive: True or False?
True (0.9599126594957205)
Doug has no motive: True or False?
True (0.7711548682745724)
Doug has opportunity: True or False?
True (0.72951977676791)
Doug has no opportunity: True or False?
False (0.5165954111147137)
Ernie is guilty: True or False?
True (0.8044059309478723)
Ernie is not guilty: True or False?
True (0.8494724067948436)
Ernie has mean: True or False?
True (0.8140528237853677)
Ernie has no mean: True or False?
False (0.5438324636094939)
Ernie has motive: True or False?
True (0.8918110736745599)
Ernie has no motive: True or False?
True (0.6540113633452196)
Ernie has opportunity: True or False?
True (0.7662936378892937)
Ernie has no opportunity: True or False?
False (0.5409238326546766)
### Captain Stark
- mean: False (0.26133090454250263)
- motive: False (0.16830945598158076)
- opportunity: False (0.29746996894161815)

### Chet
- mean: True (0.8638517255508926)
- motive: False (0.13614833881107413)
- opportunity: False (0.38583738558292013)

### Doug
- mean: True (0.7074047371961694)
- motive: False (0.22884513172542764)
- opportunity: True (0.72951977676791)

### Ernie
- mean: True (0.8140528237853677)
- motive: True (0.8918110736745599)
- opportunity: True (0.7662936378892937)

The culprit is Ernie.
In fact, it is Chet.
## 5minutemystery-the-missing-popcorn
Private First Class Dicky Mosier is guilty: True or False?
True (0.9647224545627199)
Private First Class Dicky Mosier is not guilty: True or False?

Map:   2%|▏         | 4/203 [04:30<3:38:02, 65.74s/ examples]
Map:   2%|▏         | 5/203 [05:49<3:52:59, 70.60s/ examples]True (0.9594592463344039)
Private First Class Dicky Mosier has mean: True or False?
True (0.9635062220717456)
Private First Class Dicky Mosier has no mean: True or False?
True (0.9694401626921336)
Private First Class Dicky Mosier has motive: True or False?
True (0.9865458604248776)
Private First Class Dicky Mosier has no motive: True or False?
True (0.9756698013402983)
Private First Class Dicky Mosier has opportunity: True or False?
True (0.9707432981083896)
Private First Class Dicky Mosier has no opportunity: True or False?
True (0.9720986492264091)
Private Joe Locke is guilty: True or False?
True (0.9145963197706802)
Private Joe Locke is not guilty: True or False?
True (0.9516839395409852)
Private Joe Locke has mean: True or False?
True (0.8951566249612815)
Private Joe Locke has no mean: True or False?
True (0.9095862487848758)
Private Joe Locke has motive: True or False?
True (0.9686195851543489)
Private Joe Locke has no motive: True or False?
True (0.9707987303464544)
Private Joe Locke has opportunity: True or False?
True (0.9418684262191025)
Private Joe Locke has no opportunity: True or False?
True (0.9645892964498279)
Specialist Fifth Class Ron Henson is guilty: True or False?
True (0.9449946880768697)
Specialist Fifth Class Ron Henson is not guilty: True or False?
True (0.9433475737015985)
Specialist Fifth Class Ron Henson has mean: True or False?
True (0.9460011122282159)
Specialist Fifth Class Ron Henson has no mean: True or False?
True (0.9606574760904091)
Specialist Fifth Class Ron Henson has motive: True or False?
True (0.9795897010514905)
Specialist Fifth Class Ron Henson has no motive: True or False?
True (0.9558166865608263)
Specialist Fifth Class Ron Henson has opportunity: True or False?
True (0.9536218061663073)
Specialist Fifth Class Ron Henson has no opportunity: True or False?
True (0.9334308488586655)
Specialist Fourth Class Patrick Macnamara is guilty: True or False?
True (0.9401336308904421)
Specialist Fourth Class Patrick Macnamara is not guilty: True or False?
True (0.934872446722342)
Specialist Fourth Class Patrick Macnamara has mean: True or False?
True (0.913058338092082)
Specialist Fourth Class Patrick Macnamara has no mean: True or False?
True (0.9496693599006181)
Specialist Fourth Class Patrick Macnamara has motive: True or False?
True (0.9548162813994148)
Specialist Fourth Class Patrick Macnamara has no motive: True or False?
True (0.9246877442701001)
Specialist Fourth Class Patrick Macnamara has opportunity: True or False?
True (0.8906751877407573)
Specialist Fourth Class Patrick Macnamara has no opportunity: True or False?
True (0.8683809699466569)
### Private First Class Dicky Mosier
- mean: True (0.9635062220717456)
- motive: False (0.024330198659701652)
- opportunity: True (0.9707432981083896)

### Private Joe Locke
- mean: True (0.8951566249612815)
- motive: True (0.9686195851543489)
- opportunity: True (0.9418684262191025)

### Specialist Fifth Class Ron Henson
- mean: True (0.9460011122282159)
- motive: False (0.0441833134391737)
- opportunity: False (0.06656915114133455)

### Specialist Fourth Class Patrick Macnamara
- mean: True (0.913058338092082)
- motive: False (0.07531225572989986)
- opportunity: False (0.13161903005334308)

The culprit is Private Joe Locke.
In fact, it is Private Joe Locke.
## 5minutemystery-mystery-on-the-moor
Jack MacGinnis is guilty: True or False?
True (0.8633915828320894)
Jack MacGinnis is not guilty: True or False?
True (0.8729984172167968)
Jack MacGinnis has mean: True or False?
True (0.8838389494391541)
Jack MacGinnis has no mean: True or False?
True (0.8887587777822111)
Jack MacGinnis has motive: True or False?
True (0.9444848881002107)
Jack MacGinnis has no motive: True or False?
True (0.8311430831606665)
Jack MacGinnis has opportunity: True or False?
True (0.8433797899747144)
Jack MacGinnis has no opportunity: True or False?
True (0.7704647687904915)
James Macready is guilty: True or False?
True (0.9476239083642972)
James Macready is not guilty: True or False?
True (0.9673794510762798)
James Macready has mean: True or False?
True (0.9284088027271398)
James Macready has no mean: True or False?
True (0.9273632783787477)
James Macready has motive: True or False?
True (0.9641867858895684)
James Macready has no motive: True or False?
True (0.8860265005470086)
James Macready has opportunity: True or False?
True (0.9466953276900992)
James Macready has no opportunity: True or False?
True (0.8247443993706964)
Samuel Doone is guilty: True or False?
True (0.9372107968415931)
Samuel Doone is not guilty: True or False?
True (0.9313377150989219)
Samuel Doone has mean: True or False?
True (0.8210441512234701)
Samuel Doone has no mean: True or False?
True (0.8494724067948436)
Samuel Doone has motive: True or False?
True (0.9594592463344039)
Samuel Doone has no motive: True or False?
True (0.9032942081209032)
Samuel Doone has opportunity: True or False?
True (0.869271276026005)
Samuel Doone has no opportunity: True or False?
True (0.8169911556077801)
Tom Jenkins is guilty: True or False?
True (0.9238675252821831)
Tom Jenkins is not guilty: True or False?
True (0.9556514027264735)
Tom Jenkins has mean: True or False?
True (0.8822250371924163)
Tom Jenkins has no mean: True or False?
True (0.879146813094474)
Tom Jenkins has motive: True or False?
True (0.9718859200238344)
Tom Jenkins has no motive: True or False?
True (0.874934615163517)
Tom Jenkins has opportunity: True or False?
True (0.9224823132745662)
Tom Jenkins has no opportunity: True or False?
True (0.842345065078002)
### Jack MacGinnis
- mean: True (0.8838389494391541)
- motive: False (0.16885691683933346)
- opportunity: False (0.22953523120950847)

### James Macready
- mean: False (0.07263672162125234)
- motive: False (0.1139734994529914)
- opportunity: False (0.17525560062930357)

### Samuel Doone
- mean: True (0.8210441512234701)
- motive: True (0.9594592463344039)
- opportunity: True (0.869271276026005)

### Tom Jenkins
- mean: False (0.12085318690552604)
- motive: False (0.125065384836483)
- opportunity: False (0.157654934921998)

The culprit is Samuel Doone.
In fact, it is James Macready.
## 5minutemystery-who-stole-curious-george
Dexter is guilty: True or False?
True (0.8305941261447712)
Dexter is not guilty: True or False?
True (0.892187358563457)
Dexter has mean: True or False?
True (0.7988152492192591)
Dexter has no mean: True or False?
True (0.6584175136252488)
Dexter has motive: True or False?
True (0.9575961815839735)
Dexter has no motive: True or False?
True (0.8887587777822111)
Dexter has opportunity: True or False?
True (0.9531007408873468)
Dexter has no opportunity: True or False?
True (0.7950223052877581)
Mr. Ferguson is guilty: True or False?
True (0.854884620116169)
Mr. Ferguson is not guilty: True or False?
True (0.9396923783210908)
Mr. Ferguson has mean: True or False?
True (0.8895288123486662)
Mr. Ferguson has no mean: True or False?
True (0.8360197583769845)
Mr. Ferguson has motive: True or False?
True (0.9655764090471975)
Mr. Ferguson has no motive: True or False?
True (0.7879311977554747)
Mr. Ferguson has opportunity: True or False?
True (0.9127477403975288)
Mr. Ferguson has no opportunity: True or False?
True (0.6067314814064781)
Mrs. Yee is guilty: True or False?
True (0.6187803740984554)
Mrs. Yee is not guilty: True or False?
True (0.8504685773080045)
Mrs. Yee has mean: True or False?
True (0.6800292132037243)
Mrs. Yee has no mean: True or False?
False (0.503906199448032)
Mrs. Yee has motive: True or False?
True (0.941654147692963)
Mrs. Yee has no motive: True or False?
True (0.7512833387594996)
Mrs. Yee has opportunity: True or False?
True (0.7779753136455794)
Mrs. Yee has no opportunity: True or False?
False (0.503906199448032)
Skyler is guilty: True or False?
True (0.9374402785760423)
Skyler is not guilty: True or False?
True (0.9532750262379774)
Skyler has mean: True or False?
True (0.8701565822173906)
Skyler has no mean: True or False?
True (0.8261514850267767)
Skyler has motive: True or False?
True (0.9789956218205105)
Skyler has no motive: True or False?
True (0.9351098557348285)
Skyler has opportunity: True or False?
True (0.9181872635464632)
Skyler has no opportunity: True or False?

Map:   3%|▎         | 6/203 [07:22<4:16:09, 78.02s/ examples]
Map:   3%|▎         | 7/203 [08:39<4:14:23, 77.88s/ examples]
Map:   4%|▍         | 8/203 [09:33<3:48:41, 70.36s/ examples]True (0.8152325155686644)
### Dexter
- mean: False (0.3415824863747512)
- motive: False (0.11124122221778887)
- opportunity: False (0.20497769471224192)

### Mr. Ferguson
- mean: False (0.1639802416230155)
- motive: False (0.2120688022445253)
- opportunity: False (0.39326851859352185)

### Mrs. Yee
- mean: True (0.6800292132037243)
- motive: True (0.941654147692963)
- opportunity: True (0.7779753136455794)

### Skyler
- mean: False (0.1738485149732233)
- motive: False (0.06489014426517148)
- opportunity: False (0.18476748443133562)

The culprit is Mrs. Yee.
In fact, it is Dexter.
## 5minutemystery-the-saxophones-ghost
Building Manager is guilty: True or False?
True (0.9894906286737151)
Building Manager is not guilty: True or False?
True (0.9511421913058572)
Building Manager has mean: True or False?
True (0.905989824801558)
Building Manager has no mean: True or False?
True (0.908941745727715)
Building Manager has motive: True or False?
True (0.9889064429708829)
Building Manager has no motive: True or False?
True (0.9527503243194666)
Building Manager has opportunity: True or False?
True (0.9648551350350516)
Building Manager has no opportunity: True or False?
True (0.8591918406281239)
Eric is guilty: True or False?
True (0.988038897570479)
Eric is not guilty: True or False?
True (0.972830772390074)
Eric has mean: True or False?
True (0.7898827135821628)
Eric has no mean: True or False?
True (0.8499711693725173)
Eric has motive: True or False?
True (0.9929609300067086)
Eric has no motive: True or False?
True (0.9346342066470359)
Eric has opportunity: True or False?
True (0.9520419225082909)
Eric has no opportunity: True or False?
True (0.8080671968507699)
Lenny is guilty: True or False?
True (0.9944773316650645)
Lenny is not guilty: True or False?
True (0.988842010705056)
Lenny has mean: True or False?
True (0.8423451152856819)
Lenny has no mean: True or False?
True (0.8031737798924701)
Lenny has motive: True or False?
True (0.9898106456437191)
Lenny has no motive: True or False?
True (0.9623913759339153)
Lenny has opportunity: True or False?
True (0.960804880888677)
Lenny has no opportunity: True or False?
True (0.8875948773562923)
Red is guilty: True or False?
True (0.9870296120305199)
Red is not guilty: True or False?
True (0.9697854513237307)
Red has mean: True or False?
True (0.873646620599733)
Red has no mean: True or False?
True (0.8494724067948436)
Red has motive: True or False?
True (0.9859904643821331)
Red has no motive: True or False?
True (0.936980484689786)
Red has opportunity: True or False?
True (0.9385759849623091)
Red has no opportunity: True or False?
True (0.8656789607733094)
### Building Manager
- mean: True (0.905989824801558)
- motive: False (0.0472496756805334)
- opportunity: False (0.14080815937187607)

### Eric
- mean: True (0.7898827135821628)
- motive: False (0.06536579335296411)
- opportunity: False (0.1919328031492301)

### Lenny
- mean: True (0.8423451152856819)
- motive: True (0.9898106456437191)
- opportunity: True (0.960804880888677)

### Red
- mean: False (0.1505275932051564)
- motive: False (0.06301951531021399)
- opportunity: False (0.1343210392266906)

The culprit is Lenny.
In fact, it is Building Manager.
## 5minutemystery-who-shot-mom
Dad is guilty: True or False?
True (0.8944211616820568)
Dad is not guilty: True or False?
True (0.9222025890552223)
Dad has mean: True or False?
True (0.8879840376027315)
Dad has no mean: True or False?
True (0.7620701143808404)
Dad has motive: True or False?
True (0.9693821664094352)
Dad has no motive: True or False?
True (0.9171543708147702)
Dad has opportunity: True or False?
True (0.9488224997202508)
Dad has no opportunity: True or False?
True (0.7819972591886313)
Randy is guilty: True or False?
True (0.9177460069915372)
Randy is not guilty: True or False?
True (0.9531880038608308)
Randy has mean: True or False?
True (0.8509647293237851)
Randy has no mean: True or False?
True (0.7225270177274575)
Randy has motive: True or False?
True (0.990839004835608)
Randy has no motive: True or False?
True (0.8891444205417208)
Randy has opportunity: True or False?
True (0.9672868242254096)
Randy has no opportunity: True or False?
True (0.8216173667955227)
Roger is guilty: True or False?
True (0.8647679145346777)
Roger is not guilty: True or False?
True (0.9095863097773887)
Roger has mean: True or False?
True (0.7786493288700866)
Roger has no mean: True or False?
True (0.7752646804088963)
Roger has motive: True or False?
True (0.9884696011429079)
Roger has no motive: True or False?
True (0.9281487460975983)
Roger has opportunity: True or False?
True (0.9740426532811326)
Roger has no opportunity: True or False?
True (0.8529354946829077)
Rory is guilty: True or False?
True (0.9237300750192418)
Rory is not guilty: True or False?
True (0.9514138119240159)
Rory has mean: True or False?
True (0.8856314413364714)
Rory has no mean: True or False?
True (0.7772998201448375)
Rory has motive: True or False?
True (0.9897513984446356)
Rory has no motive: True or False?
True (0.9079671476237222)
Rory has opportunity: True or False?
True (0.976310552041449)
Rory has no opportunity: True or False?
True (0.8670357473609658)
### Dad
- mean: False (0.23792988561915962)
- motive: False (0.08284562918522975)
- opportunity: False (0.21800274081136872)

### Randy
- mean: False (0.27747298227254247)
- motive: False (0.11085557945827917)
- opportunity: False (0.17838263320447734)

### Roger
- mean: True (0.7786493288700866)
- motive: True (0.9884696011429079)
- opportunity: True (0.9740426532811326)

### Rory
- mean: False (0.22270017985516255)
- motive: False (0.09203285237627779)
- opportunity: False (0.13296425263903422)

The culprit is Roger.
In fact, it is Randy.
## 5minutemystery-finding-the-flower-fund
James Faust is guilty: True or False?
True (0.9008790874146224)
James Faust is not guilty: True or False?
True (0.894973220907352)
James Faust has mean: True or False?
True (0.9354645628936168)
James Faust has no mean: True or False?
True (0.7606506998655483)
James Faust has motive: True or False?
True (0.9181873182746905)
James Faust has no motive: True or False?
True (0.8529354946829077)
James Faust has opportunity: True or False?
True (0.8795611817678315)
James Faust has no opportunity: True or False?
True (0.5813030649269245)
Justin Thorn is guilty: True or False?
True (0.904313027820426)
Justin Thorn is not guilty: True or False?
True (0.8973359441831076)
Justin Thorn has mean: True or False?
True (0.7049732238008671)
Justin Thorn has no mean: True or False?
True (0.7371581892031299)
Justin Thorn has motive: True or False?
True (0.8854335555838845)
Justin Thorn has no motive: True or False?
True (0.8620035048683017)
Justin Thorn has opportunity: True or False?
True (0.9564718616162037)
Justin Thorn has no opportunity: True or False?
True (0.8386797310322072)
Lincoln Smith is guilty: True or False?
True (0.8679338697256817)
Lincoln Smith is not guilty: True or False?
True (0.9522199623739209)
Lincoln Smith has mean: True or False?
True (0.7599387683150569)
Lincoln Smith has no mean: True or False?
True (0.8568122940392877)
Lincoln Smith has motive: True or False?
False (1.6827630606855486)
Lincoln Smith has no motive: True or False?
True (0.9227612629515897)
Lincoln Smith has opportunity: True or False?
True (0.9100670238942131)
Lincoln Smith has no opportunity: True or False?
True (0.8289388437432279)
Linda Hinton is guilty: True or False?
True (0.8539127077831877)
Linda Hinton is not guilty: True or False?
True (0.8705972382426559)
Linda Hinton has mean: True or False?
True (0.8140528237853677)
Linda Hinton has no mean: True or False?
True (0.6757646168022439)
Linda Hinton has motive: True or False?
True (0.8349459127213729)
Linda Hinton has no motive: True or False?
True (0.6766198919456847)
Linda Hinton has opportunity: True or False?
True (0.8198932995357624)
Linda Hinton has no opportunity: True or False?
True (0.5640984675176304)
### James Faust
- mean: False (0.23934930013445166)
- motive: False (0.14706450531709225)
- opportunity: False (0.4186969350730755)

### Justin Thorn
- mean: True (0.7049732238008671)
- motive: True (0.8854335555838845)
- opportunity: True (0.9564718616162037)


Map:   4%|▍         | 9/203 [10:19<3:22:42, 62.69s/ examples]
Map:   5%|▍         | 10/203 [11:23<3:22:48, 63.05s/ examples]
Map:   5%|▌         | 11/203 [12:27<3:22:08, 63.17s/ examples]### Lincoln Smith
- mean: True (0.7599387683150569)
- motive: False (1.6827630606855486)
- opportunity: False (0.1710611562567721)

### Linda Hinton
- mean: False (0.32423538319775613)
- motive: False (0.3233801080543153)
- opportunity: False (0.4359015324823696)

The culprit is Justin Thorn.
In fact, it is Lincoln Smith.
## 5minutemystery-map-of-the-traitor
Benjamin is guilty: True or False?
True (0.9531007408873468)
Benjamin is not guilty: True or False?
True (0.9677776702396809)
Benjamin has mean: True or False?
True (0.7839884808423031)
Benjamin has no mean: True or False?
True (0.8267118326419537)
Benjamin has motive: True or False?
True (0.9399133323582882)
Benjamin has no motive: True or False?
True (0.9537942396657707)
Benjamin has opportunity: True or False?
True (0.9244152304846833)
Benjamin has no opportunity: True or False?
True (0.9102267057681164)
Edward is guilty: True or False?
True (0.9759464267558225)
Edward is not guilty: True or False?
True (0.976310552041449)
Edward has mean: True or False?
True (0.7386690954574974)
Edward has no mean: True or False?
True (0.8289387819824735)
Edward has motive: True or False?
True (0.9758545755283039)
Edward has no motive: True or False?
True (0.9702398769132671)
Edward has opportunity: True or False?
True (0.9355823382423648)
Edward has no opportunity: True or False?
True (0.9205042693180057)
Jonathan is guilty: True or False?
True (0.9716717007848752)
Jonathan is not guilty: True or False?
True (0.983149946614081)
Jonathan has mean: True or False?
True (0.9196425103002197)
Jonathan has no mean: True or False?
True (0.9121235591541035)
Jonathan has motive: True or False?
True (0.9808393129553152)
Jonathan has no motive: True or False?
True (0.9559813721912603)
Jonathan has opportunity: True or False?
True (0.9505947242503305)
Jonathan has no opportunity: True or False?
True (0.9263037480179213)
Lucius is guilty: True or False?
True (0.9648551925449009)
Lucius is not guilty: True or False?
True (0.9590009457171959)
Lucius has mean: True or False?
True (0.9309620852900756)
Lucius has no mean: True or False?
True (0.8864204283224634)
Lucius has motive: True or False?
True (0.9718859797630299)
Lucius has no motive: True or False?
True (0.9539660824292815)
Lucius has opportunity: True or False?
True (0.9196425651151865)
Lucius has no opportunity: True or False?
True (0.9036349079321685)
### Benjamin
- mean: True (0.7839884808423031)
- motive: True (0.9399133323582882)
- opportunity: True (0.9244152304846833)

### Edward
- mean: True (0.7386690954574974)
- motive: False (0.029760123086732926)
- opportunity: False (0.07949573068199434)

### Jonathan
- mean: False (0.08787644084589652)
- motive: False (0.04401862780873966)
- opportunity: False (0.07369625198207874)

### Lucius
- mean: False (0.11357957167753663)
- motive: False (0.04603391757071851)
- opportunity: False (0.0963650920678315)

The culprit is Benjamin.
In fact, it is Jonathan.
## 5minutemystery-the-crusaders-robe
Captain Fosters is guilty: True or False?
True (0.9851575496109519)
Captain Fosters is not guilty: True or False?
True (0.9853843448803574)
Captain Fosters has mean: True or False?
True (0.9594592463344039)
Captain Fosters has no mean: True or False?
True (0.9546474221708894)
Captain Fosters has motive: True or False?
True (0.9946255086819855)
Captain Fosters has no motive: True or False?
True (0.985552132278138)
Captain Fosters has opportunity: True or False?
True (0.9739437102411692)
Captain Fosters has no opportunity: True or False?
True (0.9498557456415421)
Godefroi is guilty: True or False?
True (0.9623205675054309)
Godefroi is not guilty: True or False?
True (0.9840630297933298)
Godefroi has mean: True or False?
True (0.963368656065788)
Godefroi has no mean: True or False?
True (0.9388007508488514)
Godefroi has motive: True or False?
True (0.9852430220637501)
Godefroi has no motive: True or False?
True (0.9789554468203624)
Godefroi has opportunity: True or False?
True (0.972309708097824)
Godefroi has no opportunity: True or False?
True (0.9485372901378627)
Morgan Grant is guilty: True or False?
True (0.9590009457171959)
Morgan Grant is not guilty: True or False?
True (0.9596109393754703)
Morgan Grant has mean: True or False?
True (0.8204694405411458)
Morgan Grant has no mean: True or False?
True (0.770464837675413)
Morgan Grant has motive: True or False?
True (0.9876400824622509)
Morgan Grant has no motive: True or False?
True (0.9556514632478168)
Morgan Grant has opportunity: True or False?
True (0.9559813152103319)
Morgan Grant has no opportunity: True or False?
True (0.9012274173198201)
Sir Francis Walters is guilty: True or False?
True (0.9666631825345839)
Sir Francis Walters is not guilty: True or False?
True (0.9680204387474981)
Sir Francis Walters has mean: True or False?
True (0.9291837815043049)
Sir Francis Walters has no mean: True or False?
True (0.8679338697256817)
Sir Francis Walters has motive: True or False?
True (0.9902350305140533)
Sir Francis Walters has no motive: True or False?
True (0.9582260855240093)
Sir Francis Walters has opportunity: True or False?
True (0.893681109060862)
Sir Francis Walters has no opportunity: True or False?
True (0.7490872087035162)
### Captain Fosters
- mean: True (0.9594592463344039)
- motive: True (0.9946255086819855)
- opportunity: True (0.9739437102411692)

### Godefroi
- mean: False (0.061199249151148605)
- motive: False (0.021044553179637604)
- opportunity: False (0.0514627098621373)

### Morgan Grant
- mean: False (0.22953516232458704)
- motive: False (0.0443485367521832)
- opportunity: False (0.09877258268017985)

### Sir Francis Walters
- mean: False (0.13206613027431835)
- motive: False (0.04177391447599066)
- opportunity: False (0.2509127912964838)

The culprit is Captain Fosters.
In fact, it is Godefroi.
## 5minutemystery-mr-patricks-history-class
Corporal Tom Patrick is guilty: True or False?
True (0.7541915239138703)
Corporal Tom Patrick is not guilty: True or False?
True (0.8092759828926619)
Corporal Tom Patrick has mean: True or False?
True (0.5679366075542497)
Corporal Tom Patrick has no mean: True or False?
True (0.5926666351772785)
Corporal Tom Patrick has motive: True or False?
True (0.7620701143808404)
Corporal Tom Patrick has no motive: True or False?
False (0.5688949093320547)
Corporal Tom Patrick has opportunity: True or False?
True (0.7905302675820512)
Corporal Tom Patrick has no opportunity: True or False?
False (0.5048826258478675)
Pvt. Billy Calhoun is guilty: True or False?
True (0.8354835531737983)
Pvt. Billy Calhoun is not guilty: True or False?
True (0.7585106418731645)
Pvt. Billy Calhoun has mean: True or False?
True (0.7364006034245382)
Pvt. Billy Calhoun has no mean: True or False?
True (0.7341195403199204)
Pvt. Billy Calhoun has motive: True or False?
True (0.8879840376027315)
Pvt. Billy Calhoun has no motive: True or False?
True (0.7461389980806673)
Pvt. Billy Calhoun has opportunity: True or False?
True (0.7599387683150569)
Pvt. Billy Calhoun has no opportunity: True or False?
True (0.77729988964086)
Pvt. Jack Trueblood is guilty: True or False?
True (0.8762113474663927)
Pvt. Jack Trueblood is not guilty: True or False?
True (0.8469578650997759)
Pvt. Jack Trueblood has mean: True or False?
True (0.7541915239138703)
Pvt. Jack Trueblood has no mean: True or False?
True (0.8128672807499561)
Pvt. Jack Trueblood has motive: True or False?
True (0.8991214023999228)
Pvt. Jack Trueblood has no motive: True or False?
True (0.8104789202520752)
Pvt. Jack Trueblood has opportunity: True or False?
True (0.8134607635851566)
Pvt. Jack Trueblood has no opportunity: True or False?
True (0.8397339530959691)
Sgt. Patrick Culpepper is guilty: True or False?
True (0.8413047772878592)
Sgt. Patrick Culpepper is not guilty: True or False?
True (0.7981867775042927)
Sgt. Patrick Culpepper has mean: True or False?
True (0.7468781552484828)
Sgt. Patrick Culpepper has no mean: True or False?
True (0.5717666110200305)
Sgt. Patrick Culpepper has motive: True or False?
True (0.7599387683150569)
Sgt. Patrick Culpepper has no motive: True or False?
True (0.5165954726976894)
Sgt. Patrick Culpepper has opportunity: True or False?
True (0.7122321792841629)

Map:   6%|▌         | 12/203 [14:25<4:14:16, 79.87s/ examples]
Map:   6%|▋         | 13/203 [15:36<4:04:53, 77.33s/ examples]
Map:   7%|▋         | 14/203 [16:49<3:59:03, 75.89s/ examples]Sgt. Patrick Culpepper has no opportunity: True or False?
True (0.5078118910577802)
### Corporal Tom Patrick
- mean: True (0.5679366075542497)
- motive: True (0.7620701143808404)
- opportunity: True (0.7905302675820512)

### Pvt. Billy Calhoun
- mean: False (0.26588045968007956)
- motive: False (0.2538610019193327)
- opportunity: True (0.7599387683150569)

### Pvt. Jack Trueblood
- mean: True (0.7541915239138703)
- motive: False (0.18952107974792476)
- opportunity: True (0.8134607635851566)

### Sgt. Patrick Culpepper
- mean: False (0.42823338897996954)
- motive: False (0.48340452730231065)
- opportunity: False (0.49218810894221976)

The culprit is Corporal Tom Patrick.
In fact, it is Pvt. Billy Calhoun.
## 5minutemystery-bigfoot-mystery
Burt is guilty: True or False?
True (0.9284088027271398)
Burt is not guilty: True or False?
True (0.9468920823984345)
Burt has mean: True or False?
True (0.7950222460539826)
Burt has no mean: True or False?
True (0.7541915239138703)
Burt has motive: True or False?
True (0.959077715892926)
Burt has no motive: True or False?
True (0.879146760693242)
Burt has opportunity: True or False?
True (0.9124361878432953)
Burt has no opportunity: True or False?
True (0.7527403228571042)
Jerry is guilty: True or False?
True (0.879146760693242)
Jerry is not guilty: True or False?
True (0.9256342684343895)
Jerry has mean: True or False?
True (0.6197014353942354)
Jerry has no mean: True or False?
True (0.5409238326546766)
Jerry has motive: True or False?
True (0.9313377150989219)
Jerry has no motive: True or False?
True (0.7813305798204846)
Jerry has opportunity: True or False?
True (0.8013146490010521)
Jerry has no opportunity: True or False?
True (0.503906199448032)
Leng is guilty: True or False?
True (0.9372107968415931)
Leng is not guilty: True or False?
True (0.9696132548883896)
Leng has mean: True or False?
True (0.8216173667955227)
Leng has no mean: True or False?
True (0.6592954931819778)
Leng has motive: True or False?
True (0.9310874934413855)
Leng has no motive: True or False?
True (0.9343951918693363)
Leng has opportunity: True or False?
True (0.833324548637899)
Leng has no opportunity: True or False?
True (0.6901415551283886)
Winston is guilty: True or False?
True (0.9400235399552953)
Winston is not guilty: True or False?
True (0.9450961367788563)
Winston has mean: True or False?
True (0.7394224480813394)
Winston has no mean: True or False?
True (0.6297745735138451)
Winston has motive: True or False?
True (0.9543079730970608)
Winston has no motive: True or False?
True (0.8397339530959691)
Winston has opportunity: True or False?
True (0.9230391416137353)
Winston has no opportunity: True or False?
True (0.65489470935198)
### Burt
- mean: False (0.24580847608612966)
- motive: False (0.12085323930675795)
- opportunity: False (0.24725967714289576)

### Jerry
- mean: False (0.4590761673453234)
- motive: False (0.2186694201795154)
- opportunity: False (0.49609380055196795)

### Leng
- mean: True (0.8216173667955227)
- motive: True (0.9310874934413855)
- opportunity: True (0.833324548637899)

### Winston
- mean: False (0.37022542648615486)
- motive: False (0.1602660469040309)
- opportunity: False (0.34510529064802)

The culprit is Leng.
In fact, it is Jerry.
## 5minutemystery-missing-movie-money
Billy is guilty: True or False?
True (0.966726063403815)
Billy is not guilty: True or False?
True (0.9736697072900421)
Billy has mean: True or False?
True (0.9237300750192418)
Billy has no mean: True or False?
True (0.9466953276900992)
Billy has motive: True or False?
True (0.9691494704322867)
Billy has no motive: True or False?
True (0.8799743689174987)
Billy has opportunity: True or False?
True (0.9304582506719414)
Billy has no opportunity: True or False?
True (0.8454326455643386)
Cody is guilty: True or False?
True (0.9433475737015985)
Cody is not guilty: True or False?
True (0.9621076000160501)
Cody has mean: True or False?
True (0.9095862487848758)
Cody has no mean: True or False?
True (0.8848377441095496)
Cody has motive: True or False?
True (0.9541373270174538)
Cody has no motive: True or False?
True (0.7975568155246964)
Cody has opportunity: True or False?
True (0.8975157733960666)
Cody has no opportunity: True or False?
True (0.6242935037467142)
Juliet is guilty: True or False?
True (0.9015745518914653)
Juliet is not guilty: True or False?
True (0.9657707197858371)
Juliet has mean: True or False?
True (0.9798997635332343)
Juliet has no mean: True or False?
True (0.893681109060862)
Juliet has motive: True or False?
True (1.2907778613313514)
Juliet has no motive: True or False?
True (0.8062431235779619)
Juliet has opportunity: True or False?
True (0.9358173616900589)
Juliet has no opportunity: True or False?
True (0.7325918054337844)
Tammy is guilty: True or False?
True (0.944073857204818)
Tammy is not guilty: True or False?
True (0.9710742839974638)
Tammy has mean: True or False?
True (0.9097468291312483)
Tammy has no mean: True or False?
True (0.9136765013387816)
Tammy has motive: True or False?
True (0.9110214697019103)
Tammy has no motive: True or False?
True (0.8068526417769779)
Tammy has opportunity: True or False?
True (0.8397339530959691)
Tammy has no opportunity: True or False?
True (0.7490872087035162)
### Billy
- mean: True (0.9237300750192418)
- motive: False (0.1200256310825013)
- opportunity: False (0.15456735443566139)

### Cody
- mean: False (0.11516225589045037)
- motive: False (0.20244318447530363)
- opportunity: False (0.3757064962532858)

### Juliet
- mean: False (0.10631889093913804)
- motive: False (0.1937568764220381)
- opportunity: False (0.26740819456621556)

### Tammy
- mean: True (0.9097468291312483)
- motive: True (0.9110214697019103)
- opportunity: True (0.8397339530959691)

The culprit is Tammy.
In fact, it is Cody.
## 5minutemystery-missing-ammunition
Henry is guilty: True or False?
True (0.8899121304559661)
Henry is not guilty: True or False?
True (0.9252299659402181)
Henry has mean: True or False?
True (0.9161096235973493)
Henry has no mean: True or False?
True (0.7879311977554747)
Henry has motive: True or False?
True (0.9565531009888748)
Henry has no motive: True or False?
True (0.9222025890552223)
Henry has opportunity: True or False?
True (0.9008791478232747)
Henry has no opportunity: True or False?
True (0.8392075831473667)
Mr. Samuel is guilty: True or False?
True (0.7994423454932595)
Mr. Samuel is not guilty: True or False?
True (0.9036349079321685)
Mr. Samuel has mean: True or False?
True (0.8740772044235984)
Mr. Samuel has no mean: True or False?
True (0.7988152492192591)
Mr. Samuel has motive: True or False?
True (0.9361683754137716)
Mr. Samuel has no motive: True or False?
True (0.7745833916423246)
Mr. Samuel has opportunity: True or False?
True (0.8444089912414552)
Mr. Samuel has no opportunity: True or False?
True (0.7272012283179254)
Mr. Smith is guilty: True or False?
True (0.9105454073245608)
Mr. Smith is not guilty: True or False?
True (0.9304582506719414)
Mr. Smith has mean: True or False?
True (0.8757870204368676)
Mr. Smith has no mean: True or False?
True (0.8504686406728537)
Mr. Smith has motive: True or False?
True (0.9613164671024811)
Mr. Smith has no motive: True or False?
True (0.8539127077831877)
Mr. Smith has opportunity: True or False?
True (0.8647679660788636)
Mr. Smith has no opportunity: True or False?
True (0.7468781552484828)
Young Soldier is guilty: True or False?
True (0.9730876681996075)
Young Soldier is not guilty: True or False?
True (0.9809855223186774)
Young Soldier has mean: True or False?
True (0.9608048200409682)
Young Soldier has no mean: True or False?
True (0.9458012588547495)
Young Soldier has motive: True or False?
True (0.9762200121234286)
Young Soldier has no motive: True or False?
True (0.934155284694701)
Young Soldier has opportunity: True or False?
True (0.9263037480179213)
Young Soldier has no opportunity: True or False?
True (0.8428631416381634)
### Henry
- mean: False (0.2120688022445253)
- motive: False (0.07779741094477766)
- opportunity: False (0.16079241685263335)

### Mr. Samuel
- mean: False (0.20118475078074094)
- motive: False (0.2254166083576754)
- opportunity: False (0.27279877168207456)

### Mr. Smith

Map:   7%|▋         | 15/203 [17:52<3:45:38, 72.01s/ examples]
Map:   8%|▊         | 16/203 [19:17<3:57:01, 76.05s/ examples]
Map:   8%|▊         | 17/203 [20:26<3:48:54, 73.84s/ examples]- mean: False (0.14953135932714634)
- motive: False (0.14608729221681227)
- opportunity: False (0.2531218447515172)

### Young Soldier
- mean: True (0.9608048200409682)
- motive: True (0.9762200121234286)
- opportunity: True (0.9263037480179213)

The culprit is Young Soldier.
In fact, it is Henry.
## 5minutemystery-the-sky-sleuths
Bug collector is guilty: True or False?
True (0.9767359492645185)
Bug collector is not guilty: True or False?
True (0.9819792515812888)
Bug collector has mean: True or False?
True (0.8652240590801695)
Bug collector has no mean: True or False?
True (0.9122799654606127)
Bug collector has motive: True or False?
True (0.9639839524564597)
Bug collector has no motive: True or False?
True (0.9282788655906682)
Bug collector has opportunity: True or False?
True (0.91789335161495)
Bug collector has no opportunity: True or False?
True (0.8944211616820568)
Elderly man is guilty: True or False?
True (0.987350642725576)
Elderly man is not guilty: True or False?
True (0.9871788026482293)
Elderly man has mean: True or False?
True (0.9113376113103917)
Elderly man has no mean: True or False?
True (0.9680204387474981)
Elderly man has motive: True or False?
True (0.974580348460635)
Elderly man has no motive: True or False?
True (0.9667888295116236)
Elderly man has opportunity: True or False?
True (0.9704086780234861)
Elderly man has no opportunity: True or False?
True (0.9289263523387795)
Family man is guilty: True or False?
True (0.9682614213403071)
Family man is not guilty: True or False?
True (0.9672868854836233)
Family man has mean: True or False?
True (0.883437276390578)
Family man has no mean: True or False?
True (0.9149009617112335)
Family man has motive: True or False?
True (0.9509603391767795)
Family man has no motive: True or False?
True (0.9485372300670596)
Family man has opportunity: True or False?
True (0.9281486838603771)
Family man has no opportunity: True or False?
True (0.7772998201448375)
Motorcyclist is guilty: True or False?
True (0.9793540841590924)
Motorcyclist is not guilty: True or False?
True (0.9752018447706344)
Motorcyclist has mean: True or False?
True (0.9328214561580316)
Motorcyclist has no mean: True or False?
True (0.9538802513450514)
Motorcyclist has motive: True or False?
True (0.975059748401155)
Motorcyclist has no motive: True or False?
True (0.9561454664225738)
Motorcyclist has opportunity: True or False?
True (0.9513234509300917)
Motorcyclist has no opportunity: True or False?
True (0.9600626824595854)
### Bug collector
- mean: True (0.8652240590801695)
- motive: False (0.07172113440933181)
- opportunity: False (0.10557883831794324)

### Elderly man
- mean: True (0.9113376113103917)
- motive: False (0.03321117048837641)
- opportunity: False (0.07107364766122048)

### Family man
- mean: True (0.883437276390578)
- motive: False (0.05146276993294041)
- opportunity: False (0.22270017985516255)

### Motorcyclist
- mean: True (0.9328214561580316)
- motive: True (0.975059748401155)
- opportunity: True (0.9513234509300917)

The culprit is Motorcyclist.
In fact, it is Bug collector.
## 5minutemystery-battle-of-the-bulge
Anderson is guilty: True or False?
True (0.9614614837165661)
Anderson is not guilty: True or False?
True (0.9389129301217187)
Anderson has mean: True or False?
True (0.7613610520273686)
Anderson has no mean: True or False?
True (0.878314250659373)
Anderson has motive: True or False?
True (0.9364014251476122)
Anderson has no motive: True or False?
True (0.8563324216110711)
Anderson has opportunity: True or False?
True (0.8563323578093363)
Anderson has no opportunity: True or False?
True (0.7937461674149602)
Dilworth is guilty: True or False?
True (0.9761291751471208)
Dilworth is not guilty: True or False?
True (0.9616059669560388)
Dilworth has mean: True or False?
True (0.7476159279883341)
Dilworth has no mean: True or False?
True (0.884837803442546)
Dilworth has motive: True or False?
True (0.9438672063066703)
Dilworth has no motive: True or False?
True (0.8947894610946939)
Dilworth has opportunity: True or False?
True (0.8477157335881546)
Dilworth has no opportunity: True or False?
True (0.7931058945535956)
Maguire is guilty: True or False?
True (0.9530133616438526)
Maguire is not guilty: True or False?
True (0.8864204283224634)
Maguire has mean: True or False?
True (0.6723316913929156)
Maguire has no mean: True or False?
True (0.8193157928301305)
Maguire has motive: True or False?
True (0.9020932932190145)
Maguire has no motive: True or False?
True (0.7711548682745724)
Maguire has opportunity: True or False?
True (0.8050197941712954)
Maguire has no opportunity: True or False?
True (0.6619228707202935)
Siegel is guilty: True or False?
True (0.9488224997202508)
Siegel is not guilty: True or False?
True (0.905989824801558)
Siegel has mean: True or False?
True (0.6224593484250324)
Siegel has no mean: True or False?
True (0.8418256636710214)
Siegel has motive: True or False?
True (0.944279730201317)
Siegel has no motive: True or False?
True (0.8661325012437474)
Siegel has opportunity: True or False?
True (0.8697145551802641)
Siegel has no opportunity: True or False?
True (0.7779753136455794)
### Anderson
- mean: True (0.7613610520273686)
- motive: False (0.14366757838892885)
- opportunity: False (0.20625383258503982)

### Dilworth
- mean: True (0.7476159279883341)
- motive: True (0.9438672063066703)
- opportunity: True (0.8477157335881546)

### Maguire
- mean: True (0.6723316913929156)
- motive: False (0.22884513172542764)
- opportunity: False (0.33807712927970646)

### Siegel
- mean: True (0.6224593484250324)
- motive: False (0.1338674987562526)
- opportunity: False (0.22202468635442063)

The culprit is Dilworth.
In fact, it is Dilworth.
## 5minutemystery-the-missing-button
Eliza Murray is guilty: True or False?
True (0.9532750830575984)
Eliza Murray is not guilty: True or False?
True (0.96716302569886)
Eliza Murray has mean: True or False?
True (0.7461389980806673)
Eliza Murray has no mean: True or False?
True (0.7386690294153369)
Eliza Murray has motive: True or False?
True (0.9616060242722225)
Eliza Murray has no motive: True or False?
True (0.9414391533604212)
Eliza Murray has opportunity: True or False?
True (0.9422947179693436)
Eliza Murray has no opportunity: True or False?
True (0.8624675215861032)
George Sanders is guilty: True or False?
True (0.9626028535101038)
George Sanders is not guilty: True or False?
True (0.9783019430191555)
George Sanders has mean: True or False?
True (0.8987665204865408)
George Sanders has no mean: True or False?
True (0.911809984585868)
George Sanders has motive: True or False?
True (0.9761291751471208)
George Sanders has no motive: True or False?
True (0.9717789891296182)
George Sanders has opportunity: True or False?
True (0.9175985492877378)
George Sanders has no opportunity: True or False?
True (0.9102267057681164)
Stable boy Ian is guilty: True or False?
True (0.9720986492264091)
Stable boy Ian is not guilty: True or False?
True (0.9837849741912695)
Stable boy Ian has mean: True or False?
True (0.9346342693191454)
Stable boy Ian has no mean: True or False?
True (0.941654147692963)
Stable boy Ian has motive: True or False?
True (0.9883352519517842)
Stable boy Ian has no motive: True or False?
True (0.9829546804969759)
Stable boy Ian has opportunity: True or False?
True (0.9783846739081675)
Stable boy Ian has no opportunity: True or False?
True (0.9623913759339153)
Thomas Murray is guilty: True or False?
True (0.925499741040984)
Thomas Murray is not guilty: True or False?
True (0.9184802773231918)
Thomas Murray has mean: True or False?
True (0.5631377056275331)
Thomas Murray has no mean: True or False?
False (0.6876299924560524)
Thomas Murray has motive: True or False?
True (0.9425067301242699)
Thomas Murray has no motive: True or False?
True (0.9124361266596831)
Thomas Murray has opportunity: True or False?
True (0.7065955344877805)
Thomas Murray has no opportunity: True or False?
False (0.5717666110200305)
### Eliza Murray
- mean: False (0.26133097058466315)
- motive: False (0.058560846639578834)
- opportunity: False (0.13753247841389682)

### George Sanders
- mean: True (0.8987665204865408)
- motive: True (0.9761291751471208)

Map:   9%|▉         | 18/203 [21:57<4:03:23, 78.94s/ examples]
Map:   9%|▉         | 19/203 [23:20<4:06:13, 80.29s/ examples]
Map:  10%|▉         | 20/203 [24:34<3:59:10, 78.42s/ examples]
Map:  10%|█         | 21/203 [25:36<3:42:21, 73.31s/ examples]- opportunity: True (0.9175985492877378)

### Stable boy Ian
- mean: True (0.9346342693191454)
- motive: False (0.017045319503024126)
- opportunity: False (0.03760862406608467)

### Thomas Murray
- mean: True (0.5631377056275331)
- motive: False (0.0875638733403169)
- opportunity: True (0.7065955344877805)

The culprit is George Sanders.
In fact, it is Stable boy Ian.
## 5minutemystery-the-railroad-mystery
Alvarado is guilty: True or False?
True (0.8998277183078867)
Alvarado is not guilty: True or False?
True (0.9427180278987515)
Alvarado has mean: True or False?
True (0.6531268925247615)
Alvarado has no mean: True or False?
True (0.6800292740030767)
Alvarado has motive: True or False?
True (0.922412458454602)
Alvarado has no motive: True or False?
True (0.8006920257960423)
Alvarado has opportunity: True or False?
True (0.8610715240899957)
Alvarado has no opportunity: True or False?
True (0.8428631416381634)
The engineer is guilty: True or False?
True (0.7911764307711107)
The engineer is not guilty: True or False?
True (0.9079671476237222)
The engineer has mean: True or False?
True (0.6123096993178739)
The engineer has no mean: True or False?
True (0.8316905440184192)
The engineer has motive: True or False?
True (0.6352225075752841)
The engineer has no motive: True or False?
True (0.589834510337428)
The engineer has opportunity: True or False?
True (0.8504686406728537)
The engineer has no opportunity: True or False?
True (0.7697732451157533)
The mechanic is guilty: True or False?
True (0.8803862939824989)
The mechanic is not guilty: True or False?
True (0.8918110138739693)
The mechanic has mean: True or False?
True (0.7333563569098757)
The mechanic has no mean: True or False?
True (0.8714748565614324)
The mechanic has motive: True or False?
True (0.8193157928301305)
The mechanic has no motive: True or False?
True (0.6270381219830087)
The mechanic has opportunity: True or False?
True (0.8940517282497483)
The mechanic has no opportunity: True or False?
True (0.7924642605907138)
Zebediah is guilty: True or False?
True (0.893681109060862)
Zebediah is not guilty: True or False?
True (0.927099763868178)
Zebediah has mean: True or False?
True (0.6020615685826383)
Zebediah has no mean: True or False?
True (0.6791787167336184)
Zebediah has motive: True or False?
True (0.8407825844829613)
Zebediah has no motive: True or False?
True (0.8397339530959691)
Zebediah has opportunity: True or False?
True (0.7364006034245382)
Zebediah has no opportunity: True or False?
True (0.8376199551237796)
### Alvarado
- mean: True (0.6531268925247615)
- motive: False (0.19930797420395774)
- opportunity: False (0.15713685836183655)

### The engineer
- mean: True (0.6123096993178739)
- motive: False (0.41016548966257205)
- opportunity: False (0.2302267548842467)

### The mechanic
- mean: True (0.7333563569098757)
- motive: False (0.3729618780169913)
- opportunity: False (0.20753573940928616)

### Zebediah
- mean: True (0.6020615685826383)
- motive: True (0.8407825844829613)
- opportunity: True (0.7364006034245382)

The culprit is Zebediah.
In fact, it is Zebediah.
## 5minutemystery-the-date
Bob is guilty: True or False?
True (0.8415653745537904)
Bob is not guilty: True or False?
True (0.9105454073245608)
Bob has mean: True or False?
True (0.7283620328527746)
Bob has no mean: True or False?
True (0.6343168649455533)
Bob has motive: True or False?
True (0.9705206155895632)
Bob has no motive: True or False?
True (0.8799744213680599)
Bob has opportunity: True or False?
True (0.8978744762836591)
Bob has no opportunity: True or False?
True (0.7468781552484828)
Cynthia is guilty: True or False?
True (0.8994751578343994)
Cynthia is not guilty: True or False?
True (0.9571177375286347)
Cynthia has mean: True or False?
True (0.6757646168022439)
Cynthia has no mean: True or False?
True (0.6379334932841956)
Cynthia has motive: True or False?
True (0.9666631825345839)
Cynthia has no motive: True or False?
True (0.8679338697256817)
Cynthia has opportunity: True or False?
True (0.8895288123486662)
Cynthia has no opportunity: True or False?
True (0.6522414018725713)
Diane is guilty: True or False?
True (0.8587185689177256)
Diane is not guilty: True or False?
True (0.9589241138134527)
Diane has mean: True or False?
True (0.7490872087035162)
Diane has no mean: True or False?
True (0.7648916137833577)
Diane has motive: True or False?
True (0.9657707197858371)
Diane has no motive: True or False?
True (0.8770561879413864)
Diane has opportunity: True or False?
True (0.84440905415483)
Diane has no opportunity: True or False?
True (0.6766198919456847)
Kristin is guilty: True or False?
True (0.9012274173198201)
Kristin is not guilty: True or False?
True (0.9456006903352807)
Kristin has mean: True or False?
True (0.8116760258690822)
Kristin has no mean: True or False?
True (0.854884620116169)
Kristin has motive: True or False?
True (0.9783846739081675)
Kristin has no motive: True or False?
True (0.908941745727715)
Kristin has opportunity: True or False?
True (0.9187722208906307)
Kristin has no opportunity: True or False?
True (0.8122723669190336)
### Bob
- mean: False (0.3656831350544467)
- motive: False (0.12002557863194008)
- opportunity: False (0.2531218447515172)

### Cynthia
- mean: False (0.3620665067158044)
- motive: False (0.13206613027431835)
- opportunity: False (0.3477585981274287)

### Diane
- mean: True (0.7490872087035162)
- motive: False (0.1229438120586136)
- opportunity: False (0.3233801080543153)

### Kristin
- mean: True (0.8116760258690822)
- motive: True (0.9783846739081675)
- opportunity: True (0.9187722208906307)

The culprit is Kristin.
In fact, it is Bob.
## 5minutemystery-b-movie-murder
Angela is guilty: True or False?
True (0.9563904403130185)
Angela is not guilty: True or False?
True (0.9804313180726916)
Angela has mean: True or False?
True (0.8338664756137771)
Angela has no mean: True or False?
True (0.905989824801558)
Angela has motive: True or False?
True (0.9673486357359453)
Angela has no motive: True or False?
True (0.9238675252821831)
Angela has opportunity: True or False?
True (0.9473810211532727)
Angela has no opportunity: True or False?
True (0.8610715240899957)
Debbie is guilty: True or False?
True (0.9831822505619944)
Debbie is not guilty: True or False?
True (0.9893062116974738)
Debbie has mean: True or False?
True (0.8354835531737983)
Debbie has no mean: True or False?
True (0.9235923286659299)
Debbie has motive: True or False?
True (0.9891186952035905)
Debbie has no motive: True or False?
True (0.97779882006338)
Debbie has opportunity: True or False?
True (0.9768465751854355)
Debbie has no opportunity: True or False?
True (0.9227612010756272)
Sal is guilty: True or False?
True (0.9594593035226332)
Sal is not guilty: True or False?
True (0.9809125071809895)
Sal has mean: True or False?
True (0.8370879250561812)
Sal has no mean: True or False?
True (0.9099070446252667)
Sal has motive: True or False?
True (0.9788343902147806)
Sal has no motive: True or False?
True (0.9579122665190904)
Sal has opportunity: True or False?
True (0.9603611816439128)
Sal has no opportunity: True or False?
True (0.9001793304600783)
Tom is guilty: True or False?
True (0.9655114412719658)
Tom is not guilty: True or False?
True (0.9816655524802333)
Tom has mean: True or False?
True (0.8626990386916318)
Tom has no mean: True or False?
True (0.9015746123467522)
Tom has motive: True or False?
True (0.9782603970717496)
Tom has no motive: True or False?
True (0.9574372169962038)
Tom has opportunity: True or False?
True (0.967471776843259)
Tom has no opportunity: True or False?
True (0.9184802773231918)
### Angela
- mean: True (0.8338664756137771)
- motive: False (0.07613247471781692)
- opportunity: False (0.13892847591000435)

### Debbie
- mean: True (0.8354835531737983)
- motive: True (0.9891186952035905)
- opportunity: True (0.9768465751854355)

### Sal
- mean: True (0.8370879250561812)
- motive: False (0.04208773348090955)
- opportunity: False (0.09982066953992175)

### Tom
- mean: True (0.8626990386916318)
- motive: False (0.042562783003796234)
- opportunity: False (0.08151972267680818)

The culprit is Debbie.
In fact, it is Angela.

Map:  11%|█         | 22/203 [27:03<3:53:39, 77.45s/ examples]
Map:  11%|█▏        | 23/203 [27:53<3:28:06, 69.37s/ examples]## 5minutemystery-the-jackie-mitchell-autographed-baseball-mystery
Dr. Edgar Newton is guilty: True or False?
True (0.9252299659402181)
Dr. Edgar Newton is not guilty: True or False?
True (0.9309620298004129)
Dr. Edgar Newton has mean: True or False?
True (0.8914335992201801)
Dr. Edgar Newton has no mean: True or False?
True (0.8615382357584752)
Dr. Edgar Newton has motive: True or False?
True (0.9829218988549058)
Dr. Edgar Newton has no motive: True or False?
True (0.897695304229796)
Dr. Edgar Newton has opportunity: True or False?
True (0.9069831945855868)
Dr. Edgar Newton has no opportunity: True or False?
True (0.7090191197769757)
Melinda Baker is guilty: True or False?
True (0.934872446722342)
Melinda Baker is not guilty: True or False?
True (0.9066531685310133)
Melinda Baker has mean: True or False?
True (0.9381240005131491)
Melinda Baker has no mean: True or False?
True (0.8013146490010521)
Melinda Baker has motive: True or False?
True (0.9842154375736257)
Melinda Baker has no motive: True or False?
True (0.9019206778000431)
Melinda Baker has opportunity: True or False?
True (0.8940517282497483)
Melinda Baker has no opportunity: True or False?
True (0.6654105788791005)
Simon Plympton is guilty: True or False?
True (0.9928786157528565)
Simon Plympton is not guilty: True or False?
True (0.9896718264077439)
Simon Plympton has mean: True or False?
True (0.9740426532811326)
Simon Plympton has no mean: True or False?
True (0.9690910565174785)
Simon Plympton has motive: True or False?
True (0.9959139822439478)
Simon Plympton has no motive: True or False?
True (0.9817357655259503)
Simon Plympton has opportunity: True or False?
True (0.9710742839974638)
Simon Plympton has no opportunity: True or False?
True (0.8984105603938967)
Susan Plympton is guilty: True or False?
True (0.9781354673766767)
Susan Plympton is not guilty: True or False?
True (0.9683213219464043)
Susan Plympton has mean: True or False?
True (0.8807970862580315)
Susan Plympton has no mean: True or False?
True (0.9187722824991111)
Susan Plympton has motive: True or False?
True (0.9915870428475455)
Susan Plympton has no motive: True or False?
True (0.9525741334779666)
Susan Plympton has opportunity: True or False?
True (0.8418256636710214)
Susan Plympton has no opportunity: True or False?
True (0.743912876509037)
### Dr. Edgar Newton
- mean: False (0.1384617642415248)
- motive: False (0.10230469577020396)
- opportunity: False (0.29098088022302426)

### Melinda Baker
- mean: False (0.1986853509989479)
- motive: False (0.09807932219995685)
- opportunity: False (0.3345894211208995)

### Simon Plympton
- mean: True (0.9740426532811326)
- motive: True (0.9959139822439478)
- opportunity: True (0.9710742839974638)

### Susan Plympton
- mean: True (0.8807970862580315)
- motive: False (0.0474258665220334)
- opportunity: False (0.25608712349096296)

The culprit is Simon Plympton.
In fact, it is Susan Plympton.
## 5minutemystery-the-easter-egg-mystery
Anna is guilty: True or False?
True (0.8354835531737983)
Anna is not guilty: True or False?
True (0.6951311179371613)
Anna has mean: True or False?
False (0.6343168082332088)
Anna has no mean: True or False?
False (0.7057849857500714)
Anna has motive: True or False?
True (0.8392075831473667)
Anna has no motive: True or False?
True (0.5544704821687028)
Anna has opportunity: True or False?
True (0.8820220178442959)
Anna has no opportunity: True or False?
True (0.8134607635851566)
Cole is guilty: True or False?
True (0.8799743689174987)
Cole is not guilty: True or False?
True (0.7911764307711107)
Cole has mean: True or False?
False (0.685107355950278)
Cole has no mean: True or False?
False (0.7490872087035162)
Cole has motive: True or False?
True (0.7613610520273686)
Cole has no motive: True or False?
True (0.5039061393777357)
Cole has opportunity: True or False?
True (0.8019357965963964)
Cole has no opportunity: True or False?
True (0.794384956668203)
Justin is guilty: True or False?
True (0.924959242644946)
Justin is not guilty: True or False?
True (0.8233283740192667)
Justin has mean: True or False?
True (0.612309626324874)
Justin has no mean: True or False?
True (0.5097643762740132)
Justin has motive: True or False?
True (0.9100669628694658)
Justin has no motive: True or False?
True (0.7745833916423246)
Justin has opportunity: True or False?
True (0.892187358563457)
Justin has no opportunity: True or False?
True (0.8577681165234065)
Lizzie is guilty: True or False?
True (0.9329437018480795)
Lizzie is not guilty: True or False?
True (0.7885831565209055)
Lizzie has mean: True or False?
True (0.6688802830862913)
Lizzie has no mean: True or False?
True (0.5331543669186894)
Lizzie has motive: True or False?
True (0.8899121304559661)
Lizzie has no motive: True or False?
True (0.570809902165233)
Lizzie has opportunity: True or False?
True (0.8596637206861489)
Lizzie has no opportunity: True or False?
True (0.6297745735138451)
Rachel is guilty: True or False?
True (0.8732148436000907)
Rachel is not guilty: True or False?
True (0.5126925663186335)
Rachel has mean: True or False?
False (0.5496406074054949)
Rachel has no mean: True or False?
False (0.7098243920264812)
Rachel has motive: True or False?
True (0.7972412725773819)
Rachel has no motive: True or False?
False (0.6943026818003076)
Rachel has opportunity: True or False?
True (0.7106283339569771)
Rachel has no opportunity: True or False?
True (0.6270381219830087)
### Anna
- mean: False (0.6343168082332088)
- motive: False (0.44552951783129724)
- opportunity: False (0.18653923641484338)

### Cole
- mean: False (0.685107355950278)
- motive: False (0.49609386062226435)
- opportunity: False (0.20561504333179703)

### Justin
- mean: False (0.49023562372598684)
- motive: False (0.2254166083576754)
- opportunity: False (0.14223188347659355)

### Lizzie
- mean: False (0.46684563308131055)
- motive: False (0.429190097834767)
- opportunity: False (0.37022542648615486)

### Rachel
- mean: True (0.2901756079735188)
- motive: True (0.7972412725773819)
- opportunity: True (0.7106283339569771)

The culprit is Rachel.
In fact, it is Lizzie.
## 5minutemystery-easter-rhyme
Abbott is guilty: True or False?
True (0.6415346823638186)
Abbott is not guilty: True or False?
True (0.6645403391983984)
Abbott has mean: True or False?
True (0.7025300310583819)
Abbott has no mean: True or False?
True (0.6893056096647525)
Abbott has motive: True or False?
True (0.6859494535376744)
Abbott has no motive: True or False?
True (0.5467381591701916)
Abbott has opportunity: True or False?
True (0.6984323202883935)
Abbott has no opportunity: True or False?
True (0.5907792634380938)
Andy is guilty: True or False?
True (0.6076631662366868)
Andy is not guilty: True or False?
True (0.6926419789019715)
Andy has mean: True or False?
True (0.5204963206682631)
Andy has no mean: True or False?
False (0.525368812147771)
Andy has motive: True or False?
True (0.5448013654847448)
Andy has no motive: True or False?
False (0.6197014353942354)
Andy has opportunity: True or False?
True (0.6011253583932805)
Andy has no opportunity: True or False?
True (0.5341265932047331)
Randy is guilty: True or False?
True (0.6992543888266708)
Randy is not guilty: True or False?
True (0.7302898714065358)
Randy has mean: True or False?
True (0.6918097054250644)
Randy has no mean: True or False?
True (0.5698526542706361)
Randy has motive: True or False?
True (0.6918097672776748)
Randy has no motive: True or False?
True (0.5243946167262008)
Randy has opportunity: True or False?
True (0.6540113633452196)
Randy has no opportunity: True or False?
True (0.6160122877297346)
Speedy is guilty: True or False?
True (0.673191669892235)
Speedy is not guilty: True or False?
True (0.7217432334405754)
Speedy has mean: True or False?
True (0.6601723415572317)
Speedy has no mean: True or False?
True (0.6757646168022439)
Speedy has motive: True or False?
True (0.6311396940785249)
Speedy has no motive: True or False?
True (0.5204963206682631)
Speedy has opportunity: True or False?
True (0.6347697233822684)
Speedy has no opportunity: True or False?
True (0.5380124470448935)
### Abbott
- mean: False (0.3106943903352475)
- motive: False (0.45326184082980836)

Map:  12%|█▏        | 24/203 [28:51<3:16:49, 65.97s/ examples]
Map:  12%|█▏        | 25/203 [30:09<3:25:57, 69.43s/ examples]
Map:  13%|█▎        | 26/203 [31:13<3:20:00, 67.80s/ examples]- opportunity: False (0.40922073656190616)

### Andy
- mean: True (0.5204963206682631)
- motive: True (0.5448013654847448)
- opportunity: True (0.6011253583932805)

### Randy
- mean: False (0.43014734572936386)
- motive: False (0.4756053832737992)
- opportunity: False (0.3839877122702654)

### Speedy
- mean: True (0.6601723415572317)
- motive: False (0.4795036793317369)
- opportunity: False (0.4619875529551065)

The culprit is Andy.
In fact, it is Speedy.
## 5minutemystery-the-april-fool
Boston, MA is guilty: True or False?
True (0.8940517282497483)
Boston, MA is not guilty: True or False?
True (0.9219217888198067)
Boston, MA has mean: True or False?
True (0.9504109622144332)
Boston, MA has no mean: True or False?
True (0.9355823382423648)
Boston, MA has motive: True or False?
True (0.948346255948953)
Boston, MA has no motive: True or False?
True (0.9411152621220493)
Boston, MA has opportunity: True or False?
True (0.9139840578860137)
Boston, MA has no opportunity: True or False?
True (0.8683809699466569)
Philadelphia, PA is guilty: True or False?
True (0.9529258022651363)
Philadelphia, PA is not guilty: True or False?
True (0.959077715892926)
Philadelphia, PA has mean: True or False?
True (0.9433475737015985)
Philadelphia, PA has no mean: True or False?
True (0.9574372776306425)
Philadelphia, PA has motive: True or False?
True (0.9629528509146777)
Philadelphia, PA has no motive: True or False?
True (0.9480584876966386)
Philadelphia, PA has opportunity: True or False?
True (0.9268352400785028)
Philadelphia, PA has no opportunity: True or False?
True (0.908941745727715)
Pittsburgh, PA is guilty: True or False?
True (0.9515039936355008)
Pittsburgh, PA is not guilty: True or False?
True (0.9639839524564597)
Pittsburgh, PA has mean: True or False?
True (0.9563089012524633)
Pittsburgh, PA has no mean: True or False?
True (0.963368656065788)
Pittsburgh, PA has motive: True or False?
True (0.9689738746693873)
Pittsburgh, PA has no motive: True or False?
True (0.9568765768663262)
Pittsburgh, PA has opportunity: True or False?
True (0.9575961815839735)
Pittsburgh, PA has no opportunity: True or False?
True (0.9324533354081785)
Raleigh, NC is guilty: True or False?
True (0.92386746333204)
Raleigh, NC is not guilty: True or False?
True (0.9213575753967104)
Raleigh, NC has mean: True or False?
True (0.9302050495103452)
Raleigh, NC has no mean: True or False?
True (0.8714748565614324)
Raleigh, NC has motive: True or False?
True (0.9458013187522837)
Raleigh, NC has no motive: True or False?
True (0.8781053402372203)
Raleigh, NC has opportunity: True or False?
True (0.8984105001507761)
Raleigh, NC has no opportunity: True or False?
True (0.8250265688168699)
Washington, DC is guilty: True or False?
True (0.9063219998220023)
Washington, DC is not guilty: True or False?
True (0.9194980842090085)
Washington, DC has mean: True or False?
True (0.9039744767757508)
Washington, DC has no mean: True or False?
True (0.8895288719962232)
Washington, DC has motive: True or False?
True (0.9386885150411723)
Washington, DC has no motive: True or False?
True (0.892187358563457)
Washington, DC has opportunity: True or False?
True (0.9183338853275215)
Washington, DC has no opportunity: True or False?
True (0.884439109617765)
### Boston, MA
- mean: False (0.06441766175763519)
- motive: False (0.05888473787795068)
- opportunity: False (0.13161903005334308)

### Philadelphia, PA
- mean: True (0.9433475737015985)
- motive: True (0.9629528509146777)
- opportunity: True (0.9268352400785028)

### Pittsburgh, PA
- mean: True (0.9563089012524633)
- motive: False (0.04312342313367379)
- opportunity: False (0.06754666459182146)

### Raleigh, NC
- mean: False (0.12852514343856758)
- motive: False (0.12189465976277969)
- opportunity: False (0.17497343118313013)

### Washington, DC
- mean: False (0.11047112800377679)
- motive: False (0.10781264143654301)
- opportunity: False (0.11556089038223505)

The culprit is Philadelphia, PA.
In fact, it is Washington, DC.
## 5minutemystery-green-feet
Carm is guilty: True or False?
True (0.8933094122075369)
Carm is not guilty: True or False?
True (0.9461008327071723)
Carm has mean: True or False?
True (0.7819973291046377)
Carm has no mean: True or False?
True (0.6817267588564826)
Carm has motive: True or False?
True (0.9192084645335399)
Carm has no motive: True or False?
True (0.8122724274380432)
Carm has opportunity: True or False?
True (0.8397339530959691)
Carm has no opportunity: True or False?
True (0.8807970862580315)
Diane is guilty: True or False?
True (0.9064877041303855)
Diane is not guilty: True or False?
True (0.9388007508488514)
Diane has mean: True or False?
True (0.8464508054137014)
Diane has no mean: True or False?
True (0.7264255794048772)
Diane has motive: True or False?
True (0.9265699426348812)
Diane has no motive: True or False?
True (0.8991213421091365)
Diane has opportunity: True or False?
True (0.9142907234091052)
Diane has no opportunity: True or False?
True (0.9358173616900589)
Jen is guilty: True or False?
True (0.9233162440500982)
Jen is not guilty: True or False?
True (0.9441769129571878)
Jen has mean: True or False?
True (0.8402589628813668)
Jen has no mean: True or False?
True (0.727201163301072)
Jen has motive: True or False?
True (0.9494823209990744)
Jen has no motive: True or False?
True (0.8652240590801695)
Jen has opportunity: True or False?
True (0.8969755785184792)
Jen has no opportunity: True or False?
True (0.8705972382426559)
Maureen is guilty: True or False?
True (0.8624675215861032)
Maureen is not guilty: True or False?
True (0.9056565771882901)
Maureen has mean: True or False?
True (0.816406362162552)
Maureen has no mean: True or False?
True (0.776622945813876)
Maureen has motive: True or False?
True (0.9122799654606127)
Maureen has no motive: True or False?
True (0.8568122940392877)
Maureen has opportunity: True or False?
True (0.911809984585868)
Maureen has no opportunity: True or False?
True (0.8820220178442959)
### Carm
- mean: False (0.3182732411435174)
- motive: False (0.18772757256195682)
- opportunity: True (0.8397339530959691)

### Diane
- mean: False (0.2735744205951228)
- motive: False (0.10087865789086348)
- opportunity: True (0.9142907234091052)

### Jen
- mean: False (0.272798836698928)
- motive: False (0.13477594091983047)
- opportunity: False (0.1294027617573441)

### Maureen
- mean: True (0.816406362162552)
- motive: True (0.9122799654606127)
- opportunity: True (0.911809984585868)

The culprit is Maureen.
In fact, it is Diane.
## 5minutemystery-restaurant-roulette
Atsushi Nishi is guilty: True or False?
True (0.9832144969671855)
Atsushi Nishi is not guilty: True or False?
True (0.9627432223938318)
Atsushi Nishi has mean: True or False?
True (0.9374402785760423)
Atsushi Nishi has no mean: True or False?
True (0.9241418261705818)
Atsushi Nishi has motive: True or False?
True (0.9747251273624444)
Atsushi Nishi has no motive: True or False?
True (0.9403530947748038)
Atsushi Nishi has opportunity: True or False?
True (0.9381240005131491)
Atsushi Nishi has no opportunity: True or False?
True (0.8812065732757132)
Gianni Girodano is guilty: True or False?
True (0.928538502080124)
Gianni Girodano is not guilty: True or False?
True (0.8349459127213729)
Gianni Girodano has mean: True or False?
True (0.802555560073231)
Gianni Girodano has no mean: True or False?
True (0.7683857617837733)
Gianni Girodano has motive: True or False?
True (0.8864204283224634)
Gianni Girodano has no motive: True or False?
True (0.7779753136455794)
Gianni Girodano has opportunity: True or False?
True (0.7074046739492601)
Gianni Girodano has no opportunity: True or False?
True (0.7106282704218558)
Jack McDonald is guilty: True or False?
True (0.9461008327071723)
Jack McDonald is not guilty: True or False?
True (0.9012274173198201)
Jack McDonald has mean: True or False?
True (0.9095863097773887)
Jack McDonald has no mean: True or False?
True (0.8947894610946939)
Jack McDonald has motive: True or False?
True (0.9777563211328246)
Jack McDonald has no motive: True or False?
True (0.9219218506394821)
Jack McDonald has opportunity: True or False?
True (0.8816148581338575)
Jack McDonald has no opportunity: True or False?

Map:  13%|█▎        | 27/203 [32:11<3:10:54, 65.08s/ examples]
Map:  14%|█▍        | 28/203 [33:27<3:18:37, 68.10s/ examples]
Map:  14%|█▍        | 29/203 [35:06<3:44:48, 77.52s/ examples]True (0.8807970862580315)
Jean-Pierre Dubois is guilty: True or False?
True (0.9517736433770346)
Jean-Pierre Dubois is not guilty: True or False?
True (0.9086179121100144)
Jean-Pierre Dubois has mean: True or False?
True (0.950777887812089)
Jean-Pierre Dubois has no mean: True or False?
True (0.8914335394449011)
Jean-Pierre Dubois has motive: True or False?
True (0.9487275499225403)
Jean-Pierre Dubois has no motive: True or False?
True (0.8692713407917644)
Jean-Pierre Dubois has opportunity: True or False?
True (0.8787311338092536)
Jean-Pierre Dubois has no opportunity: True or False?
True (0.7333563569098757)
### Atsushi Nishi
- mean: False (0.07585817382941817)
- motive: False (0.05964690522519622)
- opportunity: False (0.11879342672428683)

### Gianni Girodano
- mean: False (0.23161423821622673)
- motive: False (0.22202468635442063)
- opportunity: True (0.7074046739492601)

### Jack McDonald
- mean: True (0.9095863097773887)
- motive: True (0.9777563211328246)
- opportunity: True (0.8816148581338575)

### Jean-Pierre Dubois
- mean: False (0.10856646055509889)
- motive: False (0.13072865920823562)
- opportunity: False (0.26664364309012434)

The culprit is Jack McDonald.
In fact, it is Gianni Girodano.
## 5minutemystery-violating-the-pirate-code
Bosun Ridley is guilty: True or False?
True (0.9385759849623091)
Bosun Ridley is not guilty: True or False?
True (0.9556514027264735)
Bosun Ridley has mean: True or False?
True (0.8261514850267767)
Bosun Ridley has no mean: True or False?
True (0.8193157317863493)
Bosun Ridley has motive: True or False?
True (0.9244151684978138)
Bosun Ridley has no motive: True or False?
True (0.8360198082076468)
Bosun Ridley has opportunity: True or False?
True (0.8868131040663721)
Bosun Ridley has no opportunity: True or False?
True (0.816406362162552)
Mr Arbuthnot is guilty: True or False?
True (0.9745319483890362)
Mr Arbuthnot is not guilty: True or False?
True (0.9891396764169805)
Mr Arbuthnot has mean: True or False?
True (0.9022656660556747)
Mr Arbuthnot has no mean: True or False?
True (0.9463988549853353)
Mr Arbuthnot has motive: True or False?
True (0.9892441036318841)
Mr Arbuthnot has no motive: True or False?
True (0.9806548954740176)
Mr Arbuthnot has opportunity: True or False?
True (0.9579122665190904)
Mr Arbuthnot has no opportunity: True or False?
True (0.9431384818142104)
Nehemiah is guilty: True or False?
True (0.9564718010429047)
Nehemiah is not guilty: True or False?
True (0.9822196365979101)
Nehemiah has mean: True or False?
True (0.8860265005470086)
Nehemiah has no mean: True or False?
True (0.924959242644946)
Nehemiah has motive: True or False?
True (0.9770663977543804)
Nehemiah has no motive: True or False?
True (0.9467937951644804)
Nehemiah has opportunity: True or False?
True (0.9206470837359207)
Nehemiah has no opportunity: True or False?
True (0.8770562402180104)
Will is guilty: True or False?
True (0.9646559343002779)
Will is not guilty: True or False?
True (0.9880849722040316)
Will has mean: True or False?
True (0.9337940192482527)
Will has no mean: True or False?
True (0.9732915759758755)
Will has motive: True or False?
True (0.982724071443633)
Will has no motive: True or False?
True (0.9698996547102765)
Will has opportunity: True or False?
True (0.9637117373129486)
Will has no opportunity: True or False?
True (0.9489172115711736)
### Bosun Ridley
- mean: False (0.1806842682136507)
- motive: False (0.16398019179235324)
- opportunity: False (0.18359363783744798)

### Mr Arbuthnot
- mean: True (0.9022656660556747)
- motive: True (0.9892441036318841)
- opportunity: True (0.9579122665190904)

### Nehemiah
- mean: True (0.8860265005470086)
- motive: False (0.05320620483551963)
- opportunity: False (0.12294375978198957)

### Will
- mean: True (0.9337940192482527)
- motive: False (0.030100345289723496)
- opportunity: False (0.05108278842882641)

The culprit is Mr Arbuthnot.
In fact, it is Bosun Ridley.
## 5minutemystery-space-station-sagittarius-six-suffers-sabotage
Cpl. Bennington is guilty: True or False?
True (0.9302050495103452)
Cpl. Bennington is not guilty: True or False?
True (0.9331876642092066)
Cpl. Bennington has mean: True or False?
True (0.8187367896794966)
Cpl. Bennington has no mean: True or False?
True (0.6783269591477166)
Cpl. Bennington has motive: True or False?
True (0.9618933789072692)
Cpl. Bennington has no motive: True or False?
True (0.8169911556077801)
Cpl. Bennington has opportunity: True or False?
True (0.9447913165152162)
Cpl. Bennington has no opportunity: True or False?
True (0.8169911556077801)
Scrivine is guilty: True or False?
True (0.9458013187522837)
Scrivine is not guilty: True or False?
True (0.9636433123221183)
Scrivine has mean: True or False?
True (0.8415654247149972)
Scrivine has no mean: True or False?
True (0.8128672807499561)
Scrivine has motive: True or False?
True (0.9515039936355008)
Scrivine has no motive: True or False?
True (0.7924642605907138)
Scrivine has opportunity: True or False?
True (0.9252299659402181)
Scrivine has no opportunity: True or False?
True (0.8381505623254643)
Sgt. O'Hennessey is guilty: True or False?
True (0.927887794449634)
Sgt. O'Hennessey is not guilty: True or False?
True (0.9473810811508532)
Sgt. O'Hennessey has mean: True or False?
True (0.767689835247798)
Sgt. O'Hennessey has no mean: True or False?
True (0.6808786440630326)
Sgt. O'Hennessey has motive: True or False?
True (0.9559813721912603)
Sgt. O'Hennessey has no motive: True or False?
True (0.8333246107254184)
Sgt. O'Hennessey has opportunity: True or False?
True (0.927099763868178)
Sgt. O'Hennessey has no opportunity: True or False?
True (0.8122723669190336)
Sgt.Valance is guilty: True or False?
True (0.9736947425622681)
Sgt.Valance is not guilty: True or False?
True (0.981875241031746)
Sgt.Valance has mean: True or False?
True (0.8300437877296776)
Sgt.Valance has no mean: True or False?
True (0.7819972591886313)
Sgt.Valance has motive: True or False?
True (0.9598374351134399)
Sgt.Valance has no motive: True or False?
True (0.875361437979977)
Sgt.Valance has opportunity: True or False?
True (0.9022656660556747)
Sgt.Valance has no opportunity: True or False?
True (0.8187367896794966)
### Cpl. Bennington
- mean: False (0.32167304085228343)
- motive: False (0.18300884439221987)
- opportunity: False (0.18300884439221987)

### Scrivine
- mean: False (0.18713271925004393)
- motive: False (0.20753573940928616)
- opportunity: False (0.16184943767453575)

### Sgt. O'Hennessey
- mean: False (0.31912135593696744)
- motive: False (0.1666753892745816)
- opportunity: False (0.1877276330809664)

### Sgt.Valance
- mean: True (0.8300437877296776)
- motive: True (0.9598374351134399)
- opportunity: True (0.9022656660556747)

The culprit is Sgt.Valance.
In fact, it is Sgt.Valance.
## 5minutemystery-flying-saucer-of-new-mexico
Dora is guilty: True or False?
True (0.9773275850444884)
Dora is not guilty: True or False?
True (0.9682013404912752)
Dora has mean: True or False?
True (0.9029524325377104)
Dora has no mean: True or False?
True (0.7662936378892937)
Dora has motive: True or False?
True (0.9683812839782183)
Dora has no motive: True or False?
True (0.8529354946829077)
Dora has opportunity: True or False?
True (0.8872045854516336)
Dora has no opportunity: True or False?
True (0.686790355176806)
Lester is guilty: True or False?
True (0.9892752166033384)
Lester is not guilty: True or False?
True (0.9853279586783672)
Lester has mean: True or False?
True (0.9614615446058614)
Lester has no mean: True or False?
True (0.8701565303520181)
Lester has motive: True or False?
True (0.9903430339413316)
Lester has no motive: True or False?
True (0.955152093302995)
Lester has opportunity: True or False?
True (0.9565531009888748)
Lester has no opportunity: True or False?
True (0.9039744767757508)
Uncle Art is guilty: True or False?
True (0.966726063403815)
Uncle Art is not guilty: True or False?
True (0.9802052373824002)
Uncle Art has mean: True or False?
True (0.9274947043807324)
Uncle Art has no mean: True or False?
True (0.8757870204368676)
Uncle Art has motive: True or False?
True (0.9736947425622681)
Uncle Art has no motive: True or False?
True (0.9362850185952675)

Map:  15%|█▍        | 30/203 [36:16<3:36:55, 75.23s/ examples]
Map:  15%|█▌        | 31/203 [37:43<3:45:31, 78.67s/ examples]
Map:  16%|█▌        | 32/203 [39:20<4:00:30, 84.39s/ examples]Uncle Art has opportunity: True or False?
True (0.9329437018480795)
Uncle Art has no opportunity: True or False?
True (0.789233749534095)
Zach is guilty: True or False?
True (0.96920782287766)
Zach is not guilty: True or False?
True (0.9759922628972598)
Zach has mean: True or False?
True (0.8951566249612815)
Zach has no mean: True or False?
True (0.7911764307711107)
Zach has motive: True or False?
True (0.9606574760904091)
Zach has no motive: True or False?
True (0.748352221542477)
Zach has opportunity: True or False?
True (0.8982321647536474)
Zach has no opportunity: True or False?
True (0.6297746298200823)
### Dora
- mean: False (0.23370636211070628)
- motive: False (0.14706450531709225)
- opportunity: False (0.313209644823194)

### Lester
- mean: True (0.9614615446058614)
- motive: True (0.9903430339413316)
- opportunity: True (0.9565531009888748)

### Uncle Art
- mean: False (0.12421297956313238)
- motive: False (0.06371498140473253)
- opportunity: False (0.21076625046590503)

### Zach
- mean: False (0.20882356922888934)
- motive: False (0.25164777845752295)
- opportunity: False (0.37022537017991775)

The culprit is Lester.
In fact, it is Dora.
## 5minutemystery-great-musket-mystery
Lyle Day is guilty: True or False?
True (0.9532750262379774)
Lyle Day is not guilty: True or False?
True (0.9697281117313339)
Lyle Day has mean: True or False?
True (0.9184802773231918)
Lyle Day has no mean: True or False?
True (0.9312127242200585)
Lyle Day has motive: True or False?
True (0.9653158197836269)
Lyle Day has no motive: True or False?
True (0.946497859305556)
Lyle Day has opportunity: True or False?
True (0.8998277786460391)
Lyle Day has no opportunity: True or False?
True (0.8795611817678315)
Mary Wright is guilty: True or False?
True (0.925499741040984)
Mary Wright is not guilty: True or False?
True (0.9317114972308657)
Mary Wright has mean: True or False?
True (0.9026095892260383)
Mary Wright has no mean: True or False?
True (0.934872446722342)
Mary Wright has motive: True or False?
True (0.9537081113927965)
Mary Wright has no motive: True or False?
True (0.9246876822649571)
Mary Wright has opportunity: True or False?
True (0.9534487112250288)
Mary Wright has no opportunity: True or False?
True (0.9032942081209032)
Paul Revere is guilty: True or False?
True (0.9443823686645129)
Paul Revere is not guilty: True or False?
True (0.9580695040202324)
Paul Revere has mean: True or False?
True (0.8973360043541736)
Paul Revere has no mean: True or False?
True (0.9022657265573043)
Paul Revere has motive: True or False?
True (0.9203612233366507)
Paul Revere has no motive: True or False?
True (0.7931058945535956)
Paul Revere has opportunity: True or False?
True (0.9237300130783155)
Paul Revere has no opportunity: True or False?
True (0.7924642605907138)
Stevie Brown is guilty: True or False?
True (0.9494823209990744)
Stevie Brown is not guilty: True or False?
True (0.966537058600438)
Stevie Brown has mean: True or False?
True (0.9746769070949022)
Stevie Brown has no mean: True or False?
True (0.9630919110597987)
Stevie Brown has motive: True or False?
True (0.9655114412719658)
Stevie Brown has no motive: True or False?
True (0.9022656660556747)
Stevie Brown has opportunity: True or False?
True (0.9400235399552953)
Stevie Brown has no opportunity: True or False?
True (0.8469578650997759)
### Lyle Day
- mean: True (0.9184802773231918)
- motive: True (0.9653158197836269)
- opportunity: True (0.8998277786460391)

### Mary Wright
- mean: True (0.9026095892260383)
- motive: False (0.07531231773504288)
- opportunity: False (0.09670579187909678)

### Paul Revere
- mean: True (0.8973360043541736)
- motive: False (0.2068941054464044)
- opportunity: False (0.20753573940928616)

### Stevie Brown
- mean: False (0.036908088940201256)
- motive: False (0.09773433394432529)
- opportunity: False (0.1530421349002241)

The culprit is Lyle Day.
In fact, it is Lyle Day.
## 5minutemystery-true-green-a-st-patricks-day-mystery
Emily Carpenter is guilty: True or False?
True (0.8519527857346616)
Emily Carpenter is not guilty: True or False?
True (0.8914335992201801)
Emily Carpenter has mean: True or False?
True (0.7114308541703346)
Emily Carpenter has no mean: True or False?
True (0.8423451152856819)
Emily Carpenter has motive: True or False?
True (0.9320833668388808)
Emily Carpenter has no motive: True or False?
True (0.6654105788791005)
Emily Carpenter has opportunity: True or False?
True (0.7655933544531522)
Emily Carpenter has no opportunity: True or False?
False (0.5535053004623279)
Evan Carpenter is guilty: True or False?
True (0.9041439284393449)
Evan Carpenter is not guilty: True or False?
True (0.8991213421091365)
Evan Carpenter has mean: True or False?
True (0.6757646168022439)
Evan Carpenter has no mean: True or False?
True (0.8104789202520752)
Evan Carpenter has motive: True or False?
True (0.9528381834886748)
Evan Carpenter has no motive: True or False?
True (0.7994423454932595)
Evan Carpenter has opportunity: True or False?
True (0.8392075831473667)
Evan Carpenter has no opportunity: True or False?
True (0.5009765603034438)
Richie Harris is guilty: True or False?
True (0.8267117710471246)
Richie Harris is not guilty: True or False?
True (0.9053223122169206)
Richie Harris has mean: True or False?
True (0.6967842494573921)
Richie Harris has no mean: True or False?
True (0.7193836643711469)
Richie Harris has motive: True or False?
True (0.914290668913133)
Richie Harris has no motive: True or False?
True (0.648688963544537)
Richie Harris has opportunity: True or False?
True (0.8255897087847518)
Richie Harris has no opportunity: True or False?
True (0.49999999904767284)
Zachary MacDonald is guilty: True or False?
True (0.8469578650997759)
Zachary MacDonald is not guilty: True or False?
True (0.8233283740192667)
Zachary MacDonald has mean: True or False?
True (0.5879430860094185)
Zachary MacDonald has no mean: True or False?
True (0.6197014353942354)
Zachary MacDonald has motive: True or False?
True (0.9237300750192418)
Zachary MacDonald has no motive: True or False?
True (0.5573634465789677)
Zachary MacDonald has opportunity: True or False?
True (0.7416740115009234)
Zachary MacDonald has no opportunity: True or False?
False (0.7209580648179327)
### Emily Carpenter
- mean: True (0.7114308541703346)
- motive: True (0.9320833668388808)
- opportunity: True (0.7655933544531522)

### Evan Carpenter
- mean: True (0.6757646168022439)
- motive: False (0.20055765450674046)
- opportunity: False (0.49902343969655616)

### Richie Harris
- mean: True (0.6967842494573921)
- motive: False (0.351311036455463)
- opportunity: False (0.5000000009523271)

### Zachary MacDonald
- mean: True (0.5879430860094185)
- motive: False (0.44263655342103225)
- opportunity: True (0.7416740115009234)

The culprit is Emily Carpenter.
In fact, it is Emily Carpenter.
## 5minutemystery-st-patricks-day-pearls
Christopher is guilty: True or False?
True (0.9456006903352807)
Christopher is not guilty: True or False?
True (0.9596109393754703)
Christopher has mean: True or False?
True (0.921357630313903)
Christopher has no mean: True or False?
True (0.9193533657123177)
Christopher has motive: True or False?
True (0.9825574747001844)
Christopher has no motive: True or False?
True (0.9481545078856665)
Christopher has opportunity: True or False?
True (0.9842760556568076)
Christopher has no opportunity: True or False?
True (0.9741412398478105)
Earl is guilty: True or False?
True (0.9158089188126235)
Earl is not guilty: True or False?
True (0.9437636745681832)
Earl has mean: True or False?
True (0.9405717864730483)
Earl has no mean: True or False?
True (0.8828325273478573)
Earl has motive: True or False?
True (0.9750121835371013)
Earl has no motive: True or False?
True (0.9433475737015985)
Earl has opportunity: True or False?
True (0.9851003883001379)
Earl has no opportunity: True or False?
True (0.9656413200400066)
Robert is guilty: True or False?
True (0.8774767496170098)
Robert is not guilty: True or False?
True (0.9295683483415352)
Robert has mean: True or False?
True (0.8670357473609658)
Robert has no mean: True or False?
True (0.8906751280163339)
Robert has motive: True or False?
True (0.9651191233711941)

Map:  16%|█▋        | 33/203 [40:29<3:45:16, 79.51s/ examples]
Map:  17%|█▋        | 34/203 [41:47<3:42:42, 79.07s/ examples]
Map:  17%|█▋        | 35/203 [42:42<3:21:05, 71.82s/ examples]Robert has no motive: True or False?
True (0.9268352400785028)
Robert has opportunity: True or False?
True (0.9680204387474981)
Robert has no opportunity: True or False?
True (0.9558166865608263)
Tom is guilty: True or False?
True (0.940789698413215)
Tom is not guilty: True or False?
True (0.9631612907883619)
Tom has mean: True or False?
True (0.9717254050158363)
Tom has no mean: True or False?
True (0.9414392129817035)
Tom has motive: True or False?
True (0.9878996018169273)
Tom has no motive: True or False?
True (0.972830772390074)
Tom has opportunity: True or False?
True (0.9805806282390328)
Tom has no opportunity: True or False?
True (0.9669139993413022)
### Christopher
- mean: True (0.921357630313903)
- motive: True (0.9825574747001844)
- opportunity: True (0.9842760556568076)

### Earl
- mean: False (0.11716747265214267)
- motive: False (0.056652426298401504)
- opportunity: False (0.03435867995999342)

### Robert
- mean: True (0.8670357473609658)
- motive: False (0.07316475992149718)
- opportunity: False (0.0441833134391737)

### Tom
- mean: False (0.05856078701829648)
- motive: False (0.027169227609926017)
- opportunity: False (0.03308600065869782)

The culprit is Christopher.
In fact, it is Tom.
## 5minutemystery-death-in-the-theatre
Helen Smith is guilty: True or False?
True (0.7364006034245382)
Helen Smith is not guilty: True or False?
True (0.7541915239138703)
Helen Smith has mean: True or False?
True (0.8216173667955227)
Helen Smith has no mean: True or False?
True (0.7872777601997338)
Helen Smith has motive: True or False?
True (0.9114953293645017)
Helen Smith has no motive: True or False?
True (0.7931058945535956)
Helen Smith has opportunity: True or False?
True (0.9155072554665495)
Helen Smith has no opportunity: True or False?
True (0.6749080895533367)
Joanne Driscoll is guilty: True or False?
True (0.7876046283319926)
Joanne Driscoll is not guilty: True or False?
True (0.833053108978257)
Joanne Driscoll has mean: True or False?
True (0.8701565303520181)
Joanne Driscoll has no mean: True or False?
True (0.861538171568877)
Joanne Driscoll has motive: True or False?
True (0.8955227118091885)
Joanne Driscoll has no motive: True or False?
True (0.8152325155686644)
Joanne Driscoll has opportunity: True or False?
True (0.8940517282497483)
Joanne Driscoll has no opportunity: True or False?
True (0.7416740115009234)
Kevin Doyle is guilty: True or False?
True (0.702530072932436)
Kevin Doyle is not guilty: True or False?
True (0.7178037814283548)
Kevin Doyle has mean: True or False?
True (0.7950222460539826)
Kevin Doyle has no mean: True or False?
True (0.776622945813876)
Kevin Doyle has motive: True or False?
True (0.8433797899747144)
Kevin Doyle has no motive: True or False?
True (0.5907792634380938)
Kevin Doyle has opportunity: True or False?
True (0.7676898810056793)
Kevin Doyle has no opportunity: True or False?
False (0.5409238971378262)
Sarah Jones is guilty: True or False?
True (0.8989440778839496)
Sarah Jones is not guilty: True or False?
True (0.9015745518914653)
Sarah Jones has mean: True or False?
True (0.8418256636710214)
Sarah Jones has no mean: True or False?
True (0.8193157928301305)
Sarah Jones has motive: True or False?
True (0.9335520893498362)
Sarah Jones has no motive: True or False?
True (0.8140528237853677)
Sarah Jones has opportunity: True or False?
True (0.9073122118500465)
Sarah Jones has no opportunity: True or False?
True (0.7065955344877805)
### Helen Smith
- mean: False (0.21272223980026617)
- motive: False (0.2068941054464044)
- opportunity: False (0.3250919104466633)

### Joanne Driscoll
- mean: False (0.13846182843112298)
- motive: False (0.18476748443133562)
- opportunity: False (0.2583259884990766)

### Kevin Doyle
- mean: True (0.7950222460539826)
- motive: True (0.8433797899747144)
- opportunity: True (0.7676898810056793)

### Sarah Jones
- mean: False (0.18068420716986955)
- motive: False (0.1859471762146323)
- opportunity: False (0.29340446551221955)

The culprit is Kevin Doyle.
In fact, it is Kevin Doyle.
## 5minutemystery-death-at-andersonville
Corporal Wardlow Horner is guilty: True or False?
True (0.9599126594957205)
Corporal Wardlow Horner is not guilty: True or False?
True (0.9632304925109479)
Corporal Wardlow Horner has mean: True or False?
True (0.9149009617112335)
Corporal Wardlow Horner has no mean: True or False?
True (0.900179384114949)
Corporal Wardlow Horner has motive: True or False?
True (0.9917323586955374)
Corporal Wardlow Horner has no motive: True or False?
True (0.9630919110597987)
Corporal Wardlow Horner has opportunity: True or False?
True (0.9660280346390409)
Corporal Wardlow Horner has no opportunity: True or False?
True (0.9029524325377104)
Private Jamie Whisenant is guilty: True or False?
True (0.9513234509300917)
Private Jamie Whisenant is not guilty: True or False?
True (0.9487275499225403)
Private Jamie Whisenant has mean: True or False?
True (0.9086179121100144)
Private Jamie Whisenant has no mean: True or False?
True (0.9224823751318276)
Private Jamie Whisenant has motive: True or False?
True (0.9868280288485443)
Private Jamie Whisenant has no motive: True or False?
True (0.9532750262379774)
Private Jamie Whisenant has opportunity: True or False?
True (0.9580694433457548)
Private Jamie Whisenant has no opportunity: True or False?
True (0.9388008138003494)
Sergeant Coleman Crosby is guilty: True or False?
True (0.8852351930010195)
Sergeant Coleman Crosby is not guilty: True or False?
True (0.9136765013387816)
Sergeant Coleman Crosby has mean: True or False?
True (0.851212260635415)
Sergeant Coleman Crosby has no mean: True or False?
True (0.7813306496768853)
Sergeant Coleman Crosby has motive: True or False?
True (0.9767802359728407)
Sergeant Coleman Crosby has no motive: True or False?
True (0.8098781635062345)
Sergeant Coleman Crosby has opportunity: True or False?
True (0.8875948773562923)
Sergeant Coleman Crosby has no opportunity: True or False?
True (0.6671476985798853)
Sergeant Josiah Thornton is guilty: True or False?
True (0.9349913039165801)
Sergeant Josiah Thornton is not guilty: True or False?
True (0.9349912412205296)
Sergeant Josiah Thornton has mean: True or False?
True (0.9161096235973493)
Sergeant Josiah Thornton has no mean: True or False?
True (0.7431679939957333)
Sergeant Josiah Thornton has motive: True or False?
True (0.9851717948106439)
Sergeant Josiah Thornton has no motive: True or False?
True (0.7988152492192591)
Sergeant Josiah Thornton has opportunity: True or False?
True (0.9086179121100144)
Sergeant Josiah Thornton has no opportunity: True or False?
True (0.6714705301843162)
### Corporal Wardlow Horner
- mean: False (0.09982061588505098)
- motive: False (0.036908088940201256)
- opportunity: False (0.0970475674622896)

### Private Jamie Whisenant
- mean: True (0.9086179121100144)
- motive: True (0.9868280288485443)
- opportunity: True (0.9580694433457548)

### Sergeant Coleman Crosby
- mean: False (0.21866935032311474)
- motive: False (0.19012183649376546)
- opportunity: False (0.3328523014201147)

### Sergeant Josiah Thornton
- mean: False (0.2568320060042667)
- motive: False (0.20118475078074094)
- opportunity: False (0.32852946981568376)

The culprit is Private Jamie Whisenant.
In fact, it is Sergeant Josiah Thornton.
## 5minutemystery-the-big-game
Carli Antor is guilty: True or False?
True (0.893866539303124)
Carli Antor is not guilty: True or False?
True (0.9144436723393062)
Carli Antor has mean: True or False?
True (0.789233749534095)
Carli Antor has no mean: True or False?
True (0.6415346823638186)
Carli Antor has motive: True or False?
True (0.943970619289785)
Carli Antor has no motive: True or False?
True (0.8250265073476026)
Carli Antor has opportunity: True or False?
True (0.945399403620829)
Carli Antor has no opportunity: True or False?
True (0.7162185953247016)
Chuck Jarrett is guilty: True or False?
True (0.8169911556077801)
Chuck Jarrett is not guilty: True or False?
True (0.8982321045224891)
Chuck Jarrett has mean: True or False?
True (0.6334102104891195)
Chuck Jarrett has no mean: True or False?
False (0.5822535180679596)
Chuck Jarrett has motive: True or False?
True (0.9484418035658785)

Map:  18%|█▊        | 36/203 [43:47<3:14:57, 70.05s/ examples]
Map:  18%|█▊        | 37/203 [44:42<3:00:57, 65.41s/ examples]
Map:  19%|█▊        | 38/203 [45:32<2:47:17, 60.83s/ examples]Chuck Jarrett has no motive: True or False?
True (0.7931059536445917)
Chuck Jarrett has opportunity: True or False?
True (0.8714748565614324)
Chuck Jarrett has no opportunity: True or False?
True (0.5888891620166576)
Rich Pender is guilty: True or False?
True (0.8074605993751186)
Rich Pender is not guilty: True or False?
True (0.8643104392003704)
Rich Pender has mean: True or False?
True (0.6513548405484016)
Rich Pender has no mean: True or False?
False (0.5370414382302919)
Rich Pender has motive: True or False?
True (0.942400812874096)
Rich Pender has no motive: True or False?
True (0.8459424357871997)
Rich Pender has opportunity: True or False?
True (0.9249593046682986)
Rich Pender has no opportunity: True or False?
True (0.7704647687904915)
Tom Barrett is guilty: True or False?
True (0.7472472734767229)
Tom Barrett is not guilty: True or False?
True (0.8899121304559661)
Tom Barrett has mean: True or False?
True (0.7752646804088963)
Tom Barrett has no mean: True or False?
True (0.5926665645259142)
Tom Barrett has motive: True or False?
True (0.9378968460746586)
Tom Barrett has no motive: True or False?
True (0.8499711693725173)
Tom Barrett has opportunity: True or False?
True (0.9567959302164903)
Tom Barrett has no opportunity: True or False?
True (0.646013666311734)
### Carli Antor
- mean: False (0.3584653176361814)
- motive: False (0.17497349265239737)
- opportunity: False (0.28378140467529844)

### Chuck Jarrett
- mean: True (0.6334102104891195)
- motive: False (0.2068940463554083)
- opportunity: False (0.41111083798334236)

### Rich Pender
- mean: True (0.6513548405484016)
- motive: True (0.942400812874096)
- opportunity: True (0.9249593046682986)

### Tom Barrett
- mean: False (0.40733343547408585)
- motive: False (0.15002883062748273)
- opportunity: False (0.35398633368826604)

The culprit is Rich Pender.
In fact, it is Tom Barrett.
## 5minutemystery-the-liberty-gun
Bob Turkle is guilty: True or False?
True (0.8568122429692968)
Bob Turkle is not guilty: True or False?
True (0.8969755785184792)
Bob Turkle has mean: True or False?
True (0.8402590129647053)
Bob Turkle has no mean: True or False?
True (0.8732147785405174)
Bob Turkle has motive: True or False?
True (0.9079671476237222)
Bob Turkle has no motive: True or False?
True (0.9063220605956304)
Bob Turkle has opportunity: True or False?
True (0.7962924261546153)
Bob Turkle has no opportunity: True or False?
True (0.7872777601997338)
Captain Parker is guilty: True or False?
True (0.8444089912414552)
Captain Parker is not guilty: True or False?
True (0.9246876822649571)
Captain Parker has mean: True or False?
True (0.8381505623254643)
Captain Parker has no mean: True or False?
True (0.8670357473609658)
Captain Parker has motive: True or False?
True (0.9418684262191025)
Captain Parker has no motive: True or False?
True (0.934155284694701)
Captain Parker has opportunity: True or False?
True (0.8683809699466569)
Captain Parker has no opportunity: True or False?
True (0.8596637847360897)
Paul Rhodes is guilty: True or False?
True (0.8333246107254184)
Paul Rhodes is not guilty: True or False?
True (0.9280183890155084)
Paul Rhodes has mean: True or False?
True (0.9036349079321685)
Paul Rhodes has no mean: True or False?
True (0.9336731438527403)
Paul Rhodes has motive: True or False?
True (0.9638480560973683)
Paul Rhodes has no motive: True or False?
True (0.9525741334779666)
Paul Rhodes has opportunity: True or False?
True (0.8887587777822111)
Paul Rhodes has no opportunity: True or False?
True (0.8360197583769845)
Tom Wise is guilty: True or False?
True (0.8879840376027315)
Tom Wise is not guilty: True or False?
True (0.9401335713518422)
Tom Wise has mean: True or False?
True (0.8539127077831877)
Tom Wise has no mean: True or False?
True (0.9233161821369215)
Tom Wise has motive: True or False?
True (0.9613891248869872)
Tom Wise has no motive: True or False?
True (0.9376689781587124)
Tom Wise has opportunity: True or False?
True (0.8925625120974553)
Tom Wise has no opportunity: True or False?
True (0.8370879250561812)
### Bob Turkle
- mean: True (0.8402590129647053)
- motive: True (0.9079671476237222)
- opportunity: True (0.7962924261546153)

### Captain Parker
- mean: True (0.8381505623254643)
- motive: False (0.065844715305299)
- opportunity: False (0.14033621526391027)

### Paul Rhodes
- mean: True (0.9036349079321685)
- motive: False (0.0474258665220334)
- opportunity: False (0.1639802416230155)

### Tom Wise
- mean: True (0.8539127077831877)
- motive: False (0.06233102184128758)
- opportunity: False (0.16291207494381876)

The culprit is Bob Turkle.
In fact, it is Captain Parker.
## 5minutemystery-summer-camp
Allie is guilty: True or False?
True (0.8820219652716884)
Allie is not guilty: True or False?
True (0.8338664134858856)
Allie has mean: True or False?
True (0.844921525814193)
Allie has no mean: True or False?
True (0.6469064338453809)
Allie has motive: True or False?
True (0.9334308488586655)
Allie has no motive: True or False?
True (0.8198933606225757)
Allie has opportunity: True or False?
True (0.844921525814193)
Allie has no opportunity: True or False?
True (0.7704647687904915)
Danny is guilty: True or False?
True (0.913058338092082)
Danny is not guilty: True or False?
True (0.9086179121100144)
Danny has mean: True or False?
True (0.8349459127213729)
Danny has no mean: True or False?
True (0.6379334932841956)
Danny has motive: True or False?
True (0.9822537304185777)
Danny has no motive: True or False?
True (0.8438950825214144)
Danny has opportunity: True or False?
True (0.9268352400785028)
Danny has no opportunity: True or False?
True (0.7786493288700866)
Diane's campers is guilty: True or False?
True (0.9317114972308657)
Diane's campers is not guilty: True or False?
True (0.8679338697256817)
Diane's campers has mean: True or False?
True (0.8333246107254184)
Diane's campers has no mean: True or False?
False (0.503906199448032)
Diane's campers has motive: True or False?
True (0.9294403817764149)
Diane's campers has no motive: True or False?
True (0.6397360437814448)
Diane's campers has opportunity: True or False?
True (0.794384956668203)
Diane's campers has no opportunity: True or False?
False (0.6001883144765984)
Tom is guilty: True or False?
True (0.8947894610946939)
Tom is not guilty: True or False?
True (0.9082930704920021)
Tom has mean: True or False?
True (0.8812066389307215)
Tom has no mean: True or False?
True (0.642432441257838)
Tom has motive: True or False?
True (0.9769347912465448)
Tom has no motive: True or False?
True (0.8509647293237851)
Tom has opportunity: True or False?
True (0.8929365260632085)
Tom has no opportunity: True or False?
True (0.7225269746614925)
### Allie
- mean: False (0.35309356615461907)
- motive: False (0.18010663937742433)
- opportunity: False (0.22953523120950847)

### Danny
- mean: False (0.3620665067158044)
- motive: False (0.15610491747858557)
- opportunity: False (0.22135067112991336)

### Diane's campers
- mean: True (0.8333246107254184)
- motive: True (0.9294403817764149)
- opportunity: True (0.794384956668203)

### Tom
- mean: False (0.35756755874216195)
- motive: False (0.14903527067621491)
- opportunity: False (0.2774730253385075)

The culprit is Diane's campers.
In fact, it is Tom.
## 5minutemystery-mystery-at-lyndleys-fort
Bo is guilty: True or False?
True (0.9053223122169206)
Bo is not guilty: True or False?
True (0.9219218506394821)
Bo has mean: True or False?
True (0.5185462156586879)
Bo has no mean: True or False?
True (0.7885832152749314)
Bo has motive: True or False?
True (0.8484706895507578)
Bo has no motive: True or False?
True (0.8596637847360897)
Bo has opportunity: True or False?
True (0.6029971163050526)
Bo has no opportunity: True or False?
True (0.7090191831682278)
John is guilty: True or False?
True (0.9401335713518422)
John is not guilty: True or False?
True (0.9554855815192022)
John has mean: True or False?
False (0.5708098341193941)
John has no mean: True or False?
True (0.794384956668203)
John has motive: True or False?
True (0.8795611817678315)
John has no motive: True or False?
True (0.8333246107254184)
John has opportunity: True or False?
True (0.570809902165233)

Map:  19%|█▉        | 39/203 [46:43<2:54:09, 63.72s/ examples]
Map:  20%|█▉        | 40/203 [47:30<2:39:50, 58.84s/ examples]
Map:  20%|██        | 41/203 [48:43<2:49:55, 62.93s/ examples]John has no opportunity: True or False?
True (0.5592900581575188)
John's wife is guilty: True or False?
True (0.8305941261447712)
John's wife is not guilty: True or False?
True (0.8910549899564296)
John's wife has mean: True or False?
True (0.60859406896259)
John's wife has no mean: True or False?
True (0.6067314814064781)
John's wife has motive: True or False?
True (0.6306849143569856)
John's wife has no motive: True or False?
True (0.6361271113853048)
John's wife has opportunity: True or False?
True (0.7122321792841629)
John's wife has no opportunity: True or False?
True (0.612309626324874)
Nathan Drew is guilty: True or False?
True (0.8519527857346616)
Nathan Drew is not guilty: True or False?
True (0.9193534273597669)
Nathan Drew has mean: True or False?
True (0.6242935037467142)
Nathan Drew has no mean: True or False?
True (0.7090191197769757)
Nathan Drew has motive: True or False?
True (0.8370879250561812)
Nathan Drew has no motive: True or False?
True (0.7225270177274575)
Nathan Drew has opportunity: True or False?
True (0.6706082735718226)
Nathan Drew has no opportunity: True or False?
True (0.6495786332146115)
### Bo
- mean: True (0.5185462156586879)
- motive: True (0.8484706895507578)
- opportunity: True (0.6029971163050526)

### John
- mean: False (0.5708098341193941)
- motive: False (0.1666753892745816)
- opportunity: False (0.44070994184248125)

### John's wife
- mean: False (0.39326851859352185)
- motive: True (0.6306849143569856)
- opportunity: False (0.38769037367512604)

### Nathan Drew
- mean: True (0.6242935037467142)
- motive: False (0.27747298227254247)
- opportunity: False (0.3504213667853885)

The culprit is Bo.
In fact, it is Nathan Drew.
## 5minutemystery-riddle-of-the-confederate-spy
Garrett is guilty: True or False?
True (0.94519740270931)
Garrett is not guilty: True or False?
True (0.9302051049548884)
Garrett has mean: True or False?
True (0.8128672807499561)
Garrett has no mean: True or False?
True (0.6976089520497016)
Garrett has motive: True or False?
True (0.9589241138134527)
Garrett has no motive: True or False?
True (0.8134607635851566)
Garrett has opportunity: True or False?
True (0.8289388437432279)
Garrett has no opportunity: True or False?
True (0.8116760258690822)
McMurty is guilty: True or False?
True (0.9697853917136491)
McMurty is not guilty: True or False?
True (0.9548162209309636)
McMurty has mean: True or False?
True (0.8407825844829613)
McMurty has no mean: True or False?
True (0.720171518230031)
McMurty has motive: True or False?
True (0.9637799266082508)
McMurty has no motive: True or False?
True (0.8289387819824735)
McMurty has opportunity: True or False?
True (0.897695304229796)
McMurty has no opportunity: True or False?
True (0.8674854614419002)
Parker is guilty: True or False?
True (0.9485372300670596)
Parker is not guilty: True or False?
True (0.9697854513237307)
Parker has mean: True or False?
True (0.811078188867804)
Parker has no mean: True or False?
True (0.7556369876990674)
Parker has motive: True or False?
True (0.9429285510753684)
Parker has no motive: True or False?
True (0.8494724067948436)
Parker has opportunity: True or False?
True (0.9429286143036572)
Parker has no opportunity: True or False?
True (0.9385759849623091)
Winslow is guilty: True or False?
True (0.9745318884872003)
Winslow is not guilty: True or False?
True (0.9735944874605075)
Winslow has mean: True or False?
True (0.8987665204865408)
Winslow has no mean: True or False?
True (0.8370879250561812)
Winslow has motive: True or False?
True (0.9599877610290866)
Winslow has no motive: True or False?
True (0.8529354311342636)
Winslow has opportunity: True or False?
True (0.9238675252821831)
Winslow has no opportunity: True or False?
True (0.862930245043327)
### Garrett
- mean: False (0.30239104795029836)
- motive: False (0.18653923641484338)
- opportunity: False (0.18832397413091784)

### McMurty
- mean: False (0.279828481769969)
- motive: False (0.1710612180175265)
- opportunity: False (0.1325145385580998)

### Parker
- mean: True (0.811078188867804)
- motive: True (0.9429285510753684)
- opportunity: True (0.9429286143036572)

### Winslow
- mean: False (0.16291207494381876)
- motive: False (0.14706456886573638)
- opportunity: False (0.13706975495667295)

The culprit is Parker.
In fact, it is Parker.
## 5minutemystery-thin-ice
Hortence Lacombe is guilty: True or False?
True (0.9181873182746905)
Hortence Lacombe is not guilty: True or False?
True (0.8966140148346177)
Hortence Lacombe has mean: True or False?
True (0.612309626324874)
Hortence Lacombe has no mean: True or False?
False (0.597373048111048)
Hortence Lacombe has motive: True or False?
True (0.9119668603126158)
Hortence Lacombe has no motive: True or False?
True (0.720171518230031)
Hortence Lacombe has opportunity: True or False?
True (0.595492552580428)
Hortence Lacombe has no opportunity: True or False?
False (0.7017130830397807)
Joe Tucker is guilty: True or False?
True (0.9448931235445592)
Joe Tucker is not guilty: True or False?
True (0.8464508054137014)
Joe Tucker has mean: True or False?
True (0.7826625131049049)
Joe Tucker has no mean: True or False?
True (0.6540113633452196)
Joe Tucker has motive: True or False?
True (0.9361683754137716)
Joe Tucker has no motive: True or False?
True (0.7248702601920561)
Joe Tucker has opportunity: True or False?
True (0.7655934000860735)
Joe Tucker has no opportunity: True or False?
False (0.6039318499573872)
Mikey Chanowski is guilty: True or False?
True (0.9442796704001448)
Mikey Chanowski is not guilty: True or False?
True (0.8812065732757132)
Mikey Chanowski has mean: True or False?
True (0.7170118721569225)
Mikey Chanowski has no mean: True or False?
True (0.6834194581047349)
Mikey Chanowski has motive: True or False?
True (0.9576753972844966)
Mikey Chanowski has no motive: True or False?
True (0.7476159279883341)
Mikey Chanowski has opportunity: True or False?
True (0.7937461674149602)
Mikey Chanowski has no opportunity: True or False?
False (0.5058591351869154)
Shea Callaghan is guilty: True or False?
True (0.9375546563206157)
Shea Callaghan is not guilty: True or False?
True (0.8936811689868521)
Shea Callaghan has mean: True or False?
True (0.7154240000492645)
Shea Callaghan has no mean: True or False?
True (0.5486734660889085)
Shea Callaghan has motive: True or False?
True (0.9026095892260383)
Shea Callaghan has no motive: True or False?
True (0.5851012033999957)
Shea Callaghan has opportunity: True or False?
True (0.7041600870830834)
Shea Callaghan has no opportunity: True or False?
False (0.6909763109505791)
### Hortence Lacombe
- mean: True (0.612309626324874)
- motive: True (0.9119668603126158)
- opportunity: True (0.595492552580428)

### Joe Tucker
- mean: False (0.3459886366547804)
- motive: False (0.27512973980794386)
- opportunity: True (0.7655934000860735)

### Mikey Chanowski
- mean: False (0.3165805418952651)
- motive: False (0.2523840720116659)
- opportunity: True (0.7937461674149602)

### Shea Callaghan
- mean: False (0.45132653391109145)
- motive: False (0.4148987966000043)
- opportunity: True (0.7041600870830834)

The culprit is Hortence Lacombe.
In fact, it is Shea Callaghan.
## 5minutemystery-flouted
Chloe Streamer is guilty: True or False?
True (0.9455001349615358)
Chloe Streamer is not guilty: True or False?
True (0.9695556762577888)
Chloe Streamer has mean: True or False?
True (0.8766343647921183)
Chloe Streamer has no mean: True or False?
True (0.7866228249849953)
Chloe Streamer has motive: True or False?
True (0.9593832497641647)
Chloe Streamer has no motive: True or False?
True (0.9216401608061056)
Chloe Streamer has opportunity: True or False?
True (0.884439109617765)
Chloe Streamer has no opportunity: True or False?
True (0.7461389980806673)
Lyle Esposito is guilty: True or False?
True (0.9672868854836233)
Lyle Esposito is not guilty: True or False?
True (0.9736947425622681)
Lyle Esposito has mean: True or False?
True (0.851212260635415)
Lyle Esposito has no mean: True or False?
True (0.8444089912414552)
Lyle Esposito has motive: True or False?
True (0.9748211501698323)
Lyle Esposito has no motive: True or False?
True (0.9392480858026054)
Lyle Esposito has opportunity: True or False?
Map:  21%|██        | 42/203 [49:57<2:58:28, 66.51s/ examples]
Map:  21%|██        | 43/203 [50:58<2:52:36, 64.73s/ examples]
Map:  22%|██▏       | 44/203 [52:12<2:58:56, 67.53s/ examples]
True (0.9364014251476122)
Lyle Esposito has no opportunity: True or False?
True (0.7641883982873323)
Marty Nolan is guilty: True or False?
True (0.9540517932883525)
Marty Nolan is not guilty: True or False?
True (0.9616059669560388)
Marty Nolan has mean: True or False?
True (0.8509646659219744)
Marty Nolan has no mean: True or False?
True (0.7577943897558946)
Marty Nolan has motive: True or False?
True (0.9669139993413022)
Marty Nolan has no motive: True or False?
True (0.8944211616820568)
Marty Nolan has opportunity: True or False?
True (0.9489172681310486)
Marty Nolan has no opportunity: True or False?
True (0.8803863464576128)
Susan Moorgate is guilty: True or False?
True (0.9193533657123177)
Susan Moorgate is not guilty: True or False?
True (0.9530133616438526)
Susan Moorgate has mean: True or False?
True (0.6662796150778861)
Susan Moorgate has no mean: True or False?
True (0.6095241816115718)
Susan Moorgate has motive: True or False?
True (0.862930245043327)
Susan Moorgate has no motive: True or False?
True (0.8529354946829077)
Susan Moorgate has opportunity: True or False?
True (0.7008947664177184)
Susan Moorgate has no opportunity: True or False?
True (0.6842640081724978)
### Chloe Streamer
- mean: False (0.21337717501500475)
- motive: False (0.07835983919389444)
- opportunity: False (0.2538610019193327)

### Lyle Esposito
- mean: False (0.1555910087585448)
- motive: False (0.06075191419739456)
- opportunity: False (0.23581160171266768)

### Marty Nolan
- mean: False (0.24220561024410536)
- motive: False (0.10557883831794324)
- opportunity: False (0.11961365354238718)

### Susan Moorgate
- mean: True (0.6662796150778861)
- motive: True (0.862930245043327)
- opportunity: True (0.7008947664177184)

The culprit is Susan Moorgate.
In fact, it is Marty Nolan.
## 5minutemystery-car-trouble
Mr. Carlson is guilty: True or False?
True (0.9162595863469921)
Mr. Carlson is not guilty: True or False?
True (0.8654516347931567)
Mr. Carlson has mean: True or False?
True (0.8608377628023384)
Mr. Carlson has no mean: True or False?
True (0.8418256636710214)
Mr. Carlson has motive: True or False?
True (0.983862637994192)
Mr. Carlson has no motive: True or False?
True (0.9340350654042096)
Mr. Carlson has opportunity: True or False?
True (0.9435559526996434)
Mr. Carlson has no opportunity: True or False?
True (0.8499711693725173)
Mr. Leamington is guilty: True or False?
True (0.9296323035994176)
Mr. Leamington is not guilty: True or False?
True (0.908941745727715)
Mr. Leamington has mean: True or False?
True (0.9063219998220023)
Mr. Leamington has no mean: True or False?
True (0.85729086409805)
Mr. Leamington has motive: True or False?
True (0.9862973096916147)
Mr. Leamington has no motive: True or False?
True (0.9552357186642073)
Mr. Leamington has opportunity: True or False?
True (0.930078152541638)
Mr. Leamington has no opportunity: True or False?
True (0.8591918406281239)
Mrs. Roberts is guilty: True or False?
True (0.8774768149941248)
Mrs. Roberts is not guilty: True or False?
True (0.8504685773080045)
Mrs. Roberts has mean: True or False?
True (0.8314170225049837)
Mrs. Roberts has no mean: True or False?
True (0.7549149897594328)
Mrs. Roberts has motive: True or False?
True (0.9815950994553841)
Mrs. Roberts has no motive: True or False?
True (0.9448931235445592)
Mrs. Roberts has opportunity: True or False?
True (0.8727816933272936)
Mrs. Roberts has no opportunity: True or False?
True (0.8037905715242155)
Randy Peters is guilty: True or False?
True (0.8902941942359355)
Randy Peters is not guilty: True or False?
True (0.8255897087847518)
Randy Peters has mean: True or False?
True (0.7704647687904915)
Randy Peters has no mean: True or False?
True (0.6601724005812412)
Randy Peters has motive: True or False?
True (0.974676967005652)
Randy Peters has no motive: True or False?
True (0.8558511727823209)
Randy Peters has opportunity: True or False?
True (0.9231777821690265)
Randy Peters has no opportunity: True or False?
True (0.6601724005812412)
### Mr. Carlson
- mean: False (0.1581743363289786)
- motive: False (0.06596493459579045)
- opportunity: False (0.15002883062748273)

### Mr. Leamington
- mean: True (0.9063219998220023)
- motive: True (0.9862973096916147)
- opportunity: True (0.930078152541638)

### Mrs. Roberts
- mean: False (0.24508501024056717)
- motive: False (0.05510687645544077)
- opportunity: False (0.1962094284757845)

### Randy Peters
- mean: False (0.33982759941875884)
- motive: False (0.14414882721767908)
- opportunity: False (0.33982759941875884)

The culprit is Mr. Leamington.
In fact, it is Randy Peters.
## 5minutemystery-mr-poes-birthday-party
Anthony is guilty: True or False?
True (0.9466953276900992)
Anthony is not guilty: True or False?
True (0.9586152443144125)
Anthony has mean: True or False?
True (0.8638516611889259)
Anthony has no mean: True or False?
True (0.8316905440184192)
Anthony has motive: True or False?
True (0.9669139993413022)
Anthony has no motive: True or False?
True (0.9346342693191454)
Anthony has opportunity: True or False?
True (0.9284088027271398)
Anthony has no opportunity: True or False?
True (0.9032942081209032)
Connor is guilty: True or False?
True (0.9173026114435064)
Connor is not guilty: True or False?
True (0.9346342066470359)
Connor has mean: True or False?
True (0.8587185689177256)
Connor has no mean: True or False?
True (0.8272706865691472)
Connor has motive: True or False?
True (0.9577544910931239)
Connor has no motive: True or False?
True (0.8787311338092536)
Connor has opportunity: True or False?
True (0.878314250659373)
Connor has no opportunity: True or False?
True (0.8647679145346777)
Skylar is guilty: True or False?
True (0.9692660578747095)
Skylar is not guilty: True or False?
True (0.9740919471316322)
Skylar has mean: True or False?
True (0.905322251510331)
Skylar has no mean: True or False?
True (0.8710367026584496)
Skylar has motive: True or False?
True (0.9824231266498078)
Skylar has no motive: True or False?
True (0.9447913165152162)
Skylar has opportunity: True or False?
True (0.897695304229796)
Skylar has no opportunity: True or False?
True (0.9390248639367113)
Stephen is guilty: True or False?
True (0.9094255002859922)
Stephen is not guilty: True or False?
True (0.9061560624998657)
Stephen has mean: True or False?
True (0.6187804294217345)
Stephen has no mean: True or False?
True (0.7371581232960549)
Stephen has motive: True or False?
True (0.9790757889289493)
Stephen has no motive: True or False?
True (0.9309620298004129)
Stephen has opportunity: True or False?
True (0.8719117627136385)
Stephen has no opportunity: True or False?
True (0.8402589628813668)
Tommy is guilty: True or False?
True (0.9074763663250294)
Tommy is not guilty: True or False?
True (0.9564718616162037)
Tommy has mean: True or False?
True (0.950041474283655)
Tommy has no mean: True or False?
True (0.884439109617765)
Tommy has motive: True or False?
True (0.9735442395649992)
Tommy has no motive: True or False?
True (0.9167080509980843)
Tommy has opportunity: True or False?
True (0.8469578650997759)
Tommy has no opportunity: True or False?
True (0.7745833916423246)
### Anthony
- mean: False (0.16830945598158076)
- motive: False (0.0653657306808546)
- opportunity: False (0.09670579187909678)

### Connor
- mean: False (0.17272931343085285)
- motive: False (0.1212688661907464)
- opportunity: False (0.13523208546532228)

### Skylar
- mean: True (0.905322251510331)
- motive: True (0.9824231266498078)
- opportunity: True (0.897695304229796)

### Stephen
- mean: True (0.6187804294217345)
- motive: False (0.06903797019958713)
- opportunity: False (0.1597410371186332)

### Tommy
- mean: False (0.11556089038223505)
- motive: False (0.08329194900191572)
- opportunity: False (0.2254166083576754)

The culprit is Skylar.
In fact, it is Connor.
## 5minutemystery-the-root-of-all-evil
Bryan Durell is guilty: True or False?
True (0.8128672807499561)
Bryan Durell is not guilty: True or False?
True (0.8464508054137014)
Bryan Durell has mean: True or False?
True (0.6967842494573921)
Bryan Durell has no mean: True or False?
True (0.7178038242127955)
Bryan Durell has motive: True or False?
True (0.9319595674053855)

Map:  22%|██▏       | 45/203 [53:20<2:57:53, 67.55s/ examples]
Map:  23%|██▎       | 46/203 [54:36<3:03:31, 70.13s/ examples]
Map:  23%|██▎       | 47/203 [55:47<3:02:51, 70.33s/ examples]Bryan Durell has no motive: True or False?
True (0.8062431235779619)
Bryan Durell has opportunity: True or False?
True (0.7819972591886313)
Bryan Durell has no opportunity: True or False?
True (0.6808786440630326)
Grieve Collier is guilty: True or False?
True (0.8787311338092536)
Grieve Collier is not guilty: True or False?
True (0.897695304229796)
Grieve Collier has mean: True or False?
True (0.7559974119430289)
Grieve Collier has no mean: True or False?
True (0.7556369876990674)
Grieve Collier has motive: True or False?
True (0.979314505527214)
Grieve Collier has no motive: True or False?
True (0.9105454073245608)
Grieve Collier has opportunity: True or False?
True (0.8563323578093363)
Grieve Collier has no opportunity: True or False?
True (0.7859663967519771)
Jacques Bourbonne is guilty: True or False?
True (0.8297680628665619)
Jacques Bourbonne is not guilty: True or False?
True (0.8407825844829613)
Jacques Bourbonne has mean: True or False?
True (0.7931058945535956)
Jacques Bourbonne has no mean: True or False?
True (0.7690802105138688)
Jacques Bourbonne has motive: True or False?
True (0.9568766339006164)
Jacques Bourbonne has no motive: True or False?
True (0.7833262085677729)
Jacques Bourbonne has opportunity: True or False?
True (0.8433797899747144)
Jacques Bourbonne has no opportunity: True or False?
True (0.5983121871760707)
Ruth Majick is guilty: True or False?
True (0.8122723669190336)
Ruth Majick is not guilty: True or False?
True (0.8484706263347676)
Ruth Majick has mean: True or False?
True (0.8433797899747144)
Ruth Majick has no mean: True or False?
True (0.7994422859301654)
Ruth Majick has motive: True or False?
True (0.935346481802689)
Ruth Majick has no motive: True or False?
True (0.7431679939957333)
Ruth Majick has opportunity: True or False?
True (0.8688268116310761)
Ruth Majick has no opportunity: True or False?
True (0.8000678954040312)
### Bryan Durell
- mean: True (0.6967842494573921)
- motive: False (0.1937568764220381)
- opportunity: False (0.31912135593696744)

### Grieve Collier
- mean: True (0.7559974119430289)
- motive: True (0.979314505527214)
- opportunity: True (0.8563323578093363)

### Jacques Bourbonne
- mean: False (0.23091978948613123)
- motive: False (0.2166737914322271)
- opportunity: False (0.4016878128239293)

### Ruth Majick
- mean: False (0.20055771406983458)
- motive: False (0.2568320060042667)
- opportunity: False (0.19993210459596877)

The culprit is Grieve Collier.
In fact, it is Bryan Durell.
## 5minutemystery-get-the-lead-out
Benjamin Trodger is guilty: True or False?
True (0.9105453462677353)
Benjamin Trodger is not guilty: True or False?
True (0.8056321690561029)
Benjamin Trodger has mean: True or False?
True (0.8770561879413864)
Benjamin Trodger has no mean: True or False?
True (0.6540113633452196)
Benjamin Trodger has motive: True or False?
True (0.9355823382423648)
Benjamin Trodger has no motive: True or False?
True (0.7483522884503825)
Benjamin Trodger has opportunity: True or False?
True (0.9012274173198201)
Benjamin Trodger has no opportunity: True or False?
True (0.5467381591701916)
Cynthia Kirwan is guilty: True or False?
True (0.9152045868398637)
Cynthia Kirwan is not guilty: True or False?
True (0.8591917766133458)
Cynthia Kirwan has mean: True or False?
True (0.7627776774954688)
Cynthia Kirwan has no mean: True or False?
True (0.6048657973050737)
Cynthia Kirwan has motive: True or False?
True (0.942081869103903)
Cynthia Kirwan has no motive: True or False?
True (0.7950222460539826)
Cynthia Kirwan has opportunity: True or False?
True (0.8832359917473193)
Cynthia Kirwan has no opportunity: True or False?
True (0.6654105193867614)
Dan Skinner is guilty: True or False?
True (0.9420819287658885)
Dan Skinner is not guilty: True or False?
True (0.9377830624037258)
Dan Skinner has mean: True or False?
True (0.8352149074858963)
Dan Skinner has no mean: True or False?
True (0.8261514850267767)
Dan Skinner has motive: True or False?
True (0.9627782093174002)
Dan Skinner has no motive: True or False?
True (0.8727817583545995)
Dan Skinner has opportunity: True or False?
True (0.9190632712053527)
Dan Skinner has no opportunity: True or False?
True (0.7090191831682278)
Shel Jonas is guilty: True or False?
True (0.9231777821690265)
Shel Jonas is not guilty: True or False?
True (0.8824278665848695)
Shel Jonas has mean: True or False?
True (0.7786493288700866)
Shel Jonas has no mean: True or False?
True (0.6859494535376744)
Shel Jonas has motive: True or False?
True (0.9403530947748038)
Shel Jonas has no motive: True or False?
True (0.8068526417769779)
Shel Jonas has opportunity: True or False?
True (0.8582439976623328)
Shel Jonas has no opportunity: True or False?
True (0.6934729802503211)
### Benjamin Trodger
- mean: False (0.3459886366547804)
- motive: False (0.2516477115496175)
- opportunity: False (0.45326184082980836)

### Cynthia Kirwan
- mean: False (0.3951342026949263)
- motive: False (0.20497775394601736)
- opportunity: False (0.33458948061323857)

### Dan Skinner
- mean: True (0.8352149074858963)
- motive: True (0.9627782093174002)
- opportunity: True (0.9190632712053527)

### Shel Jonas
- mean: False (0.31405054646232555)
- motive: False (0.1931473582230221)
- opportunity: False (0.3065270197496789)

The culprit is Dan Skinner.
In fact, it is Dan Skinner.
## 5minutemystery-popping-a-wheelie
Cory is guilty: True or False?
True (0.8577681165234065)
Cory is not guilty: True or False?
True (0.8683809699466569)
Cory has mean: True or False?
True (0.6433292707767855)
Cory has no mean: True or False?
True (0.6242935037467142)
Cory has motive: True or False?
True (0.8925625719484378)
Cory has no motive: True or False?
True (0.6531268925247615)
Cory has opportunity: True or False?
True (0.7424216889954057)
Cory has no opportunity: True or False?
False (0.5195212821349473)
David is guilty: True or False?
True (0.8692713407917644)
David is not guilty: True or False?
True (0.7786492592534148)
David has mean: True or False?
True (0.6967841871600284)
David has no mean: True or False?
True (0.7279754925085274)
David has motive: True or False?
True (0.9237300130783155)
David has no motive: True or False?
True (0.6859494535376744)
David has opportunity: True or False?
True (0.7520125537161032)
David has no opportunity: True or False?
False (0.5009765603034438)
Mark is guilty: True or False?
True (0.9677167542009312)
Mark is not guilty: True or False?
True (0.8677097529871085)
Mark has mean: True or False?
True (0.8652241235443877)
Mark has no mean: True or False?
True (0.8620035690925699)
Mark has motive: True or False?
True (0.9686788331076437)
Mark has no motive: True or False?
True (0.6451199006197486)
Mark has opportunity: True or False?
True (0.8951566849862127)
Mark has no opportunity: True or False?
True (0.5418937216067536)
String is guilty: True or False?
True (0.9124361878432953)
String is not guilty: True or False?
True (0.7634837587244478)
String has mean: True or False?
True (0.8727817583545995)
String has no mean: True or False?
True (0.8149381276646971)
String has motive: True or False?
True (0.8101787517928931)
String has no motive: True or False?
True (0.7033457082786769)
String has opportunity: True or False?
True (0.854884683810039)
String has no opportunity: True or False?
True (0.6113820047705449)
### Cory
- mean: True (0.6433292707767855)
- motive: True (0.8925625719484378)
- opportunity: True (0.7424216889954057)

### David
- mean: True (0.6967841871600284)
- motive: False (0.31405054646232555)
- opportunity: True (0.7520125537161032)

### Mark
- mean: False (0.13799643090743008)
- motive: False (0.35488009938025145)
- opportunity: False (0.45810627839324636)

### String
- mean: False (0.1850618723353029)
- motive: False (0.29665429172132307)
- opportunity: False (0.38861799522945506)

The culprit is Cory.
In fact, it is David.
## 5minutemystery-the-mystery-of-the-leprechauns-trophy
Barry is guilty: True or False?
True (0.8969755785184792)
Barry is not guilty: True or False?
True (0.8719117627136385)
Barry has mean: True or False?
True (0.9170058398600052)
Barry has no mean: True or False?
True (0.9012274173198201)
Barry has motive: True or False?
True (0.9597620378565557)
Map:  24%|██▎       | 48/203 [56:59<3:02:55, 70.81s/ examples]
Map:  24%|██▍       | 49/203 [58:10<3:02:16, 71.02s/ examples]
Map:  25%|██▍       | 50/203 [59:07<2:50:23, 66.82s/ examples]
Barry has no motive: True or False?
True (0.8376200175313318)
Barry has opportunity: True or False?
True (0.8732148436000907)
Barry has no opportunity: True or False?
True (0.7483522884503825)
Casey is guilty: True or False?
True (0.8799743689174987)
Casey is not guilty: True or False?
True (0.9396923783210908)
Casey has mean: True or False?
True (0.892187358563457)
Casey has no mean: True or False?
True (0.8615382357584752)
Casey has motive: True or False?
True (0.9094255544919778)
Casey has no motive: True or False?
True (0.8344069148356309)
Casey has opportunity: True or False?
True (0.8757870204368676)
Casey has no opportunity: True or False?
True (0.7725306828324007)
Mr. Carswell is guilty: True or False?
True (0.7333563569098757)
Mr. Carswell is not guilty: True or False?
True (0.7725306828324007)
Mr. Carswell has mean: True or False?
True (0.8392075831473667)
Mr. Carswell has no mean: True or False?
True (0.8128672807499561)
Mr. Carswell has motive: True or False?
True (0.8820219652716884)
Mr. Carswell has no motive: True or False?
True (0.7690802105138688)
Mr. Carswell has opportunity: True or False?
True (0.7669924589170153)
Mr. Carswell has no opportunity: True or False?
True (0.7008947664177184)
Tony is guilty: True or False?
True (0.8418256636710214)
Tony is not guilty: True or False?
True (0.8875949368741688)
Tony has mean: True or False?
True (0.8665847814067802)
Tony has no mean: True or False?
True (0.7106283339569771)
Tony has motive: True or False?
True (0.8816149238192855)
Tony has no motive: True or False?
True (0.6020615685826383)
Tony has opportunity: True or False?
True (0.7106282704218558)
Tony has no opportunity: True or False?
False (0.5583270361921496)
### Barry
- mean: False (0.09877258268017985)
- motive: False (0.16237998246866825)
- opportunity: False (0.2516477115496175)

### Casey
- mean: False (0.1384617642415248)
- motive: False (0.1655930851643691)
- opportunity: False (0.22746931716759933)

### Mr. Carswell
- mean: True (0.8392075831473667)
- motive: True (0.8820219652716884)
- opportunity: True (0.7669924589170153)

### Tony
- mean: False (0.2893716660430229)
- motive: False (0.39793843141736174)
- opportunity: True (0.7106282704218558)

The culprit is Mr. Carswell.
In fact, it is Tony.
## 5minutemystery-the-mysterious-chicken
Ed is guilty: True or False?
True (0.8227595062673136)
Ed is not guilty: True or False?
True (0.9082930095862076)
Ed has mean: True or False?
True (0.8793541237128909)
Ed has no mean: True or False?
True (0.8807970862580315)
Ed has motive: True or False?
True (0.9657060519221431)
Ed has no motive: True or False?
True (0.9069831945855868)
Ed has opportunity: True or False?
True (0.9726235262544756)
Ed has no opportunity: True or False?
True (0.8705973031072073)
Ed's mother is guilty: True or False?
True (0.580352087772514)
Ed's mother is not guilty: True or False?
True (0.8444089912414552)
Ed's mother has mean: True or False?
False (0.5650587803792624)
Ed's mother has no mean: True or False?
True (0.5058591351869154)
Ed's mother has motive: True or False?
True (0.9706877478963396)
Ed's mother has no motive: True or False?
True (0.9092645024391882)
Ed's mother has opportunity: True or False?
True (0.9785492416845885)
Ed's mother has no opportunity: True or False?
True (0.5917232019857303)
Ed’s Husky is guilty: True or False?
True (0.644225125126315)
Ed’s Husky is not guilty: True or False?
True (0.8587185689177256)
Ed’s Husky has mean: True or False?
False (0.6513548405484016)
Ed’s Husky has no mean: True or False?
False (0.5650587803792624)
Ed’s Husky has motive: True or False?
True (0.934872446722342)
Ed’s Husky has no motive: True or False?
True (0.7033457082786769)
Ed’s Husky has opportunity: True or False?
True (0.7453983509653428)
Ed’s Husky has no opportunity: True or False?
False (0.6388352560545881)
Zeke is guilty: True or False?
True (0.9309620852900756)
Zeke is not guilty: True or False?
True (0.9702398769132671)
Zeke has mean: True or False?
True (0.9281487460975983)
Zeke has no mean: True or False?
True (0.7416740115009234)
Zeke has motive: True or False?
True (0.9931760429948333)
Zeke has no motive: True or False?
True (0.9860979910854153)
Zeke has opportunity: True or False?
True (0.9812389020148623)
Zeke has no opportunity: True or False?
True (0.9358173616900589)
### Ed
- mean: True (0.8793541237128909)
- motive: True (0.9657060519221431)
- opportunity: True (0.9726235262544756)

### Ed's mother
- mean: False (0.5650587803792624)
- motive: False (0.09073549756081178)
- opportunity: False (0.40827679801426975)

### Ed’s Husky
- mean: True (0.4349412196207376)
- motive: False (0.29665429172132307)
- opportunity: True (0.7453983509653428)

### Zeke
- mean: False (0.2583259884990766)
- motive: False (0.013902008914584707)
- opportunity: False (0.06418263830994109)

The culprit is Ed.
In fact, it is Ed.
## 5minutemystery-the-late-night-horror-show
Andrew is guilty: True or False?
True (0.9319595674053855)
Andrew is not guilty: True or False?
True (0.8701565822173906)
Andrew has mean: True or False?
True (0.8311430212356835)
Andrew has no mean: True or False?
True (0.5477059372067781)
Andrew has motive: True or False?
True (0.8591918406281239)
Andrew has no motive: True or False?
True (0.6085939964125278)
Andrew has opportunity: True or False?
True (0.7669924589170153)
Andrew has no opportunity: True or False?
True (0.6688802830862913)
David is guilty: True or False?
True (0.8723473540228537)
David is not guilty: True or False?
True (0.7898827135821628)
David has mean: True or False?
True (0.6976089520497016)
David has no mean: True or False?
True (0.6020615685826383)
David has motive: True or False?
True (0.8958875533219306)
David has no motive: True or False?
True (0.7461389980806673)
David has opportunity: True or False?
True (0.8381505623254643)
David has no opportunity: True or False?
True (0.6992543888266708)
Dennis is guilty: True or False?
True (0.920217993899809)
Dennis is not guilty: True or False?
True (0.8783141983077656)
Dennis has mean: True or False?
True (0.8484706895507578)
Dennis has no mean: True or False?
True (0.6113819501087365)
Dennis has motive: True or False?
True (0.9063219998220023)
Dennis has no motive: True or False?
True (0.8386797935187188)
Dennis has opportunity: True or False?
True (0.8489722037469682)
Dennis has no opportunity: True or False?
True (0.8803863464576128)
Matthew is guilty: True or False?
True (0.9351098557348285)
Matthew is not guilty: True or False?
True (0.9181872635464632)
Matthew has mean: True or False?
True (0.8723473540228537)
Matthew has no mean: True or False?
True (0.686790355176806)
Matthew has motive: True or False?
True (0.9299510095943111)
Matthew has no motive: True or False?
True (0.8158201638039532)
Matthew has opportunity: True or False?
True (0.879146760693242)
Matthew has no opportunity: True or False?
True (0.6834194581047349)
### Andrew
- mean: False (0.45229406279322193)
- motive: False (0.39140600358747224)
- opportunity: False (0.3311197169137087)

### David
- mean: False (0.39793843141736174)
- motive: False (0.2538610019193327)
- opportunity: False (0.3007456111733292)

### Dennis
- mean: True (0.8484706895507578)
- motive: True (0.9063219998220023)
- opportunity: True (0.8489722037469682)

### Matthew
- mean: False (0.313209644823194)
- motive: False (0.18417983619604683)
- opportunity: False (0.3165805418952651)

The culprit is Dennis.
In fact, it is David.
## 5minutemystery-making-partner
Dan Cartman is guilty: True or False?
True (0.8134608241927087)
Dan Cartman is not guilty: True or False?
True (0.8912444106095914)
Dan Cartman has mean: True or False?
True (0.878314250659373)
Dan Cartman has no mean: True or False?
True (0.8397339530959691)
Dan Cartman has motive: True or False?
True (0.947769104959166)
Dan Cartman has no motive: True or False?
True (0.865678909174824)
Dan Cartman has opportunity: True or False?
True (0.9445872321654378)
Dan Cartman has no opportunity: True or False?
True (0.8402589628813668)
Jill is guilty: True or False?
True (0.8826302888575707)
Jill is not guilty: True or False?
True (0.934514761243551)
Jill has mean: True or False?

Map:  25%|██▌       | 51/203 [1:00:37<3:07:09, 73.88s/ examples]
Map:  26%|██▌       | 52/203 [1:01:46<3:02:15, 72.42s/ examples]
Map:  26%|██▌       | 53/203 [1:03:06<3:06:35, 74.64s/ examples]True (0.8221891570741111)
Jill has no mean: True or False?
True (0.7697731762926651)
Jill has motive: True or False?
True (0.9403530352223053)
Jill has no motive: True or False?
True (0.7563574896543893)
Jill has opportunity: True or False?
True (0.854884683810039)
Jill has no opportunity: True or False?
True (0.6397360437814448)
Mike Creighton is guilty: True or False?
True (0.6654105788791005)
Mike Creighton is not guilty: True or False?
True (0.8716934900924195)
Mike Creighton has mean: True or False?
True (0.7779753136455794)
Mike Creighton has no mean: True or False?
True (0.7799929399351836)
Mike Creighton has motive: True or False?
True (0.9226219081780128)
Mike Creighton has no motive: True or False?
True (0.7826624547920057)
Mike Creighton has opportunity: True or False?
True (0.9032942081209032)
Mike Creighton has no opportunity: True or False?
True (0.6513548405484016)
Mrs. Krantz is guilty: True or False?
True (0.7606506318580792)
Mrs. Krantz is not guilty: True or False?
True (0.9048188910591489)
Mrs. Krantz has mean: True or False?
True (0.7994423454932595)
Mrs. Krantz has no mean: True or False?
True (0.7669925046333297)
Mrs. Krantz has motive: True or False?
True (0.9367495172436676)
Mrs. Krantz has no motive: True or False?
True (0.7520125537161032)
Mrs. Krantz has opportunity: True or False?
True (0.8381505623254643)
Mrs. Krantz has no opportunity: True or False?
True (0.6451199006197486)
### Dan Cartman
- mean: True (0.878314250659373)
- motive: True (0.947769104959166)
- opportunity: True (0.9445872321654378)

### Jill
- mean: False (0.23022682370733494)
- motive: False (0.24364251034561069)
- opportunity: False (0.3602639562185552)

### Mike Creighton
- mean: True (0.7779753136455794)
- motive: False (0.2173375452079943)
- opportunity: False (0.34864515945159835)

### Mrs. Krantz
- mean: False (0.23300749536667031)
- motive: False (0.2479874462838968)
- opportunity: False (0.35488009938025145)

The culprit is Dan Cartman.
In fact, it is Mike Creighton.
## 5minutemystery-no-retreat-from-death
Amanda Kent is guilty: True or False?
True (0.9307106123564625)
Amanda Kent is not guilty: True or False?
True (0.9655764701970907)
Amanda Kent has mean: True or False?
True (0.9804313180726916)
Amanda Kent has no mean: True or False?
True (0.9219218506394821)
Amanda Kent has motive: True or False?
True (0.9868280885871353)
Amanda Kent has no motive: True or False?
True (0.897695304229796)
Amanda Kent has opportunity: True or False?
True (0.9706877478963396)
Amanda Kent has no opportunity: True or False?
True (0.8484706895507578)
Craig Willis is guilty: True or False?
True (0.9183338853275215)
Craig Willis is not guilty: True or False?
True (0.9729338284788606)
Craig Willis has mean: True or False?
True (0.9431384220853135)
Craig Willis has no mean: True or False?
True (0.9471859926317535)
Craig Willis has motive: True or False?
True (0.9891291857546544)
Craig Willis has no motive: True or False?
True (0.9621076000160501)
Craig Willis has opportunity: True or False?
True (0.9405717864730483)
Craig Willis has no opportunity: True or False?
True (0.832781373043151)
Niles Anderson is guilty: True or False?
True (0.9616059669560388)
Niles Anderson is not guilty: True or False?
True (0.9760379793845908)
Niles Anderson has mean: True or False?
True (0.9707432981083896)
Niles Anderson has no mean: True or False?
True (0.8710367026584496)
Niles Anderson has motive: True or False?
True (0.9929882285769507)
Niles Anderson has no motive: True or False?
True (0.9449946880768697)
Niles Anderson has opportunity: True or False?
True (0.972727357600667)
Niles Anderson has no opportunity: True or False?
True (0.8670358119601653)
Stephanie Clark is guilty: True or False?
True (0.9152045868398637)
Stephanie Clark is not guilty: True or False?
True (0.9610980755676962)
Stephanie Clark has mean: True or False?
True (0.9603611244019274)
Stephanie Clark has no mean: True or False?
True (0.9099070446252667)
Stephanie Clark has motive: True or False?
True (0.9865199324432031)
Stephanie Clark has no motive: True or False?
True (0.9401335713518422)
Stephanie Clark has opportunity: True or False?
True (0.9546474221708894)
Stephanie Clark has no opportunity: True or False?
True (0.8074606715677252)
### Amanda Kent
- mean: False (0.07807814936051793)
- motive: False (0.10230469577020396)
- opportunity: False (0.15152931044924223)

### Craig Willis
- mean: True (0.9431384220853135)
- motive: True (0.9891291857546544)
- opportunity: True (0.9405717864730483)

### Niles Anderson
- mean: False (0.12896329734155043)
- motive: False (0.055005311923130296)
- opportunity: False (0.13296418803983467)

### Stephanie Clark
- mean: False (0.09009295537473327)
- motive: False (0.05986642864815783)
- opportunity: False (0.19253932843227484)

The culprit is Craig Willis.
In fact, it is Niles Anderson.
## 5minutemystery-a-monster-of-a-mystery
Donald is guilty: True or False?
True (0.970070243275667)
Donald is not guilty: True or False?
True (0.9695556166618308)
Donald has mean: True or False?
True (0.9476723683039264)
Donald has no mean: True or False?
True (0.9029524325377104)
Donald has motive: True or False?
True (0.9529258022651363)
Donald has no motive: True or False?
True (0.9082930704920021)
Donald has opportunity: True or False?
True (0.9438672660817211)
Donald has no opportunity: True or False?
True (0.8649961951944259)
Linda is guilty: True or False?
True (0.9428234118096998)
Linda is not guilty: True or False?
True (0.9706878075618867)
Linda has mean: True or False?
True (0.9331876642092066)
Linda has no mean: True or False?
True (0.8661325012437474)
Linda has motive: True or False?
True (0.9753431079900657)
Linda has no motive: True or False?
True (0.9219217888198067)
Linda has opportunity: True or False?
True (0.9660280346390409)
Linda has no opportunity: True or False?
True (0.8568122940392877)
Randy is guilty: True or False?
True (0.9672868242254096)
Randy is not guilty: True or False?
True (0.9794525497172101)
Randy has mean: True or False?
True (0.9175984877579624)
Randy has no mean: True or False?
True (0.8360197583769845)
Randy has motive: True or False?
True (0.9683812262581977)
Randy has no motive: True or False?
True (0.9073122726900733)
Randy has opportunity: True or False?
True (0.9626028535101038)
Randy has no opportunity: True or False?
True (0.8216173667955227)
Wendell is guilty: True or False?
True (0.96224969617818)
Wendell is not guilty: True or False?
True (0.969295143284489)
Wendell has mean: True or False?
True (0.9071478843057855)
Wendell has no mean: True or False?
True (0.874934615163517)
Wendell has motive: True or False?
True (0.9658352120791275)
Wendell has no motive: True or False?
True (0.9036348473387281)
Wendell has opportunity: True or False?
True (0.9076402191395381)
Wendell has no opportunity: True or False?
True (0.7505527730327083)
### Donald
- mean: True (0.9476723683039264)
- motive: True (0.9529258022651363)
- opportunity: True (0.9438672660817211)

### Linda
- mean: False (0.1338674987562526)
- motive: False (0.07807821118019331)
- opportunity: False (0.14318770596071229)

### Randy
- mean: False (0.1639802416230155)
- motive: False (0.09268772730992669)
- opportunity: False (0.17838263320447734)

### Wendell
- mean: False (0.125065384836483)
- motive: False (0.09636515266127188)
- opportunity: False (0.2494472269672917)

The culprit is Donald.
In fact, it is Linda.
## 5minutemystery-chow-baby
Beryl Hives is guilty: True or False?
True (0.8757869551856522)
Beryl Hives is not guilty: True or False?
True (0.9696132548883896)
Beryl Hives has mean: True or False?
True (0.6959583025067009)
Beryl Hives has no mean: True or False?
True (0.8006919661398397)
Beryl Hives has motive: True or False?
True (0.9314625284362855)
Beryl Hives has no motive: True or False?
True (0.8906751877407573)
Beryl Hives has opportunity: True or False?
True (0.8283842201397164)
Beryl Hives has no opportunity: True or False?
True (0.6951311179371613)
Dawn de Jong is guilty: True or False?
True (0.7386690954574974)
Dawn de Jong is not guilty: True or False?
True (0.925499741040984)
Dawn de Jong has mean: True or False?
True (0.6352224318508648)

Map:  27%|██▋       | 54/203 [1:04:19<3:03:46, 74.00s/ examples]
Map:  27%|██▋       | 55/203 [1:06:11<3:30:59, 85.54s/ examples]
Map:  28%|██▊       | 56/203 [1:07:54<3:42:09, 90.68s/ examples]Dawn de Jong has no mean: True or False?
False (0.5544704160706745)
Dawn de Jong has motive: True or False?
True (0.9008791478232747)
Dawn de Jong has no motive: True or False?
True (0.6469064338453809)
Dawn de Jong has opportunity: True or False?
True (0.6306849143569856)
Dawn de Jong has no opportunity: True or False?
False (0.6104534234357184)
Konrad Pushkin is guilty: True or False?
True (0.9460011721384068)
Konrad Pushkin is not guilty: True or False?
True (0.9708540445899615)
Konrad Pushkin has mean: True or False?
True (0.7146280926688615)
Konrad Pushkin has no mean: True or False?
True (0.7193836643711469)
Konrad Pushkin has motive: True or False?
True (0.9439705630247532)
Konrad Pushkin has no motive: True or False?
True (0.8740772044235984)
Konrad Pushkin has opportunity: True or False?
True (0.8918110138739693)
Konrad Pushkin has no opportunity: True or False?
False (0.5068355091660127)
Pete Stampkowski is guilty: True or False?
True (0.8984105603938967)
Pete Stampkowski is not guilty: True or False?
True (0.9317114972308657)
Pete Stampkowski has mean: True or False?
True (0.6619228115397798)
Pete Stampkowski has no mean: True or False?
True (0.7217432334405754)
Pete Stampkowski has motive: True or False?
True (0.9575167905174621)
Pete Stampkowski has no motive: True or False?
True (0.779321849347754)
Pete Stampkowski has opportunity: True or False?
True (0.8864204283224634)
Pete Stampkowski has no opportunity: True or False?
True (0.6783269591477166)
### Beryl Hives
- mean: True (0.6959583025067009)
- motive: False (0.10932481225924273)
- opportunity: False (0.3048688820628387)

### Dawn de Jong
- mean: True (0.6352224318508648)
- motive: False (0.35309356615461907)
- opportunity: True (0.6306849143569856)

### Konrad Pushkin
- mean: True (0.7146280926688615)
- motive: True (0.9439705630247532)
- opportunity: True (0.8918110138739693)

### Pete Stampkowski
- mean: True (0.6619228115397798)
- motive: False (0.22067815065224605)
- opportunity: False (0.32167304085228343)

The culprit is Konrad Pushkin.
In fact, it is Beryl Hives.
## 5minutemystery-the-mystery-of-the-frowning-clown
Bumbo is guilty: True or False?
True (0.9643886093607492)
Bumbo is not guilty: True or False?
True (0.9855799082412889)
Bumbo has mean: True or False?
True (0.8906751877407573)
Bumbo has no mean: True or False?
True (0.8591918406281239)
Bumbo has motive: True or False?
True (0.9700134993465792)
Bumbo has no motive: True or False?
True (0.8469578650997759)
Bumbo has opportunity: True or False?
True (0.9190632712053527)
Bumbo has no opportunity: True or False?
True (0.7256486384635821)
Dusty is guilty: True or False?
True (0.9630224717531983)
Dusty is not guilty: True or False?
True (0.9772408607055925)
Dusty has mean: True or False?
True (0.9089416847784234)
Dusty has no mean: True or False?
True (0.9345148239076511)
Dusty has motive: True or False?
True (0.9722043875229701)
Dusty has no motive: True or False?
True (0.9032942081209032)
Dusty has opportunity: True or False?
True (0.9270997017012965)
Dusty has no opportunity: True or False?
True (0.7937462383814009)
Mr. Green is guilty: True or False?
True (0.9579909444975866)
Mr. Green is not guilty: True or False?
True (0.967594443404463)
Mr. Green has mean: True or False?
True (0.8973359441831076)
Mr. Green has no mean: True or False?
True (0.9291837815043049)
Mr. Green has motive: True or False?
True (0.9771101479827176)
Mr. Green has no motive: True or False?
True (0.867485409735739)
Mr. Green has opportunity: True or False?
True (0.9244151684978138)
Mr. Green has no opportunity: True or False?
True (0.7826625131049049)
Stage Manager is guilty: True or False?
True (0.9491062747098069)
Stage Manager is not guilty: True or False?
True (0.9612438076473231)
Stage Manager has mean: True or False?
True (0.9328214561580316)
Stage Manager has no mean: True or False?
True (0.9504109622144332)
Stage Manager has motive: True or False?
True (0.9792749284948266)
Stage Manager has no motive: True or False?
True (0.8987665204865408)
Stage Manager has opportunity: True or False?
True (0.959535181008237)
Stage Manager has no opportunity: True or False?
True (0.8620035048683017)
### Bumbo
- mean: False (0.14080815937187607)
- motive: False (0.1530421349002241)
- opportunity: False (0.2743513615364179)

### Dusty
- mean: True (0.9089416847784234)
- motive: False (0.09670579187909678)
- opportunity: False (0.2062537616185991)

### Mr. Green
- mean: True (0.8973359441831076)
- motive: False (0.13251459026426105)
- opportunity: False (0.21733748689509513)

### Stage Manager
- mean: True (0.9328214561580316)
- motive: True (0.9792749284948266)
- opportunity: True (0.959535181008237)

The culprit is Stage Manager.
In fact, it is Stage Manager.
## 5minutemystery-the-strangest-sport-of-all
Ernie is guilty: True or False?
True (0.9190633328333496)
Ernie is not guilty: True or False?
True (0.9476723683039264)
Ernie has mean: True or False?
True (0.8951566249612815)
Ernie has no mean: True or False?
True (0.8762112821835625)
Ernie has motive: True or False?
True (0.9102267057681164)
Ernie has no motive: True or False?
True (0.811078188867804)
Ernie has opportunity: True or False?
True (0.9394705907755942)
Ernie has no opportunity: True or False?
True (0.8413047772878592)
Gordon is guilty: True or False?
True (0.9046505126460354)
Gordon is not guilty: True or False?
True (0.9383503780077049)
Gordon has mean: True or False?
True (0.7534666630720156)
Gordon has no mean: True or False?
True (0.7879311977554747)
Gordon has motive: True or False?
True (0.8998277786460391)
Gordon has no motive: True or False?
True (0.8074606715677252)
Gordon has opportunity: True or False?
True (0.8591918406281239)
Gordon has no opportunity: True or False?
True (0.8407826471261478)
Jesse is guilty: True or False?
True (0.8910549302065384)
Jesse is not guilty: True or False?
True (0.9095863097773887)
Jesse has mean: True or False?
True (0.7950222460539826)
Jesse has no mean: True or False?
True (0.8402590129647053)
Jesse has motive: True or False?
True (0.8770561879413864)
Jesse has no motive: True or False?
True (0.7931059536445917)
Jesse has opportunity: True or False?
True (0.8062431235779619)
Jesse has no opportunity: True or False?
True (0.794384956668203)
Mac is guilty: True or False?
True (0.9307106123564625)
Mac is not guilty: True or False?
True (0.9511422515416323)
Mac has mean: True or False?
True (0.8820219652716884)
Mac has no mean: True or False?
True (0.8976952440346371)
Mac has motive: True or False?
True (0.927887794449634)
Mac has no motive: True or False?
True (0.9029524325377104)
Mac has opportunity: True or False?
True (0.8973360043541736)
Mac has no opportunity: True or False?
True (0.8887587777822111)
### Ernie
- mean: False (0.12378871781643752)
- motive: False (0.18892181113219597)
- opportunity: False (0.15869522271214076)

### Gordon
- mean: True (0.7534666630720156)
- motive: False (0.19253932843227484)
- opportunity: False (0.1592173528738522)

### Jesse
- mean: True (0.7950222460539826)
- motive: False (0.2068940463554083)
- opportunity: False (0.20561504333179703)

### Mac
- mean: True (0.8820219652716884)
- motive: True (0.927887794449634)
- opportunity: True (0.8973360043541736)

The culprit is Mac.
In fact, it is Jesse.
## 5minutemystery-who-stole-storimons-wallet
Danny is guilty: True or False?
True (0.9678993227186541)
Danny is not guilty: True or False?
True (0.9878528117793998)
Danny has mean: True or False?
True (0.8444089912414552)
Danny has no mean: True or False?
True (0.8828325273478573)
Danny has motive: True or False?
True (0.943347633443741)
Danny has no motive: True or False?
True (0.9437636745681832)
Danny has opportunity: True or False?
True (0.942081869103903)
Danny has no opportunity: True or False?
True (0.9175984877579624)
Mick is guilty: True or False?
True (0.9753431679417652)
Mick is not guilty: True or False?
True (0.9938189982894412)
Mick has mean: True or False?
True (0.9775000208126312)
Mick has no mean: True or False?
True (0.9418684262191025)
Mick has motive: True or False?
True (0.9820482724696491)
Mick has no motive: True or False?
True (0.9489172681310486)

Map:  28%|██▊       | 57/203 [1:09:28<3:43:09, 91.71s/ examples]
Map:  29%|██▊       | 58/203 [1:11:01<3:42:19, 91.99s/ examples]
Map:  29%|██▉       | 59/203 [1:12:00<3:17:16, 82.20s/ examples]Mick has opportunity: True or False?
True (0.9698996547102765)
Mick has no opportunity: True or False?
True (0.9008791478232747)
Mr. Storimon is guilty: True or False?
True (0.9683812262581977)
Mr. Storimon is not guilty: True or False?
True (0.9833748931272365)
Mr. Storimon has mean: True or False?
True (0.9598374351134399)
Mr. Storimon has no mean: True or False?
True (0.9554855815192022)
Mr. Storimon has motive: True or False?
True (0.9859634637885061)
Mr. Storimon has no motive: True or False?
True (0.9491062747098069)
Mr. Storimon has opportunity: True or False?
True (0.9759464867446064)
Mr. Storimon has no opportunity: True or False?
True (0.9365176577773374)
Policeman is guilty: True or False?
True (0.9792550794742616)
Policeman is not guilty: True or False?
True (0.9888419508445501)
Policeman has mean: True or False?
True (0.9333093181503205)
Policeman has no mean: True or False?
True (0.9594592463344039)
Policeman has motive: True or False?
True (0.9764905566616159)
Policeman has no motive: True or False?
True (0.9609517462724031)
Policeman has opportunity: True or False?
True (0.9599126594957205)
Policeman has no opportunity: True or False?
True (0.9565531009888748)
### Danny
- mean: True (0.8444089912414552)
- motive: True (0.943347633443741)
- opportunity: False (0.08240151224203762)

### Mick
- mean: False (0.058131573780897505)
- motive: False (0.0510827318689514)
- opportunity: False (0.09912085217672528)

### Mr. Storimon
- mean: False (0.044514418480797846)
- motive: False (0.05089372529019309)
- opportunity: False (0.06348234222266258)

### Policeman
- mean: True (0.9333093181503205)
- motive: True (0.9764905566616159)
- opportunity: True (0.9599126594957205)

The culprit is Policeman.
In fact, it is Mr. Storimon.
## 5minutemystery-miles-archer-solves-a-case
Arnold Grossmecker is guilty: True or False?
True (0.9465966835599983)
Arnold Grossmecker is not guilty: True or False?
True (0.9618217364339323)
Arnold Grossmecker has mean: True or False?
True (0.847967740521315)
Arnold Grossmecker has no mean: True or False?
True (0.8929365260632085)
Arnold Grossmecker has motive: True or False?
True (0.9763104920302871)
Arnold Grossmecker has no motive: True or False?
True (0.9015746123467522)
Arnold Grossmecker has opportunity: True or False?
True (0.9170058398600052)
Arnold Grossmecker has no opportunity: True or False?
True (0.861538171568877)
Brigid Jellicoe is guilty: True or False?
True (0.9537942396657707)
Brigid Jellicoe is not guilty: True or False?
True (0.9484418035658785)
Brigid Jellicoe has mean: True or False?
True (0.9073122118500465)
Brigid Jellicoe has no mean: True or False?
True (0.9155072008980665)
Brigid Jellicoe has motive: True or False?
True (0.9638480560973683)
Brigid Jellicoe has no motive: True or False?
True (0.9276260107813639)
Brigid Jellicoe has opportunity: True or False?
True (0.9405717864730483)
Brigid Jellicoe has no opportunity: True or False?
True (0.8438951328214825)
Quinton Jesselton is guilty: True or False?
True (0.9294403817764149)
Quinton Jesselton is not guilty: True or False?
True (0.9671009198161682)
Quinton Jesselton has mean: True or False?
True (0.9408984770280414)
Quinton Jesselton has no mean: True or False?
True (0.8110782492978404)
Quinton Jesselton has motive: True or False?
True (0.9736947425622681)
Quinton Jesselton has no motive: True or False?
True (0.8577681165234065)
Quinton Jesselton has opportunity: True or False?
True (0.8980534699860239)
Quinton Jesselton has no opportunity: True or False?
True (0.7627776774954688)
Sandra O’Malley is guilty: True or False?
True (0.8365545874520802)
Sandra O’Malley is not guilty: True or False?
True (0.9378968460746586)
Sandra O’Malley has mean: True or False?
True (0.6842640693504702)
Sandra O’Malley has no mean: True or False?
True (0.879146813094474)
Sandra O’Malley has motive: True or False?
True (0.9422947179693436)
Sandra O’Malley has no motive: True or False?
True (0.8037905715242155)
Sandra O’Malley has opportunity: True or False?
True (0.9193533657123177)
Sandra O’Malley has no opportunity: True or False?
True (0.7416740115009234)
### Arnold Grossmecker
- mean: True (0.847967740521315)
- motive: False (0.09842538765324782)
- opportunity: False (0.13846182843112298)

### Brigid Jellicoe
- mean: True (0.9073122118500465)
- motive: True (0.9638480560973683)
- opportunity: True (0.9405717864730483)

### Quinton Jesselton
- mean: False (0.18892175070215955)
- motive: False (0.14223188347659355)
- opportunity: False (0.23722232250453124)

### Sandra O’Malley
- mean: True (0.6842640693504702)
- motive: False (0.1962094284757845)
- opportunity: False (0.2583259884990766)

The culprit is Brigid Jellicoe.
In fact, it is Quinton Jesselton.
## 5minutemystery-murder-in-the-early-morning
Constance is guilty: True or False?
True (0.8333246107254184)
Constance is not guilty: True or False?
True (0.9133679254389228)
Constance has mean: True or False?
True (0.9687380774673213)
Constance has no mean: True or False?
True (0.9127477403975288)
Constance has motive: True or False?
True (0.9687380774673213)
Constance has no motive: True or False?
True (0.920217993899809)
Constance has opportunity: True or False?
True (0.9682614213403071)
Constance has no opportunity: True or False?
True (0.9155072554665495)
John is guilty: True or False?
True (0.71582149676272)
John is not guilty: True or False?
True (0.8255897087847518)
John has mean: True or False?
True (0.8433797899747144)
John has no mean: True or False?
True (0.8294919722593475)
John has motive: True or False?
True (0.9394705907755942)
John has no motive: True or False?
True (0.8665847814067802)
John has opportunity: True or False?
True (0.9709092372014624)
John has no opportunity: True or False?
True (0.8370879250561812)
Nancy is guilty: True or False?
True (0.7911764307711107)
Nancy is not guilty: True or False?
True (0.9304582506719414)
Nancy has mean: True or False?
True (0.7885831565209055)
Nancy has no mean: True or False?
True (0.8116759653945079)
Nancy has motive: True or False?
True (0.9284088027271398)
Nancy has no motive: True or False?
True (0.8238958672039278)
Nancy has opportunity: True or False?
True (0.920789721359066)
Nancy has no opportunity: True or False?
True (0.8305941261447712)
Vernon is guilty: True or False?
True (0.7412996266976789)
Vernon is not guilty: True or False?
True (0.8946054590684968)
Vernon has mean: True or False?
True (0.8716934900924195)
Vernon has no mean: True or False?
True (0.8494724067948436)
Vernon has motive: True or False?
True (0.9530133616438526)
Vernon has no motive: True or False?
True (0.866132552869269)
Vernon has opportunity: True or False?
True (0.9425067301242699)
Vernon has no opportunity: True or False?
True (0.7879311977554747)
### Constance
- mean: True (0.9687380774673213)
- motive: True (0.9687380774673213)
- opportunity: True (0.9682614213403071)

### John
- mean: False (0.17050802774065255)
- motive: False (0.1334152185932198)
- opportunity: False (0.16291207494381876)

### Nancy
- mean: True (0.7885831565209055)
- motive: False (0.17610413279607218)
- opportunity: False (0.16940587385522876)

### Vernon
- mean: False (0.1505275932051564)
- motive: False (0.13386744713073095)
- opportunity: False (0.2120688022445253)

The culprit is Constance.
In fact, it is Vernon.
## 5minutemystery-raiding-cane
Brent Pearson is guilty: True or False?
True (0.9563905008811648)
Brent Pearson is not guilty: True or False?
True (0.9241418261705818)
Brent Pearson has mean: True or False?
True (0.8169911556077801)
Brent Pearson has no mean: True or False?
True (0.7956581141325956)
Brent Pearson has motive: True or False?
True (0.9819446807697475)
Brent Pearson has no motive: True or False?
True (0.905656637917298)
Brent Pearson has opportunity: True or False?
True (0.8887587777822111)
Brent Pearson has no opportunity: True or False?
True (0.7178038242127955)
Frank Weiss is guilty: True or False?
True (0.9714016916045378)
Frank Weiss is not guilty: True or False?
True (0.9514137516710428)
Frank Weiss has mean: True or False?
True (0.8686040045586428)
Frank Weiss has no mean: True or False?
True (0.8596637847360897)

Map:  30%|██▉       | 60/203 [1:13:08<3:05:38, 77.89s/ examples]
Map:  30%|███       | 61/203 [1:16:46<4:43:55, 119.97s/ examples]
Map:  31%|███       | 62/203 [1:18:31<4:31:16, 115.44s/ examples]Frank Weiss has motive: True or False?
True (0.9890448453517958)
Frank Weiss has no motive: True or False?
True (0.9539660824292815)
Frank Weiss has opportunity: True or False?
True (0.8873999116020591)
Frank Weiss has no opportunity: True or False?
True (0.7333563569098757)
Michael Weiss is guilty: True or False?
True (0.9565936323912209)
Michael Weiss is not guilty: True or False?
True (0.934155284694701)
Michael Weiss has mean: True or False?
True (0.8203256148776867)
Michael Weiss has no mean: True or False?
True (0.875574405580689)
Michael Weiss has motive: True or False?
True (0.9808208937620218)
Michael Weiss has no motive: True or False?
True (0.884439109617765)
Michael Weiss has opportunity: True or False?
True (0.8253083182831968)
Michael Weiss has no opportunity: True or False?
True (0.6270381219830087)
Ronald Weiss is guilty: True or False?
True (0.9680808185196469)
Ronald Weiss is not guilty: True or False?
True (0.9592307208025933)
Ronald Weiss has mean: True or False?
True (0.8546422101536368)
Ronald Weiss has no mean: True or False?
True (0.8638516611889259)
Ronald Weiss has motive: True or False?
True (0.9823386069427514)
Ronald Weiss has no motive: True or False?
True (0.9051547640395294)
Ronald Weiss has opportunity: True or False?
True (0.8908652046764556)
Ronald Weiss has no opportunity: True or False?
True (0.6706082735718226)
### Brent Pearson
- mean: False (0.20434188586740443)
- motive: False (0.094343362082702)
- opportunity: False (0.28219617578720446)

### Frank Weiss
- mean: True (0.8686040045586428)
- motive: True (0.9890448453517958)
- opportunity: True (0.8873999116020591)

### Michael Weiss
- mean: True (0.8203256148776867)
- motive: False (0.11556089038223505)
- opportunity: False (0.3729618780169913)

### Ronald Weiss
- mean: True (0.8546422101536368)
- motive: False (0.09484523596047056)
- opportunity: False (0.3293917264281774)

The culprit is Frank Weiss.
In fact, it is Frank Weiss.
## 5minutemystery-the-missing-dagger
Chris Palmer is guilty: True or False?
True (0.960804880888677)
Chris Palmer is not guilty: True or False?
True (0.9791556598479493)
Chris Palmer has mean: True or False?
True (0.936980484689786)
Chris Palmer has no mean: True or False?
True (0.9178934131644976)
Chris Palmer has motive: True or False?
True (0.9721515187478543)
Chris Palmer has no motive: True or False?
True (0.9230391966311572)
Chris Palmer has opportunity: True or False?
True (0.962813258487323)
Chris Palmer has no opportunity: True or False?
True (0.8962513815714083)
Matthew Light is guilty: True or False?
True (0.9396923188104354)
Matthew Light is not guilty: True or False?
True (0.9427180278987515)
Matthew Light has mean: True or False?
True (0.9046505665674094)
Matthew Light has no mean: True or False?
True (0.874934615163517)
Matthew Light has motive: True or False?
True (0.9518632280135741)
Matthew Light has no motive: True or False?
True (0.8856315007226893)
Matthew Light has opportunity: True or False?
True (0.9351098557348285)
Matthew Light has no opportunity: True or False?
True (0.858718632897247)
Mitchell Land is guilty: True or False?
True (0.9471859926317535)
Mitchell Land is not guilty: True or False?
True (0.9142907234091052)
Mitchell Land has mean: True or False?
True (0.9130583993174167)
Mitchell Land has no mean: True or False?
True (0.8169911556077801)
Mitchell Land has motive: True or False?
True (0.9444848881002107)
Mitchell Land has no motive: True or False?
True (0.8193157928301305)
Mitchell Land has opportunity: True or False?
True (0.9594593035226332)
Mitchell Land has no opportunity: True or False?
True (0.8529354311342636)
Paul Benham is guilty: True or False?
True (0.9748211501698323)
Paul Benham is not guilty: True or False?
True (0.9759005309632979)
Paul Benham has mean: True or False?
True (0.9605096001181298)
Paul Benham has no mean: True or False?
True (0.921357630313903)
Paul Benham has motive: True or False?
True (0.972830772390074)
Paul Benham has no motive: True or False?
True (0.9317114347547434)
Paul Benham has opportunity: True or False?
True (0.9559813152103319)
Paul Benham has no opportunity: True or False?
True (0.8856315007226893)
Russell Smith is guilty: True or False?
True (0.9517737036527996)
Russell Smith is not guilty: True or False?
True (0.9763104920302871)
Russell Smith has mean: True or False?
True (0.9610980147014194)
Russell Smith has no mean: True or False?
True (0.935346481802689)
Russell Smith has motive: True or False?
True (0.9808393129553152)
Russell Smith has no motive: True or False?
True (0.9294403817764149)
Russell Smith has opportunity: True or False?
True (0.9634374994224176)
Russell Smith has no opportunity: True or False?
True (0.7826625131049049)
### Chris Palmer
- mean: True (0.936980484689786)
- motive: True (0.9721515187478543)
- opportunity: True (0.962813258487323)

### Matthew Light
- mean: False (0.125065384836483)
- motive: False (0.11436849927731074)
- opportunity: False (0.14128136710275296)

### Mitchell Land
- mean: False (0.18300884439221987)
- motive: False (0.18068420716986955)
- opportunity: False (0.14706456886573638)

### Paul Benham
- mean: False (0.07864236968609695)
- motive: False (0.06828856524525662)
- opportunity: False (0.11436849927731074)

### Russell Smith
- mean: False (0.06465351819731102)
- motive: False (0.07055961822358514)
- opportunity: False (0.21733748689509513)

The culprit is Chris Palmer.
In fact, it is Paul Benham.
## 5minutemystery-mystery-of-the-bratty-kid
Angelita is guilty: True or False?
True (0.8996515883738708)
Angelita is not guilty: True or False?
True (0.9323301884216684)
Angelita has mean: True or False?
True (0.8716934900924195)
Angelita has no mean: True or False?
True (0.9056565771882901)
Angelita has motive: True or False?
True (0.8624674701790345)
Angelita has no motive: True or False?
True (0.8494723435042196)
Angelita has opportunity: True or False?
True (0.9082930704920021)
Angelita has no opportunity: True or False?
True (0.797556874947312)
Emily is guilty: True or False?
True (0.944176853162527)
Emily is not guilty: True or False?
True (0.9805434346329732)
Emily has mean: True or False?
True (0.8862236142219189)
Emily has no mean: True or False?
True (0.960804880888677)
Emily has motive: True or False?
True (0.9180403984176693)
Emily has no motive: True or False?
True (0.9005297448210564)
Emily has opportunity: True or False?
True (0.950041474283655)
Emily has no opportunity: True or False?
True (0.8601343090488404)
Jessica is guilty: True or False?
True (0.9281487460975983)
Jessica is not guilty: True or False?
True (0.9735442395649992)
Jessica has mean: True or False?
True (0.8872045854516336)
Jessica has no mean: True or False?
True (0.9527503243194666)
Jessica has motive: True or False?
True (0.9340350654042096)
Jessica has no motive: True or False?
True (0.8615382357584752)
Jessica has opportunity: True or False?
True (0.9319595118562682)
Jessica has no opportunity: True or False?
True (0.8688267468984366)
Percy Wellington is guilty: True or False?
True (0.9383503780077049)
Percy Wellington is not guilty: True or False?
True (0.9543930889248589)
Percy Wellington has mean: True or False?
True (0.8852352523606669)
Percy Wellington has no mean: True or False?
True (0.9354645628936168)
Percy Wellington has motive: True or False?
True (0.8998277786460391)
Percy Wellington has no motive: True or False?
True (0.7732163648437078)
Percy Wellington has opportunity: True or False?
True (0.9388008138003494)
Percy Wellington has no opportunity: True or False?
True (0.8402590129647053)
### Angelita
- mean: True (0.8716934900924195)
- motive: True (0.8624674701790345)
- opportunity: True (0.9082930704920021)

### Emily
- mean: True (0.8862236142219189)
- motive: False (0.09947025517894359)
- opportunity: False (0.13986569095115964)

### Jessica
- mean: True (0.8872045854516336)
- motive: False (0.1384617642415248)
- opportunity: False (0.13117325310156336)

### Percy Wellington
- mean: True (0.8852352523606669)
- motive: False (0.22678363515629218)
- opportunity: False (0.1597409870352947)

The culprit is Angelita.
In fact, it is Angelita.
## 5minutemystery-the-card-shark

Map:  31%|███       | 63/203 [1:19:31<3:50:47, 98.91s/ examples] 
Map:  32%|███▏      | 64/203 [1:20:21<3:14:56, 84.15s/ examples]The cowboy is guilty: True or False?
True (0.9596865178182852)
The cowboy is not guilty: True or False?
True (0.9592307815506145)
The cowboy has mean: True or False?
True (0.8955226517597132)
The cowboy has no mean: True or False?
True (0.8727816933272936)
The cowboy has motive: True or False?
True (0.9797840121845385)
The cowboy has no motive: True or False?
True (0.9273632783787477)
The cowboy has opportunity: True or False?
True (0.9522199020698944)
The cowboy has no opportunity: True or False?
True (0.9469902528343473)
The gunslinger is guilty: True or False?
True (0.945399403620829)
The gunslinger is not guilty: True or False?
True (0.9323301884216684)
The gunslinger has mean: True or False?
True (0.919930758847437)
The gunslinger has no mean: True or False?
True (0.8227594449669557)
The gunslinger has motive: True or False?
True (0.9690910565174785)
The gunslinger has no motive: True or False?
True (0.9008791478232747)
The gunslinger has opportunity: True or False?
True (0.9584600345758558)
The gunslinger has no opportunity: True or False?
True (0.9273633336539081)
The lady is guilty: True or False?
True (0.9554855815192022)
The lady is not guilty: True or False?
True (0.9683812262581977)
The lady has mean: True or False?
True (0.8539127077831877)
The lady has no mean: True or False?
True (0.8509647293237851)
The lady has motive: True or False?
True (0.9648551350350516)
The lady has no motive: True or False?
True (0.8868130446009216)
The lady has opportunity: True or False?
True (0.8633915828320894)
The lady has no opportunity: True or False?
True (0.9079670935046645)
The sheriff is guilty: True or False?
True (0.9319595674053855)
The sheriff is not guilty: True or False?
True (0.91789335161495)
The sheriff has mean: True or False?
True (0.8740772044235984)
The sheriff has no mean: True or False?
True (0.7683857617837733)
The sheriff has motive: True or False?
True (0.9690910565174785)
The sheriff has no motive: True or False?
True (0.8469578650997759)
The sheriff has opportunity: True or False?
True (0.928538502080124)
The sheriff has no opportunity: True or False?
True (0.9304582506719414)
### The cowboy
- mean: False (0.1272183066727064)
- motive: False (0.07263672162125234)
- opportunity: False (0.053009747165652654)

### The gunslinger
- mean: False (0.17724055503304426)
- motive: False (0.09912085217672528)
- opportunity: False (0.0726366663460919)

### The lady
- mean: True (0.8539127077831877)
- motive: True (0.9648551350350516)
- opportunity: True (0.8633915828320894)

### The sheriff
- mean: False (0.23161423821622673)
- motive: False (0.1530421349002241)
- opportunity: True (0.928538502080124)

The culprit is The lady.
In fact, it is The sheriff.
## 5minutemystery-department-store-murder
Ed Puckett is guilty: True or False?
True (0.9167081124681512)
Ed Puckett is not guilty: True or False?
True (0.884439109617765)
Ed Puckett has mean: True or False?
True (0.6592954931819778)
Ed Puckett has no mean: True or False?
False (0.5832033700118571)
Ed Puckett has motive: True or False?
True (0.9505947844514345)
Ed Puckett has no motive: True or False?
True (0.7527403228571042)
Ed Puckett has opportunity: True or False?
True (0.7725306828324007)
Ed Puckett has no opportunity: True or False?
True (0.7041601500399041)
Gene Roberts is guilty: True or False?
True (0.8031737798924701)
Gene Roberts is not guilty: True or False?
True (0.7570767382203575)
Gene Roberts has mean: True or False?
False (0.5019531141001669)
Gene Roberts has no mean: True or False?
True (0.6020615685826383)
Gene Roberts has motive: True or False?
True (0.8879840376027315)
Gene Roberts has no motive: True or False?
True (0.7272012283179254)
Gene Roberts has opportunity: True or False?
True (0.8683809699466569)
Gene Roberts has no opportunity: True or False?
True (0.8193157928301305)
George Whitley is guilty: True or False?
True (0.8803863464576128)
George Whitley is not guilty: True or False?
True (0.784649255215384)
George Whitley has mean: True or False?
True (0.6859494535376744)
George Whitley has no mean: True or False?
True (0.5117165908639297)
George Whitley has motive: True or False?
True (0.8879840376027315)
George Whitley has no motive: True or False?
True (0.6662796746479285)
George Whitley has opportunity: True or False?
True (0.6252092625510083)
George Whitley has no opportunity: True or False?
True (0.7217432334405754)
Justin Tanner is guilty: True or False?
True (0.8365545874520802)
Justin Tanner is not guilty: True or False?
True (0.7648916137833577)
Justin Tanner has mean: True or False?
True (0.7379143332111532)
Justin Tanner has no mean: True or False?
True (0.6513548987840652)
Justin Tanner has motive: True or False?
True (0.940789698413215)
Justin Tanner has no motive: True or False?
True (0.740174341079517)
Justin Tanner has opportunity: True or False?
True (0.8762112821835625)
Justin Tanner has no opportunity: True or False?
True (0.8529354946829077)
### Ed Puckett
- mean: True (0.6592954931819778)
- motive: False (0.24725967714289576)
- opportunity: False (0.29583984996009594)

### Gene Roberts
- mean: False (0.5019531141001669)
- motive: False (0.27279877168207456)
- opportunity: False (0.18068420716986955)

### George Whitley
- mean: True (0.6859494535376744)
- motive: True (0.8879840376027315)
- opportunity: True (0.6252092625510083)

### Justin Tanner
- mean: False (0.34864510121593484)
- motive: False (0.25982565892048304)
- opportunity: False (0.14706450531709225)

The culprit is George Whitley.
In fact, it is Justin Tanner.
## 5minutemystery-the-candy-store-mystery
Brianna Cates is guilty: True or False?
True (0.961024938565791)
Brianna Cates is not guilty: True or False?
True (0.9649873376647033)
Brianna Cates has mean: True or False?
True (0.9008791478232747)
Brianna Cates has no mean: True or False?
True (0.8000678954040312)
Brianna Cates has motive: True or False?
True (0.9150529491683197)
Brianna Cates has no motive: True or False?
True (0.7752646804088963)
Brianna Cates has opportunity: True or False?
True (0.8936811689868521)
Brianna Cates has no opportunity: True or False?
True (0.8116760258690822)
Emilee Johnson is guilty: True or False?
True (0.9622497571173928)
Emilee Johnson is not guilty: True or False?
True (0.968856216129913)
Emilee Johnson has mean: True or False?
True (0.9378968460746586)
Emilee Johnson has no mean: True or False?
True (0.7634838269852182)
Emilee Johnson has motive: True or False?
True (0.9756234297188763)
Emilee Johnson has no motive: True or False?
True (0.8499711693725173)
Emilee Johnson has opportunity: True or False?
True (0.9558166865608263)
Emilee Johnson has no opportunity: True or False?
True (0.6926419789019715)
Justin Cates is guilty: True or False?
True (0.9569571625798028)
Justin Cates is not guilty: True or False?
True (0.9626731268425771)
Justin Cates has mean: True or False?
True (0.9219218506394821)
Justin Cates has no mean: True or False?
True (0.7718434926244166)
Justin Cates has motive: True or False?
True (0.9312127242200585)
Justin Cates has no motive: True or False?
True (0.8360197583769845)
Justin Cates has opportunity: True or False?
True (0.944176853162527)
Justin Cates has no opportunity: True or False?
True (0.8860265599597172)
Olivia (Livvie) Johnson is guilty: True or False?
True (0.960804880888677)
Olivia (Livvie) Johnson is not guilty: True or False?
True (0.9655114412719658)
Olivia (Livvie) Johnson has mean: True or False?
True (0.9235923286659299)
Olivia (Livvie) Johnson has no mean: True or False?
True (0.7988153087356352)
Olivia (Livvie) Johnson has motive: True or False?
True (0.9445872321654378)
Olivia (Livvie) Johnson has no motive: True or False?
True (0.8674854614419002)
Olivia (Livvie) Johnson has opportunity: True or False?
True (0.9082930704920021)
Olivia (Livvie) Johnson has no opportunity: True or False?
True (0.7287483223557857)
Trevor Cates is guilty: True or False?
True (0.9655115024177445)
Trevor Cates is not guilty: True or False?
True (0.9635062220717456)
Trevor Cates has mean: True or False?
True (0.8912444106095914)
Trevor Cates has no mean: True or False?
True (0.6757646168022439)
Trevor Cates has motive: True or False?

Map:  32%|███▏      | 65/203 [1:33:21<11:13:39, 292.89s/ examples]
Map:  33%|███▎      | 66/203 [1:34:45<8:45:45, 230.26s/ examples] 
Map:  33%|███▎      | 67/203 [1:35:53<6:51:28, 181.54s/ examples]True (0.9602122316574973)
Trevor Cates has no motive: True or False?
True (0.7461390425540185)
Trevor Cates has opportunity: True or False?
True (0.854884620116169)
Trevor Cates has no opportunity: True or False?
True (0.5165954726976894)
### Brianna Cates
- mean: True (0.9008791478232747)
- motive: True (0.9150529491683197)
- opportunity: True (0.8936811689868521)

### Emilee Johnson
- mean: False (0.23651617301478178)
- motive: False (0.15002883062748273)
- opportunity: False (0.30735802109802846)

### Justin Cates
- mean: False (0.22815650737558335)
- motive: False (0.1639802416230155)
- opportunity: False (0.11397344004028276)

### Olivia (Livvie) Johnson
- mean: False (0.20118469126436478)
- motive: False (0.1325145385580998)
- opportunity: False (0.2712516776442143)

### Trevor Cates
- mean: False (0.32423538319775613)
- motive: False (0.25386095744598147)
- opportunity: False (0.48340452730231065)

The culprit is Brianna Cates.
In fact, it is Justin Cates.
## 5minutemystery-for-the-birds
Billy Mumms is guilty: True or False?
True (0.8778961263000082)
Billy Mumms is not guilty: True or False?
True (0.7786492592534148)
Billy Mumms has mean: True or False?
True (0.7655933544531522)
Billy Mumms has no mean: True or False?
True (0.7839884808423031)
Billy Mumms has motive: True or False?
True (0.8244619332958376)
Billy Mumms has no motive: True or False?
True (0.7833262669301256)
Billy Mumms has opportunity: True or False?
True (0.9353465445225602)
Billy Mumms has no opportunity: True or False?
True (0.8418256636710214)
Cheryl Judson is guilty: True or False?
True (0.9326989624184171)
Cheryl Judson is not guilty: True or False?
True (0.8766343647921183)
Cheryl Judson has mean: True or False?
True (0.7490872087035162)
Cheryl Judson has no mean: True or False?
True (0.7683857617837733)
Cheryl Judson has motive: True or False?
True (0.8940517282497483)
Cheryl Judson has no motive: True or False?
True (0.8413048399699521)
Cheryl Judson has opportunity: True or False?
True (0.9427180278987515)
Cheryl Judson has no opportunity: True or False?
True (0.8504686406728537)
Stan Mifflin is guilty: True or False?
True (0.8929365260632085)
Stan Mifflin is not guilty: True or False?
True (0.8670357473609658)
Stan Mifflin has mean: True or False?
True (0.7662936378892937)
Stan Mifflin has no mean: True or False?
True (0.7364006034245382)
Stan Mifflin has motive: True or False?
True (0.934872446722342)
Stan Mifflin has no motive: True or False?
True (0.874934615163517)
Stan Mifflin has opportunity: True or False?
True (0.9693242313725606)
Stan Mifflin has no opportunity: True or False?
True (0.8727816933272936)
Tor Hansen is guilty: True or False?
True (0.8198933606225757)
Tor Hansen is not guilty: True or False?
True (0.7209580648179327)
Tor Hansen has mean: True or False?
True (0.9946713536393796)
Tor Hansen has no mean: True or False?
True (0.5888891620166576)
Tor Hansen has motive: True or False?
True (0.8272706865691472)
Tor Hansen has no motive: True or False?
True (0.7739006258141444)
Tor Hansen has opportunity: True or False?
True (0.9073122118500465)
Tor Hansen has no opportunity: True or False?
True (0.8872045854516336)
### Billy Mumms
- mean: True (0.7655933544531522)
- motive: True (0.8244619332958376)
- opportunity: True (0.9353465445225602)

### Cheryl Judson
- mean: True (0.7490872087035162)
- motive: False (0.1586951600300479)
- opportunity: False (0.14953135932714634)

### Stan Mifflin
- mean: False (0.26359939657546183)
- motive: False (0.125065384836483)
- opportunity: False (0.1272183066727064)

### Tor Hansen
- mean: False (0.41111083798334236)
- motive: False (0.22609937418585557)
- opportunity: False (0.11279541454836639)

The culprit is Billy Mumms.
In fact, it is Cheryl Judson.
## 5minutemystery-the-zoo-job
Cindy is guilty: True or False?
True (0.883638205304735)
Cindy is not guilty: True or False?
True (0.9240047963507929)
Cindy has mean: True or False?
True (0.8074606715677252)
Cindy has no mean: True or False?
True (0.8000678477162699)
Cindy has motive: True or False?
True (0.9114953293645017)
Cindy has no motive: True or False?
True (0.8860265005470086)
Cindy has opportunity: True or False?
True (0.7969253675907205)
Cindy has no opportunity: True or False?
True (0.7162185953247016)
Henry is guilty: True or False?
True (0.8797679608387514)
Henry is not guilty: True or False?
True (0.9264369634617509)
Henry has mean: True or False?
True (0.7634837587244478)
Henry has no mean: True or False?
True (0.8459424357871997)
Henry has motive: True or False?
True (0.9435560124549824)
Henry has no motive: True or False?
True (0.9161096235973493)
Henry has opportunity: True or False?
True (0.8300437258865985)
Henry has no opportunity: True or False?
True (0.8006919661398397)
Leonard is guilty: True or False?
True (0.8418256636710214)
Leonard is not guilty: True or False?
True (0.9390248079664695)
Leonard has mean: True or False?
True (0.8000678954040312)
Leonard has no mean: True or False?
True (0.7813306496768853)
Leonard has motive: True or False?
True (0.947962222968318)
Leonard has no motive: True or False?
True (0.8762112821835625)
Leonard has opportunity: True or False?
True (0.8899121304559661)
Leonard has no opportunity: True or False?
True (0.7806625377756776)
Tom is guilty: True or False?
True (0.8725647371909419)
Tom is not guilty: True or False?
True (0.9071478234767817)
Tom has mean: True or False?
True (0.8927496657814362)
Tom has no mean: True or False?
True (0.8674854614419002)
Tom has motive: True or False?
True (0.9335520893498362)
Tom has no motive: True or False?
True (0.8620035048683017)
Tom has opportunity: True or False?
True (0.8980534699860239)
Tom has no opportunity: True or False?
True (0.8674854614419002)
### Cindy
- mean: False (0.19993215228373007)
- motive: False (0.1139734994529914)
- opportunity: False (0.28378140467529844)

### Henry
- mean: True (0.7634837587244478)
- motive: True (0.9435560124549824)
- opportunity: True (0.8300437258865985)

### Leonard
- mean: False (0.21866935032311474)
- motive: False (0.12378871781643752)
- opportunity: False (0.21933746222432238)

### Tom
- mean: False (0.1325145385580998)
- motive: False (0.13799649513169832)
- opportunity: False (0.1325145385580998)

The culprit is Henry.
In fact, it is Cindy.
## 5minutemystery-did-the-vicar-solve-the-mystery
Elmer Tydings is guilty: True or False?
True (0.9820138217808033)
Elmer Tydings is not guilty: True or False?
True (0.9921080468827638)
Elmer Tydings has mean: True or False?
True (0.9743860965141968)
Elmer Tydings has no mean: True or False?
True (0.9643886093607492)
Elmer Tydings has motive: True or False?
True (0.9902445073767759)
Elmer Tydings has no motive: True or False?
True (0.972362279388711)
Elmer Tydings has opportunity: True or False?
True (0.9643214331583058)
Elmer Tydings has no opportunity: True or False?
True (0.9063219998220023)
John Stubbs is guilty: True or False?
True (0.9787533276905257)
John Stubbs is not guilty: True or False?
True (0.9884250164215337)
John Stubbs has mean: True or False?
True (0.981021999947924)
John Stubbs has no mean: True or False?
True (0.9645892964498279)
John Stubbs has motive: True or False?
True (0.9832306498689419)
John Stubbs has no motive: True or False?
True (0.9780517227981328)
John Stubbs has opportunity: True or False?
True (0.9651190622502646)
John Stubbs has no opportunity: True or False?
True (0.8899121304559661)
Katherine Tydings is guilty: True or False?
True (0.9752489919994439)
Katherine Tydings is not guilty: True or False?
True (0.9894702436088533)
Katherine Tydings has mean: True or False?
True (0.9752018447706344)
Katherine Tydings has no mean: True or False?
True (0.9658995863383641)
Katherine Tydings has motive: True or False?
True (0.9885914322998767)
Katherine Tydings has no motive: True or False?
True (0.9730364677532105)
Katherine Tydings has opportunity: True or False?
True (0.9724147321673792)
Katherine Tydings has no opportunity: True or False?
True (0.925499741040984)
Louise Stubbs is guilty: True or False?
True (0.9606574760904091)
Louise Stubbs is not guilty: True or False?
True (0.9787126175579408)
Louise Stubbs has mean: True or False?

Map:  33%|███▎      | 68/203 [1:37:20<5:45:01, 153.34s/ examples]
Map:  34%|███▍      | 69/203 [1:38:50<5:00:00, 134.33s/ examples]
Map:  34%|███▍      | 70/203 [1:40:01<4:15:34, 115.30s/ examples]True (0.9420819287658885)
Louise Stubbs has no mean: True or False?
True (0.9029524930853913)
Louise Stubbs has motive: True or False?
True (0.9738940592742902)
Louise Stubbs has no motive: True or False?
True (0.9491062747098069)
Louise Stubbs has opportunity: True or False?
True (0.9666631825345839)
Louise Stubbs has no opportunity: True or False?
True (0.8727817583545995)
### Elmer Tydings
- mean: False (0.035611390639250784)
- motive: False (0.027637720611288996)
- opportunity: False (0.09367800017799766)

### John Stubbs
- mean: False (0.03541070355017206)
- motive: False (0.021948277201867206)
- opportunity: False (0.11008786954403393)

### Katherine Tydings
- mean: True (0.9752018447706344)
- motive: True (0.9885914322998767)
- opportunity: True (0.9724147321673792)

### Louise Stubbs
- mean: False (0.09704750691460873)
- motive: False (0.05089372529019309)
- opportunity: False (0.12721824164540052)

The culprit is Katherine Tydings.
In fact, it is Katherine Tydings.
## 5minutemystery-who-scratched-the-porsche
Colonel Greenerbaum is guilty: True or False?
True (0.9113376113103917)
Colonel Greenerbaum is not guilty: True or False?
True (0.8984105603938967)
Colonel Greenerbaum has mean: True or False?
True (0.8840392254230673)
Colonel Greenerbaum has no mean: True or False?
True (0.8705973031072073)
Colonel Greenerbaum has motive: True or False?
True (0.9452984928501705)
Colonel Greenerbaum has no motive: True or False?
True (0.7483522884503825)
Colonel Greenerbaum has opportunity: True or False?
True (0.8697145551802641)
Colonel Greenerbaum has no opportunity: True or False?
True (0.7090191197769757)
Fido is guilty: True or False?
False (0.8481214046032184)
Fido is not guilty: True or False?
False (1.9338323320172133)
Fido has mean: True or False?
False (2.821102743875856)
Fido has no mean: True or False?
False (0.7271219770888045)
Fido has motive: True or False?
False (1.7946410176084657)
Fido has no motive: True or False?
False (1.0247375944792216)
Fido has opportunity: True or False?
False (1.792952879485295)
Fido has no opportunity: True or False?
False (1.5184637430347812)
Malcolm is guilty: True or False?
True (0.8998277786460391)
Malcolm is not guilty: True or False?
True (0.8795611817678315)
Malcolm has mean: True or False?
True (0.9353465445225602)
Malcolm has no mean: True or False?
True (0.821044090050916)
Malcolm has motive: True or False?
True (0.897695304229796)
Malcolm has no motive: True or False?
True (0.7549149447629944)
Malcolm has opportunity: True or False?
True (0.9036349079321685)
Malcolm has no opportunity: True or False?
True (0.7655932860037753)
Roxie is guilty: True or False?
True (0.8980535302052036)
Roxie is not guilty: True or False?
True (0.9403530352223053)
Roxie has mean: True or False?
True (0.673191669892235)
Roxie has no mean: True or False?
True (0.6224593484250324)
Roxie has motive: True or False?
True (0.904313027820426)
Roxie has no motive: True or False?
True (0.8181563669811865)
Roxie has opportunity: True or False?
True (0.8444089912414552)
Roxie has no opportunity: True or False?
True (0.7662936378892937)
### Colonel Greenerbaum
- mean: False (0.1294026968927927)
- motive: False (0.2516477115496175)
- opportunity: False (0.29098088022302426)

### Fido
- mean: False (2.821102743875856)
- motive: False (1.7946410176084657)
- opportunity: False (1.792952879485295)

### Malcolm
- mean: False (0.17895590994908395)
- motive: False (0.24508505523700563)
- opportunity: False (0.2344067139962247)

### Roxie
- mean: True (0.673191669892235)
- motive: True (0.904313027820426)
- opportunity: True (0.8444089912414552)

The culprit is Roxie.
In fact, it is Colonel Greenerbaum.
## 5minutemystery-the-thief-in-the-night-mystery
Jon Shaw is guilty: True or False?
True (0.8697145551802641)
Jon Shaw is not guilty: True or False?
True (0.8338664134858856)
Jon Shaw has mean: True or False?
True (0.8381505623254643)
Jon Shaw has no mean: True or False?
True (0.7839884808423031)
Jon Shaw has motive: True or False?
True (0.9318356525033217)
Jon Shaw has no motive: True or False?
True (0.7732163648437078)
Jon Shaw has opportunity: True or False?
True (0.7512834059294674)
Jon Shaw has no opportunity: True or False?
False (0.5117165908639297)
Max Reinke is guilty: True or False?
True (0.884439109617765)
Max Reinke is not guilty: True or False?
True (0.9178934131644976)
Max Reinke has mean: True or False?
True (0.9324533354081785)
Max Reinke has no mean: True or False?
True (0.9378968460746586)
Max Reinke has motive: True or False?
True (0.9456006903352807)
Max Reinke has no motive: True or False?
True (0.905989824801558)
Max Reinke has opportunity: True or False?
True (0.9471859926317535)
Max Reinke has no opportunity: True or False?
True (0.8606035648396906)
Todd Summers is guilty: True or False?
True (0.7348812840309261)
Todd Summers is not guilty: True or False?
True (0.6233768569026616)
Todd Summers has mean: True or False?
True (0.7988152492192591)
Todd Summers has no mean: True or False?
True (0.6169358476670045)
Todd Summers has motive: True or False?
True (0.905989824801558)
Todd Summers has no motive: True or False?
True (0.7341195403199204)
Todd Summers has opportunity: True or False?
True (0.6415346823638186)
Todd Summers has no opportunity: True or False?
False (0.5851011336505011)
Zac Coulson is guilty: True or False?
True (0.9575961815839735)
Zac Coulson is not guilty: True or False?
True (0.879146760693242)
Zac Coulson has mean: True or False?
True (0.8980534699860239)
Zac Coulson has no mean: True or False?
True (0.8918110736745599)
Zac Coulson has motive: True or False?
True (0.9761291751471208)
Zac Coulson has no motive: True or False?
True (0.9105454073245608)
Zac Coulson has opportunity: True or False?
True (0.8918110138739693)
Zac Coulson has no opportunity: True or False?
True (0.7065954713132195)
### Jon Shaw
- mean: False (0.2160115191576969)
- motive: False (0.22678363515629218)
- opportunity: True (0.7512834059294674)

### Max Reinke
- mean: True (0.9324533354081785)
- motive: True (0.9456006903352807)
- opportunity: True (0.9471859926317535)

### Todd Summers
- mean: False (0.3830641523329955)
- motive: False (0.26588045968007956)
- opportunity: True (0.6415346823638186)

### Zac Coulson
- mean: False (0.10818892632544008)
- motive: False (0.0894545926754392)
- opportunity: False (0.29340452868678046)

The culprit is Max Reinke.
In fact, it is Zac Coulson.
## 5minutemystery-ladies-at-table
Alice is guilty: True or False?
True (0.779321849347754)
Alice is not guilty: True or False?
True (0.9193534273597669)
Alice has mean: True or False?
False (0.5431680717579583)
Alice has no mean: True or False?
True (0.8068526417769779)
Alice has motive: True or False?
True (0.9167080509980843)
Alice has no motive: True or False?
True (0.8577681165234065)
Alice has opportunity: True or False?
True (0.9230391416137353)
Alice has no opportunity: True or False?
True (0.84440905415483)
Frances is guilty: True or False?
True (0.8311430212356835)
Frances is not guilty: True or False?
True (0.9227612010756272)
Frances has mean: True or False?
True (0.7256486384635821)
Frances has no mean: True or False?
True (0.7049732868303878)
Frances has motive: True or False?
True (0.905989824801558)
Frances has no motive: True or False?
True (0.8050197341926492)
Frances has opportunity: True or False?
True (0.8925625120974553)
Frances has no opportunity: True or False?
True (0.7534666630720156)
Leona is guilty: True or False?
True (0.8852351930010195)
Leona is not guilty: True or False?
True (0.9265699426348812)
Leona has mean: True or False?
True (0.847967740521315)
Leona has no mean: True or False?
True (0.8000678954040312)
Leona has motive: True or False?
True (0.9319595674053855)
Leona has no motive: True or False?
True (0.9082930704920021)
Leona has opportunity: True or False?
True (0.9516839395409852)
Leona has no opportunity: True or False?
True (0.7950222460539826)
Mary is guilty: True or False?
True (0.821044090050916)
Mary is not guilty: True or False?
True (0.919930758847437)
Mary has mean: True or False?
True (0.7988153087356352)
Mary has no mean: True or False?
True (0.64779823427608)

Map:  35%|███▍      | 71/203 [1:41:07<3:40:41, 100.32s/ examples]
Map:  35%|███▌      | 72/203 [1:42:16<3:18:43, 91.02s/ examples] 
Map:  36%|███▌      | 73/203 [1:43:19<2:59:02, 82.64s/ examples]Mary has motive: True or False?
True (0.8633915828320894)
Mary has no motive: True or False?
True (0.8643104392003704)
Mary has opportunity: True or False?
True (0.893681109060862)
Mary has no opportunity: True or False?
True (0.6160122877297346)
Ruth is guilty: True or False?
True (0.7008948290825966)
Ruth is not guilty: True or False?
True (0.8982321045224891)
Ruth has mean: True or False?
True (0.8502200206694925)
Ruth has no mean: True or False?
True (0.7217432334405754)
Ruth has motive: True or False?
True (0.9323301884216684)
Ruth has no motive: True or False?
True (0.9026096497507297)
Ruth has opportunity: True or False?
True (0.9173026661190045)
Ruth has no opportunity: True or False?
True (0.7739006258141444)
### Alice
- mean: False (0.5431680717579583)
- motive: False (0.14223188347659355)
- opportunity: False (0.15559094584516997)

### Frances
- mean: False (0.29502671316961215)
- motive: False (0.19498026580735084)
- opportunity: False (0.2465333369279844)

### Leona
- mean: True (0.847967740521315)
- motive: True (0.9319595674053855)
- opportunity: True (0.9516839395409852)

### Mary
- mean: False (0.35220176572392004)
- motive: True (0.8633915828320894)
- opportunity: False (0.3839877122702654)

### Ruth
- mean: False (0.27825676655942455)
- motive: False (0.09739035024927034)
- opportunity: False (0.22609937418585557)

The culprit is Leona.
In fact, it is Leona.
## 5minutemystery-the-diamond-necklace
Abby Grant is guilty: True or False?
True (0.9336731438527403)
Abby Grant is not guilty: True or False?
True (0.9149009617112335)
Abby Grant has mean: True or False?
True (0.7859664553110391)
Abby Grant has no mean: True or False?
True (0.9111797236708432)
Abby Grant has motive: True or False?
True (0.9753900767342161)
Abby Grant has no motive: True or False?
True (0.9390248079664695)
Abby Grant has opportunity: True or False?
True (0.9572778330298248)
Abby Grant has no opportunity: True or False?
True (0.9580695040202324)
Colonel Barrow is guilty: True or False?
True (0.8568122940392877)
Colonel Barrow is not guilty: True or False?
True (0.8534247816107388)
Colonel Barrow has mean: True or False?
True (0.5214711377329961)
Colonel Barrow has no mean: True or False?
True (0.5448014304301324)
Colonel Barrow has motive: True or False?
True (0.9787938590250385)
Colonel Barrow has no motive: True or False?
True (0.8423451152856819)
Colonel Barrow has opportunity: True or False?
True (0.983214557402718)
Colonel Barrow has no opportunity: True or False?
True (0.8624675215861032)
Fiona Duncan is guilty: True or False?
False (0.8554494017777171)
Fiona Duncan is not guilty: True or False?
False (0.5626912249720392)
Fiona Duncan has mean: True or False?
False (0.9530570094344373)
Fiona Duncan has no mean: True or False?
False (1.44517182842555)
Fiona Duncan has motive: True or False?
False (1.6622269950246393)
Fiona Duncan has no motive: True or False?
False (1.1102346723644756)
Fiona Duncan has opportunity: True or False?
False (0.9353123000985991)
Fiona Duncan has no opportunity: True or False?
False (1.2395657394523885)
Harold Duncan is guilty: True or False?
True (0.9066531077351827)
Harold Duncan is not guilty: True or False?
True (0.8652241235443877)
Harold Duncan has mean: True or False?
True (0.8074605993751186)
Harold Duncan has no mean: True or False?
False (0.5640984002718568)
Harold Duncan has motive: True or False?
True (0.971019387667922)
Harold Duncan has no motive: True or False?
True (0.7371581232960549)
Harold Duncan has opportunity: True or False?
True (0.9233161821369215)
Harold Duncan has no opportunity: True or False?
True (0.7386690954574974)
Maurice Eades is guilty: True or False?
True (0.9276259554905466)
Maurice Eades is not guilty: True or False?
True (0.9365176577773374)
Maurice Eades has mean: True or False?
False (0.5312093941731293)
Maurice Eades has no mean: True or False?
False (0.5136684743338078)
Maurice Eades has motive: True or False?
True (0.9819446807697475)
Maurice Eades has no motive: True or False?
True (0.9252299659402181)
Maurice Eades has opportunity: True or False?
True (0.9756698013402983)
Maurice Eades has no opportunity: True or False?
True (0.9536218061663073)
### Abby Grant
- mean: True (0.7859664553110391)
- motive: True (0.9753900767342161)
- opportunity: True (0.9572778330298248)

### Colonel Barrow
- mean: True (0.5214711377329961)
- motive: False (0.1576548847143181)
- opportunity: False (0.13753247841389682)

### Fiona Duncan
- mean: True (0.0)
- motive: False (1.6622269950246393)
- opportunity: True (0.0)

### Harold Duncan
- mean: True (0.8074605993751186)
- motive: False (0.2628418767039451)
- opportunity: False (0.26133090454250263)

### Maurice Eades
- mean: True (0.4863315256661922)
- motive: False (0.07477003405978189)
- opportunity: False (0.04637819383369268)

The culprit is Abby Grant.
In fact, it is Fiona Duncan.
## 5minutemystery-rhyming-presidents-mystery
George Bush is guilty: True or False?
True (0.8832359917473193)
George Bush is not guilty: True or False?
True (0.8897206197970384)
George Bush has mean: True or False?
True (0.5860491337676195)
George Bush has no mean: True or False?
True (0.8169911556077801)
George Bush has motive: True or False?
True (0.9086178579521682)
George Bush has no motive: True or False?
True (0.867485409735739)
George Bush has opportunity: True or False?
True (0.7379142672364736)
George Bush has no opportunity: True or False?
True (0.7225270177274575)
Gerald Ford is guilty: True or False?
True (0.8955227118091885)
Gerald Ford is not guilty: True or False?
True (0.8868130446009216)
Gerald Ford has mean: True or False?
True (0.7264255794048772)
Gerald Ford has no mean: True or False?
True (0.7872777601997338)
Gerald Ford has motive: True or False?
True (0.9005298588820442)
Gerald Ford has no motive: True or False?
True (0.8807970862580315)
Gerald Ford has opportunity: True or False?
True (0.6984322578436808)
Gerald Ford has no opportunity: True or False?
True (0.7570767382203575)
John Quincy Adams is guilty: True or False?
True (0.8519527857346616)
John Quincy Adams is not guilty: True or False?
True (0.8710367026584496)
John Quincy Adams has mean: True or False?
True (0.6095241271158658)
John Quincy Adams has no mean: True or False?
True (0.7813306496768853)
John Quincy Adams has motive: True or False?
True (0.878314250659373)
John Quincy Adams has no motive: True or False?
True (0.8795611817678315)
John Quincy Adams has opportunity: True or False?
True (0.6113820047705449)
John Quincy Adams has no opportunity: True or False?
True (0.6791787167336184)
Richard Nixon is guilty: True or False?
True (0.8624675215861032)
Richard Nixon is not guilty: True or False?
True (0.883638205304735)
Richard Nixon has mean: True or False?
True (0.7606506318580792)
Richard Nixon has no mean: True or False?
True (0.8670357473609658)
Richard Nixon has motive: True or False?
True (0.9244151684978138)
Richard Nixon has no motive: True or False?
True (0.8975158335791911)
Richard Nixon has opportunity: True or False?
True (0.7745833916423246)
Richard Nixon has no opportunity: True or False?
True (0.8624675215861032)
### George Bush
- mean: True (0.5860491337676195)
- motive: False (0.13251459026426105)
- opportunity: False (0.27747298227254247)

### Gerald Ford
- mean: True (0.7264255794048772)
- motive: False (0.11920291374196845)
- opportunity: True (0.6984322578436808)

### John Quincy Adams
- mean: True (0.6095241271158658)
- motive: True (0.878314250659373)
- opportunity: True (0.6113820047705449)

### Richard Nixon
- mean: True (0.7606506318580792)
- motive: False (0.10248416642080893)
- opportunity: True (0.7745833916423246)

The culprit is John Quincy Adams.
In fact, it is Gerald Ford.
## 5minutemystery-the-white-house-ghosts
Andrew Jackson is guilty: True or False?
True (0.8606036289596553)
Andrew Jackson is not guilty: True or False?
True (0.9491062747098069)
Andrew Jackson has mean: True or False?
True (0.9358173616900589)
Andrew Jackson has no mean: True or False?
True (0.8803863464576128)
Andrew Jackson has motive: True or False?
True (0.9798997635332343)
Andrew Jackson has no motive: True or False?
True (0.8969755785184792)

Map:  36%|███▋      | 74/203 [1:44:37<2:54:47, 81.30s/ examples]
Map:  37%|███▋      | 75/203 [1:45:54<2:50:37, 79.98s/ examples]Andrew Jackson has opportunity: True or False?
True (0.9124361266596831)
Andrew Jackson has no opportunity: True or False?
True (0.942081869103903)
Calvin Coolidge is guilty: True or False?
True (0.9142907234091052)
Calvin Coolidge is not guilty: True or False?
True (0.9558166865608263)
Calvin Coolidge has mean: True or False?
True (0.950777887812089)
Calvin Coolidge has no mean: True or False?
True (0.9012274173198201)
Calvin Coolidge has motive: True or False?
True (0.9694401031032759)
Calvin Coolidge has no motive: True or False?
True (0.8745065279415651)
Calvin Coolidge has opportunity: True or False?
True (0.952041865762172)
Calvin Coolidge has no opportunity: True or False?
True (0.9422946582938823)
John Adams is guilty: True or False?
True (0.9190633328333496)
John Adams is not guilty: True or False?
True (0.9582260855240093)
John Adams has mean: True or False?
True (0.9716717007848752)
John Adams has no mean: True or False?
True (0.9312127242200585)
John Adams has motive: True or False?
True (0.9826908710080852)
John Adams has no motive: True or False?
True (0.9355823382423648)
John Adams has opportunity: True or False?
True (0.9173026661190045)
John Adams has no opportunity: True or False?
True (0.9360515445140636)
William Howard Taft is guilty: True or False?
True (0.911809984585868)
William Howard Taft is not guilty: True or False?
True (0.9571177375286347)
William Howard Taft has mean: True or False?
True (0.9651191233711941)
William Howard Taft has no mean: True or False?
True (0.944176853162527)
William Howard Taft has motive: True or False?
True (0.9872772696831444)
William Howard Taft has no motive: True or False?
True (0.9381240005131491)
William Howard Taft has opportunity: True or False?
True (0.921357630313903)
William Howard Taft has no opportunity: True or False?
True (0.9263037480179213)
### Andrew Jackson
- mean: False (0.11961365354238718)
- motive: False (0.1030244214815208)
- opportunity: True (0.9124361266596831)

### Calvin Coolidge
- mean: False (0.09877258268017985)
- motive: False (0.12549347205843486)
- opportunity: False (0.05770534170611774)

### John Adams
- mean: False (0.06878727577994148)
- motive: False (0.06441766175763519)
- opportunity: True (0.9173026661190045)

### William Howard Taft
- mean: True (0.9651191233711941)
- motive: True (0.9872772696831444)
- opportunity: True (0.921357630313903)

The culprit is William Howard Taft.
In fact, it is Calvin Coolidge.
## 5minutemystery-mr-patrick-and-the-graveyard-mystery
Grave no.1 is guilty: True or False?
True (0.9655115024177445)
Grave no.1 is not guilty: True or False?
True (0.9593831890064877)
Grave no.1 has mean: True or False?
True (0.918626370973125)
Grave no.1 has no mean: True or False?
True (0.8929365260632085)
Grave no.1 has motive: True or False?
True (0.953361928704124)
Grave no.1 has no motive: True or False?
True (0.9431384220853135)
Grave no.1 has opportunity: True or False?
True (0.8902942539348153)
Grave no.1 has no opportunity: True or False?
True (0.8238959285889558)
Grave no.2 is guilty: True or False?
True (0.9652503733161137)
Grave no.2 is not guilty: True or False?
True (0.9666631825345839)
Grave no.2 has mean: True or False?
True (0.9486325389479346)
Grave no.2 has no mean: True or False?
True (0.9167080509980843)
Grave no.2 has motive: True or False?
True (0.963368656065788)
Grave no.2 has no motive: True or False?
True (0.943970619289785)
Grave no.2 has opportunity: True or False?
True (0.9155072008980665)
Grave no.2 has no opportunity: True or False?
True (0.8305941261447712)
Grave no.3 is guilty: True or False?
True (0.9666001797251225)
Grave no.3 is not guilty: True or False?
True (0.9666001797251225)
Grave no.3 has mean: True or False?
True (0.9165588616316169)
Grave no.3 has no mean: True or False?
True (0.911809923444246)
Grave no.3 has motive: True or False?
True (0.958847105894029)
Grave no.3 has no motive: True or False?
True (0.9383503780077049)
Grave no.3 has opportunity: True or False?
True (0.8973360043541736)
Grave no.3 has no opportunity: True or False?
True (0.8204694405411458)
Grave no.4 is guilty: True or False?
True (0.9747731684499236)
Grave no.4 is not guilty: True or False?
True (0.9744833710245325)
Grave no.4 has mean: True or False?
True (0.9099070446252667)
Grave no.4 has no mean: True or False?
True (0.9167081124681512)
Grave no.4 has motive: True or False?
True (0.9708540445899615)
Grave no.4 has no motive: True or False?
True (0.952041865762172)
Grave no.4 has opportunity: True or False?
True (0.8879840376027315)
Grave no.4 has no opportunity: True or False?
True (0.8210441512234701)
Grave no.5 is guilty: True or False?
True (0.9742394081324117)
Grave no.5 is not guilty: True or False?
True (0.969324171790829)
Grave no.5 has mean: True or False?
True (0.9555685526018006)
Grave no.5 has no mean: True or False?
True (0.9527502639818524)
Grave no.5 has motive: True or False?
True (0.974580348460635)
Grave no.5 has no motive: True or False?
True (0.9662834994150223)
Grave no.5 has opportunity: True or False?
True (0.9376689781587124)
Grave no.5 has no opportunity: True or False?
True (0.9257686153543061)
### Grave no.1
- mean: False (0.1070634739367915)
- motive: False (0.05686157791468649)
- opportunity: False (0.17610407141104423)

### Grave no.2
- mean: False (0.08329194900191572)
- motive: False (0.056029380710215015)
- opportunity: False (0.16940587385522876)

### Grave no.3
- mean: False (0.08819007655575395)
- motive: False (0.06164962199229507)
- opportunity: False (0.1795305594588542)

### Grave no.4
- mean: True (0.9099070446252667)
- motive: False (0.04795813423782802)
- opportunity: False (0.17895584877652992)

### Grave no.5
- mean: True (0.9555685526018006)
- motive: True (0.974580348460635)
- opportunity: True (0.9376689781587124)

The culprit is Grave no.5.
In fact, it is Grave no.4.
## 5minutemystery-lockbox-100
Edward Frates is guilty: True or False?
True (0.9291837815043049)
Edward Frates is not guilty: True or False?
True (0.948346255948953)
Edward Frates has mean: True or False?
True (0.7065955344877805)
Edward Frates has no mean: True or False?
True (0.7154240000492645)
Edward Frates has motive: True or False?
True (0.9640517228653248)
Edward Frates has no motive: True or False?
True (0.8824278665848695)
Edward Frates has opportunity: True or False?
True (0.9616780268435321)
Edward Frates has no opportunity: True or False?
True (0.9190633328333496)
James Madigan is guilty: True or False?
True (0.8577681165234065)
James Madigan is not guilty: True or False?
True (0.8606035648396906)
James Madigan has mean: True or False?
True (0.65489470935198)
James Madigan has no mean: True or False?
True (0.6671476985798853)
James Madigan has motive: True or False?
True (0.958537757711882)
James Madigan has no motive: True or False?
True (0.8812066389307215)
James Madigan has opportunity: True or False?
True (0.94948238112973)
James Madigan has no opportunity: True or False?
True (0.8895288719962232)
Peter Zielny is guilty: True or False?
True (0.8397339530959691)
Peter Zielny is not guilty: True or False?
True (0.832781310996106)
Peter Zielny has mean: True or False?
True (0.858244061606496)
Peter Zielny has no mean: True or False?
True (0.8193157928301305)
Peter Zielny has motive: True or False?
True (0.9786310784192824)
Peter Zielny has no motive: True or False?
True (0.9334307932218529)
Peter Zielny has opportunity: True or False?
True (0.9695556762577888)
Peter Zielny has no opportunity: True or False?
True (0.9531007408873468)
Ronald Finch is guilty: True or False?
True (0.9553191057869168)
Ronald Finch is not guilty: True or False?
True (0.9622497571173928)
Ronald Finch has mean: True or False?
True (0.9127477403975288)
Ronald Finch has no mean: True or False?
True (0.9139841191734227)
Ronald Finch has motive: True or False?
True (0.9863104819435934)
Ronald Finch has no motive: True or False?
True (0.9612438076473231)
Ronald Finch has opportunity: True or False?
True (0.9874235991199588)
Ronald Finch has no opportunity: True or False?
True (0.96224969617818)
Russell Winwood is guilty: True or False?
True (0.911809984585868)
Russell Winwood is not guilty: True or False?

Map:  37%|███▋      | 76/203 [1:47:06<2:43:52, 77.42s/ examples]
Map:  38%|███▊      | 77/203 [1:48:44<2:55:32, 83.59s/ examples]
Map:  38%|███▊      | 78/203 [1:50:12<2:56:54, 84.92s/ examples]True (0.921357630313903)
Russell Winwood has mean: True or False?
True (0.9114953293645017)
Russell Winwood has no mean: True or False?
True (0.7356416476869558)
Russell Winwood has motive: True or False?
True (0.972362279388711)
Russell Winwood has no motive: True or False?
True (0.879146760693242)
Russell Winwood has opportunity: True or False?
True (0.9577544910931239)
Russell Winwood has no opportunity: True or False?
True (0.8933094122075369)
### Edward Frates
- mean: True (0.7065955344877805)
- motive: False (0.11757213341513051)
- opportunity: False (0.08093666716665038)

### James Madigan
- mean: True (0.65489470935198)
- motive: False (0.11879336106927851)
- opportunity: False (0.11047112800377679)

### Peter Zielny
- mean: False (0.18068420716986955)
- motive: False (0.06656920677814715)
- opportunity: False (0.04689925911265325)

### Ronald Finch
- mean: True (0.9127477403975288)
- motive: True (0.9863104819435934)
- opportunity: True (0.9874235991199588)

### Russell Winwood
- mean: False (0.26435835231304416)
- motive: False (0.12085323930675795)
- opportunity: False (0.1066905877924631)

The culprit is Ronald Finch.
In fact, it is Russell Winwood.
## 5minutemystery-mystery-at-the-detectives-office
Joe the janitor is guilty: True or False?
True (0.9268352400785028)
Joe the janitor is not guilty: True or False?
True (0.9749168755454501)
Joe the janitor has mean: True or False?
True (0.9053223122169206)
Joe the janitor has no mean: True or False?
True (0.941654147692963)
Joe the janitor has motive: True or False?
True (0.9538802513450514)
Joe the janitor has no motive: True or False?
True (0.8962513214730718)
Joe the janitor has opportunity: True or False?
True (0.9235923286659299)
Joe the janitor has no opportunity: True or False?
True (0.814643384779728)
Larry is guilty: True or False?
True (0.9100670238942131)
Larry is not guilty: True or False?
True (0.9543930284832085)
Larry has mean: True or False?
True (0.9643214331583058)
Larry has no mean: True or False?
True (0.9491062747098069)
Larry has motive: True or False?
True (0.9718859797630299)
Larry has no motive: True or False?
True (0.9407897579933674)
Larry has opportunity: True or False?
True (0.9346342066470359)
Larry has no opportunity: True or False?
True (0.911809923444246)
Mr. Jorgensen is guilty: True or False?
True (0.866132552869269)
Mr. Jorgensen is not guilty: True or False?
True (0.9494823209990744)
Mr. Jorgensen has mean: True or False?
True (0.9392480858026054)
Mr. Jorgensen has no mean: True or False?
True (0.9102267057681164)
Mr. Jorgensen has motive: True or False?
True (0.9429286143036572)
Mr. Jorgensen has no motive: True or False?
True (0.7872777601997338)
Mr. Jorgensen has opportunity: True or False?
True (0.9053223122169206)
Mr. Jorgensen has no opportunity: True or False?
True (0.7662936378892937)
the building manager is guilty: True or False?
True (0.860369148541484)
the building manager is not guilty: True or False?
True (0.811078188867804)
the building manager has mean: True or False?
True (0.720171518230031)
the building manager has no mean: True or False?
True (0.7154240000492645)
the building manager has motive: True or False?
True (0.9127477403975288)
the building manager has no motive: True or False?
True (0.7752646804088963)
the building manager has opportunity: True or False?
True (0.8031737798924701)
the building manager has no opportunity: True or False?
True (0.5860490988363701)
### Joe the janitor
- mean: True (0.9053223122169206)
- motive: False (0.10374867852692815)
- opportunity: False (0.18535661522027203)

### Larry
- mean: True (0.9643214331583058)
- motive: True (0.9718859797630299)
- opportunity: True (0.9346342066470359)

### Mr. Jorgensen
- mean: False (0.08977329423188363)
- motive: False (0.21272223980026617)
- opportunity: False (0.23370636211070628)

### the building manager
- mean: False (0.28457599995073546)
- motive: False (0.2247353195911037)
- opportunity: False (0.41395090116362987)

The culprit is Larry.
In fact, it is the building manager.
## 5minutemystery-the-secret-in-the-old-trunk
Dennis Boyles is guilty: True or False?
True (0.9105454073245608)
Dennis Boyles is not guilty: True or False?
True (0.9372107968415931)
Dennis Boyles has mean: True or False?
True (0.9417613738325554)
Dennis Boyles has no mean: True or False?
True (0.8987665204865408)
Dennis Boyles has motive: True or False?
True (0.9324532728823121)
Dennis Boyles has no motive: True or False?
True (0.905989824801558)
Dennis Boyles has opportunity: True or False?
True (0.8795611817678315)
Dennis Boyles has no opportunity: True or False?
True (0.7779753136455794)
George Boyles is guilty: True or False?
True (0.9268353022276509)
George Boyles is not guilty: True or False?
True (0.9173026661190045)
George Boyles has mean: True or False?
True (0.9133679254389228)
George Boyles has no mean: True or False?
True (0.8413048399699521)
George Boyles has motive: True or False?
True (0.9329437018480795)
George Boyles has no motive: True or False?
True (0.913058338092082)
George Boyles has opportunity: True or False?
True (0.8272706865691472)
George Boyles has no opportunity: True or False?
True (0.6783269591477166)
John Boyles is guilty: True or False?
True (0.9141375412484458)
John Boyles is not guilty: True or False?
True (0.9319595674053855)
John Boyles has mean: True or False?
True (0.8854334962109398)
John Boyles has no mean: True or False?
True (0.8381505623254643)
John Boyles has motive: True or False?
True (0.8816148581338575)
John Boyles has no motive: True or False?
True (0.8643104392003704)
John Boyles has opportunity: True or False?
True (0.8037905715242155)
John Boyles has no opportunity: True or False?
True (0.6967842494573921)
Patricia (Trish) Boyles Sykes is guilty: True or False?
True (0.8762113474663927)
Patricia (Trish) Boyles Sykes is not guilty: True or False?
True (0.9276260107813639)
Patricia (Trish) Boyles Sykes has mean: True or False?
True (0.9281487460975983)
Patricia (Trish) Boyles Sykes has no mean: True or False?
True (0.8832359917473193)
Patricia (Trish) Boyles Sykes has motive: True or False?
True (0.9079671476237222)
Patricia (Trish) Boyles Sykes has no motive: True or False?
True (0.8647679145346777)
Patricia (Trish) Boyles Sykes has opportunity: True or False?
True (0.9184802773231918)
Patricia (Trish) Boyles Sykes has no opportunity: True or False?
True (0.8360197583769845)
Patrick Boyles is guilty: True or False?
True (0.8787311338092536)
Patrick Boyles is not guilty: True or False?
True (0.8987665204865408)
Patrick Boyles has mean: True or False?
True (0.9003546849431159)
Patrick Boyles has no mean: True or False?
True (0.8031737798924701)
Patrick Boyles has motive: True or False?
True (0.8504686406728537)
Patrick Boyles has no motive: True or False?
True (0.7931059536445917)
Patrick Boyles has opportunity: True or False?
True (0.7981867775042927)
Patrick Boyles has no opportunity: True or False?
True (0.6067314814064781)
### Dennis Boyles
- mean: False (0.10123347951345918)
- motive: False (0.09401017519844201)
- opportunity: False (0.22202468635442063)

### George Boyles
- mean: False (0.1586951600300479)
- motive: False (0.08694166190791797)
- opportunity: False (0.32167304085228343)

### John Boyles
- mean: True (0.8854334962109398)
- motive: True (0.8816148581338575)
- opportunity: True (0.8037905715242155)

### Patricia (Trish) Boyles Sykes
- mean: False (0.11676400825268074)
- motive: False (0.13523208546532228)
- opportunity: False (0.1639802416230155)

### Patrick Boyles
- mean: False (0.19682622010752993)
- motive: False (0.2068940463554083)
- opportunity: False (0.39326851859352185)

The culprit is John Boyles.
In fact, it is Patrick Boyles.
## 5minutemystery-the-restless-ghost
Casey McCormick is guilty: True or False?
True (0.9809125656479328)
Casey McCormick is not guilty: True or False?
True (0.9516839395409852)
Casey McCormick has mean: True or False?
True (0.9196425103002197)
Casey McCormick has no mean: True or False?
True (0.8294920340613177)
Casey McCormick has motive: True or False?
True (0.970070243275667)
Casey McCormick has no motive: True or False?
True (0.861071588244826)

Map:  39%|███▉      | 79/203 [1:51:49<3:03:06, 88.60s/ examples]
Map:  39%|███▉      | 80/203 [1:52:43<2:40:34, 78.33s/ examples]Casey McCormick has opportunity: True or False?
True (0.9418684262191025)
Casey McCormick has no opportunity: True or False?
True (0.7866228249849953)
Connie McCormick is guilty: True or False?
True (0.9676556581517683)
Connie McCormick is not guilty: True or False?
True (0.9669140569738693)
Connie McCormick has mean: True or False?
True (0.7090191831682278)
Connie McCormick has no mean: True or False?
False (0.5097643762740132)
Connie McCormick has motive: True or False?
True (0.9543079730970608)
Connie McCormick has no motive: True or False?
True (0.8933094122075369)
Connie McCormick has opportunity: True or False?
True (0.7779753136455794)
Connie McCormick has no opportunity: True or False?
True (0.6671476389322356)
Ellen McCormick is guilty: True or False?
True (0.9799765346854967)
Ellen McCormick is not guilty: True or False?
True (0.9783846739081675)
Ellen McCormick has mean: True or False?
True (0.866132552869269)
Ellen McCormick has no mean: True or False?
True (0.8006919661398397)
Ellen McCormick has motive: True or False?
True (0.9815244083320255)
Ellen McCormick has no motive: True or False?
True (0.943970619289785)
Ellen McCormick has opportunity: True or False?
True (0.874934615163517)
Ellen McCormick has no opportunity: True or False?
True (0.7416740115009234)
Michael McCormick, Jr. is guilty: True or False?
True (0.971455871280406)
Michael McCormick, Jr. is not guilty: True or False?
True (0.9460011122282159)
Michael McCormick, Jr. has mean: True or False?
True (0.8633915828320894)
Michael McCormick, Jr. has no mean: True or False?
True (0.740174341079517)
Michael McCormick, Jr. has motive: True or False?
True (0.9747251273624444)
Michael McCormick, Jr. has no motive: True or False?
True (0.8770561879413864)
Michael McCormick, Jr. has opportunity: True or False?
True (0.941654207327861)
Michael McCormick, Jr. has no opportunity: True or False?
True (0.7279754274224494)
The ghost of Mike McCormick, Sr. is guilty: True or False?
True (0.9210740952879496)
The ghost of Mike McCormick, Sr. is not guilty: True or False?
True (0.9314624659768579)
The ghost of Mike McCormick, Sr. has mean: True or False?
True (0.8973360043541736)
The ghost of Mike McCormick, Sr. has no mean: True or False?
True (0.8397339530959691)
The ghost of Mike McCormick, Sr. has motive: True or False?
True (0.9237300130783155)
The ghost of Mike McCormick, Sr. has no motive: True or False?
True (0.8278281049441929)
The ghost of Mike McCormick, Sr. has opportunity: True or False?
True (0.884439109617765)
The ghost of Mike McCormick, Sr. has no opportunity: True or False?
True (0.7806625377756776)
### Casey McCormick
- mean: False (0.17050796593868234)
- motive: False (0.138928411755174)
- opportunity: False (0.21337717501500475)

### Connie McCormick
- mean: True (0.7090191831682278)
- motive: True (0.9543079730970608)
- opportunity: True (0.7779753136455794)

### Ellen McCormick
- mean: False (0.19930803386016027)
- motive: False (0.056029380710215015)
- opportunity: False (0.2583259884990766)

### Michael McCormick, Jr.
- mean: False (0.25982565892048304)
- motive: False (0.1229438120586136)
- opportunity: False (0.27202457257755064)

### The ghost of Mike McCormick, Sr.
- mean: False (0.1602660469040309)
- motive: False (0.1721718950558071)
- opportunity: False (0.21933746222432238)

The culprit is Connie McCormick.
In fact, it is Casey McCormick.
## 5minutemystery-the-secret-friend
Bill Baker is guilty: True or False?
True (0.8683809699466569)
Bill Baker is not guilty: True or False?
True (0.8596637847360897)
Bill Baker has mean: True or False?
False (0.5427057221656224)
Bill Baker has no mean: True or False?
False (0.7146280500737092)
Bill Baker has motive: True or False?
True (0.9246876822649571)
Bill Baker has no motive: True or False?
True (0.7779753136455794)
Bill Baker has opportunity: True or False?
True (0.8227594449669557)
Bill Baker has no opportunity: True or False?
True (0.6723316913929156)
Harold Coker is guilty: True or False?
True (0.9362850185952675)
Harold Coker is not guilty: True or False?
True (0.9205042693180057)
Harold Coker has mean: True or False?
False (0.5757329310092021)
Harold Coker has no mean: True or False?
False (0.6057990946577705)
Harold Coker has motive: True or False?
False (1.5442224925625845)
Harold Coker has no motive: True or False?
True (0.8958875533219306)
Harold Coker has opportunity: True or False?
True (0.8438950825214144)
Harold Coker has no opportunity: True or False?
True (0.7233094544266295)
Lyn Baker is guilty: True or False?
True (0.8906751877407573)
Lyn Baker is not guilty: True or False?
True (0.844921525814193)
Lyn Baker has mean: True or False?
True (0.678326898500563)
Lyn Baker has no mean: True or False?
False (0.7287483223557857)
Lyn Baker has motive: True or False?
True (0.8820219652716884)
Lyn Baker has no motive: True or False?
True (0.6288633913849659)
Lyn Baker has opportunity: True or False?
True (0.6160122877297346)
Lyn Baker has no opportunity: True or False?
True (0.5175708506128766)
Midge Coker is guilty: True or False?
True (0.9599126594957205)
Midge Coker is not guilty: True or False?
True (0.9105454073245608)
Midge Coker has mean: True or False?
True (0.8902941942359355)
Midge Coker has no mean: True or False?
False (0.5185461538431656)
Midge Coker has motive: True or False?
True (0.9662834418200392)
Midge Coker has no motive: True or False?
True (0.8300437877296776)
Midge Coker has opportunity: True or False?
True (0.9175984877579624)
Midge Coker has no opportunity: True or False?
True (0.7592253761865491)
### Bill Baker
- mean: False (0.5427057221656224)
- motive: False (0.22202468635442063)
- opportunity: False (0.3276683086070844)

### Harold Coker
- mean: False (0.5757329310092021)
- motive: False (1.5442224925625845)
- opportunity: False (0.27669054557337047)

### Lyn Baker
- mean: True (0.678326898500563)
- motive: True (0.8820219652716884)
- opportunity: True (0.6160122877297346)

### Midge Coker
- mean: True (0.8902941942359355)
- motive: False (0.16995621227032243)
- opportunity: False (0.24077462381345094)

The culprit is Lyn Baker.
In fact, it is Midge Coker.
## 5minutemystery-the-cross-homestead-mystery
Journal entry of Edith is guilty: True or False?
True (0.9841241829125448)
Journal entry of Edith is not guilty: True or False?
True (0.9813821913528206)
Journal entry of Edith has mean: True or False?
True (0.982724071443633)
Journal entry of Edith has no mean: True or False?
True (0.9685006743812633)
Journal entry of Edith has motive: True or False?
True (0.9908566478287073)
Journal entry of Edith has no motive: True or False?
True (0.9824568029810573)
Journal entry of Edith has opportunity: True or False?
True (0.9456006903352807)
Journal entry of Edith has no opportunity: True or False?
True (0.9515039936355008)
Journal entry of Leonard is guilty: True or False?
True (0.9862973096916147)
Journal entry of Leonard is not guilty: True or False?
True (0.9781771902180998)
Journal entry of Leonard has mean: True or False?
True (0.9866748452623849)
Journal entry of Leonard has no mean: True or False?
True (0.9824904804666926)
Journal entry of Leonard has motive: True or False?
True (0.9877822992384565)
Journal entry of Leonard has no motive: True or False?
True (0.9875683784000254)
Journal entry of Leonard has opportunity: True or False?
True (0.9647888536180752)
Journal entry of Leonard has no opportunity: True or False?
True (0.96920782287766)
Journal entry of Susie is guilty: True or False?
True (0.9767580632580227)
Journal entry of Susie is not guilty: True or False?
True (0.9616059669560388)
Journal entry of Susie has mean: True or False?
True (0.9761291751471208)
Journal entry of Susie has no mean: True or False?
True (0.9603611816439128)
Journal entry of Susie has motive: True or False?
True (0.9775857921500122)
Journal entry of Susie has no motive: True or False?
True (0.9599126594957205)
Journal entry of Susie has opportunity: True or False?
True (0.9404625306133385)
Journal entry of Susie has no opportunity: True or False?
True (0.9265699426348812)
Journal entry of Victor is guilty: True or False?
True (0.9805806866861946)

Map:  40%|███▉      | 81/203 [1:54:16<2:48:16, 82.76s/ examples]
Map:  40%|████      | 82/203 [1:55:21<2:35:50, 77.28s/ examples]
Map:  41%|████      | 83/203 [1:56:54<2:44:03, 82.03s/ examples]Journal entry of Victor is not guilty: True or False?
True (0.9670387494740702)
Journal entry of Victor has mean: True or False?
True (0.9787533276905257)
Journal entry of Victor has no mean: True or False?
True (0.966537058600438)
Journal entry of Victor has motive: True or False?
True (0.9799382085917008)
Journal entry of Victor has no motive: True or False?
True (0.9698996547102765)
Journal entry of Victor has opportunity: True or False?
True (0.9531007408873468)
Journal entry of Victor has no opportunity: True or False?
True (0.945399343748748)
Journal entry of Wilbur is guilty: True or False?
True (0.9927742482115516)
Journal entry of Wilbur is not guilty: True or False?
True (0.9860979323093966)
Journal entry of Wilbur has mean: True or False?
True (0.9912717340487711)
Journal entry of Wilbur has no mean: True or False?
True (0.9821169963689194)
Journal entry of Wilbur has motive: True or False?
True (0.988884985036839)
Journal entry of Wilbur has no motive: True or False?
True (0.9777563211328246)
Journal entry of Wilbur has opportunity: True or False?
True (0.9785901910948728)
Journal entry of Wilbur has no opportunity: True or False?
True (0.9689738169140454)
### Journal entry of Edith
- mean: False (0.031499325618736695)
- motive: False (0.01754319701894269)
- opportunity: True (0.9456006903352807)

### Journal entry of Leonard
- mean: True (0.9866748452623849)
- motive: True (0.9877822992384565)
- opportunity: True (0.9647888536180752)

### Journal entry of Susie
- mean: False (0.03963881835608718)
- motive: False (0.040087340504279534)
- opportunity: False (0.07343005736511876)

### Journal entry of Victor
- mean: False (0.03346294139956196)
- motive: False (0.030100345289723496)
- opportunity: False (0.05460065625125199)

### Journal entry of Wilbur
- mean: False (0.01788300363108064)
- motive: False (0.022243678867175376)
- opportunity: False (0.031026183085954617)

The culprit is Journal entry of Leonard.
In fact, it is Journal entry of Leonard.
## 5minutemystery-is-it-a-wonderful-life
Dr. Gilchrest is guilty: True or False?
True (0.7918210572836727)
Dr. Gilchrest is not guilty: True or False?
True (0.8577681165234065)
Dr. Gilchrest has mean: True or False?
True (0.8910549302065384)
Dr. Gilchrest has no mean: True or False?
True (0.8875949368741688)
Dr. Gilchrest has motive: True or False?
True (0.9066531077351827)
Dr. Gilchrest has no motive: True or False?
True (0.9178934131644976)
Dr. Gilchrest has opportunity: True or False?
True (0.9216401608061056)
Dr. Gilchrest has no opportunity: True or False?
True (0.8661325012437474)
Jonathan Cartright is guilty: True or False?
True (0.7683857617837733)
Jonathan Cartright is not guilty: True or False?
True (0.8962513214730718)
Jonathan Cartright has mean: True or False?
True (0.9145963197706802)
Jonathan Cartright has no mean: True or False?
True (0.8984105603938967)
Jonathan Cartright has motive: True or False?
True (0.9142907234091052)
Jonathan Cartright has no motive: True or False?
True (0.9043130884593419)
Jonathan Cartright has opportunity: True or False?
True (0.8529354311342636)
Jonathan Cartright has no opportunity: True or False?
True (0.8727817583545995)
Miser James Cartright (suicide) is guilty: True or False?
True (0.8250265688168699)
Miser James Cartright (suicide) is not guilty: True or False?
True (0.9114953293645017)
Miser James Cartright (suicide) has mean: True or False?
True (0.9326989624184171)
Miser James Cartright (suicide) has no mean: True or False?
True (0.9121235591541035)
Miser James Cartright (suicide) has motive: True or False?
True (0.920789721359066)
Miser James Cartright (suicide) has no motive: True or False?
True (0.8820220178442959)
Miser James Cartright (suicide) has opportunity: True or False?
True (0.832781373043151)
Miser James Cartright (suicide) has no opportunity: True or False?
True (0.72951977676791)
Moira Laurie is guilty: True or False?
True (0.8494723435042196)
Moira Laurie is not guilty: True or False?
True (0.9319596298981465)
Moira Laurie has mean: True or False?
True (0.9360516072812131)
Moira Laurie has no mean: True or False?
True (0.913058338092082)
Moira Laurie has motive: True or False?
True (0.9252299659402181)
Moira Laurie has no motive: True or False?
True (0.9381240005131491)
Moira Laurie has opportunity: True or False?
True (0.9036349079321685)
Moira Laurie has no opportunity: True or False?
True (0.8803863464576128)
### Dr. Gilchrest
- mean: False (0.1124050631258312)
- motive: True (0.9066531077351827)
- opportunity: False (0.1338674987562526)

### Jonathan Cartright
- mean: True (0.9145963197706802)
- motive: True (0.9142907234091052)
- opportunity: True (0.8529354311342636)

### Miser James Cartright (suicide)
- mean: False (0.08787644084589652)
- motive: False (0.1179779821557041)
- opportunity: False (0.27048022323209)

### Moira Laurie
- mean: False (0.08694166190791797)
- motive: True (0.9252299659402181)
- opportunity: False (0.11961365354238718)

The culprit is Jonathan Cartright.
In fact, it is Moira Laurie.
## 5minutemystery-lestrade-solves-a-case
Archibald Hopkins is guilty: True or False?
True (0.9694401626921336)
Archibald Hopkins is not guilty: True or False?
True (0.9808393129553152)
Archibald Hopkins has mean: True or False?
True (0.9187722824991111)
Archibald Hopkins has no mean: True or False?
True (0.9304582506719414)
Archibald Hopkins has motive: True or False?
True (0.9853561522937149)
Archibald Hopkins has no motive: True or False?
True (0.960804880888677)
Archibald Hopkins has opportunity: True or False?
True (0.9516839395409852)
Archibald Hopkins has no opportunity: True or False?
True (0.862930245043327)
Countess Mannerley is guilty: True or False?
True (0.9520419225082909)
Countess Mannerley is not guilty: True or False?
True (0.973544179723875)
Countess Mannerley has mean: True or False?
True (0.9205042693180057)
Countess Mannerley has no mean: True or False?
True (0.9429285510753684)
Countess Mannerley has motive: True or False?
True (0.9772841927877102)
Countess Mannerley has no motive: True or False?
True (0.9304582506719414)
Countess Mannerley has opportunity: True or False?
True (0.958226146208407)
Countess Mannerley has no opportunity: True or False?
True (0.883638264557296)
Loralie Courtney is guilty: True or False?
True (0.9701269272790862)
Loralie Courtney is not guilty: True or False?
True (0.9882901311644948)
Loralie Courtney has mean: True or False?
True (0.9167080509980843)
Loralie Courtney has no mean: True or False?
True (0.941654147692963)
Loralie Courtney has motive: True or False?
True (0.9834386705764392)
Loralie Courtney has no motive: True or False?
True (0.948346199423113)
Loralie Courtney has opportunity: True or False?
True (0.9655115024177445)
Loralie Courtney has no opportunity: True or False?
True (0.8787311338092536)
Robert Bannington is guilty: True or False?
True (0.9690910565174785)
Robert Bannington is not guilty: True or False?
True (0.9655764701970907)
Robert Bannington has mean: True or False?
True (0.8852351930010195)
Robert Bannington has no mean: True or False?
True (0.8665847814067802)
Robert Bannington has motive: True or False?
True (0.9655764090471975)
Robert Bannington has no motive: True or False?
True (0.9133679254389228)
Robert Bannington has opportunity: True or False?
True (0.9249593046682986)
Robert Bannington has no opportunity: True or False?
True (0.8539127714046447)
### Archibald Hopkins
- mean: True (0.9187722824991111)
- motive: True (0.9853561522937149)
- opportunity: True (0.9516839395409852)

### Countess Mannerley
- mean: True (0.9205042693180057)
- motive: False (0.06954174932805857)
- opportunity: False (0.116361735442704)

### Loralie Courtney
- mean: True (0.9167080509980843)
- motive: False (0.051653800576886955)
- opportunity: False (0.1212688661907464)

### Robert Bannington
- mean: False (0.1334152185932198)
- motive: False (0.08663207456107724)
- opportunity: False (0.14608722859535528)

The culprit is Archibald Hopkins.
In fact, it is Robert Bannington.
## 5minutemystery-whole-stole-the-new-years-kiss
Danny is guilty: True or False?
True (0.847967740521315)
Danny is not guilty: True or False?
True (0.8989441381628493)

Map:  41%|████▏     | 84/203 [1:58:02<2:34:39, 77.98s/ examples]
Map:  42%|████▏     | 85/203 [1:59:17<2:31:36, 77.09s/ examples]Danny has mean: True or False?
True (0.7162186593596369)
Danny has no mean: True or False?
True (0.646013666311734)
Danny has motive: True or False?
True (0.9435559526996434)
Danny has no motive: True or False?
True (0.9181873182746905)
Danny has opportunity: True or False?
True (0.9531007408873468)
Danny has no opportunity: True or False?
True (0.920217993899809)
Jeremy is guilty: True or False?
True (0.9527502639818524)
Jeremy is not guilty: True or False?
True (0.9175984877579624)
Jeremy has mean: True or False?
True (0.8902942539348153)
Jeremy has no mean: True or False?
True (0.814643384779728)
Jeremy has motive: True or False?
True (0.9741903536012754)
Jeremy has no motive: True or False?
True (0.8991214023999228)
Jeremy has opportunity: True or False?
True (0.9543079730970608)
Jeremy has no opportunity: True or False?
True (0.8464508054137014)
RJ is guilty: True or False?
True (0.9361683754137716)
RJ is not guilty: True or False?
True (0.9022656660556747)
RJ has mean: True or False?
True (0.9541373270174538)
RJ has no mean: True or False?
True (0.8074606715677252)
RJ has motive: True or False?
True (0.9613890640022783)
RJ has no motive: True or False?
True (0.8068526417769779)
RJ has opportunity: True or False?
True (0.8918110736745599)
RJ has no opportunity: True or False?
True (0.6654105193867614)
Reese is guilty: True or False?
True (0.8854334962109398)
Reese is not guilty: True or False?
True (0.8697145551802641)
Reese has mean: True or False?
True (0.8000678477162699)
Reese has no mean: True or False?
True (0.5592900581575188)
Reese has motive: True or False?
True (0.9753900767342161)
Reese has no motive: True or False?
True (0.9299510095943111)
Reese has opportunity: True or False?
True (0.9633685950557156)
Reese has no opportunity: True or False?
True (0.7732163648437078)
### Danny
- mean: True (0.7162186593596369)
- motive: True (0.9435559526996434)
- opportunity: True (0.9531007408873468)

### Jeremy
- mean: False (0.18535661522027203)
- motive: False (0.10087859760007722)
- opportunity: False (0.15354919458629857)

### RJ
- mean: False (0.19253932843227484)
- motive: False (0.1931473582230221)
- opportunity: False (0.33458948061323857)

### Reese
- mean: False (0.44070994184248125)
- motive: False (0.0700489904056889)
- opportunity: False (0.22678363515629218)

The culprit is Danny.
In fact, it is RJ.
## 5minutemystery-the-new-years-eve-mystery
Juanita Wade is guilty: True or False?
True (0.9751071938949272)
Juanita Wade is not guilty: True or False?
True (0.966537058600438)
Juanita Wade has mean: True or False?
True (0.8732148436000907)
Juanita Wade has no mean: True or False?
True (0.7994423454932595)
Juanita Wade has motive: True or False?
True (0.9730876681996075)
Juanita Wade has no motive: True or False?
True (0.905989824801558)
Juanita Wade has opportunity: True or False?
True (0.9365176577773374)
Juanita Wade has no opportunity: True or False?
True (0.8300437258865985)
Mary Beth Sloan is guilty: True or False?
True (0.9894906286737151)
Mary Beth Sloan is not guilty: True or False?
True (0.9912208913804552)
Mary Beth Sloan has mean: True or False?
True (0.9655764701970907)
Mary Beth Sloan has no mean: True or False?
True (0.9496693599006181)
Mary Beth Sloan has motive: True or False?
True (0.9944666626011286)
Mary Beth Sloan has no motive: True or False?
True (0.9771974085932558)
Mary Beth Sloan has opportunity: True or False?
True (0.9714558133771256)
Mary Beth Sloan has no opportunity: True or False?
True (0.8998277786460391)
Noel King is guilty: True or False?
True (0.990005791112619)
Noel King is not guilty: True or False?
True (0.9900828007789163)
Noel King has mean: True or False?
True (0.9762200121234286)
Noel King has no mean: True or False?
True (0.9502266056050108)
Noel King has motive: True or False?
True (0.9929950235120173)
Noel King has no motive: True or False?
True (0.9871540669880048)
Noel King has opportunity: True or False?
True (0.9851575496109519)
Noel King has no opportunity: True or False?
True (0.9219218506394821)
Roy Wade is guilty: True or False?
True (0.9869543914070512)
Roy Wade is not guilty: True or False?
True (0.9777563211328246)
Roy Wade has mean: True or False?
True (0.6224592927728324)
Roy Wade has no mean: True or False?
True (0.6619228707202935)
Roy Wade has motive: True or False?
True (0.9826908710080852)
Roy Wade has no motive: True or False?
True (0.9317114972308657)
Roy Wade has opportunity: True or False?
True (0.9351099114717211)
Roy Wade has no opportunity: True or False?
True (0.9124361878432953)
Theresa King is guilty: True or False?
True (0.9871788026482293)
Theresa King is not guilty: True or False?
True (0.9836599234493246)
Theresa King has mean: True or False?
True (0.8807970862580315)
Theresa King has no mean: True or False?
True (0.7819973291046377)
Theresa King has motive: True or False?
True (0.9843062166752533)
Theresa King has no motive: True or False?
True (0.950777887812089)
Theresa King has opportunity: True or False?
True (0.950041474283655)
Theresa King has no opportunity: True or False?
True (0.8444089912414552)
### Juanita Wade
- mean: False (0.20055765450674046)
- motive: False (0.09401017519844201)
- opportunity: False (0.16995627411340153)

### Mary Beth Sloan
- mean: False (0.05033064009938193)
- motive: False (0.022802591406744233)
- opportunity: False (0.10017222135396087)

### Noel King
- mean: False (0.04977339439498918)
- motive: False (0.012845933011995214)
- opportunity: False (0.07807814936051793)

### Roy Wade
- mean: True (0.6224592927728324)
- motive: True (0.9826908710080852)
- opportunity: True (0.9351099114717211)

### Theresa King
- mean: False (0.2180026708953623)
- motive: False (0.04922211218791095)
- opportunity: False (0.1555910087585448)

The culprit is Roy Wade.
In fact, it is Mary Beth Sloan.
## 5minutemystery-the-twelfth-night-mystery
Balthasar is guilty: True or False?
True (0.8944211616820568)
Balthasar is not guilty: True or False?
True (0.9084555478510448)
Balthasar has mean: True or False?
True (0.8294919722593475)
Balthasar has no mean: True or False?
True (0.6020615685826383)
Balthasar has motive: True or False?
True (0.9119669214647611)
Balthasar has no motive: True or False?
True (0.745398395394548)
Balthasar has opportunity: True or False?
True (0.7655933544531522)
Balthasar has no opportunity: True or False?
True (0.7272012283179254)
Caspar is guilty: True or False?
True (0.9155072554665495)
Caspar is not guilty: True or False?
True (0.9015745518914653)
Caspar has mean: True or False?
True (0.7697732451157533)
Caspar has no mean: True or False?
True (0.5214711377329961)
Caspar has motive: True or False?
True (0.9605096001181298)
Caspar has no motive: True or False?
True (0.6406358487498992)
Caspar has opportunity: True or False?
True (0.8354835531737983)
Caspar has no opportunity: True or False?
True (0.7799929399351836)
Dad is guilty: True or False?
True (0.920789721359066)
Dad is not guilty: True or False?
True (0.9238675252821831)
Dad has mean: True or False?
True (0.8984105603938967)
Dad has no mean: True or False?
True (0.7950222460539826)
Dad has motive: True or False?
True (0.9623205675054309)
Dad has no motive: True or False?
True (0.7779753136455794)
Dad has opportunity: True or False?
True (0.894973220907352)
Dad has no opportunity: True or False?
True (0.646013666311734)
Melchoir is guilty: True or False?
True (0.9158089188126235)
Melchoir is not guilty: True or False?
True (0.9252299659402181)
Melchoir has mean: True or False?
True (0.9049869164790318)
Melchoir has no mean: True or False?
True (0.7683857617837733)
Melchoir has motive: True or False?
True (0.9635748275768365)
Melchoir has no motive: True or False?
True (0.7879311977554747)
Melchoir has opportunity: True or False?
True (0.9039745373919651)
Melchoir has no opportunity: True or False?
True (0.8006919661398397)
### Balthasar
- mean: True (0.8294919722593475)
- motive: True (0.9119669214647611)
- opportunity: True (0.7655933544531522)

### Caspar
- mean: False (0.47852886226700386)
- motive: False (0.3593641512501008)
- opportunity: False (0.2200070600648164)

### Dad
- mean: False (0.20497775394601736)
- motive: False (0.22202468635442063)
Map:  42%|████▏     | 86/203 [2:00:16<2:19:34, 71.57s/ examples]
Map:  43%|████▎     | 87/203 [2:01:26<2:17:13, 70.98s/ examples]
Map:  43%|████▎     | 88/203 [2:03:04<2:31:49, 79.21s/ examples]
- opportunity: False (0.35398633368826604)

### Melchoir
- mean: False (0.23161423821622673)
- motive: False (0.2120688022445253)
- opportunity: False (0.19930803386016027)

The culprit is Balthasar.
In fact, it is Caspar.
## 5minutemystery-sugar-lands-candy-crook
King Ted is guilty: True or False?
False (0.9425067301242699)
King Ted is not guilty: True or False?
False (0.8848377441095496)
King Ted has mean: True or False?
False (0.8906751877407573)
King Ted has no mean: True or False?
False (0.8727817583545995)
King Ted has motive: True or False?
False (0.9392481417861557)
King Ted has no motive: True or False?
False (0.9230391966311572)
King Ted has opportunity: True or False?
False (0.8086723099497763)
King Ted has no opportunity: True or False?
False (0.867485409735739)
Lancelot is guilty: True or False?
False (0.8606036289596553)
Lancelot is not guilty: True or False?
False (0.814643384779728)
Lancelot has mean: True or False?
False (0.8464508054137014)
Lancelot has no mean: True or False?
False (0.7549149897594328)
Lancelot has motive: True or False?
False (0.789233749534095)
Lancelot has no motive: True or False?
False (0.8683809699466569)
Lancelot has opportunity: True or False?
False (0.6334102859975052)
Lancelot has no opportunity: True or False?
False (0.6627964381792564)
Pride is guilty: True or False?
False (0.8958876133958744)
Pride is not guilty: True or False?
False (0.7146280500737092)
Pride has mean: True or False?
False (0.740174341079517)
Pride has no mean: True or False?
True (0.5165954726976894)
Pride has motive: True or False?
False (0.8283842201397164)
Pride has no motive: True or False?
False (0.91789335161495)
Pride has opportunity: True or False?
False (0.555435228101316)
Pride has no opportunity: True or False?
False (0.7185943809170431)
Rupert is guilty: True or False?
False (0.8803863464576128)
Rupert is not guilty: True or False?
False (0.8267117710471246)
Rupert has mean: True or False?
False (0.8710367026584496)
Rupert has no mean: True or False?
False (0.854884683810039)
Rupert has motive: True or False?
False (0.6723316913929156)
Rupert has no motive: True or False?
False (0.8062431235779619)
Rupert has opportunity: True or False?
True (0.5583270361921496)
Rupert has no opportunity: True or False?
False (0.5765419579552815)
### King Ted
- mean: True (0.12721824164540052)
- motive: True (0.07696080336884281)
- opportunity: True (0.13251459026426105)

### Lancelot
- mean: True (0.24508501024056717)
- motive: False (0.789233749534095)
- opportunity: False (0.6334102859975052)

### Pride
- mean: False (0.740174341079517)
- motive: False (0.8283842201397164)
- opportunity: False (0.555435228101316)

### Rupert
- mean: True (0.14511531618996099)
- motive: False (0.6723316913929156)
- opportunity: True (0.5583270361921496)

The culprit is King Ted.
In fact, it is King Ted.
## 5minutemystery-what-the-dickensa-christmas-eve-mystery
Fagin is guilty: True or False?
False (1.783197962502115)
Fagin is not guilty: True or False?
False (0.8202558565932071)
Fagin has mean: True or False?
True (0.9405717864730483)
Fagin has no mean: True or False?
False (1.2911046513951199)
Fagin has motive: True or False?
False (2.308052201328324)
Fagin has no motive: True or False?
False (2.806709220121151)
Fagin has opportunity: True or False?
False (2.7818942645849876)
Fagin has no opportunity: True or False?
False (2.532615957169248)
Nancy is guilty: True or False?
True (0.9378969089655451)
Nancy is not guilty: True or False?
True (0.9736946827118929)
Nancy has mean: True or False?
True (0.9149009617112335)
Nancy has no mean: True or False?
True (0.8098781635062345)
Nancy has motive: True or False?
True (0.9731387498951102)
Nancy has no motive: True or False?
True (0.9326989068252284)
Nancy has opportunity: True or False?
True (0.9396923783210908)
Nancy has no opportunity: True or False?
True (0.8454326455643386)
Oliver Twist is guilty: True or False?
True (0.9252299659402181)
Oliver Twist is not guilty: True or False?
True (0.9728823298761804)
Oliver Twist has mean: True or False?
True (0.8929365260632085)
Oliver Twist has no mean: True or False?
True (0.8227594449669557)
Oliver Twist has motive: True or False?
True (0.9761291751471208)
Oliver Twist has no motive: True or False?
True (0.8250265073476026)
Oliver Twist has opportunity: True or False?
True (0.9563089618154458)
Oliver Twist has no opportunity: True or False?
True (0.8464508054137014)
The Artful Dodger is guilty: True or False?
True (0.9712384344135814)
The Artful Dodger is not guilty: True or False?
True (0.9847816823480383)
The Artful Dodger has mean: True or False?
True (0.948346255948953)
The Artful Dodger has no mean: True or False?
True (0.7745833916423246)
The Artful Dodger has motive: True or False?
True (0.9866234067972167)
The Artful Dodger has no motive: True or False?
True (0.9122799654606127)
The Artful Dodger has opportunity: True or False?
True (0.9789956218205105)
The Artful Dodger has no opportunity: True or False?
True (0.9475753908928137)
The Rich Gentleman is guilty: True or False?
True (0.94620036983)
The Rich Gentleman is not guilty: True or False?
True (0.9879694584058729)
The Rich Gentleman has mean: True or False?
True (0.9127477403975288)
The Rich Gentleman has no mean: True or False?
True (0.9596108786033737)
The Rich Gentleman has motive: True or False?
True (0.9826576716941837)
The Rich Gentleman has no motive: True or False?
True (0.9410069597342015)
The Rich Gentleman has opportunity: True or False?
True (0.9664105191028597)
The Rich Gentleman has no opportunity: True or False?
True (0.9216402157401415)
### Fagin
- mean: True (0.9405717864730483)
- motive: True (0.0)
- opportunity: True (0.0)

### Nancy
- mean: False (0.19012183649376546)
- motive: False (0.06730109317477162)
- opportunity: False (0.15456735443566139)

### Oliver Twist
- mean: False (0.17724055503304426)
- motive: False (0.17497349265239737)
- opportunity: False (0.15354919458629857)

### The Artful Dodger
- mean: False (0.2254166083576754)
- motive: False (0.08772003453938726)
- opportunity: False (0.05242460910718627)

### The Rich Gentleman
- mean: True (0.9127477403975288)
- motive: False (0.058993040265798546)
- opportunity: False (0.07835978425985846)

The culprit is Fagin.
In fact, it is The Rich Gentleman.
## 5minutemystery-the-secret-santa-mystery
Al Busby is guilty: True or False?
True (0.9407897579933674)
Al Busby is not guilty: True or False?
True (0.9405717864730483)
Al Busby has mean: True or False?
True (0.8858291535164952)
Al Busby has no mean: True or False?
True (0.8563324216110711)
Al Busby has motive: True or False?
True (0.9532750262379774)
Al Busby has no motive: True or False?
True (0.9046505665674094)
Al Busby has opportunity: True or False?
True (0.8774768149941248)
Al Busby has no opportunity: True or False?
True (0.8140527631337082)
Bob (Bobby) Key is guilty: True or False?
True (0.9739932421876873)
Bob (Bobby) Key is not guilty: True or False?
True (0.9660920510558435)
Bob (Bobby) Key has mean: True or False?
True (0.9196425651151865)
Bob (Bobby) Key has no mean: True or False?
True (0.905656637917298)
Bob (Bobby) Key has motive: True or False?
True (0.9635748850103736)
Bob (Bobby) Key has no motive: True or False?
True (0.8918110736745599)
Bob (Bobby) Key has opportunity: True or False?
True (0.9238675252821831)
Bob (Bobby) Key has no opportunity: True or False?
True (0.8402589628813668)
Chuck Daughtry is guilty: True or False?
True (0.9449946880768697)
Chuck Daughtry is not guilty: True or False?
True (0.9265699978627552)
Chuck Daughtry has mean: True or False?
True (0.8316905440184192)
Chuck Daughtry has no mean: True or False?
True (0.7446563751413027)
Chuck Daughtry has motive: True or False?
True (0.943970619289785)
Chuck Daughtry has no motive: True or False?
True (0.8719117627136385)
Chuck Daughtry has opportunity: True or False?
True (0.8643104392003704)
Chuck Daughtry has no opportunity: True or False?
True (0.8397339530959691)
Jeff Reynolds is guilty: True or False?
True (0.9813464881551738)
Jeff Reynolds is not guilty: True or False?
True (0.9832466839924833)
Jeff Reynolds has mean: True or False?
True (0.9775000208126312)

Map:  44%|████▍     | 89/203 [2:04:57<2:49:49, 89.38s/ examples]
Map:  44%|████▍     | 90/203 [2:06:38<2:54:47, 92.81s/ examples]
Map:  45%|████▍     | 91/203 [2:07:53<2:43:30, 87.59s/ examples]Jeff Reynolds has no mean: True or False?
True (0.9445872321654378)
Jeff Reynolds has motive: True or False?
True (0.9934927819342948)
Jeff Reynolds has no motive: True or False?
True (0.9583822499072262)
Jeff Reynolds has opportunity: True or False?
True (0.9705764057188281)
Jeff Reynolds has no opportunity: True or False?
True (0.9121235591541035)
Jim Dockery is guilty: True or False?
True (0.9448931235445592)
Jim Dockery is not guilty: True or False?
True (0.9216402157401415)
Jim Dockery has mean: True or False?
True (0.8454326959560526)
Jim Dockery has no mean: True or False?
True (0.8407825844829613)
Jim Dockery has motive: True or False?
True (0.9639160647221925)
Jim Dockery has no motive: True or False?
True (0.8656789607733094)
Jim Dockery has opportunity: True or False?
True (0.8812065732757132)
Jim Dockery has no opportunity: True or False?
True (0.8031737798924701)
### Al Busby
- mean: True (0.8858291535164952)
- motive: True (0.9532750262379774)
- opportunity: True (0.8774768149941248)

### Bob (Bobby) Key
- mean: False (0.094343362082702)
- motive: False (0.10818892632544008)
- opportunity: False (0.1597410371186332)

### Chuck Daughtry
- mean: False (0.2553436248586973)
- motive: False (0.12808823728636154)
- opportunity: False (0.1602660469040309)

### Jeff Reynolds
- mean: False (0.05541276783456217)
- motive: False (0.0416177500927738)
- opportunity: False (0.08787644084589652)

### Jim Dockery
- mean: False (0.15921741551703872)
- motive: False (0.1343210392266906)
- opportunity: False (0.19682622010752993)

The culprit is Al Busby.
In fact, it is Jim Dockery.
## 5minutemystery-the-silly-santa-mystery
Mr. Corrigan is guilty: True or False?
True (0.6876299924560524)
Mr. Corrigan is not guilty: True or False?
True (0.8864204283224634)
Mr. Corrigan has mean: True or False?
True (0.5660185351323219)
Mr. Corrigan has no mean: True or False?
True (0.6076631662366868)
Mr. Corrigan has motive: True or False?
True (0.9034646765933593)
Mr. Corrigan has no motive: True or False?
True (0.8169911556077801)
Mr. Corrigan has opportunity: True or False?
True (0.7453983509653428)
Mr. Corrigan has no opportunity: True or False?
True (0.5175709123121337)
Mrs. Martin is guilty: True or False?
True (0.8577680653964441)
Mrs. Martin is not guilty: True or False?
True (0.9418684262191025)
Mrs. Martin has mean: True or False?
True (0.7348812840309261)
Mrs. Martin has no mean: True or False?
True (0.8181563060237893)
Mrs. Martin has motive: True or False?
True (0.9414391533604212)
Mrs. Martin has no motive: True or False?
True (0.9124361878432953)
Mrs. Martin has opportunity: True or False?
True (0.821044090050916)
Mrs. Martin has no opportunity: True or False?
True (0.7424217332471881)
Santa Claus is guilty: True or False?
True (0.7882573622725895)
Santa Claus is not guilty: True or False?
True (0.911809984585868)
Santa Claus has mean: True or False?
True (0.6297746298200823)
Santa Claus has no mean: True or False?
True (0.784649255215384)
Santa Claus has motive: True or False?
True (0.8638516611889259)
Santa Claus has no motive: True or False?
True (0.7272012283179254)
Santa Claus has opportunity: True or False?
True (0.7606506998655483)
Santa Claus has no opportunity: True or False?
True (0.6288633913849659)
The photographer is guilty: True or False?
True (0.9020932932190145)
The photographer is not guilty: True or False?
True (0.9351098557348285)
The photographer has mean: True or False?
True (0.7683857617837733)
The photographer has no mean: True or False?
True (0.8487216182798687)
The photographer has motive: True or False?
True (0.91321325132378)
The photographer has no motive: True or False?
True (0.8820219652716884)
The photographer has opportunity: True or False?
True (0.8785228704171453)
The photographer has no opportunity: True or False?
True (0.8037905715242155)
### Mr. Corrigan
- mean: True (0.5660185351323219)
- motive: False (0.18300884439221987)
- opportunity: False (0.4824290876878663)

### Mrs. Martin
- mean: True (0.7348812840309261)
- motive: True (0.9414391533604212)
- opportunity: True (0.821044090050916)

### Santa Claus
- mean: True (0.6297746298200823)
- motive: False (0.27279877168207456)
- opportunity: False (0.37113660861503406)

### The photographer
- mean: True (0.7683857617837733)
- motive: False (0.11797803472831159)
- opportunity: False (0.1962094284757845)

The culprit is Mrs. Martin.
In fact, it is The photographer.
## 5minutemystery-sky-jack
Clem Duster is guilty: True or False?
True (0.9531007408873468)
Clem Duster is not guilty: True or False?
True (0.9554024325650102)
Clem Duster has mean: True or False?
True (0.7577943897558946)
Clem Duster has no mean: True or False?
True (0.811078188867804)
Clem Duster has motive: True or False?
True (0.9808759696772071)
Clem Duster has no motive: True or False?
True (0.9437636147996928)
Clem Duster has opportunity: True or False?
True (0.9205042693180057)
Clem Duster has no opportunity: True or False?
True (0.8464508054137014)
Cliff Snelling is guilty: True or False?
True (0.9235923286659299)
Cliff Snelling is not guilty: True or False?
True (0.9022656660556747)
Cliff Snelling has mean: True or False?
True (0.6706082735718226)
Cliff Snelling has no mean: True or False?
True (0.6893056096647525)
Cliff Snelling has motive: True or False?
True (0.976535319718931)
Cliff Snelling has no motive: True or False?
True (0.9331876642092066)
Cliff Snelling has opportunity: True or False?
True (0.8745065279415651)
Cliff Snelling has no opportunity: True or False?
True (0.7098243920264812)
David Loftkiss is guilty: True or False?
True (0.9383503780077049)
David Loftkiss is not guilty: True or False?
True (0.959912598704516)
David Loftkiss has mean: True or False?
True (0.6817267994905651)
David Loftkiss has no mean: True or False?
True (0.821044090050916)
David Loftkiss has motive: True or False?
True (0.9571978443343412)
David Loftkiss has no motive: True or False?
True (0.8762113474663927)
David Loftkiss has opportunity: True or False?
True (0.8198932995357624)
David Loftkiss has no opportunity: True or False?
True (0.7217432334405754)
Tom Jenks is guilty: True or False?
True (0.9391365661970741)
Tom Jenks is not guilty: True or False?
True (0.9623913759339153)
Tom Jenks has mean: True or False?
True (0.7065954713132195)
Tom Jenks has no mean: True or False?
True (0.7170118721569225)
Tom Jenks has motive: True or False?
True (0.9706321357771589)
Tom Jenks has no motive: True or False?
True (0.9299510719523877)
Tom Jenks has opportunity: True or False?
True (0.842345065078002)
Tom Jenks has no opportunity: True or False?
True (0.6934729802503211)
### Clem Duster
- mean: True (0.7577943897558946)
- motive: True (0.9808759696772071)
- opportunity: True (0.9205042693180057)

### Cliff Snelling
- mean: True (0.6706082735718226)
- motive: False (0.06681233579079338)
- opportunity: False (0.2901756079735188)

### David Loftkiss
- mean: True (0.6817267994905651)
- motive: False (0.12378865253360727)
- opportunity: False (0.27825676655942455)

### Tom Jenks
- mean: True (0.7065954713132195)
- motive: False (0.07004892804761231)
- opportunity: False (0.3065270197496789)

The culprit is Clem Duster.
In fact, it is Tom Jenks.
## 5minutemystery-dr-watson-and-the-thwarted-engagement
Georgette Pelham is guilty: True or False?
True (0.9831822505619944)
Georgette Pelham is not guilty: True or False?
True (0.9731898306467035)
Georgette Pelham has mean: True or False?
True (0.9652503733161137)
Georgette Pelham has no mean: True or False?
True (0.9309620852900756)
Georgette Pelham has motive: True or False?
True (0.9947186709118788)
Georgette Pelham has no motive: True or False?
True (0.9611709710713023)
Georgette Pelham has opportunity: True or False?
True (0.9622497571173928)
Georgette Pelham has no opportunity: True or False?
True (0.8158201638039532)
Reverend Marvin Ingalls is guilty: True or False?
True (0.9771973485275812)
Reverend Marvin Ingalls is not guilty: True or False?
True (0.9686788908454032)
Reverend Marvin Ingalls has mean: True or False?
True (0.9114953293645017)
Reverend Marvin Ingalls has no mean: True or False?
True (0.9317114347547434)

Map:  45%|████▌     | 92/203 [2:09:04<2:32:23, 82.37s/ examples]
Map:  46%|████▌     | 93/203 [2:10:15<2:24:48, 78.98s/ examples]
Map:  46%|████▋     | 94/203 [2:11:28<2:20:32, 77.37s/ examples]Reverend Marvin Ingalls has motive: True or False?
True (0.9944478272754128)
Reverend Marvin Ingalls has no motive: True or False?
True (0.9731388097113137)
Reverend Marvin Ingalls has opportunity: True or False?
True (0.9731388097113137)
Reverend Marvin Ingalls has no opportunity: True or False?
True (0.8494724067948436)
Sheila Ingalls is guilty: True or False?
True (0.9821169963689194)
Sheila Ingalls is not guilty: True or False?
True (0.9837225668505918)
Sheila Ingalls has mean: True or False?
True (0.9529258626138675)
Sheila Ingalls has no mean: True or False?
True (0.9365176577773374)
Sheila Ingalls has motive: True or False?
True (0.9932156800207016)
Sheila Ingalls has no motive: True or False?
True (0.969090998755152)
Sheila Ingalls has opportunity: True or False?
True (0.9698996547102765)
Sheila Ingalls has no opportunity: True or False?
True (0.8354835531737983)
Wallace Anders is guilty: True or False?
True (0.9575961815839735)
Wallace Anders is not guilty: True or False?
True (0.9707432981083896)
Wallace Anders has mean: True or False?
True (0.9498557456415421)
Wallace Anders has no mean: True or False?
True (0.8757870204368676)
Wallace Anders has motive: True or False?
True (0.9943085313118175)
Wallace Anders has no motive: True or False?
True (0.9600626824595854)
Wallace Anders has opportunity: True or False?
True (0.9749646191773192)
Wallace Anders has no opportunity: True or False?
True (0.8697145551802641)
### Georgette Pelham
- mean: False (0.06903791470992438)
- motive: False (0.03882902892869766)
- opportunity: False (0.18417983619604683)

### Reverend Marvin Ingalls
- mean: True (0.9114953293645017)
- motive: True (0.9944478272754128)
- opportunity: True (0.9731388097113137)

### Sheila Ingalls
- mean: False (0.06348234222266258)
- motive: False (0.030909001244847967)
- opportunity: False (0.1645164468262017)

### Wallace Anders
- mean: False (0.12421297956313238)
- motive: False (0.03993731754041463)
- opportunity: False (0.13028544481973592)

The culprit is Reverend Marvin Ingalls.
In fact, it is Wallace Anders.
## 5minutemystery-shoot-out-at-splithead-canyon
Big George Ratcliffe is guilty: True or False?
True (0.9355823382423648)
Big George Ratcliffe is not guilty: True or False?
True (0.943347633443741)
Big George Ratcliffe has mean: True or False?
True (0.8734309071535719)
Big George Ratcliffe has no mean: True or False?
True (0.9196425103002197)
Big George Ratcliffe has motive: True or False?
True (0.9777138240494376)
Big George Ratcliffe has no motive: True or False?
True (0.9190632712053527)
Big George Ratcliffe has opportunity: True or False?
True (0.8582439976623328)
Big George Ratcliffe has no opportunity: True or False?
True (0.7718434926244166)
Chester Morris is guilty: True or False?
True (0.971019387667922)
Chester Morris is not guilty: True or False?
True (0.9732915759758755)
Chester Morris has mean: True or False?
True (0.9071478843057855)
Chester Morris has no mean: True or False?
True (0.8947894610946939)
Chester Morris has motive: True or False?
True (0.9835338590325645)
Chester Morris has no motive: True or False?
True (0.927887794449634)
Chester Morris has opportunity: True or False?
True (0.8978744762836591)
Chester Morris has no opportunity: True or False?
True (0.7988152492192591)
Joe Franklin is guilty: True or False?
True (0.9222025272167219)
Joe Franklin is not guilty: True or False?
True (0.9329437644068318)
Joe Franklin has mean: True or False?
True (0.8551267420488947)
Joe Franklin has no mean: True or False?
True (0.8679338050595715)
Joe Franklin has motive: True or False?
True (0.9696132548883896)
Joe Franklin has no motive: True or False?
True (0.8116760258690822)
Joe Franklin has opportunity: True or False?
True (0.8013146490010521)
Joe Franklin has no opportunity: True or False?
True (0.5813030649269245)
Slim Jameson is guilty: True or False?
True (0.9497626419596781)
Slim Jameson is not guilty: True or False?
True (0.9386884590909785)
Slim Jameson has mean: True or False?
True (0.941654147692963)
Slim Jameson has no mean: True or False?
True (0.9294404371753803)
Slim Jameson has motive: True or False?
True (0.9808393129553152)
Slim Jameson has no motive: True or False?
True (0.8864204283224634)
Slim Jameson has opportunity: True or False?
True (0.8984105603938967)
Slim Jameson has no opportunity: True or False?
True (0.7981867775042927)
### Big George Ratcliffe
- mean: True (0.8734309071535719)
- motive: True (0.9777138240494376)
- opportunity: True (0.8582439976623328)

### Chester Morris
- mean: False (0.10521053890530607)
- motive: False (0.07211220555036602)
- opportunity: False (0.20118475078074094)

### Joe Franklin
- mean: True (0.8551267420488947)
- motive: False (0.18832397413091784)
- opportunity: False (0.4186969350730755)

### Slim Jameson
- mean: False (0.07055956282461973)
- motive: False (0.11357957167753663)
- opportunity: False (0.20181322249570732)

The culprit is Big George Ratcliffe.
In fact, it is Slim Jameson.
## 5minutemystery-the-mystery-of-the-american-raid
Admiral Taro is guilty: True or False?
True (0.9263036859044167)
Admiral Taro is not guilty: True or False?
True (0.8198932995357624)
Admiral Taro has mean: True or False?
True (0.9295683483415352)
Admiral Taro has no mean: True or False?
True (0.8074605993751186)
Admiral Taro has motive: True or False?
True (0.9294404371753803)
Admiral Taro has no motive: True or False?
True (0.5438324636094939)
Admiral Taro has opportunity: True or False?
True (0.7138307731576955)
Admiral Taro has no opportunity: True or False?
True (0.6224592927728324)
Gina is guilty: True or False?
True (0.9580695040202324)
Gina is not guilty: True or False?
True (0.9682614213403071)
Gina has mean: True or False?
True (0.7898827135821628)
Gina has no mean: True or False?
True (0.745398395394548)
Gina has motive: True or False?
True (0.9664104579001461)
Gina has no motive: True or False?
True (0.8454326455643386)
Gina has opportunity: True or False?
True (0.865678909174824)
Gina has no opportunity: True or False?
True (0.5331543669186894)
Kira is guilty: True or False?
True (0.9121235591541035)
Kira is not guilty: True or False?
True (0.9597620950628327)
Kira has mean: True or False?
True (0.8558511090164419)
Kira has no mean: True or False?
True (0.726425644352388)
Kira has motive: True or False?
True (0.9399133323582882)
Kira has no motive: True or False?
True (0.7033457711626864)
Kira has opportunity: True or False?
True (0.8860265005470086)
Kira has no opportunity: True or False?
True (0.6688802232837365)
The Emperor is guilty: True or False?
True (0.9599126594957205)
The Emperor is not guilty: True or False?
True (0.9515039936355008)
The Emperor has mean: True or False?
True (0.905322251510331)
The Emperor has no mean: True or False?
True (0.9700703029032578)
The Emperor has motive: True or False?
True (0.9313377150989219)
The Emperor has no motive: True or False?
True (0.8464508054137014)
The Emperor has opportunity: True or False?
True (0.8976952440346371)
The Emperor has no opportunity: True or False?
True (0.9302051049548884)
### Admiral Taro
- mean: False (0.1925394006248814)
- motive: False (0.4561675363905061)
- opportunity: False (0.3775407072271676)

### Gina
- mean: False (0.254601604605452)
- motive: False (0.15456735443566139)
- opportunity: False (0.46684563308131055)

### Kira
- mean: False (0.273574355647612)
- motive: False (0.2966542288373136)
- opportunity: False (0.33111977671626347)

### The Emperor
- mean: True (0.905322251510331)
- motive: True (0.9313377150989219)
- opportunity: True (0.8976952440346371)

The culprit is The Emperor.
In fact, it is Admiral Taro.
## 5minutemystery-the-missing-ornament-mystery
Jackie Hadley is guilty: True or False?
True (0.983149946614081)
Jackie Hadley is not guilty: True or False?
True (0.9783846739081675)
Jackie Hadley has mean: True or False?
True (0.9403530352223053)
Jackie Hadley has no mean: True or False?
True (0.9136765013387816)
Jackie Hadley has motive: True or False?
True (0.9946045875651337)
Jackie Hadley has no motive: True or False?
True (0.9807288650933316)
Jackie Hadley has opportunity: True or False?
True (0.9704646460964202)

Map:  47%|████▋     | 95/203 [2:12:38<2:15:01, 75.02s/ examples]
Map:  47%|████▋     | 96/203 [2:13:50<2:12:29, 74.30s/ examples]Jackie Hadley has no opportunity: True or False?
True (0.9346342066470359)
Lennie Hadley is guilty: True or False?
True (0.991570711107413)
Lennie Hadley is not guilty: True or False?
True (0.9816655524802333)
Lennie Hadley has mean: True or False?
True (0.9563089012524633)
Lennie Hadley has no mean: True or False?
True (0.9216402157401415)
Lennie Hadley has motive: True or False?
True (0.9967806339468787)
Lennie Hadley has no motive: True or False?
True (0.9868026375175797)
Lennie Hadley has opportunity: True or False?
True (0.9795114404088129)
Lennie Hadley has no opportunity: True or False?
True (0.8727817583545995)
Mike Hadley is guilty: True or False?
True (0.9840936058779184)
Mike Hadley is not guilty: True or False?
True (0.9710743418780032)
Mike Hadley has mean: True or False?
True (0.9238675252821831)
Mike Hadley has no mean: True or False?
True (0.8402589628813668)
Mike Hadley has motive: True or False?
True (0.993499100107697)
Mike Hadley has no motive: True or False?
True (0.9736446146277704)
Mike Hadley has opportunity: True or False?
True (0.9569571625798028)
Mike Hadley has no opportunity: True or False?
True (0.8832359917473193)
Sandy Hadley is guilty: True or False?
True (0.9843664168051008)
Sandy Hadley is not guilty: True or False?
True (0.9744347924514057)
Sandy Hadley has mean: True or False?
True (0.9273632783787477)
Sandy Hadley has no mean: True or False?
True (0.8723474190177988)
Sandy Hadley has motive: True or False?
True (0.9943799375786527)
Sandy Hadley has no motive: True or False?
True (0.9842759969893847)
Sandy Hadley has opportunity: True or False?
True (0.9730365275631271)
Sandy Hadley has no opportunity: True or False?
True (0.9224823751318276)
Tommy Hadley is guilty: True or False?
True (0.9935618639533421)
Tommy Hadley is not guilty: True or False?
True (0.9751071938949272)
Tommy Hadley has mean: True or False?
True (0.9594593035226332)
Tommy Hadley has no mean: True or False?
True (0.8883720049821552)
Tommy Hadley has motive: True or False?
True (0.996332228175721)
Tommy Hadley has no motive: True or False?
True (0.9837225082161594)
Tommy Hadley has opportunity: True or False?
True (0.9815598126769862)
Tommy Hadley has no opportunity: True or False?
True (0.8469578650997759)
### Jackie Hadley
- mean: True (0.9403530352223053)
- motive: True (0.9946045875651337)
- opportunity: True (0.9704646460964202)

### Lennie Hadley
- mean: False (0.07835978425985846)
- motive: False (0.013197362482420316)
- opportunity: False (0.12721824164540052)

### Mike Hadley
- mean: False (0.1597410371186332)
- motive: False (0.02635538537222959)
- opportunity: False (0.11676400825268074)

### Sandy Hadley
- mean: False (0.12765258098220122)
- motive: False (0.015724003010615273)
- opportunity: False (0.07751762486817237)

### Tommy Hadley
- mean: False (0.11162799501784482)
- motive: False (0.016277491783840636)
- opportunity: False (0.1530421349002241)

The culprit is Jackie Hadley.
In fact, it is Lennie Hadley.
## 5minutemystery-the-pilgrim-thanksgiving-puzzle
John Alden is guilty: True or False?
True (0.8914335992201801)
John Alden is not guilty: True or False?
True (0.9273633336539081)
John Alden has mean: True or False?
True (0.7570766705324253)
John Alden has no mean: True or False?
True (0.8433798528114077)
John Alden has motive: True or False?
True (0.8074606715677252)
John Alden has no motive: True or False?
True (0.6740504382339836)
John Alden has opportunity: True or False?
True (0.6800292740030767)
John Alden has no opportunity: True or False?
True (0.6540113633452196)
Miles Standish is guilty: True or False?
True (0.7662936378892937)
Miles Standish is not guilty: True or False?
True (0.8770561879413864)
Miles Standish has mean: True or False?
True (0.7918210572836727)
Miles Standish has no mean: True or False?
True (0.8753613858043711)
Miles Standish has motive: True or False?
True (0.8710367026584496)
Miles Standish has no motive: True or False?
True (0.6992543888266708)
Miles Standish has opportunity: True or False?
True (0.6270381219830087)
Miles Standish has no opportunity: True or False?
True (0.5860491337676195)
Priscilla Mulllins is guilty: True or False?
True (0.9312127242200585)
Priscilla Mulllins is not guilty: True or False?
True (0.9418684262191025)
Priscilla Mulllins has mean: True or False?
True (0.8766343647921183)
Priscilla Mulllins has no mean: True or False?
True (0.8973360043541736)
Priscilla Mulllins has motive: True or False?
True (0.9210740952879496)
Priscilla Mulllins has no motive: True or False?
True (0.8509646659219744)
Priscilla Mulllins has opportunity: True or False?
True (0.7599387683150569)
Priscilla Mulllins has no opportunity: True or False?
True (0.7981867775042927)
William Bradford is guilty: True or False?
True (0.8519528492100928)
William Bradford is not guilty: True or False?
True (0.8891443609199433)
William Bradford has mean: True or False?
True (0.9066531685310133)
William Bradford has no mean: True or False?
True (0.9392480858026054)
William Bradford has motive: True or False?
True (0.8283841584202847)
William Bradford has no motive: True or False?
True (0.7498207054286419)
William Bradford has opportunity: True or False?
True (0.897695304229796)
William Bradford has no opportunity: True or False?
True (0.8261514850267767)
### John Alden
- mean: True (0.7570766705324253)
- motive: False (0.3259495617660164)
- opportunity: False (0.3459886366547804)

### Miles Standish
- mean: True (0.7918210572836727)
- motive: False (0.3007456111733292)
- opportunity: False (0.41395086623238053)

### Priscilla Mulllins
- mean: True (0.8766343647921183)
- motive: True (0.9210740952879496)
- opportunity: True (0.7599387683150569)

### William Bradford
- mean: True (0.9066531685310133)
- motive: False (0.2501792945713581)
- opportunity: False (0.1738485149732233)

The culprit is Priscilla Mulllins.
In fact, it is John Alden.
## 5minutemystery-the-disappearing-turkey
Darby is guilty: True or False?
True (0.9815950994553841)
Darby is not guilty: True or False?
True (0.9829873442201669)
Darby has mean: True or False?
True (0.9489172681310486)
Darby has no mean: True or False?
True (0.875361437979977)
Darby has motive: True or False?
True (0.9928647279268393)
Darby has no motive: True or False?
True (0.9702398769132671)
Darby has opportunity: True or False?
True (0.9630919684645517)
Darby has no opportunity: True or False?
True (0.8267117710471246)
Father is guilty: True or False?
True (0.9828891164753333)
Father is not guilty: True or False?
True (0.9825574747001844)
Father has mean: True or False?
True (0.9054895675798634)
Father has no mean: True or False?
True (0.8300437258865985)
Father has motive: True or False?
True (0.9852146509274663)
Father has no motive: True or False?
True (0.9661560069290531)
Father has opportunity: True or False?
True (0.9260366570445833)
Father has no opportunity: True or False?
True (0.8267117710471246)
Greg is guilty: True or False?
True (0.96716302569886)
Greg is not guilty: True or False?
True (0.9664105191028597)
Greg has mean: True or False?
True (0.897695304229796)
Greg has no mean: True or False?
True (0.8322366416985943)
Greg has motive: True or False?
True (0.9845754507999278)
Greg has no motive: True or False?
True (0.934155284694701)
Greg has opportunity: True or False?
True (0.9494823209990744)
Greg has no opportunity: True or False?
True (0.8489722037469682)
Uncle Larry is guilty: True or False?
True (0.9420819287658885)
Uncle Larry is not guilty: True or False?
True (0.9015745518914653)
Uncle Larry has mean: True or False?
True (0.8879840376027315)
Uncle Larry has no mean: True or False?
True (0.8031737798924701)
Uncle Larry has motive: True or False?
True (0.9871044155030217)
Uncle Larry has no motive: True or False?
True (0.9309620852900756)
Uncle Larry has opportunity: True or False?
True (0.9216402157401415)
Uncle Larry has no opportunity: True or False?
True (0.686790355176806)
### Darby
- mean: False (0.12463856202002299)
- motive: False (0.029760123086732926)
- opportunity: False (0.17328822895287543)

### Father
- mean: True (0.9054895675798634)
- motive: True (0.9852146509274663)
- opportunity: True (0.9260366570445833)

### Greg

Map:  48%|████▊     | 97/203 [2:14:45<2:00:51, 68.41s/ examples]
Map:  48%|████▊     | 98/203 [2:15:45<1:55:25, 65.96s/ examples]
Map:  49%|████▉     | 99/203 [2:16:56<1:56:34, 67.26s/ examples]
Map:  49%|████▉     | 100/203 [2:17:50<1:48:54, 63.44s/ examples]- mean: False (0.16776335830140565)
- motive: False (0.065844715305299)
- opportunity: False (0.15102779625303175)

### Uncle Larry
- mean: False (0.19682622010752993)
- motive: False (0.06903791470992438)
- opportunity: False (0.313209644823194)

The culprit is Father.
In fact, it is Father.
## 5minutemystery-a-thanksgiving-mystery-poem
Libby is guilty: True or False?
True (0.589834510337428)
Libby is not guilty: True or False?
True (0.6233768569026616)
Libby has mean: True or False?
True (1.177830223552625)
Libby has no mean: True or False?
True (2.4422430939372988)
Libby has motive: True or False?
True (1.4299377878015305)
Libby has no motive: True or False?
True (0.625201474135935)
Libby has opportunity: True or False?
True (0.9261395275636995)
Libby has no opportunity: True or False?
True (0.5840490725755711)
Rusty is guilty: True or False?
True (1.8880003495184299)
Rusty is not guilty: True or False?
True (2.0587215387782067)
Rusty has mean: True or False?
True (3.6993957079592654)
Rusty has no mean: True or False?
True (6.661533201562822)
Rusty has motive: True or False?
True (6.251786511526913)
Rusty has no motive: True or False?
True (2.271227890632313)
Rusty has opportunity: True or False?
True (2.3336385978178766)
Rusty has no opportunity: True or False?
True (2.043662405370746)
Tiny is guilty: True or False?
False (0.6645403391983984)
Tiny is not guilty: True or False?
True (0.7158956546088984)
Tiny has mean: True or False?
True (0.7997992557378433)
Tiny has no mean: True or False?
True (1.8841227158555167)
Tiny has motive: True or False?
True (1.7692136510952106)
Tiny has no motive: True or False?
True (0.6960427242035391)
Tiny has opportunity: True or False?
True (0.9304634014996606)
Tiny has no opportunity: True or False?
True (0.6961149782246056)
Tom is guilty: True or False?
True (0.8598587236220697)
Tom is not guilty: True or False?
True (1.5511907609645696)
Tom has mean: True or False?
True (3.6657931659415888)
Tom has no mean: True or False?
True (6.4439719536890765)
Tom has motive: True or False?
True (3.948028698268326)
Tom has no motive: True or False?
True (1.9979756631565808)
Tom has opportunity: True or False?
True (2.2198909046679023)
Tom has no opportunity: True or False?
True (2.260720580256548)
### Libby
- mean: False (0.0)
- motive: False (0.37479852586406504)
- opportunity: False (0.41595092742442885)

### Rusty
- mean: True (3.6993957079592654)
- motive: True (6.251786511526913)
- opportunity: True (2.3336385978178766)

### Tiny
- mean: False (0.0)
- motive: True (1.7692136510952106)
- opportunity: False (0.30388502177539445)

### Tom
- mean: False (0.0)
- motive: True (3.948028698268326)
- opportunity: False (0.0)

The culprit is Rusty.
In fact, it is Rusty.
## 5minutemystery-turkey-cull
Beaker is guilty: True or False?
True (0.981021941474458)
Beaker is not guilty: True or False?
True (0.9618217364339323)
Beaker has mean: True or False?
True (2.745320506080678)
Beaker has no mean: True or False?
True (0.7931059536445917)
Beaker has motive: True or False?
True (0.9798226954348701)
Beaker has no motive: True or False?
True (0.8104789202520752)
Beaker has opportunity: True or False?
True (0.8770561879413864)
Beaker has no opportunity: True or False?
True (0.7634837587244478)
Beau is guilty: True or False?
True (1.0713009788463974)
Beau is not guilty: True or False?
True (0.8994750975198919)
Beau has mean: True or False?
True (3.701607113358059)
Beau has no mean: True or False?
True (0.648688963544537)
Beau has motive: True or False?
True (0.9677167542009312)
Beau has no motive: True or False?
True (0.705785027818136)
Beau has opportunity: True or False?
True (0.7819973291046377)
Beau has no opportunity: True or False?
True (0.6740504382339836)
Leaf is guilty: True or False?
True (0.9616780268435321)
Leaf is not guilty: True or False?
True (0.9433475737015985)
Leaf has mean: True or False?
True (0.8897206197970384)
Leaf has no mean: True or False?
True (0.8832359917473193)
Leaf has motive: True or False?
True (0.9773707989989006)
Leaf has no motive: True or False?
True (0.8423451152856819)
Leaf has opportunity: True or False?
True (0.8951566249612815)
Leaf has no opportunity: True or False?
True (0.811078188867804)
Red is guilty: True or False?
True (0.9418684262191025)
Red is not guilty: True or False?
True (0.9443823686645129)
Red has mean: True or False?
True (1.1395321828655796)
Red has no mean: True or False?
True (0.8697145551802641)
Red has motive: True or False?
True (0.9694401626921336)
Red has no motive: True or False?
True (0.8013146490010521)
Red has opportunity: True or False?
True (0.784649255215384)
Red has no opportunity: True or False?
True (0.7759445334082792)
### Beaker
- mean: True (2.745320506080678)
- motive: False (0.18952107974792476)
- opportunity: False (0.23651624127555215)

### Beau
- mean: True (3.701607113358059)
- motive: False (0.294214972181864)
- opportunity: False (0.3259495617660164)

### Leaf
- mean: False (0.11676400825268074)
- motive: False (0.1576548847143181)
- opportunity: False (0.18892181113219597)

### Red
- mean: True (1.1395321828655796)
- motive: True (0.9694401626921336)
- opportunity: True (0.784649255215384)

The culprit is Red.
In fact, it is Beau.
## 5minutemystery-a-turkey-day-struggle
Aunt Rachel is guilty: True or False?
True (0.9529258022651363)
Aunt Rachel is not guilty: True or False?
True (0.9717254050158363)
Aunt Rachel has mean: True or False?
True (0.9383503780077049)
Aunt Rachel has no mean: True or False?
True (0.9414391533604212)
Aunt Rachel has motive: True or False?
True (0.9833749535726279)
Aunt Rachel has no motive: True or False?
True (0.9152045868398637)
Aunt Rachel has opportunity: True or False?
True (0.9440737974166838)
Aunt Rachel has no opportunity: True or False?
True (0.8652240590801695)
Chris is guilty: True or False?
True (0.9632996920284339)
Chris is not guilty: True or False?
True (0.966726063403815)
Chris has mean: True or False?
True (0.921357630313903)
Chris has no mean: True or False?
True (0.9252299659402181)
Chris has motive: True or False?
True (0.9863631130002726)
Chris has no motive: True or False?
True (0.950041474283655)
Chris has opportunity: True or False?
True (0.9312127242200585)
Chris has no opportunity: True or False?
True (0.8973360043541736)
Diane is guilty: True or False?
True (0.9560634496217031)
Diane is not guilty: True or False?
True (0.9623913759339153)
Diane has mean: True or False?
True (0.7826625131049049)
Diane has no mean: True or False?
True (0.8652240590801695)
Diane has motive: True or False?
True (0.9713473322135262)
Diane has no motive: True or False?
True (0.8444089912414552)
Diane has opportunity: True or False?
True (0.9114953293645017)
Diane has no opportunity: True or False?
True (0.7981867775042927)
Jack the Dog is guilty: True or False?
True (0.9509603994010378)
Jack the Dog is not guilty: True or False?
True (0.9725714317705416)
Jack the Dog has mean: True or False?
True (0.9180403984176693)
Jack the Dog has no mean: True or False?
True (0.9520419225082909)
Jack the Dog has motive: True or False?
True (0.9680507201226971)
Jack the Dog has no motive: True or False?
True (0.9419752346079513)
Jack the Dog has opportunity: True or False?
True (0.9241418261705818)
Jack the Dog has no opportunity: True or False?
True (0.9079671476237222)
### Aunt Rachel
- mean: True (0.9383503780077049)
- motive: False (0.08479541316013628)
- opportunity: False (0.13477594091983047)

### Chris
- mean: True (0.921357630313903)
- motive: False (0.04995852571634496)
- opportunity: False (0.1026639956458264)

### Diane
- mean: True (0.7826625131049049)
- motive: False (0.1555910087585448)
- opportunity: False (0.20181322249570732)

### Jack the Dog
- mean: True (0.9180403984176693)
- motive: True (0.9680507201226971)
- opportunity: True (0.9241418261705818)

The culprit is Jack the Dog.
In fact, it is Chris.
## 5minutemystery-the-missing-briefcase
Porter 1 is guilty: True or False?
True (0.9384632725948482)
Porter 1 is not guilty: True or False?
True (0.9390248079664695)
Porter 1 has mean: True or False?
True (0.8624675215861032)
Porter 1 has no mean: True or False?
True (0.705785027818136)

Map:  50%|████▉     | 101/203 [2:18:45<1:43:33, 60.92s/ examples]
Map:  50%|█████     | 102/203 [2:20:03<1:51:10, 66.04s/ examples]
Map:  51%|█████     | 103/203 [2:21:01<1:46:08, 63.69s/ examples]Porter 1 has motive: True or False?
True (0.9570375696873612)
Porter 1 has no motive: True or False?
True (0.9219218506394821)
Porter 1 has opportunity: True or False?
True (0.8925625120974553)
Porter 1 has no opportunity: True or False?
True (0.847967740521315)
Porter 2 is guilty: True or False?
True (0.942612469657282)
Porter 2 is not guilty: True or False?
True (0.9449946880768697)
Porter 2 has mean: True or False?
True (0.8255897087847518)
Porter 2 has no mean: True or False?
True (0.7379142672364736)
Porter 2 has motive: True or False?
True (0.9676556581517683)
Porter 2 has no motive: True or False?
True (0.9268353022276509)
Porter 2 has opportunity: True or False?
True (0.9447913165152162)
Porter 2 has no opportunity: True or False?
True (0.9139841191734227)
Porter 3 is guilty: True or False?
True (0.955152153792717)
Porter 3 is not guilty: True or False?
True (0.9600626824595854)
Porter 3 has mean: True or False?
True (0.8514594452543962)
Porter 3 has no mean: True or False?
True (0.8519527857346616)
Porter 3 has motive: True or False?
True (0.9841089245217288)
Porter 3 has no motive: True or False?
True (0.9388008138003494)
Porter 3 has opportunity: True or False?
True (0.9661559457424579)
Porter 3 has no opportunity: True or False?
True (0.9164093141890854)
Porter 4 is guilty: True or False?
True (0.9575167905174621)
Porter 4 is not guilty: True or False?
True (0.9669140569738693)
Porter 4 has mean: True or False?
True (0.8832359917473193)
Porter 4 has no mean: True or False?
True (0.8840392847025188)
Porter 4 has motive: True or False?
True (0.9848401551103727)
Porter 4 has no motive: True or False?
True (0.9317114972308657)
Porter 4 has opportunity: True or False?
True (0.948058427656158)
Porter 4 has no opportunity: True or False?
True (0.9260365949489886)
### Porter 1
- mean: False (0.294214972181864)
- motive: False (0.07807814936051793)
- opportunity: False (0.15203225947868504)

### Porter 2
- mean: False (0.2620857327635264)
- motive: False (0.07316469777234913)
- opportunity: False (0.0860158808265773)

### Porter 3
- mean: True (0.8514594452543962)
- motive: False (0.06119918619965059)
- opportunity: False (0.08359068581091456)

### Porter 4
- mean: True (0.8832359917473193)
- motive: True (0.9848401551103727)
- opportunity: True (0.948058427656158)

The culprit is Porter 4.
In fact, it is Porter 3.
## 5minutemystery-everythings-not-just-ducky
Bethany is guilty: True or False?
True (0.9155072008980665)
Bethany is not guilty: True or False?
True (0.9551520363714955)
Bethany has mean: True or False?
True (0.7718434926244166)
Bethany has no mean: True or False?
True (0.6951311179371613)
Bethany has motive: True or False?
True (0.986726105374147)
Bethany has no motive: True or False?
True (0.9205042693180057)
Bethany has opportunity: True or False?
True (0.8423451152856819)
Bethany has no opportunity: True or False?
True (0.7379143332111532)
Connor is guilty: True or False?
True (0.9304582506719414)
Connor is not guilty: True or False?
True (0.969324171790829)
Connor has mean: True or False?
True (0.7937461674149602)
Connor has no mean: True or False?
True (0.7956581141325956)
Connor has motive: True or False?
True (0.9833748931272365)
Connor has no motive: True or False?
True (0.8856314413364714)
Connor has opportunity: True or False?
True (0.8816149238192855)
Connor has no opportunity: True or False?
True (0.8233283740192667)
Emma is guilty: True or False?
True (0.9249593046682986)
Emma is not guilty: True or False?
True (0.9678385865075065)
Emma has mean: True or False?
True (0.7641884666111024)
Emma has no mean: True or False?
True (0.6662796746479285)
Emma has motive: True or False?
True (0.9796676632098326)
Emma has no motive: True or False?
True (0.9029524930853913)
Emma has opportunity: True or False?
True (0.8140527631337082)
Emma has no opportunity: True or False?
True (0.7498206607358464)
Tim is guilty: True or False?
True (0.8494724067948436)
Tim is not guilty: True or False?
True (0.9482504742145513)
Tim has mean: True or False?
True (0.6976088896786037)
Tim has no mean: True or False?
True (0.6909763109505791)
Tim has motive: True or False?
True (0.9764456756172326)
Tim has no motive: True or False?
True (0.9139841191734227)
Tim has opportunity: True or False?
True (0.8074606715677252)
Tim has no opportunity: True or False?
True (0.6680145240815963)
### Bethany
- mean: False (0.3048688820628387)
- motive: False (0.07949573068199434)
- opportunity: False (0.2620856667888468)

### Connor
- mean: True (0.7937461674149602)
- motive: False (0.11436855866352857)
- opportunity: False (0.17667162598073327)

### Emma
- mean: False (0.3337203253520715)
- motive: False (0.09704750691460873)
- opportunity: False (0.2501793392641536)

### Tim
- mean: True (0.6976088896786037)
- motive: True (0.9764456756172326)
- opportunity: True (0.8074606715677252)

The culprit is Tim.
In fact, it is Bethany.
## 5minutemystery-a-darkened-veterans-day
Colonel Abraham is guilty: True or False?
True (0.9729852083817088)
Colonel Abraham is not guilty: True or False?
True (0.9647888536180752)
Colonel Abraham has mean: True or False?
True (0.963368656065788)
Colonel Abraham has no mean: True or False?
True (0.966537058600438)
Colonel Abraham has motive: True or False?
True (0.9927952288368657)
Colonel Abraham has no motive: True or False?
True (0.9736446146277704)
Colonel Abraham has opportunity: True or False?
True (0.9815244083320255)
Colonel Abraham has no opportunity: True or False?
True (0.9475754509027036)
Frank Thompson is guilty: True or False?
True (0.9713473322135262)
Frank Thompson is not guilty: True or False?
True (0.9669139993413022)
Frank Thompson has mean: True or False?
True (0.9546474221708894)
Frank Thompson has no mean: True or False?
True (0.9473810811508532)
Frank Thompson has motive: True or False?
True (0.9873993989626895)
Frank Thompson has no motive: True or False?
True (0.9813106656194062)
Frank Thompson has opportunity: True or False?
True (0.9639160647221925)
Frank Thompson has no opportunity: True or False?
True (0.8987665204865408)
Mr. Landry is guilty: True or False?
True (0.9364014251476122)
Mr. Landry is not guilty: True or False?
True (0.9628131975124238)
Mr. Landry has mean: True or False?
True (0.9273633336539081)
Mr. Landry has no mean: True or False?
True (0.9348725094104268)
Mr. Landry has motive: True or False?
True (0.9780727024492712)
Mr. Landry has no motive: True or False?
True (0.976535319718931)
Mr. Landry has opportunity: True or False?
True (0.9563089618154458)
Mr. Landry has no opportunity: True or False?
True (0.8947894610946939)
Ryan Smith is guilty: True or False?
True (0.9780517227981328)
Ryan Smith is not guilty: True or False?
True (0.9854124786207346)
Ryan Smith has mean: True or False?
True (0.9315870392207104)
Ryan Smith has no mean: True or False?
True (0.9515039936355008)
Ryan Smith has motive: True or False?
True (0.9876400824622509)
Ryan Smith has no motive: True or False?
True (0.9854404929374018)
Ryan Smith has opportunity: True or False?
True (0.9671009774598767)
Ryan Smith has no opportunity: True or False?
True (0.9429285510753684)
### Colonel Abraham
- mean: True (0.963368656065788)
- motive: False (0.02635538537222959)
- opportunity: False (0.052424549097296436)

### Frank Thompson
- mean: False (0.05261891884914682)
- motive: False (0.018689334380593836)
- opportunity: False (0.10123347951345918)

### Mr. Landry
- mean: True (0.9273633336539081)
- motive: False (0.02346468028106896)
- opportunity: False (0.10521053890530607)

### Ryan Smith
- mean: True (0.9315870392207104)
- motive: True (0.9876400824622509)
- opportunity: True (0.9671009774598767)

The culprit is Ryan Smith.
In fact, it is Colonel Abraham.
## 5minutemystery-the-missing-ring
Fingers Ferguson is guilty: True or False?
True (0.9572777759716213)
Fingers Ferguson is not guilty: True or False?
True (0.9783018828855882)
Fingers Ferguson has mean: True or False?
False (0.6816549012710613)
Fingers Ferguson has no mean: True or False?
False (0.2875182617492339)
Fingers Ferguson has motive: True or False?
True (0.9825240364904724)
Fingers Ferguson has no motive: True or False?
True (0.9329437018480795)

Map:  51%|█████     | 104/203 [2:22:06<1:45:20, 63.84s/ examples]
Map:  52%|█████▏    | 105/203 [2:23:42<2:00:08, 73.55s/ examples]Fingers Ferguson has opportunity: True or False?
False (1.0570191495790755)
Fingers Ferguson has no opportunity: True or False?
False (0.4779886748310145)
Joe Morgan is guilty: True or False?
True (0.9226218463113949)
Joe Morgan is not guilty: True or False?
True (0.9546474221708894)
Joe Morgan has mean: True or False?
True (0.811078188867804)
Joe Morgan has no mean: True or False?
True (0.6557770400181139)
Joe Morgan has motive: True or False?
True (0.9603611244019274)
Joe Morgan has no motive: True or False?
True (0.8402589628813668)
Joe Morgan has opportunity: True or False?
True (0.9155072554665495)
Joe Morgan has no opportunity: True or False?
False (0.4174822620336551)
Manuel Garcia is guilty: True or False?
True (0.8679338050595715)
Manuel Garcia is not guilty: True or False?
True (0.9334308488586655)
Manuel Garcia has mean: True or False?
True (0.7185943809170431)
Manuel Garcia has no mean: True or False?
False (0.5631377056275331)
Manuel Garcia has motive: True or False?
True (0.9516838792709049)
Manuel Garcia has no motive: True or False?
True (0.8994750975198919)
Manuel Garcia has opportunity: True or False?
True (0.944176853162527)
Manuel Garcia has no opportunity: True or False?
True (0.6706082735718226)
Mr. Bridges is guilty: True or False?
True (0.9031234959323464)
Mr. Bridges is not guilty: True or False?
True (0.9529258022651363)
Mr. Bridges has mean: True or False?
True (0.700075275973927)
Mr. Bridges has no mean: True or False?
True (0.8392075331266983)
Mr. Bridges has motive: True or False?
True (0.9848546984022976)
Mr. Bridges has no motive: True or False?
True (0.9224823751318276)
Mr. Bridges has opportunity: True or False?
True (0.9219218506394821)
Mr. Bridges has no opportunity: True or False?
True (0.7924642605907138)
### Fingers Ferguson
- mean: True (0.7124817382507661)
- motive: True (0.9825240364904724)
- opportunity: True (0.5220113251689855)

### Joe Morgan
- mean: False (0.3442229599818861)
- motive: False (0.1597410371186332)
- opportunity: True (0.9155072554665495)

### Manuel Garcia
- mean: True (0.7185943809170431)
- motive: False (0.10052490248010815)
- opportunity: False (0.3293917264281774)

### Mr. Bridges
- mean: True (0.700075275973927)
- motive: False (0.07751762486817237)
- opportunity: False (0.20753573940928616)

The culprit is Fingers Ferguson.
In fact, it is Joe Morgan.
## 5minutemystery-brass-keyboard-mystery
April Key #4 is guilty: True or False?
True (0.9689738169140454)
April Key #4 is not guilty: True or False?
True (0.9502265454272235)
April Key #4 has mean: True or False?
True (0.8856315007226893)
April Key #4 has no mean: True or False?
True (0.9566342225308191)
April Key #4 has motive: True or False?
True (0.987829386772097)
April Key #4 has no motive: True or False?
True (0.9534487112250288)
April Key #4 has opportunity: True or False?
True (0.9458012588547495)
April Key #4 has no opportunity: True or False?
True (0.920789721359066)
Denise Key #6 is guilty: True or False?
True (0.9859363436468169)
Denise Key #6 is not guilty: True or False?
True (0.9817357070099405)
Denise Key #6 has mean: True or False?
True (0.9365176577773374)
Denise Key #6 has no mean: True or False?
True (0.976846635229549)
Denise Key #6 has motive: True or False?
True (0.9918279647218875)
Denise Key #6 has no motive: True or False?
True (0.9706877478963396)
Denise Key #6 has opportunity: True or False?
True (0.9649873987772907)
Denise Key #6 has no opportunity: True or False?
True (0.9235923286659299)
Harold Key #1 is guilty: True or False?
True (0.9631612907883619)
Harold Key #1 is not guilty: True or False?
True (0.9672868242254096)
Harold Key #1 has mean: True or False?
True (0.9102267057681164)
Harold Key #1 has no mean: True or False?
True (0.9164093756391206)
Harold Key #1 has motive: True or False?
True (0.9840016367056158)
Harold Key #1 has no motive: True or False?
True (0.9511421913058572)
Harold Key #1 has opportunity: True or False?
True (0.884837803442546)
Harold Key #1 has no opportunity: True or False?
True (0.8787311338092536)
Kirsten Key #5 is guilty: True or False?
True (0.9572777759716213)
Kirsten Key #5 is not guilty: True or False?
True (0.9593070162020048)
Kirsten Key #5 has mean: True or False?
True (0.867485409735739)
Kirsten Key #5 has no mean: True or False?
True (0.9161096235973493)
Kirsten Key #5 has motive: True or False?
True (0.9823893307032775)
Kirsten Key #5 has no motive: True or False?
True (0.9233161821369215)
Kirsten Key #5 has opportunity: True or False?
True (0.9346342066470359)
Kirsten Key #5 has no opportunity: True or False?
True (0.8514594452543962)
Robert (Buddy) Key #3 is guilty: True or False?
True (0.9733929040540585)
Robert (Buddy) Key #3 is not guilty: True or False?
True (0.9711837766333243)
Robert (Buddy) Key #3 has mean: True or False?
True (0.9039745373919651)
Robert (Buddy) Key #3 has no mean: True or False?
True (0.924959242644946)
Robert (Buddy) Key #3 has motive: True or False?
True (0.9855242965202695)
Robert (Buddy) Key #3 has no motive: True or False?
True (0.9365176577773374)
Robert (Buddy) Key #3 has opportunity: True or False?
True (0.9257686153543061)
Robert (Buddy) Key #3 has no opportunity: True or False?
True (0.8587185689177256)
### April Key #4
- mean: True (0.8856315007226893)
- motive: False (0.04655128877497117)
- opportunity: False (0.079210278640934)

### Denise Key #6
- mean: True (0.9365176577773374)
- motive: False (0.029312252103660397)
- opportunity: False (0.07640767133407012)

### Harold Key #1
- mean: True (0.9102267057681164)
- motive: True (0.9840016367056158)
- opportunity: True (0.884837803442546)

### Kirsten Key #5
- mean: True (0.867485409735739)
- motive: False (0.07668381786307854)
- opportunity: False (0.1485405547456038)

### Robert (Buddy) Key #3
- mean: True (0.9039745373919651)
- motive: False (0.06348234222266258)
- opportunity: False (0.14128143108227442)

The culprit is Harold Key #1.
In fact, it is April Key #4.
## 5minutemystery-the-curse-of-the-unlucky-streak
Coach Williams is guilty: True or False?
True (0.8688268116310761)
Coach Williams is not guilty: True or False?
True (0.9127477403975288)
Coach Williams has mean: True or False?
True (0.8751481831208795)
Coach Williams has no mean: True or False?
True (0.7468781552484828)
Coach Williams has motive: True or False?
True (0.9752253881278916)
Coach Williams has no motive: True or False?
True (0.6876299924560524)
Coach Williams has opportunity: True or False?
True (0.8951566249612815)
Coach Williams has no opportunity: True or False?
True (0.5185461538431656)
Joe is guilty: True or False?
True (0.8303191711685114)
Joe is not guilty: True or False?
True (0.9282788655906682)
Joe has mean: True or False?
True (0.918480215734292)
Joe has no mean: True or False?
True (0.8349459127213729)
Joe has motive: True or False?
True (0.9495291710083491)
Joe has no motive: True or False?
True (0.6909762697651828)
Joe has opportunity: True or False?
True (0.9325762415758686)
Joe has no opportunity: True or False?
True (0.6636689235052821)
Mrs. Williams is guilty: True or False?
True (0.7745833916423246)
Mrs. Williams is not guilty: True or False?
True (0.8128672807499561)
Mrs. Williams has mean: True or False?
True (0.7348812840309261)
Mrs. Williams has no mean: True or False?
False (0.5273165068094335)
Mrs. Williams has motive: True or False?
True (0.9486324788710994)
Mrs. Williams has no motive: True or False?
False (0.5755880655791468)
Mrs. Williams has opportunity: True or False?
True (0.8092759828926619)
Mrs. Williams has no opportunity: True or False?
False (0.7170118721569225)
Roderick is guilty: True or False?
True (0.7813305798204846)
Roderick is not guilty: True or False?
True (0.8864204283224634)
Roderick has mean: True or False?
True (0.7394223819718238)
Roderick has no mean: True or False?
False (0.5078118305218892)
Roderick has motive: True or False?
True (0.8969755785184792)
Roderick has no motive: True or False?
False (0.5841525082971981)
Roderick has opportunity: True or False?
True (0.7732163648437078)
Roderick has no opportunity: True or False?
True (0.5370414382302919)
### Coach Williams
- mean: False (0.2531218447515172)

Map:  52%|█████▏    | 106/203 [2:24:55<1:58:37, 73.37s/ examples]
Map:  53%|█████▎    | 107/203 [2:26:47<2:16:05, 85.06s/ examples]
Map:  53%|█████▎    | 108/203 [2:27:49<2:03:31, 78.01s/ examples]- motive: False (0.3123700075439476)
- opportunity: False (0.4814538461568344)

### Joe
- mean: False (0.16505408727862714)
- motive: False (0.3090237302348172)
- opportunity: False (0.33633107649471794)

### Mrs. Williams
- mean: True (0.7348812840309261)
- motive: True (0.9486324788710994)
- opportunity: True (0.8092759828926619)

### Roderick
- mean: True (0.7394223819718238)
- motive: True (0.8969755785184792)
- opportunity: False (0.46295856176970807)

The culprit is Mrs. Williams.
In fact, it is Joe.
## 5minutemystery-halloween-2008
Bride is guilty: True or False?
True (0.8204694405411458)
Bride is not guilty: True or False?
True (0.8050197341926492)
Bride has mean: True or False?
True (0.6619228707202935)
Bride has no mean: True or False?
True (0.6279512069990912)
Bride has motive: True or False?
True (0.7505527059280641)
Bride has no motive: True or False?
True (0.615087855649269)
Bride has opportunity: True or False?
True (0.6279512069990912)
Bride has no opportunity: True or False?
False (0.5204963206682631)
Groom is guilty: True or False?
True (0.9219218506394821)
Groom is not guilty: True or False?
True (0.8770561879413864)
Groom has mean: True or False?
True (0.8524448242555318)
Groom has no mean: True or False?
True (0.7379142672364736)
Groom has motive: True or False?
True (0.7911764307711107)
Groom has no motive: True or False?
True (0.7318258918270596)
Groom has opportunity: True or False?
True (0.8181563669811865)
Groom has no opportunity: True or False?
True (0.7534665957068495)
Indian Chief is guilty: True or False?
True (0.6343168082332088)
Indian Chief is not guilty: True or False?
True (0.6731917300802632)
Indian Chief has mean: True or False?
True (0.6048657973050737)
Indian Chief has no mean: True or False?
False (0.5302364729224919)
Indian Chief has motive: True or False?
True (0.6187804294217345)
Indian Chief has no motive: True or False?
False (0.5195213440667139)
Indian Chief has opportunity: True or False?
True (0.6575384105121485)
Indian Chief has no opportunity: True or False?
False (0.5631377056275331)
Wealthy Woman is guilty: True or False?
True (0.685107355950278)
Wealthy Woman is not guilty: True or False?
True (0.65489470935198)
Wealthy Woman has mean: True or False?
False (0.5360700410935405)
Wealthy Woman has no mean: True or False?
True (0.5341265295318852)
Wealthy Woman has motive: True or False?
True (0.5117165908639297)
Wealthy Woman has no motive: True or False?
False (0.503906199448032)
Wealthy Woman has opportunity: True or False?
True (0.5234203246639862)
Wealthy Woman has no opportunity: True or False?
False (0.5224457875179084)
### Bride
- mean: False (0.37204879300090876)
- motive: False (0.38491214435073096)
- opportunity: True (0.6279512069990912)

### Groom
- mean: False (0.2620857327635264)
- motive: False (0.2681741081729404)
- opportunity: False (0.24653340429315052)

### Indian Chief
- mean: True (0.6048657973050737)
- motive: True (0.6187804294217345)
- opportunity: True (0.6575384105121485)

### Wealthy Woman
- mean: False (0.5360700410935405)
- motive: True (0.5117165908639297)
- opportunity: True (0.5234203246639862)

The culprit is Indian Chief.
In fact, it is Groom.
## 5minutemystery-the-trick-or-treat-mystery
Dorothy is guilty: True or False?
True (0.9615338444102304)
Dorothy is not guilty: True or False?
True (0.9532750830575984)
Dorothy has mean: True or False?
True (0.802555560073231)
Dorothy has no mean: True or False?
True (0.7799928701983835)
Dorothy has motive: True or False?
True (0.9155072554665495)
Dorothy has no motive: True or False?
True (0.7662936378892937)
Dorothy has opportunity: True or False?
True (0.7505527730327083)
Dorothy has no opportunity: True or False?
True (0.8013146490010521)
Superman is guilty: True or False?
True (0.9657060519221431)
Superman is not guilty: True or False?
True (0.9498557456415421)
Superman has mean: True or False?
True (0.934155284694701)
Superman has no mean: True or False?
True (0.9029524325377104)
Superman has motive: True or False?
True (0.9682614213403071)
Superman has no motive: True or False?
True (0.8820219652716884)
Superman has opportunity: True or False?
True (0.9408984770280414)
Superman has no opportunity: True or False?
True (0.8714749214913714)
The Ghost is guilty: True or False?
True (0.9720455997120265)
The Ghost is not guilty: True or False?
True (0.9690910565174785)
The Ghost has mean: True or False?
True (0.7756047866813147)
The Ghost has no mean: True or False?
True (0.9405717864730483)
The Ghost has motive: True or False?
True (0.9556514027264735)
The Ghost has no motive: True or False?
True (0.7956581141325956)
The Ghost has opportunity: True or False?
True (0.9161096235973493)
The Ghost has no opportunity: True or False?
True (0.8933094122075369)
The Lion is guilty: True or False?
True (0.9828890560598048)
The Lion is not guilty: True or False?
True (0.9828891164753333)
The Lion has mean: True or False?
True (0.9235923286659299)
The Lion has no mean: True or False?
True (0.9718325725778448)
The Lion has motive: True or False?
True (0.9664105191028597)
The Lion has no motive: True or False?
True (0.8187367896794966)
The Lion has opportunity: True or False?
True (0.9543079730970608)
The Lion has no opportunity: True or False?
True (0.940680862288251)
The Witch is guilty: True or False?
True (0.9638480560973683)
The Witch is not guilty: True or False?
True (0.9528381231454964)
The Witch has mean: True or False?
True (0.854884683810039)
The Witch has no mean: True or False?
True (0.9263036859044167)
The Witch has motive: True or False?
True (0.9498557456415421)
The Witch has no motive: True or False?
True (0.720171518230031)
The Witch has opportunity: True or False?
True (0.8762112821835625)
The Witch has no opportunity: True or False?
True (0.7994422859301654)
### Dorothy
- mean: True (0.802555560073231)
- motive: True (0.9155072554665495)
- opportunity: True (0.7505527730327083)

### Superman
- mean: False (0.0970475674622896)
- motive: False (0.11797803472831159)
- opportunity: False (0.1285250785086286)

### The Ghost
- mean: True (0.7756047866813147)
- motive: False (0.20434188586740443)
- opportunity: False (0.1066905877924631)

### The Lion
- mean: True (0.9235923286659299)
- motive: False (0.1812632103205034)
- opportunity: False (0.059319137711749015)

### The Witch
- mean: True (0.854884683810039)
- motive: False (0.279828481769969)
- opportunity: False (0.20055771406983458)

The culprit is Dorothy.
In fact, it is The Witch.
## 5minutemystery-house-of-the-rising-pumpkin
Curtis is guilty: True or False?
True (0.9612438076473231)
Curtis is not guilty: True or False?
True (0.9778833990684288)
Curtis has mean: True or False?
True (0.9329437644068318)
Curtis has no mean: True or False?
True (0.8615382357584752)
Curtis has motive: True or False?
True (0.971455871280406)
Curtis has no motive: True or False?
True (0.9213575753967104)
Curtis has opportunity: True or False?
True (0.9360515445140636)
Curtis has no opportunity: True or False?
True (0.8499711693725173)
Dabney is guilty: True or False?
True (0.9726234682815975)
Dabney is not guilty: True or False?
True (0.9790357948221934)
Dabney has mean: True or False?
True (0.9094255544919778)
Dabney has no mean: True or False?
True (0.8169911556077801)
Dabney has motive: True or False?
True (0.9717254050158363)
Dabney has no motive: True or False?
True (0.9294404371753803)
Dabney has opportunity: True or False?
True (0.9193534273597669)
Dabney has no opportunity: True or False?
True (0.8193157928301305)
Kim is guilty: True or False?
True (0.9759005309632979)
Kim is not guilty: True or False?
True (0.9817706947203385)
Kim has mean: True or False?
True (0.8927496657814362)
Kim has no mean: True or False?
True (0.8887587777822111)
Kim has motive: True or False?
True (0.9713473322135262)
Kim has no motive: True or False?
True (0.9063219998220023)
Kim has opportunity: True or False?
True (0.9213575753967104)
Kim has no opportunity: True or False?
True (0.7498207054286419)
Mary is guilty: True or False?
True (0.9549844874375936)
Mary is not guilty: True or False?
True (0.9714558133771256)
Mary has mean: True or False?
True (0.927887794449634)

Map:  54%|█████▎    | 109/203 [2:29:15<2:06:00, 80.43s/ examples]
Map:  54%|█████▍    | 110/203 [2:30:23<1:59:05, 76.84s/ examples]
Map:  55%|█████▍    | 111/203 [2:31:37<1:56:21, 75.88s/ examples]Mary has no mean: True or False?
True (0.8596637206861489)
Mary has motive: True or False?
True (0.9748211501698323)
Mary has no motive: True or False?
True (0.9029524325377104)
Mary has opportunity: True or False?
True (0.8925625719484378)
Mary has no opportunity: True or False?
True (0.7879311977554747)
### Curtis
- mean: True (0.9329437644068318)
- motive: True (0.971455871280406)
- opportunity: True (0.9360515445140636)

### Dabney
- mean: False (0.18300884439221987)
- motive: False (0.07055956282461973)
- opportunity: False (0.18068420716986955)

### Kim
- mean: False (0.11124122221778887)
- motive: False (0.09367800017799766)
- opportunity: False (0.2501792945713581)

### Mary
- mean: False (0.14033627931385106)
- motive: False (0.0970475674622896)
- opportunity: False (0.2120688022445253)

The culprit is Curtis.
In fact, it is Kim.
## 5minutemystery-the-secret-of-the-scarecrows-mask
Charles Kincaid is guilty: True or False?
True (0.9563089012524633)
Charles Kincaid is not guilty: True or False?
True (0.9750122434684597)
Charles Kincaid has mean: True or False?
True (0.9467937951644804)
Charles Kincaid has no mean: True or False?
True (0.9630919110597987)
Charles Kincaid has motive: True or False?
True (0.9874962564918496)
Charles Kincaid has no motive: True or False?
True (0.9771973485275812)
Charles Kincaid has opportunity: True or False?
True (0.9683812262581977)
Charles Kincaid has no opportunity: True or False?
True (0.9548162209309636)
Chester is guilty: True or False?
True (0.9771973485275812)
Chester is not guilty: True or False?
True (0.981700658375371)
Chester has mean: True or False?
True (0.9222025272167219)
Chester has no mean: True or False?
True (0.9046505665674094)
Chester has motive: True or False?
True (0.981202900643061)
Chester has no motive: True or False?
True (0.9591542492415448)
Chester has opportunity: True or False?
True (0.9518632280135741)
Chester has no opportunity: True or False?
True (0.9365176577773374)
Mr. Winfrey is guilty: True or False?
True (0.8987665204865408)
Mr. Winfrey is not guilty: True or False?
True (0.7585106418731645)
Mr. Winfrey has mean: True or False?
True (0.8272706865691472)
Mr. Winfrey has no mean: True or False?
True (0.8134608241927087)
Mr. Winfrey has motive: True or False?
True (0.9139841191734227)
Mr. Winfrey has no motive: True or False?
True (0.85729086409805)
Mr. Winfrey has opportunity: True or False?
True (0.908941745727715)
Mr. Winfrey has no opportunity: True or False?
True (0.8300437258865985)
Mrs. Winfrey is guilty: True or False?
True (0.9447913165152162)
Mrs. Winfrey is not guilty: True or False?
True (0.879146760693242)
Mrs. Winfrey has mean: True or False?
True (0.8705973031072073)
Mrs. Winfrey has no mean: True or False?
True (0.842345065078002)
Mrs. Winfrey has motive: True or False?
True (0.9544780238917078)
Mrs. Winfrey has no motive: True or False?
True (0.9331876642092066)
Mrs. Winfrey has opportunity: True or False?
True (0.9235923286659299)
Mrs. Winfrey has no opportunity: True or False?
True (0.844921525814193)
### Charles Kincaid
- mean: True (0.9467937951644804)
- motive: True (0.9874962564918496)
- opportunity: True (0.9683812262581977)

### Chester
- mean: False (0.09534943343259061)
- motive: False (0.0408457507584552)
- opportunity: False (0.06348234222266258)

### Mr. Winfrey
- mean: False (0.1865391758072913)
- motive: False (0.14270913590195)
- opportunity: False (0.16995627411340153)

### Mrs. Winfrey
- mean: False (0.157654934921998)
- motive: False (0.06681233579079338)
- opportunity: False (0.155078474185807)

The culprit is Charles Kincaid.
In fact, it is Chester.
## 5minutemystery-the-scarecrow-slasher
Annie is guilty: True or False?
True (0.9476723683039264)
Annie is not guilty: True or False?
True (0.959535181008237)
Annie has mean: True or False?
True (0.7240905157396584)
Annie has no mean: True or False?
True (0.6774740084332073)
Annie has motive: True or False?
True (0.9655114412719658)
Annie has no motive: True or False?
True (0.9032942081209032)
Annie has opportunity: True or False?
True (0.854884683810039)
Annie has no opportunity: True or False?
True (0.6943026818003076)
Mr. Forbes is guilty: True or False?
True (0.6297746298200823)
Mr. Forbes is not guilty: True or False?
True (0.8441522053247883)
Mr. Forbes has mean: True or False?
True (0.7714994025200967)
Mr. Forbes has no mean: True or False?
True (0.7233094544266295)
Mr. Forbes has motive: True or False?
True (0.9081302297583123)
Mr. Forbes has no motive: True or False?
True (0.6627964381792564)
Mr. Forbes has opportunity: True or False?
True (0.7602949226623019)
Mr. Forbes has no opportunity: True or False?
False (0.6187805031861143)
Mrs. Avery is guilty: True or False?
True (0.9206471454701205)
Mrs. Avery is not guilty: True or False?
True (0.9334307932218529)
Mrs. Avery has mean: True or False?
True (0.7356416476869558)
Mrs. Avery has no mean: True or False?
True (0.7620701143808404)
Mrs. Avery has motive: True or False?
True (0.9823216197069597)
Mrs. Avery has no motive: True or False?
True (0.9299510095943111)
Mrs. Avery has opportunity: True or False?
True (0.8620035048683017)
Mrs. Avery has no opportunity: True or False?
True (0.6706082136147734)
Philips is guilty: True or False?
True (0.9622497571173928)
Philips is not guilty: True or False?
True (0.9527502639818524)
Philips has mean: True or False?
True (0.7581526119887462)
Philips has no mean: True or False?
True (0.8261514850267767)
Philips has motive: True or False?
True (0.9644556034131689)
Philips has no motive: True or False?
True (0.8984105603938967)
Philips has opportunity: True or False?
True (0.9358173616900589)
Philips has no opportunity: True or False?
True (0.7520125537161032)
### Annie
- mean: False (0.32252599156679274)
- motive: False (0.09670579187909678)
- opportunity: False (0.30569731819969237)

### Mr. Forbes
- mean: False (0.27669054557337047)
- motive: False (0.3372035618207436)
- opportunity: True (0.7602949226623019)

### Mrs. Avery
- mean: True (0.7356416476869558)
- motive: True (0.9823216197069597)
- opportunity: True (0.8620035048683017)

### Philips
- mean: True (0.7581526119887462)
- motive: False (0.10158943960610334)
- opportunity: False (0.2479874462838968)

The culprit is Mrs. Avery.
In fact, it is Philips.
## 5minutemystery-the-golden-ruse
Miss Jones is guilty: True or False?
True (0.7950223052877581)
Miss Jones is not guilty: True or False?
True (0.7745833916423246)
Miss Jones has mean: True or False?
True (0.9046505665674094)
Miss Jones has no mean: True or False?
True (0.5350984235603058)
Miss Jones has motive: True or False?
True (0.911809984585868)
Miss Jones has no motive: True or False?
True (0.6397360437814448)
Miss Jones has opportunity: True or False?
True (0.9127477403975288)
Miss Jones has no opportunity: True or False?
True (0.8311430212356835)
Miss. Pendlebury is guilty: True or False?
True (0.8984105603938967)
Miss. Pendlebury is not guilty: True or False?
True (0.7924642605907138)
Miss. Pendlebury has mean: True or False?
True (0.8074606715677252)
Miss. Pendlebury has no mean: True or False?
True (0.5907791930117218)
Miss. Pendlebury has motive: True or False?
True (0.8824278665848695)
Miss. Pendlebury has no motive: True or False?
True (0.5029296229885981)
Miss. Pendlebury has opportunity: True or False?
True (0.8596637206861489)
Miss. Pendlebury has no opportunity: True or False?
True (0.7541915239138703)
Mr. Horgan is guilty: True or False?
True (0.8193157317863493)
Mr. Horgan is not guilty: True or False?
True (0.7185943809170431)
Mr. Horgan has mean: True or False?
True (0.7718434926244166)
Mr. Horgan has no mean: True or False?
True (0.5370413742099674)
Mr. Horgan has motive: True or False?
True (0.9145963197706802)
Mr. Horgan has no motive: True or False?
True (0.5888891620166576)
Mr. Horgan has opportunity: True or False?
True (0.9249593046682986)
Mr. Horgan has no opportunity: True or False?
True (0.7570766705324253)
Mr. Reese is guilty: True or False?
True (0.8803863464576128)
Mr. Reese is not guilty: True or False?
True (0.7969253675907205)
Mr. Reese has mean: True or False?
True (0.8193157317863493)
Mr. Reese has no mean: True or False?

Map:  55%|█████▌    | 112/203 [2:32:37<1:47:54, 71.14s/ examples]
Map:  56%|█████▌    | 113/203 [2:33:55<1:49:55, 73.28s/ examples]
Map:  56%|█████▌    | 114/203 [2:35:03<1:46:27, 71.77s/ examples]True (0.5273165696704634)
Mr. Reese has motive: True or False?
True (0.9731898306467035)
Mr. Reese has no motive: True or False?
True (0.8311430212356835)
Mr. Reese has opportunity: True or False?
True (0.9142907234091052)
Mr. Reese has no opportunity: True or False?
True (0.7008948290825966)
### Miss Jones
- mean: False (0.4649015764396942)
- motive: False (0.3602639562185552)
- opportunity: False (0.1688569787643165)

### Miss. Pendlebury
- mean: True (0.8074606715677252)
- motive: True (0.8824278665848695)
- opportunity: True (0.8596637206861489)

### Mr. Horgan
- mean: False (0.46295862579003255)
- motive: False (0.41111083798334236)
- opportunity: False (0.24292332946757467)

### Mr. Reese
- mean: False (0.47268343032953664)
- motive: False (0.1688569787643165)
- opportunity: False (0.2991051709174034)

The culprit is Miss. Pendlebury.
In fact, it is Mr. Horgan.
## 5minutemystery-hound-of-the-buskerville
Balloon Twister is guilty: True or False?
True (0.9855382441311838)
Balloon Twister is not guilty: True or False?
True (0.9800339928658331)
Balloon Twister has mean: True or False?
True (0.9177460685312047)
Balloon Twister has no mean: True or False?
True (0.9256343236064929)
Balloon Twister has motive: True or False?
True (0.9781771902180998)
Balloon Twister has no motive: True or False?
True (0.8904848729685282)
Balloon Twister has opportunity: True or False?
True (0.9800721401531428)
Balloon Twister has no opportunity: True or False?
True (0.896794975563401)
Living Statue is guilty: True or False?
True (0.9758545755283039)
Living Statue is not guilty: True or False?
True (0.9698996547102765)
Living Statue has mean: True or False?
True (0.8866168897831055)
Living Statue has no mean: True or False?
True (0.9445872321654378)
Living Statue has motive: True or False?
True (0.962813258487323)
Living Statue has no motive: True or False?
True (0.9005298052062833)
Living Statue has opportunity: True or False?
True (0.9569571625798028)
Living Statue has no opportunity: True or False?
True (0.9155072554665495)
Mime is guilty: True or False?
True (0.9704086183750964)
Mime is not guilty: True or False?
True (0.9649213563025691)
Mime has mean: True or False?
True (0.8255897702959807)
Mime has no mean: True or False?
True (0.8919993657480679)
Mime has motive: True or False?
True (0.9603983181010374)
Mime has no motive: True or False?
True (0.8822251029233062)
Mime has opportunity: True or False?
True (0.9086178579521682)
Mime has no opportunity: True or False?
True (0.8721297391052569)
Stilt-Walker is guilty: True or False?
True (0.9709643714595256)
Stilt-Walker is not guilty: True or False?
True (0.9792749284948266)
Stilt-Walker has mean: True or False?
True (0.9199306971612747)
Stilt-Walker has no mean: True or False?
True (0.9229003224709645)
Stilt-Walker has motive: True or False?
True (0.9603611244019274)
Stilt-Walker has no motive: True or False?
True (0.8910549302065384)
Stilt-Walker has opportunity: True or False?
True (0.948346199423113)
Stilt-Walker has no opportunity: True or False?
True (0.8812066389307215)
### Balloon Twister
- mean: True (0.9177460685312047)
- motive: False (0.10951512703147182)
- opportunity: False (0.10320502443659896)

### Living Statue
- mean: True (0.8866168897831055)
- motive: True (0.962813258487323)
- opportunity: True (0.9569571625798028)

### Mime
- mean: True (0.8255897702959807)
- motive: False (0.11777489707669375)
- opportunity: False (0.12787026089474307)

### Stilt-Walker
- mean: True (0.9199306971612747)
- motive: False (0.10894506979346164)
- opportunity: False (0.11879336106927851)

The culprit is Living Statue.
In fact, it is Stilt-Walker.
## 5minutemystery-moriarty-picks-a-murderer-part-two
Hansom Cab Driver is guilty: True or False?
True (0.905989824801558)
Hansom Cab Driver is not guilty: True or False?
True (0.8732148436000907)
Hansom Cab Driver has mean: True or False?
True (0.5602526707659626)
Hansom Cab Driver has no mean: True or False?
True (0.5087881523495457)
Hansom Cab Driver has motive: True or False?
True (0.7662937064012869)
Hansom Cab Driver has no motive: True or False?
True (0.6020616403539744)
Hansom Cab Driver has opportunity: True or False?
True (0.8244619332958376)
Hansom Cab Driver has no opportunity: True or False?
True (0.6757646168022439)
Policeman is guilty: True or False?
True (0.874934615163517)
Policeman is not guilty: True or False?
True (0.8436376483291435)
Policeman has mean: True or False?
True (0.8016254254291421)
Policeman has no mean: True or False?
True (0.6926419789019715)
Policeman has motive: True or False?
True (0.8587185689177256)
Policeman has no motive: True or False?
True (0.7379143332111532)
Policeman has opportunity: True or False?
True (0.832781310996106)
Policeman has no opportunity: True or False?
True (0.7483522884503825)
Theater Usher is guilty: True or False?
True (0.9032942081209032)
Theater Usher is not guilty: True or False?
True (0.8998277183078867)
Theater Usher has mean: True or False?
True (0.5631377056275331)
Theater Usher has no mean: True or False?
True (0.7049732238008671)
Theater Usher has motive: True or False?
True (0.8128672807499561)
Theater Usher has no motive: True or False?
True (0.7512833387594996)
Theater Usher has opportunity: True or False?
True (0.8958876133958744)
Theater Usher has no opportunity: True or False?
True (0.7826624547920057)
Ticket Seller is guilty: True or False?
True (0.9029524930853913)
Ticket Seller is not guilty: True or False?
True (0.8459424988148251)
Ticket Seller has mean: True or False?
True (0.64063590602721)
Ticket Seller has no mean: True or False?
True (0.6057990946577705)
Ticket Seller has motive: True or False?
True (0.7833262085677729)
Ticket Seller has no motive: True or False?
False (0.5117165908639297)
Ticket Seller has opportunity: True or False?
True (0.7041601500399041)
Ticket Seller has no opportunity: True or False?
True (0.5917232019857303)
### Hansom Cab Driver
- mean: False (0.49121184765045434)
- motive: False (0.39793835964602564)
- opportunity: False (0.32423538319775613)

### Policeman
- mean: False (0.30735802109802846)
- motive: False (0.2620856667888468)
- opportunity: False (0.2516477115496175)

### Theater Usher
- mean: True (0.5631377056275331)
- motive: False (0.2487166612405004)
- opportunity: False (0.2173375452079943)

### Ticket Seller
- mean: True (0.64063590602721)
- motive: True (0.7833262085677729)
- opportunity: True (0.7041601500399041)

The culprit is Ticket Seller.
In fact, it is Theater Usher.
## 5minutemystery-the-scent-of-a-thief
Betty is guilty: True or False?
True (0.9781354072533421)
Betty is not guilty: True or False?
True (0.9818404909998607)
Betty has mean: True or False?
True (0.8514593818157263)
Betty has no mean: True or False?
True (0.8322366416985943)
Betty has motive: True or False?
True (0.9815598126769862)
Betty has no motive: True or False?
True (0.9181872635464632)
Betty has opportunity: True or False?
True (0.9343951361750445)
Betty has no opportunity: True or False?
True (0.8701565822173906)
Darlene is guilty: True or False?
True (0.9724147321673792)
Darlene is not guilty: True or False?
True (0.9815950994553841)
Darlene has mean: True or False?
True (0.8910549899564296)
Darlene has no mean: True or False?
True (0.8349459127213729)
Darlene has motive: True or False?
True (0.9890975956044473)
Darlene has no motive: True or False?
True (0.9447913165152162)
Darlene has opportunity: True or False?
True (0.9604354488383994)
Darlene has no opportunity: True or False?
True (0.847967740521315)
Mr. Danby is guilty: True or False?
True (0.9331876642092066)
Mr. Danby is not guilty: True or False?
True (0.9664105191028597)
Mr. Danby has mean: True or False?
True (0.8431216460935126)
Mr. Danby has no mean: True or False?
True (0.8701565822173906)
Mr. Danby has motive: True or False?
True (0.9834386705764392)
Mr. Danby has no motive: True or False?
True (0.9433475737015985)
Mr. Danby has opportunity: True or False?
True (0.9505947242503305)
Mr. Danby has no opportunity: True or False?
True (0.8255897087847518)
Mr. Harrison is guilty: True or False?
True (0.9617499703158447)
Mr. Harrison is not guilty: True or False?
True (0.979314505527214)

Map:  57%|█████▋    | 115/203 [2:36:01<1:39:05, 67.56s/ examples]
Map:  57%|█████▋    | 116/203 [2:37:13<1:39:50, 68.85s/ examples]
Map:  58%|█████▊    | 117/203 [2:38:31<1:42:41, 71.64s/ examples]Mr. Harrison has mean: True or False?
True (0.9593831890064877)
Mr. Harrison has no mean: True or False?
True (0.9394705907755942)
Mr. Harrison has motive: True or False?
True (0.9946981072726756)
Mr. Harrison has no motive: True or False?
True (0.9764006729648624)
Mr. Harrison has opportunity: True or False?
True (0.9865975971456143)
Mr. Harrison has no opportunity: True or False?
True (0.9511421913058572)
### Betty
- mean: False (0.16776335830140565)
- motive: False (0.08181273645353682)
- opportunity: False (0.12984341778260944)

### Darlene
- mean: False (0.16505408727862714)
- motive: False (0.055208683484783805)
- opportunity: False (0.15203225947868504)

### Mr. Danby
- mean: True (0.8431216460935126)
- motive: False (0.056652426298401504)
- opportunity: False (0.1744102912152482)

### Mr. Harrison
- mean: True (0.9593831890064877)
- motive: True (0.9946981072726756)
- opportunity: True (0.9865975971456143)

The culprit is Mr. Harrison.
In fact, it is Mr. Harrison.
## 5minutemystery-moriarty-picks-a-murderer-part-one
Ed the Bludgeoner is guilty: True or False?
True (0.8679338697256817)
Ed the Bludgeoner is not guilty: True or False?
True (0.9372107968415931)
Ed the Bludgeoner has mean: True or False?
True (0.9019207382785395)
Ed the Bludgeoner has no mean: True or False?
True (0.9092645024391882)
Ed the Bludgeoner has motive: True or False?
True (0.9164093141890854)
Ed the Bludgeoner has no motive: True or False?
True (0.6531269509188588)
Ed the Bludgeoner has opportunity: True or False?
True (0.9431384818142104)
Ed the Bludgeoner has no opportunity: True or False?
True (0.9145963197706802)
Fastidious Fred Fielder is guilty: True or False?
False (3.1005544453257916)
Fastidious Fred Fielder is not guilty: True or False?
False (4.4750675526704695)
Fastidious Fred Fielder has mean: True or False?
False (3.296294936941234)
Fastidious Fred Fielder has no mean: True or False?
False (3.2683597819072783)
Fastidious Fred Fielder has motive: True or False?
False (2.056922424377871)
Fastidious Fred Fielder has no motive: True or False?
False (4.527073428120372)
Fastidious Fred Fielder has opportunity: True or False?
False (3.3718678768950143)
Fastidious Fred Fielder has no opportunity: True or False?
False (10.569927223427012)
Herman Houlihan is guilty: True or False?
True (0.6918097672776748)
Herman Houlihan is not guilty: True or False?
False (0.5589251782457133)
Herman Houlihan has mean: True or False?
True (0.7931059536445917)
Herman Houlihan has no mean: True or False?
True (0.7008947664177184)
Herman Houlihan has motive: True or False?
True (0.7975568155246964)
Herman Houlihan has no motive: True or False?
True (0.6901415551283886)
Herman Houlihan has opportunity: True or False?
False (0.7133364983567047)
Herman Houlihan has no opportunity: True or False?
True (0.7759445334082792)
Morris the Ascot Dandy is guilty: True or False?
True (0.8955226517597132)
Morris the Ascot Dandy is not guilty: True or False?
True (0.9641867858895684)
Morris the Ascot Dandy has mean: True or False?
True (0.9252299659402181)
Morris the Ascot Dandy has no mean: True or False?
True (0.9252299659402181)
Morris the Ascot Dandy has motive: True or False?
True (0.9437636745681832)
Morris the Ascot Dandy has no motive: True or False?
True (0.7732163648437078)
Morris the Ascot Dandy has opportunity: True or False?
True (0.9841546417437246)
Morris the Ascot Dandy has no opportunity: True or False?
True (0.9504109622144332)
### Ed the Bludgeoner
- mean: True (0.9019207382785395)
- motive: False (0.34687304908114125)
- opportunity: False (0.08540368022931977)

### Fastidious Fred Fielder
- mean: True (0.0)
- motive: True (0.0)
- opportunity: True (0.0)

### Herman Houlihan
- mean: False (0.2991052335822816)
- motive: False (0.3098584448716114)
- opportunity: False (0.7133364983567047)

### Morris the Ascot Dandy
- mean: False (0.07477003405978189)
- motive: False (0.22678363515629218)
- opportunity: False (0.04958903778556678)

The culprit is Fastidious Fred Fielder.
In fact, it is Fastidious Fred Fielder.
## 5minutemystery-the-geneva-summit-goldfish-mystery
Ermina Glandon is guilty: True or False?
True (0.9319595674053855)
Ermina Glandon is not guilty: True or False?
True (0.9358173616900589)
Ermina Glandon has mean: True or False?
True (0.9167081124681512)
Ermina Glandon has no mean: True or False?
True (0.8278281049441929)
Ermina Glandon has motive: True or False?
True (0.9690910565174785)
Ermina Glandon has no motive: True or False?
True (0.8705973031072073)
Ermina Glandon has opportunity: True or False?
True (0.8732147785405174)
Ermina Glandon has no opportunity: True or False?
True (0.7295197332851441)
George Adams is guilty: True or False?
True (0.9291837815043049)
George Adams is not guilty: True or False?
True (0.9385759220258869)
George Adams has mean: True or False?
True (0.8624675215861032)
George Adams has no mean: True or False?
True (0.7154240000492645)
George Adams has motive: True or False?
True (0.9760835762008001)
George Adams has no motive: True or False?
True (0.8973360043541736)
George Adams has opportunity: True or False?
True (0.811078188867804)
George Adams has no opportunity: True or False?
True (0.6967842494573921)
Matthew O'Leary is guilty: True or False?
True (0.7563575572780217)
Matthew O'Leary is not guilty: True or False?
True (0.844921525814193)
Matthew O'Leary has mean: True or False?
True (0.8984105603938967)
Matthew O'Leary has no mean: True or False?
True (0.803173839733582)
Matthew O'Leary has motive: True or False?
True (0.9246876822649571)
Matthew O'Leary has no motive: True or False?
True (0.8152325155686644)
Matthew O'Leary has opportunity: True or False?
True (0.84440905415483)
Matthew O'Leary has no opportunity: True or False?
True (0.6504672743423094)
Prince Rahim is guilty: True or False?
True (0.9583821892129424)
Prince Rahim is not guilty: True or False?
True (0.933065775857525)
Prince Rahim has mean: True or False?
True (0.8175744430556572)
Prince Rahim has no mean: True or False?
True (0.866132552869269)
Prince Rahim has motive: True or False?
True (0.9777987599607383)
Prince Rahim has no motive: True or False?
True (0.9465966835599983)
Prince Rahim has opportunity: True or False?
True (0.9219218506394821)
Prince Rahim has no opportunity: True or False?
True (0.7918210572836727)
Ronald Reagan is guilty: True or False?
True (0.8272706865691472)
Ronald Reagan is not guilty: True or False?
True (0.8679338697256817)
Ronald Reagan has mean: True or False?
True (0.5583269696343842)
Ronald Reagan has no mean: True or False?
True (0.6433293282949071)
Ronald Reagan has motive: True or False?
True (0.9432430869704435)
Ronald Reagan has no motive: True or False?
True (0.8587185689177256)
Ronald Reagan has opportunity: True or False?
True (0.8068526417769779)
Ronald Reagan has no opportunity: True or False?
True (0.5669777909748143)
### Ermina Glandon
- mean: False (0.1721718950558071)
- motive: False (0.1294026968927927)
- opportunity: False (0.2704802667148559)

### George Adams
- mean: False (0.28457599995073546)
- motive: False (0.1026639956458264)
- opportunity: False (0.30321575054260785)

### Matthew O'Leary
- mean: False (0.19682616026641797)
- motive: False (0.18476748443133562)
- opportunity: False (0.34953272565769056)

### Prince Rahim
- mean: True (0.8175744430556572)
- motive: True (0.9777987599607383)
- opportunity: True (0.9219218506394821)

### Ronald Reagan
- mean: True (0.5583269696343842)
- motive: False (0.14128143108227442)
- opportunity: False (0.43302220902518573)

The culprit is Prince Rahim.
In fact, it is Ronald Reagan.
## 5minutemystery-a-straw-stuffed-mystery
Bill Albertson is guilty: True or False?
True (0.9843664168051008)
Bill Albertson is not guilty: True or False?
True (0.9745319483890362)
Bill Albertson has mean: True or False?
True (0.8596637847360897)
Bill Albertson has no mean: True or False?
True (0.8762112821835625)
Bill Albertson has motive: True or False?
True (0.9850644470823064)
Bill Albertson has no motive: True or False?
True (0.9399133323582882)
Bill Albertson has opportunity: True or False?
True (0.963230549923961)
Bill Albertson has no opportunity: True or False?

Map:  58%|█████▊    | 118/203 [2:39:29<1:35:39, 67.52s/ examples]
Map:  59%|█████▊    | 119/203 [2:40:54<1:41:41, 72.63s/ examples]
Map:  59%|█████▉    | 120/203 [2:41:53<1:35:02, 68.71s/ examples]True (0.8656789607733094)
Mr. Fletcher is guilty: True or False?
True (0.9386884590909785)
Mr. Fletcher is not guilty: True or False?
True (0.9422946582938823)
Mr. Fletcher has mean: True or False?
True (0.8451772989343147)
Mr. Fletcher has no mean: True or False?
True (0.9410069597342015)
Mr. Fletcher has motive: True or False?
True (0.9869040247745934)
Mr. Fletcher has no motive: True or False?
True (0.9674102673982512)
Mr. Fletcher has opportunity: True or False?
True (0.9527503243194666)
Mr. Fletcher has no opportunity: True or False?
True (0.911809923444246)
Professor Surenie is guilty: True or False?
True (0.9575167905174621)
Professor Surenie is not guilty: True or False?
True (0.9359346026758685)
Professor Surenie has mean: True or False?
True (0.787931139050028)
Professor Surenie has no mean: True or False?
True (0.867485409735739)
Professor Surenie has motive: True or False?
True (0.9730365275631271)
Professor Surenie has no motive: True or False?
True (0.9600626824595854)
Professor Surenie has opportunity: True or False?
True (0.9317114972308657)
Professor Surenie has no opportunity: True or False?
True (0.844921525814193)
Rachel Beaton is guilty: True or False?
True (0.9773275850444884)
Rachel Beaton is not guilty: True or False?
True (0.9605096001181298)
Rachel Beaton has mean: True or False?
True (0.873646672673131)
Rachel Beaton has no mean: True or False?
True (0.8820219652716884)
Rachel Beaton has motive: True or False?
True (0.9856215116934163)
Rachel Beaton has no motive: True or False?
True (0.9543079730970608)
Rachel Beaton has opportunity: True or False?
True (0.9435559526996434)
Rachel Beaton has no opportunity: True or False?
True (0.8233283740192667)
### Bill Albertson
- mean: True (0.8596637847360897)
- motive: False (0.06008666764171178)
- opportunity: False (0.1343210392266906)

### Mr. Fletcher
- mean: True (0.8451772989343147)
- motive: True (0.9869040247745934)
- opportunity: True (0.9527503243194666)

### Professor Surenie
- mean: True (0.787931139050028)
- motive: False (0.03993731754041463)
- opportunity: False (0.155078474185807)

### Rachel Beaton
- mean: True (0.873646672673131)
- motive: False (0.045692026902939165)
- opportunity: False (0.17667162598073327)

The culprit is Mr. Fletcher.
In fact, it is Mr. Fletcher.
## 5minutemystery-ask-marthathe-shoplifter
Jane Croydon is guilty: True or False?
True (0.9855243561799379)
Jane Croydon is not guilty: True or False?
True (0.986726105374147)
Jane Croydon has mean: True or False?
True (0.8438950825214144)
Jane Croydon has no mean: True or False?
True (0.9652503733161137)
Jane Croydon has motive: True or False?
True (0.9832467444299942)
Jane Croydon has no motive: True or False?
True (0.969670771916896)
Jane Croydon has opportunity: True or False?
True (0.9351098557348285)
Jane Croydon has no opportunity: True or False?
True (0.8647679145346777)
Johnny Martin is guilty: True or False?
True (0.9787533276905257)
Johnny Martin is not guilty: True or False?
True (0.9842154375736257)
Johnny Martin has mean: True or False?
True (0.8727816933272936)
Johnny Martin has no mean: True or False?
True (0.9224823751318276)
Johnny Martin has motive: True or False?
True (0.9758085604594696)
Johnny Martin has no motive: True or False?
True (0.9593070162020048)
Johnny Martin has opportunity: True or False?
True (0.9522199623739209)
Johnny Martin has no opportunity: True or False?
True (0.8852351930010195)
Martha Hampden is guilty: True or False?
True (0.9750121835371013)
Martha Hampden is not guilty: True or False?
True (0.9890342350298277)
Martha Hampden has mean: True or False?
True (0.8864204283224634)
Martha Hampden has no mean: True or False?
True (0.9063219998220023)
Martha Hampden has motive: True or False?
True (0.9838781949479747)
Martha Hampden has no motive: True or False?
True (0.9660279734605501)
Martha Hampden has opportunity: True or False?
True (0.9294403817764149)
Martha Hampden has no opportunity: True or False?
True (0.8360197583769845)
Steve Kravitz is guilty: True or False?
True (0.9856353404294369)
Steve Kravitz is not guilty: True or False?
True (0.9741412398478105)
Steve Kravitz has mean: True or False?
True (0.879146760693242)
Steve Kravitz has no mean: True or False?
True (0.9246876822649571)
Steve Kravitz has motive: True or False?
True (0.9680808798281443)
Steve Kravitz has no motive: True or False?
True (0.921357630313903)
Steve Kravitz has opportunity: True or False?
True (0.9392480858026054)
Steve Kravitz has no opportunity: True or False?
True (0.8519527857346616)
### Jane Croydon
- mean: True (0.8438950825214144)
- motive: True (0.9832467444299942)
- opportunity: True (0.9351098557348285)

### Johnny Martin
- mean: True (0.8727816933272936)
- motive: False (0.04069298379799524)
- opportunity: False (0.1147648069989805)

### Martha Hampden
- mean: True (0.8864204283224634)
- motive: False (0.03397202653944986)
- opportunity: False (0.1639802416230155)

### Steve Kravitz
- mean: True (0.879146760693242)
- motive: False (0.07864236968609695)
- opportunity: False (0.1480472142653384)

The culprit is Jane Croydon.
In fact, it is Johnny Martin.
## 5minutemystery-the-hanging-figure
Daisy Morris is guilty: True or False?
True (0.9563089618154458)
Daisy Morris is not guilty: True or False?
True (0.9616059669560388)
Daisy Morris has mean: True or False?
True (0.9322068701708559)
Daisy Morris has no mean: True or False?
True (0.8572908002249056)
Daisy Morris has motive: True or False?
True (0.9543930889248589)
Daisy Morris has no motive: True or False?
True (0.8606036289596553)
Daisy Morris has opportunity: True or False?
True (0.9394705907755942)
Daisy Morris has no opportunity: True or False?
True (0.879146813094474)
Dale Clark is guilty: True or False?
True (0.930078152541638)
Dale Clark is not guilty: True or False?
True (0.9388008138003494)
Dale Clark has mean: True or False?
True (0.847967740521315)
Dale Clark has no mean: True or False?
True (0.7122321792841629)
Dale Clark has motive: True or False?
True (0.9400235399552953)
Dale Clark has no motive: True or False?
True (0.8037905715242155)
Dale Clark has opportunity: True or False?
True (0.8860265599597172)
Dale Clark has no opportunity: True or False?
True (0.8175745039697023)
Iain Potts is guilty: True or False?
True (0.9308364374248909)
Iain Potts is not guilty: True or False?
True (0.9530133616438526)
Iain Potts has mean: True or False?
True (0.8856314413364714)
Iain Potts has no mean: True or False?
True (0.6306849143569856)
Iain Potts has motive: True or False?
True (0.9142907234091052)
Iain Potts has no motive: True or False?
True (0.5983121871760707)
Iain Potts has opportunity: True or False?
True (0.8832359917473193)
Iain Potts has no opportunity: True or False?
True (0.7892336789711022)
Lucy Smith is guilty: True or False?
True (0.9309620852900756)
Lucy Smith is not guilty: True or False?
True (0.9479621664653681)
Lucy Smith has mean: True or False?
True (0.9082930095862076)
Lucy Smith has no mean: True or False?
True (0.844921525814193)
Lucy Smith has motive: True or False?
True (0.9392480858026054)
Lucy Smith has no motive: True or False?
True (0.8193157317863493)
Lucy Smith has opportunity: True or False?
True (0.905322251510331)
Lucy Smith has no opportunity: True or False?
True (0.8799743689174987)
### Daisy Morris
- mean: False (0.14270919977509444)
- motive: False (0.13939637104034475)
- opportunity: False (0.12085318690552604)

### Dale Clark
- mean: False (0.28776782071583706)
- motive: False (0.1962094284757845)
- opportunity: False (0.18242549603029767)

### Iain Potts
- mean: False (0.3693150856430144)
- motive: False (0.4016878128239293)
- opportunity: False (0.2107663210288978)

### Lucy Smith
- mean: True (0.9082930095862076)
- motive: True (0.9392480858026054)
- opportunity: True (0.905322251510331)

The culprit is Lucy Smith.
In fact, it is Dale Clark.
## 5minutemystery-our-quarterback-is-missing
Coach Roster is guilty: True or False?
True (0.9637117373129486)
Coach Roster is not guilty: True or False?
True (0.9741412398478105)
Coach Roster has mean: True or False?
True (0.925094725346746)
Coach Roster has no mean: True or False?
True (0.9114953293645017)

Map:  60%|█████▉    | 121/203 [2:43:06<1:35:30, 69.89s/ examples]
Map:  60%|██████    | 122/203 [2:44:07<1:30:54, 67.35s/ examples]
Map:  61%|██████    | 123/203 [2:45:10<1:28:00, 66.00s/ examples]Coach Roster has motive: True or False?
True (0.9738443491650812)
Coach Roster has no motive: True or False?
True (0.9641867858895684)
Coach Roster has opportunity: True or False?
True (0.9386884590909785)
Coach Roster has no opportunity: True or False?
True (0.7866228835929651)
Eddie is guilty: True or False?
True (0.9408984770280414)
Eddie is not guilty: True or False?
True (0.966726063403815)
Eddie has mean: True or False?
True (0.9097467681279717)
Eddie has no mean: True or False?
True (0.8925625120974553)
Eddie has motive: True or False?
True (0.9561454058699453)
Eddie has no motive: True or False?
True (0.9241417642020455)
Eddie has opportunity: True or False?
True (0.8688267468984366)
Eddie has no opportunity: True or False?
True (0.6901415551283886)
Eddie's Mom is guilty: True or False?
True (0.9456006304504523)
Eddie's Mom is not guilty: True or False?
True (0.9593070733811604)
Eddie's Mom has mean: True or False?
True (0.9114953293645017)
Eddie's Mom has no mean: True or False?
True (0.8474634858439474)
Eddie's Mom has motive: True or False?
True (0.9673486357359453)
Eddie's Mom has no motive: True or False?
True (0.9073122726900733)
Eddie's Mom has opportunity: True or False?
True (0.9053223122169206)
Eddie's Mom has no opportunity: True or False?
True (0.7732163648437078)
Marissa is guilty: True or False?
True (0.9747251273624444)
Marissa is not guilty: True or False?
True (0.9841546417437246)
Marissa has mean: True or False?
True (0.9069831945855868)
Marissa has no mean: True or False?
True (0.9257686153543061)
Marissa has motive: True or False?
True (0.982724130018554)
Marissa has no motive: True or False?
True (0.9532750262379774)
Marissa has opportunity: True or False?
True (0.9399133918829404)
Marissa has no opportunity: True or False?
True (0.7541915688671895)
### Coach Roster
- mean: True (0.925094725346746)
- motive: True (0.9738443491650812)
- opportunity: True (0.9386884590909785)

### Eddie
- mean: False (0.1074374879025447)
- motive: False (0.07585823579795448)
- opportunity: False (0.3098584448716114)

### Eddie's Mom
- mean: False (0.15253651415605263)
- motive: False (0.09268772730992669)
- opportunity: False (0.22678363515629218)

### Marissa
- mean: True (0.9069831945855868)
- motive: False (0.04672497376202256)
- opportunity: False (0.24580843113281048)

The culprit is Coach Roster.
In fact, it is Eddie's Mom.
## 5minutemystery-ask-marthathe-case-of-the-missing-canary
Alex Johnston is guilty: True or False?
True (0.9227612010756272)
Alex Johnston is not guilty: True or False?
True (0.9494823209990744)
Alex Johnston has mean: True or False?
True (0.8852351930010195)
Alex Johnston has no mean: True or False?
True (0.9219218506394821)
Alex Johnston has motive: True or False?
True (0.9756698013402983)
Alex Johnston has no motive: True or False?
True (0.9427180278987515)
Alex Johnston has opportunity: True or False?
True (0.918480215734292)
Alex Johnston has no opportunity: True or False?
True (0.8438951328214825)
Jimmy Carstairs is guilty: True or False?
True (0.9194980842090085)
Jimmy Carstairs is not guilty: True or False?
True (0.9462997305871003)
Jimmy Carstairs has mean: True or False?
True (0.8526903338256402)
Jimmy Carstairs has no mean: True or False?
True (0.8193157928301305)
Jimmy Carstairs has motive: True or False?
True (0.9528381231454964)
Jimmy Carstairs has no motive: True or False?
True (0.884837803442546)
Jimmy Carstairs has opportunity: True or False?
True (0.9286679635448885)
Jimmy Carstairs has no opportunity: True or False?
True (0.7898827135821628)
Lydia Carstairs is guilty: True or False?
True (0.968441008005572)
Lydia Carstairs is not guilty: True or False?
True (0.972362279388711)
Lydia Carstairs has mean: True or False?
True (0.9073122118500465)
Lydia Carstairs has no mean: True or False?
True (0.9474783528129732)
Lydia Carstairs has motive: True or False?
True (0.9803562168273844)
Lydia Carstairs has no motive: True or False?
True (0.9376689222692878)
Lydia Carstairs has opportunity: True or False?
True (0.9322068701708559)
Lydia Carstairs has no opportunity: True or False?
True (0.8529354946829077)
Sarabelle is guilty: True or False?
True (0.9467937951644804)
Sarabelle is not guilty: True or False?
True (0.9610980147014194)
Sarabelle has mean: True or False?
True (0.873646672673131)
Sarabelle has no mean: True or False?
True (0.8679338050595715)
Sarabelle has motive: True or False?
True (0.9563904403130185)
Sarabelle has no motive: True or False?
True (0.8770562402180104)
Sarabelle has opportunity: True or False?
True (0.8539127714046447)
Sarabelle has no opportunity: True or False?
True (0.72951977676791)
### Alex Johnston
- mean: True (0.8852351930010195)
- motive: True (0.9756698013402983)
- opportunity: True (0.918480215734292)

### Jimmy Carstairs
- mean: False (0.18068420716986955)
- motive: False (0.11516219655745397)
- opportunity: False (0.21011728641783722)

### Lydia Carstairs
- mean: True (0.9073122118500465)
- motive: False (0.062331077730712225)
- opportunity: False (0.14706450531709225)

### Sarabelle
- mean: False (0.13206619494042848)
- motive: False (0.12294375978198957)
- opportunity: False (0.27048022323209)

The culprit is Alex Johnston.
In fact, it is Alex Johnston.
## 5minutemystery-register-robbery
Dan is guilty: True or False?
True (0.8590535670268302)
Dan is not guilty: True or False?
True (0.8751481831208795)
Dan has mean: True or False?
True (0.7676898810056793)
Dan has no mean: True or False?
True (0.8181563669811865)
Dan has motive: True or False?
True (0.9399133918829404)
Dan has no motive: True or False?
True (0.9039744767757508)
Dan has opportunity: True or False?
True (0.84440905415483)
Dan has no opportunity: True or False?
True (0.8244618718686391)
David is guilty: True or False?
True (0.8885655424665229)
David is not guilty: True or False?
True (0.8665847814067802)
David has mean: True or False?
True (0.7209580648179327)
David has no mean: True or False?
True (0.8152325155686644)
David has motive: True or False?
True (0.9324532728823121)
David has no motive: True or False?
True (0.8643104392003704)
David has opportunity: True or False?
True (0.8360197583769845)
David has no opportunity: True or False?
True (0.7918210572836727)
Robert is guilty: True or False?
True (0.8923750519147751)
Robert is not guilty: True or False?
True (0.8957052808276003)
Robert has mean: True or False?
True (0.5907791930117218)
Robert has no mean: True or False?
True (0.7505527730327083)
Robert has motive: True or False?
True (0.8914335992201801)
Robert has no motive: True or False?
True (0.8338664756137771)
Robert has opportunity: True or False?
True (0.7379143332111532)
Robert has no opportunity: True or False?
True (0.6909763109505791)
Teresa is guilty: True or False?
True (1.1983431006124314)
Teresa is not guilty: True or False?
True (0.8705973031072073)
Teresa has mean: True or False?
True (0.6011253583932805)
Teresa has no mean: True or False?
True (0.6817267588564826)
Teresa has motive: True or False?
True (1.5779629867344473)
Teresa has no motive: True or False?
True (0.8204694405411458)
Teresa has opportunity: True or False?
True (0.7248703250005105)
Teresa has no opportunity: True or False?
True (0.7648916137833577)
### Dan
- mean: True (0.7676898810056793)
- motive: False (0.09602552322424918)
- opportunity: False (0.17553812813136094)

### David
- mean: True (0.7209580648179327)
- motive: False (0.13568956079962957)
- opportunity: False (0.2081789427163273)

### Robert
- mean: True (0.5907791930117218)
- motive: False (0.16613352438622286)
- opportunity: False (0.3090236890494209)

### Teresa
- mean: True (0.6011253583932805)
- motive: True (1.5779629867344473)
- opportunity: True (0.7248703250005105)

The culprit is Teresa.
In fact, it is David.
## 5minutemystery-mr-patrick-back-in-class
CSA currency is guilty: True or False?
True (0.9434518224682585)
CSA currency is not guilty: True or False?
True (0.9234543414029781)
CSA currency has mean: True or False?
True (0.6671476985798853)
CSA currency has no mean: True or False?
True (0.6627964974378784)
CSA currency has motive: True or False?
True (0.9390248079664695)
CSA currency has no motive: True or False?

Map:  61%|██████    | 124/203 [2:46:57<1:42:56, 78.19s/ examples]
Map:  62%|██████▏   | 125/203 [2:49:08<2:02:23, 94.15s/ examples]True (0.8994750975198919)
CSA currency has opportunity: True or False?
True (0.920217993899809)
CSA currency has no opportunity: True or False?
True (0.8386797310322072)
Diamond necklace is guilty: True or False?
True (0.9886243938205078)
Diamond necklace is not guilty: True or False?
True (0.9876162412358204)
Diamond necklace has mean: True or False?
True (0.9860979323093966)
Diamond necklace has no mean: True or False?
True (0.9927180410162981)
Diamond necklace has motive: True or False?
True (0.9869166012557465)
Diamond necklace has no motive: True or False?
True (0.9858140345117591)
Diamond necklace has opportunity: True or False?
True (0.9815950994553841)
Diamond necklace has no opportunity: True or False?
True (0.9822536700421047)
Gold money clip is guilty: True or False?
True (0.9763782033334516)
Gold money clip is not guilty: True or False?
True (0.962708175773424)
Gold money clip has mean: True or False?
True (0.9375547191885567)
Gold money clip has no mean: True or False?
True (0.9694979782498893)
Gold money clip has motive: True or False?
True (0.9745561472167436)
Gold money clip has no motive: True or False?
True (0.962813258487323)
Gold money clip has opportunity: True or False?
True (0.9605836282984641)
Gold money clip has no opportunity: True or False?
True (0.9212159548464016)
Jewel encrusted pistol is guilty: True or False?
True (0.9918516877713647)
Jewel encrusted pistol is not guilty: True or False?
True (0.9838781363042661)
Jewel encrusted pistol has mean: True or False?
True (0.9716178782667568)
Jewel encrusted pistol has no mean: True or False?
True (0.9858276244824502)
Jewel encrusted pistol has motive: True or False?
True (0.9870919588955418)
Jewel encrusted pistol has no motive: True or False?
True (0.9743372796010542)
Jewel encrusted pistol has opportunity: True or False?
True (0.9717789891296182)
Jewel encrusted pistol has no opportunity: True or False?
True (0.9418684262191025)
Lithograph photo is guilty: True or False?
True (0.9805806866861946)
Lithograph photo is not guilty: True or False?
True (0.9686195238117354)
Lithograph photo has mean: True or False?
True (0.9859364033314291)
Lithograph photo has no mean: True or False?
True (0.967348574473821)
Lithograph photo has motive: True or False?
True (0.9728823298761804)
Lithograph photo has no motive: True or False?
True (0.9628131975124238)
Lithograph photo has opportunity: True or False?
True (0.9715639953911919)
Lithograph photo has no opportunity: True or False?
True (0.9593070162020048)
### CSA currency
- mean: False (0.3372035025621216)
- motive: False (0.10052490248010815)
- opportunity: False (0.16132026896779283)

### Diamond necklace
- mean: True (0.9860979323093966)
- motive: True (0.9869166012557465)
- opportunity: True (0.9815950994553841)

### Gold money clip
- mean: True (0.9375547191885567)
- motive: False (0.03718674151267698)
- opportunity: False (0.07878404515359838)

### Jewel encrusted pistol
- mean: True (0.9716178782667568)
- motive: False (0.025662720398945793)
- opportunity: False (0.058131573780897505)

### Lithograph photo
- mean: False (0.032651425526178945)
- motive: False (0.03718680248757622)
- opportunity: False (0.04069298379799524)

The culprit is Diamond necklace.
In fact, it is Lithograph photo.
## 5minutemystery-ask-marthathe-blackmailer
Horace Sage is guilty: True or False?
True (0.8656789607733094)
Horace Sage is not guilty: True or False?
True (0.8872045854516336)
Horace Sage has mean: True or False?
True (0.7981867775042927)
Horace Sage has no mean: True or False?
True (0.7279754925085274)
Horace Sage has motive: True or False?
True (0.913058338092082)
Horace Sage has no motive: True or False?
True (0.7256486384635821)
Horace Sage has opportunity: True or False?
True (0.8633915828320894)
Horace Sage has no opportunity: True or False?
True (0.6749080895533367)
Martin Amberton is guilty: True or False?
True (0.7193836000532381)
Martin Amberton is not guilty: True or False?
True (0.8663588183673241)
Martin Amberton has mean: True or False?
True (0.7745833916423246)
Martin Amberton has no mean: True or False?
True (0.6415346250061509)
Martin Amberton has motive: True or False?
True (0.8868131040663721)
Martin Amberton has no motive: True or False?
True (0.6706082735718226)
Martin Amberton has opportunity: True or False?
True (0.7233094544266295)
Martin Amberton has no opportunity: True or False?
True (0.5515737608116735)
Mary Devers is guilty: True or False?
True (0.8158201638039532)
Mary Devers is not guilty: True or False?
True (0.8795611817678315)
Mary Devers has mean: True or False?
True (0.8386797310322072)
Mary Devers has no mean: True or False?
True (0.6859493922090169)
Mary Devers has motive: True or False?
True (0.9121235591541035)
Mary Devers has no motive: True or False?
True (0.6113820047705449)
Mary Devers has opportunity: True or False?
True (0.854884620116169)
Mary Devers has no opportunity: True or False?
True (0.580352087772514)
Susan Royster is guilty: True or False?
True (0.7233094544266295)
Susan Royster is not guilty: True or False?
True (0.7981867775042927)
Susan Royster has mean: True or False?
True (0.7431679939957333)
Susan Royster has no mean: True or False?
True (0.6261241441180464)
Susan Royster has motive: True or False?
True (0.8840393439819743)
Susan Royster has no motive: True or False?
True (0.5156198737738186)
Susan Royster has opportunity: True or False?
True (0.7655933544531522)
Susan Royster has no opportunity: True or False?
True (0.5312093625105829)
### Horace Sage
- mean: False (0.27202450749147256)
- motive: False (0.2743513615364179)
- opportunity: False (0.3250919104466633)

### Martin Amberton
- mean: True (0.7745833916423246)
- motive: True (0.8868131040663721)
- opportunity: True (0.7233094544266295)

### Mary Devers
- mean: False (0.31405060779098315)
- motive: False (0.38861799522945506)
- opportunity: False (0.419647912227486)

### Susan Royster
- mean: False (0.3738758558819536)
- motive: False (0.48438012622618143)
- opportunity: False (0.4687906374894171)

The culprit is Martin Amberton.
In fact, it is Mary Devers.
## 5minutemystery-a-dream-of-old-salem
Abigail Thorpe is guilty: True or False?
True (0.8187367896794966)
Abigail Thorpe is not guilty: True or False?
True (0.8278281666221954)
Abigail Thorpe has mean: True or False?
True (0.6876299924560524)
Abigail Thorpe has no mean: True or False?
True (0.6959583025067009)
Abigail Thorpe has motive: True or False?
True (0.9284088027271398)
Abigail Thorpe has no motive: True or False?
True (0.8397339530959691)
Abigail Thorpe has opportunity: True or False?
True (0.8991213421091365)
Abigail Thorpe has no opportunity: True or False?
True (0.8333246107254184)
Adam Browne is guilty: True or False?
True (0.7839884808423031)
Adam Browne is not guilty: True or False?
True (0.7416740778117503)
Adam Browne has mean: True or False?
True (0.5409238971378262)
Adam Browne has no mean: True or False?
True (0.646013666311734)
Adam Browne has motive: True or False?
True (0.8543993214720741)
Adam Browne has no motive: True or False?
True (0.615087855649269)
Adam Browne has opportunity: True or False?
True (0.7833262085677729)
Adam Browne has no opportunity: True or False?
True (0.5660185351323219)
Goodwife Browne is guilty: True or False?
True (0.8524448242555318)
Goodwife Browne is not guilty: True or False?
True (0.7950222460539826)
Goodwife Browne has mean: True or False?
True (0.6504672743423094)
Goodwife Browne has no mean: True or False?
True (0.7106282704218558)
Goodwife Browne has motive: True or False?
True (0.9383503780077049)
Goodwife Browne has no motive: True or False?
True (0.8086723099497763)
Goodwife Browne has opportunity: True or False?
True (0.8354834909254251)
Goodwife Browne has no opportunity: True or False?
True (0.7620701143808404)
Sarah Goodwin is guilty: True or False?
True (0.8300437258865985)
Sarah Goodwin is not guilty: True or False?
True (0.8962513815714083)
Sarah Goodwin has mean: True or False?
True (0.5926666351772785)
Sarah Goodwin has no mean: True or False?
True (0.642432441257838)
Sarah Goodwin has motive: True or False?
True (0.8122724274380432)
Sarah Goodwin has no motive: True or False?

Map:  62%|██████▏   | 126/203 [2:50:36<1:58:22, 92.24s/ examples]
Map:  63%|██████▎   | 127/203 [2:52:10<1:57:26, 92.71s/ examples]True (0.6095241271158658)
Sarah Goodwin has opportunity: True or False?
True (0.7520125537161032)
Sarah Goodwin has no opportunity: True or False?
True (0.546738093993928)
### Abigail Thorpe
- mean: True (0.6876299924560524)
- motive: True (0.9284088027271398)
- opportunity: True (0.8991213421091365)

### Adam Browne
- mean: True (0.5409238971378262)
- motive: False (0.38491214435073096)
- opportunity: False (0.4339814648676781)

### Goodwife Browne
- mean: True (0.6504672743423094)
- motive: False (0.19132769005022365)
- opportunity: False (0.23792988561915962)

### Sarah Goodwin
- mean: True (0.5926666351772785)
- motive: False (0.3904758728841342)
- opportunity: False (0.45326190600607197)

The culprit is Abigail Thorpe.
In fact, it is Adam Browne.
## 5minutemystery-the-antique-clock-mystery
The grandfather clock (stopped at 10:10 p.m.) is guilty: True or False?
True (0.9527503243194666)
The grandfather clock (stopped at 10:10 p.m.) is not guilty: True or False?
True (0.9422947179693436)
The grandfather clock (stopped at 10:10 p.m.) has mean: True or False?
True (0.936749461409047)
The grandfather clock (stopped at 10:10 p.m.) has no mean: True or False?
True (0.9019206778000431)
The grandfather clock (stopped at 10:10 p.m.) has motive: True or False?
True (0.9707986706740892)
The grandfather clock (stopped at 10:10 p.m.) has no motive: True or False?
True (0.8991213421091365)
The grandfather clock (stopped at 10:10 p.m.) has opportunity: True or False?
True (0.9463988549853353)
The grandfather clock (stopped at 10:10 p.m.) has no opportunity: True or False?
True (0.8464508054137014)
The mantle clock (stopped at 10:59 p.m.) is guilty: True or False?
True (0.9313377150989219)
The mantle clock (stopped at 10:59 p.m.) is not guilty: True or False?
True (0.9326989068252284)
The mantle clock (stopped at 10:59 p.m.) has mean: True or False?
True (0.952397347230678)
The mantle clock (stopped at 10:59 p.m.) has no mean: True or False?
True (0.9164093756391206)
The mantle clock (stopped at 10:59 p.m.) has motive: True or False?
True (0.9688561547723137)
The mantle clock (stopped at 10:59 p.m.) has no motive: True or False?
True (0.9286680258169302)
The mantle clock (stopped at 10:59 p.m.) has opportunity: True or False?
True (0.9227612010756272)
The mantle clock (stopped at 10:59 p.m.) has no opportunity: True or False?
True (0.897695304229796)
The pocket watch (stopped at 3:18 a.m.) is guilty: True or False?
True (0.9624620067145623)
The pocket watch (stopped at 3:18 a.m.) is not guilty: True or False?
True (0.9664104579001461)
The pocket watch (stopped at 3:18 a.m.) has mean: True or False?
True (0.9396923783210908)
The pocket watch (stopped at 3:18 a.m.) has no mean: True or False?
True (0.9502265454272235)
The pocket watch (stopped at 3:18 a.m.) has motive: True or False?
True (0.9706321357771589)
The pocket watch (stopped at 3:18 a.m.) has no motive: True or False?
True (0.9383503780077049)
The pocket watch (stopped at 3:18 a.m.) has opportunity: True or False?
True (0.9447913165152162)
The pocket watch (stopped at 3:18 a.m.) has no opportunity: True or False?
True (0.9309620852900756)
The wall clock (stopped at 2:01 a.m.) is guilty: True or False?
True (0.9396923783210908)
The wall clock (stopped at 2:01 a.m.) is not guilty: True or False?
True (0.9265699426348812)
The wall clock (stopped at 2:01 a.m.) has mean: True or False?
True (0.9092645024391882)
The wall clock (stopped at 2:01 a.m.) has no mean: True or False?
True (0.8925625719484378)
The wall clock (stopped at 2:01 a.m.) has motive: True or False?
True (0.9705206155895632)
The wall clock (stopped at 2:01 a.m.) has no motive: True or False?
True (0.905656637917298)
The wall clock (stopped at 2:01 a.m.) has opportunity: True or False?
True (0.927887794449634)
The wall clock (stopped at 2:01 a.m.) has no opportunity: True or False?
True (0.8534247816107388)
The wristwatch (stopped at 5:22 p.m.) is guilty: True or False?
True (0.9273633336539081)
The wristwatch (stopped at 5:22 p.m.) is not guilty: True or False?
True (0.9260365949489886)
The wristwatch (stopped at 5:22 p.m.) has mean: True or False?
True (0.9121235591541035)
The wristwatch (stopped at 5:22 p.m.) has no mean: True or False?
True (0.9238675252821831)
The wristwatch (stopped at 5:22 p.m.) has motive: True or False?
True (0.9299510719523877)
The wristwatch (stopped at 5:22 p.m.) has no motive: True or False?
True (0.8868131040663721)
The wristwatch (stopped at 5:22 p.m.) has opportunity: True or False?
True (0.9063219998220023)
The wristwatch (stopped at 5:22 p.m.) has no opportunity: True or False?
True (0.883638205304735)
### The grandfather clock (stopped at 10:10 p.m.)
- mean: False (0.09807932219995685)
- motive: False (0.10087865789086348)
- opportunity: False (0.15354919458629857)

### The mantle clock (stopped at 10:59 p.m.)
- mean: False (0.08359062436087938)
- motive: False (0.0713319741830698)
- opportunity: False (0.10230469577020396)

### The pocket watch (stopped at 3:18 a.m.)
- mean: True (0.9396923783210908)
- motive: True (0.9706321357771589)
- opportunity: True (0.9447913165152162)

### The wall clock (stopped at 2:01 a.m.)
- mean: False (0.1074374280515622)
- motive: False (0.094343362082702)
- opportunity: False (0.14657521838926124)

### The wristwatch (stopped at 5:22 p.m.)
- mean: True (0.9121235591541035)
- motive: False (0.11318689593362785)
- opportunity: False (0.11636179469526498)

The culprit is The pocket watch (stopped at 3:18 a.m.).
In fact, it is The mantle clock (stopped at 10:59 p.m.).
## 5minutemystery-ask-marthathe-perjurer
Horace Osamway is guilty: True or False?
True (0.8982321647536474)
Horace Osamway is not guilty: True or False?
True (0.921357630313903)
Horace Osamway has mean: True or False?
True (0.8098781635062345)
Horace Osamway has no mean: True or False?
True (0.832781310996106)
Horace Osamway has motive: True or False?
True (0.9450961931109775)
Horace Osamway has no motive: True or False?
True (0.7988153087356352)
Horace Osamway has opportunity: True or False?
True (0.9458013187522837)
Horace Osamway has no opportunity: True or False?
True (0.7170118721569225)
John Eberley is guilty: True or False?
True (0.8622357197068287)
John Eberley is not guilty: True or False?
True (0.8394709207566112)
John Eberley has mean: True or False?
True (0.6876299924560524)
John Eberley has no mean: True or False?
True (0.6723316913929156)
John Eberley has motive: True or False?
True (0.9031234959323464)
John Eberley has no motive: True or False?
True (0.7154240000492645)
John Eberley has opportunity: True or False?
True (0.7570766705324253)
John Eberley has no opportunity: True or False?
False (0.5165954726976894)
Martha Cranston is guilty: True or False?
True (0.8247443993706964)
Martha Cranston is not guilty: True or False?
True (0.864539320523716)
Martha Cranston has mean: True or False?
True (0.591723272524637)
Martha Cranston has no mean: True or False?
False (0.566977858563838)
Martha Cranston has motive: True or False?
True (0.9087799803825275)
Martha Cranston has no motive: True or False?
True (0.6460137433225688)
Martha Cranston has opportunity: True or False?
True (0.7074046739492601)
Martha Cranston has no opportunity: True or False?
False (0.6067314814064781)
Mildred Greene is guilty: True or False?
True (0.8092759225969047)
Mildred Greene is not guilty: True or False?
True (0.8244619332958376)
Mildred Greene has mean: True or False?
True (0.5879431210535583)
Mildred Greene has no mean: True or False?
False (0.5926666351772785)
Mildred Greene has motive: True or False?
True (0.8631610245991334)
Mildred Greene has no motive: True or False?
True (0.5841525779336078)
Mildred Greene has opportunity: True or False?
True (0.7017130830397807)
Mildred Greene has no opportunity: True or False?
False (0.5612147992901458)
### Horace Osamway
- mean: True (0.8098781635062345)
- motive: False (0.20118469126436478)
- opportunity: False (0.2829881278430775)

### John Eberley
- mean: True (0.6876299924560524)
- motive: True (0.9031234959323464)
- opportunity: True (0.7570766705324253)

### Martha Cranston
- mean: True (0.591723272524637)
- motive: False (0.3539862566774312)

Map:  63%|██████▎   | 128/203 [2:53:39<1:54:46, 91.82s/ examples]
Map:  64%|██████▎   | 129/203 [2:55:18<1:55:44, 93.85s/ examples]
Map:  64%|██████▍   | 130/203 [2:56:22<1:43:17, 84.89s/ examples]- opportunity: True (0.7074046739492601)

### Mildred Greene
- mean: True (0.5879431210535583)
- motive: False (0.41584742206639225)
- opportunity: True (0.7017130830397807)

The culprit is John Eberley.
In fact, it is John Eberley.
## 5minutemystery-ask-marthathe-embezzler
Joan Carstairs is guilty: True or False?
True (0.816406362162552)
Joan Carstairs is not guilty: True or False?
True (0.9099069836112468)
Joan Carstairs has mean: True or False?
True (0.5841525779336078)
Joan Carstairs has no mean: True or False?
True (0.5360700410935405)
Joan Carstairs has motive: True or False?
True (0.9124361266596831)
Joan Carstairs has no motive: True or False?
True (0.7065955344877805)
Joan Carstairs has opportunity: True or False?
True (0.7898827135821628)
Joan Carstairs has no opportunity: True or False?
True (0.6909762697651828)
Les Nolting is guilty: True or False?
True (0.8300437877296776)
Les Nolting is not guilty: True or False?
True (0.8918110138739693)
Les Nolting has mean: True or False?
True (0.705785027818136)
Les Nolting has no mean: True or False?
True (0.6406358487498992)
Les Nolting has motive: True or False?
True (0.8883720049821552)
Les Nolting has no motive: True or False?
True (0.6011254300530117)
Les Nolting has opportunity: True or False?
True (0.7975568155246964)
Les Nolting has no opportunity: True or False?
False (0.5945512478395265)
Paul Brassard is guilty: True or False?
True (0.8714748565614324)
Paul Brassard is not guilty: True or False?
True (0.8459424357871997)
Paul Brassard has mean: True or False?
True (0.7872777601997338)
Paul Brassard has no mean: True or False?
True (0.7008947664177184)
Paul Brassard has motive: True or False?
True (0.9353465445225602)
Paul Brassard has no motive: True or False?
True (0.6791786560103119)
Paul Brassard has opportunity: True or False?
True (0.789233749534095)
Paul Brassard has no opportunity: True or False?
True (0.5321819753403337)
Sarah Kimble is guilty: True or False?
True (0.8278281666221954)
Sarah Kimble is not guilty: True or False?
True (0.8692713407917644)
Sarah Kimble has mean: True or False?
True (0.7779753136455794)
Sarah Kimble has no mean: True or False?
True (0.7333563569098757)
Sarah Kimble has motive: True or False?
True (0.9257686153543061)
Sarah Kimble has no motive: True or False?
True (0.7154240000492645)
Sarah Kimble has opportunity: True or False?
True (0.7193836643711469)
Sarah Kimble has no opportunity: True or False?
False (0.5097643762740132)
### Joan Carstairs
- mean: False (0.4639299589064595)
- motive: False (0.29340446551221955)
- opportunity: False (0.3090237302348172)

### Les Nolting
- mean: False (0.3593641512501008)
- motive: False (0.39887456994698833)
- opportunity: True (0.7975568155246964)

### Paul Brassard
- mean: False (0.2991052335822816)
- motive: False (0.3208213439896881)
- opportunity: False (0.46781802465966627)

### Sarah Kimble
- mean: True (0.7779753136455794)
- motive: True (0.9257686153543061)
- opportunity: True (0.7193836643711469)

The culprit is Sarah Kimble.
In fact, it is Sarah Kimble.
## 5minutemystery-the-backyard-slumber-party
Justin Scott is guilty: True or False?
True (0.9643214331583058)
Justin Scott is not guilty: True or False?
True (0.9826243527033713)
Justin Scott has mean: True or False?
True (0.9543079730970608)
Justin Scott has no mean: True or False?
True (0.9585376970077499)
Justin Scott has motive: True or False?
True (0.9875922800954249)
Justin Scott has no motive: True or False?
True (0.966537058600438)
Justin Scott has opportunity: True or False?
True (0.9791157846694846)
Justin Scott has no opportunity: True or False?
True (0.9329437018480795)
Martin Simmons is guilty: True or False?
True (0.927887794449634)
Martin Simmons is not guilty: True or False?
True (0.9704366318314164)
Martin Simmons has mean: True or False?
True (0.91789335161495)
Martin Simmons has no mean: True or False?
True (0.9600626824595854)
Martin Simmons has motive: True or False?
True (0.9799573413335708)
Martin Simmons has no motive: True or False?
True (0.9815950994553841)
Martin Simmons has opportunity: True or False?
True (0.9870296120305199)
Martin Simmons has no opportunity: True or False?
True (0.9817357070099405)
Stephen Kennelly is guilty: True or False?
True (0.9381240005131491)
Stephen Kennelly is not guilty: True or False?
True (0.9655764701970907)
Stephen Kennelly has mean: True or False?
True (0.8803862939824989)
Stephen Kennelly has no mean: True or False?
True (0.9036349079321685)
Stephen Kennelly has motive: True or False?
True (0.9674102673982512)
Stephen Kennelly has no motive: True or False?
True (0.9392480858026054)
Stephen Kennelly has opportunity: True or False?
True (0.9525741334779666)
Stephen Kennelly has no opportunity: True or False?
True (0.8984105603938967)
Trevor Sutherland is guilty: True or False?
True (0.9372107968415931)
Trevor Sutherland is not guilty: True or False?
True (0.9683213832701327)
Trevor Sutherland has mean: True or False?
True (0.9317114347547434)
Trevor Sutherland has no mean: True or False?
True (0.9677776702396809)
Trevor Sutherland has motive: True or False?
True (0.9746287473052455)
Trevor Sutherland has no motive: True or False?
True (0.9465966835599983)
Trevor Sutherland has opportunity: True or False?
True (0.9781354673766767)
Trevor Sutherland has no opportunity: True or False?
True (0.9403530352223053)
### Justin Scott
- mean: True (0.9543079730970608)
- motive: False (0.03346294139956196)
- opportunity: False (0.06705629815192049)

### Martin Simmons
- mean: True (0.91789335161495)
- motive: True (0.9799573413335708)
- opportunity: True (0.9870296120305199)

### Stephen Kennelly
- mean: True (0.8803862939824989)
- motive: False (0.06075191419739456)
- opportunity: False (0.10158943960610334)

### Trevor Sutherland
- mean: True (0.9317114347547434)
- motive: False (0.053403316440001736)
- opportunity: False (0.05964696477769471)

The culprit is Martin Simmons.
In fact, it is Trevor Sutherland.
## 5minutemystery-the-rock-star-mystery
Gorg is guilty: True or False?
True (0.9816655524802333)
Gorg is not guilty: True or False?
True (0.9907498958644636)
Gorg has mean: True or False?
True (0.9460011721384068)
Gorg has no mean: True or False?
True (0.9518632280135741)
Gorg has motive: True or False?
True (0.9852996465775707)
Gorg has no motive: True or False?
True (0.9748211501698323)
Gorg has opportunity: True or False?
True (0.9514138119240159)
Gorg has no opportunity: True or False?
True (0.9430335755950109)
Stu is guilty: True or False?
True (0.9319595674053855)
Stu is not guilty: True or False?
True (0.9686788908454032)
Stu has mean: True or False?
True (0.9238675252821831)
Stu has no mean: True or False?
True (0.9421883822940393)
Stu has motive: True or False?
True (0.9796676632098326)
Stu has no motive: True or False?
True (0.9600626824595854)
Stu has opportunity: True or False?
True (0.9697281713378947)
Stu has no opportunity: True or False?
True (0.8962513815714083)
The Neighborhood Burgler is guilty: True or False?
True (0.959912598704516)
The Neighborhood Burgler is not guilty: True or False?
True (0.9710742839974638)
The Neighborhood Burgler has mean: True or False?
True (0.9505029326253388)
The Neighborhood Burgler has no mean: True or False?
True (0.9554024325650102)
The Neighborhood Burgler has motive: True or False?
True (0.9816655524802333)
The Neighborhood Burgler has no motive: True or False?
True (0.9312127242200585)
The Neighborhood Burgler has opportunity: True or False?
True (0.9685006130461804)
The Neighborhood Burgler has no opportunity: True or False?
True (0.8860265599597172)
Tina is guilty: True or False?
True (0.9675331712558415)
Tina is not guilty: True or False?
True (0.9758085004791638)
Tina has mean: True or False?
True (0.878314250659373)
Tina has no mean: True or False?
True (0.9019206778000431)
Tina has motive: True or False?
True (0.9647889147180926)
Tina has no motive: True or False?
True (0.9422946582938823)
Tina has opportunity: True or False?
True (0.8991214023999228)
Tina has no opportunity: True or False?
True (0.8591917766133458)
### Gorg
- mean: True (0.9460011721384068)
- motive: True (0.9852996465775707)

Map:  65%|██████▍   | 131/203 [2:57:58<1:45:47, 88.16s/ examples]
Map:  65%|██████▌   | 132/203 [2:59:04<1:36:40, 81.69s/ examples]
Map:  66%|██████▌   | 133/203 [3:00:32<1:37:20, 83.44s/ examples]- opportunity: True (0.9514138119240159)

### Stu
- mean: True (0.9238675252821831)
- motive: False (0.03993731754041463)
- opportunity: False (0.10374861842859173)

### The Neighborhood Burgler
- mean: True (0.9505029326253388)
- motive: False (0.06878727577994148)
- opportunity: False (0.11397344004028276)

### Tina
- mean: True (0.878314250659373)
- motive: False (0.05770534170611774)
- opportunity: False (0.14080822338665422)

The culprit is Gorg.
In fact, it is Tina.
## 5minutemystery-ask-marthathe-arsonist
Keen Observer is guilty: True or False?
True (0.8524448242555318)
Keen Observer is not guilty: True or False?
True (0.9102267600218574)
Keen Observer has mean: True or False?
True (0.861071588244826)
Keen Observer has no mean: True or False?
True (0.8433797899747144)
Keen Observer has motive: True or False?
True (0.9319595674053855)
Keen Observer has no motive: True or False?
True (0.8895288123486662)
Keen Observer has opportunity: True or False?
True (0.9410069597342015)
Keen Observer has no opportunity: True or False?
True (0.9092645024391882)
Minding My Own Business is guilty: True or False?
True (0.8740772044235984)
Minding My Own Business is not guilty: True or False?
True (0.9403530352223053)
Minding My Own Business has mean: True or False?
True (0.9133679254389228)
Minding My Own Business has no mean: True or False?
True (0.8305941261447712)
Minding My Own Business has motive: True or False?
True (0.9471859926317535)
Minding My Own Business has no motive: True or False?
True (0.9102267057681164)
Minding My Own Business has opportunity: True or False?
True (0.9567959908103164)
Minding My Own Business has no opportunity: True or False?
True (0.861538171568877)
Scared Stiff is guilty: True or False?
True (0.8832359917473193)
Scared Stiff is not guilty: True or False?
True (0.9374402785760423)
Scared Stiff has mean: True or False?
True (0.9388008138003494)
Scared Stiff has no mean: True or False?
True (0.908941745727715)
Scared Stiff has motive: True or False?
True (0.9661560069290531)
Scared Stiff has no motive: True or False?
True (0.865678909174824)
Scared Stiff has opportunity: True or False?
True (0.9304582506719414)
Scared Stiff has no opportunity: True or False?
True (0.9222025890552223)
Watchful Waiter is guilty: True or False?
True (0.8175745039697023)
Watchful Waiter is not guilty: True or False?
True (0.8719117627136385)
Watchful Waiter has mean: True or False?
True (0.8019358443954961)
Watchful Waiter has no mean: True or False?
True (0.8187367896794966)
Watchful Waiter has motive: True or False?
True (0.9149009617112335)
Watchful Waiter has no motive: True or False?
True (0.8255897087847518)
Watchful Waiter has opportunity: True or False?
True (0.8701565303520181)
Watchful Waiter has no opportunity: True or False?
True (0.8031737798924701)
### Keen Observer
- mean: True (0.861071588244826)
- motive: True (0.9319595674053855)
- opportunity: True (0.9410069597342015)

### Minding My Own Business
- mean: False (0.16940587385522876)
- motive: False (0.08977329423188363)
- opportunity: False (0.13846182843112298)

### Scared Stiff
- mean: False (0.09105825427228498)
- motive: False (0.13432109082517596)
- opportunity: False (0.07779741094477766)

### Watchful Waiter
- mean: True (0.8019358443954961)
- motive: False (0.1744102912152482)
- opportunity: False (0.19682622010752993)

The culprit is Keen Observer.
In fact, it is Watchful Waiter.
## 5minutemystery-fatal-computer-crash
Alex Redoff is guilty: True or False?
True (0.9210741501882456)
Alex Redoff is not guilty: True or False?
True (0.9567151085975119)
Alex Redoff has mean: True or False?
True (0.9233161821369215)
Alex Redoff has no mean: True or False?
True (0.9205042693180057)
Alex Redoff has motive: True or False?
True (0.9565531009888748)
Alex Redoff has no motive: True or False?
True (0.9257686153543061)
Alex Redoff has opportunity: True or False?
True (0.9577545517476556)
Alex Redoff has no opportunity: True or False?
True (0.9331876642092066)
Cheryl Compton is guilty: True or False?
True (0.9257686153543061)
Cheryl Compton is not guilty: True or False?
True (0.9449947479233238)
Cheryl Compton has mean: True or False?
True (0.8872045854516336)
Cheryl Compton has no mean: True or False?
True (0.9063219998220023)
Cheryl Compton has motive: True or False?
True (0.9436599010766334)
Cheryl Compton has no motive: True or False?
True (0.9053223122169206)
Cheryl Compton has opportunity: True or False?
True (0.9356999401883446)
Cheryl Compton has no opportunity: True or False?
True (0.9235923286659299)
Claire Denninger is guilty: True or False?
True (0.9095863097773887)
Claire Denninger is not guilty: True or False?
True (0.9631959807327839)
Claire Denninger has mean: True or False?
True (0.9010534302227574)
Claire Denninger has no mean: True or False?
True (0.9430336353172679)
Claire Denninger has motive: True or False?
True (0.9347534165970482)
Claire Denninger has no motive: True or False?
True (0.8852351930010195)
Claire Denninger has opportunity: True or False?
True (0.9477691649813238)
Claire Denninger has no opportunity: True or False?
True (0.9320833668388808)
Natalie Sampson is guilty: True or False?
True (0.9199306971612747)
Natalie Sampson is not guilty: True or False?
True (0.9473810811508532)
Natalie Sampson has mean: True or False?
True (0.8895288719962232)
Natalie Sampson has no mean: True or False?
True (0.9139841191734227)
Natalie Sampson has motive: True or False?
True (0.9537942396657707)
Natalie Sampson has no motive: True or False?
True (0.8524448242555318)
Natalie Sampson has opportunity: True or False?
True (0.9466952677359475)
Natalie Sampson has no opportunity: True or False?
True (0.8925625719484378)
### Alex Redoff
- mean: False (0.07949573068199434)
- motive: False (0.0742313846456939)
- opportunity: False (0.06681233579079338)

### Cheryl Compton
- mean: True (0.8872045854516336)
- motive: True (0.9436599010766334)
- opportunity: True (0.9356999401883446)

### Claire Denninger
- mean: True (0.9010534302227574)
- motive: False (0.1147648069989805)
- opportunity: False (0.06791663316111918)

### Natalie Sampson
- mean: True (0.8895288719962232)
- motive: False (0.1475551757444682)
- opportunity: False (0.1074374280515622)

The culprit is Cheryl Compton.
In fact, it is Natalie Sampson.
## 5minutemystery-the-rob-club-murder-mystery
Al Gibson is guilty: True or False?
True (0.9854684474764122)
Al Gibson is not guilty: True or False?
True (0.9800912134408363)
Al Gibson has mean: True or False?
True (0.8723473540228537)
Al Gibson has no mean: True or False?
True (0.7931059536445917)
Al Gibson has motive: True or False?
True (0.9910233023598813)
Al Gibson has no motive: True or False?
True (0.9222025272167219)
Al Gibson has opportunity: True or False?
True (0.9760379793845908)
Al Gibson has no opportunity: True or False?
True (0.8596637206861489)
Johnny Woodward is guilty: True or False?
True (0.9873017666029376)
Johnny Woodward is not guilty: True or False?
True (0.9916842575901101)
Johnny Woodward has mean: True or False?
True (0.9741412398478105)
Johnny Woodward has no mean: True or False?
True (0.9747251273624444)
Johnny Woodward has motive: True or False?
True (0.9970963000269885)
Johnny Woodward has no motive: True or False?
True (0.9566342225308191)
Johnny Woodward has opportunity: True or False?
True (0.9957684278724305)
Johnny Woodward has no opportunity: True or False?
True (0.9494823209990744)
Ray Shields is guilty: True or False?
True (0.9859364033314291)
Ray Shields is not guilty: True or False?
True (0.9761746525814899)
Ray Shields has mean: True or False?
True (0.9596109393754703)
Ray Shields has no mean: True or False?
True (0.8929365260632085)
Ray Shields has motive: True or False?
True (0.9937949778263467)
Ray Shields has no motive: True or False?
True (0.9149009617112335)
Ray Shields has opportunity: True or False?
True (0.974580348460635)
Ray Shields has no opportunity: True or False?
True (0.8638516611889259)
Tim Acord is guilty: True or False?
True (0.9798997635332343)
Tim Acord is not guilty: True or False?
True (0.9752489919994439)
Tim Acord has mean: True or False?
True (0.9184802773231918)

Map:  66%|██████▌   | 134/203 [3:01:48<1:33:20, 81.16s/ examples]
Map:  67%|██████▋   | 135/203 [3:02:56<1:27:42, 77.39s/ examples]
Map:  67%|██████▋   | 136/203 [3:04:15<1:26:48, 77.74s/ examples]Tim Acord has no mean: True or False?
True (0.893681109060862)
Tim Acord has motive: True or False?
True (0.9898303149898466)
Tim Acord has no motive: True or False?
True (0.9086179121100144)
Tim Acord has opportunity: True or False?
True (0.9706877478963396)
Tim Acord has no opportunity: True or False?
True (0.9095862487848758)
Watson Treadway is guilty: True or False?
True (0.982590972614882)
Watson Treadway is not guilty: True or False?
True (0.9670387494740702)
Watson Treadway has mean: True or False?
True (0.8895288719962232)
Watson Treadway has no mean: True or False?
True (0.8568122940392877)
Watson Treadway has motive: True or False?
True (0.9954305886032181)
Watson Treadway has no motive: True or False?
True (0.9559813721912603)
Watson Treadway has opportunity: True or False?
True (0.9632304925109479)
Watson Treadway has no opportunity: True or False?
True (0.9381240005131491)
### Al Gibson
- mean: False (0.2068940463554083)
- motive: False (0.07779747278327809)
- opportunity: False (0.14033627931385106)

### Johnny Woodward
- mean: True (0.9741412398478105)
- motive: True (0.9970963000269885)
- opportunity: True (0.9957684278724305)

### Ray Shields
- mean: False (0.1070634739367915)
- motive: False (0.08509903828876653)
- opportunity: False (0.13614833881107413)

### Tim Acord
- mean: False (0.10631889093913804)
- motive: False (0.09138208788998559)
- opportunity: False (0.09041375121512418)

### Watson Treadway
- mean: False (0.14318770596071229)
- motive: False (0.04401862780873966)
- opportunity: False (0.06187599948685085)

The culprit is Johnny Woodward.
In fact, it is Johnny Woodward.
## 5minutemystery-ask-marthathe-litterer
Concerned Neighbor is guilty: True or False?
True (0.7394223819718238)
Concerned Neighbor is not guilty: True or False?
True (0.7898827724330132)
Concerned Neighbor has mean: True or False?
True (0.7527403228571042)
Concerned Neighbor has no mean: True or False?
True (0.7962924261546153)
Concerned Neighbor has motive: True or False?
True (0.9095862487848758)
Concerned Neighbor has no motive: True or False?
True (0.7498207054286419)
Concerned Neighbor has opportunity: True or False?
True (0.8116760258690822)
Concerned Neighbor has no opportunity: True or False?
True (0.6113820047705449)
Confused Commuter is guilty: True or False?
True (0.9412234437340664)
Confused Commuter is not guilty: True or False?
True (0.9407897579933674)
Confused Commuter has mean: True or False?
True (0.934155284694701)
Confused Commuter has no mean: True or False?
True (0.9334307932218529)
Confused Commuter has motive: True or False?
True (0.9539660824292815)
Confused Commuter has no motive: True or False?
True (0.8261514850267767)
Confused Commuter has opportunity: True or False?
True (0.9669139993413022)
Confused Commuter has no opportunity: True or False?
True (0.8778961263000082)
Perplexed Dog Walker is guilty: True or False?
True (0.9029524325377104)
Perplexed Dog Walker is not guilty: True or False?
True (0.9471859326465281)
Perplexed Dog Walker has mean: True or False?
True (0.920217993899809)
Perplexed Dog Walker has no mean: True or False?
True (0.9187722824991111)
Perplexed Dog Walker has motive: True or False?
True (0.9449947479233238)
Perplexed Dog Walker has no motive: True or False?
True (0.9029524325377104)
Perplexed Dog Walker has opportunity: True or False?
True (0.9590009457171959)
Perplexed Dog Walker has no opportunity: True or False?
True (0.8543993851297865)
Smug in Suburbia is guilty: True or False?
True (0.8553685501761973)
Smug in Suburbia is not guilty: True or False?
True (0.9252299659402181)
Smug in Suburbia has mean: True or False?
True (0.8828325273478573)
Smug in Suburbia has no mean: True or False?
True (0.8740772565226612)
Smug in Suburbia has motive: True or False?
True (0.875361437979977)
Smug in Suburbia has no motive: True or False?
True (0.8204694405411458)
Smug in Suburbia has opportunity: True or False?
True (0.8816149238192855)
Smug in Suburbia has no opportunity: True or False?
True (0.7839884808423031)
### Concerned Neighbor
- mean: True (0.7527403228571042)
- motive: False (0.2501792945713581)
- opportunity: False (0.38861799522945506)

### Confused Commuter
- mean: False (0.06656920677814715)
- motive: False (0.1738485149732233)
- opportunity: False (0.12210387369999176)

### Perplexed Dog Walker
- mean: False (0.08122771750088886)
- motive: False (0.0970475674622896)
- opportunity: False (0.14560061487021347)

### Smug in Suburbia
- mean: True (0.8828325273478573)
- motive: True (0.875361437979977)
- opportunity: True (0.8816149238192855)

The culprit is Smug in Suburbia.
In fact, it is Smug in Suburbia.
## 5minutemystery-drama-queen
Alfred Cooper is guilty: True or False?
True (0.8289388437432279)
Alfred Cooper is not guilty: True or False?
True (0.9270997017012965)
Alfred Cooper has mean: True or False?
True (0.7613611200983542)
Alfred Cooper has no mean: True or False?
True (0.49999999904767284)
Alfred Cooper has motive: True or False?
True (0.9384632725948482)
Alfred Cooper has no motive: True or False?
True (0.8413048399699521)
Alfred Cooper has opportunity: True or False?
True (0.8587185689177256)
Alfred Cooper has no opportunity: True or False?
False (0.6001883860246252)
Isabelle Rogers is guilty: True or False?
True (0.9046505126460354)
Isabelle Rogers is not guilty: True or False?
True (0.9485372300670596)
Isabelle Rogers has mean: True or False?
True (0.8407825844829613)
Isabelle Rogers has no mean: True or False?
True (0.7065955344877805)
Isabelle Rogers has motive: True or False?
True (0.9244152304846833)
Isabelle Rogers has no motive: True or False?
True (0.854884620116169)
Isabelle Rogers has opportunity: True or False?
True (0.8423451152856819)
Isabelle Rogers has no opportunity: True or False?
True (0.6566582893190611)
James Fennimore is guilty: True or False?
True (0.925499741040984)
James Fennimore is not guilty: True or False?
True (0.8872045854516336)
James Fennimore has mean: True or False?
True (0.8688267468984366)
James Fennimore has no mean: True or False?
True (0.6397360437814448)
James Fennimore has motive: True or False?
True (0.941654207327861)
James Fennimore has no motive: True or False?
True (0.7446563751413027)
James Fennimore has opportunity: True or False?
True (0.8333246107254184)
James Fennimore has no opportunity: True or False?
True (0.6706082735718226)
Madge Anderson is guilty: True or False?
True (0.92386746333204)
Madge Anderson is not guilty: True or False?
True (0.9550683507359511)
Madge Anderson has mean: True or False?
True (0.8344068526674736)
Madge Anderson has no mean: True or False?
True (0.6020616403539744)
Madge Anderson has motive: True or False?
True (0.9584600345758558)
Madge Anderson has no motive: True or False?
True (0.8987665204865408)
Madge Anderson has opportunity: True or False?
True (0.8204694405411458)
Madge Anderson has no opportunity: True or False?
True (0.5755879969637064)
### Alfred Cooper
- mean: True (0.7613611200983542)
- motive: True (0.9384632725948482)
- opportunity: True (0.8587185689177256)

### Isabelle Rogers
- mean: False (0.29340446551221955)
- motive: False (0.14511537988383105)
- opportunity: False (0.3433417106809389)

### James Fennimore
- mean: False (0.3602639562185552)
- motive: False (0.2553436248586973)
- opportunity: False (0.3293917264281774)

### Madge Anderson
- mean: False (0.39793835964602564)
- motive: False (0.10123347951345918)
- opportunity: False (0.42441200303629356)

The culprit is Alfred Cooper.
In fact, it is James Fennimore.
## 5minutemystery-the-gourmet-mystery
Antoine is guilty: True or False?
True (0.6557770400181139)
Antoine is not guilty: True or False?
True (0.8316905440184192)
Antoine has mean: True or False?
True (0.7799928701983835)
Antoine has no mean: True or False?
True (0.8499711693725173)
Antoine has motive: True or False?
True (0.8966140148346177)
Antoine has no motive: True or False?
True (0.8652241235443877)
Antoine has opportunity: True or False?
True (0.8679338697256817)
Antoine has no opportunity: True or False?
True (0.9039745373919651)
Georges Monceau is guilty: True or False?
True (0.8134607635851566)
Georges Monceau is not guilty: True or False?

Map:  67%|██████▋   | 137/203 [3:05:22<1:22:07, 74.67s/ examples]
Map:  68%|██████▊   | 138/203 [3:07:02<1:29:04, 82.22s/ examples]
Map:  68%|██████▊   | 139/203 [3:08:22<1:26:59, 81.56s/ examples]True (0.8951566249612815)
Georges Monceau has mean: True or False?
True (0.7287483223557857)
Georges Monceau has no mean: True or False?
True (0.8092759828926619)
Georges Monceau has motive: True or False?
True (0.921357630313903)
Georges Monceau has no motive: True or False?
True (0.9390248639367113)
Georges Monceau has opportunity: True or False?
True (0.8984105603938967)
Georges Monceau has no opportunity: True or False?
True (0.9399133323582882)
Sally Horvats is guilty: True or False?
True (0.8665847814067802)
Sally Horvats is not guilty: True or False?
True (0.9559813152103319)
Sally Horvats has mean: True or False?
True (0.94519740270931)
Sally Horvats has no mean: True or False?
True (0.918480215734292)
Sally Horvats has motive: True or False?
True (0.9489172681310486)
Sally Horvats has no motive: True or False?
True (0.941654207327861)
Sally Horvats has opportunity: True or False?
True (0.9284088027271398)
Sally Horvats has no opportunity: True or False?
True (0.9184802773231918)
Sam Wheeler is guilty: True or False?
True (0.816406362162552)
Sam Wheeler is not guilty: True or False?
True (0.8914335992201801)
Sam Wheeler has mean: True or False?
True (0.8643104392003704)
Sam Wheeler has no mean: True or False?
True (0.8879840376027315)
Sam Wheeler has motive: True or False?
True (0.9319595674053855)
Sam Wheeler has no motive: True or False?
True (0.9193533657123177)
Sam Wheeler has opportunity: True or False?
True (0.9257686153543061)
Sam Wheeler has no opportunity: True or False?
True (0.9046505665674094)
### Antoine
- mean: True (0.7799928701983835)
- motive: False (0.1347758764556123)
- opportunity: True (0.8679338697256817)

### Georges Monceau
- mean: True (0.7287483223557857)
- motive: True (0.921357630313903)
- opportunity: True (0.8984105603938967)

### Sally Horvats
- mean: False (0.08151978426570805)
- motive: False (0.05834579267213902)
- opportunity: False (0.08151972267680818)

### Sam Wheeler
- mean: True (0.8643104392003704)
- motive: False (0.08064663428768226)
- opportunity: False (0.09534943343259061)

The culprit is Georges Monceau.
In fact, it is Sally Horvats.
## 5minutemystery-the-potter-book-mystery
Alfred is guilty: True or False?
True (0.9485372300670596)
Alfred is not guilty: True or False?
True (0.9489172681310486)
Alfred has mean: True or False?
True (0.8255897087847518)
Alfred has no mean: True or False?
True (0.7534666630720156)
Alfred has motive: True or False?
True (0.9718859797630299)
Alfred has no motive: True or False?
True (0.9252299659402181)
Alfred has opportunity: True or False?
True (0.9422947179693436)
Alfred has no opportunity: True or False?
True (0.8474634858439474)
Ann is guilty: True or False?
True (0.9479621664653681)
Ann is not guilty: True or False?
True (0.9751071938949272)
Ann has mean: True or False?
True (0.9102267057681164)
Ann has no mean: True or False?
True (0.8278281049441929)
Ann has motive: True or False?
True (0.9545627850600183)
Ann has no motive: True or False?
True (0.893681109060862)
Ann has opportunity: True or False?
True (0.9580694433457548)
Ann has no opportunity: True or False?
True (0.8610715240899957)
Rusty is guilty: True or False?
True (0.9584600345758558)
Rusty is not guilty: True or False?
True (0.9697281117313339)
Rusty has mean: True or False?
True (0.7931059536445917)
Rusty has no mean: True or False?
True (0.7898827724330132)
Rusty has motive: True or False?
True (0.9646558768023054)
Rusty has no motive: True or False?
True (0.9105454073245608)
Rusty has opportunity: True or False?
True (0.8940516749601143)
Rusty has no opportunity: True or False?
True (0.7806625377756776)
Uncle Ezra is guilty: True or False?
True (0.7988152492192591)
Uncle Ezra is not guilty: True or False?
True (0.9336731438527403)
Uncle Ezra has mean: True or False?
True (0.7969253675907205)
Uncle Ezra has no mean: True or False?
True (0.7318258918270596)
Uncle Ezra has motive: True or False?
True (0.9308364374248909)
Uncle Ezra has no motive: True or False?
True (0.685107355950278)
Uncle Ezra has opportunity: True or False?
True (0.8860265005470086)
Uncle Ezra has no opportunity: True or False?
False (0.5389832197022594)
### Alfred
- mean: False (0.2465333369279844)
- motive: False (0.07477003405978189)
- opportunity: False (0.15253651415605263)

### Ann
- mean: False (0.1721718950558071)
- motive: False (0.10631889093913804)
- opportunity: False (0.13892847591000435)

### Rusty
- mean: True (0.7931059536445917)
- motive: True (0.9646558768023054)
- opportunity: True (0.8940516749601143)

### Uncle Ezra
- mean: False (0.2681741081729404)
- motive: False (0.31489264404972195)
- opportunity: True (0.8860265005470086)

The culprit is Rusty.
In fact, it is Uncle Ezra.
## 5minutemystery-death-in-the-office
Cynthia Peck is guilty: True or False?
True (0.9489645957880718)
Cynthia Peck is not guilty: True or False?
True (0.9707571866101593)
Cynthia Peck has mean: True or False?
True (0.9305845477606799)
Cynthia Peck has no mean: True or False?
True (0.9032942081209032)
Cynthia Peck has motive: True or False?
True (0.9508691427698753)
Cynthia Peck has no motive: True or False?
True (0.8423451152856819)
Cynthia Peck has opportunity: True or False?
True (0.8774768149941248)
Cynthia Peck has no opportunity: True or False?
True (0.6951311179371613)
Josh Kesler is guilty: True or False?
True (0.9554855815192022)
Josh Kesler is not guilty: True or False?
True (0.9612438076473231)
Josh Kesler has mean: True or False?
True (0.9465966236120936)
Josh Kesler has no mean: True or False?
True (0.9187722208906307)
Josh Kesler has motive: True or False?
True (0.9455001349615358)
Josh Kesler has no motive: True or False?
True (0.9049869771631355)
Josh Kesler has opportunity: True or False?
True (0.927099763868178)
Josh Kesler has no opportunity: True or False?
True (0.8484706263347676)
Megan Brewer is guilty: True or False?
True (0.8000678954040312)
Megan Brewer is not guilty: True or False?
True (0.9304582506719414)
Megan Brewer has mean: True or False?
True (0.861071588244826)
Megan Brewer has no mean: True or False?
True (0.7416740115009234)
Megan Brewer has motive: True or False?
True (0.8019357965963964)
Megan Brewer has no motive: True or False?
True (0.6723316913929156)
Megan Brewer has opportunity: True or False?
True (0.7725306828324007)
Megan Brewer has no opportunity: True or False?
True (0.5698526542706361)
Steve Ledbetter is guilty: True or False?
True (0.9183339469066092)
Steve Ledbetter is not guilty: True or False?
True (0.9532750830575984)
Steve Ledbetter has mean: True or False?
True (0.9643886093607492)
Steve Ledbetter has no mean: True or False?
True (0.9102267057681164)
Steve Ledbetter has motive: True or False?
True (0.9008791478232747)
Steve Ledbetter has no motive: True or False?
True (0.8895288123486662)
Steve Ledbetter has opportunity: True or False?
True (0.9189178954169608)
Steve Ledbetter has no opportunity: True or False?
True (0.7898827135821628)
### Cynthia Peck
- mean: False (0.09670579187909678)
- motive: False (0.1576548847143181)
- opportunity: False (0.3048688820628387)

### Josh Kesler
- mean: True (0.9465966236120936)
- motive: True (0.9455001349615358)
- opportunity: True (0.927099763868178)

### Megan Brewer
- mean: False (0.2583259884990766)
- motive: False (0.3276683086070844)
- opportunity: False (0.43014734572936386)

### Steve Ledbetter
- mean: False (0.08977329423188363)
- motive: False (0.11047118765133379)
- opportunity: False (0.21011728641783722)

The culprit is Josh Kesler.
In fact, it is Megan Brewer.
## 5minutemystery-chief-inspector-japp-solves-a-case
Alan Harrison is guilty: True or False?
True (0.9558166865608263)
Alan Harrison is not guilty: True or False?
True (0.969090998755152)
Alan Harrison has mean: True or False?
True (0.9304582506719414)
Alan Harrison has no mean: True or False?
True (0.8322366416985943)
Alan Harrison has motive: True or False?
True (0.9564718616162037)
Alan Harrison has no motive: True or False?
True (0.9039745373919651)
Alan Harrison has opportunity: True or False?
True (0.941654147692963)
Alan Harrison has no opportunity: True or False?
True (0.8568122429692968)
Evelyn Johnston is guilty: True or False?

Map:  69%|██████▉   | 140/203 [3:09:51<1:27:51, 83.68s/ examples]
Map:  69%|██████▉   | 141/203 [3:11:24<1:29:27, 86.58s/ examples]
Map:  70%|██████▉   | 142/203 [3:12:15<1:17:11, 75.93s/ examples]True (0.9534487112250288)
Evelyn Johnston is not guilty: True or False?
True (0.9754836557950954)
Evelyn Johnston has mean: True or False?
True (0.9319596298981465)
Evelyn Johnston has no mean: True or False?
True (0.8929365260632085)
Evelyn Johnston has motive: True or False?
True (0.9505947242503305)
Evelyn Johnston has no motive: True or False?
True (0.9155072554665495)
Evelyn Johnston has opportunity: True or False?
True (0.944176853162527)
Evelyn Johnston has no opportunity: True or False?
True (0.8381505623254643)
George Smythe is guilty: True or False?
True (0.9591543064115948)
George Smythe is not guilty: True or False?
True (0.9771974085932558)
George Smythe has mean: True or False?
True (0.9241418261705818)
George Smythe has no mean: True or False?
True (0.8376199551237796)
George Smythe has motive: True or False?
True (0.9603611816439128)
George Smythe has no motive: True or False?
True (0.9181873182746905)
George Smythe has opportunity: True or False?
True (0.9170058945178141)
George Smythe has no opportunity: True or False?
True (0.7931059536445917)
Herbert Grosvenor is guilty: True or False?
True (0.9720985894741414)
Herbert Grosvenor is not guilty: True or False?
True (0.9688561547723137)
Herbert Grosvenor has mean: True or False?
True (0.9331876642092066)
Herbert Grosvenor has no mean: True or False?
True (0.8397339530959691)
Herbert Grosvenor has motive: True or False?
True (0.972727357600667)
Herbert Grosvenor has no motive: True or False?
True (0.9235922667342402)
Herbert Grosvenor has opportunity: True or False?
True (0.9580695040202324)
Herbert Grosvenor has no opportunity: True or False?
True (0.8902942539348153)
### Alan Harrison
- mean: False (0.16776335830140565)
- motive: False (0.0960254626080349)
- opportunity: False (0.1431877570307032)

### Evelyn Johnston
- mean: True (0.9319596298981465)
- motive: True (0.9505947242503305)
- opportunity: True (0.944176853162527)

### George Smythe
- mean: False (0.16238004487622038)
- motive: False (0.08181268172530953)
- opportunity: False (0.2068940463554083)

### Herbert Grosvenor
- mean: False (0.1602660469040309)
- motive: False (0.07640773326575978)
- opportunity: False (0.10970574606518468)

The culprit is Evelyn Johnston.
In fact, it is Alan Harrison.
## 5minutemystery-who-stole-the-cavemans-dinner
Dinosaur is guilty: True or False?
True (0.8665847814067802)
Dinosaur is not guilty: True or False?
True (0.8464508054137014)
Dinosaur has mean: True or False?
False (0.5602526707659626)
Dinosaur has no mean: True or False?
True (0.6306849143569856)
Dinosaur has motive: True or False?
True (0.8294919722593475)
Dinosaur has no motive: True or False?
True (0.6901415551283886)
Dinosaur has opportunity: True or False?
True (0.811078188867804)
Dinosaur has no opportunity: True or False?
True (0.673191669892235)
Droo is guilty: True or False?
True (0.9390248079664695)
Droo is not guilty: True or False?
True (0.9032942081209032)
Droo has mean: True or False?
True (0.7725306828324007)
Droo has no mean: True or False?
True (0.7606506318580792)
Droo has motive: True or False?
True (0.9650533199435419)
Droo has no motive: True or False?
True (0.9086179121100144)
Droo has opportunity: True or False?
True (0.9309620852900756)
Droo has no opportunity: True or False?
True (0.9102267057681164)
Father is guilty: True or False?
True (0.9365176577773374)
Father is not guilty: True or False?
True (0.9102267057681164)
Father has mean: True or False?
True (0.8261514850267767)
Father has no mean: True or False?
True (0.7683857617837733)
Father has motive: True or False?
True (0.935346481802689)
Father has no motive: True or False?
True (0.8181563669811865)
Father has opportunity: True or False?
True (0.9307105568817887)
Father has no opportunity: True or False?
True (0.7371581892031299)
Monkeys is guilty: True or False?
True (0.9066531077351827)
Monkeys is not guilty: True or False?
True (0.9230391966311572)
Monkeys has mean: True or False?
True (0.8338664756137771)
Monkeys has no mean: True or False?
True (0.8261514850267767)
Monkeys has motive: True or False?
True (0.9515939960119401)
Monkeys has no motive: True or False?
True (0.7318258918270596)
Monkeys has opportunity: True or False?
True (0.9365176577773374)
Monkeys has no opportunity: True or False?
True (0.8558511727823209)
### Dinosaur
- mean: False (0.5602526707659626)
- motive: False (0.3098584448716114)
- opportunity: False (0.326808330107765)

### Droo
- mean: True (0.7725306828324007)
- motive: True (0.9650533199435419)
- opportunity: True (0.9309620852900756)

### Father
- mean: False (0.23161423821622673)
- motive: False (0.18184363301881346)
- opportunity: False (0.2628418107968701)

### Monkeys
- mean: False (0.1738485149732233)
- motive: False (0.2681741081729404)
- opportunity: False (0.14414882721767908)

The culprit is Droo.
In fact, it is Dinosaur.
## 5minutemystery-the-stolen-car-mystery
David Kelly is guilty: True or False?
True (0.928538502080124)
David Kelly is not guilty: True or False?
True (0.8587185689177256)
David Kelly has mean: True or False?
True (0.9020932932190145)
David Kelly has no mean: True or False?
True (0.6020615685826383)
David Kelly has motive: True or False?
True (0.9814889431064477)
David Kelly has no motive: True or False?
True (0.8402590129647053)
David Kelly has opportunity: True or False?
True (0.9566341655109778)
David Kelly has no opportunity: True or False?
True (0.7879311977554747)
Donna Allen is guilty: True or False?
True (0.9656412588860065)
Donna Allen is not guilty: True or False?
True (0.8692713407917644)
Donna Allen has mean: True or False?
True (0.9286680258169302)
Donna Allen has no mean: True or False?
True (0.6433292707767855)
Donna Allen has motive: True or False?
True (0.9806919106398481)
Donna Allen has no motive: True or False?
True (0.8175744430556572)
Donna Allen has opportunity: True or False?
True (0.9597620378565557)
Donna Allen has no opportunity: True or False?
True (0.8697145551802641)
Larry Roberts is guilty: True or False?
True (0.9268353022276509)
Larry Roberts is not guilty: True or False?
True (0.794384956668203)
Larry Roberts has mean: True or False?
True (0.8489722037469682)
Larry Roberts has no mean: True or False?
False (0.5448014304301324)
Larry Roberts has motive: True or False?
True (0.9680204387474981)
Larry Roberts has no motive: True or False?
True (0.8683809699466569)
Larry Roberts has opportunity: True or False?
True (0.9498557456415421)
Larry Roberts has no opportunity: True or False?
True (0.802555560073231)
Nancy Lee is guilty: True or False?
True (0.9626730694627891)
Nancy Lee is not guilty: True or False?
True (0.8539127714046447)
Nancy Lee has mean: True or False?
True (0.913058338092082)
Nancy Lee has no mean: True or False?
True (0.5048826258478675)
Nancy Lee has motive: True or False?
True (0.9822196365979101)
Nancy Lee has no motive: True or False?
True (0.8558511727823209)
Nancy Lee has opportunity: True or False?
True (0.9224823751318276)
Nancy Lee has no opportunity: True or False?
True (0.7490872087035162)
### David Kelly
- mean: False (0.39793843141736174)
- motive: False (0.1597409870352947)
- opportunity: False (0.2120688022445253)

### Donna Allen
- mean: False (0.3566707292232145)
- motive: False (0.18242555694434281)
- opportunity: False (0.13028544481973592)

### Larry Roberts
- mean: True (0.8489722037469682)
- motive: True (0.9680204387474981)
- opportunity: True (0.9498557456415421)

### Nancy Lee
- mean: False (0.49511737415213253)
- motive: False (0.14414882721767908)
- opportunity: False (0.2509127912964838)

The culprit is Larry Roberts.
In fact, it is Donna Allen.
## 5minutemystery-the-straw-hat-theater-mysteriesfinal-curtain
Arthur Glendon is guilty: True or False?
True (0.8727817583545995)
Arthur Glendon is not guilty: True or False?
True (0.8714749214913714)
Arthur Glendon has mean: True or False?
True (0.8620035048683017)
Arthur Glendon has no mean: True or False?
True (0.927887794449634)
Arthur Glendon has motive: True or False?
True (0.8762113474663927)
Arthur Glendon has no motive: True or False?
True (0.8568122940392877)
Arthur Glendon has opportunity: True or False?
True (0.9625325207646147)

Map:  70%|███████   | 143/203 [3:14:23<1:31:23, 91.40s/ examples]
Map:  71%|███████   | 144/203 [3:15:22<1:20:29, 81.86s/ examples]Arthur Glendon has no opportunity: True or False?
True (0.8984105603938967)
Josh Whitehead is guilty: True or False?
True (0.854884620116169)
Josh Whitehead is not guilty: True or False?
True (0.9089416847784234)
Josh Whitehead has mean: True or False?
True (0.9294403817764149)
Josh Whitehead has no mean: True or False?
True (0.9516839395409852)
Josh Whitehead has motive: True or False?
True (0.908941745727715)
Josh Whitehead has no motive: True or False?
True (0.8705972382426559)
Josh Whitehead has opportunity: True or False?
True (0.9460011122282159)
Josh Whitehead has no opportunity: True or False?
True (0.9008791478232747)
Linda Eberlie is guilty: True or False?
True (0.9286680258169302)
Linda Eberlie is not guilty: True or False?
True (0.9390248079664695)
Linda Eberlie has mean: True or False?
True (0.9036349079321685)
Linda Eberlie has no mean: True or False?
True (0.9360515445140636)
Linda Eberlie has motive: True or False?
True (0.9241418261705818)
Linda Eberlie has no motive: True or False?
True (0.8652241235443877)
Linda Eberlie has opportunity: True or False?
True (0.958847105894029)
Linda Eberlie has no opportunity: True or False?
True (0.9181872635464632)
Sam Watson is guilty: True or False?
True (0.9281487460975983)
Sam Watson is not guilty: True or False?
True (0.9463988549853353)
Sam Watson has mean: True or False?
True (0.9291837815043049)
Sam Watson has no mean: True or False?
True (0.970126867648015)
Sam Watson has motive: True or False?
True (0.9365176577773374)
Sam Watson has no motive: True or False?
True (0.8891444205417208)
Sam Watson has opportunity: True or False?
True (0.9716717007848752)
Sam Watson has no opportunity: True or False?
True (0.9539660824292815)
Stella Marlowe is guilty: True or False?
True (0.8305940642606888)
Stella Marlowe is not guilty: True or False?
True (0.9260365949489886)
Stella Marlowe has mean: True or False?
True (0.9216401608061056)
Stella Marlowe has no mean: True or False?
True (0.9563089618154458)
Stella Marlowe has motive: True or False?
True (0.8499711693725173)
Stella Marlowe has no motive: True or False?
True (0.7898827135821628)
Stella Marlowe has opportunity: True or False?
True (0.9561454058699453)
Stella Marlowe has no opportunity: True or False?
True (0.9170058398600052)
### Arthur Glendon
- mean: True (0.8620035048683017)
- motive: False (0.14318770596071229)
- opportunity: False (0.10158943960610334)

### Josh Whitehead
- mean: True (0.9294403817764149)
- motive: False (0.1294027617573441)
- opportunity: False (0.09912085217672528)

### Linda Eberlie
- mean: True (0.9036349079321685)
- motive: False (0.1347758764556123)
- opportunity: False (0.08181273645353682)

### Sam Watson
- mean: True (0.9291837815043049)
- motive: True (0.9365176577773374)
- opportunity: True (0.9716717007848752)

### Stella Marlowe
- mean: True (0.9216401608061056)
- motive: False (0.21011728641783722)
- opportunity: False (0.08299416013999483)

The culprit is Sam Watson.
In fact, it is Linda Eberlie.
## 5minutemystery-itheft
Lea Thompson is guilty: True or False?
True (0.9374402785760423)
Lea Thompson is not guilty: True or False?
True (0.945399343748748)
Lea Thompson has mean: True or False?
True (0.8677098176365254)
Lea Thompson has no mean: True or False?
True (0.8714748565614324)
Lea Thompson has motive: True or False?
True (0.9639160647221925)
Lea Thompson has no motive: True or False?
True (0.9246876822649571)
Lea Thompson has opportunity: True or False?
True (0.9546474221708894)
Lea Thompson has no opportunity: True or False?
True (0.8006920257960423)
Rachel Vermeer is guilty: True or False?
True (0.9008791478232747)
Rachel Vermeer is not guilty: True or False?
True (0.9307105568817887)
Rachel Vermeer has mean: True or False?
True (0.8969755785184792)
Rachel Vermeer has no mean: True or False?
True (0.8984105603938967)
Rachel Vermeer has motive: True or False?
True (0.9702962635848237)
Rachel Vermeer has no motive: True or False?
True (0.9525741334779666)
Rachel Vermeer has opportunity: True or False?
True (0.9281487460975983)
Rachel Vermeer has no opportunity: True or False?
True (0.8233283740192667)
Shawn Ramos is guilty: True or False?
True (0.9099070446252667)
Shawn Ramos is not guilty: True or False?
True (0.9476724283199579)
Shawn Ramos has mean: True or False?
True (0.8539127714046447)
Shawn Ramos has no mean: True or False?
True (0.8244619332958376)
Shawn Ramos has motive: True or False?
True (0.9808025352018944)
Shawn Ramos has no motive: True or False?
True (0.916109562167414)
Shawn Ramos has opportunity: True or False?
True (0.9435559526996434)
Shawn Ramos has no opportunity: True or False?
True (0.7256486384635821)
Shay Dulaney is guilty: True or False?
True (0.9281487460975983)
Shay Dulaney is not guilty: True or False?
True (0.9511422515416323)
Shay Dulaney has mean: True or False?
True (0.823044124016779)
Shay Dulaney has no mean: True or False?
True (0.8267117710471246)
Shay Dulaney has motive: True or False?
True (0.9558166865608263)
Shay Dulaney has no motive: True or False?
True (0.8895288719962232)
Shay Dulaney has opportunity: True or False?
True (0.9044818892710186)
Shay Dulaney has no opportunity: True or False?
True (0.7988153087356352)
### Lea Thompson
- mean: True (0.8677098176365254)
- motive: False (0.07531231773504288)
- opportunity: False (0.19930797420395774)

### Rachel Vermeer
- mean: True (0.8969755785184792)
- motive: True (0.9702962635848237)
- opportunity: True (0.9281487460975983)

### Shawn Ramos
- mean: False (0.1755380667041624)
- motive: False (0.08389043783258598)
- opportunity: False (0.2743513615364179)

### Shay Dulaney
- mean: True (0.823044124016779)
- motive: False (0.11047112800377679)
- opportunity: False (0.20118469126436478)

The culprit is Rachel Vermeer.
In fact, it is Rachel Vermeer.
## 5minutemystery-the-punch-with-a-punch
Carole is guilty: True or False?
True (0.7446563307563252)
Carole is not guilty: True or False?
True (0.8098781635062345)
Carole has mean: True or False?
False (0.5341265295318852)
Carole has no mean: True or False?
False (0.7122321792841629)
Carole has motive: True or False?
True (0.8705972382426559)
Carole has no motive: True or False?
True (0.7130321332210621)
Carole has opportunity: True or False?
True (0.8098781635062345)
Carole has no opportunity: True or False?
True (0.6834194581047349)
Dan is guilty: True or False?
True (0.6901415551283886)
Dan is not guilty: True or False?
True (0.8692713407917644)
Dan has mean: True or False?
True (0.6113819501087365)
Dan has no mean: True or False?
False (0.6592954931819778)
Dan has motive: True or False?
True (0.9319595674053855)
Dan has no motive: True or False?
True (0.8370879250561812)
Dan has opportunity: True or False?
True (0.8947895144283036)
Dan has no opportunity: True or False?
True (0.7185944237486072)
Diane is guilty: True or False?
True (0.7620701143808404)
Diane is not guilty: True or False?
True (0.873646672673131)
Diane has mean: True or False?
True (0.5292634408007735)
Diane has no mean: True or False?
False (0.6706082735718226)
Diane has motive: True or False?
True (0.9136765013387816)
Diane has no motive: True or False?
True (0.8683809699466569)
Diane has opportunity: True or False?
True (0.8104789202520752)
Diane has no opportunity: True or False?
True (0.8887587777822111)
Principal Whittenmeyer is guilty: True or False?
True (0.8204694405411458)
Principal Whittenmeyer is not guilty: True or False?
True (0.6967842494573921)
Principal Whittenmeyer has mean: True or False?
True (0.49999999904767284)
Principal Whittenmeyer has no mean: True or False?
False (0.6325027218909103)
Principal Whittenmeyer has motive: True or False?
True (0.9376689781587124)
Principal Whittenmeyer has no motive: True or False?
True (0.6504672743423094)
Principal Whittenmeyer has opportunity: True or False?
True (0.8272706865691472)
Principal Whittenmeyer has no opportunity: True or False?
False (0.5755879969637064)
### Carole
- mean: False (0.5341265295318852)
- motive: False (0.28696786677893793)
- opportunity: False (0.3165805418952651)

### Dan
- mean: True (0.6113819501087365)
- motive: False (0.16291207494381876)
- opportunity: False (0.28140557625139284)

### Diane

Map:  71%|███████▏  | 145/203 [3:16:27<1:14:00, 76.57s/ examples]
Map:  72%|███████▏  | 146/203 [3:17:39<1:11:32, 75.31s/ examples]
Map:  72%|███████▏  | 147/203 [3:19:12<1:15:14, 80.61s/ examples]- mean: True (0.5292634408007735)
- motive: True (0.9136765013387816)
- opportunity: True (0.8104789202520752)

### Principal Whittenmeyer
- mean: True (0.49999999904767284)
- motive: False (0.34953272565769056)
- opportunity: True (0.8272706865691472)

The culprit is Diane.
In fact, it is Carole.
## 5minutemystery-the-straw-hat-theater-mysteriesbox-office-nightmare
Basil Carmody is guilty: True or False?
True (0.9822537304185777)
Basil Carmody is not guilty: True or False?
True (0.9678385252143537)
Basil Carmody has mean: True or False?
True (0.9687380774673213)
Basil Carmody has no mean: True or False?
True (0.9073122118500465)
Basil Carmody has motive: True or False?
True (0.990550875800996)
Basil Carmody has no motive: True or False?
True (0.9690910565174785)
Basil Carmody has opportunity: True or False?
True (0.9768465751854355)
Basil Carmody has no opportunity: True or False?
True (0.8787311338092536)
John Franklin is guilty: True or False?
True (0.9831822505619944)
John Franklin is not guilty: True or False?
True (0.9768465751854355)
John Franklin has mean: True or False?
True (0.9718859797630299)
John Franklin has no mean: True or False?
True (0.9443823686645129)
John Franklin has motive: True or False?
True (0.9903663396202808)
John Franklin has no motive: True or False?
True (0.9644556034131689)
John Franklin has opportunity: True or False?
True (0.970126867648015)
John Franklin has no opportunity: True or False?
True (0.8647679145346777)
Lawrence Blake is guilty: True or False?
True (0.9693822259947317)
Lawrence Blake is not guilty: True or False?
True (0.9696707123138633)
Lawrence Blake has mean: True or False?
True (0.9331876642092066)
Lawrence Blake has no mean: True or False?
True (0.9309620852900756)
Lawrence Blake has motive: True or False?
True (0.9897513984446356)
Lawrence Blake has no motive: True or False?
True (0.9711291201201401)
Lawrence Blake has opportunity: True or False?
True (0.9537942396657707)
Lawrence Blake has no opportunity: True or False?
True (0.8820219652716884)
Martha Gilmont is guilty: True or False?
True (0.9686788908454032)
Martha Gilmont is not guilty: True or False?
True (0.96920782287766)
Martha Gilmont has mean: True or False?
True (0.9671630869492336)
Martha Gilmont has no mean: True or False?
True (0.9449946880768697)
Martha Gilmont has motive: True or False?
True (0.9879926447379697)
Martha Gilmont has no motive: True or False?
True (0.9698997143273816)
Martha Gilmont has opportunity: True or False?
True (0.9746286873974596)
Martha Gilmont has no opportunity: True or False?
True (0.861071588244826)
### Basil Carmody
- mean: False (0.09268778814995349)
- motive: False (0.03090894348252149)
- opportunity: False (0.1212688661907464)

### John Franklin
- mean: False (0.05561763133548714)
- motive: False (0.03554439658683106)
- opportunity: False (0.13523208546532228)

### Lawrence Blake
- mean: True (0.9331876642092066)
- motive: True (0.9897513984446356)
- opportunity: True (0.9537942396657707)

### Martha Gilmont
- mean: False (0.055005311923130296)
- motive: False (0.030100285672618354)
- opportunity: False (0.138928411755174)

The culprit is Lawrence Blake.
In fact, it is John Franklin.
## 5minutemystery-the-waffle-man-mystery
Larry is guilty: True or False?
True (0.9538802513450514)
Larry is not guilty: True or False?
True (0.9703524709836886)
Larry has mean: True or False?
True (0.9103862053899627)
Larry has no mean: True or False?
True (0.8947894610946939)
Larry has motive: True or False?
True (0.9638480560973683)
Larry has no motive: True or False?
True (0.9744347924514057)
Larry has opportunity: True or False?
True (0.9291837815043049)
Larry has no opportunity: True or False?
True (0.8294919722593475)
The Old Man is guilty: True or False?
True (0.9469901928615181)
The Old Man is not guilty: True or False?
True (0.9660279734605501)
The Old Man has mean: True or False?
True (0.9309620852900756)
The Old Man has no mean: True or False?
True (0.9534487112250288)
The Old Man has motive: True or False?
True (0.9799189575826882)
The Old Man has no motive: True or False?
True (0.9473810211532727)
The Old Man has opportunity: True or False?
True (0.9567151656221777)
The Old Man has no opportunity: True or False?
True (0.8568122940392877)
The Waffle Man is guilty: True or False?
True (0.9361683754137716)
The Waffle Man is not guilty: True or False?
True (0.957833409455459)
The Waffle Man has mean: True or False?
True (0.9097467681279717)
The Waffle Man has no mean: True or False?
True (0.94620036983)
The Waffle Man has motive: True or False?
True (0.9722307324426623)
The Waffle Man has no motive: True or False?
True (0.9592307208025933)
The Waffle Man has opportunity: True or False?
True (0.9523087127556139)
The Waffle Man has no opportunity: True or False?
True (0.8529354946829077)
Vera is guilty: True or False?
True (0.9649873987772907)
Vera is not guilty: True or False?
True (0.9825239779274779)
Vera has mean: True or False?
True (0.8774768149941248)
Vera has no mean: True or False?
True (0.9392480858026054)
Vera has motive: True or False?
True (0.9779255993272387)
Vera has no motive: True or False?
True (0.9805061218995585)
Vera has opportunity: True or False?
True (0.9566342225308191)
Vera has no opportunity: True or False?
True (0.9353465445225602)
### Larry
- mean: False (0.10521053890530607)
- motive: True (0.9638480560973683)
- opportunity: False (0.17050802774065255)

### The Old Man
- mean: True (0.9309620852900756)
- motive: False (0.05261897884672728)
- opportunity: False (0.14318770596071229)

### The Waffle Man
- mean: True (0.9097467681279717)
- motive: False (0.040769279197406694)
- opportunity: False (0.14706450531709225)

### Vera
- mean: True (0.8774768149941248)
- motive: True (0.9779255993272387)
- opportunity: True (0.9566342225308191)

The culprit is Vera.
In fact, it is Vera.
## 5minutemystery-the-sunday-school-tithe-mystery
Doc Bentson is guilty: True or False?
True (0.950777887812089)
Doc Bentson is not guilty: True or False?
True (0.8852351930010195)
Doc Bentson has mean: True or False?
True (0.8402589628813668)
Doc Bentson has no mean: True or False?
False (0.5350984235603058)
Doc Bentson has motive: True or False?
True (0.9716178782667568)
Doc Bentson has no motive: True or False?
True (0.9167080509980843)
Doc Bentson has opportunity: True or False?
True (0.9324533354081785)
Doc Bentson has no opportunity: True or False?
True (0.9056565771882901)
Ellie Wilson is guilty: True or False?
True (0.9541373270174538)
Ellie Wilson is not guilty: True or False?
True (0.9494823209990744)
Ellie Wilson has mean: True or False?
True (0.8344069148356309)
Ellie Wilson has no mean: True or False?
True (0.5736783792247284)
Ellie Wilson has motive: True or False?
True (0.9742884034320242)
Ellie Wilson has no motive: True or False?
True (0.8980534699860239)
Ellie Wilson has opportunity: True or False?
True (0.927099763868178)
Ellie Wilson has no opportunity: True or False?
True (0.8300437258865985)
James Gant is guilty: True or False?
True (0.9515039936355008)
James Gant is not guilty: True or False?
True (0.884439109617765)
James Gant has mean: True or False?
True (0.8221890958162477)
James Gant has no mean: True or False?
True (0.5068355091660127)
James Gant has motive: True or False?
True (0.982287646116634)
James Gant has no motive: True or False?
True (0.9385759849623091)
James Gant has opportunity: True or False?
True (0.9082930095862076)
James Gant has no opportunity: True or False?
True (0.8787311338092536)
Judy Gant is guilty: True or False?
True (0.9369805475192257)
Judy Gant is not guilty: True or False?
True (0.9136765013387816)
Judy Gant has mean: True or False?
True (0.6662796746479285)
Judy Gant has no mean: True or False?
True (0.7025300310583819)
Judy Gant has motive: True or False?
True (0.9586927300380139)
Judy Gant has no motive: True or False?
True (0.9069831945855868)
Judy Gant has opportunity: True or False?
True (0.9543079730970608)
Judy Gant has no opportunity: True or False?
True (0.9108631007029255)
Waylon Marsh is guilty: True or False?
True (0.966851473631521)
Waylon Marsh is not guilty: True or False?
True (0.9492946258008691)

Map:  73%|███████▎  | 148/203 [3:20:32<1:13:48, 80.51s/ examples]
Map:  73%|███████▎  | 149/203 [3:21:44<1:10:10, 77.97s/ examples]
Map:  74%|███████▍  | 150/203 [3:22:35<1:01:31, 69.66s/ examples]Waylon Marsh has mean: True or False?
True (0.9012274173198201)
Waylon Marsh has no mean: True or False?
True (0.7146280500737092)
Waylon Marsh has motive: True or False?
True (0.9863368269753094)
Waylon Marsh has no motive: True or False?
True (0.9378969089655451)
Waylon Marsh has opportunity: True or False?
True (0.952397347230678)
Waylon Marsh has no opportunity: True or False?
True (0.8568122940392877)
### Doc Bentson
- mean: True (0.8402589628813668)
- motive: True (0.9716178782667568)
- opportunity: True (0.9324533354081785)

### Ellie Wilson
- mean: False (0.4263216207752716)
- motive: False (0.10194653001397613)
- opportunity: False (0.16995627411340153)

### James Gant
- mean: False (0.4931644908339873)
- motive: False (0.061424015037690904)
- opportunity: False (0.1212688661907464)

### Judy Gant
- mean: True (0.6662796746479285)
- motive: False (0.09301680541441315)
- opportunity: False (0.08913689929707447)

### Waylon Marsh
- mean: False (0.2853719499262908)
- motive: False (0.06210309103445488)
- opportunity: False (0.14318770596071229)

The culprit is Doc Bentson.
In fact, it is Waylon Marsh.
## 5minutemystery-the-straw-hat-theater-mysteriescasting-call
Alice Cartwright is guilty: True or False?
True (0.9427180278987515)
Alice Cartwright is not guilty: True or False?
True (0.9484418035658785)
Alice Cartwright has mean: True or False?
True (0.8037905715242155)
Alice Cartwright has no mean: True or False?
True (0.8300437877296776)
Alice Cartwright has motive: True or False?
True (0.941654147692963)
Alice Cartwright has no motive: True or False?
True (0.8338664756137771)
Alice Cartwright has opportunity: True or False?
True (0.7911763836133219)
Alice Cartwright has no opportunity: True or False?
True (0.7950222460539826)
Arthur Glendon is guilty: True or False?
True (0.9509603391767795)
Arthur Glendon is not guilty: True or False?
True (0.9281486838603771)
Arthur Glendon has mean: True or False?
True (0.8940516749601143)
Arthur Glendon has no mean: True or False?
True (0.8050197341926492)
Arthur Glendon has motive: True or False?
True (0.9553191057869168)
Arthur Glendon has no motive: True or False?
True (0.7718434926244166)
Arthur Glendon has opportunity: True or False?
True (0.8428631416381634)
Arthur Glendon has no opportunity: True or False?
True (0.5669777909748143)
Janice Starling is guilty: True or False?
True (0.9382373082603129)
Janice Starling is not guilty: True or False?
True (0.9621076000160501)
Janice Starling has mean: True or False?
True (0.9032942081209032)
Janice Starling has no mean: True or False?
True (0.8947894610946939)
Janice Starling has motive: True or False?
True (0.9618217364339323)
Janice Starling has no motive: True or False?
True (0.7994422859301654)
Janice Starling has opportunity: True or False?
True (0.776622945813876)
Janice Starling has no opportunity: True or False?
True (0.6627964974378784)
Sandra Buckingham is guilty: True or False?
True (0.9693242313725606)
Sandra Buckingham is not guilty: True or False?
True (0.9471859926317535)
Sandra Buckingham has mean: True or False?
True (0.866132552869269)
Sandra Buckingham has no mean: True or False?
True (0.7885832152749314)
Sandra Buckingham has motive: True or False?
True (0.9548162813994148)
Sandra Buckingham has no motive: True or False?
True (0.7272012283179254)
Sandra Buckingham has opportunity: True or False?
True (0.8140527631337082)
Sandra Buckingham has no opportunity: True or False?
False (0.5009765603034438)
### Alice Cartwright
- mean: True (0.8037905715242155)
- motive: True (0.941654147692963)
- opportunity: True (0.7911763836133219)

### Arthur Glendon
- mean: False (0.19498026580735084)
- motive: False (0.22815650737558335)
- opportunity: False (0.43302220902518573)

### Janice Starling
- mean: False (0.10521053890530607)
- motive: False (0.20055771406983458)
- opportunity: False (0.3372035025621216)

### Sandra Buckingham
- mean: False (0.21141678472506864)
- motive: False (0.27279877168207456)
- opportunity: True (0.8140527631337082)

The culprit is Alice Cartwright.
In fact, it is Arthur Glendon.
## 5minutemystery-the-anonymous-bank-robber
Edward Cantrell is guilty: True or False?
True (0.9886682030396517)
Edward Cantrell is not guilty: True or False?
True (0.9876638653948571)
Edward Cantrell has mean: True or False?
True (0.9520419225082909)
Edward Cantrell has no mean: True or False?
True (0.9744347924514057)
Edward Cantrell has motive: True or False?
True (0.9939613341638746)
Edward Cantrell has no motive: True or False?
True (0.9889278415048399)
Edward Cantrell has opportunity: True or False?
True (0.9811668987645739)
Edward Cantrell has no opportunity: True or False?
True (0.9602121708473209)
Larry Brooks is guilty: True or False?
True (0.9690910565174785)
Larry Brooks is not guilty: True or False?
True (0.9730364677532105)
Larry Brooks has mean: True or False?
True (0.8181563669811865)
Larry Brooks has no mean: True or False?
True (0.9309620852900756)
Larry Brooks has motive: True or False?
True (0.9872034791669495)
Larry Brooks has no motive: True or False?
True (0.9561454664225738)
Larry Brooks has opportunity: True or False?
True (0.9715639953911919)
Larry Brooks has no opportunity: True or False?
True (0.9139841191734227)
Lester Barton is guilty: True or False?
True (0.9908919928962941)
Lester Barton is not guilty: True or False?
True (0.981453479162328)
Lester Barton has mean: True or False?
True (0.9603611244019274)
Lester Barton has no mean: True or False?
True (0.94519740270931)
Lester Barton has motive: True or False?
True (0.9967428446694364)
Lester Barton has no motive: True or False?
True (0.9811668402824711)
Lester Barton has opportunity: True or False?
True (0.9799765346854967)
Lester Barton has no opportunity: True or False?
True (0.9625325207646147)
Oscar Jordan is guilty: True or False?
True (0.9853561522937149)
Oscar Jordan is not guilty: True or False?
True (0.9752018447706344)
Oscar Jordan has mean: True or False?
True (0.8980534699860239)
Oscar Jordan has no mean: True or False?
True (0.9504109622144332)
Oscar Jordan has motive: True or False?
True (0.9949199557758223)
Oscar Jordan has no motive: True or False?
True (0.9655114412719658)
Oscar Jordan has opportunity: True or False?
True (0.9826908710080852)
Oscar Jordan has no opportunity: True or False?
True (0.9175984877579624)
### Edward Cantrell
- mean: True (0.9520419225082909)
- motive: True (0.9939613341638746)
- opportunity: True (0.9811668987645739)

### Larry Brooks
- mean: True (0.8181563669811865)
- motive: False (0.04385453357742619)
- opportunity: False (0.0860158808265773)

### Lester Barton
- mean: False (0.054802597290690036)
- motive: False (0.018833159717528858)
- opportunity: False (0.03746747923538529)

### Oscar Jordan
- mean: True (0.8980534699860239)
- motive: False (0.034488558728034246)
- opportunity: False (0.08240151224203762)

The culprit is Edward Cantrell.
In fact, it is Lester Barton.
## 5minutemystery-the-house-of-lies
Debra is guilty: True or False?
True (0.9463988549853353)
Debra is not guilty: True or False?
True (0.976846635229549)
Debra has mean: True or False?
True (0.948058427656158)
Debra has no mean: True or False?
True (0.7676898810056793)
Debra has motive: True or False?
True (0.9644556034131689)
Debra has no motive: True or False?
True (0.8504686406728537)
Debra has opportunity: True or False?
True (0.8929365260632085)
Debra has no opportunity: True or False?
True (0.6370307821695329)
Luke is guilty: True or False?
True (0.935228290192913)
Luke is not guilty: True or False?
True (0.9671009774598767)
Luke has mean: True or False?
True (0.7772998201448375)
Luke has no mean: True or False?
True (0.6740504382339836)
Luke has motive: True or False?
True (0.9681411371390284)
Luke has no motive: True or False?
True (0.7975568155246964)
Luke has opportunity: True or False?
True (0.9181872635464632)
Luke has no opportunity: True or False?
True (0.7074046739492601)
Olivia is guilty: True or False?
True (0.9362850185952675)
Olivia is not guilty: True or False?
True (0.963368656065788)
Olivia has mean: True or False?
True (0.884837803442546)
Olivia has no mean: True or False?
True (0.7745833916423246)

Map:  74%|███████▍  | 151/203 [3:23:53<1:02:34, 72.20s/ examples]
Map:  75%|███████▍  | 152/203 [3:25:19<1:04:54, 76.36s/ examples]
Map:  75%|███████▌  | 153/203 [3:26:21<1:00:04, 72.09s/ examples]Olivia has motive: True or False?
True (0.9683812262581977)
Olivia has no motive: True or False?
True (0.9246876822649571)
Olivia has opportunity: True or False?
True (0.936749461409047)
Olivia has no opportunity: True or False?
True (0.776622945813876)
The Butler is guilty: True or False?
True (0.9744347924514057)
The Butler is not guilty: True or False?
True (0.981700658375371)
The Butler has mean: True or False?
True (0.9390248639367113)
The Butler has no mean: True or False?
True (0.9410069597342015)
The Butler has motive: True or False?
True (0.9746769070949022)
The Butler has no motive: True or False?
True (0.9152045868398637)
The Butler has opportunity: True or False?
True (0.9509603994010378)
The Butler has no opportunity: True or False?
True (0.85729086409805)
### Debra
- mean: False (0.23231011899432075)
- motive: False (0.14953135932714634)
- opportunity: False (0.3629692178304671)

### Luke
- mean: False (0.3259495617660164)
- motive: False (0.20244318447530363)
- opportunity: False (0.2925953260507399)

### Olivia
- mean: False (0.2254166083576754)
- motive: False (0.07531231773504288)
- opportunity: False (0.22337705418612397)

### The Butler
- mean: True (0.9390248639367113)
- motive: True (0.9746769070949022)
- opportunity: True (0.9509603994010378)

The culprit is The Butler.
In fact, it is The Butler.
## 5minutemystery-the-straw-hat-theater-mysterieson-stage
Grace Upshaw is guilty: True or False?
True (0.9463988549853353)
Grace Upshaw is not guilty: True or False?
True (0.9463988549853353)
Grace Upshaw has mean: True or False?
True (0.8991214023999228)
Grace Upshaw has no mean: True or False?
True (0.65489470935198)
Grace Upshaw has motive: True or False?
True (0.9791157846694846)
Grace Upshaw has no motive: True or False?
True (0.8727817583545995)
Grace Upshaw has opportunity: True or False?
True (0.942081869103903)
Grace Upshaw has no opportunity: True or False?
True (0.7114308541703346)
Linda Grant is guilty: True or False?
True (0.9365176577773374)
Linda Grant is not guilty: True or False?
True (0.9613890640022783)
Linda Grant has mean: True or False?
True (0.8957052808276003)
Linda Grant has no mean: True or False?
True (0.7988152492192591)
Linda Grant has motive: True or False?
True (0.9802052373824002)
Linda Grant has no motive: True or False?
True (0.9372107968415931)
Linda Grant has opportunity: True or False?
True (0.9376689222692878)
Linda Grant has no opportunity: True or False?
True (0.8255897087847518)
Molly Trumbull is guilty: True or False?
True (0.9358173616900589)
Molly Trumbull is not guilty: True or False?
True (0.9385759220258869)
Molly Trumbull has mean: True or False?
True (0.811078188867804)
Molly Trumbull has no mean: True or False?
True (0.6388353131709135)
Molly Trumbull has motive: True or False?
True (0.9615337835163564)
Molly Trumbull has no motive: True or False?
True (0.8529354946829077)
Molly Trumbull has opportunity: True or False?
True (0.9273632783787477)
Molly Trumbull has no opportunity: True or False?
True (0.7690802105138688)
Samantha Powers is guilty: True or False?
True (0.9433475737015985)
Samantha Powers is not guilty: True or False?
True (0.9534487716068757)
Samantha Powers has mean: True or False?
True (0.9181873182746905)
Samantha Powers has no mean: True or False?
True (0.77729988964086)
Samantha Powers has motive: True or False?
True (0.9819446807697475)
Samantha Powers has no motive: True or False?
True (0.908941745727715)
Samantha Powers has opportunity: True or False?
True (0.9574372776306425)
Samantha Powers has no opportunity: True or False?
True (0.7718434926244166)
### Grace Upshaw
- mean: False (0.34510529064802)
- motive: False (0.12721824164540052)
- opportunity: False (0.2885691458296654)

### Linda Grant
- mean: True (0.8957052808276003)
- motive: True (0.9802052373824002)
- opportunity: True (0.9376689222692878)

### Molly Trumbull
- mean: False (0.36116468682908653)
- motive: False (0.14706450531709225)
- opportunity: False (0.23091978948613123)

### Samantha Powers
- mean: False (0.22270011035913995)
- motive: False (0.09105825427228498)
- opportunity: False (0.22815650737558335)

The culprit is Linda Grant.
In fact, it is Grace Upshaw.
## 5minutemystery-canada-day
Little black-haired girl is guilty: True or False?
True (0.9522199623739209)
Little black-haired girl is not guilty: True or False?
True (0.9558166865608263)
Little black-haired girl has mean: True or False?
True (0.9653158197836269)
Little black-haired girl has no mean: True or False?
True (0.8994751578343994)
Little black-haired girl has motive: True or False?
True (0.9688561547723137)
Little black-haired girl has no motive: True or False?
True (0.9071478234767817)
Little black-haired girl has opportunity: True or False?
True (0.9051547640395294)
Little black-haired girl has no opportunity: True or False?
True (0.7348812840309261)
Redheaded woman is guilty: True or False?
True (0.9521309719757854)
Redheaded woman is not guilty: True or False?
True (0.9674102673982512)
Redheaded woman has mean: True or False?
True (0.9612438076473231)
Redheaded woman has no mean: True or False?
True (0.9155072008980665)
Redheaded woman has motive: True or False?
True (0.9583042252239092)
Redheaded woman has no motive: True or False?
True (0.91789335161495)
Redheaded woman has opportunity: True or False?
True (0.8444089912414552)
Redheaded woman has no opportunity: True or False?
True (0.7879311977554747)
Stocky blonde man is guilty: True or False?
True (0.9546474221708894)
Stocky blonde man is not guilty: True or False?
True (0.9474783528129732)
Stocky blonde man has mean: True or False?
True (0.9302051049548884)
Stocky blonde man has no mean: True or False?
True (0.9113376724203427)
Stocky blonde man has motive: True or False?
True (0.9430336353172679)
Stocky blonde man has no motive: True or False?
True (0.9227612010756272)
Stocky blonde man has opportunity: True or False?
True (0.8947894610946939)
Stocky blonde man has no opportunity: True or False?
True (0.8740772565226612)
Tall bald man is guilty: True or False?
True (0.9178934131644976)
Tall bald man is not guilty: True or False?
True (0.9414391533604212)
Tall bald man has mean: True or False?
True (0.8862236142219189)
Tall bald man has no mean: True or False?
True (0.7676898810056793)
Tall bald man has motive: True or False?
True (0.9300782079786175)
Tall bald man has no motive: True or False?
True (0.8879840376027315)
Tall bald man has opportunity: True or False?
True (0.7962924261546153)
Tall bald man has no opportunity: True or False?
True (0.6951311179371613)
### Little black-haired girl
- mean: False (0.10052484216560065)
- motive: False (0.09285217652321831)
- opportunity: False (0.2651187159690739)

### Redheaded woman
- mean: False (0.08449279910193352)
- motive: False (0.08210664838505)
- opportunity: False (0.2120688022445253)

### Stocky blonde man
- mean: True (0.9302051049548884)
- motive: True (0.9430336353172679)
- opportunity: True (0.8947894610946939)

### Tall bald man
- mean: False (0.23231011899432075)
- motive: False (0.11201596239726852)
- opportunity: False (0.3048688820628387)

The culprit is Stocky blonde man.
In fact, it is Tall bald man.
## 5minutemystery-the-missing-communion-set
Allison Jordan is guilty: True or False?
True (0.854884620116169)
Allison Jordan is not guilty: True or False?
True (0.8723474190177988)
Allison Jordan has mean: True or False?
True (0.6723316913929156)
Allison Jordan has no mean: True or False?
True (0.6315942370470465)
Allison Jordan has motive: True or False?
True (0.9196425651151865)
Allison Jordan has no motive: True or False?
True (0.784649255215384)
Allison Jordan has opportunity: True or False?
True (0.7498206607358464)
Allison Jordan has no opportunity: True or False?
True (0.8397339530959691)
Heather Guse is guilty: True or False?
True (0.9119669214647611)
Heather Guse is not guilty: True or False?
True (0.9187722208906307)
Heather Guse has mean: True or False?
True (0.7931058945535956)
Heather Guse has no mean: True or False?
True (0.5784481782924303)
Heather Guse has motive: True or False?
True (0.9616780268435321)
Heather Guse has no motive: True or False?
True (0.7911764307711107)

Map:  76%|███████▌  | 154/203 [3:28:40<1:15:17, 92.18s/ examples]
Map:  76%|███████▋  | 155/203 [3:29:38<1:05:29, 81.86s/ examples]
Map:  77%|███████▋  | 156/203 [3:30:35<58:24, 74.55s/ examples]  Heather Guse has opportunity: True or False?
True (0.8255897087847518)
Heather Guse has no opportunity: True or False?
False (0.5019531141001669)
Janelle Herbst is guilty: True or False?
True (0.8901032777981455)
Janelle Herbst is not guilty: True or False?
True (0.9392480858026054)
Janelle Herbst has mean: True or False?
True (0.8216173055802608)
Janelle Herbst has no mean: True or False?
True (0.6688802232837365)
Janelle Herbst has motive: True or False?
True (0.9702399365512847)
Janelle Herbst has no motive: True or False?
True (0.7697732451157533)
Janelle Herbst has opportunity: True or False?
True (0.875361437979977)
Janelle Herbst has no opportunity: True or False?
True (0.5573635130218721)
Josh Darvin is guilty: True or False?
True (0.9309620852900756)
Josh Darvin is not guilty: True or False?
True (0.9233161821369215)
Josh Darvin has mean: True or False?
True (0.9105454073245608)
Josh Darvin has no mean: True or False?
True (0.7490872087035162)
Josh Darvin has motive: True or False?
True (0.9833749535726279)
Josh Darvin has no motive: True or False?
True (0.8955226517597132)
Josh Darvin has opportunity: True or False?
True (0.9516839395409852)
Josh Darvin has no opportunity: True or False?
True (0.5418937862055231)
Justin Paul is guilty: True or False?
True (0.9543930284832085)
Justin Paul is not guilty: True or False?
True (0.9408984174410038)
Justin Paul has mean: True or False?
True (0.9056565771882901)
Justin Paul has no mean: True or False?
True (0.7416740115009234)
Justin Paul has motive: True or False?
True (0.9907140133328187)
Justin Paul has no motive: True or False?
True (0.9502265454272235)
Justin Paul has opportunity: True or False?
True (0.9443823686645129)
Justin Paul has no opportunity: True or False?
True (0.6370307821695329)
### Allison Jordan
- mean: True (0.6723316913929156)
- motive: True (0.9196425651151865)
- opportunity: True (0.7498206607358464)

### Heather Guse
- mean: False (0.42155182170756966)
- motive: False (0.20882356922888934)
- opportunity: True (0.8255897087847518)

### Janelle Herbst
- mean: False (0.33111977671626347)
- motive: False (0.2302267548842467)
- opportunity: False (0.44263648697812785)

### Josh Darvin
- mean: False (0.2509127912964838)
- motive: False (0.10447734824028676)
- opportunity: False (0.4581062137944769)

### Justin Paul
- mean: False (0.2583259884990766)
- motive: False (0.04977345457277649)
- opportunity: False (0.3629692178304671)

The culprit is Allison Jordan.
In fact, it is Josh Darvin.
## 5minutemystery-who-stole-super-bowl-sunday
Aunt Mary is guilty: True or False?
True (0.9695556166618308)
Aunt Mary is not guilty: True or False?
True (0.9790357346435182)
Aunt Mary has mean: True or False?
True (0.9012274173198201)
Aunt Mary has no mean: True or False?
True (0.8615382357584752)
Aunt Mary has motive: True or False?
True (0.966726063403815)
Aunt Mary has no motive: True or False?
True (0.9709092372014624)
Aunt Mary has opportunity: True or False?
True (0.9365175949789369)
Aunt Mary has no opportunity: True or False?
True (0.9046505665674094)
Phil is guilty: True or False?
True (0.9856353404294369)
Phil is not guilty: True or False?
True (0.9760836361980141)
Phil has mean: True or False?
True (0.9576754579340193)
Phil has no mean: True or False?
True (0.943970619289785)
Phil has motive: True or False?
True (0.9922594430312686)
Phil has no motive: True or False?
True (0.9586927300380139)
Phil has opportunity: True or False?
True (0.9843363767844491)
Phil has no opportunity: True or False?
True (0.9390248079664695)
Rick is guilty: True or False?
True (0.9701269272790862)
Rick is not guilty: True or False?
True (0.9763556123726495)
Rick has mean: True or False?
True (0.8413047772878592)
Rick has no mean: True or False?
True (0.8799743689174987)
Rick has motive: True or False?
True (0.9777987599607383)
Rick has no motive: True or False?
True (0.9492946258008691)
Rick has opportunity: True or False?
True (0.9562272444658398)
Rick has no opportunity: True or False?
True (0.9410069597342015)
Uncle Charlie is guilty: True or False?
True (0.9217811254507657)
Uncle Charlie is not guilty: True or False?
True (0.9695556762577888)
Uncle Charlie has mean: True or False?
True (0.9391365661970741)
Uncle Charlie has no mean: True or False?
True (0.959912598704516)
Uncle Charlie has motive: True or False?
True (0.9843062166752533)
Uncle Charlie has no motive: True or False?
True (0.9715639953911919)
Uncle Charlie has opportunity: True or False?
True (0.9578334701149885)
Uncle Charlie has no opportunity: True or False?
True (0.861538171568877)
### Aunt Mary
- mean: False (0.1384617642415248)
- motive: True (0.966726063403815)
- opportunity: False (0.09534943343259061)

### Phil
- mean: False (0.056029380710215015)
- motive: False (0.04130726996198608)
- opportunity: False (0.06097519203353052)

### Rick
- mean: True (0.8413047772878592)
- motive: True (0.9777987599607383)
- opportunity: True (0.9562272444658398)

### Uncle Charlie
- mean: True (0.9391365661970741)
- motive: False (0.02843600460880813)
- opportunity: False (0.13846182843112298)

The culprit is Rick.
In fact, it is Aunt Mary.
## 5minutemystery-the-cocktail-conundrum
Ian Fairbank is guilty: True or False?
True (0.942612469657282)
Ian Fairbank is not guilty: True or False?
True (0.9461008327071723)
Ian Fairbank has mean: True or False?
True (0.7225270177274575)
Ian Fairbank has no mean: True or False?
False (0.6522414018725713)
Ian Fairbank has motive: True or False?
True (0.9747731684499236)
Ian Fairbank has no motive: True or False?
True (0.879146760693242)
Ian Fairbank has opportunity: True or False?
True (0.8732148436000907)
Ian Fairbank has no opportunity: True or False?
True (0.7025300310583819)
Mr. Fairbank is guilty: True or False?
True (0.8638516611889259)
Mr. Fairbank is not guilty: True or False?
True (0.9220623362560066)
Mr. Fairbank has mean: True or False?
True (0.7439129430200341)
Mr. Fairbank has no mean: True or False?
True (0.615087855649269)
Mr. Fairbank has motive: True or False?
True (0.9796870954125814)
Mr. Fairbank has no motive: True or False?
True (0.9289263523387795)
Mr. Fairbank has opportunity: True or False?
True (0.8019358443954961)
Mr. Fairbank has no opportunity: True or False?
True (0.7704647687904915)
Mr. Lewis Rhys is guilty: True or False?
True (0.8927496657814362)
Mr. Lewis Rhys is not guilty: True or False?
True (0.8637368084632712)
Mr. Lewis Rhys has mean: True or False?
True (0.7033457082786769)
Mr. Lewis Rhys has no mean: True or False?
False (0.525368812147771)
Mr. Lewis Rhys has motive: True or False?
True (0.9458013187522837)
Mr. Lewis Rhys has no motive: True or False?
True (0.8193157928301305)
Mr. Lewis Rhys has opportunity: True or False?
True (0.7512834059294674)
Mr. Lewis Rhys has no opportunity: True or False?
True (0.5097643762740132)
Mrs. Fairbank is guilty: True or False?
True (0.9076401582775206)
Mrs. Fairbank is not guilty: True or False?
True (0.8991213421091365)
Mrs. Fairbank has mean: True or False?
True (0.8365545874520802)
Mrs. Fairbank has no mean: True or False?
True (0.5964331079469681)
Mrs. Fairbank has motive: True or False?
True (0.9660279734605501)
Mrs. Fairbank has no motive: True or False?
True (0.9001793304600783)
Mrs. Fairbank has opportunity: True or False?
True (0.9606574760904091)
Mrs. Fairbank has no opportunity: True or False?
True (0.8998278389841956)
### Ian Fairbank
- mean: True (0.7225270177274575)
- motive: False (0.12085323930675795)
- opportunity: False (0.29746996894161815)

### Mr. Fairbank
- mean: True (0.7439129430200341)
- motive: True (0.9796870954125814)
- opportunity: True (0.8019358443954961)

### Mr. Lewis Rhys
- mean: True (0.7033457082786769)
- motive: False (0.18068420716986955)
- opportunity: False (0.49023562372598684)

### Mrs. Fairbank
- mean: False (0.40356689205303187)
- motive: False (0.09982066953992175)
- opportunity: False (0.1001721610158044)

The culprit is Mr. Fairbank.
In fact, it is Mrs. Fairbank.
## 5minutemystery-the-gypsys-secret-numbers
Great Marchelli is guilty: True or False?
True (0.873646620599733)
Great Marchelli is not guilty: True or False?
True (0.9447913165152162)

Map:  77%|███████▋  | 157/203 [3:31:40<54:54, 71.63s/ examples]
Map:  78%|███████▊  | 158/203 [3:33:01<55:53, 74.52s/ examples]
Map:  78%|███████▊  | 159/203 [3:34:20<55:28, 75.65s/ examples]Great Marchelli has mean: True or False?
True (0.9026095892260383)
Great Marchelli has no mean: True or False?
True (0.9175984877579624)
Great Marchelli has motive: True or False?
True (0.9680808798281443)
Great Marchelli has no motive: True or False?
True (0.911809923444246)
Great Marchelli has opportunity: True or False?
True (0.8489722037469682)
Great Marchelli has no opportunity: True or False?
True (0.7520125537161032)
Lorenzo is guilty: True or False?
True (0.8370879250561812)
Lorenzo is not guilty: True or False?
True (0.9329437018480795)
Lorenzo has mean: True or False?
True (0.8887587777822111)
Lorenzo has no mean: True or False?
True (0.8418256636710214)
Lorenzo has motive: True or False?
True (0.9431384220853135)
Lorenzo has no motive: True or False?
True (0.8795611817678315)
Lorenzo has opportunity: True or False?
True (0.7662936378892937)
Lorenzo has no opportunity: True or False?
True (0.7911764307711107)
Ringmaster is guilty: True or False?
True (0.9309620852900756)
Ringmaster is not guilty: True or False?
True (0.9498556854872413)
Ringmaster has mean: True or False?
True (0.8582439976623328)
Ringmaster has no mean: True or False?
True (0.869271276026005)
Ringmaster has motive: True or False?
True (0.9687380774673213)
Ringmaster has no motive: True or False?
True (0.9385759849623091)
Ringmaster has opportunity: True or False?
True (0.8998277786460391)
Ringmaster has no opportunity: True or False?
True (0.8679338697256817)
Sheriff is guilty: True or False?
True (0.8633916342942395)
Sheriff is not guilty: True or False?
True (0.8860265599597172)
Sheriff has mean: True or False?
True (0.7872777601997338)
Sheriff has no mean: True or False?
True (0.7620701143808404)
Sheriff has motive: True or False?
True (0.9001793304600783)
Sheriff has no motive: True or False?
True (0.8484706263347676)
Sheriff has opportunity: True or False?
True (0.6513548405484016)
Sheriff has no opportunity: True or False?
True (0.7697732451157533)
### Great Marchelli
- mean: True (0.9026095892260383)
- motive: False (0.08819007655575395)
- opportunity: False (0.2479874462838968)

### Lorenzo
- mean: False (0.1581743363289786)
- motive: False (0.12043881823216851)
- opportunity: True (0.7662936378892937)

### Ringmaster
- mean: True (0.8582439976623328)
- motive: True (0.9687380774673213)
- opportunity: True (0.8998277786460391)

### Sheriff
- mean: False (0.23792988561915962)
- motive: False (0.15152937366523245)
- opportunity: True (0.6513548405484016)

The culprit is Ringmaster.
In fact, it is Sheriff.
## 5minutemystery-its-gone
Abe is guilty: True or False?
True (0.9854404929374018)
Abe is not guilty: True or False?
True (0.9886901378424794)
Abe has mean: True or False?
True (0.9495758995187151)
Abe has no mean: True or False?
True (0.970520555934293)
Abe has motive: True or False?
True (0.9845754507999278)
Abe has no motive: True or False?
True (0.9579909444975866)
Abe has opportunity: True or False?
True (0.9771538382869732)
Abe has no opportunity: True or False?
True (0.9555685526018006)
Lance is guilty: True or False?
True (0.9848983286494055)
Lance is not guilty: True or False?
True (0.9847816823480383)
Lance has mean: True or False?
True (0.878314250659373)
Lance has no mean: True or False?
True (0.9216402157401415)
Lance has motive: True or False?
True (0.9818404909998607)
Lance has no motive: True or False?
True (0.9329437018480795)
Lance has opportunity: True or False?
True (0.9362850185952675)
Lance has no opportunity: True or False?
True (0.9173026661190045)
The Amazing Andrew is guilty: True or False?
True (0.9832788702399727)
The Amazing Andrew is not guilty: True or False?
True (0.9891396764169805)
The Amazing Andrew has mean: True or False?
True (0.8957052808276003)
The Amazing Andrew has no mean: True or False?
True (0.9394706502722077)
The Amazing Andrew has motive: True or False?
True (0.9903196098332093)
The Amazing Andrew has no motive: True or False?
True (0.9683812839782183)
The Amazing Andrew has opportunity: True or False?
True (0.9784259207825959)
The Amazing Andrew has no opportunity: True or False?
True (0.9473810211532727)
Zora the Magnificent is guilty: True or False?
True (0.9857180718083847)
Zora the Magnificent is not guilty: True or False?
True (0.9775429364944704)
Zora the Magnificent has mean: True or False?
True (0.9489172681310486)
Zora the Magnificent has no mean: True or False?
True (0.963230549923961)
Zora the Magnificent has motive: True or False?
True (0.9841850996844234)
Zora the Magnificent has no motive: True or False?
True (0.9559813721912603)
Zora the Magnificent has opportunity: True or False?
True (0.9622497571173928)
Zora the Magnificent has no opportunity: True or False?
True (0.9520419225082909)
### Abe
- mean: True (0.9495758995187151)
- motive: False (0.042009055502413406)
- opportunity: False (0.044431447398199375)

### Lance
- mean: True (0.878314250659373)
- motive: False (0.06705629815192049)
- opportunity: False (0.08269733388099554)

### The Amazing Andrew
- mean: True (0.8957052808276003)
- motive: False (0.03161871602178168)
- opportunity: False (0.05261897884672728)

### Zora the Magnificent
- mean: True (0.9489172681310486)
- motive: True (0.9841850996844234)
- opportunity: True (0.9622497571173928)

The culprit is Zora the Magnificent.
In fact, it is The Amazing Andrew.
## 5minutemystery-the-misers-hoard
Bob Parsons is guilty: True or False?
True (0.909666538803496)
Bob Parsons is not guilty: True or False?
True (0.8989440778839496)
Bob Parsons has mean: True or False?
True (0.7704647687904915)
Bob Parsons has no mean: True or False?
True (0.5312093941731293)
Bob Parsons has motive: True or False?
True (0.9690910565174785)
Bob Parsons has no motive: True or False?
True (0.7386690954574974)
Bob Parsons has opportunity: True or False?
True (0.9173026114435064)
Bob Parsons has no opportunity: True or False?
True (0.7090191197769757)
John Entwhistle III is guilty: True or False?
True (0.9670387494740702)
John Entwhistle III is not guilty: True or False?
True (0.9299510719523877)
John Entwhistle III has mean: True or False?
True (0.9001793304600783)
John Entwhistle III has no mean: True or False?
True (0.743912876509037)
John Entwhistle III has motive: True or False?
True (0.9692661174528692)
John Entwhistle III has no motive: True or False?
True (0.8872045854516336)
John Entwhistle III has opportunity: True or False?
True (0.9463988549853353)
John Entwhistle III has no opportunity: True or False?
True (0.8918110138739693)
Sam Greenway is guilty: True or False?
True (0.9187722824991111)
Sam Greenway is not guilty: True or False?
True (0.8925625120974553)
Sam Greenway has mean: True or False?
True (0.9100670238942131)
Sam Greenway has no mean: True or False?
True (0.5631377056275331)
Sam Greenway has motive: True or False?
True (0.9783433085003262)
Sam Greenway has no motive: True or False?
True (0.8250265688168699)
Sam Greenway has opportunity: True or False?
True (0.8899121304559661)
Sam Greenway has no opportunity: True or False?
True (0.7162185953247016)
Sarah Parsons is guilty: True or False?
True (0.9065704359329319)
Sarah Parsons is not guilty: True or False?
True (0.8883720049821552)
Sarah Parsons has mean: True or False?
True (0.7898827135821628)
Sarah Parsons has no mean: True or False?
False (0.5156199352405011)
Sarah Parsons has motive: True or False?
True (0.963368656065788)
Sarah Parsons has no motive: True or False?
True (0.6169358476670045)
Sarah Parsons has opportunity: True or False?
True (0.7585105966624085)
Sarah Parsons has no opportunity: True or False?
False (0.5273165068094335)
### Bob Parsons
- mean: False (0.4687906058268707)
- motive: False (0.26133090454250263)
- opportunity: False (0.29098088022302426)

### John Entwhistle III
- mean: False (0.25608712349096296)
- motive: False (0.11279541454836639)
- opportunity: False (0.10818898612603067)

### Sam Greenway
- mean: False (0.43686229437246693)
- motive: False (0.17497343118313013)
- opportunity: False (0.28378140467529844)

### Sarah Parsons
- mean: True (0.7898827135821628)
- motive: True (0.963368656065788)
- opportunity: True (0.7585105966624085)

The culprit is Sarah Parsons.
In fact, it is Sarah Parsons.

Map:  79%|███████▉  | 160/203 [3:34:52<44:51, 62.58s/ examples]
Map:  79%|███████▉  | 161/203 [3:35:59<44:43, 63.90s/ examples]
Map:  80%|███████▉  | 162/203 [3:37:35<50:13, 73.51s/ examples]## 5minutemystery-the-cornfield-caper
Austin is guilty: True or False?
True (0.9632304925109479)
Austin is not guilty: True or False?
True (0.9572778330298248)
Austin has mean: True or False?
True (0.8128672807499561)
Austin has no mean: True or False?
True (0.720171518230031)
Austin has motive: True or False?
True (0.9579909444975866)
Austin has no motive: True or False?
True (0.946200309907194)
Austin has opportunity: True or False?
True (0.9498557456415421)
Austin has no opportunity: True or False?
True (0.9241418261705818)
Billy is guilty: True or False?
True (0.9689738169140454)
Billy is not guilty: True or False?
True (0.9735442395649992)
Billy has mean: True or False?
True (0.7401742969616896)
Billy has no mean: True or False?
True (0.6671476389322356)
Billy has motive: True or False?
True (0.9295683483415352)
Billy has no motive: True or False?
True (0.9133679254389228)
Billy has opportunity: True or False?
True (0.9001793304600783)
Billy has no opportunity: True or False?
True (0.8868131040663721)
Nick is guilty: True or False?
True (0.972727357600667)
Nick is not guilty: True or False?
True (0.9739437102411692)
Nick has mean: True or False?
True (0.8469578650997759)
Nick has no mean: True or False?
True (0.8933094122075369)
Nick has motive: True or False?
True (0.9515489937596097)
Nick has no motive: True or False?
True (0.9528381231454964)
Nick has opportunity: True or False?
True (0.9569571019757698)
Nick has no opportunity: True or False?
True (0.8820219652716884)
### Austin
- mean: False (0.279828481769969)
- motive: False (0.05379969009280605)
- opportunity: False (0.07585817382941817)

### Billy
- mean: True (0.7401742969616896)
- motive: True (0.9295683483415352)
- opportunity: True (0.9001793304600783)

### Nick
- mean: True (0.8469578650997759)
- motive: True (0.9515489937596097)
- opportunity: False (0.11797803472831159)

The culprit is Billy.
In fact, it is Billy.
## 5minutemystery-a-stolen-future
Donna Blake is guilty: True or False?
True (0.9447913165152162)
Donna Blake is not guilty: True or False?
True (0.9530133616438526)
Donna Blake has mean: True or False?
True (0.9437636745681832)
Donna Blake has no mean: True or False?
True (0.8514594452543962)
Donna Blake has motive: True or False?
True (0.9797452684142095)
Donna Blake has no motive: True or False?
True (0.9111796625714835)
Donna Blake has opportunity: True or False?
True (0.9289263523387795)
Donna Blake has no opportunity: True or False?
True (0.6451199006197486)
George Wilson is guilty: True or False?
True (0.9468920823984345)
George Wilson is not guilty: True or False?
True (0.9527502639818524)
George Wilson has mean: True or False?
True (0.9145963197706802)
George Wilson has no mean: True or False?
True (0.8723473540228537)
George Wilson has motive: True or False?
True (0.9829546804969759)
George Wilson has no motive: True or False?
True (0.9487275499225403)
George Wilson has opportunity: True or False?
True (0.9408984770280414)
George Wilson has no opportunity: True or False?
True (0.7549149897594328)
Jeffery Sharp is guilty: True or False?
True (0.9402434229803527)
Jeffery Sharp is not guilty: True or False?
True (0.966537058600438)
Jeffery Sharp has mean: True or False?
True (0.9509603994010378)
Jeffery Sharp has no mean: True or False?
True (0.905656637917298)
Jeffery Sharp has motive: True or False?
True (0.9930961729703996)
Jeffery Sharp has no motive: True or False?
True (0.9662834418200392)
Jeffery Sharp has opportunity: True or False?
True (0.9791157846694846)
Jeffery Sharp has no opportunity: True or False?
True (0.8558511090164419)
Pete Thompson is guilty: True or False?
True (0.9001793304600783)
Pete Thompson is not guilty: True or False?
True (0.9572777759716213)
Pete Thompson has mean: True or False?
True (0.7994422859301654)
Pete Thompson has no mean: True or False?
True (0.7950222460539826)
Pete Thompson has motive: True or False?
True (0.9629527935182168)
Pete Thompson has no motive: True or False?
True (0.9481545078856665)
Pete Thompson has opportunity: True or False?
True (0.9390248079664695)
Pete Thompson has no opportunity: True or False?
True (0.7905302675820512)
### Donna Blake
- mean: False (0.1485405547456038)
- motive: False (0.08882033742851647)
- opportunity: False (0.35488009938025145)

### George Wilson
- mean: False (0.12765264597714632)
- motive: False (0.05127245007745973)
- opportunity: False (0.24508501024056717)

### Jeffery Sharp
- mean: False (0.094343362082702)
- motive: False (0.033716558179960776)
- opportunity: False (0.1441488909835581)

### Pete Thompson
- mean: True (0.7994422859301654)
- motive: True (0.9629527935182168)
- opportunity: True (0.9390248079664695)

The culprit is Pete Thompson.
In fact, it is Jeffery Sharp.
## 5minutemystery-the-dirty-half-dozen
Bethany Knight is guilty: True or False?
True (0.9498556854872413)
Bethany Knight is not guilty: True or False?
True (0.9385759220258869)
Bethany Knight has mean: True or False?
True (0.8050197341926492)
Bethany Knight has no mean: True or False?
True (0.7520125537161032)
Bethany Knight has motive: True or False?
True (0.9611709710713023)
Bethany Knight has no motive: True or False?
True (0.9082930704920021)
Bethany Knight has opportunity: True or False?
True (0.8140527631337082)
Bethany Knight has no opportunity: True or False?
True (0.6433293282949071)
Joe Clark is guilty: True or False?
True (0.9418683665706381)
Joe Clark is not guilty: True or False?
True (0.9234543414029781)
Joe Clark has mean: True or False?
True (0.8776866744811284)
Joe Clark has no mean: True or False?
True (0.776622945813876)
Joe Clark has motive: True or False?
True (0.9626028535101038)
Joe Clark has no motive: True or False?
True (0.869271276026005)
Joe Clark has opportunity: True or False?
True (0.8344069148356309)
Joe Clark has no opportunity: True or False?
True (0.6808785831877406)
Sherry Fogle is guilty: True or False?
True (0.9422946582938823)
Sherry Fogle is not guilty: True or False?
True (0.9325762415758686)
Sherry Fogle has mean: True or False?
True (0.8661325012437474)
Sherry Fogle has no mean: True or False?
True (0.8080671968507699)
Sherry Fogle has motive: True or False?
True (0.9742394680162697)
Sherry Fogle has no motive: True or False?
True (0.933065775857525)
Sherry Fogle has opportunity: True or False?
True (0.814643384779728)
Sherry Fogle has no opportunity: True or False?
True (0.6697448487720212)
Tonya Muse is guilty: True or False?
True (1.7651923355465458)
Tonya Muse is not guilty: True or False?
True (1.0445430595969383)
Tonya Muse has mean: True or False?
True (0.5888891269161294)
Tonya Muse has no mean: True or False?
True (0.589834510337428)
Tonya Muse has motive: True or False?
True (0.9537943000694998)
Tonya Muse has no motive: True or False?
True (0.8386797310322072)
Tonya Muse has opportunity: True or False?
True (0.6288633913849659)
Tonya Muse has no opportunity: True or False?
False (0.6270381219830087)
Wayne Clark is guilty: True or False?
True (0.957037509078236)
Wayne Clark is not guilty: True or False?
True (0.9360516072812131)
Wayne Clark has mean: True or False?
True (0.8987665204865408)
Wayne Clark has no mean: True or False?
True (0.8283841584202847)
Wayne Clark has motive: True or False?
True (0.9653158197836269)
Wayne Clark has no motive: True or False?
True (0.9026095892260383)
Wayne Clark has opportunity: True or False?
True (0.8376199551237796)
Wayne Clark has no opportunity: True or False?
True (0.7302898714065358)
### Bethany Knight
- mean: False (0.2479874462838968)
- motive: False (0.09170692950799786)
- opportunity: False (0.3566706717050929)

### Joe Clark
- mean: False (0.22337705418612397)
- motive: False (0.13072872397399504)
- opportunity: False (0.31912141681225936)

### Sherry Fogle
- mean: False (0.1919328031492301)
- motive: False (0.06693422414247496)
- opportunity: False (0.33025515122797877)

### Tonya Muse
- mean: True (0.5888891269161294)
- motive: True (0.9537943000694998)
- opportunity: True (0.6288633913849659)

### Wayne Clark
- mean: False (0.17161584157971532)
- motive: False (0.09739041077396171)
- opportunity: False (0.2697101285934642)

The culprit is Tonya Muse.
In fact, it is Wayne Clark.

Map:  80%|████████  | 163/203 [3:39:04<52:07, 78.18s/ examples]
Map:  81%|████████  | 164/203 [3:40:14<49:12, 75.69s/ examples]## 5minutemystery-a-porsche-of-course
Amy Golden is guilty: True or False?
True (0.9837225082161594)
Amy Golden is not guilty: True or False?
True (0.9895715114165718)
Amy Golden has mean: True or False?
True (0.9585376970077499)
Amy Golden has no mean: True or False?
True (0.9829546804969759)
Amy Golden has motive: True or False?
True (0.9902161360821735)
Amy Golden has no motive: True or False?
True (0.9887118935740483)
Amy Golden has opportunity: True or False?
True (0.9814889431064477)
Amy Golden has no opportunity: True or False?
True (0.9632304925109479)
Frankie Cole is guilty: True or False?
True (0.9785492416845885)
Frankie Cole is not guilty: True or False?
True (0.972727357600667)
Frankie Cole has mean: True or False?
True (0.9302050495103452)
Frankie Cole has no mean: True or False?
True (0.9658995863383641)
Frankie Cole has motive: True or False?
True (0.9839708801996613)
Frankie Cole has no motive: True or False?
True (0.9730364677532105)
Frankie Cole has opportunity: True or False?
True (0.9750122434684597)
Frankie Cole has no opportunity: True or False?
True (0.9392480858026054)
Jeremy Steele is guilty: True or False?
True (0.9716178782667568)
Jeremy Steele is not guilty: True or False?
True (0.9688561547723137)
Jeremy Steele has mean: True or False?
True (0.9260365949489886)
Jeremy Steele has no mean: True or False?
True (0.948346199423113)
Jeremy Steele has motive: True or False?
True (0.9764007329815675)
Jeremy Steele has no motive: True or False?
True (0.94620036983)
Jeremy Steele has opportunity: True or False?
True (0.9671630869492336)
Jeremy Steele has no opportunity: True or False?
True (0.9076402191395381)
Lionel Jacobs is guilty: True or False?
True (0.9789554468203624)
Lionel Jacobs is not guilty: True or False?
True (0.9643214331583058)
Lionel Jacobs has mean: True or False?
True (0.94620036983)
Lionel Jacobs has no mean: True or False?
True (0.9412234437340664)
Lionel Jacobs has motive: True or False?
True (0.9774139529645163)
Lionel Jacobs has no motive: True or False?
True (0.9707986706740892)
Lionel Jacobs has opportunity: True or False?
True (0.9678385865075065)
Lionel Jacobs has no opportunity: True or False?
True (0.9039744767757508)
Susan Barker is guilty: True or False?
True (0.976580083009196)
Susan Barker is not guilty: True or False?
True (0.9760379193901831)
Susan Barker has mean: True or False?
True (0.9294403817764149)
Susan Barker has no mean: True or False?
True (0.9591542492415448)
Susan Barker has motive: True or False?
True (0.9712384344135814)
Susan Barker has no motive: True or False?
True (0.9575961815839735)
Susan Barker has opportunity: True or False?
True (0.9515039936355008)
Susan Barker has no opportunity: True or False?
True (0.9238675252821831)
### Amy Golden
- mean: True (0.9585376970077499)
- motive: True (0.9902161360821735)
- opportunity: True (0.9814889431064477)

### Frankie Cole
- mean: True (0.9302050495103452)
- motive: False (0.02696353224678949)
- opportunity: False (0.06075191419739456)

### Jeremy Steele
- mean: True (0.9260365949489886)
- motive: False (0.05379963017)
- opportunity: False (0.09235978086046193)

### Lionel Jacobs
- mean: False (0.05877655626593359)
- motive: False (0.029201329325910796)
- opportunity: False (0.09602552322424918)

### Susan Barker
- mean: True (0.9294403817764149)
- motive: False (0.04240381841602647)
- opportunity: False (0.07613247471781692)

The culprit is Amy Golden.
In fact, it is Frankie Cole.
## 5minutemystery-the-mystery-of-the-missing-story
Alex Rebmevon is guilty: True or False?
True (0.91789335161495)
Alex Rebmevon is not guilty: True or False?
True (0.9162595863469921)
Alex Rebmevon has mean: True or False?
True (0.7041601500399041)
Alex Rebmevon has no mean: True or False?
True (0.7041601500399041)
Alex Rebmevon has motive: True or False?
True (0.958226146208407)
Alex Rebmevon has no motive: True or False?
True (0.854884620116169)
Alex Rebmevon has opportunity: True or False?
True (0.8013146490010521)
Alex Rebmevon has no opportunity: True or False?
False (0.5515736950589613)
Amy is guilty: True or False?
True (0.8640812064457842)
Amy is not guilty: True or False?
True (0.9609516854153933)
Amy has mean: True or False?
True (0.8433797899747144)
Amy has no mean: True or False?
True (0.7772998201448375)
Amy has motive: True or False?
True (0.9705764057188281)
Amy has no motive: True or False?
True (0.8991213421091365)
Amy has opportunity: True or False?
True (0.8413047772878592)
Amy has no opportunity: True or False?
True (0.644225125126315)
Lucy is guilty: True or False?
True (0.7779753136455794)
Lucy is not guilty: True or False?
True (0.8354835531737983)
Lucy has mean: True or False?
True (0.5907792634380938)
Lucy has no mean: True or False?
True (0.5535053004623279)
Lucy has motive: True or False?
True (0.9615337835163564)
Lucy has no motive: True or False?
True (0.8104788598666923)
Lucy has opportunity: True or False?
True (0.7264255794048772)
Lucy has no opportunity: True or False?
True (0.5428632463719839)
Sarah is guilty: True or False?
True (0.8308687759814434)
Sarah is not guilty: True or False?
True (0.914290668913133)
Sarah has mean: True or False?
True (0.8175745039697023)
Sarah has no mean: True or False?
True (0.678326898500563)
Sarah has motive: True or False?
True (0.9662834418200392)
Sarah has no motive: True or False?
True (0.8697145551802641)
Sarah has opportunity: True or False?
True (0.8606036289596553)
Sarah has no opportunity: True or False?
True (0.5832033352502285)
### Alex Rebmevon
- mean: True (0.7041601500399041)
- motive: True (0.958226146208407)
- opportunity: True (0.8013146490010521)

### Amy
- mean: False (0.22270017985516255)
- motive: False (0.10087865789086348)
- opportunity: False (0.355774874873685)

### Lucy
- mean: False (0.44649469953767207)
- motive: False (0.18952114013330768)
- opportunity: False (0.4571367536280161)

### Sarah
- mean: False (0.32167310149943695)
- motive: False (0.13028544481973592)
- opportunity: False (0.4167966647497715)

The culprit is Alex Rebmevon.
In fact, it is Lucy.
## 5minutemystery-the-case-of-the-missing-friend
Billy Friend is guilty: True or False?
True (0.8354835531737983)
Billy Friend is not guilty: True or False?
True (0.873646672673131)
Billy Friend has mean: True or False?
True (0.9628131975124238)
Billy Friend has no mean: True or False?
True (0.816406362162552)
Billy Friend has motive: True or False?
False (0.6073669806570988)
Billy Friend has no motive: True or False?
True (0.8053261634128519)
Billy Friend has opportunity: True or False?
True (0.8887587777822111)
Billy Friend has no opportunity: True or False?
True (0.7098243920264812)
Diana Scott is guilty: True or False?
True (0.9194980294026535)
Diana Scott is not guilty: True or False?
True (0.9589241138134527)
Diana Scott has mean: True or False?
True (0.9711837766333243)
Diana Scott has no mean: True or False?
True (0.8044059309478723)
Diana Scott has motive: True or False?
True (0.9482983939002998)
Diana Scott has no motive: True or False?
True (0.8365545874520802)
Diana Scott has opportunity: True or False?
True (0.8846386054372942)
Diana Scott has no opportunity: True or False?
True (0.580352018589158)
Harrell Garner is guilty: True or False?
True (0.9419752942631836)
Harrell Garner is not guilty: True or False?
True (0.9653811448171958)
Harrell Garner has mean: True or False?
True (0.9807288650933316)
Harrell Garner has no mean: True or False?
True (0.8910549899564296)
Harrell Garner has motive: True or False?
True (0.9534053189771676)
Harrell Garner has no motive: True or False?
True (0.8994750975198919)
Harrell Garner has opportunity: True or False?
True (0.943970619289785)
Harrell Garner has no opportunity: True or False?
True (0.686790355176806)
Susan Allen is guilty: True or False?
True (0.814643384779728)
Susan Allen is not guilty: True or False?
True (0.9206470837359207)
Susan Allen has mean: True or False?
True (0.9339146597970963)
Susan Allen has no mean: True or False?
True (0.6315942370470465)
Susan Allen has motive: True or False?
False (0.72520429508428)
Susan Allen has no motive: True or False?
True (0.7333563569098757)
Susan Allen has opportunity: True or False?

Map:  81%|████████▏ | 165/203 [3:41:17<45:35, 71.99s/ examples]
Map:  82%|████████▏ | 166/203 [3:42:22<43:02, 69.80s/ examples]
Map:  82%|████████▏ | 167/203 [3:43:36<42:45, 71.25s/ examples]True (0.7799928701983835)
Susan Allen has no opportunity: True or False?
True (0.5243946792389143)
### Billy Friend
- mean: False (0.18359363783744798)
- motive: False (0.6073669806570988)
- opportunity: False (0.2901756079735188)

### Diana Scott
- mean: False (0.19559406905212773)
- motive: False (0.16344541254791978)
- opportunity: False (0.41964798141084203)

### Harrell Garner
- mean: True (0.9807288650933316)
- motive: True (0.9534053189771676)
- opportunity: True (0.943970619289785)

### Susan Allen
- mean: False (0.36840576295295346)
- motive: False (0.72520429508428)
- opportunity: False (0.47560532076108575)

The culprit is Harrell Garner.
In fact, it is Diana Scott.
## 5minutemystery-sweat-it-out
Chris Henderson is guilty: True or False?
True (0.9229003224709645)
Chris Henderson is not guilty: True or False?
True (0.9579909444975866)
Chris Henderson has mean: True or False?
True (0.9076401582775206)
Chris Henderson has no mean: True or False?
True (0.8856314413364714)
Chris Henderson has motive: True or False?
True (0.9634374994224176)
Chris Henderson has no motive: True or False?
True (0.8914335992201801)
Chris Henderson has opportunity: True or False?
True (0.9473810811508532)
Chris Henderson has no opportunity: True or False?
True (0.9043130884593419)
Dave Perkins is guilty: True or False?
True (0.8665847814067802)
Dave Perkins is not guilty: True or False?
True (0.9402434229803527)
Dave Perkins has mean: True or False?
True (0.8840392847025188)
Dave Perkins has no mean: True or False?
True (0.7468781997658912)
Dave Perkins has motive: True or False?
True (0.9658351545108645)
Dave Perkins has no motive: True or False?
True (0.8633915828320894)
Dave Perkins has opportunity: True or False?
True (0.9233161821369215)
Dave Perkins has no opportunity: True or False?
True (0.8674854614419002)
Larry Douglas is guilty: True or False?
True (0.8919993657480679)
Larry Douglas is not guilty: True or False?
True (0.9473810811508532)
Larry Douglas has mean: True or False?
True (0.8587185689177256)
Larry Douglas has no mean: True or False?
True (0.7905302675820512)
Larry Douglas has motive: True or False?
True (0.9738194950619852)
Larry Douglas has no motive: True or False?
True (0.9487275499225403)
Larry Douglas has opportunity: True or False?
True (0.9376689222692878)
Larry Douglas has no opportunity: True or False?
True (0.8770561879413864)
Nathan Elliott is guilty: True or False?
True (0.8906751280163339)
Nathan Elliott is not guilty: True or False?
True (0.9547319423032952)
Nathan Elliott has mean: True or False?
True (0.9537942396657707)
Nathan Elliott has no mean: True or False?
True (0.9079671476237222)
Nathan Elliott has motive: True or False?
True (0.9949334859556598)
Nathan Elliott has no motive: True or False?
True (0.9608783125643616)
Nathan Elliott has opportunity: True or False?
True (0.9727272996216001)
Nathan Elliott has no opportunity: True or False?
True (0.892187358563457)
### Chris Henderson
- mean: True (0.9076401582775206)
- motive: True (0.9634374994224176)
- opportunity: True (0.9473810811508532)

### Dave Perkins
- mean: False (0.2531218002341088)
- motive: False (0.1366084171679106)
- opportunity: False (0.1325145385580998)

### Larry Douglas
- mean: False (0.20946973241794875)
- motive: False (0.05127245007745973)
- opportunity: False (0.1229438120586136)

### Nathan Elliott
- mean: False (0.09203285237627779)
- motive: False (0.039121687435638375)
- opportunity: False (0.10781264143654301)

The culprit is Chris Henderson.
In fact, it is Chris Henderson.
## 5minutemystery-mystery-of-the-missing-heart
Eric Winter is guilty: True or False?
True (0.8987665204865408)
Eric Winter is not guilty: True or False?
True (0.9108630396247971)
Eric Winter has mean: True or False?
True (0.8221891570741111)
Eric Winter has no mean: True or False?
True (0.7799928701983835)
Eric Winter has motive: True or False?
True (0.9846346375905863)
Eric Winter has no motive: True or False?
True (0.8360197583769845)
Eric Winter has opportunity: True or False?
True (0.9012274173198201)
Eric Winter has no opportunity: True or False?
False (0.6334102859975052)
Jenny Jackson is guilty: True or False?
True (0.8568122940392877)
Jenny Jackson is not guilty: True or False?
True (0.8494724067948436)
Jenny Jackson has mean: True or False?
True (0.6662796746479285)
Jenny Jackson has no mean: True or False?
False (0.5302364729224919)
Jenny Jackson has motive: True or False?
True (0.919930758847437)
Jenny Jackson has no motive: True or False?
True (0.6959583025067009)
Jenny Jackson has opportunity: True or False?
True (0.8338664134858856)
Jenny Jackson has no opportunity: True or False?
False (0.7356416476869558)
Jimmy Jackson is guilty: True or False?
True (0.8774767496170098)
Jimmy Jackson is not guilty: True or False?
True (0.8037905715242155)
Jimmy Jackson has mean: True or False?
True (0.791821116278941)
Jimmy Jackson has no mean: True or False?
False (0.5544704160706745)
Jimmy Jackson has motive: True or False?
True (0.9092645024391882)
Jimmy Jackson has no motive: True or False?
True (0.7786493288700866)
Jimmy Jackson has opportunity: True or False?
True (0.8762113474663927)
Jimmy Jackson has no opportunity: True or False?
False (0.555435161888281)
Wendy LaRue is guilty: True or False?
True (0.9307105568817887)
Wendy LaRue is not guilty: True or False?
True (0.8799743689174987)
Wendy LaRue has mean: True or False?
True (0.6477981763584071)
Wendy LaRue has no mean: True or False?
True (0.5822535180679596)
Wendy LaRue has motive: True or False?
True (0.9798226352078263)
Wendy LaRue has no motive: True or False?
True (0.6513548405484016)
Wendy LaRue has opportunity: True or False?
True (0.8587185689177256)
Wendy LaRue has no opportunity: True or False?
False (0.7256486384635821)
### Eric Winter
- mean: False (0.22000712980161652)
- motive: False (0.1639802416230155)
- opportunity: True (0.9012274173198201)

### Jenny Jackson
- mean: True (0.6662796746479285)
- motive: False (0.3040416974932991)
- opportunity: True (0.8338664134858856)

### Jimmy Jackson
- mean: True (0.791821116278941)
- motive: True (0.9092645024391882)
- opportunity: True (0.8762113474663927)

### Wendy LaRue
- mean: False (0.41774648193204045)
- motive: False (0.34864515945159835)
- opportunity: True (0.8587185689177256)

The culprit is Jimmy Jackson.
In fact, it is Eric Winter.
## 5minutemystery-stealing-second-base
Coach Joe Morgan is guilty: True or False?
True (0.7931058945535956)
Coach Joe Morgan is not guilty: True or False?
True (0.8402590129647053)
Coach Joe Morgan has mean: True or False?
True (0.6619228707202935)
Coach Joe Morgan has no mean: True or False?
False (0.5029296229885981)
Coach Joe Morgan has motive: True or False?
True (0.9385759849623091)
Coach Joe Morgan has no motive: True or False?
True (0.7634837587244478)
Coach Joe Morgan has opportunity: True or False?
True (0.8031737798924701)
Coach Joe Morgan has no opportunity: True or False?
False (0.6325027972911149)
Mary Thornton is guilty: True or False?
True (0.9029524325377104)
Mary Thornton is not guilty: True or False?
True (0.9164093756391206)
Mary Thornton has mean: True or False?
True (0.8086723099497763)
Mary Thornton has no mean: True or False?
True (0.7248702601920561)
Mary Thornton has motive: True or False?
True (0.975059748401155)
Mary Thornton has no motive: True or False?
True (0.8875949368741688)
Mary Thornton has opportunity: True or False?
True (0.9403530352223053)
Mary Thornton has no opportunity: True or False?
True (0.6893056096647525)
Randy Newsom is guilty: True or False?
True (0.9319595674053855)
Randy Newsom is not guilty: True or False?
True (0.9378968460746586)
Randy Newsom has mean: True or False?
True (0.7534666630720156)
Randy Newsom has no mean: True or False?
True (0.566977858563838)
Randy Newsom has motive: True or False?
True (0.9558991201960071)
Randy Newsom has no motive: True or False?
True (0.8710367026584496)
Randy Newsom has opportunity: True or False?
True (0.9314624659768579)
Randy Newsom has no opportunity: True or False?
True (0.6540113633452196)
Shorty Gilstrap is guilty: True or False?
True (0.9336731438527403)
Shorty Gilstrap is not guilty: True or False?

Map:  83%|████████▎ | 168/203 [3:44:45<41:06, 70.47s/ examples]
Map:  83%|████████▎ | 169/203 [3:45:58<40:26, 71.38s/ examples]
Map:  84%|████████▎ | 170/203 [3:47:07<38:49, 70.58s/ examples]True (0.9170058945178141)
Shorty Gilstrap has mean: True or False?
True (0.7662936378892937)
Shorty Gilstrap has no mean: True or False?
True (0.6160122877297346)
Shorty Gilstrap has motive: True or False?
True (0.9724670646029822)
Shorty Gilstrap has no motive: True or False?
True (0.8929365260632085)
Shorty Gilstrap has opportunity: True or False?
True (0.9431384220853135)
Shorty Gilstrap has no opportunity: True or False?
True (0.7662936378892937)
### Coach Joe Morgan
- mean: True (0.6619228707202935)
- motive: True (0.9385759849623091)
- opportunity: True (0.8031737798924701)

### Mary Thornton
- mean: False (0.27512973980794386)
- motive: False (0.1124050631258312)
- opportunity: False (0.3106943903352475)

### Randy Newsom
- mean: False (0.433022141436162)
- motive: False (0.12896329734155043)
- opportunity: False (0.3459886366547804)

### Shorty Gilstrap
- mean: False (0.3839877122702654)
- motive: False (0.1070634739367915)
- opportunity: False (0.23370636211070628)

The culprit is Coach Joe Morgan.
In fact, it is Mary Thornton.
## 5minutemystery-murder-in-the-old-house
Bathroom is guilty: True or False?
True (0.9666001797251225)
Bathroom is not guilty: True or False?
True (0.97805178109456)
Bathroom has mean: True or False?
True (0.9412234437340664)
Bathroom has no mean: True or False?
True (0.9259027265283752)
Bathroom has motive: True or False?
True (0.9835338590325645)
Bathroom has no motive: True or False?
True (0.9447913165152162)
Bathroom has opportunity: True or False?
True (0.9481545679322319)
Bathroom has no opportunity: True or False?
True (0.927887794449634)
Bedroom of daughter, Anita Jensen is guilty: True or False?
True (1.1329194703045333)
Bedroom of daughter, Anita Jensen is not guilty: True or False?
True (0.9227612010756272)
Bedroom of daughter, Anita Jensen has mean: True or False?
True (0.8803862939824989)
Bedroom of daughter, Anita Jensen has no mean: True or False?
True (0.935346481802689)
Bedroom of daughter, Anita Jensen has motive: True or False?
True (0.9760835762008001)
Bedroom of daughter, Anita Jensen has no motive: True or False?
True (0.9640516654033661)
Bedroom of daughter, Anita Jensen has opportunity: True or False?
True (0.9158089188126235)
Bedroom of daughter, Anita Jensen has no opportunity: True or False?
True (0.9015746123467522)
Bedroom of oldest son, Harry Jensen is guilty: True or False?
True (0.9388008138003494)
Bedroom of oldest son, Harry Jensen is not guilty: True or False?
True (0.9329437018480795)
Bedroom of oldest son, Harry Jensen has mean: True or False?
True (0.918626370973125)
Bedroom of oldest son, Harry Jensen has no mean: True or False?
True (0.9233161821369215)
Bedroom of oldest son, Harry Jensen has motive: True or False?
True (0.9751071938949272)
Bedroom of oldest son, Harry Jensen has no motive: True or False?
True (0.948346199423113)
Bedroom of oldest son, Harry Jensen has opportunity: True or False?
True (0.9385759220258869)
Bedroom of oldest son, Harry Jensen has no opportunity: True or False?
True (0.878314250659373)
Bedroom of youngest son, Edward Jensen is guilty: True or False?
True (1.2674606319009032)
Bedroom of youngest son, Edward Jensen is not guilty: True or False?
True (0.9527502639818524)
Bedroom of youngest son, Edward Jensen has mean: True or False?
True (0.9320833112823845)
Bedroom of youngest son, Edward Jensen has no mean: True or False?
True (0.9322068701708559)
Bedroom of youngest son, Edward Jensen has motive: True or False?
True (0.9854404929374018)
Bedroom of youngest son, Edward Jensen has no motive: True or False?
True (0.946497859305556)
Bedroom of youngest son, Edward Jensen has opportunity: True or False?
True (0.9603611816439128)
Bedroom of youngest son, Edward Jensen has no opportunity: True or False?
True (0.884837803442546)
Master bedroom of Earl and Mildrid Jensen is guilty: True or False?
True (0.9796286813551001)
Master bedroom of Earl and Mildrid Jensen is not guilty: True or False?
True (0.9658352120791275)
Master bedroom of Earl and Mildrid Jensen has mean: True or False?
True (0.9755768767688796)
Master bedroom of Earl and Mildrid Jensen has no mean: True or False?
True (0.9860442877958637)
Master bedroom of Earl and Mildrid Jensen has motive: True or False?
True (0.9848983882711804)
Master bedroom of Earl and Mildrid Jensen has no motive: True or False?
True (0.9618216755218261)
Master bedroom of Earl and Mildrid Jensen has opportunity: True or False?
True (0.9615338444102304)
Master bedroom of Earl and Mildrid Jensen has no opportunity: True or False?
True (0.9473810211532727)
### Bathroom
- mean: False (0.07409727347162476)
- motive: False (0.055208683484783805)
- opportunity: False (0.07211220555036602)

### Bedroom of daughter, Anita Jensen
- mean: True (0.8803862939824989)
- motive: True (0.9760835762008001)
- opportunity: True (0.9158089188126235)

### Bedroom of oldest son, Harry Jensen
- mean: True (0.918626370973125)
- motive: False (0.051653800576886955)
- opportunity: False (0.12168574934062704)

### Bedroom of youngest son, Edward Jensen
- mean: True (0.9320833112823845)
- motive: False (0.053502140694444034)
- opportunity: False (0.11516219655745397)

### Master bedroom of Earl and Mildrid Jensen
- mean: True (0.9755768767688796)
- motive: False (0.03817832447817393)
- opportunity: False (0.05261897884672728)

The culprit is Bedroom of daughter, Anita Jensen.
In fact, it is Bathroom.
## 5minutemystery-the-chess-mystery
Father is guilty: True or False?
True (0.9778411387040619)
Father is not guilty: True or False?
True (0.9682614213403071)
Father has mean: True or False?
True (0.9212159548464016)
Father has no mean: True or False?
True (0.8543993851297865)
Father has motive: True or False?
True (0.9590009457171959)
Father has no motive: True or False?
True (0.9362850185952675)
Father has opportunity: True or False?
True (0.7924642605907138)
Father has no opportunity: True or False?
True (0.6951311179371613)
Greg is guilty: True or False?
True (0.9449947479233238)
Greg is not guilty: True or False?
True (0.9515940562763279)
Greg has mean: True or False?
True (0.8311430212356835)
Greg has no mean: True or False?
True (0.8376199551237796)
Greg has motive: True or False?
True (0.9812389020148623)
Greg has no motive: True or False?
True (0.905656637917298)
Greg has opportunity: True or False?
True (0.9222025890552223)
Greg has no opportunity: True or False?
True (0.7240905804783984)
Tina is guilty: True or False?
True (0.9479621664653681)
Tina is not guilty: True or False?
True (0.9492946258008691)
Tina has mean: True or False?
True (0.8175745039697023)
Tina has no mean: True or False?
True (0.6610481693322063)
Tina has motive: True or False?
True (0.9591543064115948)
Tina has no motive: True or False?
True (0.8344069148356309)
Tina has opportunity: True or False?
True (0.8365545251239088)
Tina has no opportunity: True or False?
True (0.5669777909748143)
Uncle Larry is guilty: True or False?
True (0.8820219652716884)
Uncle Larry is not guilty: True or False?
True (0.8991213421091365)
Uncle Larry has mean: True or False?
True (0.8092759828926619)
Uncle Larry has no mean: True or False?
True (0.7570766705324253)
Uncle Larry has motive: True or False?
True (0.934155284694701)
Uncle Larry has no motive: True or False?
True (0.8514594452543962)
Uncle Larry has opportunity: True or False?
True (0.7759445334082792)
Uncle Larry has no opportunity: True or False?
True (0.5019531141001669)
### Father
- mean: True (0.9212159548464016)
- motive: True (0.9590009457171959)
- opportunity: True (0.7924642605907138)

### Greg
- mean: True (0.8311430212356835)
- motive: False (0.094343362082702)
- opportunity: False (0.27590941952160164)

### Tina
- mean: False (0.33895183066779366)
- motive: False (0.1655930851643691)
- opportunity: False (0.43302220902518573)

### Uncle Larry
- mean: False (0.24292332946757467)
- motive: False (0.1485405547456038)
- opportunity: False (0.49804688589983315)

The culprit is Father.
In fact, it is Greg.
## 5minutemystery-lost-stolen-and-found
John Beddington is guilty: True or False?
True (0.7662936378892937)
John Beddington is not guilty: True or False?
True (0.8816148581338575)

Map:  84%|████████▍ | 171/203 [3:48:11<36:35, 68.62s/ examples]
Map:  85%|████████▍ | 172/203 [3:49:11<34:06, 66.01s/ examples]
Map:  85%|████████▌ | 173/203 [3:50:23<33:54, 67.80s/ examples]John Beddington has mean: True or False?
True (0.8895288719962232)
John Beddington has no mean: True or False?
True (0.8193157317863493)
John Beddington has motive: True or False?
True (0.9374402785760423)
John Beddington has no motive: True or False?
True (0.8098781635062345)
John Beddington has opportunity: True or False?
True (0.8294920340613177)
John Beddington has no opportunity: True or False?
True (0.7248702601920561)
Louisa Perry is guilty: True or False?
True (0.7697732451157533)
Louisa Perry is not guilty: True or False?
True (0.893681109060862)
Louisa Perry has mean: True or False?
True (0.8973360043541736)
Louisa Perry has no mean: True or False?
True (0.6424325178417575)
Louisa Perry has motive: True or False?
True (0.9492946859196381)
Louisa Perry has no motive: True or False?
True (0.7446563307563252)
Louisa Perry has opportunity: True or False?
True (0.8013146490010521)
Louisa Perry has no opportunity: True or False?
True (0.5409238971378262)
Mary Ingram is guilty: True or False?
True (0.7416740778117503)
Mary Ingram is not guilty: True or False?
True (0.8402590129647053)
Mary Ingram has mean: True or False?
True (0.8951566249612815)
Mary Ingram has no mean: True or False?
True (0.7520125537161032)
Mary Ingram has motive: True or False?
True (0.9456006903352807)
Mary Ingram has no motive: True or False?
True (0.7627776774954688)
Mary Ingram has opportunity: True or False?
True (0.8665847814067802)
Mary Ingram has no opportunity: True or False?
True (0.5612147992901458)
Sarah Upton is guilty: True or False?
True (0.875361437979977)
Sarah Upton is not guilty: True or False?
True (0.9178934131644976)
Sarah Upton has mean: True or False?
True (0.9038048413863352)
Sarah Upton has no mean: True or False?
True (0.9043130884593419)
Sarah Upton has motive: True or False?
True (0.9535353169313603)
Sarah Upton has no motive: True or False?
True (0.874934615163517)
Sarah Upton has opportunity: True or False?
True (0.9116528030198908)
Sarah Upton has no opportunity: True or False?
True (0.5983121871760707)
### John Beddington
- mean: True (0.8895288719962232)
- motive: True (0.9374402785760423)
- opportunity: True (0.8294920340613177)

### Louisa Perry
- mean: False (0.3575674821582425)
- motive: False (0.2553436692436748)
- opportunity: False (0.4590761028621738)

### Mary Ingram
- mean: False (0.2479874462838968)
- motive: False (0.23722232250453124)
- opportunity: False (0.43878520070985416)

### Sarah Upton
- mean: True (0.9038048413863352)
- motive: False (0.125065384836483)
- opportunity: False (0.4016878128239293)

The culprit is John Beddington.
In fact, it is Louisa Perry.
## 5minutemystery-the-chocolate-cupcake-caper
Geraldine is guilty: True or False?
True (0.9322068701708559)
Geraldine is not guilty: True or False?
True (0.9841850391892343)
Geraldine has mean: True or False?
True (0.8856315007226893)
Geraldine has no mean: True or False?
True (0.815232454829111)
Geraldine has motive: True or False?
True (0.9818056233287176)
Geraldine has no motive: True or False?
True (0.985552132278138)
Geraldine has opportunity: True or False?
True (0.9612438076473231)
Geraldine has no opportunity: True or False?
True (0.9541373270174538)
Julianna is guilty: True or False?
True (0.8872045854516336)
Julianna is not guilty: True or False?
True (0.9636433123221183)
Julianna has mean: True or False?
True (0.9015745518914653)
Julianna has no mean: True or False?
True (0.779321849347754)
Julianna has motive: True or False?
True (0.9798997635332343)
Julianna has no motive: True or False?
True (0.9731388097113137)
Julianna has opportunity: True or False?
True (0.9591543064115948)
Julianna has no opportunity: True or False?
True (0.9378969089655451)
Luis is guilty: True or False?
True (0.9171543708147702)
Luis is not guilty: True or False?
True (0.9756234297188763)
Luis has mean: True or False?
True (0.8426043397677332)
Luis has no mean: True or False?
True (0.7341195403199204)
Luis has motive: True or False?
True (0.9843062166752533)
Luis has no motive: True or False?
True (0.9791955348264648)
Luis has opportunity: True or False?
True (0.920789721359066)
Luis has no opportunity: True or False?
True (0.9124361878432953)
Mr. Bento is guilty: True or False?
True (0.897695304229796)
Mr. Bento is not guilty: True or False?
True (0.9475754509027036)
Mr. Bento has mean: True or False?
True (0.8316905440184192)
Mr. Bento has no mean: True or False?
True (0.7549149897594328)
Mr. Bento has motive: True or False?
True (0.9847230314726132)
Mr. Bento has no motive: True or False?
True (0.9637799266082508)
Mr. Bento has opportunity: True or False?
True (0.883638205304735)
Mr. Bento has no opportunity: True or False?
True (0.8428631416381634)
### Geraldine
- mean: True (0.8856315007226893)
- motive: True (0.9818056233287176)
- opportunity: True (0.9612438076473231)

### Julianna
- mean: False (0.22067815065224605)
- motive: False (0.026861190288686276)
- opportunity: False (0.06210309103445488)

### Luis
- mean: False (0.26588045968007956)
- motive: False (0.02080446517353518)
- opportunity: False (0.08756381215670472)

### Mr. Bento
- mean: False (0.24508501024056717)
- motive: False (0.03622007339174915)
- opportunity: False (0.15713685836183655)

The culprit is Geraldine.
In fact, it is Geraldine.
## 5minutemystery-dead-mans-island
Grandpa is guilty: True or False?
True (0.8534247816107388)
Grandpa is not guilty: True or False?
True (0.8799743689174987)
Grandpa has mean: True or False?
True (0.6706082735718226)
Grandpa has no mean: True or False?
True (0.615087818987177)
Grandpa has motive: True or False?
True (0.9558991201960071)
Grandpa has no motive: True or False?
True (0.6808785831877406)
Grandpa has opportunity: True or False?
True (0.8050197341926492)
Grandpa has no opportunity: True or False?
True (0.5107405249783342)
Grandpa's grandfather is guilty: True or False?
True (0.7162185953247016)
Grandpa's grandfather is not guilty: True or False?
True (0.7310586002437232)
Grandpa's grandfather has mean: True or False?
True (0.7041601500399041)
Grandpa's grandfather has no mean: True or False?
False (0.6233768569026616)
Grandpa's grandfather has motive: True or False?
True (0.8852351930010195)
Grandpa's grandfather has no motive: True or False?
True (0.580352087772514)
Grandpa's grandfather has opportunity: True or False?
True (0.7017130830397807)
Grandpa's grandfather has no opportunity: True or False?
False (0.7122321792841629)
Lisa is guilty: True or False?
True (0.7556369876990674)
Lisa is not guilty: True or False?
True (0.6662796746479285)
Lisa has mean: True or False?
False (0.685107355950278)
Lisa has no mean: True or False?
False (0.883638205304735)
Lisa has motive: True or False?
True (0.7074046739492601)
Lisa has no motive: True or False?
False (0.5292633777076584)
Lisa has opportunity: True or False?
True (0.6388352560545881)
Lisa has no opportunity: True or False?
False (0.5851012033999957)
Mike is guilty: True or False?
True (0.7905302675820512)
Mike is not guilty: True or False?
True (0.7356416038392981)
Mike has mean: True or False?
True (0.6141625595066657)
Mike has no mean: True or False?
False (0.6967842494573921)
Mike has motive: True or False?
True (0.8984105603938967)
Mike has no motive: True or False?
True (0.7527403228571042)
Mike has opportunity: True or False?
True (0.8807970862580315)
Mike has no opportunity: True or False?
True (0.644225125126315)
### Grandpa
- mean: False (0.384912181012823)
- motive: False (0.31912141681225936)
- opportunity: False (0.4892594750216658)

### Grandpa's grandfather
- mean: True (0.7041601500399041)
- motive: False (0.419647912227486)
- opportunity: True (0.7017130830397807)

### Lisa
- mean: True (0.11636179469526498)
- motive: True (0.7074046739492601)
- opportunity: True (0.6388352560545881)

### Mike
- mean: True (0.6141625595066657)
- motive: False (0.24725967714289576)
- opportunity: False (0.355774874873685)

The culprit is Lisa.
In fact, it is Lisa.
## 5minutemystery-who-stole-the-rock-of-ages
Denise Hurst is guilty: True or False?
True (0.9326989068252284)
Denise Hurst is not guilty: True or False?
True (0.9609517462724031)
Denise Hurst has mean: True or False?
True (0.9612438076473231)
Map:  86%|████████▌ | 174/203 [3:51:33<33:05, 68.47s/ examples]
Map:  86%|████████▌ | 175/203 [3:52:41<31:49, 68.21s/ examples]
Map:  87%|████████▋ | 176/203 [3:53:40<29:28, 65.49s/ examples]
Denise Hurst has no mean: True or False?
True (0.8872045854516336)
Denise Hurst has motive: True or False?
True (0.9842759969893847)
Denise Hurst has no motive: True or False?
True (0.874934615163517)
Denise Hurst has opportunity: True or False?
True (0.9467937951644804)
Denise Hurst has no opportunity: True or False?
True (0.8244619332958376)
Jim Gaigon is guilty: True or False?
True (0.9319595674053855)
Jim Gaigon is not guilty: True or False?
True (0.9196425103002197)
Jim Gaigon has mean: True or False?
True (0.8227594449669557)
Jim Gaigon has no mean: True or False?
True (0.847967740521315)
Jim Gaigon has motive: True or False?
True (0.9571177945772992)
Jim Gaigon has no motive: True or False?
True (0.8086723099497763)
Jim Gaigon has opportunity: True or False?
True (0.9433475737015985)
Jim Gaigon has no opportunity: True or False?
True (0.8261514357843124)
Juan Carde is guilty: True or False?
True (0.9026096497507297)
Juan Carde is not guilty: True or False?
True (0.9467937951644804)
Juan Carde has mean: True or False?
True (0.883638205304735)
Juan Carde has no mean: True or False?
True (0.8529354311342636)
Juan Carde has motive: True or False?
True (0.9596109393754703)
Juan Carde has no motive: True or False?
True (0.8283841584202847)
Juan Carde has opportunity: True or False?
True (0.9276260107813639)
Juan Carde has no opportunity: True or False?
True (0.8181563669811865)
Skye Smith is guilty: True or False?
True (0.9394706502722077)
Skye Smith is not guilty: True or False?
True (0.9569571625798028)
Skye Smith has mean: True or False?
True (0.9529258626138675)
Skye Smith has no mean: True or False?
True (0.9319595674053855)
Skye Smith has motive: True or False?
True (0.9815244083320255)
Skye Smith has no motive: True or False?
True (0.8820219652716884)
Skye Smith has opportunity: True or False?
True (0.9492946258008691)
Skye Smith has no opportunity: True or False?
True (0.8816149238192855)
### Denise Hurst
- mean: False (0.11279541454836639)
- motive: False (0.125065384836483)
- opportunity: False (0.1755380667041624)

### Jim Gaigon
- mean: True (0.8227594449669557)
- motive: False (0.19132769005022365)
- opportunity: False (0.17384856421568762)

### Juan Carde
- mean: False (0.14706456886573638)
- motive: False (0.17161584157971532)
- opportunity: False (0.18184363301881346)

### Skye Smith
- mean: True (0.9529258626138675)
- motive: True (0.9815244083320255)
- opportunity: True (0.9492946258008691)

The culprit is Skye Smith.
In fact, it is Juan Carde.
## 5minutemystery-all-washed-up
Captain Kildare is guilty: True or False?
True (0.8620035048683017)
Captain Kildare is not guilty: True or False?
True (0.8694930622665686)
Captain Kildare has mean: True or False?
True (0.8714748565614324)
Captain Kildare has no mean: True or False?
True (0.837354128670069)
Captain Kildare has motive: True or False?
True (0.9260365949489886)
Captain Kildare has no motive: True or False?
True (0.6688802830862913)
Captain Kildare has opportunity: True or False?
True (0.8441522053247883)
Captain Kildare has no opportunity: True or False?
True (0.6048657973050737)
Latrisha Lanigan is guilty: True or False?
True (0.9489172115711736)
Latrisha Lanigan is not guilty: True or False?
True (0.933065775857525)
Latrisha Lanigan has mean: True or False?
True (0.9007045635949587)
Latrisha Lanigan has no mean: True or False?
True (0.8233283740192667)
Latrisha Lanigan has motive: True or False?
True (0.9193534273597669)
Latrisha Lanigan has no motive: True or False?
True (0.7264255794048772)
Latrisha Lanigan has opportunity: True or False?
True (0.7956581141325956)
Latrisha Lanigan has no opportunity: True or False?
True (0.5832033352502285)
Mark Colson is guilty: True or False?
True (0.9339146597970963)
Mark Colson is not guilty: True or False?
True (0.9001793304600783)
Mark Colson has mean: True or False?
True (0.8233283740192667)
Mark Colson has no mean: True or False?
True (0.7606506998655483)
Mark Colson has motive: True or False?
True (0.9322068701708559)
Mark Colson has no motive: True or False?
True (0.7431679939957333)
Mark Colson has opportunity: True or False?
True (0.9015745518914653)
Mark Colson has no opportunity: True or False?
True (0.6315943123389512)
Marvin Fishback is guilty: True or False?
True (0.9493885642537184)
Marvin Fishback is not guilty: True or False?
True (0.9390248639367113)
Marvin Fishback has mean: True or False?
True (0.9066531077351827)
Marvin Fishback has no mean: True or False?
True (0.8080672570564699)
Marvin Fishback has motive: True or False?
True (0.9412234437340664)
Marvin Fishback has no motive: True or False?
True (0.7541915688671895)
Marvin Fishback has opportunity: True or False?
True (0.9145963197706802)
Marvin Fishback has no opportunity: True or False?
True (0.6288633913849659)
### Captain Kildare
- mean: False (0.16264587132993102)
- motive: False (0.3311197169137087)
- opportunity: False (0.3951342026949263)

### Latrisha Lanigan
- mean: True (0.9007045635949587)
- motive: True (0.9193534273597669)
- opportunity: True (0.7956581141325956)

### Mark Colson
- mean: False (0.23934930013445166)
- motive: False (0.2568320060042667)
- opportunity: False (0.36840568766104875)

### Marvin Fishback
- mean: False (0.19193274294353013)
- motive: False (0.24580843113281048)
- opportunity: False (0.37113660861503406)

The culprit is Latrisha Lanigan.
In fact, it is Mark Colson.
## 5minutemystery-the-hidden-messenger
Jean is guilty: True or False?
True (0.9026095892260383)
Jean is not guilty: True or False?
True (0.9111797236708432)
Jean has mean: True or False?
True (0.879146760693242)
Jean has no mean: True or False?
True (0.686790355176806)
Jean has motive: True or False?
True (0.972151576692602)
Jean has no motive: True or False?
True (0.9307106123564625)
Jean has opportunity: True or False?
True (0.8980534699860239)
Jean has no opportunity: True or False?
True (0.8620035048683017)
Marie is guilty: True or False?
True (0.9392480858026054)
Marie is not guilty: True or False?
True (0.934155284694701)
Marie has mean: True or False?
True (0.8250265688168699)
Marie has no mean: True or False?
True (0.5784481782924303)
Marie has motive: True or False?
True (0.9639839524564597)
Marie has no motive: True or False?
True (0.9142907234091052)
Marie has opportunity: True or False?
True (0.8558511727823209)
Marie has no opportunity: True or False?
True (0.6943026818003076)
Molly is guilty: True or False?
True (0.9388008138003494)
Molly is not guilty: True or False?
True (0.9531007408873468)
Molly has mean: True or False?
True (0.8086723702005608)
Molly has no mean: True or False?
True (0.6095241271158658)
Molly has motive: True or False?
True (0.9772842528587228)
Molly has no motive: True or False?
True (0.8723474190177988)
Molly has opportunity: True or False?
True (0.9489172681310486)
Molly has no opportunity: True or False?
True (0.8175745039697023)
Smith is guilty: True or False?
True (0.9494823209990744)
Smith is not guilty: True or False?
True (0.9488224997202508)
Smith has mean: True or False?
True (0.8037905715242155)
Smith has no mean: True or False?
True (0.8216173055802608)
Smith has motive: True or False?
True (0.9756929870688384)
Smith has no motive: True or False?
True (0.9554855815192022)
Smith has opportunity: True or False?
True (0.8575297062839006)
Smith has no opportunity: True or False?
True (0.8210441512234701)
### Jean
- mean: False (0.313209644823194)
- motive: False (0.06928938764353754)
- opportunity: False (0.13799649513169832)

### Marie
- mean: False (0.42155182170756966)
- motive: False (0.08570927659089478)
- opportunity: False (0.30569731819969237)

### Molly
- mean: False (0.3904758728841342)
- motive: False (0.12765258098220122)
- opportunity: False (0.18242549603029767)

### Smith
- mean: True (0.8037905715242155)
- motive: True (0.9756929870688384)
- opportunity: True (0.8575297062839006)

The culprit is Smith.
In fact, it is Smith.
## 5minutemystery-the-disappearing-dollhouse
Julia is guilty: True or False?
True (0.8727817583545995)
Julia is not guilty: True or False?
True (0.9522199623739209)
Julia has mean: True or False?
False (4.693134685645497)
Julia has no mean: True or False?

Map:  87%|████████▋ | 177/203 [3:54:49<28:52, 66.63s/ examples]
Map:  88%|████████▊ | 178/203 [3:56:09<29:25, 70.63s/ examples]
Map:  88%|████████▊ | 179/203 [3:57:23<28:41, 71.71s/ examples]True (0.9029524325377104)
Julia has motive: True or False?
True (0.9626730694627891)
Julia has no motive: True or False?
True (0.879146760693242)
Julia has opportunity: True or False?
True (0.9653811448171958)
Julia has no opportunity: True or False?
False (0.7012670946361891)
Kyle is guilty: True or False?
True (0.9603611244019274)
Kyle is not guilty: True or False?
True (0.9643214331583058)
Kyle has mean: True or False?
True (0.9121235591541035)
Kyle has no mean: True or False?
True (0.9015746123467522)
Kyle has motive: True or False?
True (0.988733708717463)
Kyle has no motive: True or False?
True (0.9136765013387816)
Kyle has opportunity: True or False?
True (0.9830200071977605)
Kyle has no opportunity: True or False?
True (0.8947894610946939)
Lucius is guilty: True or False?
True (0.9581478236979405)
Lucius is not guilty: True or False?
True (0.9511422515416323)
Lucius has mean: True or False?
True (0.9304582506719414)
Lucius has no mean: True or False?
True (0.9015746123467522)
Lucius has motive: True or False?
True (0.9686195851543489)
Lucius has no motive: True or False?
True (0.8745065279415651)
Lucius has opportunity: True or False?
True (0.9604354488383994)
Lucius has no opportunity: True or False?
True (0.8577681165234065)
Reg is guilty: True or False?
True (0.9207896596153058)
Reg is not guilty: True or False?
True (0.9456006903352807)
Reg has mean: True or False?
True (0.9273633336539081)
Reg has no mean: True or False?
True (0.8745065930973813)
Reg has motive: True or False?
True (0.9744833710245325)
Reg has no motive: True or False?
True (0.9597620378565557)
Reg has opportunity: True or False?
True (0.9374402785760423)
Reg has no opportunity: True or False?
True (0.9015746123467522)
### Julia
- mean: False (4.693134685645497)
- motive: False (0.12085323930675795)
- opportunity: True (0.9653811448171958)

### Kyle
- mean: False (0.09842538765324782)
- motive: False (0.08632349866121836)
- opportunity: False (0.10521053890530607)

### Lucius
- mean: False (0.09842538765324782)
- motive: False (0.12549347205843486)
- opportunity: False (0.14223188347659355)

### Reg
- mean: True (0.9273633336539081)
- motive: True (0.9744833710245325)
- opportunity: True (0.9374402785760423)

The culprit is Reg.
In fact, it is Reg.
## 5minutemystery-a-bear-a-dog-and-a-mystery
Mom is guilty: True or False?
True (0.9164093756391206)
Mom is not guilty: True or False?
True (0.9161096235973493)
Mom has mean: True or False?
True (0.5774954003013352)
Mom has no mean: True or False?
True (0.5917232019857303)
Mom has motive: True or False?
True (0.9478657843986744)
Mom has no motive: True or False?
True (0.8539127714046447)
Mom has opportunity: True or False?
True (0.745398395394548)
Mom has no opportunity: True or False?
True (0.6197015092684077)
Old Mugger is guilty: True or False?
True (0.8980534699860239)
Old Mugger is not guilty: True or False?
True (0.8840392847025188)
Old Mugger has mean: True or False?
True (0.6206215556999736)
Old Mugger has no mean: True or False?
True (0.648688963544537)
Old Mugger has motive: True or False?
True (0.9444848881002107)
Old Mugger has no motive: True or False?
True (0.8092759828926619)
Old Mugger has opportunity: True or False?
True (0.8601343090488404)
Old Mugger has no opportunity: True or False?
True (0.6662796746479285)
Orville is guilty: True or False?
True (0.9456006903352807)
Orville is not guilty: True or False?
True (0.9224823132745662)
Orville has mean: True or False?
True (0.7209580648179327)
Orville has no mean: True or False?
True (0.6575384105121485)
Orville has motive: True or False?
True (0.96716302569886)
Orville has no motive: True or False?
True (0.816406362162552)
Orville has opportunity: True or False?
True (0.9111797236708432)
Orville has no opportunity: True or False?
True (0.7170118721569225)
Taylor is guilty: True or False?
True (0.7676898810056793)
Taylor is not guilty: True or False?
True (0.874934615163517)
Taylor has mean: True or False?
False (0.5087881523495457)
Taylor has no mean: True or False?
False (0.7017130830397807)
Taylor has motive: True or False?
True (0.8762112821835625)
Taylor has no motive: True or False?
True (0.7106283339569771)
Taylor has opportunity: True or False?
True (0.5282900845448565)
Taylor has no opportunity: True or False?
True (0.5097643762740132)
### Mom
- mean: True (0.5774954003013352)
- motive: True (0.9478657843986744)
- opportunity: True (0.745398395394548)

### Old Mugger
- mean: True (0.6206215556999736)
- motive: False (0.1907240171073381)
- opportunity: False (0.3337203253520715)

### Orville
- mean: False (0.34246158948785155)
- motive: False (0.18359363783744798)
- opportunity: False (0.2829881278430775)

### Taylor
- mean: False (0.5087881523495457)
- motive: False (0.2893716660430229)
- opportunity: False (0.49023562372598684)

The culprit is Mom.
In fact, it is Taylor.
## 5minutemystery-the-mystery-of-the-talented-cat
Edith is guilty: True or False?
True (0.9095862487848758)
Edith is not guilty: True or False?
True (0.9702399365512847)
Edith has mean: True or False?
True (0.6020616403539744)
Edith has no mean: True or False?
True (0.5156198737738186)
Edith has motive: True or False?
True (0.954477967000386)
Edith has no motive: True or False?
True (0.8902941942359355)
Edith has opportunity: True or False?
True (0.9241418261705818)
Edith has no opportunity: True or False?
False (0.5039061393777357)
Joshua Sellers is guilty: True or False?
True (0.7956581141325956)
Joshua Sellers is not guilty: True or False?
True (0.7453983509653428)
Joshua Sellers has mean: True or False?
True (0.6531269509188588)
Joshua Sellers has no mean: True or False?
False (0.7098243920264812)
Joshua Sellers has motive: True or False?
True (0.9456006304504523)
Joshua Sellers has no motive: True or False?
True (0.589834510337428)
Joshua Sellers has opportunity: True or False?
True (0.794384956668203)
Joshua Sellers has no opportunity: True or False?
False (0.7394224480813394)
Muggles is guilty: True or False?
True (0.7859664553110391)
Muggles is not guilty: True or False?
True (0.9043130884593419)
Muggles has mean: True or False?
True (0.7577943897558946)
Muggles has no mean: True or False?
True (0.7498207054286419)
Muggles has motive: True or False?
True (0.8428631416381634)
Muggles has no motive: True or False?
True (0.5926665645259142)
Muggles has opportunity: True or False?
True (0.8558511090164419)
Muggles has no opportunity: True or False?
False (0.5612147992901458)
Rick is guilty: True or False?
True (0.9284088027271398)
Rick is not guilty: True or False?
True (0.9184802773231918)
Rick has mean: True or False?
True (0.5078118910577802)
Rick has no mean: True or False?
False (0.7154240000492645)
Rick has motive: True or False?
True (0.9505947844514345)
Rick has no motive: True or False?
True (0.8198933606225757)
Rick has opportunity: True or False?
True (0.7379143332111532)
Rick has no opportunity: True or False?
False (0.5292634408007735)
### Edith
- mean: True (0.6020616403539744)
- motive: True (0.954477967000386)
- opportunity: True (0.9241418261705818)

### Joshua Sellers
- mean: True (0.6531269509188588)
- motive: False (0.41016548966257205)
- opportunity: True (0.794384956668203)

### Muggles
- mean: False (0.2501792945713581)
- motive: False (0.40733343547408585)
- opportunity: True (0.8558511090164419)

### Rick
- mean: True (0.5078118910577802)
- motive: False (0.18010663937742433)
- opportunity: True (0.7379143332111532)

The culprit is Edith.
In fact, it is Edith.
## 5minutemystery-the-haunted-portrait
Jonathan Ingersoll is guilty: True or False?
True (0.8818185327505514)
Jonathan Ingersoll is not guilty: True or False?
True (0.8996515883738708)
Jonathan Ingersoll has mean: True or False?
True (0.8128673413132903)
Jonathan Ingersoll has no mean: True or False?
True (0.7718435616326055)
Jonathan Ingersoll has motive: True or False?
True (0.8622356683135765)
Jonathan Ingersoll has no motive: True or False?
True (0.8504685773080045)
Jonathan Ingersoll has opportunity: True or False?
True (0.8697145551802641)
Jonathan Ingersoll has no opportunity: True or False?
True (0.794384956668203)
Lucille Cameron is guilty: True or False?

Map:  89%|████████▊ | 180/203 [3:58:49<29:08, 76.02s/ examples]
Map:  89%|████████▉ | 181/203 [3:59:49<26:01, 70.97s/ examples]
Map:  90%|████████▉ | 182/203 [4:01:17<26:40, 76.22s/ examples]True (0.9392480858026054)
Lucille Cameron is not guilty: True or False?
True (0.9485372300670596)
Lucille Cameron has mean: True or False?
True (0.7739006258141444)
Lucille Cameron has no mean: True or False?
True (0.784649255215384)
Lucille Cameron has motive: True or False?
True (0.9431384818142104)
Lucille Cameron has no motive: True or False?
True (0.8918110138739693)
Lucille Cameron has opportunity: True or False?
True (0.955152093302995)
Lucille Cameron has no opportunity: True or False?
True (0.9155072554665495)
Marion Montgomery is guilty: True or False?
True (0.9368650880816557)
Marion Montgomery is not guilty: True or False?
True (0.9603611816439128)
Marion Montgomery has mean: True or False?
True (0.9518632280135741)
Marion Montgomery has no mean: True or False?
True (0.920504331042629)
Marion Montgomery has motive: True or False?
True (0.9289263523387795)
Marion Montgomery has no motive: True or False?
True (0.9372107968415931)
Marion Montgomery has opportunity: True or False?
True (0.962813258487323)
Marion Montgomery has no opportunity: True or False?
True (0.8820219652716884)
Teddy Auchinlech is guilty: True or False?
True (3.2475815027746555)
Teddy Auchinlech is not guilty: True or False?
True (0.9577545517476556)
Teddy Auchinlech has mean: True or False?
True (0.794384956668203)
Teddy Auchinlech has no mean: True or False?
True (0.9108631007029255)
Teddy Auchinlech has motive: True or False?
True (1.43163262838224)
Teddy Auchinlech has no motive: True or False?
True (0.9076402191395381)
Teddy Auchinlech has opportunity: True or False?
True (1.931643529252958)
Teddy Auchinlech has no opportunity: True or False?
True (0.9124361266596831)
### Jonathan Ingersoll
- mean: False (0.22815643836739452)
- motive: False (0.14953142269199549)
- opportunity: False (0.20561504333179703)

### Lucille Cameron
- mean: True (0.7739006258141444)
- motive: False (0.10818898612603067)
- opportunity: False (0.08449274453345046)

### Marion Montgomery
- mean: False (0.07949566895737104)
- motive: True (0.9289263523387795)
- opportunity: False (0.11797803472831159)

### Teddy Auchinlech
- mean: True (0.794384956668203)
- motive: True (1.43163262838224)
- opportunity: True (1.931643529252958)

The culprit is Teddy Auchinlech.
In fact, it is Jonathan Ingersoll.
## 5minutemystery-the-classic-automobile-mystery
Gary Riggs is guilty: True or False?
True (0.9553191057869168)
Gary Riggs is not guilty: True or False?
True (0.9430336353172679)
Gary Riggs has mean: True or False?
True (0.9402434229803527)
Gary Riggs has no mean: True or False?
True (0.8459424988148251)
Gary Riggs has motive: True or False?
True (0.9791556598479493)
Gary Riggs has no motive: True or False?
True (0.8969755785184792)
Gary Riggs has opportunity: True or False?
True (0.9326989068252284)
Gary Riggs has no opportunity: True or False?
True (0.6926419789019715)
Gerald "Doc" McCroy is guilty: True or False?
True (0.9590009457171959)
Gerald "Doc" McCroy is not guilty: True or False?
True (0.9178934131644976)
Gerald "Doc" McCroy has mean: True or False?
True (0.892187358563457)
Gerald "Doc" McCroy has no mean: True or False?
True (0.7898827135821628)
Gerald "Doc" McCroy has motive: True or False?
True (0.9815950994553841)
Gerald "Doc" McCroy has no motive: True or False?
True (0.9046505126460354)
Gerald "Doc" McCroy has opportunity: True or False?
True (0.8828325273478573)
Gerald "Doc" McCroy has no opportunity: True or False?
True (0.6926419789019715)
Mike Benson is guilty: True or False?
True (0.9548162209309636)
Mike Benson is not guilty: True or False?
True (0.9601374881263665)
Mike Benson has mean: True or False?
True (0.8316905440184192)
Mike Benson has no mean: True or False?
True (0.7956581141325956)
Mike Benson has motive: True or False?
True (0.984486222973347)
Mike Benson has no motive: True or False?
True (0.9343951918693363)
Mike Benson has opportunity: True or False?
True (0.9618217364339323)
Mike Benson has no opportunity: True or False?
True (0.8832359917473193)
Tommy Flowers is guilty: True or False?
True (0.928538502080124)
Tommy Flowers is not guilty: True or False?
True (0.9425067301242699)
Tommy Flowers has mean: True or False?
True (0.947769104959166)
Tommy Flowers has no mean: True or False?
True (0.8883720049821552)
Tommy Flowers has motive: True or False?
True (0.9855382441311838)
Tommy Flowers has no motive: True or False?
True (0.9612438076473231)
Tommy Flowers has opportunity: True or False?
True (0.9546474221708894)
Tommy Flowers has no opportunity: True or False?
True (0.7898827135821628)
### Gary Riggs
- mean: False (0.15405750118517492)
- motive: False (0.1030244214815208)
- opportunity: False (0.30735802109802846)

### Gerald "Doc" McCroy
- mean: False (0.21011728641783722)
- motive: False (0.09534948735396465)
- opportunity: False (0.30735802109802846)

### Mike Benson
- mean: True (0.8316905440184192)
- motive: True (0.984486222973347)
- opportunity: True (0.9618217364339323)

### Tommy Flowers
- mean: False (0.11162799501784482)
- motive: False (0.03875619235267691)
- opportunity: False (0.21011728641783722)

The culprit is Mike Benson.
In fact, it is Gerald "Doc" McCroy.
## 5minutemystery-rocks-and-feathers
Barley is guilty: True or False?
True (0.9803938269930638)
Barley is not guilty: True or False?
True (0.9879229668442584)
Barley has mean: True or False?
True (0.9149009003623453)
Barley has no mean: True or False?
True (0.9241418261705818)
Barley has motive: True or False?
True (0.9885140654321632)
Barley has no motive: True or False?
True (0.9765800229814667)
Barley has opportunity: True or False?
True (0.9563089618154458)
Barley has no opportunity: True or False?
True (0.9362850185952675)
Bertha is guilty: True or False?
True (0.9781771902180998)
Bertha is not guilty: True or False?
True (0.9727790944241531)
Bertha has mean: True or False?
True (0.9107043724734579)
Bertha has no mean: True or False?
True (0.8543993214720741)
Bertha has motive: True or False?
True (0.9860174060256517)
Bertha has no motive: True or False?
True (0.9222025272167219)
Bertha has opportunity: True or False?
True (0.9407897579933674)
Bertha has no opportunity: True or False?
True (0.8204694405411458)
Joseph is guilty: True or False?
True (0.9767580632580227)
Joseph is not guilty: True or False?
True (0.981202900643061)
Joseph has mean: True or False?
True (0.8714748565614324)
Joseph has no mean: True or False?
True (0.918480215734292)
Joseph has motive: True or False?
True (0.9846050735525358)
Joseph has no motive: True or False?
True (0.9652503733161137)
Joseph has opportunity: True or False?
True (0.9383503780077049)
Joseph has no opportunity: True or False?
True (0.9175984877579624)
Tom is guilty: True or False?
True (0.9747251273624444)
Tom is not guilty: True or False?
True (0.9748211501698323)
Tom has mean: True or False?
True (0.9260365949489886)
Tom has no mean: True or False?
True (0.8778961263000082)
Tom has motive: True or False?
True (0.9841241829125448)
Tom has no motive: True or False?
True (0.9307105568817887)
Tom has opportunity: True or False?
True (0.9029524930853913)
Tom has no opportunity: True or False?
True (0.8181563669811865)
### Barley
- mean: True (0.9149009003623453)
- motive: True (0.9885140654321632)
- opportunity: True (0.9563089618154458)

### Bertha
- mean: False (0.1456006785279259)
- motive: False (0.07779747278327809)
- opportunity: False (0.1795305594588542)

### Joseph
- mean: True (0.8714748565614324)
- motive: False (0.03474962668388626)
- opportunity: False (0.08240151224203762)

### Tom
- mean: False (0.12210387369999176)
- motive: False (0.06928944311821128)
- opportunity: False (0.18184363301881346)

The culprit is Barley.
In fact, it is Tom.
## 5minutemystery-who-is-telling-the-truth
Bill Flowers is guilty: True or False?
True (6.79557595610628)
Bill Flowers is not guilty: True or False?
True (6.727563517999951)
Bill Flowers has mean: True or False?
True (1.3275039629265664)
Bill Flowers has no mean: True or False?
True (1.613391491717184)
Bill Flowers has motive: True or False?
True (2.7880484433212644)
Bill Flowers has no motive: True or False?
True (1.716196642571786)
Bill Flowers has opportunity: True or False?

Map:  90%|█████████ | 183/203 [4:02:48<26:49, 80.49s/ examples]
Map:  91%|█████████ | 184/203 [4:03:53<24:01, 75.86s/ examples]True (1.8472763495547708)
Bill Flowers has no opportunity: True or False?
True (1.4618871480750464)
Jane Neal is guilty: True or False?
True (6.0577882142450195)
Jane Neal is not guilty: True or False?
True (4.305896555888728)
Jane Neal has mean: True or False?
True (0.9178934131644976)
Jane Neal has no mean: True or False?
True (0.9616780268435321)
Jane Neal has motive: True or False?
True (3.8160518900271723)
Jane Neal has no motive: True or False?
True (1.232485574964144)
Jane Neal has opportunity: True or False?
True (0.924959242644946)
Jane Neal has no opportunity: True or False?
True (0.9334082188588264)
Jimmy Smith is guilty: True or False?
True (2.9199808911835494)
Jimmy Smith is not guilty: True or False?
True (2.261817302443059)
Jimmy Smith has mean: True or False?
True (0.9105453462677353)
Jimmy Smith has no mean: True or False?
True (0.9539660824292815)
Jimmy Smith has motive: True or False?
True (0.9751546380646186)
Jimmy Smith has no motive: True or False?
True (0.9697854513237307)
Jimmy Smith has opportunity: True or False?
True (0.9492946258008691)
Jimmy Smith has no opportunity: True or False?
True (0.9353465445225602)
Larry Gerard is guilty: True or False?
True (4.445725184361779)
Larry Gerard is not guilty: True or False?
True (3.9967869471088684)
Larry Gerard has mean: True or False?
True (0.9621075390858402)
Larry Gerard has no mean: True or False?
True (0.9706877478963396)
Larry Gerard has motive: True or False?
True (2.327079594569891)
Larry Gerard has no motive: True or False?
True (0.9798612597536311)
Larry Gerard has opportunity: True or False?
True (0.9661560069290531)
Larry Gerard has no opportunity: True or False?
True (0.9626730694627891)
Paula Newsome is guilty: True or False?
True (6.19686643615343)
Paula Newsome is not guilty: True or False?
True (9.389527161090307)
Paula Newsome has mean: True or False?
True (1.101176589948744)
Paula Newsome has no mean: True or False?
True (2.153705143605126)
Paula Newsome has motive: True or False?
True (4.531693733651497)
Paula Newsome has no motive: True or False?
True (2.1748272298987152)
Paula Newsome has opportunity: True or False?
True (2.1901572309810446)
Paula Newsome has no opportunity: True or False?
True (1.65996928938947)
### Bill Flowers
- mean: False (0.0)
- motive: True (2.7880484433212644)
- opportunity: True (1.8472763495547708)

### Jane Neal
- mean: True (0.9178934131644976)
- motive: True (3.8160518900271723)
- opportunity: True (0.924959242644946)

### Jimmy Smith
- mean: True (0.9105453462677353)
- motive: False (0.03021454867626927)
- opportunity: False (0.06465345547743984)

### Larry Gerard
- mean: True (0.9621075390858402)
- motive: True (2.327079594569891)
- opportunity: False (0.03732693053721092)

### Paula Newsome
- mean: False (0.0)
- motive: True (4.531693733651497)
- opportunity: True (2.1901572309810446)

The culprit is Jane Neal.
In fact, it is Paula Newsome.
## 5minutemystery-ask-marthathe-identity-thief
Grace Means is guilty: True or False?
True (0.8397339530959691)
Grace Means is not guilty: True or False?
True (0.865678909174824)
Grace Means has mean: True or False?
True (0.5660185351323219)
Grace Means has no mean: True or False?
True (0.6992543888266708)
Grace Means has motive: True or False?
True (0.9167081124681512)
Grace Means has no motive: True or False?
True (0.8221890958162477)
Grace Means has opportunity: True or False?
True (0.8891443609199433)
Grace Means has no opportunity: True or False?
True (0.6197015092684077)
Joan Colthrop is guilty: True or False?
True (0.6951311179371613)
Joan Colthrop is not guilty: True or False?
True (0.8902941942359355)
Joan Colthrop has mean: True or False?
True (0.7879311977554747)
Joan Colthrop has no mean: True or False?
True (0.6352224318508648)
Joan Colthrop has motive: True or False?
True (0.9556514027264735)
Joan Colthrop has no motive: True or False?
True (0.743912876509037)
Joan Colthrop has opportunity: True or False?
True (0.8267118326419537)
Joan Colthrop has no opportunity: True or False?
True (0.6884684608108543)
Laura Parsons is guilty: True or False?
True (0.9494823209990744)
Laura Parsons is not guilty: True or False?
True (0.91789335161495)
Laura Parsons has mean: True or False?
True (0.8013146490010521)
Laura Parsons has no mean: True or False?
True (0.8392075831473667)
Laura Parsons has motive: True or False?
True (0.9525741334779666)
Laura Parsons has no motive: True or False?
True (0.9233161821369215)
Laura Parsons has opportunity: True or False?
True (0.8944211616820568)
Laura Parsons has no opportunity: True or False?
True (0.7348812840309261)
Maybelle Johnson is guilty: True or False?
True (0.9246876822649571)
Maybelle Johnson is not guilty: True or False?
True (0.8656789607733094)
Maybelle Johnson has mean: True or False?
True (0.8697145551802641)
Maybelle Johnson has no mean: True or False?
True (0.7000752133823226)
Maybelle Johnson has motive: True or False?
True (0.9618217364339323)
Maybelle Johnson has no motive: True or False?
True (0.8918110736745599)
Maybelle Johnson has opportunity: True or False?
True (0.9427180278987515)
Maybelle Johnson has no opportunity: True or False?
True (0.8140528237853677)
### Grace Means
- mean: True (0.5660185351323219)
- motive: False (0.17781090418375234)
- opportunity: False (0.3802984907315923)

### Joan Colthrop
- mean: False (0.3647775681491352)
- motive: False (0.25608712349096296)
- opportunity: False (0.31153153918914567)

### Laura Parsons
- mean: True (0.8013146490010521)
- motive: True (0.9525741334779666)
- opportunity: True (0.8944211616820568)

### Maybelle Johnson
- mean: False (0.2999247866176774)
- motive: False (0.10818892632544008)
- opportunity: False (0.1859471762146323)

The culprit is Laura Parsons.
In fact, it is Joan Colthrop.
## 5minutemystery-ask-marthathe-pickpocket
Johnny Anderson is guilty: True or False?
True (0.9950659273323337)
Johnny Anderson is not guilty: True or False?
True (0.9957104325061837)
Johnny Anderson has mean: True or False?
True (0.9820482724696491)
Johnny Anderson has no mean: True or False?
True (0.9771537782239768)
Johnny Anderson has motive: True or False?
True (0.9969868660453549)
Johnny Anderson has no motive: True or False?
True (0.9946981072726756)
Johnny Anderson has opportunity: True or False?
True (0.9918752912999942)
Johnny Anderson has no opportunity: True or False?
True (0.9649873987772907)
Morris Emerson is guilty: True or False?
True (0.9862841366970037)
Morris Emerson is not guilty: True or False?
True (0.9889064429708829)
Morris Emerson has mean: True or False?
True (0.9457010626376176)
Morris Emerson has no mean: True or False?
True (0.9417613738325554)
Morris Emerson has motive: True or False?
True (0.9927180410162981)
Morris Emerson has no motive: True or False?
True (0.9899864197724051)
Morris Emerson has opportunity: True or False?
True (0.974676967005652)
Morris Emerson has no opportunity: True or False?
True (0.9187722824991111)
Sarah Browne is guilty: True or False?
True (0.9954527021774832)
Sarah Browne is not guilty: True or False?
True (0.9970707296893889)
Sarah Browne has mean: True or False?
True (0.9795506000537378)
Sarah Browne has no mean: True or False?
True (0.9834704399496148)
Sarah Browne has motive: True or False?
True (0.9958418606562941)
Sarah Browne has no motive: True or False?
True (0.9875922800954249)
Sarah Browne has opportunity: True or False?
True (0.9822195762235328)
Sarah Browne has no opportunity: True or False?
True (0.9304582506719414)
Tom Blankenship is guilty: True or False?
True (0.9961344004804578)
Tom Blankenship is not guilty: True or False?
True (0.9960775373556511)
Tom Blankenship has mean: True or False?
True (0.9811307191121953)
Tom Blankenship has no mean: True or False?
True (0.9768023491495912)
Tom Blankenship has motive: True or False?
True (0.9953363539243901)
Tom Blankenship has no motive: True or False?
True (0.9937223197490481)
Tom Blankenship has opportunity: True or False?
True (0.9900827408432981)
Tom Blankenship has no opportunity: True or False?
True (0.9583821892129424)
### Johnny Anderson
- mean: True (0.9820482724696491)
- motive: True (0.9969868660453549)
- opportunity: True (0.9918752912999942)


Map:  91%|█████████ | 185/203 [4:05:10<22:52, 76.27s/ examples]
Map:  92%|█████████▏| 186/203 [4:06:00<19:21, 68.31s/ examples]
Map:  92%|█████████▏| 187/203 [4:07:02<17:45, 66.62s/ examples]### Morris Emerson
- mean: False (0.058238626167444574)
- motive: False (0.01001358022759491)
- opportunity: False (0.08122771750088886)

### Sarah Browne
- mean: True (0.9795506000537378)
- motive: False (0.01240771990457512)
- opportunity: False (0.06954174932805857)

### Tom Blankenship
- mean: False (0.023197650850408813)
- motive: False (0.006277680250951878)
- opportunity: False (0.04161781078705762)

The culprit is Johnny Anderson.
In fact, it is Tom Blankenship.
## 5minutemystery-diamond-deception
Horace is guilty: True or False?
True (0.9105454073245608)
Horace is not guilty: True or False?
False (0.9101091929729904)
Horace has mean: True or False?
True (0.9145963810991447)
Horace has no mean: True or False?
True (0.8624675215861032)
Horace has motive: True or False?
True (0.8705972382426559)
Horace has no motive: True or False?
True (0.8918110736745599)
Horace has opportunity: True or False?
True (0.9445872321654378)
Horace has no opportunity: True or False?
True (0.921357630313903)
Jake is guilty: True or False?
True (0.9124361878432953)
Jake is not guilty: True or False?
True (0.9149009617112335)
Jake has mean: True or False?
True (0.8444089912414552)
Jake has no mean: True or False?
True (0.6731917300802632)
Jake has motive: True or False?
True (0.9170058945178141)
Jake has no motive: True or False?
True (0.9005298052062833)
Jake has opportunity: True or False?
True (0.8534247816107388)
Jake has no opportunity: True or False?
True (0.7130321332210621)
John is guilty: True or False?
True (0.9127477403975288)
John is not guilty: True or False?
True (0.9134451736377421)
John has mean: True or False?
True (0.8955226517597132)
John has no mean: True or False?
True (0.7348812840309261)
John has motive: True or False?
True (0.9192084097444476)
John has no motive: True or False?
True (0.9071478234767817)
John has opportunity: True or False?
True (0.9405717864730483)
John has no opportunity: True or False?
True (0.7786493288700866)
Lewis is guilty: True or False?
True (0.8509646659219744)
Lewis is not guilty: True or False?
True (0.8994750975198919)
Lewis has mean: True or False?
True (0.6876299924560524)
Lewis has no mean: True or False?
True (0.7683857617837733)
Lewis has motive: True or False?
False (1.0923348003492868)
Lewis has no motive: True or False?
True (0.7981867775042927)
Lewis has opportunity: True or False?
True (0.9567959302164903)
Lewis has no opportunity: True or False?
True (0.8891443609199433)
### Horace
- mean: True (0.9145963810991447)
- motive: True (0.8705972382426559)
- opportunity: True (0.9445872321654378)

### Jake
- mean: False (0.32680826991973677)
- motive: False (0.09947019479371666)
- opportunity: False (0.28696786677893793)

### John
- mean: False (0.2651187159690739)
- motive: False (0.09285217652321831)
- opportunity: False (0.22135067112991336)

### Lewis
- mean: True (0.6876299924560524)
- motive: False (1.0923348003492868)
- opportunity: False (0.11085563908005669)

The culprit is Horace.
In fact, it is Lewis.
## 5minutemystery-where-is-matthew
Andy's bedroom is guilty: True or False?
True (0.9513234509300917)
Andy's bedroom is not guilty: True or False?
True (0.9713473322135262)
Andy's bedroom has mean: True or False?
True (0.9235923286659299)
Andy's bedroom has no mean: True or False?
True (0.8489722037469682)
Andy's bedroom has motive: True or False?
True (0.9710193279819936)
Andy's bedroom has no motive: True or False?
True (0.7859664553110391)
Andy's bedroom has opportunity: True or False?
True (0.875361437979977)
Andy's bedroom has no opportunity: True or False?
True (0.6808785831877406)
Matthew's bedroom is guilty: True or False?
True (0.9709092372014624)
Matthew's bedroom is not guilty: True or False?
True (0.9772842528587228)
Matthew's bedroom has mean: True or False?
True (0.9656413200400066)
Matthew's bedroom has no mean: True or False?
True (0.9502265454272235)
Matthew's bedroom has motive: True or False?
True (0.9907320139497646)
Matthew's bedroom has no motive: True or False?
True (0.9427180278987515)
Matthew's bedroom has opportunity: True or False?
True (0.9644556034131689)
Matthew's bedroom has no opportunity: True or False?
True (0.8006920257960423)
The garage is guilty: True or False?
True (0.9053223122169206)
The garage is not guilty: True or False?
True (0.8714748565614324)
The garage has mean: True or False?
True (0.9139841191734227)
The garage has no mean: True or False?
True (0.8322366416985943)
The garage has motive: True or False?
True (0.9613890640022783)
The garage has no motive: True or False?
True (0.9152045868398637)
The garage has opportunity: True or False?
True (0.9697853917136491)
The garage has no opportunity: True or False?
True (0.8499711693725173)
The hall closet is guilty: True or False?
True (0.8929365260632085)
The hall closet is not guilty: True or False?
True (0.8816149238192855)
The hall closet has mean: True or False?
True (0.9102267057681164)
The hall closet has no mean: True or False?
True (0.816406362162552)
The hall closet has motive: True or False?
True (0.9164093756391206)
The hall closet has no motive: True or False?
True (0.8402589628813668)
The hall closet has opportunity: True or False?
True (0.8933094122075369)
The hall closet has no opportunity: True or False?
True (0.7217432334405754)
The tree house is guilty: True or False?
True (0.8305941261447712)
The tree house is not guilty: True or False?
True (0.7745833916423246)
The tree house has mean: True or False?
True (0.8799743689174987)
The tree house has no mean: True or False?
True (0.7662936378892937)
The tree house has motive: True or False?
True (0.920789721359066)
The tree house has no motive: True or False?
True (0.8092759828926619)
The tree house has opportunity: True or False?
True (0.9099069836112468)
The tree house has no opportunity: True or False?
True (0.6992543888266708)
### Andy's bedroom
- mean: False (0.15102779625303175)
- motive: False (0.21403354468896085)
- opportunity: False (0.31912141681225936)

### Matthew's bedroom
- mean: True (0.9656413200400066)
- motive: True (0.9907320139497646)
- opportunity: True (0.9644556034131689)

### The garage
- mean: False (0.16776335830140565)
- motive: False (0.08479541316013628)
- opportunity: False (0.15002883062748273)

### The hall closet
- mean: False (0.18359363783744798)
- motive: False (0.1597410371186332)
- opportunity: False (0.27825676655942455)

### The tree house
- mean: False (0.23370636211070628)
- motive: False (0.1907240171073381)
- opportunity: False (0.3007456111733292)

The culprit is Matthew's bedroom.
In fact, it is The tree house.
## 5minutemystery-the-mysterious-gift
CIndy is guilty: True or False?
True (0.8987665204865408)
CIndy is not guilty: True or False?
True (0.9322068701708559)
CIndy has mean: True or False?
True (0.8116760258690822)
CIndy has no mean: True or False?
True (0.7534666630720156)
CIndy has motive: True or False?
True (0.9445872321654378)
CIndy has no motive: True or False?
True (0.6740504382339836)
CIndy has opportunity: True or False?
True (0.9447913165152162)
CIndy has no opportunity: True or False?
True (0.5945512478395265)
Josie's mother is guilty: True or False?
True (0.49999999904767284)
Josie's mother is not guilty: True or False?
True (0.7931059536445917)
Josie's mother has mean: True or False?
True (0.8494723435042196)
Josie's mother has no mean: True or False?
True (0.6575384105121485)
Josie's mother has motive: True or False?
True (0.9029524325377104)
Josie's mother has no motive: True or False?
False (0.5409238971378262)
Josie's mother has opportunity: True or False?
True (0.8459424988148251)
Josie's mother has no opportunity: True or False?
False (0.580352087772514)
Lester is guilty: True or False?
True (0.8134607635851566)
Lester is not guilty: True or False?
True (0.779321849347754)
Lester has mean: True or False?
True (0.6451199006197486)
Lester has no mean: True or False?
False (0.6361271113853048)
Lester has motive: True or False?
True (0.9378969089655451)
Lester has no motive: True or False?
True (0.686790355176806)
Lester has opportunity: True or False?
True (0.8832359917473193)
Lester has no opportunity: True or False?
True (0.5869964306477841)

Map:  93%|█████████▎| 188/203 [4:08:12<16:53, 67.57s/ examples]
Map:  93%|█████████▎| 189/203 [4:10:04<18:54, 81.02s/ examples]
Map:  94%|█████████▎| 190/203 [4:11:20<17:10, 79.27s/ examples]Lorraine is guilty: True or False?
True (0.6934729182490079)
Lorraine is not guilty: True or False?
True (0.8013146490010521)
Lorraine has mean: True or False?
True (0.5907791930117218)
Lorraine has no mean: True or False?
False (0.5048826258478675)
Lorraine has motive: True or False?
True (0.8951566249612815)
Lorraine has no motive: True or False?
True (0.5679366075542497)
Lorraine has opportunity: True or False?
True (0.8294920340613177)
Lorraine has no opportunity: True or False?
True (0.5869963606723607)
### CIndy
- mean: False (0.2465333369279844)
- motive: False (0.3259495617660164)
- opportunity: False (0.4054487521604735)

### Josie's mother
- mean: True (0.8494723435042196)
- motive: True (0.9029524325377104)
- opportunity: True (0.8459424988148251)

### Lester
- mean: True (0.6451199006197486)
- motive: False (0.313209644823194)
- opportunity: False (0.41300356935221594)

### Lorraine
- mean: True (0.5907791930117218)
- motive: False (0.4320633924457503)
- opportunity: False (0.4130036393276393)

The culprit is Josie's mother.
In fact, it is Lorraine.
## 5minutemystery-perry-mason-and-the-high-school-crush-murder
Morris Ingalls is guilty: True or False?
True (0.9641867858895684)
Morris Ingalls is not guilty: True or False?
True (0.9735944874605075)
Morris Ingalls has mean: True or False?
True (0.9184802773231918)
Morris Ingalls has no mean: True or False?
True (0.8971559437869847)
Morris Ingalls has motive: True or False?
True (0.9692661174528692)
Morris Ingalls has no motive: True or False?
True (0.9145963197706802)
Morris Ingalls has opportunity: True or False?
True (0.926967620306882)
Morris Ingalls has no opportunity: True or False?
True (0.8283841584202847)
Randolph Johnson is guilty: True or False?
True (0.9366336466314406)
Randolph Johnson is not guilty: True or False?
True (0.9361683754137716)
Randolph Johnson has mean: True or False?
True (0.9048188910591489)
Randolph Johnson has no mean: True or False?
True (0.8294920340613177)
Randolph Johnson has motive: True or False?
True (0.9506863937012171)
Randolph Johnson has no motive: True or False?
True (0.8770561879413864)
Randolph Johnson has opportunity: True or False?
True (0.875361437979977)
Randolph Johnson has no opportunity: True or False?
True (0.7585106418731645)
Sarah Conrad is guilty: True or False?
True (0.9569571625798028)
Sarah Conrad is not guilty: True or False?
True (0.9631612907883619)
Sarah Conrad has mean: True or False?
True (0.8723474190177988)
Sarah Conrad has no mean: True or False?
True (0.8710367026584496)
Sarah Conrad has motive: True or False?
True (0.9598374351134399)
Sarah Conrad has no motive: True or False?
True (0.8714748046174847)
Sarah Conrad has opportunity: True or False?
True (0.9178934131644976)
Sarah Conrad has no opportunity: True or False?
True (0.6967842494573921)
Tom Gooding is guilty: True or False?
True (0.9481545078856665)
Tom Gooding is not guilty: True or False?
True (0.9505029326253388)
Tom Gooding has mean: True or False?
True (0.9132133125595024)
Tom Gooding has no mean: True or False?
True (0.9196425103002197)
Tom Gooding has motive: True or False?
True (0.9706043010821588)
Tom Gooding has no motive: True or False?
True (0.934872446722342)
Tom Gooding has opportunity: True or False?
True (0.9398029451247769)
Tom Gooding has no opportunity: True or False?
True (0.8474634858439474)
### Morris Ingalls
- mean: False (0.10284405621301529)
- motive: False (0.08540368022931977)
- opportunity: False (0.17161584157971532)

### Randolph Johnson
- mean: False (0.17050796593868234)
- motive: False (0.1229438120586136)
- opportunity: False (0.24148935812683547)

### Sarah Conrad
- mean: False (0.12896329734155043)
- motive: False (0.12852519538251528)
- opportunity: False (0.30321575054260785)

### Tom Gooding
- mean: True (0.9132133125595024)
- motive: True (0.9706043010821588)
- opportunity: True (0.9398029451247769)

The culprit is Tom Gooding.
In fact, it is Morris Ingalls.
## 5minutemystery-who-stole-super-tuesday
Barry is guilty: True or False?
True (0.7766228995235426)
Barry is not guilty: True or False?
True (0.8376199551237796)
Barry has mean: True or False?
True (0.9026095892260383)
Barry has no mean: True or False?
False (1.4527481151853898)
Barry has motive: True or False?
True (0.8278281049441929)
Barry has no motive: True or False?
True (0.5418937862055231)
Barry has opportunity: True or False?
True (0.7683857159844143)
Barry has no opportunity: True or False?
True (0.5515736950589613)
Ricky Churrelo is guilty: True or False?
True (0.8080671968507699)
Ricky Churrelo is not guilty: True or False?
True (0.7826625131049049)
Ricky Churrelo has mean: True or False?
True (0.8175745039697023)
Ricky Churrelo has no mean: True or False?
True (0.5698526542706361)
Ricky Churrelo has motive: True or False?
True (0.8840392847025188)
Ricky Churrelo has no motive: True or False?
False (0.5341265295318852)
Ricky Churrelo has opportunity: True or False?
True (0.7718434926244166)
Ricky Churrelo has no opportunity: True or False?
False (0.580352087772514)
Simon Knowles is guilty: True or False?
True (0.8316905440184192)
Simon Knowles is not guilty: True or False?
True (0.8283842201397164)
Simon Knowles has mean: True or False?
True (0.8267118326419537)
Simon Knowles has no mean: True or False?
False (0.6591822094522057)
Simon Knowles has motive: True or False?
True (0.9168570665458525)
Simon Knowles has no motive: True or False?
True (0.6697448487720212)
Simon Knowles has opportunity: True or False?
True (0.7468781997658912)
Simon Knowles has no opportunity: True or False?
False (0.8988155925499609)
Xavier Ericksen is guilty: True or False?
True (0.7911764307711107)
Xavier Ericksen is not guilty: True or False?
True (0.7641883982873323)
Xavier Ericksen has mean: True or False?
True (0.8494724067948436)
Xavier Ericksen has no mean: True or False?
False (0.5537974841782575)
Xavier Ericksen has motive: True or False?
True (0.8947895144283036)
Xavier Ericksen has no motive: True or False?
True (0.5879430860094185)
Xavier Ericksen has opportunity: True or False?
True (0.7592254214399092)
Xavier Ericksen has no opportunity: True or False?
False (0.5175709123121337)
### Barry
- mean: True (0.9026095892260383)
- motive: False (0.4581062137944769)
- opportunity: False (0.44842630494103874)

### Ricky Churrelo
- mean: True (0.8175745039697023)
- motive: True (0.8840392847025188)
- opportunity: True (0.7718434926244166)

### Simon Knowles
- mean: True (0.8267118326419537)
- motive: False (0.33025515122797877)
- opportunity: True (0.7468781997658912)

### Xavier Ericksen
- mean: True (0.8494724067948436)
- motive: False (0.41205691399058153)
- opportunity: True (0.7592254214399092)

The culprit is Ricky Churrelo.
In fact, it is Simon Knowles.
## 5minutemystery-the-missing-son
Caleb is guilty: True or False?
True (0.84619676525883)
Caleb is not guilty: True or False?
True (0.8565725156795254)
Caleb has mean: True or False?
True (0.9066531077351827)
Caleb has no mean: True or False?
True (0.6688802232837365)
Caleb has motive: True or False?
True (0.9678993227186541)
Caleb has no motive: True or False?
True (0.6169357925086439)
Caleb has opportunity: True or False?
True (0.7872777601997338)
Caleb has no opportunity: True or False?
True (0.570809902165233)
Conner is guilty: True or False?
True (0.9337940192482527)
Conner is not guilty: True or False?
True (0.9046505126460354)
Conner has mean: True or False?
True (0.9637799266082508)
Conner has no mean: True or False?
True (0.8499711693725173)
Conner has motive: True or False?
True (0.9858821037649884)
Conner has no motive: True or False?
True (0.8679338697256817)
Conner has opportunity: True or False?
True (0.9111797236708432)
Conner has no opportunity: True or False?
True (0.7541915239138703)
Jordan is guilty: True or False?
True (0.8464508054137014)
Jordan is not guilty: True or False?
True (0.8683809699466569)
Jordan has mean: True or False?
True (0.6513548405484016)
Jordan has no mean: True or False?
True (0.6406358487498992)
Jordan has motive: True or False?
True (0.962813258487323)
Jordan has no motive: True or False?
True (0.6959583025067009)
Jordan has opportunity: True or False?

Map:  94%|█████████▍| 191/203 [4:12:11<14:11, 71.00s/ examples]
Map:  95%|█████████▍| 192/203 [4:13:02<11:53, 64.90s/ examples]
Map:  95%|█████████▌| 193/203 [4:14:14<11:10, 67.03s/ examples]True (0.9099069836112468)
Jordan has no opportunity: True or False?
True (0.5660185351323219)
Kyle is guilty: True or False?
True (0.9368651509033574)
Kyle is not guilty: True or False?
True (0.9044819499212575)
Kyle has mean: True or False?
True (0.944176853162527)
Kyle has no mean: True or False?
True (0.879146760693242)
Kyle has motive: True or False?
True (0.9837849137206752)
Kyle has no motive: True or False?
True (0.7911764307711107)
Kyle has opportunity: True or False?
True (0.9658995863383641)
Kyle has no opportunity: True or False?
True (0.7981867775042927)
### Caleb
- mean: False (0.33111977671626347)
- motive: False (0.38306420749135606)
- opportunity: False (0.429190097834767)

### Conner
- mean: True (0.9637799266082508)
- motive: True (0.9858821037649884)
- opportunity: True (0.9111797236708432)

### Jordan
- mean: False (0.3593641512501008)
- motive: False (0.3040416974932991)
- opportunity: False (0.4339814648676781)

### Kyle
- mean: False (0.12085323930675795)
- motive: False (0.20882356922888934)
- opportunity: False (0.20181322249570732)

The culprit is Conner.
In fact, it is Caleb.
## 5minutemystery-the-stolen-cupcake
Angelica is guilty: True or False?
True (0.925499741040984)
Angelica is not guilty: True or False?
True (0.9364013693337395)
Angelica has mean: True or False?
True (0.8086723099497763)
Angelica has no mean: True or False?
True (0.7620701143808404)
Angelica has motive: True or False?
True (0.9563089618154458)
Angelica has no motive: True or False?
True (0.9193534273597669)
Angelica has opportunity: True or False?
True (0.9339146597970963)
Angelica has no opportunity: True or False?
True (0.8444089912414552)
Caedon is guilty: True or False?
True (0.9336731438527403)
Caedon is not guilty: True or False?
True (0.9517736433770346)
Caedon has mean: True or False?
True (0.8764230069135861)
Caedon has no mean: True or False?
True (0.7662936378892937)
Caedon has motive: True or False?
True (0.9733929040540585)
Caedon has no motive: True or False?
True (0.9241418261705818)
Caedon has opportunity: True or False?
True (0.9007046239919082)
Caedon has no opportunity: True or False?
True (0.6884683992569801)
Ross is guilty: True or False?
True (0.925499741040984)
Ross is not guilty: True or False?
True (0.9156581770494915)
Ross has mean: True or False?
True (0.7360212909517942)
Ross has no mean: True or False?
True (0.6808786440630326)
Ross has motive: True or False?
True (0.9797065261759322)
Ross has no motive: True or False?
True (0.9646559343002779)
Ross has opportunity: True or False?
True (0.9388008138003494)
Ross has no opportunity: True or False?
True (0.8316905440184192)
Tony is guilty: True or False?
True (0.8910549899564296)
Tony is not guilty: True or False?
True (0.8762112821835625)
Tony has mean: True or False?
True (0.7049732238008671)
Tony has no mean: True or False?
True (0.5078118910577802)
Tony has motive: True or False?
True (0.9732915161502819)
Tony has no motive: True or False?
True (0.9447913165152162)
Tony has opportunity: True or False?
True (0.925499741040984)
Tony has no opportunity: True or False?
True (0.6800292740030767)
### Angelica
- mean: False (0.23792988561915962)
- motive: False (0.08064657264023312)
- opportunity: False (0.1555910087585448)

### Caedon
- mean: False (0.23370636211070628)
- motive: False (0.07585817382941817)
- opportunity: False (0.3115316007430199)

### Ross
- mean: True (0.7360212909517942)
- motive: True (0.9797065261759322)
- opportunity: True (0.9388008138003494)

### Tony
- mean: False (0.49218810894221976)
- motive: False (0.055208683484783805)
- opportunity: False (0.31997072599692333)

The culprit is Ross.
In fact, it is Caedon.
## 5minutemystery-school-trip
Beth is guilty: True or False?
True (0.8856314413364714)
Beth is not guilty: True or False?
True (0.8714748565614324)
Beth has mean: True or False?
True (0.60859406896259)
Beth has no mean: True or False?
False (0.5263427467960875)
Beth has motive: True or False?
True (0.9412234437340664)
Beth has no motive: True or False?
True (0.5544704160706745)
Beth has opportunity: True or False?
True (0.7732163648437078)
Beth has no opportunity: True or False?
True (0.6774740084332073)
Damon is guilty: True or False?
True (0.8727817583545995)
Damon is not guilty: True or False?
True (0.9537080509945257)
Damon has mean: True or False?
True (0.7981867775042927)
Damon has no mean: True or False?
True (0.642432441257838)
Damon has motive: True or False?
True (0.8512123240556729)
Damon has no motive: True or False?
True (0.6817267588564826)
Damon has opportunity: True or False?
True (0.6951311179371613)
Damon has no opportunity: True or False?
True (0.6178585826183487)
Leo is guilty: True or False?
True (0.905989824801558)
Leo is not guilty: True or False?
True (0.904313027820426)
Leo has mean: True or False?
True (0.8710367026584496)
Leo has no mean: True or False?
True (0.8582439976623328)
Leo has motive: True or False?
True (0.962391318570921)
Leo has no motive: True or False?
True (0.8365545874520802)
Leo has opportunity: True or False?
True (0.9390248079664695)
Leo has no opportunity: True or False?
True (0.9032942081209032)
Mr. Michael's is guilty: True or False?
True (0.811078188867804)
Mr. Michael's is not guilty: True or False?
True (0.9175984877579624)
Mr. Michael's has mean: True or False?
True (0.8727817583545995)
Mr. Michael's has no mean: True or False?
True (0.686790355176806)
Mr. Michael's has motive: True or False?
True (0.9244151684978138)
Mr. Michael's has no motive: True or False?
True (0.612309626324874)
Mr. Michael's has opportunity: True or False?
True (0.8122723669190336)
Mr. Michael's has no opportunity: True or False?
True (0.6270381219830087)
The Seniors is guilty: True or False?
True (0.5525396910980834)
The Seniors is not guilty: True or False?
True (0.8438950825214144)
The Seniors has mean: True or False?
True (0.7806625377756776)
The Seniors has no mean: True or False?
False (0.5263427467960875)
The Seniors has motive: True or False?
True (0.7786493288700866)
The Seniors has no motive: True or False?
False (0.6859494535376744)
The Seniors has opportunity: True or False?
False (0.5302364729224919)
The Seniors has no opportunity: True or False?
True (0.5612147992901458)
### Beth
- mean: True (0.60859406896259)
- motive: False (0.4455295839293255)
- opportunity: False (0.32252599156679274)

### Damon
- mean: False (0.35756755874216195)
- motive: False (0.3182732411435174)
- opportunity: False (0.3821414173816513)

### Leo
- mean: True (0.8710367026584496)
- motive: True (0.962391318570921)
- opportunity: True (0.9390248079664695)

### Mr. Michael's
- mean: False (0.313209644823194)
- motive: False (0.38769037367512604)
- opportunity: False (0.3729618780169913)

### The Seniors
- mean: True (0.7806625377756776)
- motive: True (0.7786493288700866)
- opportunity: False (0.5302364729224919)

The culprit is Leo.
In fact, it is The Seniors.
## 5minutemystery-arsonist-attack
Jade Foster is guilty: True or False?
True (0.8734308550930344)
Jade Foster is not guilty: True or False?
True (0.8577680653964441)
Jade Foster has mean: True or False?
True (0.7348812840309261)
Jade Foster has no mean: True or False?
True (0.8080671968507699)
Jade Foster has motive: True or False?
True (0.7225270177274575)
Jade Foster has no motive: True or False?
True (0.6723316913929156)
Jade Foster has opportunity: True or False?
True (0.8322366416985943)
Jade Foster has no opportunity: True or False?
True (0.7348812183274223)
Jock Matt is guilty: True or False?
True (0.8558511727823209)
Jock Matt is not guilty: True or False?
True (0.8757870204368676)
Jock Matt has mean: True or False?
False (0.5136684130997575)
Jock Matt has no mean: True or False?
True (0.6029970803636248)
Jock Matt has motive: True or False?
True (0.7799928701983835)
Jock Matt has no motive: True or False?
True (0.7162185953247016)
Jock Matt has opportunity: True or False?
True (0.7853085971692302)
Jock Matt has no opportunity: True or False?
True (0.6169357925086439)
Madelyn Reader is guilty: True or False?
True (0.8661325012437474)
Madelyn Reader is not guilty: True or False?
True (0.873646672673131)
Madelyn Reader has mean: True or False?

Map:  96%|█████████▌| 194/203 [4:15:42<11:00, 73.35s/ examples]
Map:  96%|█████████▌| 195/203 [4:27:03<34:04, 255.55s/ examples]
Map:  97%|█████████▋| 196/203 [4:28:00<22:53, 196.17s/ examples]True (0.550607385906944)
Madelyn Reader has no mean: True or False?
True (0.6029970803636248)
Madelyn Reader has motive: True or False?
True (0.7634837587244478)
Madelyn Reader has no motive: True or False?
True (0.525368812147771)
Madelyn Reader has opportunity: True or False?
True (0.8056321690561029)
Madelyn Reader has no opportunity: True or False?
True (0.6645402797838648)
Max Crabgrass is guilty: True or False?
True (1.2484914190047414)
Max Crabgrass is not guilty: True or False?
True (0.8916224227612378)
Max Crabgrass has mean: True or False?
True (0.7185943809170431)
Max Crabgrass has no mean: True or False?
True (0.7885831565209055)
Max Crabgrass has motive: True or False?
True (0.8826302888575707)
Max Crabgrass has no motive: True or False?
True (0.8787311338092536)
Max Crabgrass has opportunity: True or False?
True (0.9008791478232747)
Max Crabgrass has no opportunity: True or False?
True (0.7725306828324007)
Security Guard is guilty: True or False?
True (0.9289263523387795)
Security Guard is not guilty: True or False?
True (0.9422946582938823)
Security Guard has mean: True or False?
True (0.8958876133958744)
Security Guard has no mean: True or False?
True (0.875361437979977)
Security Guard has motive: True or False?
True (0.9161096235973493)
Security Guard has no motive: True or False?
True (0.8991214023999228)
Security Guard has opportunity: True or False?
True (0.9136765013387816)
Security Guard has no opportunity: True or False?
True (0.8169911556077801)
### Jade Foster
- mean: True (0.7348812840309261)
- motive: True (0.7225270177274575)
- opportunity: True (0.8322366416985943)

### Jock Matt
- mean: False (0.5136684130997575)
- motive: False (0.28378140467529844)
- opportunity: False (0.38306420749135606)

### Madelyn Reader
- mean: True (0.550607385906944)
- motive: False (0.474631187852229)
- opportunity: False (0.33545972021613524)

### Max Crabgrass
- mean: True (0.7185943809170431)
- motive: False (0.1212688661907464)
- opportunity: False (0.22746931716759933)

### Security Guard
- mean: False (0.12463856202002299)
- motive: False (0.10087859760007722)
- opportunity: False (0.18300884439221987)

The culprit is Jade Foster.
In fact, it is Jade Foster.
## 5minutemystery-investigation-sabotager
Emma is guilty: True or False?
True (0.9658995287662642)
Emma is not guilty: True or False?
True (0.9613890640022783)
Emma has mean: True or False?
True (0.8803863464576128)
Emma has no mean: True or False?
True (0.6654105788791005)
Emma has motive: True or False?
True (0.9326989068252284)
Emma has no motive: True or False?
True (0.8086723702005608)
Emma has opportunity: True or False?
True (0.9447913165152162)
Emma has no opportunity: True or False?
True (0.8316905440184192)
Mary is guilty: True or False?
True (0.9263036859044167)
Mary is not guilty: True or False?
True (0.869271276026005)
Mary has mean: True or False?
True (0.8812065732757132)
Mary has no mean: True or False?
True (0.7620701143808404)
Mary has motive: True or False?
True (0.934872446722342)
Mary has no motive: True or False?
True (0.6688802830862913)
Mary has opportunity: True or False?
True (0.9682614213403071)
Mary has no opportunity: True or False?
True (0.8714748565614324)
Peter is guilty: True or False?
True (0.8719117627136385)
Peter is not guilty: True or False?
True (0.8423451152856819)
Peter has mean: True or False?
True (0.8289387819824735)
Peter has no mean: True or False?
True (0.7272012283179254)
Peter has motive: True or False?
True (0.9190633328333496)
Peter has no motive: True or False?
True (0.8322367037050584)
Peter has opportunity: True or False?
True (0.9289263523387795)
Peter has no opportunity: True or False?
True (0.8261514850267767)
Tim is guilty: True or False?
True (0.9369805475192257)
Tim is not guilty: True or False?
True (0.9487275499225403)
Tim has mean: True or False?
True (0.9729852083817088)
Tim has no mean: True or False?
True (0.8856315007226893)
Tim has motive: True or False?
True (0.9602867377475474)
Tim has no motive: True or False?
True (0.8824278665848695)
Tim has opportunity: True or False?
True (0.9012274173198201)
Tim has no opportunity: True or False?
True (0.7813305798204846)
Valerie is guilty: True or False?
True (0.814643384779728)
Valerie is not guilty: True or False?
True (0.7193836000532381)
Valerie has mean: True or False?
True (0.8376199551237796)
Valerie has no mean: True or False?
False (0.5907791930117218)
Valerie has motive: True or False?
True (0.7122321792841629)
Valerie has no motive: True or False?
True (0.5418937216067536)
Valerie has opportunity: True or False?
True (0.943347633443741)
Valerie has no opportunity: True or False?
True (0.6619228115397798)
### Emma
- mean: False (0.3345894211208995)
- motive: False (0.19132762979943918)
- opportunity: False (0.16830945598158076)

### Mary
- mean: False (0.23792988561915962)
- motive: False (0.3311197169137087)
- opportunity: False (0.12852514343856758)

### Peter
- mean: True (0.8289387819824735)
- motive: True (0.9190633328333496)
- opportunity: True (0.9289263523387795)

### Tim
- mean: False (0.11436849927731074)
- motive: False (0.11757213341513051)
- opportunity: False (0.2186694201795154)

### Valerie
- mean: True (0.8376199551237796)
- motive: False (0.45810627839324636)
- opportunity: False (0.33807718846022017)

The culprit is Peter.
In fact, it is Emma.
## 5minutemystery-the-presidential-smear-campaint-a-jacelyn-drew-mystery
Brittany is guilty: True or False?
True (0.9336731438527403)
Brittany is not guilty: True or False?
True (0.920217993899809)
Brittany has mean: True or False?
True (0.8563324216110711)
Brittany has no mean: True or False?
True (0.7704647687904915)
Brittany has motive: True or False?
True (0.9425067301242699)
Brittany has no motive: True or False?
True (0.8469578650997759)
Brittany has opportunity: True or False?
True (0.9516838792709049)
Brittany has no opportunity: True or False?
True (0.9029524325377104)
Isis is guilty: True or False?
True (0.9682013404912752)
Isis is not guilty: True or False?
True (0.974580348460635)
Isis has mean: True or False?
True (0.8816149238192855)
Isis has no mean: True or False?
True (0.9152045868398637)
Isis has motive: True or False?
True (0.9673486357359453)
Isis has no motive: True or False?
True (0.958226146208407)
Isis has opportunity: True or False?
True (0.943451882217003)
Isis has no opportunity: True or False?
True (0.9124361878432953)
Marie is guilty: True or False?
True (0.9515039936355008)
Marie is not guilty: True or False?
True (0.946100889099178)
Marie has mean: True or False?
True (0.8745065930973813)
Marie has no mean: True or False?
True (0.9076402191395381)
Marie has motive: True or False?
True (0.9429286143036572)
Marie has no motive: True or False?
True (0.9437636745681832)
Marie has opportunity: True or False?
True (0.962813258487323)
Marie has no opportunity: True or False?
True (0.8868131040663721)
Norma is guilty: True or False?
True (0.9240047963507929)
Norma is not guilty: True or False?
True (0.9298236969789664)
Norma has mean: True or False?
True (0.7885832152749314)
Norma has no mean: True or False?
True (0.8169911556077801)
Norma has motive: True or False?
True (0.9261703516148618)
Norma has no motive: True or False?
True (0.8705973031072073)
Norma has opportunity: True or False?
True (0.9583821892129424)
Norma has no opportunity: True or False?
True (0.9121235591541035)
### Brittany
- mean: False (0.22953523120950847)
- motive: False (0.1530421349002241)
- opportunity: False (0.0970475674622896)

### Isis
- mean: True (0.8816149238192855)
- motive: True (0.9673486357359453)
- opportunity: True (0.943451882217003)

### Marie
- mean: True (0.8745065930973813)
- motive: True (0.9429286143036572)
- opportunity: False (0.11318689593362785)

### Norma
- mean: True (0.7885832152749314)
- motive: False (0.1294026968927927)
- opportunity: False (0.08787644084589652)

The culprit is Isis.
In fact, it is Isis.
## 5minutemystery-the-sunday-mystery
Jack Jackson is guilty: True or False?
True (0.7853085971692302)
Jack Jackson is not guilty: True or False?
True (0.9068182712676458)
Jack Jackson has mean: True or False?
True (0.8134608241927087)

Map:  97%|█████████▋| 197/203 [4:29:08<15:45, 157.51s/ examples]
Map:  98%|█████████▊| 198/203 [4:29:58<10:27, 125.51s/ examples]Jack Jackson has no mean: True or False?
True (0.7833262085677729)
Jack Jackson has motive: True or False?
True (0.9799765949220004)
Jack Jackson has no motive: True or False?
True (0.9273632783787477)
Jack Jackson has opportunity: True or False?
True (0.9681411371390284)
Jack Jackson has no opportunity: True or False?
True (0.8895288123486662)
Jimmy Jackson is guilty: True or False?
True (0.8104789202520752)
Jimmy Jackson is not guilty: True or False?
True (0.844921525814193)
Jimmy Jackson has mean: True or False?
False (0.6584175136252488)
Jimmy Jackson has no mean: True or False?
False (0.514644215419305)
Jimmy Jackson has motive: True or False?
True (0.9680204387474981)
Jimmy Jackson has no motive: True or False?
True (0.8740772044235984)
Jimmy Jackson has opportunity: True or False?
True (0.9076402191395381)
Jimmy Jackson has no opportunity: True or False?
True (0.6825736720802238)
Jon Jackson is guilty: True or False?
True (0.9196425103002197)
Jon Jackson is not guilty: True or False?
True (0.8955226517597132)
Jon Jackson has mean: True or False?
True (0.595492552580428)
Jon Jackson has no mean: True or False?
True (0.5302364729224919)
Jon Jackson has motive: True or False?
True (0.958847105894029)
Jon Jackson has no motive: True or False?
True (0.7476159279883341)
Jon Jackson has opportunity: True or False?
True (0.9005298052062833)
Jon Jackson has no opportunity: True or False?
True (0.7302898714065358)
Maria Jackson is guilty: True or False?
True (0.8080671968507699)
Maria Jackson is not guilty: True or False?
True (0.8868131040663721)
Maria Jackson has mean: True or False?
True (0.7950222460539826)
Maria Jackson has no mean: True or False?
True (0.7527403228571042)
Maria Jackson has motive: True or False?
True (0.9683213832701327)
Maria Jackson has no motive: True or False?
True (0.7154239360853772)
Maria Jackson has opportunity: True or False?
True (0.929696145502287)
Maria Jackson has no opportunity: True or False?
True (0.5650587803792624)
Spot is guilty: True or False?
True (0.8910549899564296)
Spot is not guilty: True or False?
True (0.966726063403815)
Spot has mean: True or False?
False (0.5992506595844092)
Spot has no mean: True or False?
True (0.8198932995357624)
Spot has motive: True or False?
False (0.6463158311908145)
Spot has no motive: True or False?
True (0.9032942081209032)
Spot has opportunity: True or False?
True (0.9549844874375936)
Spot has no opportunity: True or False?
True (0.94519740270931)
### Jack Jackson
- mean: True (0.8134608241927087)
- motive: True (0.9799765949220004)
- opportunity: True (0.9681411371390284)

### Jimmy Jackson
- mean: True (0.48535578458069495)
- motive: False (0.12592279557640162)
- opportunity: False (0.3174263279197762)

### Jon Jackson
- mean: False (0.4697635270775081)
- motive: False (0.2523840720116659)
- opportunity: False (0.2697101285934642)

### Maria Jackson
- mean: False (0.24725967714289576)
- motive: False (0.28457606391462276)
- opportunity: False (0.4349412196207376)

### Spot
- mean: False (0.5992506595844092)
- motive: False (0.6463158311908145)
- opportunity: False (0.054802597290690036)

The culprit is Jack Jackson.
In fact, it is Spot.
## 5minutemystery-the-mystery-of-heritage
Jack Anderson is guilty: True or False?
True (0.9651848090355489)
Jack Anderson is not guilty: True or False?
True (0.940789698413215)
Jack Anderson has mean: True or False?
True (0.7866228249849953)
Jack Anderson has no mean: True or False?
True (0.525368812147771)
Jack Anderson has motive: True or False?
True (0.9564719186263709)
Jack Anderson has no motive: True or False?
True (0.8529354946829077)
Jack Anderson has opportunity: True or False?
True (0.8638516611889259)
Jack Anderson has no opportunity: True or False?
True (0.8902941942359355)
Jessica Anderson is guilty: True or False?
True (0.9757623676279906)
Jessica Anderson is not guilty: True or False?
True (0.916109562167414)
Jessica Anderson has mean: True or False?
True (0.8098781635062345)
Jessica Anderson has no mean: True or False?
True (0.6095241271158658)
Jessica Anderson has motive: True or False?
True (0.9774139529645163)
Jessica Anderson has no motive: True or False?
True (0.8519527857346616)
Jessica Anderson has opportunity: True or False?
True (0.9573576465213919)
Jessica Anderson has no opportunity: True or False?
True (0.740174341079517)
Martha Anderson is guilty: True or False?
True (0.9734434487527764)
Martha Anderson is not guilty: True or False?
True (0.9312126617773815)
Martha Anderson has mean: True or False?
True (0.9105454073245608)
Martha Anderson has no mean: True or False?
True (0.7008948290825966)
Martha Anderson has motive: True or False?
True (0.9843664168051008)
Martha Anderson has no motive: True or False?
True (0.9079670935046645)
Martha Anderson has opportunity: True or False?
True (0.9614615446058614)
Martha Anderson has no opportunity: True or False?
True (0.8951566249612815)
Mrs. Neil is guilty: True or False?
True (0.9625325207646147)
Mrs. Neil is not guilty: True or False?
True (0.9564718616162037)
Mrs. Neil has mean: True or False?
True (0.927887794449634)
Mrs. Neil has no mean: True or False?
True (0.6270381219830087)
Mrs. Neil has motive: True or False?
True (0.982590972614882)
Mrs. Neil has no motive: True or False?
True (0.905989824801558)
Mrs. Neil has opportunity: True or False?
True (0.9824568029810573)
Mrs. Neil has no opportunity: True or False?
True (0.8504685773080045)
### Jack Anderson
- mean: True (0.7866228249849953)
- motive: True (0.9564719186263709)
- opportunity: True (0.8638516611889259)

### Jessica Anderson
- mean: False (0.3904758728841342)
- motive: False (0.1480472142653384)
- opportunity: False (0.25982565892048304)

### Martha Anderson
- mean: False (0.2991051709174034)
- motive: False (0.09203290649533546)
- opportunity: False (0.10484337503871854)

### Mrs. Neil
- mean: False (0.3729618780169913)
- motive: False (0.09401017519844201)
- opportunity: False (0.14953142269199549)

The culprit is Jack Anderson.
In fact, it is Jessica Anderson.
## 5minutemystery-murder-of-the-actor
Bruce Whittingley is guilty: True or False?
True (0.986151396974789)
Bruce Whittingley is not guilty: True or False?
True (0.9437636147996928)
Bruce Whittingley has mean: True or False?
True (0.8080671968507699)
Bruce Whittingley has no mean: True or False?
True (0.6800292740030767)
Bruce Whittingley has motive: True or False?
True (0.9558166865608263)
Bruce Whittingley has no motive: True or False?
True (0.8998277786460391)
Bruce Whittingley has opportunity: True or False?
True (0.9498557456415421)
Bruce Whittingley has no opportunity: True or False?
True (0.7577943897558946)
Marie Carloette is guilty: True or False?
True (0.9846050735525358)
Marie Carloette is not guilty: True or False?
True (0.9748690125906128)
Marie Carloette has mean: True or False?
True (0.9730365275631271)
Marie Carloette has no mean: True or False?
True (0.9291837815043049)
Marie Carloette has motive: True or False?
True (0.9729338284788606)
Marie Carloette has no motive: True or False?
True (0.9378968460746586)
Marie Carloette has opportunity: True or False?
True (0.9642542005689824)
Marie Carloette has no opportunity: True or False?
True (0.8998277786460391)
Mario Marcino is guilty: True or False?
True (0.9863368866841652)
Mario Marcino is not guilty: True or False?
True (0.9789956218205105)
Mario Marcino has mean: True or False?
True (0.9473810211532727)
Mario Marcino has no mean: True or False?
True (0.9365176577773374)
Mario Marcino has motive: True or False?
True (0.9862576727459876)
Mario Marcino has no motive: True or False?
True (0.9717789891296182)
Mario Marcino has opportunity: True or False?
True (0.9797840705842182)
Mario Marcino has no opportunity: True or False?
True (0.9331876642092066)
### Bruce Whittingley
- mean: False (0.31997072599692333)
- motive: False (0.10017222135396087)
- opportunity: False (0.24220561024410536)

### Marie Carloette
- mean: False (0.07081621849569508)
- motive: False (0.06210315392534138)
- opportunity: False (0.10017222135396087)

### Mario Marcino
- mean: True (0.9473810211532727)
- motive: True (0.9862576727459876)
- opportunity: True (0.9797840705842182)


Map:  98%|█████████▊| 199/203 [4:30:35<06:35, 98.89s/ examples] 
Map:  99%|█████████▊| 200/203 [4:31:45<04:30, 90.08s/ examples]
Map:  99%|█████████▉| 201/203 [4:32:33<02:35, 77.56s/ examples]The culprit is Mario Marcino.
In fact, it is Marie Carloette.
## 5minutemystery-another-hotel-murder
Dianne Shelby is guilty: True or False?
True (0.8919052512911346)
Dianne Shelby is not guilty: True or False?
True (0.9201569761137415)
Dianne Shelby has mean: True or False?
True (0.7866228835929651)
Dianne Shelby has no mean: True or False?
True (0.8524448242555318)
Dianne Shelby has motive: True or False?
True (0.9525520223134187)
Dianne Shelby has no motive: True or False?
True (0.8963421613698933)
Dianne Shelby has opportunity: True or False?
True (0.864539320523716)
Dianne Shelby has no opportunity: True or False?
True (0.6671476985798853)
James Castro is guilty: True or False?
True (1.0058063062603522)
James Castro is not guilty: True or False?
True (1.2002095424626835)
James Castro has mean: True or False?
True (0.860369148541484)
James Castro has no mean: True or False?
True (0.8914335992201801)
James Castro has motive: True or False?
True (0.9067357195193472)
James Castro has no motive: True or False?
True (0.9094255002859922)
James Castro has opportunity: True or False?
True (0.892187358563457)
James Castro has no opportunity: True or False?
True (0.8071567377359422)
Kevin King is guilty: True or False?
True (0.9458512675695098)
Kevin King is not guilty: True or False?
True (0.9558991201960071)
Kevin King has mean: True or False?
True (0.9064877041303855)
Kevin King has no mean: True or False?
True (0.9295683483415352)
Kevin King has motive: True or False?
True (0.9545415629477866)
Kevin King has no motive: True or False?
True (0.9322068701708559)
Kevin King has opportunity: True or False?
True (0.9515490540211475)
Kevin King has no opportunity: True or False?
True (0.8776866221669275)
Roger Shelby is guilty: True or False?
True (0.8488469713350262)
Roger Shelby is not guilty: True or False?
True (0.8781053402372203)
Roger Shelby has mean: True or False?
True (0.7704647687904915)
Roger Shelby has no mean: True or False?
True (0.8334601463887776)
Roger Shelby has motive: True or False?
True (0.9137535101236324)
Roger Shelby has no motive: True or False?
True (0.8888552820594576)
Roger Shelby has opportunity: True or False?
True (0.8881781721623143)
Roger Shelby has no opportunity: True or False?
True (0.7390459841313068)
### Dianne Shelby
- mean: True (0.7866228835929651)
- motive: False (0.10365783863010669)
- opportunity: False (0.3328523014201147)

### James Castro
- mean: True (0.860369148541484)
- motive: True (0.9067357195193472)
- opportunity: True (0.892187358563457)

### Kevin King
- mean: True (0.9064877041303855)
- motive: False (0.0677931298291441)
- opportunity: False (0.1223133778330725)

### Roger Shelby
- mean: True (0.7704647687904915)
- motive: False (0.11114471794054237)
- opportunity: False (0.26095401586869316)

The culprit is James Castro.
In fact, it is James Castro.
## 5minutemystery-the-missing-book
Brad is guilty: True or False?
True (0.955152093302995)
Brad is not guilty: True or False?
True (0.967471776843259)
Brad has mean: True or False?
True (0.9319595674053855)
Brad has no mean: True or False?
True (0.9076402191395381)
Brad has motive: True or False?
True (0.9369805475192257)
Brad has no motive: True or False?
True (0.8987665204865408)
Brad has opportunity: True or False?
True (0.9832788702399727)
Brad has no opportunity: True or False?
True (0.960804880888677)
Fred is guilty: True or False?
True (0.9656413200400066)
Fred is not guilty: True or False?
True (0.9709092372014624)
Fred has mean: True or False?
True (0.9475755109125973)
Fred has no mean: True or False?
True (0.9564718616162037)
Fred has motive: True or False?
False (0.7665304747562915)
Fred has no motive: True or False?
True (0.9385759220258869)
Fred has opportunity: True or False?
False (0.6321309950802387)
Fred has no opportunity: True or False?
False (0.7240636712410182)
Mrs. Dunwoodee is guilty: True or False?
True (0.9693242313725606)
Mrs. Dunwoodee is not guilty: True or False?
True (0.9736446744750681)
Mrs. Dunwoodee has mean: True or False?
True (0.9167080509980843)
Mrs. Dunwoodee has no mean: True or False?
True (0.884439109617765)
Mrs. Dunwoodee has motive: True or False?
True (0.9384632725948482)
Mrs. Dunwoodee has no motive: True or False?
True (0.8344069148356309)
Mrs. Dunwoodee has opportunity: True or False?
True (0.9458012588547495)
Mrs. Dunwoodee has no opportunity: True or False?
True (0.94519740270931)
Ricky is guilty: True or False?
True (0.9698996547102765)
Ricky is not guilty: True or False?
True (0.9771973485275812)
Ricky has mean: True or False?
True (0.9031234421019929)
Ricky has no mean: True or False?
True (0.893681109060862)
Ricky has motive: True or False?
True (0.9639160647221925)
Ricky has no motive: True or False?
True (0.8895288719962232)
Ricky has opportunity: True or False?
True (0.9571978443343412)
Ricky has no opportunity: True or False?
True (0.9133679254389228)
### Brad
- mean: True (0.9319595674053855)
- motive: True (0.9369805475192257)
- opportunity: True (0.9832788702399727)

### Fred
- mean: True (0.9475755109125973)
- motive: False (0.7665304747562915)
- opportunity: False (0.6321309950802387)

### Mrs. Dunwoodee
- mean: False (0.11556089038223505)
- motive: False (0.1655930851643691)
- opportunity: False (0.054802597290690036)

### Ricky
- mean: False (0.10631889093913804)
- motive: False (0.11047112800377679)
- opportunity: False (0.08663207456107724)

The culprit is Brad.
In fact, it is Fred.
## 5minutemystery-the-necklace
Aunt Mary is guilty: True or False?
True (0.9675331712558415)
Aunt Mary is not guilty: True or False?
True (0.9689738169140454)
Aunt Mary has mean: True or False?
True (0.9008791478232747)
Aunt Mary has no mean: True or False?
True (0.8998277786460391)
Aunt Mary has motive: True or False?
True (0.9318356525033217)
Aunt Mary has no motive: True or False?
True (0.9181873182746905)
Aunt Mary has opportunity: True or False?
True (0.9527502639818524)
Aunt Mary has no opportunity: True or False?
True (0.884439109617765)
Dad is guilty: True or False?
True (0.9902538653604824)
Dad is not guilty: True or False?
True (0.9843664168051008)
Dad has mean: True or False?
True (0.9237300750192418)
Dad has no mean: True or False?
True (0.9307105568817887)
Dad has motive: True or False?
True (0.985057294041011)
Dad has no motive: True or False?
True (0.9851289983588206)
Dad has opportunity: True or False?
True (0.9354645628936168)
Dad has no opportunity: True or False?
True (0.9237300130783155)
Mom is guilty: True or False?
True (0.9853984116501415)
Mom is not guilty: True or False?
True (0.9760835762008001)
Mom has mean: True or False?
True (0.8824278665848695)
Mom has no mean: True or False?
True (0.9276260107813639)
Mom has motive: True or False?
True (0.9817357655259503)
Mom has no motive: True or False?
True (0.9825574747001844)
Mom has opportunity: True or False?
True (0.9214990117475544)
Mom has no opportunity: True or False?
True (0.8846386054372942)
Uncle Henry is guilty: True or False?
True (0.9630224717531983)
Uncle Henry is not guilty: True or False?
True (0.9635748275768365)
Uncle Henry has mean: True or False?
True (0.9543079730970608)
Uncle Henry has no mean: True or False?
True (0.9628131975124238)
Uncle Henry has motive: True or False?
True (0.9696132548883896)
Uncle Henry has no motive: True or False?
True (0.9664104579001461)
Uncle Henry has opportunity: True or False?
True (0.9739436503754907)
Uncle Henry has no opportunity: True or False?
True (0.9527503243194666)
Uncle John is guilty: True or False?
True (0.9678385865075065)
Uncle John is not guilty: True or False?
True (0.9718859797630299)
Uncle John has mean: True or False?
True (0.9658351545108645)
Uncle John has no mean: True or False?
True (0.966851473631521)
Uncle John has motive: True or False?
True (0.972204327764203)
Uncle John has no motive: True or False?
True (0.9732407327993322)
Uncle John has opportunity: True or False?
True (0.9762653119462512)
Uncle John has no opportunity: True or False?
True (0.9618217364339323)
### Aunt Mary
- mean: False (0.10017222135396087)
- motive: False (0.08181268172530953)
- opportunity: False (0.11556089038223505)

### Dad
- mean: True (0.9237300750192418)

Map: 100%|█████████▉| 202/203 [4:33:34<01:12, 72.64s/ examples]
Map: 100%|██████████| 203/203 [4:34:53<00:00, 74.53s/ examples]
Map: 100%|██████████| 203/203 [4:34:53<00:00, 81.25s/ examples]
- motive: True (0.985057294041011)
- opportunity: True (0.9354645628936168)

### Mom
- mean: True (0.8824278665848695)
- motive: True (0.9817357655259503)
- opportunity: False (0.11536139456270578)

### Uncle Henry
- mean: True (0.9543079730970608)
- motive: False (0.033589542099853875)
- opportunity: False (0.0472496756805334)

### Uncle John
- mean: True (0.9658351545108645)
- motive: True (0.972204327764203)
- opportunity: False (0.03817826356606768)

The culprit is Dad.
In fact, it is Dad.
## 5minutemystery-the-purloined-wallet
Bill Buchanan is guilty: True or False?
True (0.9022657265573043)
Bill Buchanan is not guilty: True or False?
True (0.9384632725948482)
Bill Buchanan has mean: True or False?
True (0.9014011626580862)
Bill Buchanan has no mean: True or False?
True (0.8534247816107388)
Bill Buchanan has motive: True or False?
True (1.469602350642461)
Bill Buchanan has no motive: True or False?
True (0.8354834909254251)
Bill Buchanan has opportunity: True or False?
True (0.9082930095862076)
Bill Buchanan has no opportunity: True or False?
True (0.8031737798924701)
Carson Thomson is guilty: True or False?
True (0.9372107409794781)
Carson Thomson is not guilty: True or False?
True (0.9404624710539093)
Carson Thomson has mean: True or False?
True (0.9353465445225602)
Carson Thomson has no mean: True or False?
True (0.9383503780077049)
Carson Thomson has motive: True or False?
True (0.8467044802440825)
Carson Thomson has no motive: True or False?
True (0.8697145551802641)
Carson Thomson has opportunity: True or False?
True (0.9095862487848758)
Carson Thomson has no opportunity: True or False?
True (0.9403530947748038)
Cooper is guilty: True or False?
True (0.874934615163517)
Cooper is not guilty: True or False?
True (0.9265699978627552)
Cooper has mean: True or False?
True (0.5964331434971528)
Cooper has no mean: True or False?
True (0.8883720049821552)
Cooper has motive: True or False?
True (0.85729086409805)
Cooper has no motive: True or False?
True (0.9378969089655451)
Cooper has opportunity: True or False?
True (0.9541373270174538)
Cooper has no opportunity: True or False?
True (0.9515039936355008)
David Nader is guilty: True or False?
True (0.8643104392003704)
David Nader is not guilty: True or False?
True (0.8931231526306965)
David Nader has mean: True or False?
True (0.8944211616820568)
David Nader has no mean: True or False?
True (0.929696145502287)
David Nader has motive: True or False?
True (0.8050197941712954)
David Nader has no motive: True or False?
True (0.9063219998220023)
David Nader has opportunity: True or False?
True (0.9666631213158693)
David Nader has no opportunity: True or False?
True (0.9655114412719658)
Vincent Garcia is guilty: True or False?
True (0.8812066389307215)
Vincent Garcia is not guilty: True or False?
True (0.915959419239083)
Vincent Garcia has mean: True or False?
True (0.9079670935046645)
Vincent Garcia has no mean: True or False?
True (0.9485372300670596)
Vincent Garcia has motive: True or False?
True (0.8524448242555318)
Vincent Garcia has no motive: True or False?
True (0.8812066389307215)
Vincent Garcia has opportunity: True or False?
True (0.9233162440500982)
Vincent Garcia has no opportunity: True or False?
True (0.9230391966311572)
### Bill Buchanan
- mean: False (0.14657521838926124)
- motive: True (1.469602350642461)
- opportunity: False (0.19682622010752993)

### Carson Thomson
- mean: True (0.9353465445225602)
- motive: True (0.8467044802440825)
- opportunity: True (0.9095862487848758)

### Cooper
- mean: True (0.5964331434971528)
- motive: True (0.85729086409805)
- opportunity: False (0.048496006364499245)

### David Nader
- mean: True (0.8944211616820568)
- motive: True (0.8050197941712954)
- opportunity: False (0.034488558728034246)

### Vincent Garcia
- mean: True (0.9079670935046645)
- motive: True (0.8524448242555318)
- opportunity: False (0.07696080336884281)

The culprit is Carson Thomson.
In fact, it is David Nader.
Solved 42 out of 203.
