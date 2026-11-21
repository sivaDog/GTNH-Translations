# ja_JP forceload/betterquesting 未翻訳ブロック一覧

対象ファイル: `ja_JP/config/txloader/forceload/betterquesting/lang/ja_JP.lang`
生成日: 2026-11-20

## 検出方法

- `.name=` / `.desc=` の値にひらがな・カタカナ・漢字が1文字も含まれない行を「未翻訳」と判定。
- クエスト単位(コメント行+name+desc)でグルーピングし、name/descのどちらかでも未翻訳なら
  そのクエスト全体をブロックに含める。
- 空行を挟んでも直後のクエストが未翻訳なら同じブロックとして連結。翻訳済みクエストが
  1つでも間に挟まればブロックを区切る。
- 値が `[下書き]` で始まる場合は日本語を含んでいても未翻訳扱い(下書きは正式訳ではないため)。
- `# Quest:` 等のコメント行自体は判定対象外。表示では `Quest:` / `Quest Line:` 接頭辞を省略。
- `## Quest Line:` 単位を「章」として、各ブロックが属する章でグループ化。
- 翻訳確認は実機(2.9.0)のゲームインスタンスで行うが、翻訳作業はmaster側。
  個々のクエストのIDを2.9.0実機のクエストDBとmaster(GT-New-Horizons-Modpack)の
  クエストDBで突き合わせ、実機にのみ存在(masterで削除済み)のクエストは
  この資料から除外し、翻訳作業もしない(questlineは対象外)。

## 除外した誤検出(15件)

nameのみが未翻訳判定でdescは翻訳済み、かつnameが化学式・元素記号・Tier表記(`Tier N (XX)`)・
Mod名・本文中でも英語のまま使われる固有名詞など、翻訳不要と判断できるもの。

- L1000 C9H8O4...NaCl...H2O...
- L1108 LPG
- L1745 Tier 2 (MV)
- L1757 HCL
- L2038 Tier 3 (HV)
- L2438 NaK
- L2459 Tier 4 (EV)
- L4092 Tier 9 (UHV)
- L5222 Weed-EX
- L6503 Botany
- L6639 Carpenter's Blocks
- L10275 Applied Energistics
- L12186 Hardcore End(er) Expansion
- L14861 Better Questing?
- L15428 Trigger: Loot Game

## バージョン差異による除外(0件)

実機のクエストDBにのみ存在し、masterでは削除されているクエスト。
この資料には載せず、翻訳作業の対象にもしない。


## サマリー

- ファイル内の全クエスト/クエストライン数: 3860(誤検出・バージョン差異除外後 3845)
- 未翻訳率: 2031/3845 (53%)
  - うち `[下書き]` 表記(未訳扱い): 58件
- 連続ブロック数: 239

## 進捗(前回資料生成からの差分)

基準: 前回資料生成時点(2026-11-17) との比較。

- この基準以降に翻訳が完了したクエスト: 2件
- この基準以降に新規追加された未翻訳クエスト(フォーク元の更新等): 0件

翻訳完了したクエスト一覧:

- L11609 Smouldering
- L11829 Zinc

## 章ごとの未翻訳ブロック

### Tier 2 - MV時代  _(L1433)_ — 未翻訳率: 4/141 (3%)

- [ ] L1989-L2003 (4) Dislocator Inhibitor / String Theory? / Still No Filing in MV / Conduit Probe

### Tier 3 - HV時代  _(L2006)_ — 未翻訳率: 4/107 (4%)

- [ ] L2018-L2020 (1) Personal Dimension
- [ ] L2422-L2432 (3) Fluoro-who now? / Melting and Refreezing / Ender Fluid Conduits

### Tier 4 - EV時代  _(L2443)_ — 未翻訳率: 22/85 (26%)

- [ ] L2599-L2601 (1) HSS-G
- [ ] L2631-L2633 (1) One Dragon Egg is Not Enough Mr Bond
- [ ] L2639-L2669 (8) Ender Egg / Draconium Egg / Dragon Egg Omelet / Glass Fiber / Fiber Reinforced Epoxid Sheet / Empty Fiber Reinforced Glass Board … 他2件
- [ ] L2675-L2689 (4) Data Orbs / Create New Materials Out of Pure Energy / Critical Materials / What's in the Box?
- [ ] L2723-L2729 (2) Just Enough Tungstensteel For Your Rocket / Bigger Drums
- [ ] L2743-L2749 (2) Advanced Ilmenite Processing / Water, Fast
- [ ] L2767-L2781 (4) Niobium-Titanium / Four fluids in the one Hatch! / EV Field Generator / HV Field Generator

### Tier 5 - IV時代  _(L2788)_ — 未翻訳率: 126/131 (96%)

- [ ] L2792-L2810 (5) IV Field Generator / Tier 5 (IV) / On Your Way to Asteroids and Other Rocket Tier 3 DIMs / Callisto Trip / Europa Trip
- [ ] L2816-L2818 (1) IV Mixer
- [ ] L2824-L2934 (28) You're Gonna Hate This 5 and 6 in IV / Ceres Trip / Quantum Star / HSS-S / Argon / Your First Naquadah Ingot … 他22件
- [ ] L2940-L2962 (6) Quantum Supercomputer / Quantum Mainframe / Cheaper LV Circuits / On Your Way to Tier 4 DIMs / Mercury Trip / Venus Trip
- [ ] L2968-L3310 (86) IV Assembler / Palladium Processing / Platinum Group Processing - All the Other Metals / First Separation - Rhodium / Second Separation - Ruthenium / Re-Solving the Purity Issue … 他80件

### Tier 6 - LuV時代  _(L3313)_ — 未翻訳率: 75/78 (96%)

- [ ] L3317-L3351 (9) Netherite Scrap Seed / Dense Netherite Plate / Nefarious Production / Hot Netherite Scrap / Netherite Materials / Automated Mining … 他3件
- [ ] L3357-L3415 (15) Now You're Really Gonna Hate This 5 and 6 in LuV / Tier 6 (LuV) / Fluid TP for Magic-Haters / Thought Emitters Were Bad Enough? / Accelerating Things II / Accelerating Things III … 他9件
- [ ] L3421-L3623 (51) LuV Assembler / Assline Quest Updates / Panning For Gold is For Chumps / LuV Energy Hatch / Fetch Quests / Imprints, They're Important … 他45件

### Tier 7 - ZPM時代  _(L3626)_ — 未翻訳率: 50/66 (76%)

- [ ] L3630-L3636 (2) Prismatic Naquadah Composite Slurry / Prismatic Acid
- [ ] L3682-L3708 (7) Energy Infuser / Quantum Anomaly / Fusion Reactor MKII - Bigger, Better, Fusor / Making Americium / Learning Curve? Where We're Going There Are No Curves / The Beginning of the End Game … 他1件
- [ ] L3714-L3788 (19) You Can't Get Enough of This Pt 2 in ZPM / ZPM Superconductors (131,072 EU/t) / ZPM Field Generator / ZPM Assembler / ZPM Energy Hatch / Europium Doped Wafers … 他13件
- [ ] L3794-L3828 (9) Concentration / Recycle Trinium / Linear Accelerator / Refining / N.N.Q.Q.N.Q.Q / Purification … 他3件
- [ ] L3838-L3888 (13) Prismarine Recycling Pt. 2 / Prismarine Solution / Prismarine!? What Do I Need That For? / Prismatic Gas / Wormhole Generator / Naquarite Universal Insulator Foil … 他7件

### Tier 8 - UV時代  _(L3891)_ — 未翻訳率: 41/43 (95%)

- [ ] L3899-L4061 (41) I Put Fusion in Your Fusion so you Can Fusion While You Fusion / Time for Another Reactor / Americium Doped Wafers / Quantum Computer / Research Station / Maintenance Free At Last! … 他35件

### Tier 9 - UHV時代  _(L4064)_ — 未翻訳率: 29/33 (88%)

- [ ] L4068-L4074 (2) Draconic Core / Wyvern Core
- [ ] L4080-L4090 (3) Infinite Vis Storage, kinda? / Infinite Oxygen Tank / Misc Endgame Goals
- [ ] L4104-L4198 (24) UHV Superconductors (2,097,152 EU/t) / UHV Field Generator / UHV Energy Hatch / Assembling Living Circuits / The Final Frontier? / It's Not Going Bad, I Swear! … 他18件

### Tier 10 - UEV時代  _(L4201)_ — 未翻訳率: 53/55 (96%)

- [ ] L4205-L4263 (15) Capturing Light on a Circuit Board / Stopping the Infinity Bleed / My Eyes Hurt! #2 / NAC™: Advanced Routing Package / NAC™: Fundamentals Package / Awakened Core … 他9件
- [ ] L4269-L4419 (38) Longbow of the Heavens / My Eyes Hurt! #4 / Tesseract / Dragonblood / Metastable Oganesson / Infinity Boots … 他32件

### Tier 11 - UIV時代  _(L4422)_ — 未翻訳率: 46/47 (98%)

- [ ] L4426-L4608 (46) Bending Space and Time / Quantum Tank X / Heliofusion Exoticizer / A Fork in The Road / Tunnels Of Light / Dyson Swarm Modules … 他40件

### Tier 12 - UMV時代  _(L4611)_ — 未翻訳率: 44/45 (98%)

- [ ] L4615-L4789 (44) T4: Advanced / Finally, Universium! / Wireless Multi-Amp Hatches / Magnetohydrodynamically Constrained Star Matter / Guzzling Massive Amounts of Gas / UMV Energy Hatch … 他38件

### エンドゲーム - ゴール  _(L4792)_ — 未翻訳率: 29/30 (97%)

- [ ] L4796-L4910 (29) A Universe In Your Drives / MAX Circuits / Strings Upon Strings Upon Strings Upon- / Tier 13 (UXV) / The Door to Heaven? / Stargate Ring Block … 他23件

### 自給自足  _(L4913)_ — 未翻訳率: 8/48 (17%)

- [ ] L5025-L5027 (1) Dezil's Marshmallow
- [ ] L5049-L5063 (4) Really OP Food / Uncooked Slush / Glowing Marshmallow / Cooling Your Marshmallow
- [ ] L5097-L5108 (3) A Magical Lunchbox? / Ice Ice Baby / The Green Revolution

### 緑の革命  _(L5106)_ — 未翻訳率: 1/163 (1%)

- [ ] L5366-L5368 (1) Platina

### 旅に出かけよう...  _(L5765)_ — 未翻訳率: 24/65 (37%)

- [ ] L5769-L5771 (1) Indestructible Vessel
- [ ] L5777-L5779 (1) Relocator
- [ ] L5813-L5815 (1) Advanced Electric Jetpack
- [ ] L5909-L5911 (1) Travelocity!
- [ ] L5917-L5927 (3) Angel Wings / Secret-Angel-Assassin / Angel Wings - Ultra Force!
- [ ] L5945-L5979 (9) Better Boots with a little pizzazz / Walk all over you / Walking across the stars / Flying Like....Mary Poppins? / Flying With the Greatest of Ease / Working While Flying? … 他3件
- [ ] L5985-L6011 (7) Travelocity² / Let's Go Lava Surfing! / Enhanced Charm of Dislocation / Charm of Dislocation / Planar Gateways / Chaos Locator … 他1件
- [ ] L6021-L6023 (1) Spare Battery

### ...死ぬことなしに  _(L6026)_ — 未翻訳率: 28/99 (28%)

- [ ] L6034-L6044 (3) Protect Your Base: Tier 4 / Make Love, Not War / Why Grenades...
- [ ] L6054-L6068 (4) Protect Your Base: Tier 5 / Turret Base Tier 5 / PewPew! / Railguns, What Else
- [ ] L6094-L6096 (1) Luke, I'm Your Father
- [ ] L6102-L6116 (4) Protect Your Base: Tier 2 / Tier 2 Turret Base / Sometimes, a Bullet Will Do / Burn Them. Burn Them All!
- [ ] L6122-L6140 (5) Protect Your Base: Tier 3 / Tier 3 Base / This is Relatively Useful / Fire in the Hole / Turret Base Tier 4
- [ ] L6206-L6212 (2) Dark Steel Armor Basic Upgrades / Dark Steel Armor Advanced Upgrades
- [ ] L6270-L6292 (6) Nano Goggles / Quantum Goggles / Goggles > 9000 / Compressed Steel Armor / Compressed Desh Armor / Compressed Titanium Armor
- [ ] L6382-L6384 (1) Eldritch Striders
- [ ] L6390-L6392 (1) Apprentice Striders
- [ ] L6402-L6404 (1) Archmage Striders

### キッチリ基地を建築  _(L6423)_ — 未翻訳率: 31/83 (37%)

- [ ] L6427-L6429 (1) Let it Glow!
- [ ] L6435-L6441 (2) Barrel Upgrades / Texturing made easy
- [ ] L6599-L6605 (2) Lighting Up a Large Area, Without Electricity / Lighting Up a Large Area, With Electricity
- [ ] L6611-L6613 (1) BetterIO?
- [ ] L6647-L6673 (7) Excavation Upgrade / Crystal Shulker Box / Let's get Building! / Chests Had Quite the Glow-up! / Obsidian Barrel / Obsidian Shulker Box … 他1件
- [ ] L6679-L6681 (1) Iron Shulker Box
- [ ] L6687-L6725 (10) Gotta Go Fast! / Gold Shulker Box / Finally, Some Real Power! / Shulker Upgrades / Diamond Shulker Box / Advanced Concrete Backfiller … 他4件
- [ ] L6731-L6757 (7) Cooper's Mallet / Advanced Filing Cabinet / Marking Your Base / Silver Shulker Box / Draconic Chest / Concrete Backfiller … 他1件

### Forestryとマルチファーム  _(L6764)_ — 未翻訳率: 21/68 (31%)

- [ ] L6768-L6772 (1) THE RAINMAKER
- [ ] L6790-L6806 (3) The Multifarm / Farm Logic / Changing Your Foresty Circuit Configuration
- [ ] L6816-L6856 (7) Multifarm: Hatch / Multifarm: Valve / Multifarm: Control / Multifarm: Gearbox / Enhanced Farm Logic / Refined Farm Logic … 他1件
- [ ] L6874-L6878 (1) Copper, Tin, Bronze Tubes
- [ ] L6886-L6896 (2) Rubberised, Obsidian, Lapis Tubes / Blazing, Ender, Emerald Tubes
- [ ] L6910-L6932 (4) Another Path to Ethanol / Why No, This is Not Fit For Human Consumption / Better Fermenter Outputs / Such Pretty Leaves...
- [ ] L6938-L6942 (1) Seeing the Fruits of Your Labor
- [ ] L6956-L6958 (1) Speak For the Trees
- [ ] L7008-L7012 (1) U-238 Tu-Wait, Seriously?

### マルチブロックの旅  _(L7079)_ — 未翻訳率: 65/118 (55%)

- [ ] L7083-L7089 (2) Distill the Atmosphere / Collision Course
- [ ] L7151-L7161 (3) An Industrial Mobfarm / Powderbarrels / TNT
- [ ] L7203-L7205 (1) Let's Get Crackin!
- [ ] L7227-L7245 (5) Still Not Enough Charcoal? / It's Time to Get More Steam / Steam is Never Enough / Moooooore Steam / Even More Steam? Are You Sure?
- [ ] L7251-L7257 (2) A Very Useful Scanner / The 'Water Problems' Are Solved
- [ ] L7263-L7281 (5) Assembly Line / Data Access Hatches / Time to Drill For Ore! / Thermal Boiler - Lava you long time / Electrum Flux Coil Upgrade
- [ ] L7291-L7293 (1) Helium is Not Just for Balloons
- [ ] L7299-L7345 (12) Playing With the Big Boys, Chemically / Better Glass Upgrade, EV Glass / IV Glass / LuV Glass / ZPM Glass / UV Glass … 他6件
- [ ] L7355-L7361 (2) Getting Muddy With Monazite / Dissolution Tank
- [ ] L7375-L7385 (3) Neutron Activator / Neutron Sensor / Neutron Accelerator
- [ ] L7403-L7425 (6) Focusing Science and Mystery / Catalyzing Miracles / Tier 2 Shielding / Tier 3 Shielding / Tier 4 Shielding / Too much Indium?
- [ ] L7431-L7465 (9) Eternal Coil Upgrade / Algae Pond / Tier 2 Manipulating / A Beginner's Guide to Particle Physics / Producing Solar Panels in BULK!! / Synchrotron (No Relation to the Catalyst) … 他3件
- [ ] L7471-L7493 (6) Don't ask how this works / Decay Warehouse / Don't Lose That Multiblock Miner! / Using That Algae / A Little More Sigma (Squared) / No More (IC) Engraving
- [ ] L7503-L7509 (2) Filtered Beamline Output Hatch / Component Assembly Line
- [ ] L7519-L7521 (1) Drones are not Drones!
- [ ] L7531-L7549 (5) Draconic Development / One Fluid Tank to Store it All!! / Tier 4 Manipulating / Tier 3 Manipulating / More Algae Uses

### 大量処理  _(L7552)_ — 未翻訳率: 57/66 (86%)

- [ ] L7560-L7690 (33) Big Beautiful Brewery / This Kinda Burns... / Mass Processing at UV and Beyond! / Fits The Mold / T2 Maceration Stack / Smelt All The Things Stack-Wise... … 他27件
- [ ] L7696-L7714 (5) MABS / Another Chemical Multiblock? / Mass Processing in LuV / Clean Implosions?! / Extraction Point
- [ ] L7720-L7734 (4) Insane Voltage Multiblocks / L.A.T.E.X. Cable Coater / The Form of the Former Former: Reformed / See You Lather
- [ ] L7744-L7790 (12) Taking Things Apart / Advanced Assembly Line / Advanced Autoclaving / Megalomania / ...With The Power of Science! / You've Gotta Keep 'Em Separated … 他6件
- [ ] L7796-L7798 (1) Thermic Heating Device
- [ ] L7804-L7810 (2) Engraving With Style / Extreme Voltage Multiblocks

### 発電方法のハウ・トゥー  _(L7817)_ — 未翻訳率: 120/137 (88%)

- [ ] L7821-L7835 (4) Marie Curium? / XL Turbo Steam Turbine / Calcium Bottlenecking / Portable Clean Energy IV
- [ ] L7857-L7927 (18) Power of the Sun at MV Level / Power of the Sun 1x1 MV / Power of the Sun at HV Level / Power of the Sun 1x1 HV / We Need Big Toys / Power of the Sun at LV Level … 他12件
- [ ] L7933-L7955 (6) What Was That? I Can't Hear You Over the Engine! / Power of the Sun at EV Level / Power of the Sun 1x1 EV / Power of the Sun at IV Level / Power of the Sun 1x1 IV / Do You Hear That Engine Revving?
- [ ] L7965-L7971 (2) Fluid Regulator / Gas Turbine
- [ ] L7985-L8059 (19) Rocket Engine EV / Kinetic Wind Power EV / Kinetic Water Power IV / Kinetic Wind Power IV / Kinetic Water Power LuV / Power of the Sun at LuV Level … 他13件
- [ ] L8073-L8111 (10) You Haven't Learned How to Separate Fluids Yet? Seriously? / Acid Trip / Hallucinogenics Not Included / Portable Clean Energy EV / Portable Clean Energy LuV / Portable Clean Energy ZPM … 他4件
- [ ] L8117-L8223 (27) Radioisotope Thermoelectric Generator / Kinetic Power EV / Kinetic Power IV / Kinetic Power LuV / Kinetic Power ZPM / Kinetic Water Power EV … 他21件
- [ ] L8229-L8363 (34) Large Naquadah Reactor / Nuclear Based Fuel (Th) / Nuclear Based Fuel (U) / Nuclear Based Fuel (Pu) / Naquadah Fuel Refinery / Tier 2 Coil … 他28件

### EUの蓄電と変圧  _(L8366)_ — 未翻訳率: 37/63 (59%)

- [ ] L8370-L8380 (3) IV 16A Hatches / Can we get much higher? / Energized Wireless Dynamo Hatch
- [ ] L8470-L8508 (10) EU packets flowing everywhere... / Who Cares About a Little Cancer... / Lapotronic Energy Storage Unit / Manual Transformer / L.E.S.U. Upgrade - LV Tier / L.E.S.U. Upgrade - MV Tier … 他4件
- [ ] L8514-L8564 (13) Not Enough Amps? / More Than 4 Amps? Crazy! / Energy Buffers / Engraved Lapotrons / Lapotronic Energy Orb / One BILLION EU … 他7件
- [ ] L8570-L8600 (8) Gotta Pump It Up / Let it flow, let it floww ... / Extremely Ultimate and Ultimately Extreme / Wireless Power!? / EV 4A Hatches / Power Goggles … 他2件
- [ ] L8606-L8616 (3) IV 4A Hatches / EV 16A Hatches / At last, the final capacitor!

### 石油のための労働  _(L8619)_ — 未翻訳率: 31/46 (67%)

- [ ] L8623-L8646 (6) Maxed Oil Cracker / Super Fuel At The Top / Breaking the Mold / Ultimate Distillation / Hyperheated Steam / Universal Fuel Power
- [ ] L8664-L8670 (2) The Era of Multis / Generator Power
- [ ] L8712-L8802 (23) Using All the Fractions / Oil Cracker / Boosting the Diesel / Special Rubber from Oil / Distilled Heavy Fuel / Acetone and Ethenone … 他17件

### 大衆("マス")のためのバイオ  _(L8805)_ — 未翻訳率: 34/48 (71%)

- [ ] L8849-L8851 (1) Biological Diesel
- [ ] L8857-L8907 (13) Pyrolyse Oven / Large Steel Boiler / Wood Tar / The Most Powerful Biodiesel / Trees Growing Faster / Sapling Power … 他7件
- [ ] L8913-L8943 (8) Green Nitric Acid / Green Ethenone / Green Cetane-Boosted Diesel / Fermented Biomass / Free For All Fertilizer / Methane Stinks … 他2件
- [ ] L8949-L8995 (12) Upgrading Your Benzene / CBD Into Steam / Mass Distilled Water / Nitric And Sulfuric Acid / Titanium Chemical Plant / Nitrobenzene … 他6件

### 原子核物理学は強力  _(L8998)_ — 未翻訳率: 34/57 (60%)

- [ ] L9006-L9008 (1) Focus on Breeding
- [ ] L9018-L9024 (2) Build the Assembly Line First / Improved Fission
- [ ] L9030-L9036 (2) The Path of Fusion / Building the Reactor
- [ ] L9054-L9080 (7) Focus On Power Generation / Liquid Fluorine Thorium Reactor / First Half of LFTR Breeding / Sparge Tower / Fusion Europium / How Much Power From One Reactor? … 他1件
- [ ] L9122-L9192 (18) Nuclear Fuel Processing / Inputs and Outputs in the LFTR / First Steps in Reprocessing / Second Half of LFTR Breeding / Faster Lutetium Excitement / Exciting Liquid Nuking … 他12件
- [ ] L9210-L9224 (4) Duranium and the Beam Crafter / Reactors are Expensive! / Establishment of Fusion / A Second Reactor?

### スペース・レース  _(L9227)_ — 未翻訳率: 118/141 (84%)

- [ ] L9235-L9265 (8) Can I Build A Mothership For My Father? / The Legs On The Shuttle Rocket Go Step, Step, Step... / Shuttle Nose Cone / A Reward / H8N4C2O4 (Green) Rocket Fuel / Load and Unload the Rocket … 他2件
- [ ] L9335-L9345 (3) Oxygen Compressor / Parachute / Advanced Wafers
- [ ] L9351-L9377 (7) 1,1-Dimethylhydrazine / Formaldehyde / Space Station / Are You Prepared? / Moon Arrival / Ceres Dungeon … 他1件
- [ ] L9383-L9645 (66) Tier 4 Heavy Duty Plates / Rocket Tier 4 / Find Some Meteoric Iron / Tier 2 Heavy Duty Plates / Tier 2 Control Computer / Rocket Tier 2 … 他60件
- [ ] L9651-L9733 (21) Coal Tar Distilling / Dense Hydrazine / Monomethylhydrazine / CN3H7O3 (Purple) Rocket Fuel / 2-Ethylanthrahydroquinone / 2-Ethylanthraquinone … 他15件
- [ ] L9739-L9789 (13) Proteus Dungeon / Tier 6 Control Computer / Enceladus Dungeon / Space Pumping / How Do I Charge This Stuff? / steve@mothership:~$ … 他7件

### 基本的な自動化  _(L9792)_ — 未翻訳率: 15/35 (43%)

- [ ] L9800-L9850 (13) Cart Modules: Coal Power / Automated (un-)Loading / Cart Modules: Farming / Cart Modules: Storage / A Simple Cart / Cart Modules: Wood Cutter … 他7件
- [ ] L9920-L9922 (1) Dealing with H2S
- [ ] L9928-L9930 (1) Reward for Desulfurizing Automation

### SFMとコンピューター  _(L9933)_ — 未翻訳率: 53/54 (98%)

- [ ] L9937-L10147 (53) It's everytime these Transistors / Welcome to OpenComputers! / Your First Microchip / Your First Computer / Arithmetic Logic Circuits / All Your Card Are Belong To Us … 他47件

### パイプでロジスティクス  _(L10150)_ — 未翻訳率: 7/31 (23%)

- [ ] L10190-L10196 (2) Sorting Incoming / More ItemSinks in NEI
- [ ] L10206-L10208 (1) There Is Extra Stuff...
- [ ] L10226-L10228 (1) Time to See The Process
- [ ] L10238-L10240 (1) It's DA BEST
- [ ] L10258-L10260 (1) Modular Upgrades
- [ ] L10266-L10268 (1) I NEED THAT!!!!!!

### Applied Energistics  _(L10275)_ — 未翻訳率: 181/185 (98%)

- [ ] L10279-L10315 (9) 1024k Essentia Component / AE Tier 2 Fluid Storage / Quantum Entangled Singularities / Cribs / Need More Information? / 16384k Fluid Component … 他3件
- [ ] L10321-L10323 (1) 16k Item Storage Cell
- [ ] L10329-L10399 (18) Applied Crafting / Getting Your First Processors / Cables / Basic Terminals / Bundled AE Channels / Quantum Storage … 他12件
- [ ] L10405-L10859 (114) Keeping Your Network Happy / Storing Your ME Data / Speeding Up Growth / Perfecting Crystal Growth / Purifying the Impure / Maximum Security … 他108件
- [ ] L10865-L11019 (39) Co-Processing x256 / 4096k Essentia Storage Cell / Get Your Priorities Straight / 16384k Essentia Component / Hyper Acceleration! / Advanced Neutronium Tech … 他33件

### 養蜂要領を守って  _(L11022)_ — 未翻訳率: 41/83 (49%)

- [ ] L11026-L11028 (1) The Truth About Serum
- [ ] L11034-L11038 (1) Top-Tier Analyzer
- [ ] L11064-L11188 (21) Mutatron / Genetic Sampler / Diamondware / Genetic Imprinter / Genetic Transposer / Advanced Mutatron … 他15件
- [ ] L11246-L11250 (1) Breeding Bees Into Oblivion
- [ ] L11296-L11324 (5) Genepool / Isolator / Sequencer / Polymeriser / Gene Database
- [ ] L11330-L11340 (2) Registry / Droning On
- [ ] L11354-L11358 (1) Keep Calm and Bee On
- [ ] L11364-L11368 (1) Bee Slurry, the Breakfast of, Well, Weirdos
- [ ] L11378-L11394 (3) A Bag for Butterflies, yawn / Only the Best: Tree Breeding / Only the Worst: Trees Suck!
- [ ] L11400-L11410 (2) IAADDS / Pollen Collection Kit
- [ ] L11416-L11426 (3) Fluorescent Dye / Enzyme on The Mind / Growth Medium

### 交配の方蜂(ほうほう)  _(L11429)_ — 未翻訳率: 44/189 (23%)

- [ ] L11433-L11435 (1) MakeMake
- [ ] L11453-L11455 (1) Iridium
- [ ] L11461-L11463 (1) Neutronium
- [ ] L11473-L11475 (1) Naquadah
- [ ] L11493-L11495 (1) Gassy Bees
- [ ] L11525-L11531 (2) End Dust / Indium
- [ ] L11537-L11539 (1) Dragon Blood
- [ ] L11853-L11855 (1) Titanium
- [ ] L11865-L11867 (1) Uranium
- [ ] L11953-L11959 (2) Spirit / Soul
- [ ] L11973-L11979 (2) Rejuvenating / Empowering
- [ ] L12001-L12003 (1) Thaumic Shards
- [ ] L12017-L12027 (3) Abandoned / Draconic / Wither
- [ ] L12053-L12063 (3) D-O-B / Ender Shard / Nether Shard
- [ ] L12077-L12099 (6) Uranus / Moon / Salt / Barnarda / Glowstone / Infinity
- [ ] L12105-L12139 (9) Trinium / Sunnarium / Kevlar / Pyrotheum / Oriharukon / Cosmic Neutronium … 他3件
- [ ] L12145-L12167 (6) Pluto / Neptune / Essentia / Mars / Lapotron / Jupiter
- [ ] L12177-L12183 (2) Oberon / Infinity Catalyst

### Hardcore End(er) Expansion  _(L12186)_ — 未翻訳率: 40/40 (100%)

- [ ] L12190-L12348 (40) Spatial Distortions / Dimensional Chest / Is This the End? No, it's the END Dimension / Ender Towers / Welcome to the End! / Dragon Essence Altar … 他34件

### 初歩的な魔導学  _(L12351)_ — 未翻訳率: 29/102 (28%)

- [ ] L12355-L12365 (3) The Choice: Ordo / The Choice: Aqua / The Choice: Aer
- [ ] L12371-L12373 (1) Witchy (Wo)man
- [ ] L12395-L12397 (1) Tome of Knowledge
- [ ] L12447-L12465 (5) The Choice: Ignis / The Choice... / The Choice: Terra / The Choice: Perditio / This is the End...
- [ ] L12487-L12497 (3) Infinite... Lava? / Infinite Water! / Improved Armor: Samurai Style
- [ ] L12515-L12521 (2) Gold-Banded Greatwood Scepter / Primal Charm
- [ ] L12539-L12545 (2) Division Sigil / Cursed Earth
- [ ] L12587-L12589 (1) The Night's Not Dark Anymore
- [ ] L12607-L12609 (1) 3 Plus 4, Carry the 2...
- [ ] L12619-L12621 (1) Boots Are Made For Walking
- [ ] L12627-L12629 (1) Infinite Bats! Wait, What??
- [ ] L12643-L12645 (1) Everything Fuzzy? Try Some Lenses
- [ ] L12651-L12653 (1) Gimme gimme gimme
- [ ] L12671-L12673 (1) Comparing at a Distance
- [ ] L12687-L12689 (1) Shadow Metal
- [ ] L12707-L12709 (1) Thaumic Dendrology
- [ ] L12719-L12721 (1) Adding More Functions
- [ ] L12743-L12745 (1) Counting Items
- [ ] L12755-L12757 (1) Infinite Durability

### 発展的な魔導学  _(L12760)_ — 未翻訳率: 76/78 (97%)

- [ ] L12764-L12990 (57) Smoke Your Normal Warp Away / Adept Thaumaturgy / An Awesome Magic Conductor / A Silverwood Wand at Last / Creating a Better Wand / More Energetic Screws to Finish the New Wand … 他51件
- [ ] L12996-L13070 (19) Healing Your Nodes / Disenchanted / Fool's Gold / Gen XXXXXXXXXX... / Purge...Some of Your Warp? / Essentia Transmission … 他13件

### カーミー、ハーミー、...波ァ！  _(L13073)_ — 未翻訳率: 36/37 (97%)

- [ ] L13077-L13219 (36) Lord of the Rings? / The Power of Gods / Shards of Opposite Worlds / Unleashed the Power - Cowl / Unbreakable Cowl / Unleashed the Power - Leggings … 他30件

### 杖の杖星とEMT  _(L13222)_ — 未翻訳率: 38/40 (95%)

- [ ] L13226-L13264 (10) An Appropriate Weapon / Dropped in Asgard, Fallen to Earth / Repaired it! / Super-Mjolnir / Sparking Nitor...? / Rechargeable Scribing Tools … 他4件
- [ ] L13270-L13380 (28) I Don't Want to Set the World on Fire / Diggy Diggy Hole / Bzzap! / Trade Offer / Snowball Fight! / Magical Base Defense … 他22件

### 花の力  _(L13383)_ — 未翻訳率: 26/43 (60%)

- [ ] L13387-L13389 (1) Fountain Of Conjuration
- [ ] L13423-L13449 (7) A Glimpse Into A Watery Future / Botanic Infusion / Terrasteel / Alfheim / Round One... FIGHT! / A Deal With Alfar Industries … 他1件
- [ ] L13483-L13553 (18) Anti-Magnetism / Violence Is Blue / Roses Are Blood-Red / Magic Blue Dust / Better Generating Flowers / Shut Down Your Canning Machine … 他12件

### "端"に目を向ける  _(L13556)_ — 未翻訳率: 89/93 (96%)

- [ ] L13564-L13654 (23) Offerings / ...Cauldron Bubble / Don't Touch the Needle! / Probably Usable For Soup / Don't Shake it Too Much / Spirit Coin Transfer … 他17件
- [ ] L13660-L13886 (57) Purified Milk / Brew of Love / Sleep Well! / The Spirit World - Nightmare / Early Bird Gets the...Nightmare? / Wake Up Early … 他51件
- [ ] L13892-L13926 (9) The Easy Way to Change Biomes / The Hard Way to Change Biomes / More Hearts for Valentines / Are You Grassping What I'm Telling You? / PETA Approved* / Mad Science is the Best Science … 他3件

### 高い対価を払って  _(L13929)_ — 未翻訳率: 73/74 (99%)

- [ ] L13933-L14223 (73) Incense Crucible / Tier 2 Sigils / Paying the Highest Price / Portable Battery... / Poke / Tier 3 Sigils … 他67件

### 全部ブッ殺せ  _(L14226)_ — 未翻訳率: 151/344 (44%)

- [ ] L14230-L14264 (9) Time To Kill (Crimson Knight) / Kill Baba Yaga / Kill Horned Huntsman / Kill Ender Dragon / Kill Shade of Leonard / Kill Lord of Tormentum … 他3件
- [ ] L14274-L14284 (3) Slay the Eyes! / Ender Guardians / Slay the Dragon. (Again)
- [ ] L14426-L14440 (4) Time to Kill (Fire Golem) / Time to kill (Haunted Miners) / Time to Kill (Louse) / Time to Kill (Scorching Lens)
- [ ] L14565-L14587 (6) Something From Nothing Pt 2 / Industrial Water Purification / Waterproof Tech / Integrated Ore Factory - All in One! / Proto-Volt Stabilizer / Streamlined Casters
- [ ] L14625-L14631 (2) Dark Steel Tools / And It Will Never Break
- [ ] L14641-L14643 (1) Monitoring Your Reactor
- [ ] L14661-L14671 (3) Magical Waystones / Industrial 3D Copying Machine / Draconic Evolution
- [ ] L14717-L14723 (2) Advanced Nano Chestplate / Gravi Suit
- [ ] L14729-L14735 (2) Dark Steel Tool and Weapon Basic Upgrades / Dark Steel Tool and Weapon Advanced Upgrades
- [ ] L14765-L14767 (1) Power of the Sun ULV
- [ ] L14841-L14847 (2) Making Power With Your Plasma / Turbine Time
- [ ] L14885-L14887 (1) Angel Wings - Combine!
- [ ] L14893-L14911 (5) Pimp Your Wand Focus / Mallard Rust Smelly / Shake That Booty... / Launch Controller / Arc Lamp
- [ ] L14961-L14963 (1) Planetary Tears
- [ ] L14969-L14971 (1) Don't Put a Finger in That Socket
- [ ] L14989-L14999 (3) Too Much Mercury? / I'll Send Wireless Signals Where I Want, Thank You / Wireless 3.0
- [ ] L15017-L15047 (8) Unlimited LP / Infinity Chest / UV Solar / Does Anyone Even Still Use These? / Transform and...Stay Put Actually / What Even is This? … 他2件
- [ ] L15053-L15055 (1) 「 」
- [ ] L15061-L15103 (11) Nano Forge Tier 2 / Nano Forge Tier 3 / Chemical Pseudo-Altercations / Precise Assembler / Industrial Coke Oven / Bet On The Distillus … 他5件
- [ ] L15109-L15167 (15) Power in the Ether / PCB Factory / Bio Chamber / Liquid Cooling Tower / PCB Factory Tier 2 / Liquid Cooling Tower Tier 2 … 他9件
- [ ] L15173-L15187 (4) Heliocast Reinforcement / Balance is Everything / Asgardandelion / Celestial Gateways
- [ ] L15193-L15195 (1) Large Molecular Assembler
- [ ] L15201-L15207 (2) Sentient Overclocker / Large Hadron Collider
- [ ] L15221-L15243 (6) The Quest for Holy Water / High Energy Laser Purification / Neutronium Compressor / Matter Manipulator MKI / Universal Collapser / Matter Manipulator MKIII
- [ ] L15253-L15267 (4) Absolute Purity / Crafting Input Proxy / The Everlasting Guilty Pool / pH Neutralization
- [ ] L15273-L15275 (1) Hypercooler
- [ ] L15281-L15283 (1) Nano Forge Tier 4
- [ ] L15289-L15295 (2) Never Hungry Again / Quantum Uplink
- [ ] L15301-L15303 (1) Clarifier
- [ ] L15309-L15311 (1) Purifying Water With Plasma
- [ ] L15317-L15319 (1) Flocculation
- [ ] L15325-L15339 (4) Crafting, but with Beams! / Thaumometric Essentia Cell / Creative Mana Tablet / Exo-Foundry
- [ ] L15344-L15370 (7) Trigger: Nano Boots of the Traveller Skip / Trigger: Runeforged Thaumaturge's Ring / Trigger: Nightvision Goggle Skip / Trigger: Hafnium Skip / Trigger: Rocket Shuttle Skip / Trigger: Naquadria Skip … 他1件
- [ ] L15404-L15406 (1) Bees Template
- [ ] L15432-L15434 (1) Trigger: Flippers
- [ ] L15476-L15542 (17) Tool: Never complete / Trigger: Quantum Armor Skip / Trigger: NaK Skip / Trigger: Dense Hydrazine Skip / Trigger: Zirconium Skip / Trigger: Netherite Skip … 他11件
- [ ] L15548-L15582 (9) Trigger: Rocket Tier 2 Skip / Trigger: SMD Inductor Skip / Trigger: Division Sigil / Trigger: Polyphenylene Sulfide Skip / Trigger: Rocket Tier 7 Skip / Trigger: Profane Wand … 他3件
- [ ] L15588-L15614 (7) Trigger: Prismarine Line Skip / Trigger: CN3H7O3 (Purple) Rocket Fuel Skip / Ice Cream Trophy / Trigger: Oblivion Frame / Trigger: Rocket Tier 6 Skip / Trigger: Stonelily Tutorial Skip … 他1件

