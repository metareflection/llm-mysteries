nohup: ignoring input
/home/sraja/mambaforge/envs/llm-mysteries/lib/python3.10/site-packages/transformers/models/auto/auto_factory.py:472: FutureWarning: The `use_auth_token` argument is deprecated and will be removed in v5 of Transformers. Please use `token` instead.
  warnings.warn(
Loading checkpoint shards:   0%|          | 0/3 [00:00<?, ?it/s]Loading checkpoint shards:  33%|███▎      | 1/3 [00:02<00:04,  2.15s/it]Loading checkpoint shards:  67%|██████▋   | 2/3 [00:04<00:02,  2.07s/it]Loading checkpoint shards: 100%|██████████| 3/3 [00:05<00:00,  1.65s/it]Loading checkpoint shards: 100%|██████████| 3/3 [00:05<00:00,  1.77s/it]
/home/sraja/mambaforge/envs/llm-mysteries/lib/python3.10/site-packages/dill/_dill.py:412: PicklingWarning: Cannot locate reference to <class '_ctypes.PyCFuncPtrType'>.
  StockPickler.save(self, obj, save_persistent_id)
/home/sraja/mambaforge/envs/llm-mysteries/lib/python3.10/site-packages/dill/_dill.py:412: PicklingWarning: Cannot pickle <class '_ctypes.PyCFuncPtrType'>: _ctypes.PyCFuncPtrType has recursive self-references that trigger a RecursionError.
  StockPickler.save(self, obj, save_persistent_id)
Parameter 'function'=<function processCase at 0x7fe67086cb80> of the transform datasets.arrow_dataset.Dataset._map_single couldn't be hashed properly, a random hash was used instead. Make sure your transforms and parameters are serializable with pickle or dill for the dataset fingerprinting and caching to work. If you reuse this transform, the caching mechanism will consider it to be different from the previous calls and recompute everything. This warning is only showed once. Subsequent hashing failures won't be showed.
Map:   0%|          | 0/203 [00:00<?, ? examples/s]Map:   0%|          | 1/203 [00:22<1:14:23, 22.10s/ examples]Map:   1%|          | 2/203 [00:42<1:10:57, 21.18s/ examples]## 5minutemystery-who-let-the-frogs-out
Kyle Kravetsky is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9105454073245608)
Kyle Kravetsky has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9606574760904091)
Kyle Kravetsky has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8799743689174987)
Kyle Kravetsky had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7606506318580792)
Marnie Pepper is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8856314413364714)
Marnie Pepper has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9677776702396809)
Marnie Pepper has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8469578019965)
Marnie Pepper had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8459424988148251)
Matilda Robbens is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9079670935046645)
Matilda Robbens has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9744347924514057)
Matilda Robbens has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8509647293237851)
Matilda Robbens had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7563575572780217)
Sergio Ramos is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8509646659219744)
Sergio Ramos has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.958847105894029)
Sergio Ramos has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8175744430556572)
Sergio Ramos had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7786492592534148)
### Kyle Kravetsky
- mean: False (0.03934252390959092)
- motive: False (0.1200256310825013)
- opportunity: False (0.23934936814192076)

### Marnie Pepper
- mean: True (0.9677776702396809)
- motive: True (0.8469578019965)
- opportunity: True (0.8459424988148251)

### Matilda Robbens
- mean: False (0.02556520754859426)
- motive: False (0.14903527067621491)
- opportunity: False (0.24364244272197833)

### Sergio Ramos
- mean: False (0.041152894105971005)
- motive: False (0.18242555694434281)
- opportunity: False (0.22135074074658523)

The culprit is Marnie Pepper.
In fact, it is Matilda Robbens.
## 5minutemystery-uncle-buck-field-trip
Collin is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.878314250659373)
Collin has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.958537757711882)
Collin has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9246876822649571)
Collin had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8757870204368676)
Erica is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8770561879413864)
Erica has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9600626824595854)
Erica has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9190632712053527)
Erica had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8848377441095496)
Rory is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8998277786460391)
Rory has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9781354072533421)
Rory has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9317114347547434)
Rory had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8749346673136854)
Rusty is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8828325273478573)
Rusty has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9536217457735022)
Rusty has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8936811689868521)
Rusty had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8255897087847518)
### Collin
- mean: False (0.04146224228811801)
- motive: False (0.07531231773504288)
- opportunity: False (0.12421297956313238)

### Erica
- mean: False (0.03993731754041463)
- motive: False (0.0809367287946473)
- opportunity: False (0.11516225589045037)

### Rory
- mean: True (0.9781354072533421)
- motive: True (0.9317114347547434)
- opportunity: True (0.8749346673136854)

### Rusty
- mean: False (0.04637825422649777)
- motive: False (0.10631883101314787)
- opportunity: False (0.1744102912152482)

The culprit is Rory.
In fact, it is Rory.
## 5minutemystery-mystery-of-the-white-hats
Captain Stark is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7813306496768853)
Captain Stark has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9286680258169302)
Captain Stark has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9299510095943111)
Captain Stark had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8615382357584752)
Map:   1%|▏         | 3/203 [01:04<1:10:57, 21.29s/ examples]Map:   2%|▏         | 4/203 [01:22<1:06:45, 20.13s/ examples]Chet is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8824278665848695)
Chet has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.936749461409047)
Chet has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9577544910931239)
Chet had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8994751578343994)
Doug is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8104789202520752)
Doug has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8795611817678315)
Doug has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8577681165234065)
Doug had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7813306496768853)
Ernie is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.884439109617765)
Ernie has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9532750262379774)
Ernie has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9227612010756272)
Ernie had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8955226517597132)
### Captain Stark
- mean: False (0.0713319741830698)
- motive: False (0.0700489904056889)
- opportunity: False (0.1384617642415248)

### Chet
- mean: True (0.936749461409047)
- motive: True (0.9577544910931239)
- opportunity: True (0.8994751578343994)

### Doug
- mean: False (0.12043881823216851)
- motive: False (0.14223188347659355)
- opportunity: False (0.21866935032311474)

### Ernie
- mean: False (0.04672497376202256)
- motive: False (0.0772387989243728)
- opportunity: False (0.10447734824028676)

The culprit is Chet.
In fact, it is Chet.
## 5minutemystery-the-missing-popcorn
Private First Class Dicky Mosier is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8134607635851566)
Private First Class Dicky Mosier has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9326989068252284)
Private First Class Dicky Mosier has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8175745039697023)
Private First Class Dicky Mosier had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5360699771890155)
Private Joe Locke is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8719117627136385)
Private Joe Locke has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9496693599006181)
Private Joe Locke has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8519527857346616)
Private Joe Locke had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5389832197022594)
Specialist Fifth Class Ron Henson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7937461674149602)
Specialist Fifth Class Ron Henson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8910549302065384)
Specialist Fifth Class Ron Henson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.705785027818136)
Specialist Fifth Class Ron Henson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.570809902165233)
Specialist Fourth Class Patrick Macnamara is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.816406362162552)
Specialist Fourth Class Patrick Macnamara has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8947895144283036)
Specialist Fourth Class Patrick Macnamara has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6909763109505791)
Specialist Fourth Class Patrick Macnamara had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5660185351323219)
### Private First Class Dicky Mosier
- mean: False (0.06730109317477162)
- motive: False (0.18242549603029767)
- opportunity: False (0.4639300228109845)

### Private Joe Locke
- mean: True (0.9496693599006181)
- motive: True (0.8519527857346616)
- opportunity: True (0.5389832197022594)

### Specialist Fifth Class Ron Henson
- mean: False (0.10894506979346164)
- motive: False (0.294214972181864)
- opportunity: False (0.429190097834767)

### Specialist Fourth Class Patrick Macnamara
- mean: False (0.10521048557169643)
- motive: False (0.3090236890494209)
- opportunity: False (0.4339814648676781)

The culprit is Private Joe Locke.
In fact, it is Private Joe Locke.
## 5minutemystery-mystery-on-the-moor
Jack MacGinnis is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7732163648437078)
Jack MacGinnis has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.861071588244826)
Jack MacGinnis has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8122724274380432)
Jack MacGinnis had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6584175136252488)
James Macready is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7185943809170431)
James Macready has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8333246107254184)
Map:   2%|▏         | 5/203 [01:44<1:09:15, 20.99s/ examples]Map:   3%|▎         | 6/203 [02:10<1:13:46, 22.47s/ examples]James Macready has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7759445334082792)
James Macready had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.64779823427608)
Samuel Doone is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7648915681922661)
Samuel Doone has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8723473540228537)
Samuel Doone has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8210441512234701)
Samuel Doone had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7520125537161032)
Tom Jenkins is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7341195403199204)
Tom Jenkins has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8925625120974553)
Tom Jenkins has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7648916137833577)
Tom Jenkins had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6495786332146115)
### Jack MacGinnis
- mean: False (0.138928411755174)
- motive: False (0.18772757256195682)
- opportunity: False (0.3415824863747512)

### James Macready
- mean: False (0.1666753892745816)
- motive: False (0.22405546659172082)
- opportunity: False (0.35220176572392004)

### Samuel Doone
- mean: True (0.8723473540228537)
- motive: True (0.8210441512234701)
- opportunity: True (0.7520125537161032)

### Tom Jenkins
- mean: False (0.1074374879025447)
- motive: False (0.23510838621664232)
- opportunity: False (0.3504213667853885)

The culprit is Samuel Doone.
In fact, it is James Macready.
## 5minutemystery-who-stole-curious-george
Dexter is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7256486384635821)
Dexter has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8534247816107388)
Dexter has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8606036289596553)
Dexter had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8840392847025188)
Mr. Ferguson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6926419789019715)
Mr. Ferguson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8643104392003704)
Mr. Ferguson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8958876133958744)
Mr. Ferguson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8116760258690822)
Mrs. Yee is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6859494535376744)
Mrs. Yee has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8883720049821552)
Mrs. Yee has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9339146041314464)
Mrs. Yee had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8799743689174987)
Skyler is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5621764690603255)
Skyler has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8158201638039532)
Skyler has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7924642605907138)
Skyler had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8397340156610265)
### Dexter
- mean: False (0.14657521838926124)
- motive: False (0.13939637104034475)
- opportunity: False (0.1159607152974812)

### Mr. Ferguson
- mean: False (0.13568956079962957)
- motive: False (0.10411238660412558)
- opportunity: False (0.18832397413091784)

### Mrs. Yee
- mean: True (0.8883720049821552)
- motive: True (0.9339146041314464)
- opportunity: True (0.8799743689174987)

### Skyler
- mean: False (0.18417983619604683)
- motive: False (0.20753573940928616)
- opportunity: False (0.16026598433897354)

The culprit is Mrs. Yee.
In fact, it is Dexter.
## 5minutemystery-the-saxophones-ghost
Building Manager is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6619228707202935)
Building Manager has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8807970862580315)
Building Manager has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8994751578343994)
Building Manager had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7759445334082792)
Eric is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6397360437814448)
Eric has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9124361266596831)
Eric has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8940516749601143)
Eric had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7634837587244478)
Lenny is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.779321849347754)
Lenny has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8816149238192855)
Map:   3%|▎         | 7/203 [02:32<1:13:16, 22.43s/ examples]Map:   4%|▍         | 8/203 [02:51<1:08:45, 21.15s/ examples]Lenny has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.883638264557296)
Lenny had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8529354946829077)
Red is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6662796746479285)
Red has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8732148436000907)
Red has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8697146199790504)
Red had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8006920257960423)
### Building Manager
- mean: False (0.11920291374196845)
- motive: False (0.10052484216560065)
- opportunity: False (0.22405546659172082)

### Eric
- mean: False (0.0875638733403169)
- motive: False (0.10594832503988572)
- opportunity: False (0.23651624127555215)

### Lenny
- mean: True (0.8816149238192855)
- motive: True (0.883638264557296)
- opportunity: True (0.8529354946829077)

### Red
- mean: False (0.12678515639990928)
- motive: False (0.13028538002094958)
- opportunity: False (0.19930797420395774)

The culprit is Lenny.
In fact, it is Building Manager.
## 5minutemystery-who-shot-mom
Dad is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8221890958162477)
Dad has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9759464267558225)
Dad has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8413048399699521)
Dad had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8947894610946939)
Randy is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7409249009267298)
Randy has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9747250674487342)
Randy has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.879146813094474)
Randy had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.861538171568877)
Roger is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7541915688671895)
Roger has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9757623676279906)
Roger has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9108631007029255)
Roger had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9039744767757508)
Rory is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7512834059294674)
Rory has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9754836557950954)
Rory has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8864204283224634)
Rory had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9082930095862076)
### Dad
- mean: False (0.02405357324417745)
- motive: False (0.1586951600300479)
- opportunity: False (0.10521053890530607)

### Randy
- mean: False (0.025274932551265783)
- motive: False (0.12085318690552604)
- opportunity: False (0.13846182843112298)

### Roger
- mean: True (0.9757623676279906)
- motive: True (0.9108631007029255)
- opportunity: True (0.9039744767757508)

### Rory
- mean: False (0.02451634420490456)
- motive: False (0.11357957167753663)
- opportunity: False (0.09170699041379238)

The culprit is Roger.
In fact, it is Randy.
## 5minutemystery-finding-the-flower-fund
James Faust is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8868131040663721)
James Faust has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9630919110597987)
James Faust has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7866228249849953)
James Faust had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6934729802503211)
Justin Thorn is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8577681165234065)
Justin Thorn has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9645892389558273)
Justin Thorn has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7468781552484828)
Justin Thorn had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7924642605907138)
Lincoln Smith is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9509603994010378)
Lincoln Smith has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9835969212828963)
Lincoln Smith has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9193533657123177)
Lincoln Smith had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.884837803442546)
Linda Hinton is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9281486838603771)
Linda Hinton has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9686195238117354)
Linda Hinton has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8504686406728537)
Map:   4%|▍         | 9/203 [03:05<1:01:56, 19.16s/ examples]Map:   5%|▍         | 10/203 [03:25<1:02:16, 19.36s/ examples]Map:   5%|▌         | 11/203 [03:44<1:01:11, 19.12s/ examples]Linda Hinton had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8062431235779619)
### James Faust
- mean: False (0.036908088940201256)
- motive: False (0.21337717501500475)
- opportunity: False (0.3065270197496789)

### Justin Thorn
- mean: False (0.035410761044172734)
- motive: False (0.2531218447515172)
- opportunity: False (0.20753573940928616)

### Lincoln Smith
- mean: True (0.9835969212828963)
- motive: True (0.9193533657123177)
- opportunity: True (0.884837803442546)

### Linda Hinton
- mean: False (0.03138047618826456)
- motive: False (0.14953135932714634)
- opportunity: False (0.1937568764220381)

The culprit is Lincoln Smith.
In fact, it is Lincoln Smith.
## 5minutemystery-map-of-the-traitor
Benjamin is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8365545874520802)
Benjamin has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8984105603938967)
Benjamin has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.879146813094474)
Benjamin had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.874934615163517)
Edward is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6169357925086439)
Edward has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7718434926244166)
Edward has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6740504382339836)
Edward had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6723316913929156)
Jonathan is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7248702601920561)
Jonathan has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8714748565614324)
Jonathan has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8459424357871997)
Jonathan had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7892336789711022)
Lucius is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8392075331266983)
Lucius has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9403530352223053)
Lucius has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.874934615163517)
Lucius had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8984105603938967)
### Benjamin
- mean: False (0.10158943960610334)
- motive: False (0.12085318690552604)
- opportunity: False (0.125065384836483)

### Edward
- mean: False (0.22815650737558335)
- motive: False (0.3259495617660164)
- opportunity: False (0.3276683086070844)

### Jonathan
- mean: False (0.12852514343856758)
- motive: False (0.15405756421280026)
- opportunity: False (0.2107663210288978)

### Lucius
- mean: True (0.9403530352223053)
- motive: True (0.874934615163517)
- opportunity: True (0.8984105603938967)

The culprit is Lucius.
In fact, it is Jonathan.
## 5minutemystery-the-crusaders-robe
Captain Fosters is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6808786440630326)
Captain Fosters has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9066531077351827)
Captain Fosters has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8705973031072073)
Captain Fosters had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8031737798924701)
Godefroi is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6706082735718226)
Godefroi has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8092759828926619)
Godefroi has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8670357473609658)
Godefroi had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7786493288700866)
Morgan Grant is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7154240000492645)
Morgan Grant has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8688267468984366)
Morgan Grant has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8365545874520802)
Morgan Grant had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7786493288700866)
Sir Francis Walters is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6697448487720212)
Sir Francis Walters has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8852352523606669)
Sir Francis Walters has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8596637847360897)
Sir Francis Walters had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7505527730327083)
### Captain Fosters
- mean: True (0.9066531077351827)
- motive: True (0.8705973031072073)
- opportunity: True (0.8031737798924701)

### Godefroi
- mean: False (0.1907240171073381)
- motive: False (0.13296425263903422)
- opportunity: False (0.22135067112991336)

### Morgan Grant
- mean: False (0.13117325310156336)
- motive: False (0.16344541254791978)
- opportunity: False (0.22135067112991336)

### Sir Francis Walters
- mean: False (0.11476474763933309)
- motive: False (0.14033621526391027)
- opportunity: False (0.2494472269672917)

The culprit is Captain Fosters.
In fact, it is Godefroi.
## 5minutemystery-mr-patricks-history-class
Map:   6%|▌         | 12/203 [04:15<1:12:47, 22.87s/ examples]Map:   6%|▋         | 13/203 [04:35<1:09:17, 21.88s/ examples]Corporal Tom Patrick is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8407826471261478)
Corporal Tom Patrick has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9142907234091052)
Corporal Tom Patrick has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6477981763584071)
Corporal Tom Patrick had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5851011336505011)
Pvt. Billy Calhoun is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9001793304600783)
Pvt. Billy Calhoun has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9284088027271398)
Pvt. Billy Calhoun has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7217431689117048)
Pvt. Billy Calhoun had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5195213440667139)
Pvt. Jack Trueblood is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9407897579933674)
Pvt. Jack Trueblood has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9496693599006181)
Pvt. Jack Trueblood has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8278281666221954)
Pvt. Jack Trueblood had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6808786440630326)
Sgt. Patrick Culpepper is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8872045854516336)
Sgt. Patrick Culpepper has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9257686153543061)
Sgt. Patrick Culpepper has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7956581141325956)
Sgt. Patrick Culpepper had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6566582306092376)
### Corporal Tom Patrick
- mean: False (0.08570927659089478)
- motive: False (0.3522018236415929)
- opportunity: False (0.4148988663494989)

### Pvt. Billy Calhoun
- mean: False (0.07159119727286023)
- motive: False (0.27825683108829524)
- opportunity: False (0.4804786559332861)

### Pvt. Jack Trueblood
- mean: True (0.9496693599006181)
- motive: True (0.8278281666221954)
- opportunity: True (0.6808786440630326)

### Sgt. Patrick Culpepper
- mean: False (0.0742313846456939)
- motive: False (0.20434188586740443)
- opportunity: False (0.34334176939076244)

The culprit is Pvt. Jack Trueblood.
In fact, it is Pvt. Billy Calhoun.
## 5minutemystery-bigfoot-mystery
Burt is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8529354311342636)
Burt has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9403530352223053)
Burt has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9705764653775313)
Burt had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8652241235443877)
Jerry is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8994751578343994)
Jerry has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9704646460964202)
Jerry has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9814534188350442)
Jerry had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9394705907755942)
Leng is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8031737798924701)
Leng has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9289263523387795)
Leng has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9669139993413022)
Leng had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8840392847025188)
Winston is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8092759828926619)
Winston has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9241418261705818)
Winston has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9599126594957205)
Winston had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8670357473609658)
### Burt
- mean: False (0.05964696477769471)
- motive: False (0.029423534622468717)
- opportunity: False (0.1347758764556123)

### Jerry
- mean: True (0.9704646460964202)
- motive: True (0.9814534188350442)
- opportunity: True (0.9394705907755942)

### Leng
- mean: False (0.07107364766122048)
- motive: False (0.03308600065869782)
- opportunity: False (0.1159607152974812)

### Winston
- mean: False (0.07585817382941817)
- motive: False (0.040087340504279534)
- opportunity: False (0.13296425263903422)

The culprit is Jerry.
In fact, it is Jerry.
## 5minutemystery-missing-movie-money
Billy is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8333246107254184)
Billy has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9167080509980843)
Billy has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8333246107254184)
Billy had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.821044090050916)
Map:   7%|▋         | 14/203 [04:55<1:07:24, 21.40s/ examples]Map:   7%|▋         | 15/203 [05:15<1:05:46, 20.99s/ examples]Cody is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7937461674149602)
Cody has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8947894610946939)
Cody has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8740772044235984)
Cody had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7879311977554747)
Juliet is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8316905440184192)
Juliet has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9142907234091052)
Juliet has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8587185689177256)
Juliet had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8056321690561029)
Tammy is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6601723415572317)
Tammy has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8397339530959691)
Tammy has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7431679939957333)
Tammy had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7090191197769757)
### Billy
- mean: False (0.08329194900191572)
- motive: False (0.1666753892745816)
- opportunity: False (0.17895590994908395)

### Cody
- mean: False (0.10521053890530607)
- motive: False (0.12592279557640162)
- opportunity: False (0.2120688022445253)

### Juliet
- mean: True (0.9142907234091052)
- motive: True (0.8587185689177256)
- opportunity: True (0.8056321690561029)

### Tammy
- mean: False (0.1602660469040309)
- motive: False (0.2568320060042667)
- opportunity: False (0.29098088022302426)

The culprit is Juliet.
In fact, it is Cody.
## 5minutemystery-missing-ammunition
Henry is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.862930245043327)
Henry has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8519527857346616)
Henry has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9178934131644976)
Henry had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8316905440184192)
Mr. Samuel is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8221890958162477)
Mr. Samuel has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9309620852900756)
Mr. Samuel has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9056565771882901)
Mr. Samuel had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8601343603168419)
Mr. Smith is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8418256636710214)
Mr. Smith has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9456006903352807)
Mr. Smith has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9227612010756272)
Mr. Smith had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.862930245043327)
Young Soldier is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6352224318508648)
Young Soldier has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8969755785184792)
Young Soldier has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8705972382426559)
Young Soldier had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8169911556077801)
### Henry
- mean: False (0.1480472142653384)
- motive: False (0.08210658683550243)
- opportunity: False (0.16830945598158076)

### Mr. Samuel
- mean: False (0.06903791470992438)
- motive: False (0.09434342281170993)
- opportunity: False (0.13986563968315813)

### Mr. Smith
- mean: True (0.9456006903352807)
- motive: True (0.9227612010756272)
- opportunity: True (0.862930245043327)

### Young Soldier
- mean: False (0.1030244214815208)
- motive: False (0.1294027617573441)
- opportunity: False (0.18300884439221987)

The culprit is Mr. Smith.
In fact, it is Henry.
## 5minutemystery-the-sky-sleuths
Bug collector is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.687629930977143)
Bug collector has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8333246107254184)
Bug collector has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8661325012437474)
Bug collector had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6825737331070684)
Elderly man is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7386690294153369)
Elderly man has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9105454073245608)
Elderly man has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9309620852900756)
Elderly man had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7074046739492601)
Family man is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6187804294217345)
Map:   8%|▊         | 16/203 [05:39<1:07:55, 21.80s/ examples]Map:   8%|▊         | 17/203 [05:59<1:06:09, 21.34s/ examples]Family man has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9268353022276509)
Family man has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.936749461409047)
Family man had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6406358487498992)
Motorcyclist is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6424325178417575)
Motorcyclist has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8824278139880716)
Motorcyclist has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8895288719962232)
Motorcyclist had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7090191197769757)
### Bug collector
- mean: False (0.1666753892745816)
- motive: False (0.1338674987562526)
- opportunity: False (0.31742626689293163)

### Elderly man
- mean: True (0.9105454073245608)
- motive: True (0.9309620852900756)
- opportunity: True (0.7074046739492601)

### Family man
- mean: False (0.07316469777234913)
- motive: False (0.06325053859095298)
- opportunity: False (0.3593641512501008)

### Motorcyclist
- mean: False (0.11757218601192843)
- motive: False (0.11047112800377679)
- opportunity: False (0.29098088022302426)

The culprit is Elderly man.
In fact, it is Bug collector.
## 5minutemystery-battle-of-the-bulge
Anderson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6671476985798853)
Anderson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8539127714046447)
Anderson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7853085971692302)
Anderson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6959583025067009)
Dilworth is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8670357473609658)
Dilworth has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8354835531737983)
Dilworth has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8840392847025188)
Dilworth had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.844921525814193)
Maguire is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7233095190955371)
Maguire has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7826625131049049)
Maguire has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8140528237853677)
Maguire had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7592254214399092)
Siegel is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7704647687904915)
Siegel has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7839884808423031)
Siegel has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8392075831473667)
Siegel had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7799929399351836)
### Anderson
- mean: False (0.14608722859535528)
- motive: False (0.21469140283076982)
- opportunity: False (0.3040416974932991)

### Dilworth
- mean: True (0.8354835531737983)
- motive: True (0.8840392847025188)
- opportunity: True (0.844921525814193)

### Maguire
- mean: False (0.21733748689509513)
- motive: False (0.1859471762146323)
- opportunity: False (0.24077457856009077)

### Siegel
- mean: False (0.2160115191576969)
- motive: False (0.16079241685263335)
- opportunity: False (0.2200070600648164)

The culprit is Dilworth.
In fact, it is Dilworth.
## 5minutemystery-the-missing-button
Eliza Murray is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8539127714046447)
Eliza Murray has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8774767496170098)
Eliza Murray has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9658995863383641)
Eliza Murray had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8895288719962232)
George Sanders is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8080671968507699)
George Sanders has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7634837587244478)
George Sanders has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9092645024391882)
George Sanders had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8000678954040312)
Stable boy Ian is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.740174341079517)
Stable boy Ian has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8770561879413864)
Stable boy Ian has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.934155284694701)
Stable boy Ian had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8402589628813668)
Thomas Murray is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8305941261447712)
Map:   9%|▉         | 18/203 [06:26<1:11:09, 23.08s/ examples]Map:   9%|▉         | 19/203 [06:49<1:10:56, 23.13s/ examples]Thomas Murray has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8647679145346777)
Thomas Murray has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9513234509300917)
Thomas Murray had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8381505623254643)
### Eliza Murray
- mean: True (0.8774767496170098)
- motive: True (0.9658995863383641)
- opportunity: True (0.8895288719962232)

### George Sanders
- mean: False (0.23651624127555215)
- motive: False (0.09073549756081178)
- opportunity: False (0.19993210459596877)

### Stable boy Ian
- mean: False (0.1229438120586136)
- motive: False (0.065844715305299)
- opportunity: False (0.1597410371186332)

### Thomas Murray
- mean: False (0.13523208546532228)
- motive: False (0.04867654906990826)
- opportunity: False (0.16184943767453575)

The culprit is Eliza Murray.
In fact, it is Stable boy Ian.
## 5minutemystery-the-railroad-mystery
Alvarado is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6315943123389512)
Alvarado has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8582439976623328)
Alvarado has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8929365260632085)
Alvarado had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6513548405484016)
The engineer is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6601724005812412)
The engineer has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7866228249849953)
The engineer has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8479678036998373)
The engineer had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.767689835247798)
The mechanic is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6297746298200823)
The mechanic has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7905302675820512)
The mechanic has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8587185689177256)
The mechanic had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7981867775042927)
Zebediah is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6636689235052821)
Zebediah has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8278281666221954)
Zebediah has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8386797935187188)
Zebediah had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7690802105138688)
### Alvarado
- mean: False (0.14175600233766716)
- motive: False (0.1070634739367915)
- opportunity: False (0.34864515945159835)

### The engineer
- mean: False (0.21337717501500475)
- motive: False (0.15203219630016274)
- opportunity: False (0.232310164752202)

### The mechanic
- mean: True (0.7905302675820512)
- motive: True (0.8587185689177256)
- opportunity: True (0.7981867775042927)

### Zebediah
- mean: False (0.17217183337780462)
- motive: False (0.1613202064812812)
- opportunity: False (0.23091978948613123)

The culprit is The mechanic.
In fact, it is Zebediah.
## 5minutemystery-the-date
Bob is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7490872087035162)
Bob has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8633916342942395)
Bob has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9167080509980843)
Bob had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.789233749534095)
Cynthia is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8019357965963964)
Cynthia has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9566341655109778)
Cynthia has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9559813721912603)
Cynthia had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8365545874520802)
Diane is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.720171518230031)
Diane has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.918480215734292)
Diane has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9343951361750445)
Diane had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8365545874520802)
Kristin is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6688802830862913)
Kristin has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8879840376027315)
Kristin has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9190633328333496)
Kristin had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7341195403199204)
### Bob
- mean: False (0.13660836570576051)
- motive: False (0.08329194900191572)
- opportunity: False (0.21076625046590503)

### Cynthia
- mean: True (0.9566341655109778)
- motive: True (0.9559813721912603)
- opportunity: True (0.8365545874520802)

### Diane
- mean: False (0.08151978426570805)
Map:  10%|▉         | 20/203 [07:10<1:08:32, 22.47s/ examples]Map:  10%|█         | 21/203 [07:29<1:04:24, 21.23s/ examples]Map:  11%|█         | 22/203 [07:54<1:07:49, 22.48s/ examples]- motive: False (0.06560486382495545)
- opportunity: False (0.16344541254791978)

### Kristin
- mean: False (0.11201596239726852)
- motive: False (0.08093666716665038)
- opportunity: False (0.26588045968007956)

The culprit is Cynthia.
In fact, it is Bob.
## 5minutemystery-b-movie-murder
Angela is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6531269509188588)
Angela has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8407825844829613)
Angela has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8469578650997759)
Angela had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7090191197769757)
Debbie is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5679366075542497)
Debbie has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7853085971692302)
Debbie has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8175745039697023)
Debbie had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6909762697651828)
Sal is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5544704821687028)
Sal has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7799928701983835)
Sal has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7563575572780217)
Sal had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6477981763584071)
Tom is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6095241816115718)
Tom has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8140528237853677)
Tom has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7431679939957333)
Tom had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6636689828419103)
### Angela
- mean: True (0.8407825844829613)
- motive: True (0.8469578650997759)
- opportunity: True (0.7090191197769757)

### Debbie
- mean: False (0.21469140283076982)
- motive: False (0.18242549603029767)
- opportunity: False (0.3090237302348172)

### Sal
- mean: False (0.22000712980161652)
- motive: False (0.24364244272197833)
- opportunity: False (0.3522018236415929)

### Tom
- mean: False (0.1859471762146323)
- motive: False (0.2568320060042667)
- opportunity: False (0.33633101715808966)

The culprit is Angela.
In fact, it is Angela.
## 5minutemystery-the-jackie-mitchell-autographed-baseball-mystery
Dr. Edgar Newton is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7648916137833577)
Dr. Edgar Newton has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8031737798924701)
Dr. Edgar Newton has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8840392847025188)
Dr. Edgar Newton had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6584174547581384)
Melinda Baker is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7956581141325956)
Melinda Baker has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8918110736745599)
Melinda Baker has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8469578650997759)
Melinda Baker had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7461389980806673)
Simon Plympton is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7994422859301654)
Simon Plympton has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9046505665674094)
Simon Plympton has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8633916342942395)
Simon Plympton had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.740174341079517)
Susan Plympton is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8577681165234065)
Susan Plympton has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8918110138739693)
Susan Plympton has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8509647293237851)
Susan Plympton had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7520125537161032)
### Dr. Edgar Newton
- mean: False (0.19682622010752993)
- motive: False (0.1159607152974812)
- opportunity: False (0.3415825452418616)

### Melinda Baker
- mean: False (0.10818892632544008)
- motive: False (0.1530421349002241)
- opportunity: False (0.2538610019193327)

### Simon Plympton
- mean: True (0.9046505665674094)
- motive: True (0.8633916342942395)
- opportunity: True (0.740174341079517)

### Susan Plympton
- mean: False (0.10818898612603067)
- motive: False (0.14903527067621491)
- opportunity: False (0.2479874462838968)

The culprit is Simon Plympton.
In fact, it is Susan Plympton.
## 5minutemystery-the-easter-egg-mystery
Anna is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8370879250561812)
Anna has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9372107968415931)
Anna has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.893681109060862)
Map:  11%|█▏        | 23/203 [08:13<1:04:03, 21.35s/ examples]Map:  12%|█▏        | 24/203 [08:32<1:01:32, 20.63s/ examples]Anna had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8895288719962232)
Cole is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7461389980806673)
Cole has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9304582506719414)
Cole has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8807970862580315)
Cole had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8683809699466569)
Justin is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7866228249849953)
Justin has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9312126617773815)
Justin has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7962924261546153)
Justin had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7759445334082792)
Lizzie is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8679338697256817)
Lizzie has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9498557456415421)
Lizzie has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9108631007029255)
Lizzie had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9026095892260383)
Rachel is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7732163648437078)
Rachel has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9102267057681164)
Rachel has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8169911556077801)
Rachel had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8386797935187188)
### Anna
- mean: False (0.06278920315840686)
- motive: False (0.10631889093913804)
- opportunity: False (0.11047112800377679)

### Cole
- mean: False (0.06954174932805857)
- motive: False (0.11920291374196845)
- opportunity: False (0.13161903005334308)

### Justin
- mean: False (0.06878733822261851)
- motive: False (0.20370757384538474)
- opportunity: False (0.22405546659172082)

### Lizzie
- mean: True (0.9498557456415421)
- motive: True (0.9108631007029255)
- opportunity: True (0.9026095892260383)

### Rachel
- mean: False (0.08977329423188363)
- motive: False (0.18300884439221987)
- opportunity: False (0.1613202064812812)

The culprit is Lizzie.
In fact, it is Lizzie.
## 5minutemystery-easter-rhyme
Abbott is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7146280500737092)
Abbott has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8514594452543962)
Abbott has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8428631416381634)
Abbott had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7669924589170153)
Andy is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7170119362627824)
Andy has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8803863464576128)
Andy has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.832781373043151)
Andy had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7468781552484828)
Randy is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7892336789711022)
Randy has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9121235591541035)
Randy has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.875361437979977)
Randy had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8068526417769779)
Speedy is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.794384956668203)
Speedy has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9063219998220023)
Speedy has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8606036289596553)
Speedy had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8098781635062345)
### Abbott
- mean: False (0.1485405547456038)
- motive: False (0.15713685836183655)
- opportunity: False (0.23300754108298471)

### Andy
- mean: False (0.11961365354238718)
- motive: False (0.16721862695684897)
- opportunity: False (0.2531218447515172)

### Randy
- mean: True (0.9121235591541035)
- motive: True (0.875361437979977)
- opportunity: True (0.8068526417769779)

### Speedy
- mean: False (0.09367800017799766)
- motive: False (0.13939637104034475)
- opportunity: False (0.19012183649376546)

The culprit is Randy.
In fact, it is Speedy.
## 5minutemystery-the-april-fool
Boston, MA is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7641883982873323)
Boston, MA has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8727816933272936)
Boston, MA has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8647679145346777)
Boston, MA had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
Map:  12%|█▏        | 25/203 [08:56<1:04:03, 21.59s/ examples]Map:  13%|█▎        | 26/203 [09:15<1:01:36, 20.88s/ examples]True (0.8300437877296776)
Philadelphia, PA is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6039318499573872)
Philadelphia, PA has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.879146760693242)
Philadelphia, PA has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7534666630720156)
Philadelphia, PA had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8006919661398397)
Pittsburgh, PA is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7364006034245382)
Pittsburgh, PA has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8701565822173906)
Pittsburgh, PA has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.811078188867804)
Pittsburgh, PA had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8454326455643386)
Raleigh, NC is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7057849857500714)
Raleigh, NC has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.883638264557296)
Raleigh, NC has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.832781310996106)
Raleigh, NC had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8289388437432279)
Washington, DC is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7826624547920057)
Washington, DC has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9139841191734227)
Washington, DC has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8875949368741688)
Washington, DC had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8543993214720741)
### Boston, MA
- mean: False (0.1272183066727064)
- motive: False (0.13523208546532228)
- opportunity: False (0.16995621227032243)

### Philadelphia, PA
- mean: False (0.12085323930675795)
- motive: False (0.2465333369279844)
- opportunity: False (0.19930803386016027)

### Pittsburgh, PA
- mean: False (0.12984341778260944)
- motive: False (0.18892181113219597)
- opportunity: False (0.15456735443566139)

### Raleigh, NC
- mean: False (0.116361735442704)
- motive: False (0.16721868900389403)
- opportunity: False (0.1710611562567721)

### Washington, DC
- mean: True (0.9139841191734227)
- motive: True (0.8875949368741688)
- opportunity: True (0.8543993214720741)

The culprit is Washington, DC.
In fact, it is Washington, DC.
## 5minutemystery-green-feet
Carm is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8499711693725173)
Carm has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9152045868398637)
Carm has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8278281049441929)
Carm had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7718434926244166)
Diane is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8872045854516336)
Diane has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9336731438527403)
Diane has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8807970862580315)
Diane had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8418256636710214)
Jen is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8193157928301305)
Jen has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8582439976623328)
Jen has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8044059309478723)
Jen had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7371581892031299)
Maureen is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8633915828320894)
Maureen has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9465966236120936)
Maureen has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8766343647921183)
Maureen had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8267117710471246)
### Carm
- mean: False (0.08479541316013628)
- motive: False (0.1721718950558071)
- opportunity: False (0.22815650737558335)

### Diane
- mean: True (0.9336731438527403)
- motive: True (0.8807970862580315)
- opportunity: True (0.8418256636710214)

### Jen
- mean: False (0.14175600233766716)
- motive: False (0.19559406905212773)
- opportunity: False (0.2628418107968701)

### Maureen
- mean: False (0.053403376387906376)
- motive: False (0.12336563520788169)
- opportunity: False (0.17328822895287543)

The culprit is Diane.
In fact, it is Diane.
## 5minutemystery-restaurant-roulette
Atsushi Nishi is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.72951977676791)
Atsushi Nishi has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8349459127213729)
Atsushi Nishi has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8474634858439474)
Atsushi Nishi had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
Map:  13%|█▎        | 27/203 [09:34<59:48, 20.39s/ examples]  Map:  14%|█▍        | 28/203 [09:56<1:00:39, 20.80s/ examples]True (0.7534666630720156)
Gianni Girodano is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8221891570741111)
Gianni Girodano has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7905303264811482)
Gianni Girodano has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8828325273478573)
Gianni Girodano had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7981867775042927)
Jack McDonald is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8365545874520802)
Jack McDonald has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8944211017064463)
Jack McDonald has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8910549899564296)
Jack McDonald had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7690802105138688)
Jean-Pierre Dubois is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8875948773562923)
Jean-Pierre Dubois has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9334308488586655)
Jean-Pierre Dubois has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9541373270174538)
Jean-Pierre Dubois had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8872045854516336)
### Atsushi Nishi
- mean: False (0.16505408727862714)
- motive: False (0.15253651415605263)
- opportunity: False (0.2465333369279844)

### Gianni Girodano
- mean: False (0.20946967351885182)
- motive: False (0.11716747265214267)
- opportunity: False (0.20181322249570732)

### Jack McDonald
- mean: False (0.10557889829355371)
- motive: False (0.10894501004357038)
- opportunity: False (0.23091978948613123)

### Jean-Pierre Dubois
- mean: True (0.9334308488586655)
- motive: True (0.9541373270174538)
- opportunity: True (0.8872045854516336)

The culprit is Jean-Pierre Dubois.
In fact, it is Gianni Girodano.
## 5minutemystery-violating-the-pirate-code
Bosun Ridley is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8140527631337082)
Bosun Ridley has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9653811448171958)
Bosun Ridley has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9429286143036572)
Bosun Ridley had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8267118326419537)
Mr Arbuthnot is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8914335394449011)
Mr Arbuthnot has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9637799266082508)
Mr Arbuthnot has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.934872446722342)
Mr Arbuthnot had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8354835531737983)
Nehemiah is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8509647293237851)
Nehemiah has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9612438076473231)
Nehemiah has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9263037480179213)
Nehemiah had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8661325012437474)
Will is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8504685773080045)
Will has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9612438076473231)
Will has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9339146597970963)
Will had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8092759828926619)
### Bosun Ridley
- mean: False (0.034618855182804165)
- motive: False (0.05707138569634285)
- opportunity: False (0.1732881673580463)

### Mr Arbuthnot
- mean: False (0.03622007339174915)
- motive: False (0.06512755327765796)
- opportunity: False (0.1645164468262017)

### Nehemiah
- mean: True (0.9612438076473231)
- motive: True (0.9263037480179213)
- opportunity: True (0.8661325012437474)

### Will
- mean: False (0.03875619235267691)
- motive: False (0.06608534020290369)
- opportunity: False (0.1907240171073381)

The culprit is Nehemiah.
In fact, it is Bosun Ridley.
## 5minutemystery-space-station-sagittarius-six-suffers-sabotage
Cpl. Bennington is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8267118326419537)
Cpl. Bennington has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9207896596153058)
Cpl. Bennington has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9525741334779666)
Cpl. Bennington had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8459424357871997)
Scrivine is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8679338697256817)
Scrivine has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8895288123486662)
Scrivine has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9329437018480795)
Map:  14%|█▍        | 29/203 [10:17<1:00:56, 21.01s/ examples]Map:  15%|█▍        | 30/203 [10:37<59:19, 20.58s/ examples]  Scrivine had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7956581141325956)
Sgt. O'Hennessey is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8333246107254184)
Sgt. O'Hennessey has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9294404371753803)
Sgt. O'Hennessey has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.94620036983)
Sgt. O'Hennessey had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8705973031072073)
Sgt.Valance is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7826625131049049)
Sgt.Valance has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8714749214913714)
Sgt.Valance has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8624675215861032)
Sgt.Valance had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7041600870830834)
### Cpl. Bennington
- mean: False (0.07921034038469421)
- motive: False (0.0474258665220334)
- opportunity: False (0.15405756421280026)

### Scrivine
- mean: False (0.11047118765133379)
- motive: False (0.06705629815192049)
- opportunity: False (0.20434188586740443)

### Sgt. O'Hennessey
- mean: True (0.9294404371753803)
- motive: True (0.94620036983)
- opportunity: True (0.8705973031072073)

### Sgt.Valance
- mean: False (0.1285250785086286)
- motive: False (0.13753247841389682)
- opportunity: False (0.2958399129169166)

The culprit is Sgt. O'Hennessey.
In fact, it is Sgt.Valance.
## 5minutemystery-flying-saucer-of-new-mexico
Dora is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7240905804783984)
Dora has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8795611817678315)
Dora has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.920504331042629)
Dora had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7931058945535956)
Lester is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7074046739492601)
Lester has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7745833454735581)
Lester has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8418256009501243)
Lester had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6619228707202935)
Uncle Art is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8140527631337082)
Uncle Art has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8740772044235984)
Uncle Art has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9111797236708432)
Uncle Art had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7892336789711022)
Zach is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7648916137833577)
Zach has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8679338697256817)
Zach has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9102267057681164)
Zach had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7918210572836727)
### Dora
- mean: True (0.8795611817678315)
- motive: True (0.920504331042629)
- opportunity: True (0.7931058945535956)

### Lester
- mean: False (0.22541665452644188)
- motive: False (0.15817439904987574)
- opportunity: False (0.33807712927970646)

### Uncle Art
- mean: False (0.12592279557640162)
- motive: False (0.08882027632915679)
- opportunity: False (0.2107663210288978)

### Zach
- mean: False (0.13206613027431835)
- motive: False (0.08977329423188363)
- opportunity: False (0.2081789427163273)

The culprit is Dora.
In fact, it is Dora.
## 5minutemystery-great-musket-mystery
Lyle Day is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7620701143808404)
Lyle Day has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8864204283224634)
Lyle Day has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9210740952879496)
Lyle Day had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8524448242555318)
Mary Wright is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7325918709325988)
Mary Wright has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8080671968507699)
Mary Wright has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8633915828320894)
Mary Wright had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7634837587244478)
Paul Revere is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6619228115397798)
Paul Revere has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8519528492100928)
Paul Revere has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8175745039697023)
Map:  15%|█▌        | 31/203 [11:00<1:01:16, 21.38s/ examples]Map:  16%|█▌        | 32/203 [11:30<1:08:05, 23.89s/ examples]Paul Revere had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7371581892031299)
Stevie Brown is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7592253761865491)
Stevie Brown has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8925625719484378)
Stevie Brown has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9069831945855868)
Stevie Brown had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8344069148356309)
### Lyle Day
- mean: True (0.8864204283224634)
- motive: True (0.9210740952879496)
- opportunity: True (0.8524448242555318)

### Mary Wright
- mean: False (0.1919328031492301)
- motive: False (0.1366084171679106)
- opportunity: False (0.23651624127555215)

### Paul Revere
- mean: False (0.14804715078990716)
- motive: False (0.18242549603029767)
- opportunity: False (0.2628418107968701)

### Stevie Brown
- mean: False (0.1074374280515622)
- motive: False (0.09301680541441315)
- opportunity: False (0.1655930851643691)

The culprit is Lyle Day.
In fact, it is Lyle Day.
## 5minutemystery-true-green-a-st-patricks-day-mystery
Emily Carpenter is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6297745735138451)
Emily Carpenter has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9092645024391882)
Emily Carpenter has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7981867775042927)
Emily Carpenter had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7325918054337844)
Evan Carpenter is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5058590748838109)
Evan Carpenter has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8509646659219744)
Evan Carpenter has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7577943897558946)
Evan Carpenter had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6057990946577705)
Richie Harris is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5813030649269245)
Richie Harris has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7918210572836727)
Richie Harris has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7279754274224494)
Richie Harris had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.571766542860143)
Zachary MacDonald is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.615087855649269)
Zachary MacDonald has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8984105603938967)
Zachary MacDonald has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8006920257960423)
Zachary MacDonald had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6740504382339836)
### Emily Carpenter
- mean: True (0.9092645024391882)
- motive: True (0.7981867775042927)
- opportunity: True (0.7325918054337844)

### Evan Carpenter
- mean: False (0.1490353340780256)
- motive: False (0.24220561024410536)
- opportunity: False (0.3942009053422295)

### Richie Harris
- mean: False (0.2081789427163273)
- motive: False (0.27202457257755064)
- opportunity: False (0.42823345713985705)

### Zachary MacDonald
- mean: False (0.10158943960610334)
- motive: False (0.19930797420395774)
- opportunity: False (0.3259495617660164)

The culprit is Emily Carpenter.
In fact, it is Emily Carpenter.
## 5minutemystery-st-patricks-day-pearls
Christopher is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8044059309478723)
Christopher has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9273632783787477)
Christopher has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9260365949489886)
Christopher had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8438950825214144)
Earl is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8255897087847518)
Earl has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8705972382426559)
Earl has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8740772044235984)
Earl had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7981867775042927)
Robert is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8267117710471246)
Robert has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9142907234091052)
Robert has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8933094122075369)
Robert had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8289388437432279)
Tom is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7813306496768853)
Tom has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8940517282497483)
Tom has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8679338697256817)
Map:  16%|█▋        | 33/203 [11:49<1:03:15, 22.33s/ examples]Map:  17%|█▋        | 34/203 [12:13<1:04:35, 22.93s/ examples]Tom had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8080671968507699)
### Christopher
- mean: True (0.9273632783787477)
- motive: True (0.9260365949489886)
- opportunity: True (0.8438950825214144)

### Earl
- mean: False (0.1294027617573441)
- motive: False (0.12592279557640162)
- opportunity: False (0.20181322249570732)

### Robert
- mean: False (0.08570927659089478)
- motive: False (0.1066905877924631)
- opportunity: False (0.1710611562567721)

### Tom
- mean: False (0.10594827175025168)
- motive: False (0.13206613027431835)
- opportunity: False (0.1919328031492301)

The culprit is Christopher.
In fact, it is Tom.
## 5minutemystery-death-in-the-theatre
Helen Smith is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6893056096647525)
Helen Smith has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8705973031072073)
Helen Smith has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8596637847360897)
Helen Smith had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8104789202520752)
Joanne Driscoll is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8006920257960423)
Joanne Driscoll has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9076402191395381)
Joanne Driscoll has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8824278665848695)
Joanne Driscoll had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8006920257960423)
Kevin Doyle is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6943026818003076)
Kevin Doyle has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8824278665848695)
Kevin Doyle has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8428631416381634)
Kevin Doyle had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7786493288700866)
Sarah Jones is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.740174341079517)
Sarah Jones has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8891443609199433)
Sarah Jones has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8719117627136385)
Sarah Jones had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8289388437432279)
### Helen Smith
- mean: False (0.1294026968927927)
- motive: False (0.14033621526391027)
- opportunity: False (0.18952107974792476)

### Joanne Driscoll
- mean: True (0.9076402191395381)
- motive: True (0.8824278665848695)
- opportunity: True (0.8006920257960423)

### Kevin Doyle
- mean: False (0.11757213341513051)
- motive: False (0.15713685836183655)
- opportunity: False (0.22135067112991336)

### Sarah Jones
- mean: False (0.11085563908005669)
- motive: False (0.12808823728636154)
- opportunity: False (0.1710611562567721)

The culprit is Joanne Driscoll.
In fact, it is Kevin Doyle.
## 5minutemystery-death-at-andersonville
Corporal Wardlow Horner is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7483522884503825)
Corporal Wardlow Horner has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8872045854516336)
Corporal Wardlow Horner has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6433292707767855)
Corporal Wardlow Horner had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5774954003013352)
Private Jamie Whisenant is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7348812840309261)
Private Jamie Whisenant has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.873646672673131)
Private Jamie Whisenant has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.5851012033999957)
Private Jamie Whisenant had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6654105788791005)
Sergeant Coleman Crosby is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7272012283179254)
Sergeant Coleman Crosby has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8906751877407573)
Sergeant Coleman Crosby has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
False (0.5679366075542497)
Sergeant Coleman Crosby had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
False (0.5321819753403337)
Sergeant Josiah Thornton is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7520125537161032)
Sergeant Josiah Thornton has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9026095892260383)
Sergeant Josiah Thornton has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.648688963544537)
Sergeant Josiah Thornton had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5926665645259142)
### Corporal Wardlow Horner
- mean: False (0.11279541454836639)
- motive: False (0.3566707292232145)
- opportunity: False (0.42250459969866483)

### Private Jamie Whisenant
- mean: False (0.126353327326869)
- motive: False (0.4148987966000043)
- opportunity: False (0.3345894211208995)

### Sergeant Coleman Crosby
- mean: False (0.10932481225924273)
- motive: False (0.5679366075542497)
Map:  17%|█▋        | 35/203 [12:31<1:00:00, 21.43s/ examples]Map:  18%|█▊        | 36/203 [12:51<58:25, 20.99s/ examples]  Map:  18%|█▊        | 37/203 [13:09<55:30, 20.06s/ examples]- opportunity: False (0.5321819753403337)

### Sergeant Josiah Thornton
- mean: True (0.9026095892260383)
- motive: True (0.648688963544537)
- opportunity: True (0.5926665645259142)

The culprit is Sergeant Josiah Thornton.
In fact, it is Sergeant Josiah Thornton.
## 5minutemystery-the-big-game
Carli Antor is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8407825844829613)
Carli Antor has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.945399403620829)
Carli Antor has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8289388437432279)
Carli Antor had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8344068526674736)
Chuck Jarrett is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8233283740192667)
Chuck Jarrett has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9435559526996434)
Chuck Jarrett has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8278281666221954)
Chuck Jarrett had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8413048399699521)
Rich Pender is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8620035048683017)
Rich Pender has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9294404371753803)
Rich Pender has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7662937064012869)
Rich Pender had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7981867775042927)
Tom Barrett is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7233094544266295)
Tom Barrett has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8966140749572745)
Tom Barrett has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.740174341079517)
Tom Barrett had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8204694405411458)
### Carli Antor
- mean: False (0.05460059637917103)
- motive: False (0.1710611562567721)
- opportunity: False (0.1655931473325264)

### Chuck Jarrett
- mean: True (0.9435559526996434)
- motive: True (0.8278281666221954)
- opportunity: True (0.8413048399699521)

### Rich Pender
- mean: False (0.07055956282461973)
- motive: False (0.2337062935987131)
- opportunity: False (0.20181322249570732)

### Tom Barrett
- mean: False (0.10338592504272548)
- motive: False (0.25982565892048304)
- opportunity: False (0.1795305594588542)

The culprit is Chuck Jarrett.
In fact, it is Tom Barrett.
## 5minutemystery-the-liberty-gun
Bob Turkle is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5851012033999957)
Bob Turkle has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7416740115009234)
Bob Turkle has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.821044090050916)
Bob Turkle had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7634837587244478)
Captain Parker is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7318258918270596)
Captain Parker has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8998277786460391)
Captain Parker has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8962513815714083)
Captain Parker had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8683809699466569)
Paul Rhodes is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7041600870830834)
Paul Rhodes has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.6123096993178739)
Paul Rhodes has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8244619332958376)
Paul Rhodes had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.740174341079517)
Tom Wise is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6233768569026616)
Tom Wise has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.6825737331070684)
Tom Wise has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7853085971692302)
Tom Wise had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7356416476869558)
### Bob Turkle
- mean: False (0.2583259884990766)
- motive: False (0.17895590994908395)
- opportunity: False (0.23651624127555215)

### Captain Parker
- mean: True (0.8998277786460391)
- motive: True (0.8962513815714083)
- opportunity: True (0.8683809699466569)

### Paul Rhodes
- mean: False (0.38769030068212607)
- motive: False (0.1755380667041624)
- opportunity: False (0.25982565892048304)

### Tom Wise
- mean: False (0.31742626689293163)
- motive: False (0.21469140283076982)
- opportunity: False (0.26435835231304416)

The culprit is Captain Parker.
In fact, it is Captain Parker.
## 5minutemystery-summer-camp
Allie is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7356416038392981)
Allie has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9407897579933674)
Allie has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
Map:  19%|█▊        | 38/203 [13:25<51:44, 18.81s/ examples]Map:  19%|█▉        | 39/203 [13:46<53:44, 19.66s/ examples]True (0.9046505665674094)
Allie had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8407825844829613)
Danny is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8354835531737983)
Danny has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9339146597970963)
Danny has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9167080509980843)
Danny had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8633916342942395)
Diane's campers is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8080671968507699)
Diane's campers has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.950777887812089)
Diane's campers has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9492946258008691)
Diane's campers had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9399133918829404)
Tom is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7704647687904915)
Tom has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9390248079664695)
Tom has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8984105603938967)
Tom had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8233283740192667)
### Allie
- mean: False (0.05921024200663261)
- motive: False (0.09534943343259061)
- opportunity: False (0.15921741551703872)

### Danny
- mean: False (0.06608534020290369)
- motive: False (0.08329194900191572)
- opportunity: False (0.13660836570576051)

### Diane's campers
- mean: True (0.950777887812089)
- motive: True (0.9492946258008691)
- opportunity: True (0.9399133918829404)

### Tom
- mean: False (0.06097519203353052)
- motive: False (0.10158943960610334)
- opportunity: False (0.17667162598073327)

The culprit is Diane's campers.
In fact, it is Tom.
## 5minutemystery-mystery-at-lyndleys-fort
Bo is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7655933544531522)
Bo has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7819972591886313)
Bo has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8397339530959691)
Bo had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7725306828324007)
John is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6379335503198971)
John has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7534666630720156)
John has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7669924589170153)
John had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6397360437814448)
John's wife is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5312093941731293)
John's wife has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7613611200983542)
John's wife has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8092759828926619)
John's wife had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7065955344877805)
Nathan Drew is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6706082735718226)
Nathan Drew has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7766228995235426)
Nathan Drew has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7813305798204846)
Nathan Drew had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6619228707202935)
### Bo
- mean: True (0.7819972591886313)
- motive: True (0.8397339530959691)
- opportunity: True (0.7725306828324007)

### John
- mean: False (0.2465333369279844)
- motive: False (0.23300754108298471)
- opportunity: False (0.3602639562185552)

### John's wife
- mean: False (0.23863887990164578)
- motive: False (0.1907240171073381)
- opportunity: False (0.29340446551221955)

### Nathan Drew
- mean: False (0.22337710047645742)
- motive: False (0.2186694201795154)
- opportunity: False (0.33807712927970646)

The culprit is Bo.
In fact, it is Nathan Drew.
## 5minutemystery-riddle-of-the-confederate-spy
Garrett is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9170058398600052)
Garrett has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.925499741040984)
Garrett has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.913058338092082)
Garrett had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8891443609199433)
McMurty is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9355823382423648)
McMurty has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9235923286659299)
McMurty has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9102267057681164)
McMurty had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
Map:  20%|█▉        | 40/203 [14:02<50:27, 18.58s/ examples]Map:  20%|██        | 41/203 [14:24<52:31, 19.45s/ examples]True (0.8591918406281239)
Parker is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.944176853162527)
Parker has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9302050495103452)
Parker has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9111796625714835)
Parker had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9063219998220023)
Winslow is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8955226517597132)
Winslow has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8803863464576128)
Winslow has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8365545251239088)
Winslow had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8596637206861489)
### Garrett
- mean: False (0.07450025895901602)
- motive: False (0.08694166190791797)
- opportunity: False (0.11085563908005669)

### McMurty
- mean: False (0.07640767133407012)
- motive: False (0.08977329423188363)
- opportunity: False (0.14080815937187607)

### Parker
- mean: True (0.9302050495103452)
- motive: True (0.9111796625714835)
- opportunity: True (0.9063219998220023)

### Winslow
- mean: False (0.11961365354238718)
- motive: False (0.16344547487609118)
- opportunity: False (0.14033627931385106)

The culprit is Parker.
In fact, it is Parker.
## 5minutemystery-thin-ice
Hortence Lacombe is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8757869551856522)
Hortence Lacombe has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9599126594957205)
Hortence Lacombe has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9339146597970963)
Hortence Lacombe had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8152325155686644)
Joe Tucker is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8787310683386846)
Joe Tucker has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9491062747098069)
Joe Tucker has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9216401608061056)
Joe Tucker had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7476159279883341)
Mikey Chanowski is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9196425651151865)
Mikey Chanowski has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9695556762577888)
Mikey Chanowski has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9534487716068757)
Mikey Chanowski had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8872045854516336)
Shea Callaghan is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8697145551802641)
Shea Callaghan has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.966537058600438)
Shea Callaghan has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9307105568817887)
Shea Callaghan had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8392075331266983)
### Hortence Lacombe
- mean: False (0.040087340504279534)
- motive: False (0.06608534020290369)
- opportunity: False (0.18476748443133562)

### Joe Tucker
- mean: False (0.05089372529019309)
- motive: False (0.07835983919389444)
- opportunity: False (0.2523840720116659)

### Mikey Chanowski
- mean: True (0.9695556762577888)
- motive: True (0.9534487716068757)
- opportunity: True (0.8872045854516336)

### Shea Callaghan
- mean: False (0.03346294139956196)
- motive: False (0.06928944311821128)
- opportunity: False (0.16079246687330173)

The culprit is Mikey Chanowski.
In fact, it is Shea Callaghan.
## 5minutemystery-flouted
Chloe Streamer is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.904313027820426)
Chloe Streamer has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9661559457424579)
Chloe Streamer has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9019206778000431)
Chloe Streamer had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8856314413364714)
Lyle Esposito is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8962513815714083)
Lyle Esposito has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9554855815192022)
Lyle Esposito has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.892187358563457)
Lyle Esposito had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8558511090164419)
Marty Nolan is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9012274173198201)
Marty Nolan has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9690910565174785)
Marty Nolan has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8757870204368676)
Marty Nolan had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8643104392003704)
Map:  21%|██        | 42/203 [14:46<54:22, 20.26s/ examples]Map:  21%|██        | 43/203 [15:05<53:12, 19.95s/ examples]Susan Moorgate is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.883638205304735)
Susan Moorgate has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9630919684645517)
Susan Moorgate has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9111796625714835)
Susan Moorgate had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8740772044235984)
### Chloe Streamer
- mean: True (0.9661559457424579)
- motive: True (0.9019206778000431)
- opportunity: True (0.8856314413364714)

### Lyle Esposito
- mean: False (0.044514418480797846)
- motive: False (0.10781264143654301)
- opportunity: False (0.1441488909835581)

### Marty Nolan
- mean: False (0.03090894348252149)
- motive: False (0.12421297956313238)
- opportunity: False (0.13568956079962957)

### Susan Moorgate
- mean: False (0.036908031535448305)
- motive: False (0.08882033742851647)
- opportunity: False (0.12592279557640162)

The culprit is Chloe Streamer.
In fact, it is Marty Nolan.
## 5minutemystery-car-trouble
Mr. Carlson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7106282704218558)
Mr. Carlson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9079670935046645)
Mr. Carlson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8929365260632085)
Mr. Carlson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.816406362162552)
Mr. Leamington is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7225270177274575)
Mr. Leamington has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9161096235973493)
Mr. Leamington has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8661325012437474)
Mr. Leamington had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7981867775042927)
Mrs. Roberts is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8104789202520752)
Mrs. Roberts has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9181873182746905)
Mrs. Roberts has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.920217993899809)
Mrs. Roberts had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8300437877296776)
Randy Peters is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6723316913929156)
Randy Peters has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9012274173198201)
Randy Peters has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8918110138739693)
Randy Peters had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7662936378892937)
### Mr. Carlson
- mean: False (0.09203290649533546)
- motive: False (0.1070634739367915)
- opportunity: False (0.18359363783744798)

### Mr. Leamington
- mean: False (0.08389037640265073)
- motive: False (0.1338674987562526)
- opportunity: False (0.20181322249570732)

### Mrs. Roberts
- mean: True (0.9181873182746905)
- motive: True (0.920217993899809)
- opportunity: True (0.8300437877296776)

### Randy Peters
- mean: False (0.09877258268017985)
- motive: False (0.10818898612603067)
- opportunity: False (0.23370636211070628)

The culprit is Mrs. Roberts.
In fact, it is Randy Peters.
## 5minutemystery-mr-poes-birthday-party
Anthony is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6654105788791005)
Anthony has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9039745373919651)
Anthony has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7356416038392981)
Anthony had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.821044090050916)
Connor is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7008948290825966)
Connor has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9032942081209032)
Connor has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7233094544266295)
Connor had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8661325012437474)
Skylar is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6325027218909103)
Skylar has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8568122429692968)
Skylar has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.5983121871760707)
Skylar had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7106282704218558)
Stephen is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7033457082786769)
Stephen has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8879840376027315)
Stephen has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.615087855649269)
Stephen had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7041600870830834)
Map:  22%|██▏       | 44/203 [15:30<56:42, 21.40s/ examples]Map:  22%|██▏       | 45/203 [15:51<55:43, 21.16s/ examples]Tommy is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6334102859975052)
Tommy has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9324532728823121)
Tommy has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7446563307563252)
Tommy had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8670357473609658)
### Anthony
- mean: False (0.0960254626080349)
- motive: False (0.2643583961607019)
- opportunity: False (0.17895590994908395)

### Connor
- mean: False (0.09670579187909678)
- motive: False (0.27669054557337047)
- opportunity: False (0.1338674987562526)

### Skylar
- mean: False (0.1431877570307032)
- motive: False (0.4016878128239293)
- opportunity: False (0.28937172957814417)

### Stephen
- mean: False (0.11201596239726852)
- motive: False (0.38491214435073096)
- opportunity: False (0.2958399129169166)

### Tommy
- mean: True (0.9324532728823121)
- motive: True (0.7446563307563252)
- opportunity: True (0.8670357473609658)

The culprit is Tommy.
In fact, it is Connor.
## 5minutemystery-the-root-of-all-evil
Bryan Durell is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8062431235779619)
Bryan Durell has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.919930758847437)
Bryan Durell has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7577943897558946)
Bryan Durell had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
False (0.5457699116223576)
Grieve Collier is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8244619332958376)
Grieve Collier has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9257686153543061)
Grieve Collier has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.77729988964086)
Grieve Collier had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6808785831877406)
Jacques Bourbonne is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7074046739492601)
Jacques Bourbonne has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8879840376027315)
Jacques Bourbonne has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7866228249849953)
Jacques Bourbonne had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6279512069990912)
Ruth Majick is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8397339530959691)
Ruth Majick has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9477691649813238)
Ruth Majick has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8918110138739693)
Ruth Majick had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8438950825214144)
### Bryan Durell
- mean: False (0.08006924115256298)
- motive: False (0.24220561024410536)
- opportunity: False (0.5457699116223576)

### Grieve Collier
- mean: False (0.0742313846456939)
- motive: False (0.22270011035913995)
- opportunity: False (0.31912141681225936)

### Jacques Bourbonne
- mean: False (0.11201596239726852)
- motive: False (0.21337717501500475)
- opportunity: False (0.37204879300090876)

### Ruth Majick
- mean: True (0.9477691649813238)
- motive: True (0.8918110138739693)
- opportunity: True (0.8438950825214144)

The culprit is Ruth Majick.
In fact, it is Bryan Durell.
## 5minutemystery-get-the-lead-out
Benjamin Trodger is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7592254214399092)
Benjamin Trodger has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9053223122169206)
Benjamin Trodger has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8233284353620131)
Benjamin Trodger had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7520125537161032)
Cynthia Kirwan is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7090191197769757)
Cynthia Kirwan has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8799743689174987)
Cynthia Kirwan has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7918210572836727)
Cynthia Kirwan had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6943027438758075)
Dan Skinner is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7185944237486072)
Dan Skinner has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8824278665848695)
Dan Skinner has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7154240000492645)
Dan Skinner had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6791786560103119)
Shel Jonas is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.72951977676791)
Shel Jonas has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8799744213680599)
Shel Jonas has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7476159948304097)
Map:  23%|██▎       | 46/203 [16:13<56:21, 21.54s/ examples]Map:  23%|██▎       | 47/203 [16:34<55:53, 21.50s/ examples]Map:  24%|██▎       | 48/203 [16:56<55:20, 21.42s/ examples]Shel Jonas had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.816406362162552)
### Benjamin Trodger
- mean: True (0.9053223122169206)
- motive: True (0.8233284353620131)
- opportunity: True (0.7520125537161032)

### Cynthia Kirwan
- mean: False (0.1200256310825013)
- motive: False (0.2081789427163273)
- opportunity: False (0.3056972561241925)

### Dan Skinner
- mean: False (0.11757213341513051)
- motive: False (0.28457599995073546)
- opportunity: False (0.3208213439896881)

### Shel Jonas
- mean: False (0.12002557863194008)
- motive: False (0.25238400516959025)
- opportunity: False (0.18359363783744798)

The culprit is Benjamin Trodger.
In fact, it is Dan Skinner.
## 5minutemystery-popping-a-wheelie
Cory is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7310585348819939)
Cory has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8940516749601143)
Cory has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8679338050595715)
Cory had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7662936378892937)
David is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7520125537161032)
David has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9142907234091052)
David has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8591918406281239)
David had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7008948290825966)
Mark is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8238958672039278)
Mark has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9394705907755942)
Mark has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9079671476237222)
Mark had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8459424357871997)
String is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5945512478395265)
String has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8489722037469682)
String has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8175745039697023)
String had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7704647687904915)
### Cory
- mean: False (0.10594832503988572)
- motive: False (0.13206619494042848)
- opportunity: False (0.23370636211070628)

### David
- mean: False (0.08570927659089478)
- motive: False (0.14080815937187607)
- opportunity: False (0.2991051709174034)

### Mark
- mean: True (0.9394705907755942)
- motive: True (0.9079671476237222)
- opportunity: True (0.8459424357871997)

### String
- mean: False (0.15102779625303175)
- motive: False (0.18242549603029767)
- opportunity: False (0.22953523120950847)

The culprit is Mark.
In fact, it is David.
## 5minutemystery-the-mystery-of-the-leprechauns-trophy
Barry is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7872777601997338)
Barry has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8679338697256817)
Barry has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9149009617112335)
Barry had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8925625719484378)
Casey is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7813306496768853)
Casey has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9481545078856665)
Casey has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9252299659402181)
Casey had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.893681109060862)
Mr. Carswell is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6893056096647525)
Mr. Carswell has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7718434926244166)
Mr. Carswell has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8381505623254643)
Mr. Carswell had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.776622945813876)
Tony is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7994422859301654)
Tony has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.934155284694701)
Tony has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9222025890552223)
Tony had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.861071588244826)
### Barry
- mean: False (0.13206613027431835)
- motive: False (0.08509903828876653)
- opportunity: False (0.1074374280515622)

### Casey
- mean: True (0.9481545078856665)
- motive: True (0.9252299659402181)
- opportunity: True (0.893681109060862)

### Mr. Carswell
- mean: False (0.22815650737558335)
- motive: False (0.16184943767453575)
- opportunity: False (0.22337705418612397)

### Tony
- mean: False (0.065844715305299)
- motive: False (0.07779741094477766)
- opportunity: False (0.138928411755174)

The culprit is Casey.
In fact, it is Tony.
## 5minutemystery-the-mysterious-chicken
Ed is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7534666630720156)
Map:  24%|██▍       | 49/203 [17:16<54:06, 21.08s/ examples]Map:  25%|██▍       | 50/203 [17:31<49:30, 19.42s/ examples]Ed has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8984105603938967)
Ed has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9066531077351827)
Ed had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6619228707202935)
Ed's mother is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7718434926244166)
Ed's mother has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9066531685310133)
Ed's mother has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8705972382426559)
Ed's mother had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7956581141325956)
Ed’s Husky is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8454326455643386)
Ed’s Husky has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.878314250659373)
Ed’s Husky has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9312126617773815)
Ed’s Husky had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7969253675907205)
Zeke is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7745833916423246)
Zeke has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.934872446722342)
Zeke has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.941654147692963)
Zeke had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8140528237853677)
### Ed
- mean: False (0.10158943960610334)
- motive: False (0.0933468922648173)
- opportunity: False (0.33807712927970646)

### Ed's mother
- mean: False (0.0933468314689867)
- motive: False (0.1294027617573441)
- opportunity: False (0.20434188586740443)

### Ed’s Husky
- mean: False (0.12168574934062704)
- motive: False (0.06878733822261851)
- opportunity: False (0.20307463240927948)

### Zeke
- mean: True (0.934872446722342)
- motive: True (0.941654147692963)
- opportunity: True (0.8140528237853677)

The culprit is Zeke.
In fact, it is Ed.
## 5minutemystery-the-late-night-horror-show
Andrew is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5755879969637064)
Andrew has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9114953293645017)
Andrew has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.64779823427608)
Andrew had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.776622945813876)
David is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.794384956668203)
David has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9509603994010378)
David has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7490872087035162)
David had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8489722037469682)
Dennis is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7264255794048772)
Dennis has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9527502639818524)
Dennis has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7772998201448375)
Dennis had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8238958672039278)
Matthew is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6926419789019715)
Matthew has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9405717864730483)
Matthew has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6791787167336184)
Matthew had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8152325155686644)
### Andrew
- mean: False (0.08850467063549827)
- motive: False (0.35220176572392004)
- opportunity: False (0.22337705418612397)

### David
- mean: False (0.049039600598962174)
- motive: False (0.2509127912964838)
- opportunity: False (0.15102779625303175)

### Dennis
- mean: True (0.9527502639818524)
- motive: True (0.7772998201448375)
- opportunity: True (0.8238958672039278)

### Matthew
- mean: False (0.05942821352695171)
- motive: False (0.3208212832663816)
- opportunity: False (0.18476748443133562)

The culprit is Dennis.
In fact, it is David.
## 5minutemystery-making-partner
Dan Cartman is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7520125537161032)
Dan Cartman has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.934872446722342)
Dan Cartman has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8692713407917644)
Dan Cartman had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7866228249849953)
Jill is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6433293282949071)
Jill has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8872045854516336)
Map:  25%|██▌       | 51/203 [17:56<53:21, 21.07s/ examples]Map:  26%|██▌       | 52/203 [18:17<52:37, 20.91s/ examples]Jill has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9095863097773887)
Jill had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7676898810056793)
Mike Creighton is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6601724005812412)
Mike Creighton has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.879146760693242)
Mike Creighton has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8524448242555318)
Mike Creighton had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8152325155686644)
Mrs. Krantz is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.705785027818136)
Mrs. Krantz has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8991213421091365)
Mrs. Krantz has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9167081124681512)
Mrs. Krantz had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7386690954574974)
### Dan Cartman
- mean: True (0.934872446722342)
- motive: True (0.8692713407917644)
- opportunity: True (0.7866228249849953)

### Jill
- mean: False (0.11279541454836639)
- motive: False (0.09041369022261125)
- opportunity: False (0.23231011899432075)

### Mike Creighton
- mean: False (0.12085323930675795)
- motive: False (0.1475551757444682)
- opportunity: False (0.18476748443133562)

### Mrs. Krantz
- mean: False (0.10087865789086348)
- motive: False (0.0832918875318488)
- opportunity: False (0.26133090454250263)

The culprit is Dan Cartman.
In fact, it is Mike Creighton.
## 5minutemystery-no-retreat-from-death
Amanda Kent is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5851012033999957)
Amanda Kent has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7106283339569771)
Amanda Kent has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8158201638039532)
Amanda Kent had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6076631662366868)
Craig Willis is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.503906199448032)
Craig Willis has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.847967740521315)
Craig Willis has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7826625131049049)
Craig Willis had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6601724005812412)
Niles Anderson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
False (0.5292633777076584)
Niles Anderson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7325918054337844)
Niles Anderson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7846493136763113)
Niles Anderson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
False (0.5234203246639862)
Stephanie Clark is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5350984235603058)
Stephanie Clark has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7371581232960549)
Stephanie Clark has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.802555560073231)
Stephanie Clark had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5907791930117218)
### Amanda Kent
- mean: False (0.2893716660430229)
- motive: False (0.18417983619604683)
- opportunity: False (0.3923368337633132)

### Craig Willis
- mean: True (0.847967740521315)
- motive: True (0.7826625131049049)
- opportunity: True (0.6601724005812412)

### Niles Anderson
- mean: False (0.26740819456621556)
- motive: False (0.2153506863236887)
- opportunity: False (0.5234203246639862)

### Stephanie Clark
- mean: False (0.2628418767039451)
- motive: False (0.19744443992676897)
- opportunity: False (0.40922080698827823)

The culprit is Craig Willis.
In fact, it is Niles Anderson.
## 5minutemystery-a-monster-of-a-mystery
Donald is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6566582306092376)
Donald has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7981867775042927)
Donald has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8587185689177256)
Donald had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6893056507505698)
Linda is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6334102859975052)
Linda has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8509647293237851)
Linda has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8745065279415651)
Linda had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7217432334405754)
Randy is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6926419789019715)
Randy has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8587185689177256)
Map:  26%|██▌       | 53/203 [18:41<54:20, 21.74s/ examples]Map:  27%|██▋       | 54/203 [19:03<54:17, 21.86s/ examples]Randy has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8918110138739693)
Randy had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6723316913929156)
Wendell is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.646013666311734)
Wendell has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8175744430556572)
Wendell has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8587185689177256)
Wendell had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7386690954574974)
### Donald
- mean: False (0.20181322249570732)
- motive: False (0.14128143108227442)
- opportunity: False (0.3106943492494302)

### Linda
- mean: True (0.8509647293237851)
- motive: True (0.8745065279415651)
- opportunity: True (0.7217432334405754)

### Randy
- mean: False (0.14128143108227442)
- motive: False (0.10818898612603067)
- opportunity: False (0.3276683086070844)

### Wendell
- mean: False (0.18242555694434281)
- motive: False (0.14128143108227442)
- opportunity: False (0.26133090454250263)

The culprit is Linda.
In fact, it is Linda.
## 5minutemystery-chow-baby
Beryl Hives is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6169358476670045)
Beryl Hives has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7634837587244478)
Beryl Hives has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7549149897594328)
Beryl Hives had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6636689235052821)
Dawn de Jong is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6740504382339836)
Dawn de Jong has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8221890958162477)
Dawn de Jong has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7813306496768853)
Dawn de Jong had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7563575572780217)
Konrad Pushkin is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6297746298200823)
Konrad Pushkin has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8044059309478723)
Konrad Pushkin has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8198932995357624)
Konrad Pushkin had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6261242000979097)
Pete Stampkowski is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6842640693504702)
Pete Stampkowski has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8568122940392877)
Pete Stampkowski has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8311430831606665)
Pete Stampkowski had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6774740084332073)
### Beryl Hives
- mean: False (0.23651624127555215)
- motive: False (0.24508501024056717)
- opportunity: False (0.33633107649471794)

### Dawn de Jong
- mean: False (0.17781090418375234)
- motive: False (0.21866935032311474)
- opportunity: False (0.24364244272197833)

### Konrad Pushkin
- mean: False (0.19559406905212773)
- motive: False (0.1801067004642376)
- opportunity: False (0.3738757999020903)

### Pete Stampkowski
- mean: True (0.8568122940392877)
- motive: True (0.8311430831606665)
- opportunity: True (0.6774740084332073)

The culprit is Pete Stampkowski.
In fact, it is Beryl Hives.
## 5minutemystery-the-mystery-of-the-frowning-clown
Bumbo is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9487276064711105)
Bumbo has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9619649048746262)
Bumbo has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9702399365512847)
Bumbo had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9299510095943111)
Dusty is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.924959242644946)
Dusty has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8633915828320894)
Dusty has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9376689781587124)
Dusty had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.879146760693242)
Mr. Green is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9032942081209032)
Mr. Green has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9583821892129424)
Mr. Green has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9744347924514057)
Mr. Green had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8757870204368676)
Stage Manager is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8807970862580315)
Stage Manager has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9704646460964202)
Map:  27%|██▋       | 55/203 [19:34<1:00:56, 24.71s/ examples]Map:  28%|██▊       | 56/203 [20:02<1:03:10, 25.79s/ examples]Map:  28%|██▊       | 57/203 [20:29<1:03:01, 25.90s/ examples]Stage Manager has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9811668402824711)
Stage Manager had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9257686705344172)
### Bumbo
- mean: False (0.03803509512537384)
- motive: False (0.02976006344871529)
- opportunity: False (0.0700489904056889)

### Dusty
- mean: False (0.1366084171679106)
- motive: False (0.06233102184128758)
- opportunity: False (0.12085323930675795)

### Mr. Green
- mean: False (0.04161781078705762)
- motive: False (0.02556520754859426)
- opportunity: False (0.12421297956313238)

### Stage Manager
- mean: True (0.9704646460964202)
- motive: True (0.9811668402824711)
- opportunity: True (0.9257686705344172)

The culprit is Stage Manager.
In fact, it is Stage Manager.
## 5minutemystery-the-strangest-sport-of-all
Ernie is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9433475737015985)
Ernie has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9640516654033661)
Ernie has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9720985894741414)
Ernie had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9207896596153058)
Gordon is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9187722208906307)
Gordon has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9385759849623091)
Gordon has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9467937951644804)
Gordon had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8365545874520802)
Jesse is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9046505665674094)
Jesse has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9289263523387795)
Jesse has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8940517282497483)
Jesse had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8991213421091365)
Mac is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9369805475192257)
Mac has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9491062747098069)
Mac has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9622497571173928)
Mac had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8553686139061228)
### Ernie
- mean: True (0.9640516654033661)
- motive: True (0.9720985894741414)
- opportunity: True (0.9207896596153058)

### Gordon
- mean: False (0.061424015037690904)
- motive: False (0.05320620483551963)
- opportunity: False (0.16344541254791978)

### Jesse
- mean: False (0.07107364766122048)
- motive: False (0.10594827175025168)
- opportunity: False (0.10087865789086348)

### Mac
- mean: False (0.05089372529019309)
- motive: False (0.0377502428826072)
- opportunity: False (0.14463138609387716)

The culprit is Ernie.
In fact, it is Jesse.
## 5minutemystery-who-stole-storimons-wallet
Danny is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7025300310583819)
Danny has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8333246107254184)
Danny has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.844921525814193)
Danny had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8365545251239088)
Mick is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7008948290825966)
Mick has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8962513815714083)
Mick has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8697145551802641)
Mick had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.847967740521315)
Mr. Storimon is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6113819501087365)
Mr. Storimon has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8807970862580315)
Mr. Storimon has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9307106123564625)
Mr. Storimon had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8128673413132903)
Policeman is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
False (0.5019531141001669)
Policeman has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8688268116310761)
Policeman has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.904313027820426)
Policeman had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8365545874520802)
### Danny
- mean: False (0.1666753892745816)
- motive: False (0.155078474185807)
- opportunity: False (0.16344547487609118)

### Mick
- mean: False (0.10374861842859173)
- motive: False (0.13028544481973592)
- opportunity: False (0.15203225947868504)

### Mr. Storimon
- mean: True (0.8807970862580315)
- motive: True (0.9307106123564625)
- opportunity: True (0.8128673413132903)

### Policeman
- mean: False (0.1311731883689239)
- motive: False (0.095686972179574)
- opportunity: False (0.16344541254791978)

The culprit is Mr. Storimon.
In fact, it is Mr. Storimon.
Map:  29%|██▊       | 58/203 [20:54<1:02:33, 25.89s/ examples]Map:  29%|██▉       | 59/203 [21:13<57:06, 23.79s/ examples]  ## 5minutemystery-miles-archer-solves-a-case
Arnold Grossmecker is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7122321792841629)
Arnold Grossmecker has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.887204644943339)
Arnold Grossmecker has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9401335713518422)
Arnold Grossmecker had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.767689835247798)
Brigid Jellicoe is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7641884666111024)
Brigid Jellicoe has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.878314250659373)
Brigid Jellicoe has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9317114347547434)
Brigid Jellicoe had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8606036289596553)
Quinton Jesselton is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7534666630720156)
Quinton Jesselton has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9334308488586655)
Quinton Jesselton has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9549844874375936)
Quinton Jesselton had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8558511727823209)
Sandra O’Malley is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6943026818003076)
Sandra O’Malley has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8962513815714083)
Sandra O’Malley has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9463989149207153)
Sandra O’Malley had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7662937064012869)
### Arnold Grossmecker
- mean: False (0.11279535505666105)
- motive: False (0.05986642864815783)
- opportunity: False (0.232310164752202)

### Brigid Jellicoe
- mean: False (0.12168574934062704)
- motive: False (0.06828856524525662)
- opportunity: False (0.13939637104034475)

### Quinton Jesselton
- mean: True (0.9334308488586655)
- motive: True (0.9549844874375936)
- opportunity: True (0.8558511727823209)

### Sandra O’Malley
- mean: False (0.10374861842859173)
- motive: False (0.05360108507928474)
- opportunity: False (0.2337062935987131)

The culprit is Quinton Jesselton.
In fact, it is Quinton Jesselton.
## 5minutemystery-murder-in-the-early-morning
Constance is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6893056096647525)
Constance has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8193157928301305)
Constance has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7592254214399092)
Constance had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6451199006197486)
John is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6522414018725713)
John has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8062431836477579)
John has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6531269509188588)
John had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
False (0.5621765360769869)
Nancy is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6909763109505791)
Nancy has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8701565303520181)
Nancy has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7170118721569225)
Nancy had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.720171518230031)
Vernon is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7759445796581789)
Vernon has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8386797310322072)
Vernon has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7386690294153369)
Vernon had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5097643762740132)
### Constance
- mean: False (0.18068420716986955)
- motive: False (0.24077457856009077)
- opportunity: False (0.35488009938025145)

### John
- mean: False (0.19375681635224207)
- motive: False (0.34687304908114125)
- opportunity: False (0.5621765360769869)

### Nancy
- mean: True (0.8701565303520181)
- motive: True (0.7170118721569225)
- opportunity: True (0.720171518230031)

### Vernon
- mean: False (0.16132026896779283)
- motive: False (0.26133097058466315)
- opportunity: False (0.49023562372598684)

The culprit is Nancy.
In fact, it is Vernon.
## 5minutemystery-raiding-cane
Brent Pearson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7527403228571042)
Brent Pearson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8647679145346777)
Brent Pearson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7937462383814009)
Brent Pearson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
Map:  30%|██▉       | 60/203 [21:33<53:43, 22.54s/ examples]Map:  30%|███       | 61/203 [22:01<57:00, 24.09s/ examples]True (0.789233749534095)
Frank Weiss is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9032942081209032)
Frank Weiss has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9407897579933674)
Frank Weiss has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.927887794449634)
Frank Weiss had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8745065279415651)
Michael Weiss is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7669925046333297)
Michael Weiss has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8987665204865408)
Michael Weiss has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8074606715677252)
Michael Weiss had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7256486384635821)
Ronald Weiss is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7859664553110391)
Ronald Weiss has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.925499741040984)
Ronald Weiss has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8925625120974553)
Ronald Weiss had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7676898810056793)
### Brent Pearson
- mean: False (0.13523208546532228)
- motive: False (0.2062537616185991)
- opportunity: False (0.21076625046590503)

### Frank Weiss
- mean: True (0.9407897579933674)
- motive: True (0.927887794449634)
- opportunity: True (0.8745065279415651)

### Michael Weiss
- mean: False (0.10123347951345918)
- motive: False (0.19253932843227484)
- opportunity: False (0.2743513615364179)

### Ronald Weiss
- mean: False (0.07450025895901602)
- motive: False (0.1074374879025447)
- opportunity: False (0.23231011899432075)

The culprit is Frank Weiss.
In fact, it is Frank Weiss.
## 5minutemystery-the-missing-dagger
Chris Palmer is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8688268116310761)
Chris Palmer has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9152045868398637)
Chris Palmer has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.935346481802689)
Chris Palmer had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8910549302065384)
Matthew Light is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7813306496768853)
Matthew Light has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8848377441095496)
Matthew Light has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8714748565614324)
Matthew Light had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8068526417769779)
Mitchell Land is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8068526417769779)
Mitchell Land has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9207896596153058)
Mitchell Land has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9111797236708432)
Mitchell Land had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8568122940392877)
Paul Benham is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.854884683810039)
Paul Benham has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9383503780077049)
Paul Benham has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8539127077831877)
Paul Benham had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8278281049441929)
Russell Smith is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.821044090050916)
Russell Smith has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9304582506719414)
Russell Smith has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.847967740521315)
Russell Smith had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8407826471261478)
### Chris Palmer
- mean: True (0.9152045868398637)
- motive: True (0.935346481802689)
- opportunity: True (0.8910549302065384)

### Matthew Light
- mean: False (0.11516225589045037)
- motive: False (0.12852514343856758)
- opportunity: False (0.1931473582230221)

### Mitchell Land
- mean: False (0.07921034038469421)
- motive: False (0.08882027632915679)
- opportunity: False (0.14318770596071229)

### Paul Benham
- mean: False (0.06164962199229507)
- motive: False (0.14608729221681227)
- opportunity: False (0.1721718950558071)

### Russell Smith
- mean: False (0.06954174932805857)
- motive: False (0.15203225947868504)
- opportunity: False (0.1592173528738522)

The culprit is Chris Palmer.
In fact, it is Paul Benham.
## 5minutemystery-mystery-of-the-bratty-kid
Angelita is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7577943897558946)
Angelita has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7799928701983835)
Angelita has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9431384220853135)
Map:  31%|███       | 62/203 [22:29<59:52, 25.48s/ examples]Map:  31%|███       | 63/203 [22:49<55:14, 23.67s/ examples]Angelita had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7918210572836727)
Emily is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8459424357871997)
Emily has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8606036289596553)
Emily has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9645892389558273)
Emily had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8418256636710214)
Jessica is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7057849857500714)
Jessica has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7759445334082792)
Jessica has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9401335713518422)
Jessica had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7905302675820512)
Percy Wellington is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9056565771882901)
Percy Wellington has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9339146597970963)
Percy Wellington has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9730364677532105)
Percy Wellington had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8902942539348153)
### Angelita
- mean: False (0.22000712980161652)
- motive: False (0.05686157791468649)
- opportunity: False (0.2081789427163273)

### Emily
- mean: False (0.13939637104034475)
- motive: False (0.035410761044172734)
- opportunity: False (0.1581743363289786)

### Jessica
- mean: False (0.22405546659172082)
- motive: False (0.05986642864815783)
- opportunity: False (0.20946973241794875)

### Percy Wellington
- mean: True (0.9339146597970963)
- motive: True (0.9730364677532105)
- opportunity: True (0.8902942539348153)

The culprit is Percy Wellington.
In fact, it is Angelita.
## 5minutemystery-the-card-shark
The cowboy is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6388353131709135)
The cowboy has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7892336789711022)
The cowboy has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.5563995301351303)
The cowboy had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5409238326546766)
The gunslinger is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6460137433225688)
The gunslinger has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7577943220037995)
The gunslinger has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6187804294217345)
The gunslinger had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5736783792247284)
The lady is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7577943220037995)
The lady has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7994423454932595)
The lady has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6169357925086439)
The lady had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6076631662366868)
The sheriff is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6279512069990912)
The sheriff has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7577943897558946)
The sheriff has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7000752133823226)
The sheriff had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6095241816115718)
### The cowboy
- mean: False (0.2107663210288978)
- motive: False (0.4436004698648697)
- opportunity: False (0.4590761673453234)

### The gunslinger
- mean: False (0.24220567799620052)
- motive: False (0.3812195705782655)
- opportunity: False (0.4263216207752716)

### The lady
- mean: False (0.20055765450674046)
- motive: False (0.38306420749135606)
- opportunity: False (0.3923368337633132)

### The sheriff
- mean: True (0.7577943897558946)
- motive: True (0.7000752133823226)
- opportunity: True (0.6095241816115718)

The culprit is The sheriff.
In fact, it is The sheriff.
## 5minutemystery-department-store-murder
Ed Puckett is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6513548405484016)
Ed Puckett has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.94519740270931)
Ed Puckett has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.64779823427608)
Ed Puckett had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8198932995357624)
Gene Roberts is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6495786332146115)
Gene Roberts has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8824278665848695)
Gene Roberts has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.642432441257838)
Map:  32%|███▏      | 64/203 [23:06<50:27, 21.78s/ examples]Map:  32%|███▏      | 65/203 [23:28<50:20, 21.89s/ examples]Gene Roberts had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7520125537161032)
George Whitley is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7170118721569225)
George Whitley has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9351099114717211)
George Whitley has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7563575572780217)
George Whitley had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7885831565209055)
Justin Tanner is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7154240000492645)
Justin Tanner has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9447913165152162)
Justin Tanner has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7356416476869558)
Justin Tanner had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7931059536445917)
### Ed Puckett
- mean: False (0.054802597290690036)
- motive: False (0.35220176572392004)
- opportunity: False (0.1801067004642376)

### Gene Roberts
- mean: False (0.11757213341513051)
- motive: False (0.35756755874216195)
- opportunity: False (0.2479874462838968)

### George Whitley
- mean: True (0.9351099114717211)
- motive: True (0.7563575572780217)
- opportunity: True (0.7885831565209055)

### Justin Tanner
- mean: False (0.055208683484783805)
- motive: False (0.26435835231304416)
- opportunity: False (0.2068940463554083)

The culprit is George Whitley.
In fact, it is Justin Tanner.
## 5minutemystery-the-candy-store-mystery
Brianna Cates is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8037905715242155)
Brianna Cates has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9629528509146777)
Brianna Cates has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.908941745727715)
Brianna Cates had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8914335992201801)
Emilee Johnson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7994423454932595)
Emilee Johnson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9669139993413022)
Emilee Johnson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.874934615163517)
Emilee Johnson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9069831945855868)
Justin Cates is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7248702601920561)
Justin Cates has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9284088027271398)
Justin Cates has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8198933606225757)
Justin Cates had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.811078188867804)
Olivia (Livvie) Johnson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7924642605907138)
Olivia (Livvie) Johnson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9498557456415421)
Olivia (Livvie) Johnson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8553685501761973)
Olivia (Livvie) Johnson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9124361266596831)
Trevor Cates is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7162185953247016)
Trevor Cates has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9541373270174538)
Trevor Cates has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8233283740192667)
Trevor Cates had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8615382357584752)
### Brianna Cates
- mean: True (0.9629528509146777)
- motive: True (0.908941745727715)
- opportunity: True (0.8914335992201801)

### Emilee Johnson
- mean: False (0.03308600065869782)
- motive: False (0.125065384836483)
- opportunity: False (0.09301680541441315)

### Justin Cates
- mean: False (0.07159119727286023)
- motive: False (0.18010663937742433)
- opportunity: False (0.18892181113219597)

### Olivia (Livvie) Johnson
- mean: False (0.05014425435845793)
- motive: False (0.14463144982380272)
- opportunity: False (0.0875638733403169)

### Trevor Cates
- mean: False (0.045862672982546204)
- motive: False (0.17667162598073327)
- opportunity: False (0.1384617642415248)

The culprit is Brianna Cates.
In fact, it is Justin Cates.
## 5minutemystery-for-the-birds
Billy Mumms is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.77729988964086)
Billy Mumms has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9164093141890854)
Billy Mumms has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8799743689174987)
Billy Mumms had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8333246107254184)
Cheryl Judson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8080671968507699)
Cheryl Judson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
Map:  33%|███▎      | 66/203 [23:52<51:06, 22.38s/ examples]Map:  33%|███▎      | 67/203 [24:12<49:23, 21.79s/ examples]True (0.9322068076615162)
Cheryl Judson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9063219458010031)
Cheryl Judson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9001793304600783)
Stan Mifflin is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7534666630720156)
Stan Mifflin has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9284088027271398)
Stan Mifflin has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8568122940392877)
Stan Mifflin had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8181563669811865)
Tor Hansen is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.779321849347754)
Tor Hansen has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9353465445225602)
Tor Hansen has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8499711693725173)
Tor Hansen had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8661325012437474)
### Billy Mumms
- mean: False (0.08359068581091456)
- motive: False (0.1200256310825013)
- opportunity: False (0.1666753892745816)

### Cheryl Judson
- mean: True (0.9322068076615162)
- motive: True (0.9063219458010031)
- opportunity: True (0.9001793304600783)

### Stan Mifflin
- mean: False (0.07159119727286023)
- motive: False (0.14318770596071229)
- opportunity: False (0.18184363301881346)

### Tor Hansen
- mean: False (0.06465345547743984)
- motive: False (0.15002883062748273)
- opportunity: False (0.1338674987562526)

The culprit is Cheryl Judson.
In fact, it is Cheryl Judson.
## 5minutemystery-the-zoo-job
Cindy is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8238958672039278)
Cindy has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.941654147692963)
Cindy has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9216401608061056)
Cindy had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8128673413132903)
Henry is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8349459127213729)
Henry has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9294404371753803)
Henry has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9381240005131491)
Henry had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8418256636710214)
Leonard is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8175744430556572)
Leonard has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9099069836112468)
Leonard has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8962513214730718)
Leonard had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7879311977554747)
Tom is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7585105966624085)
Tom has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9059897640502081)
Tom has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8929365260632085)
Tom had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7170118721569225)
### Cindy
- mean: False (0.05834585230703704)
- motive: False (0.07835983919389444)
- opportunity: False (0.1871326586867097)

### Henry
- mean: True (0.9294404371753803)
- motive: True (0.9381240005131491)
- opportunity: True (0.8418256636710214)

### Leonard
- mean: False (0.09009301638875322)
- motive: False (0.10374867852692815)
- opportunity: False (0.2120688022445253)

### Tom
- mean: False (0.09401023594979185)
- motive: False (0.1070634739367915)
- opportunity: False (0.2829881278430775)

The culprit is Henry.
In fact, it is Cindy.
## 5minutemystery-did-the-vicar-solve-the-mystery
Elmer Tydings is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8464508054137014)
Elmer Tydings has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8955226517597132)
Elmer Tydings has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.892187358563457)
Elmer Tydings had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9049869164790318)
John Stubbs is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8338664134858856)
John Stubbs has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8267117710471246)
John Stubbs has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.847967740521315)
John Stubbs had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8591917766133458)
Katherine Tydings is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7905303264811482)
Katherine Tydings has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8333246107254184)
Map:  33%|███▎      | 68/203 [24:37<51:14, 22.78s/ examples]Map:  34%|███▍      | 69/203 [25:01<51:38, 23.12s/ examples]Katherine Tydings has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8601343603168419)
Katherine Tydings had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8820219652716884)
Louise Stubbs is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.884439109617765)
Louise Stubbs has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8244619332958376)
Louise Stubbs has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8606036289596553)
Louise Stubbs had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8723473540228537)
### Elmer Tydings
- mean: True (0.8955226517597132)
- motive: True (0.892187358563457)
- opportunity: True (0.9049869164790318)

### John Stubbs
- mean: False (0.17328822895287543)
- motive: False (0.15203225947868504)
- opportunity: False (0.14080822338665422)

### Katherine Tydings
- mean: False (0.1666753892745816)
- motive: False (0.13986563968315813)
- opportunity: False (0.11797803472831159)

### Louise Stubbs
- mean: False (0.1755380667041624)
- motive: False (0.13939637104034475)
- opportunity: False (0.12765264597714632)

The culprit is Elmer Tydings.
In fact, it is Katherine Tydings.
## 5minutemystery-who-scratched-the-porsche
Colonel Greenerbaum is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7866228249849953)
Colonel Greenerbaum has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9230391416137353)
Colonel Greenerbaum has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9381240005131491)
Colonel Greenerbaum had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8895288719962232)
Fido is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.794384956668203)
Fido has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.887204644943339)
Fido has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9291837815043049)
Fido had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8783141983077656)
Malcolm is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7606506318580792)
Malcolm has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8553685501761973)
Malcolm has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9043130884593419)
Malcolm had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7662936378892937)
Roxie is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7994423454932595)
Roxie has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8987665204865408)
Roxie has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9319595674053855)
Roxie had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8539127714046447)
### Colonel Greenerbaum
- mean: True (0.9230391416137353)
- motive: True (0.9381240005131491)
- opportunity: True (0.8895288719962232)

### Fido
- mean: False (0.11279535505666105)
- motive: False (0.07081621849569508)
- opportunity: False (0.12168580169223442)

### Malcolm
- mean: False (0.14463144982380272)
- motive: False (0.09568691154065811)
- opportunity: False (0.23370636211070628)

### Roxie
- mean: False (0.10123347951345918)
- motive: False (0.06804043259461445)
- opportunity: False (0.14608722859535528)

The culprit is Colonel Greenerbaum.
In fact, it is Colonel Greenerbaum.
## 5minutemystery-the-thief-in-the-night-mystery
Jon Shaw is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6654105788791005)
Jon Shaw has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8244619332958376)
Jon Shaw has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6992543888266708)
Jon Shaw had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6531268925247615)
Max Reinke is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6992544513448877)
Max Reinke has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9127477403975288)
Max Reinke has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.72951977676791)
Max Reinke had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6688802232837365)
Todd Summers is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6774740084332073)
Todd Summers has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9309620852900756)
Todd Summers has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7786492592534148)
Todd Summers had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6206216296838327)
Zac Coulson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7969253675907205)
Zac Coulson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9086179121100144)
Map:  34%|███▍      | 70/203 [25:21<49:19, 22.25s/ examples]Map:  35%|███▍      | 71/203 [25:41<47:08, 21.43s/ examples]Zac Coulson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7994423454932595)
Zac Coulson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.720171518230031)
### Jon Shaw
- mean: False (0.1755380667041624)
- motive: False (0.3007456111733292)
- opportunity: False (0.3468731074752385)

### Max Reinke
- mean: False (0.08725225960247118)
- motive: False (0.27048022323209)
- opportunity: False (0.33111977671626347)

### Todd Summers
- mean: False (0.06903791470992438)
- motive: False (0.22135074074658523)
- opportunity: False (0.3793783703161673)

### Zac Coulson
- mean: True (0.9086179121100144)
- motive: True (0.7994423454932595)
- opportunity: True (0.720171518230031)

The culprit is Zac Coulson.
In fact, it is Zac Coulson.
## 5minutemystery-ladies-at-table
Alice is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.873646672673131)
Alice has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9487276064711105)
Alice has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8169911556077801)
Alice had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8068526417769779)
Frances is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8278281666221954)
Frances has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.844921525814193)
Frances has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7620701143808404)
Frances had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7892336789711022)
Leona is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.858244061606496)
Leona has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8976952440346371)
Leona has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7772998201448375)
Leona had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7826625131049049)
Mary is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.803173839733582)
Mary has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8933094122075369)
Mary has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7409249009267298)
Mary had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7918210572836727)
Ruth is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7732163648437078)
Ruth has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8933094122075369)
Ruth has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7534666630720156)
Ruth had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8376199551237796)
### Alice
- mean: True (0.9487276064711105)
- motive: True (0.8169911556077801)
- opportunity: True (0.8068526417769779)

### Frances
- mean: False (0.155078474185807)
- motive: False (0.23792988561915962)
- opportunity: False (0.2107663210288978)

### Leona
- mean: False (0.10230475596536293)
- motive: False (0.22270017985516255)
- opportunity: False (0.21733748689509513)

### Mary
- mean: False (0.1066905877924631)
- motive: False (0.2590750990732702)
- opportunity: False (0.2081789427163273)

### Ruth
- mean: False (0.1066905877924631)
- motive: False (0.2465333369279844)
- opportunity: False (0.16238004487622038)

The culprit is Alice.
In fact, it is Leona.
## 5minutemystery-the-diamond-necklace
Abby Grant is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7556369876990674)
Abby Grant has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9219218506394821)
Abby Grant has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7049732238008671)
Abby Grant had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8134608241927087)
Colonel Barrow is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6984322578436808)
Colonel Barrow has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9539661392900927)
Colonel Barrow has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7648916137833577)
Colonel Barrow had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9127477403975288)
Fiona Duncan is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
False (4.623004603616179)
Fiona Duncan has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
False (3.399789497444135)
Fiona Duncan has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6288633913849659)
Fiona Duncan had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
False (1.6828751000675346)
Harold Duncan is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7248702601920561)
Harold Duncan has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9398029451247769)
Map:  35%|███▌      | 72/203 [26:05<48:29, 22.21s/ examples]Map:  36%|███▌      | 73/203 [26:24<45:59, 21.22s/ examples]Harold Duncan has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7248702601920561)
Harold Duncan had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8278281666221954)
Maurice Eades is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.802555560073231)
Maurice Eades has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.948346199423113)
Maurice Eades has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7225270177274575)
Maurice Eades had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8037905715242155)
### Abby Grant
- mean: False (0.07807814936051793)
- motive: False (0.29502677619913287)
- opportunity: False (0.1865391758072913)

### Colonel Barrow
- mean: True (0.9539661392900927)
- motive: True (0.7648916137833577)
- opportunity: True (0.9127477403975288)

### Fiona Duncan
- mean: False (3.399789497444135)
- motive: False (0.37113660861503406)
- opportunity: False (1.6828751000675346)

### Harold Duncan
- mean: False (0.06019705487522309)
- motive: False (0.27512973980794386)
- opportunity: False (0.17217183337780462)

### Maurice Eades
- mean: False (0.051653800576886955)
- motive: False (0.27747298227254247)
- opportunity: False (0.1962094284757845)

The culprit is Colonel Barrow.
In fact, it is Fiona Duncan.
## 5minutemystery-rhyming-presidents-mystery
George Bush is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6352224318508648)
George Bush has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8563323578093363)
George Bush has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7318258918270596)
George Bush had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7122321792841629)
Gerald Ford is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6671476985798853)
Gerald Ford has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7819972591886313)
Gerald Ford has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7090191197769757)
Gerald Ford had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7310585348819939)
John Quincy Adams is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7356416476869558)
John Quincy Adams has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7924642605907138)
John Quincy Adams has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7739006258141444)
John Quincy Adams had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7885831565209055)
Richard Nixon is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7627776774954688)
Richard Nixon has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8856314413364714)
Richard Nixon has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8238958672039278)
Richard Nixon had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7911764307711107)
### George Bush
- mean: False (0.14366764219066375)
- motive: False (0.2681741081729404)
- opportunity: False (0.28776782071583706)

### Gerald Ford
- mean: False (0.21800274081136872)
- motive: False (0.29098088022302426)
- opportunity: False (0.2689414651180061)

### John Quincy Adams
- mean: False (0.20753573940928616)
- motive: False (0.22609937418585557)
- opportunity: False (0.2114168434790945)

### Richard Nixon
- mean: True (0.8856314413364714)
- motive: True (0.8238958672039278)
- opportunity: True (0.7911764307711107)

The culprit is Richard Nixon.
In fact, it is Gerald Ford.
## 5minutemystery-the-white-house-ghosts
Andrew Jackson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9317114347547434)
Andrew Jackson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9609516854153933)
Andrew Jackson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8962513815714083)
Andrew Jackson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8615382357584752)
Calvin Coolidge is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9260365949489886)
Calvin Coolidge has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9537943000694998)
Calvin Coolidge has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8652240590801695)
Calvin Coolidge had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.821044090050916)
John Adams is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.920217993899809)
John Adams has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9252299659402181)
John Adams has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8872045854516336)
John Adams had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8624675215861032)
William Howard Taft is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9012274173198201)
Map:  36%|███▋      | 74/203 [26:48<47:45, 22.21s/ examples]Map:  37%|███▋      | 75/203 [27:13<48:39, 22.81s/ examples]William Howard Taft has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9199306971612747)
William Howard Taft has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8757869551856522)
William Howard Taft had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.811078188867804)
### Andrew Jackson
- mean: True (0.9609516854153933)
- motive: True (0.8962513815714083)
- opportunity: True (0.8615382357584752)

### Calvin Coolidge
- mean: False (0.046205699930500166)
- motive: False (0.13477594091983047)
- opportunity: False (0.17895590994908395)

### John Adams
- mean: False (0.07477003405978189)
- motive: False (0.11279541454836639)
- opportunity: False (0.13753247841389682)

### William Howard Taft
- mean: False (0.08006930283872526)
- motive: False (0.1242130448143478)
- opportunity: False (0.18892181113219597)

The culprit is Andrew Jackson.
In fact, it is Calvin Coolidge.
## 5minutemystery-mr-patrick-and-the-graveyard-mystery
Grave no.1 is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9069831945855868)
Grave no.1 has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.884439109617765)
Grave no.1 has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8407825844829613)
Grave no.1 had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8438950825214144)
Grave no.2 is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9069831945855868)
Grave no.2 has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8563323578093363)
Grave no.2 has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8402590129647053)
Grave no.2 had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8244619332958376)
Grave no.3 is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9019206778000431)
Grave no.3 has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8563324216110711)
Grave no.3 has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8563323578093363)
Grave no.3 had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8204694405411458)
Grave no.4 is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8987665204865408)
Grave no.4 has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8553685501761973)
Grave no.4 has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8250265073476026)
Grave no.4 had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8349459127213729)
Grave no.5 is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9012274173198201)
Grave no.5 has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8469578019965)
Grave no.5 has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8365545251239088)
Grave no.5 had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8283841584202847)
### Grave no.1
- mean: True (0.884439109617765)
- motive: True (0.8407825844829613)
- opportunity: True (0.8438950825214144)

### Grave no.2
- mean: False (0.14366764219066375)
- motive: False (0.1597409870352947)
- opportunity: False (0.1755380667041624)

### Grave no.3
- mean: False (0.14366757838892885)
- motive: False (0.14366764219066375)
- opportunity: False (0.1795305594588542)

### Grave no.4
- mean: False (0.14463144982380272)
- motive: False (0.17497349265239737)
- opportunity: False (0.16505408727862714)

### Grave no.5
- mean: False (0.15304219800350005)
- motive: False (0.16344547487609118)
- opportunity: False (0.17161584157971532)

The culprit is Grave no.1.
In fact, it is Grave no.4.
## 5minutemystery-lockbox-100
Edward Frates is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
False (0.7025300310583819)
Edward Frates has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.550607385906944)
Edward Frates has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
False (0.5583269696343842)
Edward Frates had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
False (0.5794004215835179)
James Madigan is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
False (0.7025300310583819)
James Madigan has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.6697448487720212)
James Madigan has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
False (0.5774954003013352)
James Madigan had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
False (0.5331544304756466)
Peter Zielny is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
False (0.6680145838067516)
Peter Zielny has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8006920257960423)
Peter Zielny has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.646013666311734)
Peter Zielny had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6132365353114321)
Map:  37%|███▋      | 76/203 [27:35<47:51, 22.61s/ examples]Map:  38%|███▊      | 77/203 [28:02<50:42, 24.15s/ examples]Ronald Finch is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
False (0.5195213440667139)
Ronald Finch has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8006919661398397)
Ronald Finch has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7122322217365102)
Ronald Finch had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6020615685826383)
Russell Winwood is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
False (0.5273165068094335)
Russell Winwood has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.811078188867804)
Russell Winwood has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6297746298200823)
Russell Winwood had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5698526542706361)
### Edward Frates
- mean: False (0.449392614093056)
- motive: False (0.5583269696343842)
- opportunity: False (0.5794004215835179)

### James Madigan
- mean: False (0.33025515122797877)
- motive: False (0.5774954003013352)
- opportunity: False (0.5331544304756466)

### Peter Zielny
- mean: False (0.19930797420395774)
- motive: False (0.35398633368826604)
- opportunity: False (0.3867634646885679)

### Ronald Finch
- mean: True (0.8006919661398397)
- motive: True (0.7122322217365102)
- opportunity: True (0.6020615685826383)

### Russell Winwood
- mean: False (0.18892181113219597)
- motive: False (0.37022537017991775)
- opportunity: False (0.43014734572936386)

The culprit is Ronald Finch.
In fact, it is Russell Winwood.
## 5minutemystery-mystery-at-the-detectives-office
Joe the janitor is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8175744430556572)
Joe the janitor has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8558511727823209)
Joe the janitor has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9284088027271398)
Joe the janitor had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8322366416985943)
Larry is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6688802830862913)
Larry has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8633915828320894)
Larry has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8918110138739693)
Larry had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6859494535376744)
Mr. Jorgensen is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7592254214399092)
Mr. Jorgensen has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8679338697256817)
Mr. Jorgensen has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8824278665848695)
Mr. Jorgensen had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6671476389322356)
the building manager is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6388352560545881)
the building manager has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.854884620116169)
the building manager has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8705972382426559)
the building manager had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7233094544266295)
### Joe the janitor
- mean: True (0.8558511727823209)
- motive: True (0.9284088027271398)
- opportunity: True (0.8322366416985943)

### Larry
- mean: False (0.1366084171679106)
- motive: False (0.10818898612603067)
- opportunity: False (0.31405054646232555)

### Mr. Jorgensen
- mean: False (0.13206613027431835)
- motive: False (0.11757213341513051)
- opportunity: False (0.3328523610677644)

### the building manager
- mean: False (0.14511537988383105)
- motive: False (0.1294027617573441)
- opportunity: False (0.27669054557337047)

The culprit is Joe the janitor.
In fact, it is the building manager.
## 5minutemystery-the-secret-in-the-old-trunk
Dennis Boyles is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8370879874240941)
Dennis Boyles has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9456006903352807)
Dennis Boyles has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8418256636710214)
Dennis Boyles had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8037906314112822)
George Boyles is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8006920257960423)
George Boyles has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8944211616820568)
George Boyles has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8255897087847518)
George Boyles had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7217431689117048)
John Boyles is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8267117710471246)
John Boyles has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9158089188126235)
John Boyles has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8233283740192667)
Map:  38%|███▊      | 78/203 [28:29<51:41, 24.81s/ examples]Map:  39%|███▉      | 79/203 [28:56<52:59, 25.64s/ examples]John Boyles had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7409249009267298)
Patricia (Trish) Boyles Sykes is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8261514850267767)
Patricia (Trish) Boyles Sykes has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9291838438109349)
Patricia (Trish) Boyles Sykes has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7279754274224494)
Patricia (Trish) Boyles Sykes had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6723316913929156)
Patrick Boyles is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7627776774954688)
Patrick Boyles has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9249593046682986)
Patrick Boyles has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.821044090050916)
Patrick Boyles had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7302898714065358)
### Dennis Boyles
- mean: True (0.9456006903352807)
- motive: True (0.8418256636710214)
- opportunity: True (0.8037906314112822)

### George Boyles
- mean: False (0.10557883831794324)
- motive: False (0.1744102912152482)
- opportunity: False (0.27825683108829524)

### John Boyles
- mean: False (0.0841910811873765)
- motive: False (0.17667162598073327)
- opportunity: False (0.2590750990732702)

### Patricia (Trish) Boyles Sykes
- mean: False (0.07081615618906512)
- motive: False (0.27202457257755064)
- opportunity: False (0.3276683086070844)

### Patrick Boyles
- mean: False (0.07504069533170143)
- motive: False (0.17895590994908395)
- opportunity: False (0.2697101285934642)

The culprit is Dennis Boyles.
In fact, it is Patrick Boyles.
## 5minutemystery-the-restless-ghost
Casey McCormick is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7534666630720156)
Casey McCormick has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9399133323582882)
Casey McCormick has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.821044090050916)
Casey McCormick had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8255897087847518)
Connie McCormick is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7431679939957333)
Connie McCormick has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9362849627883332)
Connie McCormick has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8152325155686644)
Connie McCormick had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8128672807499561)
Ellen McCormick is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6774740084332073)
Ellen McCormick has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9019206778000431)
Ellen McCormick has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7931059536445917)
Ellen McCormick had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7718434926244166)
Michael McCormick, Jr. is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6388353131709135)
Michael McCormick, Jr. has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8661325012437474)
Michael McCormick, Jr. has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.821044090050916)
Michael McCormick, Jr. had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7759445334082792)
The ghost of Mike McCormick, Sr. is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6169358476670045)
The ghost of Mike McCormick, Sr. has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8596637847360897)
The ghost of Mike McCormick, Sr. has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7154239360853772)
The ghost of Mike McCormick, Sr. had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8104789202520752)
### Casey McCormick
- mean: True (0.9399133323582882)
- motive: True (0.821044090050916)
- opportunity: True (0.8255897087847518)

### Connie McCormick
- mean: False (0.06371503721166683)
- motive: False (0.18476748443133562)
- opportunity: False (0.18713271925004393)

### Ellen McCormick
- mean: False (0.09807932219995685)
- motive: False (0.2068940463554083)
- opportunity: False (0.22815650737558335)

### Michael McCormick, Jr.
- mean: False (0.1338674987562526)
- motive: False (0.17895590994908395)
- opportunity: False (0.22405546659172082)

### The ghost of Mike McCormick, Sr.
- mean: False (0.14033621526391027)
- motive: False (0.28457606391462276)
- opportunity: False (0.18952107974792476)

The culprit is Casey McCormick.
In fact, it is Casey McCormick.
## 5minutemystery-the-secret-friend
Bill Baker is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7364006034245382)
Bill Baker has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8832359917473193)
Bill Baker has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7866228249849953)
Bill Baker had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7994422859301654)
Map:  39%|███▉      | 80/203 [29:14<47:32, 23.19s/ examples]Map:  40%|███▉      | 81/203 [29:39<48:21, 23.78s/ examples]Harold Coker is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8643105035965187)
Harold Coker has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9210740952879496)
Harold Coker has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8044059309478723)
Harold Coker had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8624675215861032)
Lyn Baker is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8267117710471246)
Lyn Baker has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9187722208906307)
Lyn Baker has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8509647293237851)
Lyn Baker had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8940517282497483)
Midge Coker is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8392075331266983)
Midge Coker has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9241418261705818)
Midge Coker has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.789233749534095)
Midge Coker had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8705972382426559)
### Bill Baker
- mean: False (0.11676400825268074)
- motive: False (0.21337717501500475)
- opportunity: False (0.20055771406983458)

### Harold Coker
- mean: False (0.07892590471205041)
- motive: False (0.19559406905212773)
- opportunity: False (0.13753247841389682)

### Lyn Baker
- mean: True (0.9187722208906307)
- motive: True (0.8509647293237851)
- opportunity: True (0.8940517282497483)

### Midge Coker
- mean: False (0.07585817382941817)
- motive: False (0.21076625046590503)
- opportunity: False (0.1294027617573441)

The culprit is Lyn Baker.
In fact, it is Midge Coker.
## 5minutemystery-the-cross-homestead-mystery
Journal entry of Edith is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7866228249849953)
Journal entry of Edith has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9019206778000431)
Journal entry of Edith has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8386797310322072)
Journal entry of Edith had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6057990946577705)
Journal entry of Leonard is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7918210572836727)
Journal entry of Leonard has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.879146813094474)
Journal entry of Leonard has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7592253761865491)
Journal entry of Leonard had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7577943897558946)
Journal entry of Susie is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8233283740192667)
Journal entry of Susie has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.878314250659373)
Journal entry of Susie has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7786492592534148)
Journal entry of Susie had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.591723272524637)
Journal entry of Victor is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8300437258865985)
Journal entry of Victor has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8864204283224634)
Journal entry of Victor has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7772998201448375)
Journal entry of Victor had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6566582306092376)
Journal entry of Wilbur is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8152325155686644)
Journal entry of Wilbur has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9099069836112468)
Journal entry of Wilbur has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8568122940392877)
Journal entry of Wilbur had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8116760258690822)
### Journal entry of Edith
- mean: False (0.09807932219995685)
- motive: False (0.16132026896779283)
- opportunity: False (0.3942009053422295)

### Journal entry of Leonard
- mean: False (0.12085318690552604)
- motive: False (0.24077462381345094)
- opportunity: False (0.24220561024410536)

### Journal entry of Susie
- mean: False (0.12168574934062704)
- motive: False (0.22135074074658523)
- opportunity: False (0.40827672747536303)

### Journal entry of Victor
- mean: False (0.11357957167753663)
- motive: False (0.22270017985516255)
- opportunity: False (0.34334176939076244)

### Journal entry of Wilbur
- mean: True (0.9099069836112468)
- motive: True (0.8568122940392877)
- opportunity: True (0.8116760258690822)

The culprit is Journal entry of Wilbur.
In fact, it is Journal entry of Leonard.
## 5minutemystery-is-it-a-wonderful-life
Dr. Gilchrest is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6757645563841816)
Dr. Gilchrest has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.779321849347754)
Map:  40%|████      | 82/203 [29:59<45:36, 22.62s/ examples]Map:  41%|████      | 83/203 [30:24<46:26, 23.22s/ examples]Dr. Gilchrest has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8824278139880716)
Dr. Gilchrest had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8244619332958376)
Jonathan Cartright is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.646013666311734)
Jonathan Cartright has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7937461674149602)
Jonathan Cartright has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8175745039697023)
Jonathan Cartright had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7839884808423031)
Miser James Cartright (suicide) is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6113820047705449)
Miser James Cartright (suicide) has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7279754274224494)
Miser James Cartright (suicide) has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7577943897558946)
Miser James Cartright (suicide) had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6671476985798853)
Moira Laurie is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7302898714065358)
Moira Laurie has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7613611200983542)
Moira Laurie has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8910549899564296)
Moira Laurie had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8305941261447712)
### Dr. Gilchrest
- mean: True (0.779321849347754)
- motive: True (0.8824278139880716)
- opportunity: True (0.8244619332958376)

### Jonathan Cartright
- mean: False (0.20625383258503982)
- motive: False (0.18242549603029767)
- opportunity: False (0.2160115191576969)

### Miser James Cartright (suicide)
- mean: False (0.27202457257755064)
- motive: False (0.24220561024410536)
- opportunity: False (0.3328523014201147)

### Moira Laurie
- mean: False (0.23863887990164578)
- motive: False (0.10894501004357038)
- opportunity: False (0.16940587385522876)

The culprit is Dr. Gilchrest.
In fact, it is Moira Laurie.
## 5minutemystery-lestrade-solves-a-case
Archibald Hopkins is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5698527222023703)
Archibald Hopkins has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8198933606225757)
Archibald Hopkins has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6740504382339836)
Archibald Hopkins had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.644225125126315)
Countess Mannerley is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5907791930117218)
Countess Mannerley has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8469578650997759)
Countess Mannerley has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7739006258141444)
Countess Mannerley had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.726425644352388)
Loralie Courtney is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
False (0.5370414382302919)
Loralie Courtney has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7170118721569225)
Loralie Courtney has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6566582306092376)
Loralie Courtney had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.615087855649269)
Robert Bannington is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6909762697651828)
Robert Bannington has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8688267468984366)
Robert Bannington has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8770562402180104)
Robert Bannington had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7759445334082792)
### Archibald Hopkins
- mean: False (0.18010663937742433)
- motive: False (0.3259495617660164)
- opportunity: False (0.355774874873685)

### Countess Mannerley
- mean: False (0.1530421349002241)
- motive: False (0.22609937418585557)
- opportunity: False (0.273574355647612)

### Loralie Courtney
- mean: False (0.2829881278430775)
- motive: False (0.34334176939076244)
- opportunity: False (0.38491214435073096)

### Robert Bannington
- mean: True (0.8688267468984366)
- motive: True (0.8770562402180104)
- opportunity: True (0.7759445334082792)

The culprit is Robert Bannington.
In fact, it is Robert Bannington.
## 5minutemystery-whole-stole-the-new-years-kiss
Danny is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8824278665848695)
Danny has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9713473322135262)
Danny has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9294404371753803)
Danny had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9353465445225602)
Jeremy is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6757646168022439)
Map:  41%|████▏     | 84/203 [30:40<42:03, 21.21s/ examples]Map:  42%|████▏     | 85/203 [31:02<42:12, 21.46s/ examples]Jeremy has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9513234509300917)
Jeremy has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8092759828926619)
Jeremy had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8914335992201801)
RJ is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8233284353620131)
RJ has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9828891164753333)
RJ has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9268353022276509)
RJ had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9268353022276509)
Reese is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8444089912414552)
Reese has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9774570469332207)
Reese has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9324533354081785)
Reese had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9173026661190045)
### Danny
- mean: False (0.028652667786473796)
- motive: False (0.07055956282461973)
- opportunity: False (0.06465345547743984)

### Jeremy
- mean: False (0.04867654906990826)
- motive: False (0.1907240171073381)
- opportunity: False (0.10856640077981994)

### RJ
- mean: True (0.9828891164753333)
- motive: True (0.9268353022276509)
- opportunity: True (0.9268353022276509)

### Reese
- mean: False (0.022542953066779337)
- motive: False (0.06754666459182146)
- opportunity: False (0.08269733388099554)

The culprit is RJ.
In fact, it is RJ.
## 5minutemystery-the-new-years-eve-mystery
Juanita Wade is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8272706865691472)
Juanita Wade has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9408984174410038)
Juanita Wade has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8311430831606665)
Juanita Wade had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8474634858439474)
Mary Beth Sloan is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8624675215861032)
Mary Beth Sloan has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9689738169140454)
Mary Beth Sloan has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9149009617112335)
Mary Beth Sloan had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9567959302164903)
Noel King is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8221890958162477)
Noel King has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9388007508488514)
Noel King has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8365545874520802)
Noel King had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9029524325377104)
Roy Wade is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7711548682745724)
Roy Wade has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9546474221708894)
Roy Wade has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8723474190177988)
Roy Wade had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8740772044235984)
Theresa King is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8193157928301305)
Theresa King has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9299510719523877)
Theresa King has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9039744767757508)
Theresa King had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.934872446722342)
### Juanita Wade
- mean: False (0.059101582558996224)
- motive: False (0.16885691683933346)
- opportunity: False (0.15253651415605263)

### Mary Beth Sloan
- mean: True (0.9689738169140454)
- motive: True (0.9149009617112335)
- opportunity: True (0.9567959302164903)

### Noel King
- mean: False (0.061199249151148605)
- motive: False (0.16344541254791978)
- opportunity: False (0.0970475674622896)

### Roy Wade
- mean: False (0.04535257782911062)
- motive: False (0.12765258098220122)
- opportunity: False (0.12592279557640162)

### Theresa King
- mean: False (0.07004892804761231)
- motive: False (0.09602552322424918)
- opportunity: False (0.06512755327765796)

The culprit is Mary Beth Sloan.
In fact, it is Mary Beth Sloan.
## 5minutemystery-the-twelfth-night-mystery
Balthasar is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8958876133958744)
Balthasar has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8925625120974553)
Balthasar has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8757869551856522)
Balthasar had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8705973031072073)
Caspar is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7911763836133219)
Map:  42%|████▏     | 86/203 [31:20<39:38, 20.33s/ examples]Map:  43%|████▎     | 87/203 [31:41<40:02, 20.71s/ examples]Caspar has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8134607635851566)
Caspar has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7826625131049049)
Caspar had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7732163648437078)
Dad is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8558511727823209)
Dad has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9329437018480795)
Dad has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8509647293237851)
Dad had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8740772565226612)
Melchoir is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.893681109060862)
Melchoir has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.95498442695849)
Melchoir has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9133679254389228)
Melchoir had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9015746123467522)
### Balthasar
- mean: False (0.1074374879025447)
- motive: False (0.1242130448143478)
- opportunity: False (0.1294026968927927)

### Caspar
- mean: False (0.18653923641484338)
- motive: False (0.21733748689509513)
- opportunity: False (0.22678363515629218)

### Dad
- mean: False (0.06705629815192049)
- motive: False (0.14903527067621491)
- opportunity: False (0.12592274347733878)

### Melchoir
- mean: True (0.95498442695849)
- motive: True (0.9133679254389228)
- opportunity: True (0.9015746123467522)

The culprit is Melchoir.
In fact, it is Caspar.
## 5minutemystery-sugar-lands-candy-crook
King Ted is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.832781310996106)
King Ted has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9082930704920021)
King Ted has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9222025272167219)
King Ted had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8951566249612815)
Lancelot is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8181563669811865)
Lancelot has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8933094122075369)
Lancelot has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9158089188126235)
Lancelot had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8615382357584752)
Pride is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8723474190177988)
Pride has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.91789335161495)
Pride has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9383503780077049)
Pride had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8929365260632085)
Rupert is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8169911556077801)
Rupert has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9015746123467522)
Rupert has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9244151684978138)
Rupert had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8688267468984366)
### King Ted
- mean: False (0.09170692950799786)
- motive: False (0.07779747278327809)
- opportunity: False (0.10484337503871854)

### Lancelot
- mean: False (0.1066905877924631)
- motive: False (0.0841910811873765)
- opportunity: False (0.1384617642415248)

### Pride
- mean: True (0.91789335161495)
- motive: True (0.9383503780077049)
- opportunity: True (0.8929365260632085)

### Rupert
- mean: False (0.09842538765324782)
- motive: False (0.0755848315021862)
- opportunity: False (0.13117325310156336)

The culprit is Pride.
In fact, it is King Ted.
## 5minutemystery-what-the-dickensa-christmas-eve-mystery
Fagin is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7839884808423031)
Fagin has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8740772044235984)
Fagin has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
False (0.4034737958917728)
Fagin had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6601723415572317)
Nancy is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7154240000492645)
Nancy has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8407825844829613)
Nancy has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8128673413132903)
Nancy had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7386690294153369)
Oliver Twist is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7606506998655483)
Oliver Twist has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9092645024391882)
Map:  43%|████▎     | 88/203 [32:11<44:37, 23.29s/ examples]Map:  44%|████▍     | 89/203 [32:44<50:06, 26.37s/ examples]Oliver Twist has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8074605993751186)
Oliver Twist had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7732163648437078)
The Artful Dodger is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6825737331070684)
The Artful Dodger has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.920217993899809)
The Artful Dodger has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8140527631337082)
The Artful Dodger had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7106283339569771)
The Rich Gentleman is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7799928701983835)
The Rich Gentleman has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.905989824801558)
The Rich Gentleman has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8514594452543962)
The Rich Gentleman had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6876299924560524)
### Fagin
- mean: False (0.12592279557640162)
- motive: False (0.4034737958917728)
- opportunity: False (0.3398276584427683)

### Nancy
- mean: False (0.15921741551703872)
- motive: False (0.1871326586867097)
- opportunity: False (0.26133097058466315)

### Oliver Twist
- mean: True (0.9092645024391882)
- motive: True (0.8074605993751186)
- opportunity: True (0.7732163648437078)

### The Artful Dodger
- mean: False (0.07978200610019104)
- motive: False (0.18594723686629178)
- opportunity: False (0.2893716660430229)

### The Rich Gentleman
- mean: False (0.09401017519844201)
- motive: False (0.1485405547456038)
- opportunity: False (0.3123700075439476)

The culprit is Oliver Twist.
In fact, it is The Rich Gentleman.
## 5minutemystery-the-secret-santa-mystery
Al Busby is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5926665645259142)
Al Busby has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8553685501761973)
Al Busby has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7170118721569225)
Al Busby had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8255897087847518)
Bob (Bobby) Key is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5983121871760707)
Bob (Bobby) Key has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8891444205417208)
Bob (Bobby) Key has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8175745039697023)
Bob (Bobby) Key had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8962513214730718)
Chuck Daughtry is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6654105788791005)
Chuck Daughtry has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9086179121100144)
Chuck Daughtry has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8615382357584752)
Chuck Daughtry had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8940517282497483)
Jeff Reynolds is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6279512069990912)
Jeff Reynolds has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8824278665848695)
Jeff Reynolds has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8300437258865985)
Jeff Reynolds had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8267117710471246)
Jim Dockery is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6334102859975052)
Jim Dockery has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.879146760693242)
Jim Dockery has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7476159279883341)
Jim Dockery had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7745833916423246)
### Al Busby
- mean: False (0.14463144982380272)
- motive: False (0.2829881278430775)
- opportunity: False (0.1744102912152482)

### Bob (Bobby) Key
- mean: False (0.11085557945827917)
- motive: False (0.18242549603029767)
- opportunity: False (0.10374867852692815)

### Chuck Daughtry
- mean: True (0.9086179121100144)
- motive: True (0.8615382357584752)
- opportunity: True (0.8940517282497483)

### Jeff Reynolds
- mean: False (0.11757213341513051)
- motive: False (0.16995627411340153)
- opportunity: False (0.17328822895287543)

### Jim Dockery
- mean: False (0.12085323930675795)
- motive: False (0.2523840720116659)
- opportunity: False (0.2254166083576754)

The culprit is Chuck Daughtry.
In fact, it is Jim Dockery.
## 5minutemystery-the-silly-santa-mystery
Mr. Corrigan is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7648916137833577)
Mr. Corrigan has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.867485409735739)
Mr. Corrigan has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7950222460539826)
Mr. Corrigan had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8062431235779619)
Map:  44%|████▍     | 90/203 [33:11<50:04, 26.59s/ examples]Map:  45%|████▍     | 91/203 [33:34<47:33, 25.48s/ examples]Mrs. Martin is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.811078188867804)
Mrs. Martin has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.874934615163517)
Mrs. Martin has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8489722037469682)
Mrs. Martin had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8056321690561029)
Santa Claus is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6859494535376744)
Santa Claus has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.861071588244826)
Santa Claus has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8193157928301305)
Santa Claus had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7570766705324253)
The photographer is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7082125449089324)
The photographer has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8181563669811865)
The photographer has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7872777015429719)
The photographer had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6893056507505698)
### Mr. Corrigan
- mean: False (0.13251459026426105)
- motive: False (0.20497775394601736)
- opportunity: False (0.1937568764220381)

### Mrs. Martin
- mean: True (0.874934615163517)
- motive: True (0.8489722037469682)
- opportunity: True (0.8056321690561029)

### Santa Claus
- mean: False (0.138928411755174)
- motive: False (0.18068420716986955)
- opportunity: False (0.24292332946757467)

### The photographer
- mean: False (0.18184363301881346)
- motive: False (0.21272229845702806)
- opportunity: False (0.3106943492494302)

The culprit is Mrs. Martin.
In fact, it is The photographer.
## 5minutemystery-sky-jack
Clem Duster is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8019357965963964)
Clem Duster has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9299510719523877)
Clem Duster has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9005298052062833)
Clem Duster had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7839884808423031)
Cliff Snelling is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.816406362162552)
Cliff Snelling has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.905989824801558)
Cliff Snelling has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8816148581338575)
Cliff Snelling had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7476159279883341)
David Loftkiss is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8080671968507699)
David Loftkiss has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9026095892260383)
David Loftkiss has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8991214023999228)
David Loftkiss had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7386690954574974)
Tom Jenks is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7813306496768853)
Tom Jenks has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9294404371753803)
Tom Jenks has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8766344170435998)
Tom Jenks had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7981867775042927)
### Clem Duster
- mean: True (0.9299510719523877)
- motive: True (0.9005298052062833)
- opportunity: True (0.7839884808423031)

### Cliff Snelling
- mean: False (0.09401017519844201)
- motive: False (0.11838514186614246)
- opportunity: False (0.2523840720116659)

### David Loftkiss
- mean: False (0.09739041077396171)
- motive: False (0.10087859760007722)
- opportunity: False (0.26133090454250263)

### Tom Jenks
- mean: False (0.07055956282461973)
- motive: False (0.12336558295640021)
- opportunity: False (0.20181322249570732)

The culprit is Clem Duster.
In fact, it is Tom Jenks.
## 5minutemystery-dr-watson-and-the-thwarted-engagement
Georgette Pelham is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5370413742099674)
Georgette Pelham has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.6495786332146115)
Georgette Pelham has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7122321792841629)
Georgette Pelham had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6169358476670045)
Reverend Marvin Ingalls is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.64779823427608)
Reverend Marvin Ingalls has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8233283740192667)
Reverend Marvin Ingalls has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7704647687904915)
Map:  45%|████▌     | 92/203 [33:54<44:08, 23.86s/ examples]Map:  46%|████▌     | 93/203 [34:16<42:26, 23.15s/ examples]Reverend Marvin Ingalls had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5370413742099674)
Sheila Ingalls is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6671476389322356)
Sheila Ingalls has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8092759225969047)
Sheila Ingalls has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7826625131049049)
Sheila Ingalls had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6723316913929156)
Wallace Anders is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6723316913929156)
Wallace Anders has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.770464837675413)
Wallace Anders has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7386690294153369)
Wallace Anders had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6001883144765984)
### Georgette Pelham
- mean: False (0.3504213667853885)
- motive: False (0.28776782071583706)
- opportunity: False (0.3830641523329955)

### Reverend Marvin Ingalls
- mean: False (0.17667162598073327)
- motive: False (0.22953523120950847)
- opportunity: False (0.46295862579003255)

### Sheila Ingalls
- mean: True (0.8092759225969047)
- motive: True (0.7826625131049049)
- opportunity: True (0.6723316913929156)

### Wallace Anders
- mean: False (0.22953516232458704)
- motive: False (0.26133097058466315)
- opportunity: False (0.3998116855234016)

The culprit is Sheila Ingalls.
In fact, it is Wallace Anders.
## 5minutemystery-shoot-out-at-splithead-canyon
Big George Ratcliffe is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7512834059294674)
Big George Ratcliffe has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8940516749601143)
Big George Ratcliffe has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7956580548514487)
Big George Ratcliffe had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7090191197769757)
Chester Morris is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7520125537161032)
Chester Morris has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.916109562167414)
Chester Morris has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8438950825214144)
Chester Morris had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7690802105138688)
Joe Franklin is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6791787167336184)
Joe Franklin has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8740772565226612)
Joe Franklin has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8092759828926619)
Joe Franklin had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6825737331070684)
Slim Jameson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7074046739492601)
Slim Jameson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8529354946829077)
Slim Jameson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7732163648437078)
Slim Jameson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6261241441180464)
### Big George Ratcliffe
- mean: False (0.10594832503988572)
- motive: False (0.2043419451485513)
- opportunity: False (0.29098088022302426)

### Chester Morris
- mean: True (0.916109562167414)
- motive: True (0.8438950825214144)
- opportunity: True (0.7690802105138688)

### Joe Franklin
- mean: False (0.12592274347733878)
- motive: False (0.1907240171073381)
- opportunity: False (0.31742626689293163)

### Slim Jameson
- mean: False (0.14706450531709225)
- motive: False (0.22678363515629218)
- opportunity: False (0.3738758558819536)

The culprit is Chester Morris.
In fact, it is Slim Jameson.
## 5minutemystery-the-mystery-of-the-american-raid
Admiral Taro is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7106283339569771)
Admiral Taro has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8489722037469682)
Admiral Taro has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8543993851297865)
Admiral Taro had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7859664553110391)
Gina is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6783269591477166)
Gina has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7563575572780217)
Gina has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8688267468984366)
Gina had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7634837587244478)
Kira is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6901415551283886)
Kira has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8181563669811865)
Map:  46%|████▋     | 94/203 [34:37<40:51, 22.49s/ examples]Map:  47%|████▋     | 95/203 [34:59<40:20, 22.41s/ examples]Kira has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8883720049821552)
Kira had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8140528237853677)
The Emperor is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.874934615163517)
The Emperor has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.929696145502287)
The Emperor has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.929696145502287)
The Emperor had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8464508054137014)
### Admiral Taro
- mean: False (0.15102779625303175)
- motive: False (0.14560061487021347)
- opportunity: False (0.21403354468896085)

### Gina
- mean: False (0.24364244272197833)
- motive: False (0.13117325310156336)
- opportunity: False (0.23651624127555215)

### Kira
- mean: False (0.18184363301881346)
- motive: False (0.11162799501784482)
- opportunity: False (0.1859471762146323)

### The Emperor
- mean: True (0.929696145502287)
- motive: True (0.929696145502287)
- opportunity: True (0.8464508054137014)

The culprit is The Emperor.
In fact, it is Admiral Taro.
## 5minutemystery-the-missing-ornament-mystery
Jackie Hadley is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8606036289596553)
Jackie Hadley has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9571177375286347)
Jackie Hadley has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9329437018480795)
Jackie Hadley had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8848377441095496)
Lennie Hadley is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.926967620306882)
Lennie Hadley has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9800530672366293)
Lennie Hadley has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9458012588547495)
Lennie Hadley had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9145963197706802)
Mike Hadley is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8895288719962232)
Mike Hadley has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9778833990684288)
Mike Hadley has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9475754509027036)
Mike Hadley had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.920217993899809)
Sandy Hadley is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8647679145346777)
Sandy Hadley has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9628131975124238)
Sandy Hadley has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9257686153543061)
Sandy Hadley had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9244152304846833)
Tommy Hadley is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8714749214913714)
Tommy Hadley has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9753900767342161)
Tommy Hadley has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9190633328333496)
Tommy Hadley had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8984105603938967)
### Jackie Hadley
- mean: False (0.042882262471365284)
- motive: False (0.06705629815192049)
- opportunity: False (0.11516225589045037)

### Lennie Hadley
- mean: False (0.019946932763370673)
- motive: False (0.05419874114525047)
- opportunity: False (0.08540368022931977)

### Mike Hadley
- mean: True (0.9778833990684288)
- motive: True (0.9475754509027036)
- opportunity: True (0.920217993899809)

### Sandy Hadley
- mean: False (0.03718680248757622)
- motive: False (0.0742313846456939)
- opportunity: False (0.07558476951531667)

### Tommy Hadley
- mean: False (0.02460992326578393)
- motive: False (0.08093666716665038)
- opportunity: False (0.10158943960610334)

The culprit is Mike Hadley.
In fact, it is Lennie Hadley.
## 5minutemystery-the-pilgrim-thanksgiving-puzzle
John Alden is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7745833916423246)
John Alden has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8519527857346616)
John Alden has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8056321690561029)
John Alden had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6740504382339836)
Miles Standish is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7988152492192591)
Miles Standish has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8745065930973813)
Miles Standish has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.743912876509037)
Miles Standish had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7090191831682278)
Priscilla Mulllins is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.779321849347754)
Map:  47%|████▋     | 96/203 [35:21<39:35, 22.20s/ examples]Map:  48%|████▊     | 97/203 [35:38<36:24, 20.61s/ examples]Priscilla Mulllins has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8828325273478573)
Priscilla Mulllins has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8433797899747144)
Priscilla Mulllins had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7279754274224494)
William Bradford is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7371581232960549)
William Bradford has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7931059536445917)
William Bradford has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7279754274224494)
William Bradford had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6315943123389512)
### John Alden
- mean: False (0.1480472142653384)
- motive: False (0.1943678309438971)
- opportunity: False (0.3259495617660164)

### Miles Standish
- mean: False (0.12549340690261868)
- motive: False (0.25608712349096296)
- opportunity: False (0.29098081683177224)

### Priscilla Mulllins
- mean: True (0.8828325273478573)
- motive: True (0.8433797899747144)
- opportunity: True (0.7279754274224494)

### William Bradford
- mean: False (0.2068940463554083)
- motive: False (0.27202457257755064)
- opportunity: False (0.36840568766104875)

The culprit is Priscilla Mulllins.
In fact, it is John Alden.
## 5minutemystery-the-disappearing-turkey
Darby is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6388352560545881)
Darby has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8392075331266983)
Darby has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7256486384635821)
Darby had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7577943220037995)
Father is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5794004215835179)
Father has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8697146199790504)
Father has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.784649255215384)
Father had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7725306828324007)
Greg is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6808786440630326)
Greg has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8807970862580315)
Greg has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8438950825214144)
Greg had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7248702601920561)
Uncle Larry is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.72951977676791)
Uncle Larry has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9522199623739209)
Uncle Larry has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.854884620116169)
Uncle Larry had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8519527857346616)
### Darby
- mean: False (0.16079246687330173)
- motive: False (0.2743513615364179)
- opportunity: False (0.24220567799620052)

### Father
- mean: False (0.13028538002094958)
- motive: False (0.21535074478461602)
- opportunity: False (0.22746931716759933)

### Greg
- mean: False (0.11920291374196845)
- motive: False (0.15610491747858557)
- opportunity: False (0.27512973980794386)

### Uncle Larry
- mean: True (0.9522199623739209)
- motive: True (0.854884620116169)
- opportunity: True (0.8519527857346616)

The culprit is Uncle Larry.
In fact, it is Father.
## 5minutemystery-a-thanksgiving-mystery-poem
Libby is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9114953293645017)
Libby has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9244152304846833)
Libby has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9233161821369215)
Libby had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.903294268691502)
Rusty is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9291837815043049)
Rusty has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9443823686645129)
Rusty has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9509603994010378)
Rusty had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9161096235973493)
Tiny is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.952041865762172)
Tiny has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9473810811508532)
Tiny has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9605096001181298)
Tiny had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.936749461409047)
Tom is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9142907234091052)
Map:  48%|████▊     | 98/203 [35:56<34:36, 19.78s/ examples]Map:  49%|████▉     | 99/203 [36:15<33:59, 19.61s/ examples]Tom has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9187722208906307)
Tom has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9355823382423648)
Tom had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8899121304559661)
### Libby
- mean: False (0.07558476951531667)
- motive: False (0.07668381786307854)
- opportunity: False (0.09670573130849802)

### Rusty
- mean: False (0.05561763133548714)
- motive: False (0.049039600598962174)
- opportunity: False (0.08389037640265073)

### Tiny
- mean: True (0.9473810811508532)
- motive: True (0.9605096001181298)
- opportunity: True (0.936749461409047)

### Tom
- mean: False (0.08122777910936929)
- motive: False (0.06441766175763519)
- opportunity: False (0.11008786954403393)

The culprit is Tiny.
In fact, it is Rusty.
## 5minutemystery-turkey-cull
Beaker is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6343168082332088)
Beaker has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.879146760693242)
Beaker has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.5273165696704634)
Beaker had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
False (0.615087818987177)
Beau is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6451199006197486)
Beau has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9351098557348285)
Beau has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7683857617837733)
Beau had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5973730125048408)
Leaf is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7272012283179254)
Leaf has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8553685501761973)
Leaf has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.5292633777076584)
Leaf had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
False (0.6297745735138451)
Red is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6749080895533367)
Red has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.85729086409805)
Red has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
False (0.5380124470448935)
Red had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
False (0.7106283339569771)
### Beaker
- mean: False (0.12085323930675795)
- motive: False (0.47268343032953664)
- opportunity: False (0.615087818987177)

### Beau
- mean: True (0.9351098557348285)
- motive: True (0.7683857617837733)
- opportunity: True (0.5973730125048408)

### Leaf
- mean: False (0.14463144982380272)
- motive: False (0.4707366222923416)
- opportunity: False (0.6297745735138451)

### Red
- mean: False (0.14270913590195)
- motive: False (0.5380124470448935)
- opportunity: False (0.7106283339569771)

The culprit is Beau.
In fact, it is Beau.
## 5minutemystery-a-turkey-day-struggle
Aunt Rachel is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6842640081724978)
Aunt Rachel has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9437636745681832)
Aunt Rachel has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7690802105138688)
Aunt Rachel had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8221891570741111)
Chris is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7759445334082792)
Chris has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9773707989989006)
Chris has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9155072554665495)
Chris had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7879311977554747)
Diane is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7683857617837733)
Diane has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9532750830575984)
Diane has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8221891570741111)
Diane had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7704647687904915)
Jack the Dog is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7074046739492601)
Jack the Dog has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9569571625798028)
Jack the Dog has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7853085971692302)
Jack the Dog had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7969253675907205)
### Aunt Rachel
- mean: False (0.05623632543181678)
- motive: False (0.23091978948613123)
- opportunity: False (0.1778108429258889)

### Chris
- mean: True (0.9773707989989006)
- motive: True (0.9155072554665495)
- opportunity: True (0.7879311977554747)

### Diane
- mean: False (0.04672491694240155)
- motive: False (0.1778108429258889)
- opportunity: False (0.22953523120950847)

### Jack the Dog
- mean: False (0.04304283742019721)
Map:  49%|████▉     | 100/203 [36:32<32:32, 18.96s/ examples]Map:  50%|████▉     | 101/203 [36:50<31:43, 18.67s/ examples]Map:  50%|█████     | 102/203 [37:13<33:40, 20.00s/ examples]- motive: False (0.21469140283076982)
- opportunity: False (0.20307463240927948)

The culprit is Chris.
In fact, it is Chris.
## 5minutemystery-the-missing-briefcase
Porter 1 is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9299510719523877)
Porter 1 has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9767580632580227)
Porter 1 has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.904313027820426)
Porter 1 had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8958875533219306)
Porter 2 is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9299510095943111)
Porter 2 has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9778833990684288)
Porter 2 has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9152045868398637)
Porter 2 had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9390248079664695)
Porter 3 is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.936749461409047)
Porter 3 has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9777138240494376)
Porter 3 has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.91789335161495)
Porter 3 had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9414391533604212)
Porter 4 is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.936980484689786)
Porter 4 has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9774569868515869)
Porter 4 has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9155072008980665)
Porter 4 had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9152045868398637)
### Porter 1
- mean: False (0.023241936741977276)
- motive: False (0.095686972179574)
- opportunity: False (0.1041124466780694)

### Porter 2
- mean: False (0.022116600931571195)
- motive: False (0.08479541316013628)
- opportunity: False (0.06097519203353052)

### Porter 3
- mean: True (0.9777138240494376)
- motive: True (0.91789335161495)
- opportunity: True (0.9414391533604212)

### Porter 4
- mean: False (0.022543013148413116)
- motive: False (0.08449279910193352)
- opportunity: False (0.08479541316013628)

The culprit is Porter 3.
In fact, it is Porter 3.
## 5minutemystery-everythings-not-just-ducky
Bethany is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7371581892031299)
Bethany has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9429286143036572)
Bethany has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8998277786460391)
Bethany had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7431679939957333)
Connor is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7505527730327083)
Connor has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9549844874375936)
Connor has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8757870204368676)
Connor had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7185944237486072)
Emma is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7786493288700866)
Emma has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9429286143036572)
Emma has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9066531685310133)
Emma had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7853085971692302)
Tim is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7025300310583819)
Tim has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9314624659768579)
Tim has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8710367026584496)
Tim had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6825737331070684)
### Bethany
- mean: False (0.05707138569634285)
- motive: False (0.10017222135396087)
- opportunity: False (0.2568320060042667)

### Connor
- mean: False (0.045015512562406435)
- motive: False (0.12421297956313238)
- opportunity: False (0.28140557625139284)

### Emma
- mean: True (0.9429286143036572)
- motive: True (0.9066531685310133)
- opportunity: True (0.7853085971692302)

### Tim
- mean: False (0.06853753402314211)
- motive: False (0.12896329734155043)
- opportunity: False (0.31742626689293163)

The culprit is Emma.
In fact, it is Bethany.
## 5minutemystery-a-darkened-veterans-day
Colonel Abraham is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9149009617112335)
Colonel Abraham has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9715639953911919)
Colonel Abraham has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.897695304229796)
Colonel Abraham had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8864204283224634)
Map:  51%|█████     | 103/203 [37:31<32:25, 19.45s/ examples]Map:  51%|█████     | 104/203 [37:51<32:21, 19.61s/ examples]Frank Thompson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8534248451958423)
Frank Thompson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9513233906828413)
Frank Thompson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.884439109617765)
Frank Thompson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8762113474663927)
Mr. Landry is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8255897087847518)
Mr. Landry has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9491062747098069)
Mr. Landry has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7662936378892937)
Mr. Landry had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7759445334082792)
Ryan Smith is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.815232454829111)
Ryan Smith has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.950777887812089)
Ryan Smith has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7718434926244166)
Ryan Smith had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8198933606225757)
### Colonel Abraham
- mean: True (0.9715639953911919)
- motive: True (0.897695304229796)
- opportunity: True (0.8864204283224634)

### Frank Thompson
- mean: False (0.04867660931715867)
- motive: False (0.11556089038223505)
- opportunity: False (0.12378865253360727)

### Mr. Landry
- mean: False (0.05089372529019309)
- motive: False (0.23370636211070628)
- opportunity: False (0.22405546659172082)

### Ryan Smith
- mean: False (0.04922211218791095)
- motive: False (0.22815650737558335)
- opportunity: False (0.18010663937742433)

The culprit is Colonel Abraham.
In fact, it is Colonel Abraham.
## 5minutemystery-the-missing-ring
Fingers Ferguson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6697447888921682)
Fingers Ferguson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8969755785184792)
Fingers Ferguson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7461389980806673)
Fingers Ferguson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7279754274224494)
Joe Morgan is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5832033700118571)
Joe Morgan has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9073122118500465)
Joe Morgan has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8534247816107388)
Joe Morgan had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7217431689117048)
Manuel Garcia is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5156198737738186)
Manuel Garcia has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7853085971692302)
Manuel Garcia has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7520125537161032)
Manuel Garcia had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6187805031861143)
Mr. Bridges is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6601723415572317)
Mr. Bridges has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8333246107254184)
Mr. Bridges has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8116759653945079)
Mr. Bridges had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6976089520497016)
### Fingers Ferguson
- mean: False (0.1030244214815208)
- motive: False (0.2538610019193327)
- opportunity: False (0.27202457257755064)

### Joe Morgan
- mean: True (0.9073122118500465)
- motive: True (0.8534247816107388)
- opportunity: True (0.7217431689117048)

### Manuel Garcia
- mean: False (0.21469140283076982)
- motive: False (0.2479874462838968)
- opportunity: False (0.38121949681388567)

### Mr. Bridges
- mean: False (0.1666753892745816)
- motive: False (0.18832403460549207)
- opportunity: False (0.30239104795029836)

The culprit is Joe Morgan.
In fact, it is Joe Morgan.
## 5minutemystery-brass-keyboard-mystery
April Key #4 is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7333563569098757)
April Key #4 has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8175745039697023)
April Key #4 has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7008947664177184)
April Key #4 had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5312093941731293)
Denise Key #6 is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8418256636710214)
Denise Key #6 has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8902941942359355)
Denise Key #6 has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7090191197769757)
Denise Key #6 had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8128673413132903)
Map:  52%|█████▏    | 105/203 [38:20<36:15, 22.20s/ examples]Map:  52%|█████▏    | 106/203 [38:40<35:11, 21.77s/ examples]Harold Key #1 is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8267117710471246)
Harold Key #1 has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9105454073245608)
Harold Key #1 has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6992544513448877)
Harold Key #1 had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7341195403199204)
Kirsten Key #5 is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7279754274224494)
Kirsten Key #5 has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7826624547920057)
Kirsten Key #5 has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.65489470935198)
Kirsten Key #5 had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6057990946577705)
Robert (Buddy) Key #3 is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6959583025067009)
Robert (Buddy) Key #3 has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.815232454829111)
Robert (Buddy) Key #3 has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.5370414382302919)
Robert (Buddy) Key #3 had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6757646168022439)
### April Key #4
- mean: False (0.18242549603029767)
- motive: False (0.2991052335822816)
- opportunity: False (0.4687906058268707)

### Denise Key #6
- mean: True (0.8902941942359355)
- motive: True (0.7090191197769757)
- opportunity: True (0.8128673413132903)

### Harold Key #1
- mean: False (0.0894545926754392)
- motive: False (0.30074554865511227)
- opportunity: False (0.26588045968007956)

### Kirsten Key #5
- mean: False (0.2173375452079943)
- motive: False (0.34510529064802)
- opportunity: False (0.3942009053422295)

### Robert (Buddy) Key #3
- mean: False (0.184767545170889)
- motive: False (0.46295856176970807)
- opportunity: False (0.32423538319775613)

The culprit is Denise Key #6.
In fact, it is April Key #4.
## 5minutemystery-the-curse-of-the-unlucky-streak
Coach Williams is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8587185689177256)
Coach Williams has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9230391416137353)
Coach Williams has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8647679145346777)
Coach Williams had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8278281666221954)
Joe is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8509646659219744)
Joe has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9449946880768697)
Joe has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8233283740192667)
Joe had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7662937064012869)
Mrs. Williams is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8633916342942395)
Mrs. Williams has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9437636745681832)
Mrs. Williams has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.878314250659373)
Mrs. Williams had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8255897087847518)
Roderick is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8381505623254643)
Roderick has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9190633328333496)
Roderick has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8610715240899957)
Roderick had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7592254214399092)
### Coach Williams
- mean: False (0.07696085838626465)
- motive: False (0.13523208546532228)
- opportunity: False (0.17217183337780462)

### Joe
- mean: False (0.055005311923130296)
- motive: False (0.17667162598073327)
- opportunity: False (0.2337062935987131)

### Mrs. Williams
- mean: True (0.9437636745681832)
- motive: True (0.878314250659373)
- opportunity: True (0.8255897087847518)

### Roderick
- mean: False (0.08093666716665038)
- motive: False (0.13892847591000435)
- opportunity: False (0.24077457856009077)

The culprit is Mrs. Williams.
In fact, it is Joe.
## 5minutemystery-halloween-2008
Bride is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8987665204865408)
Bride has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8962513815714083)
Bride has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9032942081209032)
Bride had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.858718632897247)
Groom is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8381505623254643)
Groom has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8816149238192855)
Groom has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8633915828320894)
Map:  53%|█████▎    | 107/203 [39:12<39:21, 24.60s/ examples]Map:  53%|█████▎    | 108/203 [39:32<36:44, 23.21s/ examples]Groom had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8140528237853677)
Indian Chief is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8098781635062345)
Indian Chief has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8360197583769845)
Indian Chief has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8459423727595791)
Indian Chief had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8267117710471246)
Wealthy Woman is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8966140148346177)
Wealthy Woman has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9219218506394821)
Wealthy Woman has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9124361878432953)
Wealthy Woman had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8951566249612815)
### Bride
- mean: False (0.10374861842859173)
- motive: False (0.09670579187909678)
- opportunity: False (0.14128136710275296)

### Groom
- mean: False (0.11838507618071448)
- motive: False (0.1366084171679106)
- opportunity: False (0.1859471762146323)

### Indian Chief
- mean: False (0.1639802416230155)
- motive: False (0.15405762724042094)
- opportunity: False (0.17328822895287543)

### Wealthy Woman
- mean: True (0.9219218506394821)
- motive: True (0.9124361878432953)
- opportunity: True (0.8951566249612815)

The culprit is Wealthy Woman.
In fact, it is Groom.
## 5minutemystery-the-trick-or-treat-mystery
Dorothy is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7975568155246964)
Dorothy has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9317114347547434)
Dorothy has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7826624547920057)
Dorothy had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7885831565209055)
Superman is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6662796746479285)
Superman has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8914335992201801)
Superman has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7937461674149602)
Superman had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7541915239138703)
The Ghost is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8381505623254643)
The Ghost has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8553685501761973)
The Ghost has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7534666630720156)
The Ghost had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8152325155686644)
The Lion is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8098781635062345)
The Lion has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8633915828320894)
The Lion has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8080671968507699)
The Lion had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.794384956668203)
The Witch is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8128672807499561)
The Witch has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8864204283224634)
The Witch has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7341195403199204)
The Witch had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7461389980806673)
### Dorothy
- mean: True (0.9317114347547434)
- motive: True (0.7826624547920057)
- opportunity: True (0.7885831565209055)

### Superman
- mean: False (0.10856640077981994)
- motive: False (0.20625383258503982)
- opportunity: False (0.24580847608612966)

### The Ghost
- mean: False (0.14463144982380272)
- motive: False (0.2465333369279844)
- opportunity: False (0.18476748443133562)

### The Lion
- mean: False (0.1366084171679106)
- motive: False (0.1919328031492301)
- opportunity: False (0.20561504333179703)

### The Witch
- mean: False (0.11357957167753663)
- motive: False (0.26588045968007956)
- opportunity: False (0.2538610019193327)

The culprit is Dorothy.
In fact, it is The Witch.
## 5minutemystery-house-of-the-rising-pumpkin
Curtis is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7962924854830264)
Curtis has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.900179384114949)
Curtis has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8591917766133458)
Curtis had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6740504382339836)
Dabney is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8652240590801695)
Dabney has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9249593046682986)
Dabney has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9039744767757508)
Map:  54%|█████▎    | 109/203 [39:56<37:07, 23.70s/ examples]Map:  54%|█████▍    | 110/203 [40:17<35:21, 22.81s/ examples]Dabney had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7786492592534148)
Kim is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8050197941712954)
Kim has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9205042693180057)
Kim has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8534247816107388)
Kim had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.740174341079517)
Mary is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7988153087356352)
Mary has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9207896596153058)
Mary has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.816406362162552)
Mary had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7217432334405754)
### Curtis
- mean: False (0.09982061588505098)
- motive: False (0.14080822338665422)
- opportunity: False (0.3259495617660164)

### Dabney
- mean: True (0.9249593046682986)
- motive: True (0.9039744767757508)
- opportunity: True (0.7786492592534148)

### Kim
- mean: False (0.07949573068199434)
- motive: False (0.14657521838926124)
- opportunity: False (0.25982565892048304)

### Mary
- mean: False (0.07921034038469421)
- motive: False (0.18359363783744798)
- opportunity: False (0.27825676655942455)

The culprit is Dabney.
In fact, it is Kim.
## 5minutemystery-the-secret-of-the-scarecrows-mask
Charles Kincaid is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7041601500399041)
Charles Kincaid has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8652240590801695)
Charles Kincaid has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8233283740192667)
Charles Kincaid had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7170118721569225)
Chester is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.811078188867804)
Chester has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8807970337584357)
Chester has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8824278665848695)
Chester had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8407825844829613)
Mr. Winfrey is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7683857617837733)
Mr. Winfrey has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8958875533219306)
Mr. Winfrey has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8966140148346177)
Mr. Winfrey had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8638516611889259)
Mrs. Winfrey is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8216173667955227)
Mrs. Winfrey has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.897695304229796)
Mrs. Winfrey has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9199306971612747)
Mrs. Winfrey had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8688268116310761)
### Charles Kincaid
- mean: False (0.13477594091983047)
- motive: False (0.17667162598073327)
- opportunity: False (0.2829881278430775)

### Chester
- mean: False (0.11920296624156435)
- motive: False (0.11757213341513051)
- opportunity: False (0.15921741551703872)

### Mr. Winfrey
- mean: False (0.1041124466780694)
- motive: False (0.10338598516538233)
- opportunity: False (0.13614833881107413)

### Mrs. Winfrey
- mean: True (0.897695304229796)
- motive: True (0.9199306971612747)
- opportunity: True (0.8688268116310761)

The culprit is Mrs. Winfrey.
In fact, it is Chester.
## 5minutemystery-the-scarecrow-slasher
Annie is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8509647293237851)
Annie has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9012274173198201)
Annie has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9152045868398637)
Annie had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.911809923444246)
Mr. Forbes is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8397339530959691)
Mr. Forbes has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9284088027271398)
Mr. Forbes has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9158089188126235)
Mr. Forbes had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8966140749572745)
Mrs. Avery is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8740772044235984)
Mrs. Avery has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9284088027271398)
Mrs. Avery has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.927099763868178)
Map:  55%|█████▍    | 111/203 [40:39<34:18, 22.37s/ examples]Map:  55%|█████▌    | 112/203 [40:55<31:03, 20.48s/ examples]Mrs. Avery had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9076402191395381)
Philips is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.844921525814193)
Philips has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8887587777822111)
Philips has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9012274173198201)
Philips had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9167080509980843)
### Annie
- mean: False (0.09877258268017985)
- motive: False (0.08479541316013628)
- opportunity: False (0.08819007655575395)

### Mr. Forbes
- mean: False (0.07159119727286023)
- motive: False (0.0841910811873765)
- opportunity: False (0.10338592504272548)

### Mrs. Avery
- mean: True (0.9284088027271398)
- motive: True (0.927099763868178)
- opportunity: True (0.9076402191395381)

### Philips
- mean: False (0.11124122221778887)
- motive: False (0.09877258268017985)
- opportunity: False (0.08329194900191572)

The culprit is Mrs. Avery.
In fact, it is Philips.
## 5minutemystery-the-golden-ruse
Miss Jones is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7704647687904915)
Miss Jones has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9719924933469237)
Miss Jones has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9246876822649571)
Miss Jones had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.862930245043327)
Miss. Pendlebury is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7872777601997338)
Miss. Pendlebury has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9586927300380139)
Miss. Pendlebury has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8856314413364714)
Miss. Pendlebury had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8740772044235984)
Mr. Horgan is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9108630396247971)
Mr. Horgan has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9773707989989006)
Mr. Horgan has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.950041474283655)
Mr. Horgan had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8966140148346177)
Mr. Reese is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.911809923444246)
Mr. Reese has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9820137614190769)
Mr. Reese has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9602121708473209)
Mr. Reese had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9056565771882901)
### Miss Jones
- mean: False (0.028007506653076275)
- motive: False (0.07531231773504288)
- opportunity: False (0.13706975495667295)

### Miss. Pendlebury
- mean: False (0.04130726996198608)
- motive: False (0.11436855866352857)
- opportunity: False (0.12592279557640162)

### Mr. Horgan
- mean: False (0.02262920100109944)
- motive: False (0.04995852571634496)
- opportunity: False (0.10338598516538233)

### Mr. Reese
- mean: True (0.9820137614190769)
- motive: True (0.9602121708473209)
- opportunity: True (0.9056565771882901)

The culprit is Mr. Reese.
In fact, it is Mr. Horgan.
## 5minutemystery-hound-of-the-buskerville
Balloon Twister is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8489722037469682)
Balloon Twister has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9458012588547495)
Balloon Twister has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8732147785405174)
Balloon Twister had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8386797935187188)
Living Statue is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7122321792841629)
Living Statue has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8856314413364714)
Living Statue has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7106282704218558)
Living Statue had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5717666110200305)
Mime is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7839884808423031)
Mime has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9155072554665495)
Mime has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.816406362162552)
Mime had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7090191197769757)
Stilt-Walker is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7310585348819939)
Stilt-Walker has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9012274173198201)
Stilt-Walker has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7138307093362539)
Map:  56%|█████▌    | 113/203 [41:18<31:57, 21.31s/ examples]Map:  56%|█████▌    | 114/203 [41:38<31:01, 20.92s/ examples]Map:  57%|█████▋    | 115/203 [41:57<29:42, 20.25s/ examples]Stilt-Walker had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5698526542706361)
### Balloon Twister
- mean: True (0.9458012588547495)
- motive: True (0.8732147785405174)
- opportunity: True (0.8386797935187188)

### Living Statue
- mean: False (0.11436855866352857)
- motive: False (0.28937172957814417)
- opportunity: False (0.42823338897996954)

### Mime
- mean: False (0.08449274453345046)
- motive: False (0.18359363783744798)
- opportunity: False (0.29098088022302426)

### Stilt-Walker
- mean: False (0.09877258268017985)
- motive: False (0.2861692906637461)
- opportunity: False (0.43014734572936386)

The culprit is Balloon Twister.
In fact, it is Stilt-Walker.
## 5minutemystery-moriarty-picks-a-murderer-part-two
Hansom Cab Driver is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6825737331070684)
Hansom Cab Driver has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7371581232960549)
Hansom Cab Driver has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6584175136252488)
Hansom Cab Driver had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5467381591701916)
Policeman is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
False (0.5544704160706745)
Policeman has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.6057990946577705)
Policeman has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.5698526542706361)
Policeman had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
False (0.5380124470448935)
Theater Usher is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
False (0.5341265295318852)
Theater Usher has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
False (0.5341265295318852)
Theater Usher has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.5156199352405011)
Theater Usher had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
False (0.5583269696343842)
Ticket Seller is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7279754274224494)
Ticket Seller has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7937462383814009)
Ticket Seller has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6757646168022439)
Ticket Seller had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6610481693322063)
### Hansom Cab Driver
- mean: False (0.2628418767039451)
- motive: False (0.3415824863747512)
- opportunity: False (0.45326184082980836)

### Policeman
- mean: False (0.3942009053422295)
- motive: False (0.43014734572936386)
- opportunity: False (0.5380124470448935)

### Theater Usher
- mean: False (0.5341265295318852)
- motive: False (0.4843800647594989)
- opportunity: False (0.5583269696343842)

### Ticket Seller
- mean: True (0.7937462383814009)
- motive: True (0.6757646168022439)
- opportunity: True (0.6610481693322063)

The culprit is Ticket Seller.
In fact, it is Theater Usher.
## 5minutemystery-the-scent-of-a-thief
Betty is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5204963206682631)
Betty has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9307105568817887)
Betty has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9329437018480795)
Betty had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8973360043541736)
Darlene is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7272012283179254)
Darlene has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9196425651151865)
Darlene has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9224823751318276)
Darlene had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8305941261447712)
Mr. Danby is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6791786560103119)
Mr. Danby has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8895288719962232)
Mr. Danby has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.875361437979977)
Mr. Danby had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8509647293237851)
Mr. Harrison is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6379335503198971)
Mr. Harrison has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9012274173198201)
Mr. Harrison has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8820220178442959)
Mr. Harrison had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8322366416985943)
### Betty
- mean: True (0.9307105568817887)
- motive: True (0.9329437018480795)
- opportunity: True (0.8973360043541736)

### Darlene
- mean: False (0.0803574348848135)
- motive: False (0.07751762486817237)
- opportunity: False (0.16940587385522876)

### Mr. Danby
- mean: False (0.11047112800377679)
- motive: False (0.12463856202002299)
- opportunity: False (0.14903527067621491)

### Mr. Harrison
- mean: False (0.09877258268017985)
- motive: False (0.1179779821557041)
- opportunity: False (0.16776335830140565)

The culprit is Betty.
In fact, it is Mr. Harrison.
Map:  57%|█████▋    | 116/203 [42:18<29:48, 20.56s/ examples]## 5minutemystery-moriarty-picks-a-murderer-part-one
Ed the Bludgeoner is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5612147992901458)
Ed the Bludgeoner has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7217432334405754)
Ed the Bludgeoner has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8539127714046447)
Ed the Bludgeoner had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6076631662366868)
Fastidious Fred Fielder is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
False (0.5097644370426659)
Fastidious Fred Fielder has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8037905715242155)
Fastidious Fred Fielder has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8267117710471246)
Fastidious Fred Fielder had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5983121871760707)
Herman Houlihan is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5621765360769869)
Herman Houlihan has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7956581141325956)
Herman Houlihan has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8459424357871997)
Herman Houlihan had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6654105788791005)
Morris the Ascot Dandy is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6601723415572317)
Morris the Ascot Dandy has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8244619332958376)
Morris the Ascot Dandy has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8428631416381634)
Morris the Ascot Dandy had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6187804294217345)
### Ed the Bludgeoner
- mean: False (0.27825676655942455)
- motive: False (0.14608722859535528)
- opportunity: False (0.3923368337633132)

### Fastidious Fred Fielder
- mean: False (0.1962094284757845)
- motive: False (0.17328822895287543)
- opportunity: False (0.4016878128239293)

### Herman Houlihan
- mean: True (0.7956581141325956)
- motive: True (0.8459424357871997)
- opportunity: True (0.6654105788791005)

### Morris the Ascot Dandy
- mean: False (0.1755380667041624)
- motive: False (0.15713685836183655)
- opportunity: False (0.3812195705782655)

The culprit is Herman Houlihan.
In fact, it is Fastidious Fred Fielder.
## 5minutemystery-the-geneva-summit-goldfish-mystery
Ermina Glandon is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6406358487498992)
Ermina Glandon has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8300437877296776)
Ermina Glandon has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7106282704218558)
Ermina Glandon had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5717666110200305)
George Adams is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6343168082332088)
George Adams has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7772998201448375)
George Adams has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.64779823427608)
George Adams had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5794004215835179)
Matthew O'Leary is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.525368812147771)
Matthew O'Leary has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8529354311342636)
Matthew O'Leary has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8745065279415651)
Matthew O'Leary had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5813030649269245)
Prince Rahim is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6469064338453809)
Prince Rahim has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8969755785184792)
Prince Rahim has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7534666630720156)
Prince Rahim had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7122322217365102)
Ronald Reagan is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
False (0.6297746298200823)
Ronald Reagan has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8459424357871997)
Ronald Reagan has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6334102859975052)
Ronald Reagan had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5467381591701916)
### Ermina Glandon
- mean: False (0.16995621227032243)
- motive: False (0.28937172957814417)
- opportunity: False (0.42823338897996954)

### George Adams
- mean: False (0.22270017985516255)
- motive: False (0.35220176572392004)
- opportunity: False (0.4205995784164821)

### Matthew O'Leary
- mean: False (0.14706456886573638)
- motive: False (0.12549347205843486)
Map:  58%|█████▊    | 117/203 [42:41<30:45, 21.46s/ examples]Map:  58%|█████▊    | 118/203 [42:59<28:34, 20.17s/ examples]Map:  59%|█████▊    | 119/203 [43:24<30:19, 21.66s/ examples]- opportunity: False (0.4186969350730755)

### Prince Rahim
- mean: True (0.8969755785184792)
- motive: True (0.7534666630720156)
- opportunity: True (0.7122322217365102)

### Ronald Reagan
- mean: False (0.15405756421280026)
- motive: False (0.36658971400249485)
- opportunity: False (0.45326184082980836)

The culprit is Prince Rahim.
In fact, it is Ronald Reagan.
## 5minutemystery-a-straw-stuffed-mystery
Bill Albertson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7025300310583819)
Bill Albertson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8670357473609658)
Bill Albertson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9111797236708432)
Bill Albertson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7386690954574974)
Mr. Fletcher is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7745833916423246)
Mr. Fletcher has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8697145551802641)
Mr. Fletcher has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.897695304229796)
Mr. Fletcher had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6909762697651828)
Professor Surenie is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7371581232960549)
Professor Surenie has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.879146760693242)
Professor Surenie has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9105454073245608)
Professor Surenie had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7170118721569225)
Rachel Beaton is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6424325178417575)
Rachel Beaton has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8449215887657546)
Rachel Beaton has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8376199551237796)
Rachel Beaton had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.702530072932436)
### Bill Albertson
- mean: True (0.8670357473609658)
- motive: True (0.9111797236708432)
- opportunity: True (0.7386690954574974)

### Mr. Fletcher
- mean: False (0.13028544481973592)
- motive: False (0.10230469577020396)
- opportunity: False (0.3090237302348172)

### Professor Surenie
- mean: False (0.12085323930675795)
- motive: False (0.0894545926754392)
- opportunity: False (0.2829881278430775)

### Rachel Beaton
- mean: False (0.15507841123424537)
- motive: False (0.16238004487622038)
- opportunity: False (0.29746992706756403)

The culprit is Bill Albertson.
In fact, it is Mr. Fletcher.
## 5minutemystery-ask-marthathe-shoplifter
Jane Croydon is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8322366416985943)
Jane Croydon has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8820219652716884)
Jane Croydon has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8169910947371979)
Jane Croydon had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7170118721569225)
Johnny Martin is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8807970862580315)
Johnny Martin has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9136765013387816)
Johnny Martin has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8397339530959691)
Johnny Martin had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7476159279883341)
Martha Hampden is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8031737798924701)
Martha Hampden has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8872045854516336)
Martha Hampden has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.779321849347754)
Martha Hampden had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.615087855649269)
Steve Kravitz is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8661325012437474)
Steve Kravitz has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8994751578343994)
Steve Kravitz has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8233283740192667)
Steve Kravitz had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6584174547581384)
### Jane Croydon
- mean: False (0.11797803472831159)
- motive: False (0.1830089052628021)
- opportunity: False (0.2829881278430775)

### Johnny Martin
- mean: True (0.9136765013387816)
- motive: True (0.8397339530959691)
- opportunity: True (0.7476159279883341)

### Martha Hampden
- mean: False (0.11279541454836639)
- motive: False (0.22067815065224605)
- opportunity: False (0.38491214435073096)

### Steve Kravitz
- mean: False (0.10052484216560065)
- motive: False (0.17667162598073327)
- opportunity: False (0.3415825452418616)

The culprit is Johnny Martin.
In fact, it is Johnny Martin.
## 5minutemystery-the-hanging-figure
Daisy Morris is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.920217993899809)
Map:  59%|█████▉    | 120/203 [43:42<28:41, 20.74s/ examples]Map:  60%|█████▉    | 121/203 [44:03<28:21, 20.75s/ examples]Daisy Morris has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9385759849623091)
Daisy Morris has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8238958672039278)
Daisy Morris had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8322367037050584)
Dale Clark is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9026095892260383)
Dale Clark has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.919930758847437)
Dale Clark has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8582439976623328)
Dale Clark had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8638516611889259)
Iain Potts is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.884439109617765)
Iain Potts has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.936980484689786)
Iain Potts has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8705973031072073)
Iain Potts had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8509647293237851)
Lucy Smith is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8529354946829077)
Lucy Smith has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.948346199423113)
Lucy Smith has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8272706865691472)
Lucy Smith had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8816149238192855)
### Daisy Morris
- mean: False (0.061424015037690904)
- motive: False (0.17610413279607218)
- opportunity: False (0.16776329629494158)

### Dale Clark
- mean: False (0.08006924115256298)
- motive: False (0.14175600233766716)
- opportunity: False (0.13614833881107413)

### Iain Potts
- mean: True (0.936980484689786)
- motive: True (0.8705973031072073)
- opportunity: True (0.8509647293237851)

### Lucy Smith
- mean: False (0.051653800576886955)
- motive: False (0.17272931343085285)
- opportunity: False (0.11838507618071448)

The culprit is Iain Potts.
In fact, it is Dale Clark.
## 5minutemystery-our-quarterback-is-missing
Coach Roster is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7341195403199204)
Coach Roster has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8459424357871997)
Coach Roster has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.920789721359066)
Coach Roster had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8879840376027315)
Eddie is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8013146490010521)
Eddie has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8991213421091365)
Eddie has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9265699426348812)
Eddie had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8868131040663721)
Eddie's Mom is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8086723702005608)
Eddie's Mom has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8991213421091365)
Eddie's Mom has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9312127242200585)
Eddie's Mom had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8757870204368676)
Marissa is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7371581892031299)
Marissa has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9092645024391882)
Marissa has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9456006903352807)
Marissa had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9158089188126235)
### Coach Roster
- mean: False (0.15405756421280026)
- motive: False (0.079210278640934)
- opportunity: False (0.11201596239726852)

### Eddie
- mean: False (0.10087865789086348)
- motive: False (0.07343005736511876)
- opportunity: False (0.11318689593362785)

### Eddie's Mom
- mean: False (0.10087865789086348)
- motive: False (0.06878727577994148)
- opportunity: False (0.12421297956313238)

### Marissa
- mean: True (0.9092645024391882)
- motive: True (0.9456006903352807)
- opportunity: True (0.9158089188126235)

The culprit is Marissa.
In fact, it is Eddie's Mom.
## 5minutemystery-ask-marthathe-case-of-the-missing-canary
Alex Johnston is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7446563307563252)
Alex Johnston has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9145963810991447)
Alex Johnston has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8499711693725173)
Alex Johnston had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7233094544266295)
Jimmy Carstairs is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6893056507505698)
Map:  60%|██████    | 122/203 [44:20<26:36, 19.71s/ examples]Map:  61%|██████    | 123/203 [44:39<25:42, 19.28s/ examples]Jimmy Carstairs has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.875361437979977)
Jimmy Carstairs has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7962924854830264)
Jimmy Carstairs had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6297746298200823)
Lydia Carstairs is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6992544513448877)
Lydia Carstairs has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8643104392003704)
Lydia Carstairs has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8221891570741111)
Lydia Carstairs had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.72951977676791)
Sarabelle is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6540113633452196)
Sarabelle has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.842345065078002)
Sarabelle has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8050197941712954)
Sarabelle had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6279512069990912)
### Alex Johnston
- mean: True (0.9145963810991447)
- motive: True (0.8499711693725173)
- opportunity: True (0.7233094544266295)

### Jimmy Carstairs
- mean: False (0.12463856202002299)
- motive: False (0.20370751451697355)
- opportunity: False (0.37022537017991775)

### Lydia Carstairs
- mean: False (0.13568956079962957)
- motive: False (0.1778108429258889)
- opportunity: False (0.27048022323209)

### Sarabelle
- mean: False (0.157654934921998)
- motive: False (0.19498020582870457)
- opportunity: False (0.37204879300090876)

The culprit is Alex Johnston.
In fact, it is Alex Johnston.
## 5minutemystery-register-robbery
Dan is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8037905715242155)
Dan has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9241418261705818)
Dan has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.847967740521315)
Dan had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8289387819824735)
David is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8474634858439474)
David has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9394705907755942)
David has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9012274173198201)
David had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.847967740521315)
Robert is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.862930245043327)
Robert has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9629528509146777)
Robert has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9362849627883332)
Robert had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8509647293237851)
Teresa is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8428631416381634)
Teresa has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9553191662872157)
Teresa has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9230391966311572)
Teresa had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8652240590801695)
### Dan
- mean: False (0.07585817382941817)
- motive: False (0.15203225947868504)
- opportunity: False (0.1710612180175265)

### David
- mean: False (0.06052940922440575)
- motive: False (0.09877258268017985)
- opportunity: False (0.15203225947868504)

### Robert
- mean: True (0.9629528509146777)
- motive: True (0.9362849627883332)
- opportunity: True (0.8509647293237851)

### Teresa
- mean: False (0.04468083371278431)
- motive: False (0.07696080336884281)
- opportunity: False (0.13477594091983047)

The culprit is Robert.
In fact, it is David.
## 5minutemystery-mr-patrick-back-in-class
CSA currency is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7975568155246964)
CSA currency has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9388008138003494)
CSA currency has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8433797899747144)
CSA currency had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8795611817678315)
Diamond necklace is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7170118721569225)
Diamond necklace has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9210741501882456)
Diamond necklace has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7295197332851441)
Diamond necklace had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7461389980806673)
Gold money clip is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6859494535376744)
Map:  61%|██████    | 124/203 [45:08<29:17, 22.24s/ examples]Map:  62%|██████▏   | 125/203 [45:34<30:21, 23.35s/ examples]Gold money clip has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9161096235973493)
Gold money clip has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7240905157396584)
Gold money clip had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7648916137833577)
Jewel encrusted pistol is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7185943809170431)
Jewel encrusted pistol has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9196425651151865)
Jewel encrusted pistol has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7620701143808404)
Jewel encrusted pistol had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7041600870830834)
Lithograph photo is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7786493288700866)
Lithograph photo has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9412234437340664)
Lithograph photo has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8418256009501243)
Lithograph photo had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.832781310996106)
### CSA currency
- mean: True (0.9388008138003494)
- motive: True (0.8433797899747144)
- opportunity: True (0.8795611817678315)

### Diamond necklace
- mean: False (0.07892584981175443)
- motive: False (0.2704802667148559)
- opportunity: False (0.2538610019193327)

### Gold money clip
- mean: False (0.08389037640265073)
- motive: False (0.27590948426034156)
- opportunity: False (0.23510838621664232)

### Jewel encrusted pistol
- mean: False (0.0803574348848135)
- motive: False (0.23792988561915962)
- opportunity: False (0.2958399129169166)

### Lithograph photo
- mean: False (0.05877655626593359)
- motive: False (0.15817439904987574)
- opportunity: False (0.16721868900389403)

The culprit is CSA currency.
In fact, it is Lithograph photo.
## 5minutemystery-ask-marthathe-blackmailer
Horace Sage is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8647679145346777)
Horace Sage has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9142907234091052)
Horace Sage has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8697145551802641)
Horace Sage had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7520125537161032)
Martin Amberton is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9069831945855868)
Martin Amberton has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9606574760904091)
Martin Amberton has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9173026661190045)
Martin Amberton had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8044058710149623)
Mary Devers is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8244619332958376)
Mary Devers has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9324533354081785)
Mary Devers has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8774768149941248)
Mary Devers had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7799928701983835)
Susan Royster is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8074605993751186)
Susan Royster has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.927887794449634)
Susan Royster has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9105454073245608)
Susan Royster had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7799928701983835)
### Horace Sage
- mean: False (0.08570927659089478)
- motive: False (0.13028544481973592)
- opportunity: False (0.2479874462838968)

### Martin Amberton
- mean: True (0.9606574760904091)
- motive: True (0.9173026661190045)
- opportunity: True (0.8044058710149623)

### Mary Devers
- mean: False (0.06754666459182146)
- motive: False (0.12252318500587522)
- opportunity: False (0.22000712980161652)

### Susan Royster
- mean: False (0.07211220555036602)
- motive: False (0.0894545926754392)
- opportunity: False (0.22000712980161652)

The culprit is Martin Amberton.
In fact, it is Mary Devers.
## 5minutemystery-a-dream-of-old-salem
Abigail Thorpe is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5698526542706361)
Abigail Thorpe has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.803173839733582)
Abigail Thorpe has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6976088896786037)
Abigail Thorpe had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8278281049441929)
Adam Browne is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5544704160706745)
Adam Browne has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.794384956668203)
Adam Browne has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8509647293237851)
Map:  62%|██████▏   | 126/203 [45:58<30:17, 23.60s/ examples]Map:  63%|██████▎   | 127/203 [46:26<31:36, 24.96s/ examples]Adam Browne had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8322366416985943)
Goodwife Browne is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6654105193867614)
Goodwife Browne has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9079671476237222)
Goodwife Browne has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8774768149941248)
Goodwife Browne had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8969755785184792)
Sarah Goodwin is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6095241816115718)
Sarah Goodwin has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8887587777822111)
Sarah Goodwin has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8255897087847518)
Sarah Goodwin had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8697145551802641)
### Abigail Thorpe
- mean: False (0.19682616026641797)
- motive: False (0.3023911103213963)
- opportunity: False (0.1721718950558071)

### Adam Browne
- mean: False (0.20561504333179703)
- motive: False (0.14903527067621491)
- opportunity: False (0.16776335830140565)

### Goodwife Browne
- mean: True (0.9079671476237222)
- motive: True (0.8774768149941248)
- opportunity: True (0.8969755785184792)

### Sarah Goodwin
- mean: False (0.11124122221778887)
- motive: False (0.1744102912152482)
- opportunity: False (0.13028544481973592)

The culprit is Goodwife Browne.
In fact, it is Adam Browne.
## 5minutemystery-the-antique-clock-mystery
The grandfather clock (stopped at 10:10 p.m.) is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8289387819824735)
The grandfather clock (stopped at 10:10 p.m.) has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8991213421091365)
The grandfather clock (stopped at 10:10 p.m.) has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7534666630720156)
The grandfather clock (stopped at 10:10 p.m.) had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7446563307563252)
The mantle clock (stopped at 10:59 p.m.) is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8407825844829613)
The mantle clock (stopped at 10:59 p.m.) has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.897695304229796)
The mantle clock (stopped at 10:59 p.m.) has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7853085971692302)
The mantle clock (stopped at 10:59 p.m.) had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8255897087847518)
The pocket watch (stopped at 3:18 a.m.) is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8524448242555318)
The pocket watch (stopped at 3:18 a.m.) has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.918480215734292)
The pocket watch (stopped at 3:18 a.m.) has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8305941261447712)
The pocket watch (stopped at 3:18 a.m.) had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8031737798924701)
The wall clock (stopped at 2:01 a.m.) is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8563324216110711)
The wall clock (stopped at 2:01 a.m.) has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9124361878432953)
The wall clock (stopped at 2:01 a.m.) has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8418256636710214)
The wall clock (stopped at 2:01 a.m.) had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8031737798924701)
The wristwatch (stopped at 5:22 p.m.) is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.816406362162552)
The wristwatch (stopped at 5:22 p.m.) has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8875949368741688)
The wristwatch (stopped at 5:22 p.m.) has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7641883982873323)
The wristwatch (stopped at 5:22 p.m.) had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7279754274224494)
### The grandfather clock (stopped at 10:10 p.m.)
- mean: False (0.10087865789086348)
- motive: False (0.2465333369279844)
- opportunity: False (0.2553436692436748)

### The mantle clock (stopped at 10:59 p.m.)
- mean: False (0.10230469577020396)
- motive: False (0.21469140283076982)
- opportunity: False (0.1744102912152482)

### The pocket watch (stopped at 3:18 a.m.)
- mean: False (0.08151978426570805)
- motive: False (0.16940587385522876)
- opportunity: False (0.19682622010752993)

### The wall clock (stopped at 2:01 a.m.)
- mean: True (0.9124361878432953)
- motive: True (0.8418256636710214)
- opportunity: True (0.8031737798924701)

### The wristwatch (stopped at 5:22 p.m.)
- mean: False (0.1124050631258312)
- motive: False (0.23581160171266768)
- opportunity: False (0.27202457257755064)

The culprit is The wall clock (stopped at 2:01 a.m.).
In fact, it is The mantle clock (stopped at 10:59 p.m.).
## 5minutemystery-ask-marthathe-perjurer
Horace Osamway is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8910549899564296)
Horace Osamway has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9477691649813238)
Map:  63%|██████▎   | 128/203 [46:50<30:43, 24.59s/ examples]Map:  64%|██████▎   | 129/203 [47:16<30:52, 25.04s/ examples]Horace Osamway has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9121235591541035)
Horace Osamway had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8233283740192667)
John Eberley is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8311430831606665)
John Eberley has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9289263523387795)
John Eberley has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8688268116310761)
John Eberley had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7386690954574974)
Martha Cranston is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8116760258690822)
Martha Cranston has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9661559457424579)
Martha Cranston has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8652240590801695)
Martha Cranston had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8300437258865985)
Mildred Greene is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8757870204368676)
Mildred Greene has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9606574760904091)
Mildred Greene has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8918110138739693)
Mildred Greene had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8068526417769779)
### Horace Osamway
- mean: True (0.9477691649813238)
- motive: True (0.9121235591541035)
- opportunity: True (0.8233283740192667)

### John Eberley
- mean: False (0.07107364766122048)
- motive: False (0.1311731883689239)
- opportunity: False (0.26133090454250263)

### Martha Cranston
- mean: False (0.03384405425754211)
- motive: False (0.13477594091983047)
- opportunity: False (0.16995627411340153)

### Mildred Greene
- mean: False (0.03934252390959092)
- motive: False (0.10818898612603067)
- opportunity: False (0.1931473582230221)

The culprit is Horace Osamway.
In fact, it is John Eberley.
## 5minutemystery-ask-marthathe-embezzler
Joan Carstairs is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7341195403199204)
Joan Carstairs has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9268353022276509)
Joan Carstairs has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8289387819824735)
Joan Carstairs had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7534666630720156)
Les Nolting is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7461389980806673)
Les Nolting has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8969755785184792)
Les Nolting has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8354835531737983)
Les Nolting had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6584175136252488)
Paul Brassard is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8679338697256817)
Paul Brassard has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9473810811508532)
Paul Brassard has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.913058338092082)
Paul Brassard had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7620700689579233)
Sarah Kimble is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7853085971692302)
Sarah Kimble has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9073122118500465)
Sarah Kimble has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8714748565614324)
Sarah Kimble had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7138307093362539)
### Joan Carstairs
- mean: False (0.07316469777234913)
- motive: False (0.1710612180175265)
- opportunity: False (0.2465333369279844)

### Les Nolting
- mean: False (0.1030244214815208)
- motive: False (0.1645164468262017)
- opportunity: False (0.3415824863747512)

### Paul Brassard
- mean: True (0.9473810811508532)
- motive: True (0.913058338092082)
- opportunity: True (0.7620700689579233)

### Sarah Kimble
- mean: False (0.09268778814995349)
- motive: False (0.12852514343856758)
- opportunity: False (0.2861692906637461)

The culprit is Paul Brassard.
In fact, it is Sarah Kimble.
## 5minutemystery-the-backyard-slumber-party
Justin Scott is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6495786332146115)
Justin Scott has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7826625131049049)
Justin Scott has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8652240590801695)
Justin Scott had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7826625131049049)
Martin Simmons is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6297746298200823)
Map:  64%|██████▍   | 130/203 [47:34<28:04, 23.08s/ examples]Map:  65%|██████▍   | 131/203 [48:01<29:01, 24.19s/ examples]Martin Simmons has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8365545874520802)
Martin Simmons has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.821044090050916)
Martin Simmons had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7138307093362539)
Stephen Kennelly is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6513548405484016)
Stephen Kennelly has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8300437258865985)
Stephen Kennelly has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8333246107254184)
Stephen Kennelly had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7431679939957333)
Trevor Sutherland is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6132365353114321)
Trevor Sutherland has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8665847814067802)
Trevor Sutherland has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7931059536445917)
Trevor Sutherland had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6893056096647525)
### Justin Scott
- mean: True (0.7826625131049049)
- motive: True (0.8652240590801695)
- opportunity: True (0.7826625131049049)

### Martin Simmons
- mean: False (0.16344541254791978)
- motive: False (0.17895590994908395)
- opportunity: False (0.2861692906637461)

### Stephen Kennelly
- mean: False (0.16995627411340153)
- motive: False (0.1666753892745816)
- opportunity: False (0.2568320060042667)

### Trevor Sutherland
- mean: False (0.1334152185932198)
- motive: False (0.2068940463554083)
- opportunity: False (0.3106943903352475)

The culprit is Justin Scott.
In fact, it is Trevor Sutherland.
## 5minutemystery-the-rock-star-mystery
Gorg is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7371581232960549)
Gorg has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8962513815714083)
Gorg has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9713473322135262)
Gorg had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9046505665674094)
Stu is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7505527730327083)
Stu has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8816149238192855)
Stu has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8966140749572745)
Stu had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8688267468984366)
The Neighborhood Burgler is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5983121871760707)
The Neighborhood Burgler has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7839884808423031)
The Neighborhood Burgler has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8647679145346777)
The Neighborhood Burgler had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7185944237486072)
Tina is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6406358487498992)
Tina has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8732147785405174)
Tina has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8947894610946939)
Tina had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8140528237853677)
### Gorg
- mean: True (0.8962513815714083)
- motive: True (0.9713473322135262)
- opportunity: True (0.9046505665674094)

### Stu
- mean: False (0.11838507618071448)
- motive: False (0.10338592504272548)
- opportunity: False (0.13117325310156336)

### The Neighborhood Burgler
- mean: False (0.2160115191576969)
- motive: False (0.13523208546532228)
- opportunity: False (0.28140557625139284)

### Tina
- mean: False (0.12678522145948257)
- motive: False (0.10521053890530607)
- opportunity: False (0.1859471762146323)

The culprit is Gorg.
In fact, it is Tina.
## 5minutemystery-ask-marthathe-arsonist
Keen Observer is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6654105788791005)
Keen Observer has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8910549899564296)
Keen Observer has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8723473540228537)
Keen Observer had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6808786440630326)
Minding My Own Business is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6943026818003076)
Minding My Own Business has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8879840376027315)
Minding My Own Business has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7170118721569225)
Minding My Own Business had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6654105788791005)
Scared Stiff is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
Map:  65%|██████▌   | 132/203 [48:21<27:02, 22.86s/ examples]Map:  66%|██████▌   | 133/203 [48:46<27:27, 23.53s/ examples]True (0.7185943809170431)
Scared Stiff has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8624675215861032)
Scared Stiff has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7918210572836727)
Scared Stiff had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6584175136252488)
Watchful Waiter is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.769080279275001)
Watchful Waiter has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9161096235973493)
Watchful Waiter has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.874934615163517)
Watchful Waiter had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7264255794048772)
### Keen Observer
- mean: False (0.10894501004357038)
- motive: False (0.12765264597714632)
- opportunity: False (0.31912135593696744)

### Minding My Own Business
- mean: False (0.11201596239726852)
- motive: False (0.2829881278430775)
- opportunity: False (0.3345894211208995)

### Scared Stiff
- mean: False (0.13753247841389682)
- motive: False (0.2081789427163273)
- opportunity: False (0.3415824863747512)

### Watchful Waiter
- mean: True (0.9161096235973493)
- motive: True (0.874934615163517)
- opportunity: True (0.7264255794048772)

The culprit is Watchful Waiter.
In fact, it is Watchful Waiter.
## 5minutemystery-fatal-computer-crash
Alex Redoff is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7074046739492601)
Alex Redoff has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8519527857346616)
Alex Redoff has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8428631416381634)
Alex Redoff had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7041601500399041)
Cheryl Compton is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7201714538416826)
Cheryl Compton has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9026095892260383)
Cheryl Compton has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9124361266596831)
Cheryl Compton had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.72951977676791)
Claire Denninger is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6688802830862913)
Claire Denninger has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.879146760693242)
Claire Denninger has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8529354946829077)
Claire Denninger had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7233095190955371)
Natalie Sampson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6020615685826383)
Natalie Sampson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8596637847360897)
Natalie Sampson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8895288719962232)
Natalie Sampson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6688802830862913)
### Alex Redoff
- mean: False (0.1480472142653384)
- motive: False (0.15713685836183655)
- opportunity: False (0.29583984996009594)

### Cheryl Compton
- mean: True (0.9026095892260383)
- motive: True (0.9124361266596831)
- opportunity: True (0.72951977676791)

### Claire Denninger
- mean: False (0.12085323930675795)
- motive: False (0.14706450531709225)
- opportunity: False (0.2766904809044629)

### Natalie Sampson
- mean: False (0.14033621526391027)
- motive: False (0.11047112800377679)
- opportunity: False (0.3311197169137087)

The culprit is Cheryl Compton.
In fact, it is Natalie Sampson.
## 5minutemystery-the-rob-club-murder-mystery
Al Gibson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.621540893468236)
Al Gibson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9582260855240093)
Al Gibson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8267117710471246)
Al Gibson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7690802105138688)
Johnny Woodward is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7041601500399041)
Johnny Woodward has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9492946258008691)
Johnny Woodward has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8278281666221954)
Johnny Woodward had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7745833916423246)
Ray Shields is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6926419789019715)
Ray Shields has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9196425103002197)
Ray Shields has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7431679939957333)
Ray Shields had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7170118721569225)
Map:  66%|██████▌   | 134/203 [49:11<27:35, 24.00s/ examples]Map:  67%|██████▋   | 135/203 [49:32<26:00, 22.95s/ examples]Tim Acord is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6584174547581384)
Tim Acord has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.958847105894029)
Tim Acord has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8740772044235984)
Tim Acord had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7813306496768853)
Watson Treadway is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7745833916423246)
Watson Treadway has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.95150405034956)
Watson Treadway has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8558511727823209)
Watson Treadway had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7994423454932595)
### Al Gibson
- mean: False (0.04177391447599066)
- motive: False (0.17328822895287543)
- opportunity: False (0.23091978948613123)

### Johnny Woodward
- mean: False (0.050705374199130904)
- motive: False (0.17217183337780462)
- opportunity: False (0.2254166083576754)

### Ray Shields
- mean: False (0.0803574896997803)
- motive: False (0.2568320060042667)
- opportunity: False (0.2829881278430775)

### Tim Acord
- mean: True (0.958847105894029)
- motive: True (0.8740772044235984)
- opportunity: True (0.7813306496768853)

### Watson Treadway
- mean: False (0.04849594965044002)
- motive: False (0.14414882721767908)
- opportunity: False (0.20055765450674046)

The culprit is Tim Acord.
In fact, it is Johnny Woodward.
## 5minutemystery-ask-marthathe-litterer
Concerned Neighbor is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9263037480179213)
Concerned Neighbor has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9445872321654378)
Concerned Neighbor has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9246876822649571)
Concerned Neighbor had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7905303264811482)
Confused Commuter is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8799743689174987)
Confused Commuter has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9420819287658885)
Confused Commuter has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9487276064711105)
Confused Commuter had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8244619332958376)
Perplexed Dog Walker is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8984105603938967)
Perplexed Dog Walker has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9433475737015985)
Perplexed Dog Walker has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9178934131644976)
Perplexed Dog Walker had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8499711693725173)
Smug in Suburbia is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9012274173198201)
Smug in Suburbia has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9477691649813238)
Smug in Suburbia has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9173026661190045)
Smug in Suburbia had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8624675215861032)
### Concerned Neighbor
- mean: False (0.05541276783456217)
- motive: False (0.07531231773504288)
- opportunity: False (0.20946967351885182)

### Confused Commuter
- mean: False (0.05791807123411152)
- motive: False (0.05127239352888946)
- opportunity: False (0.1755380667041624)

### Perplexed Dog Walker
- mean: False (0.056652426298401504)
- motive: False (0.08210658683550243)
- opportunity: False (0.15002883062748273)

### Smug in Suburbia
- mean: True (0.9477691649813238)
- motive: True (0.9173026661190045)
- opportunity: True (0.8624675215861032)

The culprit is Smug in Suburbia.
In fact, it is Smug in Suburbia.
## 5minutemystery-drama-queen
Alfred Cooper is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7924642605907138)
Alfred Cooper has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8652240590801695)
Alfred Cooper has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8169911556077801)
Alfred Cooper had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7416740115009234)
Isabelle Rogers is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7371581892031299)
Isabelle Rogers has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8723473540228537)
Isabelle Rogers has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8499711693725173)
Isabelle Rogers had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8278281049441929)
James Fennimore is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7826625131049049)
James Fennimore has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8255897702959807)
Map:  67%|██████▋   | 136/203 [49:56<26:16, 23.52s/ examples]Map:  67%|██████▋   | 137/203 [50:17<24:51, 22.60s/ examples]James Fennimore has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7879311977554747)
James Fennimore had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6757646168022439)
Madge Anderson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7431679939957333)
Madge Anderson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.918480215734292)
Madge Anderson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8489722037469682)
Madge Anderson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8322366416985943)
### Alfred Cooper
- mean: False (0.13477594091983047)
- motive: False (0.18300884439221987)
- opportunity: False (0.2583259884990766)

### Isabelle Rogers
- mean: False (0.12765264597714632)
- motive: False (0.15002883062748273)
- opportunity: False (0.1721718950558071)

### James Fennimore
- mean: False (0.17441022970401932)
- motive: False (0.2120688022445253)
- opportunity: False (0.32423538319775613)

### Madge Anderson
- mean: True (0.918480215734292)
- motive: True (0.8489722037469682)
- opportunity: True (0.8322366416985943)

The culprit is Madge Anderson.
In fact, it is James Fennimore.
## 5minutemystery-the-gourmet-mystery
Antoine is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8283841584202847)
Antoine has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8816148581338575)
Antoine has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8568122940392877)
Antoine had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8577681165234065)
Georges Monceau is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7356416038392981)
Georges Monceau has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8499711693725173)
Georges Monceau has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8122723669190336)
Georges Monceau had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8233283740192667)
Sally Horvats is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.85729086409805)
Sally Horvats has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9049869164790318)
Sally Horvats has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8633915828320894)
Sally Horvats had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8966140148346177)
Sam Wheeler is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8086723099497763)
Sam Wheeler has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8902942539348153)
Sam Wheeler has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8459424357871997)
Sam Wheeler had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8386797935187188)
### Antoine
- mean: False (0.11838514186614246)
- motive: False (0.14318770596071229)
- opportunity: False (0.14223188347659355)

### Georges Monceau
- mean: False (0.15002883062748273)
- motive: False (0.1877276330809664)
- opportunity: False (0.17667162598073327)

### Sally Horvats
- mean: True (0.9049869164790318)
- motive: True (0.8633915828320894)
- opportunity: True (0.8966140148346177)

### Sam Wheeler
- mean: False (0.10970574606518468)
- motive: False (0.15405756421280026)
- opportunity: False (0.1613202064812812)

The culprit is Sally Horvats.
In fact, it is Sally Horvats.
## 5minutemystery-the-potter-book-mystery
Alfred is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6020615685826383)
Alfred has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8031737798924701)
Alfred has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.833324548637899)
Alfred had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7592253761865491)
Ann is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6113819501087365)
Ann has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8428631416381634)
Ann has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9136765626055674)
Ann had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8407825844829613)
Rusty is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6531268925247615)
Rusty has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8778961263000082)
Rusty has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9396923783210908)
Rusty had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7592253761865491)
Uncle Ezra is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.752012620951268)
Uncle Ezra has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9319595674053855)
Map:  68%|██████▊   | 138/203 [50:45<26:15, 24.24s/ examples]Map:  68%|██████▊   | 139/203 [51:09<25:39, 24.05s/ examples]Uncle Ezra has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9089416847784234)
Uncle Ezra had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8719117627136385)
### Alfred
- mean: False (0.19682622010752993)
- motive: False (0.16667545136210105)
- opportunity: False (0.24077462381345094)

### Ann
- mean: False (0.15713685836183655)
- motive: False (0.0863234373944326)
- opportunity: False (0.15921741551703872)

### Rusty
- mean: False (0.12210387369999176)
- motive: False (0.06030762167890924)
- opportunity: False (0.24077462381345094)

### Uncle Ezra
- mean: True (0.9319595674053855)
- motive: True (0.9089416847784234)
- opportunity: True (0.8719117627136385)

The culprit is Uncle Ezra.
In fact, it is Uncle Ezra.
## 5minutemystery-death-in-the-office
Cynthia Peck is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7431679939957333)
Cynthia Peck has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.913058338092082)
Cynthia Peck has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7752646804088963)
Cynthia Peck had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.646013666311734)
Josh Kesler is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7662936378892937)
Josh Kesler has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8499711693725173)
Josh Kesler has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7556369876990674)
Josh Kesler had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6279512069990912)
Megan Brewer is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6039318499573872)
Megan Brewer has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7759445334082792)
Megan Brewer has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6976088896786037)
Megan Brewer had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5907791930117218)
Steve Ledbetter is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7490872087035162)
Steve Ledbetter has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8624675215861032)
Steve Ledbetter has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8175745039697023)
Steve Ledbetter had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6909762697651828)
### Cynthia Peck
- mean: False (0.08694166190791797)
- motive: False (0.2247353195911037)
- opportunity: False (0.35398633368826604)

### Josh Kesler
- mean: False (0.15002883062748273)
- motive: False (0.2443630123009326)
- opportunity: False (0.37204879300090876)

### Megan Brewer
- mean: False (0.22405546659172082)
- motive: False (0.3023911103213963)
- opportunity: False (0.40922080698827823)

### Steve Ledbetter
- mean: True (0.8624675215861032)
- motive: True (0.8175745039697023)
- opportunity: True (0.6909762697651828)

The culprit is Steve Ledbetter.
In fact, it is Megan Brewer.
## 5minutemystery-chief-inspector-japp-solves-a-case
Alan Harrison is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6531269509188588)
Alan Harrison has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7676898810056793)
Alan Harrison has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8428631416381634)
Alan Harrison had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7325918709325988)
Evelyn Johnston is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6842640081724978)
Evelyn Johnston has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.833324548637899)
Evelyn Johnston has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9086179121100144)
Evelyn Johnston had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8104788598666923)
George Smythe is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6601723415572317)
George Smythe has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.65489470935198)
George Smythe has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8705972382426559)
George Smythe had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7431679939957333)
Herbert Grosvenor is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.705785027818136)
Herbert Grosvenor has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7892336789711022)
Herbert Grosvenor has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9092645024391882)
Herbert Grosvenor had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8187367896794966)
### Alan Harrison
- mean: False (0.23231011899432075)
- motive: False (0.15713685836183655)
- opportunity: False (0.2674081290674012)

### Evelyn Johnston
- mean: True (0.833324548637899)
- motive: True (0.9086179121100144)
- opportunity: True (0.8104788598666923)

### George Smythe
- mean: False (0.34510529064802)
Map:  69%|██████▉   | 140/203 [51:31<24:48, 23.62s/ examples]Map:  69%|██████▉   | 141/203 [51:58<25:20, 24.52s/ examples]Map:  70%|██████▉   | 142/203 [52:15<22:45, 22.39s/ examples]- motive: False (0.1294027617573441)
- opportunity: False (0.2568320060042667)

### Herbert Grosvenor
- mean: False (0.2107663210288978)
- motive: False (0.09073549756081178)
- opportunity: False (0.1812632103205034)

The culprit is Evelyn Johnston.
In fact, it is Alan Harrison.
## 5minutemystery-who-stole-the-cavemans-dinner
Dinosaur is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7468781997658912)
Dinosaur has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9207896596153058)
Dinosaur has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9284088027271398)
Dinosaur had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8606036289596553)
Droo is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8624675215861032)
Droo has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8656789607733094)
Droo has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9235923286659299)
Droo had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9032942081209032)
Father is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6714705301843162)
Father has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7704647687904915)
Father has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8656789607733094)
Father had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
False (0.5638532418618873)
Monkeys is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5428633110863297)
Monkeys has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.832781310996106)
Monkeys has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7981867775042927)
Monkeys had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8116760258690822)
### Dinosaur
- mean: True (0.9207896596153058)
- motive: True (0.9284088027271398)
- opportunity: True (0.8606036289596553)

### Droo
- mean: False (0.1343210392266906)
- motive: False (0.07640767133407012)
- opportunity: False (0.09670579187909678)

### Father
- mean: False (0.22953523120950847)
- motive: False (0.1343210392266906)
- opportunity: False (0.5638532418618873)

### Monkeys
- mean: False (0.16721868900389403)
- motive: False (0.20181322249570732)
- opportunity: False (0.18832397413091784)

The culprit is Dinosaur.
In fact, it is Dinosaur.
## 5minutemystery-the-stolen-car-mystery
David Kelly is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6791786560103119)
David Kelly has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9489172681310486)
David Kelly has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8539127714046447)
David Kelly had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7956580548514487)
Donna Allen is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6451199006197486)
Donna Allen has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9066531077351827)
Donna Allen has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.815232454829111)
Donna Allen had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7690802105138688)
Larry Roberts is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7240905804783984)
Larry Roberts has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9190632712053527)
Larry Roberts has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8428631416381634)
Larry Roberts had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7683857617837733)
Nancy Lee is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7505527730327083)
Nancy Lee has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9268353022276509)
Nancy Lee has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8652240590801695)
Nancy Lee had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7853085971692302)
### David Kelly
- mean: True (0.9489172681310486)
- motive: True (0.8539127714046447)
- opportunity: True (0.7956580548514487)

### Donna Allen
- mean: False (0.0933468922648173)
- motive: False (0.184767545170889)
- opportunity: False (0.23091978948613123)

### Larry Roberts
- mean: False (0.0809367287946473)
- motive: False (0.15713685836183655)
- opportunity: False (0.23161423821622673)

### Nancy Lee
- mean: False (0.07316469777234913)
- motive: False (0.13477594091983047)
- opportunity: False (0.21469140283076982)

The culprit is David Kelly.
In fact, it is Donna Allen.
## 5minutemystery-the-straw-hat-theater-mysteriesfinal-curtain
Arthur Glendon is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7248702601920561)
Arthur Glendon has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.893681109060862)
Arthur Glendon has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8553685501761973)
Map:  70%|███████   | 143/203 [52:49<25:55, 25.93s/ examples]Map:  71%|███████   | 144/203 [53:08<23:15, 23.65s/ examples]Arthur Glendon had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.844921525814193)
Josh Whitehead is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7711548682745724)
Josh Whitehead has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8701565303520181)
Josh Whitehead has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9127477403975288)
Josh Whitehead had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8587185689177256)
Linda Eberlie is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7498207054286419)
Linda Eberlie has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9092645024391882)
Linda Eberlie has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8958875533219306)
Linda Eberlie had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8529354946829077)
Sam Watson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.726425644352388)
Sam Watson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8832359917473193)
Sam Watson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8674854614419002)
Sam Watson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.794384956668203)
Stella Marlowe is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6001883860246252)
Stella Marlowe has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8428631416381634)
Stella Marlowe has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7931059536445917)
Stella Marlowe had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7279754274224494)
### Arthur Glendon
- mean: False (0.10631889093913804)
- motive: False (0.14463144982380272)
- opportunity: False (0.155078474185807)

### Josh Whitehead
- mean: False (0.12984346964798188)
- motive: False (0.08725225960247118)
- opportunity: False (0.14128143108227442)

### Linda Eberlie
- mean: True (0.9092645024391882)
- motive: True (0.8958875533219306)
- opportunity: True (0.8529354946829077)

### Sam Watson
- mean: False (0.11676400825268074)
- motive: False (0.1325145385580998)
- opportunity: False (0.20561504333179703)

### Stella Marlowe
- mean: False (0.15713685836183655)
- motive: False (0.2068940463554083)
- opportunity: False (0.27202457257755064)

The culprit is Linda Eberlie.
In fact, it is Linda Eberlie.
## 5minutemystery-itheft
Lea Thompson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6859494535376744)
Lea Thompson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.861538171568877)
Lea Thompson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7138307731576955)
Lea Thompson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7310586002437232)
Rachel Vermeer is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7310586002437232)
Rachel Vermeer has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8633916342942395)
Rachel Vermeer has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7592253761865491)
Rachel Vermeer had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6671476389322356)
Shawn Ramos is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7732163648437078)
Shawn Ramos has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.879146760693242)
Shawn Ramos has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7446563751413027)
Shawn Ramos had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7534666630720156)
Shay Dulaney is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7662936378892937)
Shay Dulaney has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8969755785184792)
Shay Dulaney has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7606506318580792)
Shay Dulaney had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7386690954574974)
### Lea Thompson
- mean: False (0.13846182843112298)
- motive: False (0.2861692268423045)
- opportunity: False (0.26894139975627684)

### Rachel Vermeer
- mean: False (0.13660836570576051)
- motive: False (0.24077462381345094)
- opportunity: False (0.3328523610677644)

### Shawn Ramos
- mean: False (0.12085323930675795)
- motive: False (0.2553436248586973)
- opportunity: False (0.2465333369279844)

### Shay Dulaney
- mean: True (0.8969755785184792)
- motive: True (0.7606506318580792)
- opportunity: True (0.7386690954574974)

The culprit is Shay Dulaney.
In fact, it is Rachel Vermeer.
## 5minutemystery-the-punch-with-a-punch
Carole is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7739006258141444)
Carole has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.913058338092082)
Map:  71%|███████▏  | 145/203 [53:28<21:47, 22.54s/ examples]Map:  72%|███████▏  | 146/203 [53:48<20:53, 21.99s/ examples]Carole has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9127477403975288)
Carole had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8757869551856522)
Dan is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7704647687904915)
Dan has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8998277786460391)
Dan has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.913058338092082)
Dan had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.832781310996106)
Diane is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8499711693725173)
Diane has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.934155284694701)
Diane has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9433475737015985)
Diane had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9043130884593419)
Principal Whittenmeyer is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8413048399699521)
Principal Whittenmeyer has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9695556166618308)
Principal Whittenmeyer has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9491062747098069)
Principal Whittenmeyer had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8951566249612815)
### Carole
- mean: False (0.08694166190791797)
- motive: False (0.08725225960247118)
- opportunity: False (0.1242130448143478)

### Dan
- mean: False (0.10017222135396087)
- motive: False (0.08694166190791797)
- opportunity: False (0.16721868900389403)

### Diane
- mean: False (0.065844715305299)
- motive: False (0.056652426298401504)
- opportunity: False (0.09568691154065811)

### Principal Whittenmeyer
- mean: True (0.9695556166618308)
- motive: True (0.9491062747098069)
- opportunity: True (0.8951566249612815)

The culprit is Principal Whittenmeyer.
In fact, it is Carole.
## 5minutemystery-the-straw-hat-theater-mysteriesbox-office-nightmare
Basil Carmody is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5774953314585229)
Basil Carmody has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8679338050595715)
Basil Carmody has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7981867775042927)
Basil Carmody had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6531268925247615)
John Franklin is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5869964306477841)
John Franklin has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8714748565614324)
John Franklin has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7981867775042927)
John Franklin had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7549149897594328)
Lawrence Blake is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.65489470935198)
Lawrence Blake has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8577681165234065)
Lawrence Blake has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7718434926244166)
Lawrence Blake had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6706082735718226)
Martha Gilmont is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6433292707767855)
Martha Gilmont has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8688268116310761)
Martha Gilmont has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8080671968507699)
Martha Gilmont had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7185944237486072)
### Basil Carmody
- mean: False (0.13206619494042848)
- motive: False (0.20181322249570732)
- opportunity: False (0.3468731074752385)

### John Franklin
- mean: True (0.8714748565614324)
- motive: True (0.7981867775042927)
- opportunity: True (0.7549149897594328)

### Lawrence Blake
- mean: False (0.14223188347659355)
- motive: False (0.22815650737558335)
- opportunity: False (0.3293917264281774)

### Martha Gilmont
- mean: False (0.1311731883689239)
- motive: False (0.1919328031492301)
- opportunity: False (0.28140557625139284)

The culprit is John Franklin.
In fact, it is John Franklin.
## 5minutemystery-the-waffle-man-mystery
Larry is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6197014353942354)
Larry has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.873646672673131)
Larry has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8906751877407573)
Larry had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7718434926244166)
The Old Man is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6415346823638186)
The Old Man has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8311430212356835)
Map:  72%|███████▏  | 147/203 [54:15<21:50, 23.40s/ examples]Map:  73%|███████▎  | 148/203 [54:37<20:59, 22.90s/ examples]The Old Man has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8620035048683017)
The Old Man had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6876299924560524)
The Waffle Man is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.644225125126315)
The Waffle Man has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8019357965963964)
The Waffle Man has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8305941261447712)
The Waffle Man had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6959583025067009)
Vera is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6206216296838327)
Vera has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8587185689177256)
Vera has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8386797310322072)
Vera had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7879311977554747)
### Larry
- mean: True (0.873646672673131)
- motive: True (0.8906751877407573)
- opportunity: True (0.7718434926244166)

### The Old Man
- mean: False (0.1688569787643165)
- motive: False (0.13799649513169832)
- opportunity: False (0.3123700075439476)

### The Waffle Man
- mean: False (0.19806420340360364)
- motive: False (0.16940587385522876)
- opportunity: False (0.3040416974932991)

### Vera
- mean: False (0.14128143108227442)
- motive: False (0.16132026896779283)
- opportunity: False (0.2120688022445253)

The culprit is Larry.
In fact, it is Vera.
## 5minutemystery-the-sunday-school-tithe-mystery
Doc Bentson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7725306828324007)
Doc Bentson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9567959302164903)
Doc Bentson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6513548405484016)
Doc Bentson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7041601500399041)
Ellie Wilson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6825737331070684)
Ellie Wilson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9130583993174167)
Ellie Wilson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.5409238971378262)
Ellie Wilson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6627964381792564)
James Gant is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6361271113853048)
James Gant has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9158089733990905)
James Gant has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.5813030649269245)
James Gant had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6334102859975052)
Judy Gant is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5640984675176304)
Judy Gant has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8875949368741688)
Judy Gant has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.5097643762740132)
Judy Gant had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6992543888266708)
Waylon Marsh is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6740504984987916)
Waylon Marsh has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9092645024391882)
Waylon Marsh has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.5438324636094939)
Waylon Marsh had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5907792634380938)
### Doc Bentson
- mean: True (0.9567959302164903)
- motive: True (0.6513548405484016)
- opportunity: True (0.7041601500399041)

### Ellie Wilson
- mean: False (0.08694160068258328)
- motive: False (0.4590761028621738)
- opportunity: False (0.3372035618207436)

### James Gant
- mean: False (0.08419102660090949)
- motive: False (0.4186969350730755)
- opportunity: False (0.36658971400249485)

### Judy Gant
- mean: False (0.1124050631258312)
- motive: False (0.49023562372598684)
- opportunity: False (0.3007456111733292)

### Waylon Marsh
- mean: False (0.09073549756081178)
- motive: False (0.4561675363905061)
- opportunity: False (0.40922073656190616)

The culprit is Doc Bentson.
In fact, it is Waylon Marsh.
## 5minutemystery-the-straw-hat-theater-mysteriescasting-call
Alice Cartwright is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6808786440630326)
Alice Cartwright has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8799743689174987)
Alice Cartwright has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8255897702959807)
Alice Cartwright had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6757646168022439)
Arthur Glendon is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.802555560073231)
Map:  73%|███████▎  | 149/203 [54:58<20:10, 22.41s/ examples]Map:  74%|███████▍  | 150/203 [55:16<18:36, 21.06s/ examples]Arthur Glendon has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.903294268691502)
Arthur Glendon has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8261514850267767)
Arthur Glendon had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6926419789019715)
Janice Starling is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6834195192071987)
Janice Starling has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8606036289596553)
Janice Starling has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7806625377756776)
Janice Starling had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6688802830862913)
Sandra Buckingham is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7279754274224494)
Sandra Buckingham has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8679338697256817)
Sandra Buckingham has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8300437877296776)
Sandra Buckingham had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6352224318508648)
### Alice Cartwright
- mean: False (0.1200256310825013)
- motive: False (0.17441022970401932)
- opportunity: False (0.32423538319775613)

### Arthur Glendon
- mean: True (0.903294268691502)
- motive: True (0.8261514850267767)
- opportunity: True (0.6926419789019715)

### Janice Starling
- mean: False (0.13939637104034475)
- motive: False (0.21933746222432238)
- opportunity: False (0.3311197169137087)

### Sandra Buckingham
- mean: False (0.13206613027431835)
- motive: False (0.16995621227032243)
- opportunity: False (0.3647775681491352)

The culprit is Arthur Glendon.
In fact, it is Arthur Glendon.
## 5minutemystery-the-anonymous-bank-robber
Edward Cantrell is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6297746298200823)
Edward Cantrell has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8670357473609658)
Edward Cantrell has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.767689835247798)
Edward Cantrell had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6740504984987916)
Larry Brooks is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.580352018589158)
Larry Brooks has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8272706865691472)
Larry Brooks has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.686790355176806)
Larry Brooks had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5869964306477841)
Lester Barton is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6540113633452196)
Lester Barton has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9029524325377104)
Lester Barton has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7585105966624085)
Lester Barton had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7424217332471881)
Oscar Jordan is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.60859406896259)
Oscar Jordan has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8714748565614324)
Oscar Jordan has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7779753136455794)
Oscar Jordan had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7248703250005105)
### Edward Cantrell
- mean: False (0.13296425263903422)
- motive: False (0.232310164752202)
- opportunity: False (0.3259495015012084)

### Larry Brooks
- mean: False (0.17272931343085285)
- motive: False (0.313209644823194)
- opportunity: False (0.41300356935221594)

### Lester Barton
- mean: True (0.9029524325377104)
- motive: True (0.7585105966624085)
- opportunity: True (0.7424217332471881)

### Oscar Jordan
- mean: False (0.12852514343856758)
- motive: False (0.22202468635442063)
- opportunity: False (0.2751296749994895)

The culprit is Lester Barton.
In fact, it is Lester Barton.
## 5minutemystery-the-house-of-lies
Debra is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7154240000492645)
Debra has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9353465445225602)
Debra has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8891444205417208)
Debra had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8267117710471246)
Luke is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7193836000532381)
Luke has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9222025272167219)
Luke has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9114953293645017)
Luke had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.854884683810039)
Olivia is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.767689835247798)
Map:  74%|███████▍  | 151/203 [55:39<18:50, 21.74s/ examples]Map:  75%|███████▍  | 152/203 [56:03<19:02, 22.41s/ examples]Olivia has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9572777759716213)
Olivia has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9420819287658885)
Olivia had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9167081124681512)
The Butler is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7325918054337844)
The Butler has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9304582506719414)
The Butler has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8925625120974553)
The Butler had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8289388437432279)
### Debra
- mean: False (0.06465345547743984)
- motive: False (0.11085557945827917)
- opportunity: False (0.17328822895287543)

### Luke
- mean: False (0.07779747278327809)
- motive: False (0.08850467063549827)
- opportunity: False (0.14511531618996099)

### Olivia
- mean: True (0.9572777759716213)
- motive: True (0.9420819287658885)
- opportunity: True (0.9167081124681512)

### The Butler
- mean: False (0.06954174932805857)
- motive: False (0.1074374879025447)
- opportunity: False (0.1710611562567721)

The culprit is Olivia.
In fact, it is The Butler.
## 5minutemystery-the-straw-hat-theater-mysterieson-stage
Grace Upshaw is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6370308391245257)
Grace Upshaw has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.879146760693242)
Grace Upshaw has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8122724274380432)
Grace Upshaw had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7074046739492601)
Linda Grant is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7981867775042927)
Linda Grant has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8872045854516336)
Linda Grant has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9076402191395381)
Linda Grant had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7620701143808404)
Molly Trumbull is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6224592927728324)
Molly Trumbull has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.879146760693242)
Molly Trumbull has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8879840376027315)
Molly Trumbull had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6876299924560524)
Samantha Powers is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6740504382339836)
Samantha Powers has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9149009617112335)
Samantha Powers has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9346342066470359)
Samantha Powers had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7577943897558946)
### Grace Upshaw
- mean: False (0.12085323930675795)
- motive: False (0.18772757256195682)
- opportunity: False (0.2925953260507399)

### Linda Grant
- mean: False (0.11279541454836639)
- motive: False (0.09235978086046193)
- opportunity: False (0.23792988561915962)

### Molly Trumbull
- mean: False (0.12085323930675795)
- motive: False (0.11201596239726852)
- opportunity: False (0.3123700075439476)

### Samantha Powers
- mean: True (0.9149009617112335)
- motive: True (0.9346342066470359)
- opportunity: True (0.7577943897558946)

The culprit is Samantha Powers.
In fact, it is Grace Upshaw.
## 5minutemystery-canada-day
Little black-haired girl is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.644225125126315)
Little black-haired girl has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7969253675907205)
Little black-haired girl has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6926420201866519)
Little black-haired girl had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6388352560545881)
Redheaded woman is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6636689235052821)
Redheaded woman has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8469578019965)
Redheaded woman has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.5640984675176304)
Redheaded woman had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5234203246639862)
Stocky blonde man is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8092759828926619)
Stocky blonde man has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.920217993899809)
Stocky blonde man has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7786493288700866)
Stocky blonde man had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6825737331070684)
Map:  75%|███████▌  | 153/203 [56:22<17:52, 21.44s/ examples]Map:  76%|███████▌  | 154/203 [56:45<17:43, 21.70s/ examples]Tall bald man is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7279754274224494)
Tall bald man has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8820219652716884)
Tall bald man has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6261242000979097)
Tall bald man had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6315942370470465)
### Little black-haired girl
- mean: False (0.20307463240927948)
- motive: False (0.3073579798133481)
- opportunity: False (0.36116474394541187)

### Redheaded woman
- mean: False (0.15304219800350005)
- motive: False (0.4359015324823696)
- opportunity: False (0.47657967533601375)

### Stocky blonde man
- mean: True (0.920217993899809)
- motive: True (0.7786493288700866)
- opportunity: True (0.6825737331070684)

### Tall bald man
- mean: False (0.11797803472831159)
- motive: False (0.3738757999020903)
- opportunity: False (0.36840576295295346)

The culprit is Stocky blonde man.
In fact, it is Tall bald man.
## 5minutemystery-the-missing-communion-set
Allison Jordan is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
False (0.5234203246639862)
Allison Jordan has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7424217332471881)
Allison Jordan has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
False (0.5302364729224919)
Allison Jordan had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5774954003013352)
Heather Guse is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5195212821349473)
Heather Guse has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8238958672039278)
Heather Guse has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6893056096647525)
Heather Guse had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7217432334405754)
Janelle Herbst is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
False (0.5312093625105829)
Janelle Herbst has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8294919722593475)
Janelle Herbst has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6842640693504702)
Janelle Herbst had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6406358487498992)
Josh Darvin is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.705785027818136)
Josh Darvin has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8856314413364714)
Josh Darvin has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.64779823427608)
Josh Darvin had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7248702601920561)
Justin Paul is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6001883860246252)
Justin Paul has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.811078188867804)
Justin Paul has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.5009765005823875)
Justin Paul had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6343168082332088)
### Allison Jordan
- mean: False (0.2575782667528119)
- motive: False (0.5302364729224919)
- opportunity: False (0.42250459969866483)

### Heather Guse
- mean: False (0.17610413279607218)
- motive: False (0.3106943903352475)
- opportunity: False (0.27825676655942455)

### Janelle Herbst
- mean: False (0.17050802774065255)
- motive: False (0.31573593064952976)
- opportunity: False (0.3593641512501008)

### Josh Darvin
- mean: True (0.8856314413364714)
- motive: True (0.64779823427608)
- opportunity: True (0.7248702601920561)

### Justin Paul
- mean: False (0.18892181113219597)
- motive: False (0.4990234994176125)
- opportunity: False (0.3656831917667912)

The culprit is Josh Darvin.
In fact, it is Josh Darvin.
## 5minutemystery-who-stole-super-bowl-sunday
Aunt Mary is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7872777601997338)
Aunt Mary has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.943970619289785)
Aunt Mary has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9381240634192676)
Aunt Mary had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9427180278987515)
Phil is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7606506318580792)
Phil has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9053223122169206)
Phil has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9019206778000431)
Phil had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8824278665848695)
Rick is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7264255794048772)
Rick has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9475754509027036)
Rick has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8887587777822111)
Map:  76%|███████▋  | 155/203 [57:03<16:38, 20.80s/ examples]Map:  77%|███████▋  | 156/203 [57:22<15:40, 20.01s/ examples]Rick had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8899121304559661)
Uncle Charlie is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8365545874520802)
Uncle Charlie has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.972204327764203)
Uncle Charlie has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9564718616162037)
Uncle Charlie had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9651191233711941)
### Aunt Mary
- mean: False (0.056029380710215015)
- motive: False (0.06187593658073243)
- opportunity: False (0.057281972101248524)

### Phil
- mean: False (0.09467768778307939)
- motive: False (0.09807932219995685)
- opportunity: False (0.11757213341513051)

### Rick
- mean: False (0.052424549097296436)
- motive: False (0.11124122221778887)
- opportunity: False (0.11008786954403393)

### Uncle Charlie
- mean: True (0.972204327764203)
- motive: True (0.9564718616162037)
- opportunity: True (0.9651191233711941)

The culprit is Uncle Charlie.
In fact, it is Aunt Mary.
## 5minutemystery-the-cocktail-conundrum
Ian Fairbank is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8840392847025188)
Ian Fairbank has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.927099763868178)
Ian Fairbank has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.803173839733582)
Ian Fairbank had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7461389980806673)
Mr. Fairbank is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8899120707827096)
Mr. Fairbank has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9385759849623091)
Mr. Fairbank has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8705972382426559)
Mr. Fairbank had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7994422859301654)
Mr. Lewis Rhys is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8710367026584496)
Mr. Lewis Rhys has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.921357630313903)
Mr. Lewis Rhys has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8080671968507699)
Mr. Lewis Rhys had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.784649255215384)
Mrs. Fairbank is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9164093141890854)
Mrs. Fairbank has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9549844874375936)
Mrs. Fairbank has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8947894610946939)
Mrs. Fairbank had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7534665957068495)
### Ian Fairbank
- mean: False (0.07290023613182195)
- motive: False (0.19682616026641797)
- opportunity: False (0.2538610019193327)

### Mr. Fairbank
- mean: True (0.9385759849623091)
- motive: True (0.8705972382426559)
- opportunity: True (0.7994422859301654)

### Mr. Lewis Rhys
- mean: False (0.07864236968609695)
- motive: False (0.1919328031492301)
- opportunity: False (0.21535074478461602)

### Mrs. Fairbank
- mean: False (0.045015512562406435)
- motive: False (0.10521053890530607)
- opportunity: False (0.24653340429315052)

The culprit is Mr. Fairbank.
In fact, it is Mrs. Fairbank.
## 5minutemystery-the-gypsys-secret-numbers
Great Marchelli is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8524448242555318)
Great Marchelli has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9238675252821831)
Great Marchelli has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.936749461409047)
Great Marchelli had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9233161821369215)
Lorenzo is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8816148581338575)
Lorenzo has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9543079730970608)
Lorenzo has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9429286143036572)
Lorenzo had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9326989068252284)
Ringmaster is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.832781310996106)
Ringmaster has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.905322251510331)
Ringmaster has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.927887794449634)
Ringmaster had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.85729086409805)
Sheriff is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8370879874240941)
Sheriff has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8980534699860239)
Sheriff has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9343951361750445)
Map:  77%|███████▋  | 157/203 [57:42<15:28, 20.18s/ examples]Map:  78%|███████▊  | 158/203 [58:07<16:05, 21.46s/ examples]Sheriff had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8998277786460391)
### Great Marchelli
- mean: False (0.07613247471781692)
- motive: False (0.06325053859095298)
- opportunity: False (0.07668381786307854)

### Lorenzo
- mean: True (0.9543079730970608)
- motive: True (0.9429286143036572)
- opportunity: True (0.9326989068252284)

### Ringmaster
- mean: False (0.09467774848966903)
- motive: False (0.07211220555036602)
- opportunity: False (0.14270913590195)

### Sheriff
- mean: False (0.10194653001397613)
- motive: False (0.06560486382495545)
- opportunity: False (0.10017222135396087)

The culprit is Lorenzo.
In fact, it is Sheriff.
## 5minutemystery-its-gone
Abe is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6749080895533367)
Abe has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8311430212356835)
Abe has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8962513815714083)
Abe had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7356416038392981)
Lance is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6774740084332073)
Lance has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8365545874520802)
Lance has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8947894610946939)
Lance had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7248702601920561)
The Amazing Andrew is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6206215556999736)
The Amazing Andrew has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8289387819824735)
The Amazing Andrew has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8386797935187188)
The Amazing Andrew had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6601724005812412)
Zora the Magnificent is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6909762697651828)
Zora the Magnificent has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8774767496170098)
Zora the Magnificent has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9187722208906307)
Zora the Magnificent had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7853085971692302)
### Abe
- mean: False (0.1688569787643165)
- motive: False (0.10374861842859173)
- opportunity: False (0.2643583961607019)

### Lance
- mean: False (0.16344541254791978)
- motive: False (0.10521053890530607)
- opportunity: False (0.27512973980794386)

### The Amazing Andrew
- mean: False (0.1710612180175265)
- motive: False (0.1613202064812812)
- opportunity: False (0.33982759941875884)

### Zora the Magnificent
- mean: True (0.8774767496170098)
- motive: True (0.9187722208906307)
- opportunity: True (0.7853085971692302)

The culprit is Zora the Magnificent.
In fact, it is The Amazing Andrew.
## 5minutemystery-the-misers-hoard
Bob Parsons is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8582439976623328)
Bob Parsons has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9026095892260383)
Bob Parsons has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8539127714046447)
Bob Parsons had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6859494535376744)
John Entwhistle III is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8524448242555318)
John Entwhistle III has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9155072008980665)
John Entwhistle III has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7356416476869558)
John Entwhistle III had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7233095190955371)
Sam Greenway is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.85729086409805)
Sam Greenway has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9235922667342402)
Sam Greenway has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7512833387594996)
Sam Greenway had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6976088896786037)
Sarah Parsons is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7988153087356352)
Sarah Parsons has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8803863464576128)
Sarah Parsons has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7885831565209055)
Sarah Parsons had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6671476985798853)
### Bob Parsons
- mean: True (0.9026095892260383)
- motive: True (0.8539127714046447)
- opportunity: True (0.6859494535376744)

### John Entwhistle III
- mean: False (0.08449279910193352)
- motive: False (0.26435835231304416)
- opportunity: False (0.2766904809044629)

### Sam Greenway
- mean: False (0.07640773326575978)
- motive: False (0.2487166612405004)
- opportunity: False (0.3023911103213963)

### Sarah Parsons
- mean: False (0.11961365354238718)
- motive: False (0.2114168434790945)
- opportunity: False (0.3328523014201147)

The culprit is Bob Parsons.
Map:  78%|███████▊  | 159/203 [58:29<15:51, 21.63s/ examples]Map:  79%|███████▉  | 160/203 [58:41<13:29, 18.83s/ examples]Map:  79%|███████▉  | 161/203 [59:00<13:18, 19.01s/ examples]In fact, it is Sarah Parsons.
## 5minutemystery-the-cornfield-caper
Austin is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7549149897594328)
Austin has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8459424357871997)
Austin has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8887587777822111)
Austin had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8068525816617738)
Billy is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.862930180750016)
Billy has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8469578650997759)
Billy has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.91789335161495)
Billy had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8187367896794966)
Nick is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7981867775042927)
Nick has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8322366416985943)
Nick has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9142907234091052)
Nick had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7718434926244166)
### Austin
- mean: False (0.15405756421280026)
- motive: False (0.11124122221778887)
- opportunity: False (0.19314741833822624)

### Billy
- mean: True (0.8469578650997759)
- motive: True (0.91789335161495)
- opportunity: True (0.8187367896794966)

### Nick
- mean: False (0.16776335830140565)
- motive: False (0.08570927659089478)
- opportunity: False (0.22815650737558335)

The culprit is Billy.
In fact, it is Billy.
## 5minutemystery-a-stolen-future
Donna Blake is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7008948290825966)
Donna Blake has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8221891570741111)
Donna Blake has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7476159948304097)
Donna Blake had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6842640081724978)
George Wilson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5964331434971528)
George Wilson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8175745039697023)
George Wilson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7620700689579233)
George Wilson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7476159279883341)
Jeffery Sharp is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6242935037467142)
Jeffery Sharp has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8386797935187188)
Jeffery Sharp has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6791787167336184)
Jeffery Sharp had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5832033700118571)
Pete Thompson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6334102859975052)
Pete Thompson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8267117710471246)
Pete Thompson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7090191197769757)
Pete Thompson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7356416038392981)
### Donna Blake
- mean: False (0.1778108429258889)
- motive: False (0.25238400516959025)
- opportunity: False (0.3157359918275022)

### George Wilson
- mean: True (0.8175745039697023)
- motive: True (0.7620700689579233)
- opportunity: True (0.7476159279883341)

### Jeffery Sharp
- mean: False (0.1613202064812812)
- motive: False (0.3208212832663816)
- opportunity: False (0.41679662998814293)

### Pete Thompson
- mean: False (0.17328822895287543)
- motive: False (0.29098088022302426)
- opportunity: False (0.2643583961607019)

The culprit is George Wilson.
In fact, it is Jeffery Sharp.
## 5minutemystery-the-dirty-half-dozen
Bethany Knight is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8198933606225757)
Bethany Knight has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.911809923444246)
Bethany Knight has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.879146760693242)
Bethany Knight had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.789233749534095)
Joe Clark is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8661325012437474)
Joe Clark has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9429286143036572)
Joe Clark has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9362850185952675)
Joe Clark had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8116760258690822)
Sherry Fogle is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.854884620116169)
Map:  80%|███████▉  | 162/203 [59:29<15:03, 22.03s/ examples]Map:  80%|████████  | 163/203 [59:55<15:24, 23.11s/ examples]Sherry Fogle has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9390248079664695)
Sherry Fogle has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9336731438527403)
Sherry Fogle had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7476159279883341)
Tonya Muse is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8140528237853677)
Tonya Muse has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9429285510753684)
Tonya Muse has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9471859326465281)
Tonya Muse had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.821044090050916)
Wayne Clark is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8714748046174847)
Wayne Clark has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9294404371753803)
Wayne Clark has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.936749461409047)
Wayne Clark had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8210441512234701)
### Bethany Knight
- mean: False (0.08819007655575395)
- motive: False (0.12085323930675795)
- opportunity: False (0.21076625046590503)

### Joe Clark
- mean: False (0.05707138569634285)
- motive: False (0.06371498140473253)
- opportunity: False (0.18832397413091784)

### Sherry Fogle
- mean: False (0.06097519203353052)
- motive: False (0.06632685614725975)
- opportunity: False (0.2523840720116659)

### Tonya Muse
- mean: True (0.9429285510753684)
- motive: True (0.9471859326465281)
- opportunity: True (0.821044090050916)

### Wayne Clark
- mean: False (0.07055956282461973)
- motive: False (0.06325053859095298)
- opportunity: False (0.17895584877652992)

The culprit is Tonya Muse.
In fact, it is Wayne Clark.
## 5minutemystery-a-porsche-of-course
Amy Golden is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7634837587244478)
Amy Golden has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8719117627136385)
Amy Golden has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8661325012437474)
Amy Golden had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8187367896794966)
Frankie Cole is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8714749214913714)
Frankie Cole has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9304583061315765)
Frankie Cole has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9518632280135741)
Frankie Cole had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.892187358563457)
Jeremy Steele is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7648916137833577)
Jeremy Steele has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8354835531737983)
Jeremy Steele has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8906751877407573)
Jeremy Steele had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.720171518230031)
Lionel Jacobs is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7813306496768853)
Lionel Jacobs has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8856315007226893)
Lionel Jacobs has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8812065732757132)
Lionel Jacobs had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8509646659219744)
Susan Barker is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.854884683810039)
Susan Barker has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9015746123467522)
Susan Barker has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9133679254389228)
Susan Barker had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8558511727823209)
### Amy Golden
- mean: False (0.12808823728636154)
- motive: False (0.1338674987562526)
- opportunity: False (0.1812632103205034)

### Frankie Cole
- mean: True (0.9304583061315765)
- motive: True (0.9518632280135741)
- opportunity: True (0.892187358563457)

### Jeremy Steele
- mean: False (0.1645164468262017)
- motive: False (0.10932481225924273)
- opportunity: False (0.279828481769969)

### Lionel Jacobs
- mean: False (0.11436849927731074)
- motive: False (0.11879342672428683)
- opportunity: False (0.1490353340780256)

### Susan Barker
- mean: False (0.09842538765324782)
- motive: False (0.08663207456107724)
- opportunity: False (0.14414882721767908)

The culprit is Frankie Cole.
In fact, it is Frankie Cole.
## 5minutemystery-the-mystery-of-the-missing-story
Alex Rebmevon is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8333246107254184)
Alex Rebmevon has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9621076000160501)
Alex Rebmevon has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7813306496768853)
Map:  81%|████████  | 164/203 [1:00:16<14:30, 22.31s/ examples]Map:  81%|████████▏ | 165/203 [1:00:32<13:06, 20.69s/ examples]Alex Rebmevon had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7786493288700866)
Amy is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7256486384635821)
Amy has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9167080509980843)
Amy has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8104789202520752)
Amy had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7356416038392981)
Lucy is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6800292132037243)
Lucy has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9161096235973493)
Lucy has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7154239360853772)
Lucy had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7592253761865491)
Sarah is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6601724005812412)
Sarah has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8947895144283036)
Sarah has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7217432334405754)
Sarah had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7008948290825966)
### Alex Rebmevon
- mean: True (0.9621076000160501)
- motive: True (0.7813306496768853)
- opportunity: True (0.7786493288700866)

### Amy
- mean: False (0.08329194900191572)
- motive: False (0.18952107974792476)
- opportunity: False (0.2643583961607019)

### Lucy
- mean: False (0.08389037640265073)
- motive: False (0.28457606391462276)
- opportunity: False (0.24077462381345094)

### Sarah
- mean: False (0.10521048557169643)
- motive: False (0.27825676655942455)
- opportunity: False (0.2991051709174034)

The culprit is Alex Rebmevon.
In fact, it is Lucy.
## 5minutemystery-the-case-of-the-missing-friend
Billy Friend is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.615087855649269)
Billy Friend has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9152045868398637)
Billy Friend has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.5936092727363199)
Billy Friend had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6859494535376744)
Diana Scott is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5888891269161294)
Diana Scott has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9139841191734227)
Diana Scott has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.5660185351323219)
Diana Scott had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7662936378892937)
Harrell Garner is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
False (0.525368812147771)
Harrell Garner has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9173026661190045)
Harrell Garner has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
False (0.5019531141001669)
Harrell Garner had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7570766705324253)
Susan Allen is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
False (0.5019531141001669)
Susan Allen has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9331876642092066)
Susan Allen has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7074047371961694)
Susan Allen had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7606506998655483)
### Billy Friend
- mean: False (0.08479541316013628)
- motive: False (0.4063907272636801)
- opportunity: False (0.31405054646232555)

### Diana Scott
- mean: False (0.0860158808265773)
- motive: False (0.4339814648676781)
- opportunity: False (0.23370636211070628)

### Harrell Garner
- mean: False (0.08269733388099554)
- motive: False (0.5019531141001669)
- opportunity: False (0.24292332946757467)

### Susan Allen
- mean: True (0.9331876642092066)
- motive: True (0.7074047371961694)
- opportunity: True (0.7606506998655483)

The culprit is Susan Allen.
In fact, it is Diana Scott.
## 5minutemystery-sweat-it-out
Chris Henderson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6766198919456847)
Chris Henderson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8757870204368676)
Chris Henderson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8824278665848695)
Chris Henderson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8169911556077801)
Dave Perkins is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6976088896786037)
Dave Perkins has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9076401582775206)
Dave Perkins has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8587185689177256)
Map:  82%|████████▏ | 166/203 [1:00:51<12:26, 20.17s/ examples]Map:  82%|████████▏ | 167/203 [1:01:13<12:23, 20.65s/ examples]Dave Perkins had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8080671968507699)
Larry Douglas is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
False (0.5195213440667139)
Larry Douglas has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.789233749534095)
Larry Douglas has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7490872087035162)
Larry Douglas had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7209580648179327)
Nathan Elliott is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6406358487498992)
Nathan Elliott has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9145963810991447)
Nathan Elliott has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8428631416381634)
Nathan Elliott had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8438950825214144)
### Chris Henderson
- mean: False (0.12421297956313238)
- motive: False (0.11757213341513051)
- opportunity: False (0.18300884439221987)

### Dave Perkins
- mean: False (0.09235984172247935)
- motive: False (0.14128143108227442)
- opportunity: False (0.1919328031492301)

### Larry Douglas
- mean: False (0.21076625046590503)
- motive: False (0.2509127912964838)
- opportunity: False (0.2790419351820673)

### Nathan Elliott
- mean: True (0.9145963810991447)
- motive: True (0.8428631416381634)
- opportunity: True (0.8438950825214144)

The culprit is Nathan Elliott.
In fact, it is Chris Henderson.
## 5minutemystery-mystery-of-the-missing-heart
Eric Winter is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7025300310583819)
Eric Winter has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8933094122075369)
Eric Winter has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9056565771882901)
Eric Winter had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7154240000492645)
Jenny Jackson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7476159279883341)
Jenny Jackson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8568122940392877)
Jenny Jackson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9114953293645017)
Jenny Jackson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7969253675907205)
Jimmy Jackson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7248703250005105)
Jimmy Jackson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8719117627136385)
Jimmy Jackson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8879840376027315)
Jimmy Jackson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7826625131049049)
Wendy LaRue is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7577943897558946)
Wendy LaRue has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9155072554665495)
Wendy LaRue has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9224823132745662)
Wendy LaRue had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8080671968507699)
### Eric Winter
- mean: False (0.1066905877924631)
- motive: False (0.09434342281170993)
- opportunity: False (0.28457599995073546)

### Jenny Jackson
- mean: False (0.14318770596071229)
- motive: False (0.08850467063549827)
- opportunity: False (0.20307463240927948)

### Jimmy Jackson
- mean: False (0.12808823728636154)
- motive: False (0.11201596239726852)
- opportunity: False (0.21733748689509513)

### Wendy LaRue
- mean: True (0.9155072554665495)
- motive: True (0.9224823132745662)
- opportunity: True (0.8080671968507699)

The culprit is Wendy LaRue.
In fact, it is Eric Winter.
## 5minutemystery-stealing-second-base
Coach Joe Morgan is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7718434926244166)
Coach Joe Morgan has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9136765013387816)
Coach Joe Morgan has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8267118326419537)
Coach Joe Morgan had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7905303264811482)
Mary Thornton is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8056322290803791)
Mary Thornton has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.927887794449634)
Mary Thornton has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8596637206861489)
Mary Thornton had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8152325155686644)
Randy Newsom is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.833324548637899)
Randy Newsom has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9273633336539081)
Map:  83%|████████▎ | 168/203 [1:01:34<12:02, 20.65s/ examples]Map:  83%|████████▎ | 169/203 [1:01:57<12:08, 21.44s/ examples]Randy Newsom has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8933094122075369)
Randy Newsom had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8044059309478723)
Shorty Gilstrap is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8354835531737983)
Shorty Gilstrap has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9167080509980843)
Shorty Gilstrap has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8068526417769779)
Shorty Gilstrap had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8128673413132903)
### Coach Joe Morgan
- mean: False (0.08632349866121836)
- motive: False (0.1732881673580463)
- opportunity: False (0.20946967351885182)

### Mary Thornton
- mean: False (0.07211220555036602)
- motive: False (0.14033627931385106)
- opportunity: False (0.18476748443133562)

### Randy Newsom
- mean: True (0.9273633336539081)
- motive: True (0.8933094122075369)
- opportunity: True (0.8044059309478723)

### Shorty Gilstrap
- mean: False (0.08329194900191572)
- motive: False (0.1931473582230221)
- opportunity: False (0.1871326586867097)

The culprit is Randy Newsom.
In fact, it is Mary Thornton.
## 5minutemystery-murder-in-the-old-house
Bathroom is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6671476389322356)
Bathroom has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.883638264557296)
Bathroom has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6388352560545881)
Bathroom had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7931059536445917)
Bedroom of daughter, Anita Jensen is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.720171518230031)
Bedroom of daughter, Anita Jensen has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8844391689240307)
Bedroom of daughter, Anita Jensen has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7483522884503825)
Bedroom of daughter, Anita Jensen had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8370879874240941)
Bedroom of oldest son, Harry Jensen is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6495786332146115)
Bedroom of oldest son, Harry Jensen has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.847967740521315)
Bedroom of oldest son, Harry Jensen has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6714705702070799)
Bedroom of oldest son, Harry Jensen had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7683857617837733)
Bedroom of youngest son, Edward Jensen is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6370308391245257)
Bedroom of youngest son, Edward Jensen has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8529354946829077)
Bedroom of youngest son, Edward Jensen has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7185943809170431)
Bedroom of youngest son, Edward Jensen had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7490872087035162)
Master bedroom of Earl and Mildrid Jensen is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8031737798924701)
Master bedroom of Earl and Mildrid Jensen has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.91789335161495)
Master bedroom of Earl and Mildrid Jensen has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7386690954574974)
Master bedroom of Earl and Mildrid Jensen had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8795611817678315)
### Bathroom
- mean: False (0.116361735442704)
- motive: False (0.36116474394541187)
- opportunity: False (0.2068940463554083)

### Bedroom of daughter, Anita Jensen
- mean: False (0.11556083107596926)
- motive: False (0.2516477115496175)
- opportunity: False (0.16291201257590593)

### Bedroom of oldest son, Harry Jensen
- mean: False (0.15203225947868504)
- motive: False (0.3285294297929201)
- opportunity: False (0.23161423821622673)

### Bedroom of youngest son, Edward Jensen
- mean: False (0.14706450531709225)
- motive: False (0.2814056190829569)
- opportunity: False (0.2509127912964838)

### Master bedroom of Earl and Mildrid Jensen
- mean: True (0.91789335161495)
- motive: True (0.7386690954574974)
- opportunity: True (0.8795611817678315)

The culprit is Master bedroom of Earl and Mildrid Jensen.
In fact, it is Bathroom.
## 5minutemystery-the-chess-mystery
Father is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5136684743338078)
Father has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7634837587244478)
Father has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8615382357584752)
Father had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7956581141325956)
Greg is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5292633777076584)
Greg has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7994423454932595)
Greg has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
Map:  84%|████████▎ | 170/203 [1:02:17<11:30, 20.93s/ examples]Map:  84%|████████▍ | 171/203 [1:02:37<10:58, 20.57s/ examples]True (0.8633915828320894)
Greg had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7839884808423031)
Tina is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6001883144765984)
Tina has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9039744767757508)
Tina has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9284088027271398)
Tina had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8354835531737983)
Uncle Larry is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5851012033999957)
Uncle Larry has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.861538171568877)
Uncle Larry has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8962513815714083)
Uncle Larry had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8311430212356835)
### Father
- mean: False (0.23651624127555215)
- motive: False (0.1384617642415248)
- opportunity: False (0.20434188586740443)

### Greg
- mean: False (0.20055765450674046)
- motive: False (0.1366084171679106)
- opportunity: False (0.2160115191576969)

### Tina
- mean: True (0.9039744767757508)
- motive: True (0.9284088027271398)
- opportunity: True (0.8354835531737983)

### Uncle Larry
- mean: False (0.13846182843112298)
- motive: False (0.10374861842859173)
- opportunity: False (0.1688569787643165)

The culprit is Tina.
In fact, it is Greg.
## 5minutemystery-lost-stolen-and-found
John Beddington is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7394224480813394)
John Beddington has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9142907234091052)
John Beddington has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7969253675907205)
John Beddington had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8031737798924701)
Louisa Perry is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6859494535376744)
Louisa Perry has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.879146813094474)
Louisa Perry has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8116760258690822)
Louisa Perry had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7905303264811482)
Mary Ingram is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7341195403199204)
Mary Ingram has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9032942081209032)
Mary Ingram has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8006920257960423)
Mary Ingram had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.77729988964086)
Sarah Upton is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7122321792841629)
Sarah Upton has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8918110736745599)
Sarah Upton has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7918210572836727)
Sarah Upton had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8376200175313318)
### John Beddington
- mean: False (0.08570927659089478)
- motive: False (0.20307463240927948)
- opportunity: False (0.19682622010752993)

### Louisa Perry
- mean: False (0.12085318690552604)
- motive: False (0.18832397413091784)
- opportunity: False (0.20946967351885182)

### Mary Ingram
- mean: False (0.09670579187909678)
- motive: False (0.19930797420395774)
- opportunity: False (0.22270011035913995)

### Sarah Upton
- mean: True (0.8918110736745599)
- motive: True (0.7918210572836727)
- opportunity: True (0.8376200175313318)

The culprit is Sarah Upton.
In fact, it is Louisa Perry.
## 5minutemystery-the-chocolate-cupcake-caper
Geraldine is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
False (0.5389832197022594)
Geraldine has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7264255794048772)
Geraldine has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.5583269696343842)
Geraldine had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6876299924560524)
Julianna is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5583269696343842)
Julianna has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8354835531737983)
Julianna has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7512833387594996)
Julianna had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7138307093362539)
Luis is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6325027972911149)
Luis has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8238959285889558)
Luis has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.595492552580428)
Map:  85%|████████▍ | 172/203 [1:02:55<10:15, 19.86s/ examples]Map:  85%|████████▌ | 173/203 [1:03:16<10:03, 20.13s/ examples]Luis had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7563575572780217)
Mr. Bento is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6800292132037243)
Mr. Bento has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9108631007029255)
Mr. Bento has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7613610520273686)
Mr. Bento had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7866228249849953)
### Geraldine
- mean: False (0.2735744205951228)
- motive: False (0.4416730303656158)
- opportunity: False (0.3123700075439476)

### Julianna
- mean: False (0.1645164468262017)
- motive: False (0.2487166612405004)
- opportunity: False (0.2861692906637461)

### Luis
- mean: False (0.17610407141104423)
- motive: False (0.404507447419572)
- opportunity: False (0.24364244272197833)

### Mr. Bento
- mean: True (0.9108631007029255)
- motive: True (0.7613610520273686)
- opportunity: True (0.7866228249849953)

The culprit is Mr. Bento.
In fact, it is Geraldine.
## 5minutemystery-dead-mans-island
Grandpa is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6242935037467142)
Grandpa has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9358173616900589)
Grandpa has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9155072554665495)
Grandpa had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7988153087356352)
Grandpa's grandfather is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5292633777076584)
Grandpa's grandfather has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9241418261705818)
Grandpa's grandfather has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9053223122169206)
Grandpa's grandfather had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8587185689177256)
Lisa is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5525396910980834)
Lisa has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8832359917473193)
Lisa has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.884439109617765)
Lisa had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6893056096647525)
Mike is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7813306496768853)
Mike has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9249593046682986)
Mike has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9105454073245608)
Mike had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7416740778117503)
### Grandpa
- mean: False (0.06418263830994109)
- motive: False (0.08449274453345046)
- opportunity: False (0.20118469126436478)

### Grandpa's grandfather
- mean: True (0.9241418261705818)
- motive: True (0.9053223122169206)
- opportunity: True (0.8587185689177256)

### Lisa
- mean: False (0.11676400825268074)
- motive: False (0.11556089038223505)
- opportunity: False (0.3106943903352475)

### Mike
- mean: False (0.07504069533170143)
- motive: False (0.0894545926754392)
- opportunity: False (0.2583259221882497)

The culprit is Grandpa's grandfather.
In fact, it is Lisa.
## 5minutemystery-who-stole-the-rock-of-ages
Denise Hurst is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7217431689117048)
Denise Hurst has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8745065279415651)
Denise Hurst has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8638516611889259)
Denise Hurst had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8606036289596553)
Jim Gaigon is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6706082735718226)
Jim Gaigon has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8392075831473667)
Jim Gaigon has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.743912876509037)
Jim Gaigon had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7409249450892966)
Juan Carde is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6495786332146115)
Juan Carde has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7905302675820512)
Juan Carde has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7956581141325956)
Juan Carde had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7981867775042927)
Skye Smith is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5650587803792624)
Skye Smith has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7683857617837733)
Skye Smith has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.686790355176806)
Map:  86%|████████▌ | 174/203 [1:03:35<09:39, 19.99s/ examples]Map:  86%|████████▌ | 175/203 [1:03:55<09:21, 20.06s/ examples]Map:  87%|████████▋ | 176/203 [1:04:15<09:01, 20.04s/ examples]Skye Smith had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6723316913929156)
### Denise Hurst
- mean: True (0.8745065279415651)
- motive: True (0.8638516611889259)
- opportunity: True (0.8606036289596553)

### Jim Gaigon
- mean: False (0.16079241685263335)
- motive: False (0.25608712349096296)
- opportunity: False (0.2590750549107034)

### Juan Carde
- mean: False (0.20946973241794875)
- motive: False (0.20434188586740443)
- opportunity: False (0.20181322249570732)

### Skye Smith
- mean: False (0.23161423821622673)
- motive: False (0.313209644823194)
- opportunity: False (0.3276683086070844)

The culprit is Denise Hurst.
In fact, it is Juan Carde.
## 5minutemystery-all-washed-up
Captain Kildare is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7853085971692302)
Captain Kildare has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9257686153543061)
Captain Kildare has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8474634353311888)
Captain Kildare had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7786492592534148)
Latrisha Lanigan is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5078118305218892)
Latrisha Lanigan has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7759445334082792)
Latrisha Lanigan has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7439129430200341)
Latrisha Lanigan had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5525396910980834)
Mark Colson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6575384105121485)
Mark Colson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8255897087847518)
Mark Colson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6766198919456847)
Mark Colson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6095241271158658)
Marvin Fishback is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6757645563841816)
Marvin Fishback has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7577943897558946)
Marvin Fishback has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7424217332471881)
Marvin Fishback had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5983121871760707)
### Captain Kildare
- mean: True (0.9257686153543061)
- motive: True (0.8474634353311888)
- opportunity: True (0.7786492592534148)

### Latrisha Lanigan
- mean: False (0.22405546659172082)
- motive: False (0.2560870569799659)
- opportunity: False (0.44746030890191657)

### Mark Colson
- mean: False (0.1744102912152482)
- motive: False (0.3233801080543153)
- opportunity: False (0.3904758728841342)

### Marvin Fishback
- mean: False (0.24220561024410536)
- motive: False (0.2575782667528119)
- opportunity: False (0.4016878128239293)

The culprit is Captain Kildare.
In fact, it is Mark Colson.
## 5minutemystery-the-hidden-messenger
Jean is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8803863464576128)
Jean has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9652503733161137)
Jean has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9475753908928137)
Jean had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8918110736745599)
Marie is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7348812840309261)
Marie has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8872045854516336)
Marie has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8688267468984366)
Marie had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7759445334082792)
Molly is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7826624547920057)
Molly has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9022657265573043)
Molly has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8740772044235984)
Molly had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8227594449669557)
Smith is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7279754274224494)
Smith has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8601343603168419)
Smith has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8244619332958376)
Smith had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7185943809170431)
### Jean
- mean: True (0.9652503733161137)
- motive: True (0.9475753908928137)
- opportunity: True (0.8918110736745599)

### Marie
- mean: False (0.11279541454836639)
- motive: False (0.13117325310156336)
- opportunity: False (0.22405546659172082)

### Molly
- mean: False (0.0977342734426957)
- motive: False (0.12592279557640162)
- opportunity: False (0.17724055503304426)

### Smith
- mean: False (0.13986563968315813)
- motive: False (0.1755380667041624)
- opportunity: False (0.2814056190829569)

The culprit is Jean.
In fact, it is Smith.
## 5minutemystery-the-disappearing-dollhouse
Map:  87%|████████▋ | 177/203 [1:04:37<08:54, 20.55s/ examples]Map:  88%|████████▊ | 178/203 [1:05:01<09:01, 21.65s/ examples]Julia is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7641884666111024)
Julia has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9252299659402181)
Julia has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9286679635448885)
Julia had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.847967740521315)
Kyle is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6654105788791005)
Kyle has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8397339530959691)
Kyle has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.875361437979977)
Kyle had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7122321792841629)
Lucius is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6113820047705449)
Lucius has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8519527857346616)
Lucius has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8344068526674736)
Lucius had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7106283339569771)
Reg is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6601724005812412)
Reg has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8670357473609658)
Reg has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8529354946829077)
Reg had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7839884808423031)
### Julia
- mean: True (0.9252299659402181)
- motive: True (0.9286679635448885)
- opportunity: True (0.847967740521315)

### Kyle
- mean: False (0.1602660469040309)
- motive: False (0.12463856202002299)
- opportunity: False (0.28776782071583706)

### Lucius
- mean: False (0.1480472142653384)
- motive: False (0.1655931473325264)
- opportunity: False (0.2893716660430229)

### Reg
- mean: False (0.13296425263903422)
- motive: False (0.14706450531709225)
- opportunity: False (0.2160115191576969)

The culprit is Julia.
In fact, it is Reg.
## 5minutemystery-a-bear-a-dog-and-a-mystery
Mom is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7446563307563252)
Mom has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7416740115009234)
Mom has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8037905715242155)
Mom had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7839884808423031)
Old Mugger is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7446563751413027)
Old Mugger has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7799928701983835)
Old Mugger has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8300437258865985)
Old Mugger had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7799929399351836)
Orville is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7759445334082792)
Orville has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8643104392003704)
Orville has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8840392847025188)
Orville had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8489722037469682)
Taylor is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7090191197769757)
Taylor has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8958876133958744)
Taylor has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8906751877407573)
Taylor had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8499711693725173)
### Mom
- mean: False (0.2583259884990766)
- motive: False (0.1962094284757845)
- opportunity: False (0.2160115191576969)

### Old Mugger
- mean: False (0.22000712980161652)
- motive: False (0.16995627411340153)
- opportunity: False (0.2200070600648164)

### Orville
- mean: False (0.13568956079962957)
- motive: False (0.1159607152974812)
- opportunity: False (0.15102779625303175)

### Taylor
- mean: True (0.8958876133958744)
- motive: True (0.8906751877407573)
- opportunity: True (0.8499711693725173)

The culprit is Taylor.
In fact, it is Taylor.
## 5minutemystery-the-mystery-of-the-talented-cat
Edith is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6169358476670045)
Edith has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.91789335161495)
Edith has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8509646659219744)
Edith had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8577681165234065)
Joshua Sellers is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7745833916423246)
Map:  88%|████████▊ | 179/203 [1:05:23<08:36, 21.51s/ examples]Map:  89%|████████▊ | 180/203 [1:05:47<08:35, 22.41s/ examples]Joshua Sellers has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9643214942287215)
Joshua Sellers has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9418684262191025)
Joshua Sellers had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8976952440346371)
Muggles is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8333246107254184)
Muggles has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.962391318570921)
Muggles has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.95150405034956)
Muggles had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9477691649813238)
Rick is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6688802830862913)
Rick has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9314624659768579)
Rick has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.811078188867804)
Rick had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8558511090164419)
### Edith
- mean: False (0.08210664838505)
- motive: False (0.1490353340780256)
- opportunity: False (0.14223188347659355)

### Joshua Sellers
- mean: False (0.03567850577127851)
- motive: False (0.058131573780897505)
- opportunity: False (0.10230475596536293)

### Muggles
- mean: True (0.962391318570921)
- motive: True (0.95150405034956)
- opportunity: True (0.9477691649813238)

### Rick
- mean: False (0.06853753402314211)
- motive: False (0.18892181113219597)
- opportunity: False (0.1441488909835581)

The culprit is Muggles.
In fact, it is Edith.
## 5minutemystery-the-haunted-portrait
Jonathan Ingersoll is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7233094544266295)
Jonathan Ingersoll has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8128673413132903)
Jonathan Ingersoll has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.936749461409047)
Jonathan Ingersoll had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8322366416985943)
Lucille Cameron is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7325918054337844)
Lucille Cameron has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8529354311342636)
Lucille Cameron has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.934872446722342)
Lucille Cameron had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8386797935187188)
Marion Montgomery is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7041600870830834)
Marion Montgomery has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8080671968507699)
Marion Montgomery has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9294403817764149)
Marion Montgomery had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8175745039697023)
Teddy Auchinlech is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6842640081724978)
Teddy Auchinlech has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.815232454829111)
Teddy Auchinlech has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.879146760693242)
Teddy Auchinlech had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7969253675907205)
### Jonathan Ingersoll
- mean: False (0.1871326586867097)
- motive: False (0.06325053859095298)
- opportunity: False (0.16776335830140565)

### Lucille Cameron
- mean: True (0.8529354311342636)
- motive: True (0.934872446722342)
- opportunity: True (0.8386797935187188)

### Marion Montgomery
- mean: False (0.1919328031492301)
- motive: False (0.07055961822358514)
- opportunity: False (0.18242549603029767)

### Teddy Auchinlech
- mean: False (0.184767545170889)
- motive: False (0.12085323930675795)
- opportunity: False (0.20307463240927948)

The culprit is Lucille Cameron.
In fact, it is Jonathan Ingersoll.
## 5minutemystery-the-classic-automobile-mystery
Gary Riggs is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6842640081724978)
Gary Riggs has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.934155284694701)
Gary Riggs has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7170118721569225)
Gary Riggs had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7505527730327083)
Gerald "Doc" McCroy is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6057990946577705)
Gerald "Doc" McCroy has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8895288123486662)
Gerald "Doc" McCroy has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7520125537161032)
Gerald "Doc" McCroy had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7866228249849953)
Map:  89%|████████▉ | 181/203 [1:06:06<07:50, 21.37s/ examples]Map:  90%|████████▉ | 182/203 [1:06:32<07:55, 22.65s/ examples]Mike Benson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6261242000979097)
Mike Benson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9046505126460354)
Mike Benson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6688802830862913)
Mike Benson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6842640081724978)
Tommy Flowers is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.615087855649269)
Tommy Flowers has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9155072554665495)
Tommy Flowers has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.6723317515040557)
Tommy Flowers had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7371581892031299)
### Gary Riggs
- mean: False (0.065844715305299)
- motive: False (0.2829881278430775)
- opportunity: False (0.2494472269672917)

### Gerald "Doc" McCroy
- mean: True (0.8895288123486662)
- motive: True (0.7520125537161032)
- opportunity: True (0.7866228249849953)

### Mike Benson
- mean: False (0.09534948735396465)
- motive: False (0.3311197169137087)
- opportunity: False (0.3157359918275022)

### Tommy Flowers
- mean: False (0.08449274453345046)
- motive: False (0.32766824849594434)
- opportunity: False (0.2628418107968701)

The culprit is Gerald "Doc" McCroy.
In fact, it is Gerald "Doc" McCroy.
## 5minutemystery-rocks-and-feathers
Barley is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6187804294217345)
Barley has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7106282704218558)
Barley has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7662936378892937)
Barley had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7416740115009234)
Bertha is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.702530072932436)
Bertha has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8568122940392877)
Bertha has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8762112821835625)
Bertha had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8140528237853677)
Joseph is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6513548405484016)
Joseph has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7866228249849953)
Joseph has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8098781635062345)
Joseph had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7185943809170431)
Tom is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6976089520497016)
Tom has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8587185689177256)
Tom has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8140527631337082)
Tom had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.77729988964086)
### Barley
- mean: False (0.28937172957814417)
- motive: False (0.23370636211070628)
- opportunity: False (0.2583259884990766)

### Bertha
- mean: True (0.8568122940392877)
- motive: True (0.8762112821835625)
- opportunity: True (0.8140528237853677)

### Joseph
- mean: False (0.21337717501500475)
- motive: False (0.19012183649376546)
- opportunity: False (0.2814056190829569)

### Tom
- mean: False (0.14128143108227442)
- motive: False (0.18594723686629178)
- opportunity: False (0.22270011035913995)

The culprit is Bertha.
In fact, it is Tom.
## 5minutemystery-who-is-telling-the-truth
Bill Flowers is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7718435616326055)
Bill Flowers has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8454326959560526)
Bill Flowers has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.847967740521315)
Bill Flowers had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6992543888266708)
Jane Neal is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7826625131049049)
Jane Neal has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9187722824991111)
Jane Neal has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8902942539348153)
Jane Neal had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7911763836133219)
Jimmy Smith is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.745398395394548)
Jimmy Smith has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8454326959560526)
Jimmy Smith has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7592253761865491)
Jimmy Smith had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6057990946577705)
Larry Gerard is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.759938723019178)
Map:  90%|█████████ | 183/203 [1:06:57<07:52, 23.60s/ examples]Map:  91%|█████████ | 184/203 [1:07:17<07:04, 22.35s/ examples]Larry Gerard has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8376199551237796)
Larry Gerard has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.811078188867804)
Larry Gerard had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6513548405484016)
Paula Newsome is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7655933544531522)
Paula Newsome has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8824278665848695)
Paula Newsome has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.842345065078002)
Paula Newsome had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7154240000492645)
### Bill Flowers
- mean: False (0.15456730404394736)
- motive: False (0.15203225947868504)
- opportunity: False (0.3007456111733292)

### Jane Neal
- mean: True (0.9187722824991111)
- motive: True (0.8902942539348153)
- opportunity: True (0.7911763836133219)

### Jimmy Smith
- mean: False (0.15456730404394736)
- motive: False (0.24077462381345094)
- opportunity: False (0.3942009053422295)

### Larry Gerard
- mean: False (0.16238004487622038)
- motive: False (0.18892181113219597)
- opportunity: False (0.34864515945159835)

### Paula Newsome
- mean: False (0.11757213341513051)
- motive: False (0.157654934921998)
- opportunity: False (0.28457599995073546)

The culprit is Jane Neal.
In fact, it is Paula Newsome.
## 5minutemystery-ask-marthathe-identity-thief
Grace Means is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8267117710471246)
Grace Means has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9473810811508532)
Grace Means has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8558511727823209)
Grace Means had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8633916342942395)
Joan Colthrop is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7606506318580792)
Joan Colthrop has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9764905566616159)
Joan Colthrop has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8940517282497483)
Joan Colthrop had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9046505126460354)
Laura Parsons is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7248702601920561)
Laura Parsons has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9666631825345839)
Laura Parsons has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.897695304229796)
Laura Parsons had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9105453462677353)
Maybelle Johnson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7264255794048772)
Maybelle Johnson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9664104579001461)
Maybelle Johnson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8757870204368676)
Maybelle Johnson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8774767496170098)
### Grace Means
- mean: False (0.05261891884914682)
- motive: False (0.14414882721767908)
- opportunity: False (0.13660836570576051)

### Joan Colthrop
- mean: True (0.9764905566616159)
- motive: True (0.8940517282497483)
- opportunity: True (0.9046505126460354)

### Laura Parsons
- mean: False (0.03333681746541606)
- motive: False (0.10230469577020396)
- opportunity: False (0.08945465373226469)

### Maybelle Johnson
- mean: False (0.033589542099853875)
- motive: False (0.12421297956313238)
- opportunity: False (0.12252325038299017)

The culprit is Joan Colthrop.
In fact, it is Joan Colthrop.
## 5minutemystery-ask-marthathe-pickpocket
Johnny Anderson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7154239360853772)
Johnny Anderson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.7826625131049049)
Johnny Anderson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9304582506719414)
Johnny Anderson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7879311977554747)
Morris Emerson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7662936378892937)
Morris Emerson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8910549302065384)
Morris Emerson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9372107968415931)
Morris Emerson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.803173839733582)
Sarah Browne is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7520125537161032)
Sarah Browne has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8807970862580315)
Sarah Browne has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9425067301242699)
Map:  91%|█████████ | 185/203 [1:07:39<06:39, 22.18s/ examples]Map:  92%|█████████▏| 186/203 [1:07:55<05:49, 20.57s/ examples]Sarah Browne had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8529354311342636)
Tom Blankenship is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7634837587244478)
Tom Blankenship has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9073122726900733)
Tom Blankenship has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9394706502722077)
Tom Blankenship had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7981867775042927)
### Johnny Anderson
- mean: False (0.21733748689509513)
- motive: False (0.06954174932805857)
- opportunity: False (0.2120688022445253)

### Morris Emerson
- mean: False (0.10894506979346164)
- motive: False (0.06278920315840686)
- opportunity: False (0.19682616026641797)

### Sarah Browne
- mean: True (0.8807970862580315)
- motive: True (0.9425067301242699)
- opportunity: True (0.8529354311342636)

### Tom Blankenship
- mean: False (0.09268772730992669)
- motive: False (0.060529349727792336)
- opportunity: False (0.20181322249570732)

The culprit is Sarah Browne.
In fact, it is Tom Blankenship.
## 5minutemystery-diamond-deception
Horace is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8774767496170098)
Horace has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.920504331042629)
Horace has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8519527857346616)
Horace had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8479678036998373)
Jake is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8947894610946939)
Jake has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.936749461409047)
Jake has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.905989824801558)
Jake had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8714748565614324)
John is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8770562402180104)
John has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9556514027264735)
John has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8925625719484378)
John had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8757870204368676)
Lewis is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8697145551802641)
Lewis has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9458012588547495)
Lewis has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8991214023999228)
Lewis had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8697146199790504)
### Horace
- mean: False (0.07949566895737104)
- motive: False (0.1480472142653384)
- opportunity: False (0.15203219630016274)

### Jake
- mean: False (0.06325053859095298)
- motive: False (0.09401017519844201)
- opportunity: False (0.12852514343856758)

### John
- mean: True (0.9556514027264735)
- motive: True (0.8925625719484378)
- opportunity: True (0.8757870204368676)

### Lewis
- mean: False (0.05419874114525047)
- motive: False (0.10087859760007722)
- opportunity: False (0.13028538002094958)

The culprit is John.
In fact, it is Lewis.
## 5minutemystery-where-is-matthew
Andy's bedroom is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5964331434971528)
Andy's bedroom has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9594593035226332)
Andy's bedroom has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9133679254389228)
Andy's bedroom had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.94519740270931)
Matthew's bedroom is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
False (0.6187804294217345)
Matthew's bedroom has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9219217888198067)
Matthew's bedroom has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7950222460539826)
Matthew's bedroom had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9029524325377104)
The garage is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7476159279883341)
The garage has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9369805475192257)
The garage has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7483522884503825)
The garage had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7931059536445917)
The hall closet is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7394223819718238)
The hall closet has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9219217888198067)
The hall closet has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7333564224770464)
Map:  92%|█████████▏| 187/203 [1:08:15<05:25, 20.37s/ examples]Map:  93%|█████████▎| 188/203 [1:08:37<05:11, 20.77s/ examples]The hall closet had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7534666630720156)
The tree house is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7371581232960549)
The tree house has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9522199623739209)
The tree house has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7872777601997338)
The tree house had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8122724274380432)
### Andy's bedroom
- mean: True (0.9594593035226332)
- motive: True (0.9133679254389228)
- opportunity: True (0.94519740270931)

### Matthew's bedroom
- mean: False (0.07807821118019331)
- motive: False (0.20497775394601736)
- opportunity: False (0.0970475674622896)

### The garage
- mean: False (0.06301945248077434)
- motive: False (0.2516477115496175)
- opportunity: False (0.2068940463554083)

### The hall closet
- mean: False (0.07807821118019331)
- motive: False (0.26664357752295365)
- opportunity: False (0.2465333369279844)

### The tree house
- mean: False (0.047780037626079075)
- motive: False (0.21272223980026617)
- opportunity: False (0.18772757256195682)

The culprit is Andy's bedroom.
In fact, it is The tree house.
## 5minutemystery-the-mysterious-gift
CIndy is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7225270177274575)
CIndy has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8984105603938967)
CIndy has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8499711693725173)
CIndy had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7918210572836727)
Josie's mother is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6859494535376744)
Josie's mother has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8933094122075369)
Josie's mother has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8670357473609658)
Josie's mother had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7981867775042927)
Lester is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7248702601920561)
Lester has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8679338050595715)
Lester has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8606035648396906)
Lester had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7341195403199204)
Lorraine is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6460137433225688)
Lorraine has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8489722037469682)
Lorraine has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8175744430556572)
Lorraine had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6566582893190611)
### CIndy
- mean: False (0.10158943960610334)
- motive: False (0.15002883062748273)
- opportunity: False (0.2081789427163273)

### Josie's mother
- mean: True (0.8933094122075369)
- motive: True (0.8670357473609658)
- opportunity: True (0.7981867775042927)

### Lester
- mean: False (0.13206619494042848)
- motive: False (0.13939643516030942)
- opportunity: False (0.26588045968007956)

### Lorraine
- mean: False (0.15102779625303175)
- motive: False (0.18242555694434281)
- opportunity: False (0.3433417106809389)

The culprit is Josie's mother.
In fact, it is Lorraine.
## 5minutemystery-perry-mason-and-the-high-school-crush-murder
Morris Ingalls is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8278281666221954)
Morris Ingalls has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9270997017012965)
Morris Ingalls has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.91789335161495)
Morris Ingalls had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7950222460539826)
Randolph Johnson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7505527730327083)
Randolph Johnson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8824278665848695)
Randolph Johnson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8745065279415651)
Randolph Johnson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7008948290825966)
Sarah Conrad is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7732163648437078)
Sarah Conrad has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8947894610946939)
Sarah Conrad has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8891444205417208)
Sarah Conrad had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7446563751413027)
Tom Gooding is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.816406362162552)
Tom Gooding has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9302051049548884)
Map:  93%|█████████▎| 189/203 [1:09:07<05:28, 23.49s/ examples]Map:  94%|█████████▎| 190/203 [1:09:29<05:00, 23.12s/ examples]Tom Gooding has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9238675252821831)
Tom Gooding had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7981867775042927)
### Morris Ingalls
- mean: False (0.07290029829870348)
- motive: False (0.08210664838505)
- opportunity: False (0.20497775394601736)

### Randolph Johnson
- mean: False (0.11757213341513051)
- motive: False (0.12549347205843486)
- opportunity: False (0.2991051709174034)

### Sarah Conrad
- mean: False (0.10521053890530607)
- motive: False (0.11085557945827917)
- opportunity: False (0.2553436248586973)

### Tom Gooding
- mean: True (0.9302051049548884)
- motive: True (0.9238675252821831)
- opportunity: True (0.7981867775042927)

The culprit is Tom Gooding.
In fact, it is Morris Ingalls.
## 5minutemystery-who-stole-super-tuesday
Barry is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8376200175313318)
Barry has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8966140148346177)
Barry has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9331876642092066)
Barry had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8910549302065384)
Ricky Churrelo is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7866228249849953)
Ricky Churrelo has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8918110736745599)
Ricky Churrelo has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9331876642092066)
Ricky Churrelo had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8397339530959691)
Simon Knowles is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7170118721569225)
Simon Knowles has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8529354946829077)
Simon Knowles has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9092645024391882)
Simon Knowles had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8344069148356309)
Xavier Ericksen is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7114308541703346)
Xavier Ericksen has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8688268116310761)
Xavier Ericksen has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9207896596153058)
Xavier Ericksen had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8322366416985943)
### Barry
- mean: True (0.8966140148346177)
- motive: True (0.9331876642092066)
- opportunity: True (0.8910549302065384)

### Ricky Churrelo
- mean: False (0.10818892632544008)
- motive: False (0.06681233579079338)
- opportunity: False (0.1602660469040309)

### Simon Knowles
- mean: False (0.14706450531709225)
- motive: False (0.09073549756081178)
- opportunity: False (0.1655930851643691)

### Xavier Ericksen
- mean: False (0.1311731883689239)
- motive: False (0.07921034038469421)
- opportunity: False (0.16776335830140565)

The culprit is Barry.
In fact, it is Simon Knowles.
## 5minutemystery-the-missing-son
Caleb is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8169911556077801)
Caleb has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9678992614216547)
Caleb has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8832359917473193)
Caleb had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8210441512234701)
Conner is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7641883982873323)
Conner has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9687380774673213)
Conner has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8386797935187188)
Conner had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6808786440630326)
Jordan is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7248703250005105)
Jordan has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9556514632478168)
Jordan has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.794384956668203)
Jordan had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7154240000492645)
Kyle is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6992543888266708)
Kyle has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9537943000694998)
Kyle has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8278281666221954)
Kyle had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7446563307563252)
### Caleb
- mean: True (0.9678992614216547)
- motive: True (0.8832359917473193)
- opportunity: True (0.8210441512234701)

### Conner
- mean: False (0.031261922532678676)
- motive: False (0.1613202064812812)
- opportunity: False (0.31912135593696744)

### Jordan
- mean: False (0.0443485367521832)
- motive: False (0.20561504333179703)
- opportunity: False (0.28457599995073546)

### Kyle
- mean: False (0.046205699930500166)
- motive: False (0.17217183337780462)
Map:  94%|█████████▍| 191/203 [1:09:47<04:19, 21.62s/ examples]Map:  95%|█████████▍| 192/203 [1:10:07<03:51, 21.01s/ examples]Map:  95%|█████████▌| 193/203 [1:10:31<03:38, 21.87s/ examples]- opportunity: False (0.2553436692436748)

The culprit is Caleb.
In fact, it is Caleb.
## 5minutemystery-the-stolen-cupcake
Angelica is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5214711998972037)
Angelica has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8719117627136385)
Angelica has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7549149897594328)
Angelica had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6992543888266708)
Caedon is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5175709123121337)
Caedon has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8474634858439474)
Caedon has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7879311977554747)
Caedon had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6057990946577705)
Ross is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6306849707446135)
Ross has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8914335992201801)
Ross has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8714748565614324)
Ross had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.644225125126315)
Tony is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (1.3441128399883517)
Tony has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8652240590801695)
Tony has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8068526417769779)
Tony had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6619228115397798)
### Angelica
- mean: False (0.12808823728636154)
- motive: False (0.24508501024056717)
- opportunity: False (0.3007456111733292)

### Caedon
- mean: False (0.15253651415605263)
- motive: False (0.2120688022445253)
- opportunity: False (0.3942009053422295)

### Ross
- mean: True (0.8914335992201801)
- motive: True (0.8714748565614324)
- opportunity: True (0.644225125126315)

### Tony
- mean: False (0.13477594091983047)
- motive: False (0.1931473582230221)
- opportunity: False (0.33807718846022017)

The culprit is Ross.
In fact, it is Caedon.
## 5minutemystery-school-trip
Beth is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7859664553110391)
Beth has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8596637206861489)
Beth has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7592254214399092)
Beth had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7648916137833577)
Damon is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8289387819824735)
Damon has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8832359917473193)
Damon has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7431679939957333)
Damon had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.833324548637899)
Leo is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8289387819824735)
Leo has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9383503780077049)
Leo has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8402590129647053)
Leo had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8832359917473193)
Mr. Michael's is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6279512069990912)
Mr. Michael's has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9086179121100144)
Mr. Michael's has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8563323578093363)
Mr. Michael's had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8757869551856522)
The Seniors is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.776622945813876)
The Seniors has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9133679254389228)
The Seniors has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7074047371961694)
The Seniors had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8140528237853677)
### Beth
- mean: False (0.14033627931385106)
- motive: False (0.24077457856009077)
- opportunity: False (0.23510838621664232)

### Damon
- mean: False (0.11676400825268074)
- motive: False (0.2568320060042667)
- opportunity: False (0.16667545136210105)

### Leo
- mean: True (0.9383503780077049)
- motive: True (0.8402590129647053)
- opportunity: True (0.8832359917473193)

### Mr. Michael's
- mean: False (0.09138208788998559)
- motive: False (0.14366764219066375)
- opportunity: False (0.1242130448143478)

### The Seniors
- mean: False (0.08663207456107724)
- motive: False (0.29259526280383064)
- opportunity: False (0.1859471762146323)

The culprit is Leo.
In fact, it is The Seniors.
## 5minutemystery-arsonist-attack
Map:  96%|█████████▌| 194/203 [1:10:57<03:28, 23.11s/ examples]Jade Foster is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7279754274224494)
Jade Foster has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8606035648396906)
Jade Foster has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8864204283224634)
Jade Foster had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8774768149941248)
Jock Matt is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6406358487498992)
Jock Matt has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8679338697256817)
Jock Matt has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8596637206861489)
Jock Matt had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8459424357871997)
Madelyn Reader is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6791786560103119)
Madelyn Reader has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.874934615163517)
Madelyn Reader has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8947894610946939)
Madelyn Reader had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8723473540228537)
Max Crabgrass is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6757645563841816)
Max Crabgrass has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8984105603938967)
Max Crabgrass has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8606036289596553)
Max Crabgrass had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8872045854516336)
Security Guard is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7826625131049049)
Security Guard has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8933094122075369)
Security Guard has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8955227118091885)
Security Guard had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.847967740521315)
### Jade Foster
- mean: False (0.13939643516030942)
- motive: False (0.11357957167753663)
- opportunity: False (0.12252318500587522)

### Jock Matt
- mean: False (0.13206613027431835)
- motive: False (0.14033627931385106)
- opportunity: False (0.15405756421280026)

### Madelyn Reader
- mean: False (0.125065384836483)
- motive: False (0.10521053890530607)
- opportunity: False (0.12765264597714632)

### Max Crabgrass
- mean: True (0.8984105603938967)
- motive: True (0.8606036289596553)
- opportunity: True (0.8872045854516336)

### Security Guard
- mean: False (0.1066905877924631)
- motive: False (0.10447728819081148)
- opportunity: False (0.15203225947868504)

The culprit is Max Crabgrass.
In fact, it is Jade Foster.
## 5minutemystery-investigation-sabotager
Emma is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9449947479233238)
Emma has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9704647057482538)
Emma has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9257686705344172)
Emma had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9032942081209032)
Mary is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9142907234091052)
Mary has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9319595674053855)
Mary has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8848377441095496)
Mary had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8947894610946939)
Peter is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8558511090164419)
Peter has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9429286143036572)
Peter has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9155072554665495)
Peter had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9437636147996928)
Tim is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8092759828926619)
Tim has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8887587777822111)
Tim has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.897695304229796)
Tim had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8354835531737983)
Valerie is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8365545874520802)
Valerie has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9343951918693363)
Valerie has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8991214023999228)
Map:  96%|█████████▌| 195/203 [1:11:17<02:58, 22.30s/ examples]Map:  97%|█████████▋| 196/203 [1:11:37<02:30, 21.46s/ examples]Valerie had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8624675215861032)
### Emma
- mean: False (0.02953529425174617)
- motive: False (0.07423132946558275)
- opportunity: False (0.09670579187909678)

### Mary
- mean: False (0.06804043259461445)
- motive: False (0.11516225589045037)
- opportunity: False (0.10521053890530607)

### Peter
- mean: True (0.9429286143036572)
- motive: True (0.9155072554665495)
- opportunity: True (0.9437636147996928)

### Tim
- mean: False (0.11124122221778887)
- motive: False (0.10230469577020396)
- opportunity: False (0.1645164468262017)

### Valerie
- mean: False (0.06560480813066372)
- motive: False (0.10087859760007722)
- opportunity: False (0.13753247841389682)

The culprit is Peter.
In fact, it is Emma.
## 5minutemystery-the-presidential-smear-campaint-a-jacelyn-drew-mystery
Brittany is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7264255794048772)
Brittany has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9284088027271398)
Brittany has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9105454073245608)
Brittany had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.884439109617765)
Isis is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.687629930977143)
Isis has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.905989824801558)
Isis has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9314625284362855)
Isis had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8514594452543962)
Marie is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7106282704218558)
Marie has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9219218506394821)
Marie has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9086178579521682)
Marie had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8852352523606669)
Norma is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6740504382339836)
Norma has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8652240590801695)
Norma has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8338664756137771)
Norma had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8305941261447712)
### Brittany
- mean: True (0.9284088027271398)
- motive: True (0.9105454073245608)
- opportunity: True (0.884439109617765)

### Isis
- mean: False (0.09401017519844201)
- motive: False (0.06853747156371448)
- opportunity: False (0.1485405547456038)

### Marie
- mean: False (0.07807814936051793)
- motive: False (0.0913821420478318)
- opportunity: False (0.11476474763933309)

### Norma
- mean: False (0.13477594091983047)
- motive: False (0.16613352438622286)
- opportunity: False (0.16940587385522876)

The culprit is Brittany.
In fact, it is Isis.
## 5minutemystery-the-sunday-mystery
Jack Jackson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6791787167336184)
Jack Jackson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9329437018480795)
Jack Jackson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8958876133958744)
Jack Jackson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9196425103002197)
Jimmy Jackson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7240905157396584)
Jimmy Jackson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9574372776306425)
Jimmy Jackson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9196425651151865)
Jimmy Jackson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9149009617112335)
Jon Jackson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.767689835247798)
Jon Jackson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9553191057869168)
Jon Jackson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9249593046682986)
Jon Jackson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9265699426348812)
Maria Jackson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6943026818003076)
Maria Jackson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9676556581517683)
Maria Jackson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9210740952879496)
Maria Jackson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9403530352223053)
Spot is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.702530072932436)
Spot has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9597620378565557)
Spot has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9591543064115948)
Map:  97%|█████████▋| 197/203 [1:12:00<02:12, 22.03s/ examples]Map:  98%|█████████▊| 198/203 [1:12:18<01:43, 20.78s/ examples]Map:  98%|█████████▊| 199/203 [1:12:31<01:14, 18.51s/ examples]Spot had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9294404371753803)
### Jack Jackson
- mean: False (0.06705629815192049)
- motive: False (0.10411238660412558)
- opportunity: False (0.0803574896997803)

### Jimmy Jackson
- mean: False (0.04256272236935754)
- motive: False (0.0803574348848135)
- opportunity: False (0.08509903828876653)

### Jon Jackson
- mean: False (0.04468089421308319)
- motive: False (0.07504069533170143)
- opportunity: False (0.07343005736511876)

### Maria Jackson
- mean: False (0.03234434184823165)
- motive: False (0.07892590471205041)
- opportunity: False (0.05964696477769471)

### Spot
- mean: True (0.9597620378565557)
- motive: True (0.9591543064115948)
- opportunity: True (0.9294404371753803)

The culprit is Spot.
In fact, it is Spot.
## 5minutemystery-the-mystery-of-heritage
Jack Anderson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8311430212356835)
Jack Anderson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9796676632098326)
Jack Anderson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9238675252821831)
Jack Anderson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8370879874240941)
Jessica Anderson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8774768149941248)
Jessica Anderson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9820138217808033)
Jessica Anderson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9477691649813238)
Jessica Anderson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8864204283224634)
Martha Anderson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8714748565614324)
Martha Anderson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.981021999947924)
Martha Anderson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9414392129817035)
Martha Anderson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8864204283224634)
Mrs. Neil is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9334307932218529)
Mrs. Neil has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9751071938949272)
Mrs. Neil has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9619649048746262)
Mrs. Neil had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8615382357584752)
### Jack Anderson
- mean: False (0.020332336790167438)
- motive: False (0.07613247471781692)
- opportunity: False (0.16291201257590593)

### Jessica Anderson
- mean: True (0.9820138217808033)
- motive: True (0.9477691649813238)
- opportunity: True (0.8864204283224634)

### Martha Anderson
- mean: False (0.01897800005207595)
- motive: False (0.05856078701829648)
- opportunity: False (0.11357957167753663)

### Mrs. Neil
- mean: False (0.02489280610507283)
- motive: False (0.03803509512537384)
- opportunity: False (0.1384617642415248)

The culprit is Jessica Anderson.
In fact, it is Jessica Anderson.
## 5minutemystery-murder-of-the-actor
Bruce Whittingley is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.879146760693242)
Bruce Whittingley has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9575961815839735)
Bruce Whittingley has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9167080509980843)
Bruce Whittingley had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9230391966311572)
Marie Carloette is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8289388437432279)
Marie Carloette has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9520419225082909)
Marie Carloette has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8577681165234065)
Marie Carloette had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.929696145502287)
Mario Marcino is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8407825844829613)
Mario Marcino has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9477691649813238)
Mario Marcino has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9149009617112335)
Mario Marcino had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.897695304229796)
### Bruce Whittingley
- mean: True (0.9575961815839735)
- motive: True (0.9167080509980843)
- opportunity: True (0.9230391966311572)

### Marie Carloette
- mean: False (0.047958077491709106)
- motive: False (0.14223188347659355)
- opportunity: False (0.07030385449771304)

### Mario Marcino
- mean: False (0.0522308350186762)
- motive: False (0.08509903828876653)
- opportunity: False (0.10230469577020396)

The culprit is Bruce Whittingley.
In fact, it is Marie Carloette.
## 5minutemystery-another-hotel-murder
Dianne Shelby is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.787931139050028)
Dianne Shelby has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8092759828926619)
Dianne Shelby has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8828325273478573)
Map:  99%|█████████▊| 200/203 [1:12:52<00:57, 19.32s/ examples]Map:  99%|█████████▉| 201/203 [1:13:10<00:37, 18.79s/ examples]Dianne Shelby had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7008947664177184)
James Castro is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.5156199352405011)
James Castro has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.6654105788791005)
James Castro has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.7956581141325956)
James Castro had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.5926665645259142)
Kevin King is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.6406358487498992)
Kevin King has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8044059309478723)
Kevin King has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8504686406728537)
Kevin King had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.6976088896786037)
Roger Shelby is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8322366416985943)
Roger Shelby has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.854884683810039)
Roger Shelby has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8710367026584496)
Roger Shelby had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.7310585348819939)
### Dianne Shelby
- mean: False (0.1907240171073381)
- motive: False (0.11716747265214267)
- opportunity: False (0.2991052335822816)

### James Castro
- mean: False (0.3345894211208995)
- motive: False (0.20434188586740443)
- opportunity: False (0.40733343547408585)

### Kevin King
- mean: False (0.19559406905212773)
- motive: False (0.14953135932714634)
- opportunity: False (0.3023911103213963)

### Roger Shelby
- mean: True (0.854884683810039)
- motive: True (0.8710367026584496)
- opportunity: True (0.7310585348819939)

The culprit is Roger Shelby.
In fact, it is James Castro.
## 5minutemystery-the-missing-book
Brad is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8464508684792033)
Brad has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8891444205417208)
Brad has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8757869551856522)
Brad had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8820219652716884)
Fred is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
False (0.829538893640443)
Fred has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8745065279415651)
Fred has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.878314250659373)
Fred had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9121236203167563)
Mrs. Dunwoodee is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8848377441095496)
Mrs. Dunwoodee has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8349459127213729)
Mrs. Dunwoodee has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8381505623254643)
Mrs. Dunwoodee had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8906751280163339)
Ricky is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8000678954040312)
Ricky has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8879840376027315)
Ricky has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8402589628813668)
Ricky had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8824278665848695)
### Brad
- mean: False (0.11085557945827917)
- motive: False (0.1242130448143478)
- opportunity: False (0.11797803472831159)

### Fred
- mean: True (0.8745065279415651)
- motive: True (0.878314250659373)
- opportunity: True (0.9121236203167563)

### Mrs. Dunwoodee
- mean: False (0.16505408727862714)
- motive: False (0.16184943767453575)
- opportunity: False (0.10932487198366614)

### Ricky
- mean: False (0.11201596239726852)
- motive: False (0.1597410371186332)
- opportunity: False (0.11757213341513051)

The culprit is Fred.
In fact, it is Fred.
## 5minutemystery-the-necklace
Aunt Mary is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8944211616820568)
Aunt Mary has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.945399403620829)
Aunt Mary has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9433475737015985)
Aunt Mary had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.924959242644946)
Dad is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9001793304600783)
Dad has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.8879840376027315)
Dad has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8918110736745599)
Dad had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
Map: 100%|█████████▉| 202/203 [1:13:32<00:19, 19.65s/ examples]Map: 100%|██████████| 203/203 [1:13:58<00:00, 21.67s/ examples]Map: 100%|██████████| 203/203 [1:13:58<00:00, 21.87s/ examples]
True (0.9158089188126235)
Mom is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9073122726900733)
Mom has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9036349079321685)
Mom has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9015746123467522)
Mom had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9216402157401415)
Uncle Henry is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9121235591541035)
Uncle Henry has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9711290604274667)
Uncle Henry has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9606575369287865)
Uncle Henry had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.9593070162020048)
Uncle John is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.9095862487848758)
Uncle John has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9703525306286271)
Uncle John has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.9473810811508532)
Uncle John had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.950777887812089)
### Aunt Mary
- mean: False (0.05460059637917103)
- motive: False (0.056652426298401504)
- opportunity: False (0.075040757355054)

### Dad
- mean: False (0.11201596239726852)
- motive: False (0.10818892632544008)
- opportunity: False (0.0841910811873765)

### Mom
- mean: False (0.0963650920678315)
- motive: False (0.09842538765324782)
- opportunity: False (0.07835978425985846)

### Uncle Henry
- mean: True (0.9711290604274667)
- motive: True (0.9606575369287865)
- opportunity: True (0.9593070162020048)

### Uncle John
- mean: False (0.02964746937137286)
- motive: False (0.05261891884914682)
- opportunity: False (0.04922211218791095)

The culprit is Uncle Henry.
In fact, it is Dad.
## 5minutemystery-the-purloined-wallet
Bill Buchanan is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7813305798204846)
Bill Buchanan has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9392480858026054)
Bill Buchanan has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8757870204368676)
Bill Buchanan had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.789233749534095)
Carson Thomson is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8433797899747144)
Carson Thomson has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9405717864730483)
Carson Thomson has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.905989824801558)
Carson Thomson had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8679338697256817)
Cooper is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.8216173667955227)
Cooper has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.934872446722342)
Cooper has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8534247816107388)
Cooper had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8591918406281239)
David Nader is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.7853085971692302)
David Nader has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9066531077351827)
David Nader has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8820219652716884)
David Nader had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.794384956668203)
Vincent Garcia is guiltyConsider all the evidence and context from the story. Is this conclusion about guilt reasonable?
True (0.740174341079517)
Vincent Garcia has means to commit the crimeReflect on the resources and tools available to the suspect as described in the story. Does this suspect have the means necessary for the crime?
True (0.9376689781587124)
Vincent Garcia has motive for the crimeConsider the suspect's potential reasons and incentives as depicted in the story. Does this suggest a motive for committing the crime?
True (0.8582439976623328)
Vincent Garcia had the opportunity to commit the crimeAnalyze the timeline and the suspect's whereabouts as narrated in the story. Did this suspect have the opportunity to commit the crime?
True (0.8289388437432279)
### Bill Buchanan
- mean: False (0.06075191419739456)
- motive: False (0.12421297956313238)
- opportunity: False (0.21076625046590503)

### Carson Thomson
- mean: True (0.9405717864730483)
- motive: True (0.905989824801558)
- opportunity: True (0.8679338697256817)

### Cooper
- mean: False (0.06512755327765796)
- motive: False (0.14657521838926124)
- opportunity: False (0.14080815937187607)

### David Nader
- mean: False (0.0933468922648173)
- motive: False (0.11797803472831159)
- opportunity: False (0.20561504333179703)

### Vincent Garcia
- mean: False (0.06233102184128758)
- motive: False (0.14175600233766716)
- opportunity: False (0.1710611562567721)

The culprit is Carson Thomson.
In fact, it is David Nader.
Solved 55 out of 203.
