M2D2_SPLIT_NAMES = ["Art", "Culture_and_the_arts", "Culture_and_the_arts__Culture_and_Humanities", "Culture_and_the_arts__Games_and_Toys", "Culture_and_the_arts__Mass_media", "Culture_and_the_arts__Performing_arts", "Culture_and_the_arts__Sports_and_Recreation", "Culture_and_the_arts__The_arts_and_Entertainment", "Culture_and_the_arts__Visual_arts", "General_referece", "General_referece__Further_research_tools_and_topics", "General_referece__Reference_works", "Health_and_fitness", "Health_and_fitness__Exercise", "Health_and_fitness__Health_science", "Health_and_fitness__Human_medicine", "Health_and_fitness__Nutrition", "Health_and_fitness__Public_health", "Health_and_fitness__Self_care", "History_and_events", "History_and_events__By_continent", "History_and_events__By_period", "History_and_events__By_region", "Human_activites", "Human_activites__Human_activities", "Human_activites__Impact_of_human_activity", "Mathematics_and_logic", "Mathematics_and_logic__Fields_of_mathematics", "Mathematics_and_logic__Logic", "Mathematics_and_logic__Mathematics", "Natural_and_physical_sciences", "Natural_and_physical_sciences__Biology", "Natural_and_physical_sciences__Earth_sciences", "Natural_and_physical_sciences__Nature", "Natural_and_physical_sciences__Physical_sciences", "Philosophy", "Philosophy_and_thinking", "Philosophy_and_thinking__Philosophy", "Philosophy_and_thinking__Thinking", "Religion_and_belief_systems", "Religion_and_belief_systems__Allah", "Religion_and_belief_systems__Belief_systems", "Religion_and_belief_systems__Major_beliefs_of_the_world", "Society_and_social_sciences", "Society_and_social_sciences__Social_sciences", "Society_and_social_sciences__Society", "Technology_and_applied_sciences", "Technology_and_applied_sciences__Agriculture", "Technology_and_applied_sciences__Computing", "Technology_and_applied_sciences__Engineering", "Technology_and_applied_sciences__Transport", "alg-geom", "ao-sci", "astro-ph", "astro-ph.CO", "astro-ph.EP", "astro-ph.GA", "astro-ph.HE", "astro-ph.IM", "astro-ph.SR", "astro-ph_l1", "atom-ph", "bayes-an", "chao-dyn", "chem-ph", "cmp-lg", "comp-gas", "cond-mat", "cond-mat.dis-nn", "cond-mat.mes-hall", "cond-mat.mtrl-sci", "cond-mat.other", "cond-mat.quant-gas", "cond-mat.soft", "cond-mat.stat-mech", "cond-mat.str-el", "cond-mat.supr-con", "cond-mat_l1", "cs.AI", "cs.AR", "cs.CC", "cs.CE", "cs.CG", "cs.CL", "cs.CR", "cs.CV", "cs.CY", "cs.DB", "cs.DC", "cs.DL", "cs.DM", "cs.DS", "cs.ET", "cs.FL", "cs.GL", "cs.GR", "cs.GT", "cs.HC", "cs.IR", "cs.IT", "cs.LG", "cs.LO", "cs.MA", "cs.MM", "cs.MS", "cs.NA", "cs.NE", "cs.NI", "cs.OH", "cs.OS", "cs.PF", "cs.PL", "cs.RO", "cs.SC", "cs.SD", "cs.SE", "cs.SI", "cs.SY", "cs_l1", "dg-ga", "econ.EM", "econ.GN", "econ.TH", "econ_l1", "eess.AS", "eess.IV", "eess.SP", "eess.SY", "eess_l1", "eval_sets", "funct-an", "gr-qc", "hep-ex", "hep-lat", "hep-ph", "hep-th", "math-ph", "math.AC", "math.AG", "math.AP", "math.AT", "math.CA", "math.CO", "math.CT", "math.CV", "math.DG", "math.DS", "math.FA", "math.GM", "math.GN", "math.GR", "math.GT", "math.HO", "math.IT", "math.KT", "math.LO", "math.MG", "math.MP", "math.NA", "math.NT", "math.OA", "math.OC", "math.PR", "math.QA", "math.RA", "math.RT", "math.SG", "math.SP", "math.ST", "math_l1", "mtrl-th", "nlin.AO", "nlin.CD", "nlin.CG", "nlin.PS", "nlin.SI", "nlin_l1", "nucl-ex", "nucl-th", "only_text", "only_txt2", "patt-sol", "physics.acc-ph", "physics.ao-ph", "physics.app-ph", "physics.atm-clus", "physics.atom-ph", "physics.bio-ph", "physics.chem-ph", "physics.class-ph", "physics.comp-ph", "physics.data-an", "physics.ed-ph", "physics.flu-dyn", "physics.gen-ph", "physics.geo-ph", "physics.hist-ph", "physics.ins-det", "physics.med-ph", "physics.optics", "physics.plasm-ph", "physics.pop-ph", "physics.soc-ph", "physics.space-ph", "physics_l1", "plasm-ph", "q-alg", "q-bio", "q-bio.BM", "q-bio.CB", "q-bio.GN", "q-bio.MN", "q-bio.NC", "q-bio.OT", "q-bio.PE", "q-bio.QM", "q-bio.SC", "q-bio.TO", "q-bio_l1", "q-fin.CP", "q-fin.EC", "q-fin.GN", "q-fin.MF", "q-fin.PM", "q-fin.PR", "q-fin.RM", "q-fin.ST", "q-fin.TR", "q-fin_l1", "quant-ph", "solv-int", "stat.AP", "stat.CO", "stat.ME", "stat.ML", "stat.OT", "stat.TH", "stat_l1", "supr-con"]

print(f"number of splits: ", len(M2D2_SPLIT_NAMES))


s2orc = """cs.CE, cs.IT, cs.CG, cs.SI, cond-mat.quant-gas, math.SG, cs.SC, cs.CY, econ.GN, math.CO, cs.AR,
cs.MS, cs.DC, q-bio.TO, cs.GR, physics.acc-ph, physics.geo-ph, math.RT, math.HO, cs.RO, q-bio.SC,
math.QA, cs.NI, math.CA, cs.DS, astro-ph.GA, physics.atom-ph, math.CT, cs.CV, cond-mat.mtrl-sci,
math.CV, math.AC, cond-mat.str-el, physics.comp-ph, cs.CC, math.FA, cond-mat.dis-nn, econ.TH,
physics.gen-ph, physics.data-an, astro-ph.IM, q-bio.CB, math.LO, physics.ins-det, q-bio.BM, cs.LO,
math.GR, physics.optics, cs.GT, math.AG, cs.NE, cs.SY, physics.bio-ph, physics.flu-dyn, cs.CL, math.MG,
cs.AI, math.OC, nlin.CG, math.IT, stat.OT, math.OA, cond-mat.soft, Art, cs.GL, cs.PF, math.ST,
physics.ao-ph, physics.plasm-ph, math.RA, physics.hist-ph, cs.PL, cs.MA, physics.chem-ph, physics.socph, physics.med-ph, physics.ed-ph, stat.AP, stat.CO, math.DS, cs.DB, nlin.SI, q-bio.GN, physics.atmclus, nlin.CD, astro-ph.CO, cs.CR, cond-mat.supr-con, cs.LG, math.KT, stat.ML, nlin.PS, q-bio.MN,
cs.IR, math.GT, cs.SD, math.NA, cond-mat.other, math.NT, cs.FL, physics.pop-ph, cond-mat.stat-mech,
math.GN, cs.DL, astro-ph.EP, q-bio.QM, cs.ET, q-bio.PE, cs.OH, Philosophy, physics.space-ph, econ.EM,
physics.class-ph, cs.DM, cond-mat.mes-hall, stat.TH, cs.SE, astro-ph.HE, math.MP, nlin.AO, math.AP,
q-bio.NC, q-bio.OT, astro-ph.SR, math.DG, math.AT, cs.MM, stat.ME, cs.OS, math.SP, physics.app-ph,
cs.NA, math.PR, math.GM, cs.HC"""
wiki = """Culture and Humanities, Games and Toys, Mass media, Performing arts, Sports and Recreation, The
arts and Entertainment, Visual arts, Further research tools and topics, Reference works, Exercise, Health
science, Human medicine, Nutrition, Public health, Self care, By continent, By period, By region, Human
activities, Impact of human activity, Fields of mathematics, Logic, Mathematics, Biology, Earth sciences,
Nature, Physical sciences, Philosophy, Thinking, Allah, Belief systems, Major beliefs of the world, Social
sciences, Society, Agriculture, Computing, Engineering, Transport"""

set1 = set([i.lower().strip() for i in s2orc.split(", ")])
set2 = set([i.lower().strip() for i in wiki.split(", ")])
print(len(s2orc.split(", ")))
print(len(wiki.split(", ")))

set1.update(set2)
print(len(set1))

