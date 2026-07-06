---
title: "Projet : {params.projeto}"
---

```sql proj
select * from bsc.kpis_bsc_ia where project_name = '${params.projeto}'
```

```sql falhas_proj
select * from bsc.dominancia_erros where project_name = '${params.projeto}'
```

```sql hora_proj
select hora_brt, interrupcoes from bsc.interrupcoes_hora where project_name = '${params.projeto}' order by hora_brt
```

```sql waste_proj
select CASE categoria_waste WHEN 'Defeito (Defects) - Alucinacao/Retrabalho' THEN 'Défaut - Hallucination/Reprise' WHEN 'Defeito - Alucinacao' THEN 'Défaut - Hallucination' WHEN 'Espera (Waiting) - Cota/429' THEN 'Attente - Quota/429' WHEN 'Espera - Cota/429' THEN 'Attente - Quota/429' WHEN 'Espera (Waiting) - Latencia Alta' THEN 'Attente - Latence Élevée' WHEN 'Espera - Latencia Alta' THEN 'Attente - Latence Élevée' WHEN 'Superprocessamento - Prompt Inflado' THEN 'Surtraitement - Prompt Gonflé' ELSE categoria_waste END as categoria_waste, waste_tokens, pct_do_projeto, CASE solucao WHEN 'Fila com backoff + fallback por cota + upgrade de Tier (meta IOLI abaixo de 1%)' THEN 'File avec backoff + fallback par quota + upgrade de Tier (cible IOLI < 1%)' WHEN 'System prompt rigido + saida JSON + validacao LLM-as-judge (meta IITA abaixo de 10%)' THEN 'System prompt strict + sortie JSON + validation LLM-as-judge (cible IITA < 10%)' WHEN 'RAG/embeddings + sumarizacao + poda de historico (meta ITR estavel ou em queda)' THEN 'RAG/embeddings + résumé + élagage d''historique (cible ITR stable ou en baisse)' WHEN 'Streaming/TTFT + modelo rapido + cache (meta latencia abaixo de 3s)' THEN 'Streaming/TTFT + modèle rapide + cache (cible latence < 3s)' WHEN 'Converter aberto em estruturado: system prompt restritivo + few-shot + guardrails de escopo' THEN 'Convertir l''ouvert en structuré : system prompt restrictif + few-shot + garde-fous de portée' WHEN 'Few-shot valido + exigir testes + validacao de sintaxe/execucao + RAG das docs da lib' THEN 'Few-shot valide + exiger des tests + validation syntaxe/exécution + RAG des docs de la lib' WHEN 'Decomposicao em etapas + verificacao por etapa + self-consistency' THEN 'Décomposition en étapes + vérification par étape + self-consistency' WHEN 'JSON mode/schema + regex de validacao + exemplos entrada-saida' THEN 'JSON mode/schema + regex de validation + exemples entrée-sortie' WHEN 'Melhorar retrieval (re-rank) + citar fontes + grounding obrigatorio' THEN 'Améliorer le retrieval (re-rank) + citer les sources + grounding obligatoire' WHEN 'Templates fixos + exemplos de saida + JSON mode' THEN 'Modèles fixes + exemples de sortie + JSON mode' WHEN 'Limites de tamanho + instrucoes de fidelidade + QA factual' THEN 'Limites de taille + instructions de fidélité + QA factuel' ELSE solucao END as solucao from bsc.wastes_lean where project_name = '${params.projeto}' order by waste_tokens desc
```

```sql aluc_proj
select CASE prompt_categoria WHEN 'Conversa/Aberto' THEN 'Conversation/Ouvert' WHEN 'RAG/Busca' THEN 'RAG/Recherche' WHEN 'Transformacao/Formato' THEN 'Transformation/Format' WHEN 'Raciocinio/Analise' THEN 'Raisonnement/Analyse' WHEN 'Sumarizacao' THEN 'Résumé' WHEN 'Geracao de Codigo' THEN 'Génération de Code' WHEN 'Extracao de Dados' THEN 'Extraction de Données' ELSE prompt_categoria END as prompt_categoria, alucinacoes, taxa_aluc, CASE solucao WHEN 'Fila com backoff + fallback por cota + upgrade de Tier (meta IOLI abaixo de 1%)' THEN 'File avec backoff + fallback par quota + upgrade de Tier (cible IOLI < 1%)' WHEN 'System prompt rigido + saida JSON + validacao LLM-as-judge (meta IITA abaixo de 10%)' THEN 'System prompt strict + sortie JSON + validation LLM-as-judge (cible IITA < 10%)' WHEN 'RAG/embeddings + sumarizacao + poda de historico (meta ITR estavel ou em queda)' THEN 'RAG/embeddings + résumé + élagage d''historique (cible ITR stable ou en baisse)' WHEN 'Streaming/TTFT + modelo rapido + cache (meta latencia abaixo de 3s)' THEN 'Streaming/TTFT + modèle rapide + cache (cible latence < 3s)' WHEN 'Converter aberto em estruturado: system prompt restritivo + few-shot + guardrails de escopo' THEN 'Convertir l''ouvert en structuré : system prompt restrictif + few-shot + garde-fous de portée' WHEN 'Few-shot valido + exigir testes + validacao de sintaxe/execucao + RAG das docs da lib' THEN 'Few-shot valide + exiger des tests + validation syntaxe/exécution + RAG des docs de la lib' WHEN 'Decomposicao em etapas + verificacao por etapa + self-consistency' THEN 'Décomposition en étapes + vérification par étape + self-consistency' WHEN 'JSON mode/schema + regex de validacao + exemplos entrada-saida' THEN 'JSON mode/schema + regex de validation + exemples entrée-sortie' WHEN 'Melhorar retrieval (re-rank) + citar fontes + grounding obrigatorio' THEN 'Améliorer le retrieval (re-rank) + citer les sources + grounding obligatoire' WHEN 'Templates fixos + exemplos de saida + JSON mode' THEN 'Modèles fixes + exemples de sortie + JSON mode' WHEN 'Limites de tamanho + instrucoes de fidelidade + QA factual' THEN 'Limites de taille + instructions de fidélité + QA factuel' ELSE solucao END as solucao from bsc.alucinacao_categoria where project_name = '${params.projeto}' and alucinacoes > 0 order by alucinacoes desc
```

# 🛠️ {params.projeto}

<BigValue data={proj} value=kpi_psr title="PSR (0-5)" fmt=num2/>
<BigValue data={proj} value=kpi_peuc title="PEUC (%)" fmt=num1/>
<BigValue data={proj} value=total_tokens title="Tokens" fmt=num0/>
<BigValue data={proj} value=kpi_cpp title="CPP (R$/%)" fmt='$#,##0.00'/>

## Diagnostic d'Efficience

<DataTable data={proj}>
  <Column id=kpi_iita title="IITA % (hallucination)" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS % (gaspillage Lean)" fmt=num1/>
  <Column id=kpi_ioli title="IOLI % (inactivité)" fmt=num1/>
  <Column id=kpi_itr title="ITR (tok/req)" fmt=num0/>
  <Column id=kpi_ieet_hh_por_mtoken title="IEET (HH/M-tok)" fmt=num2/>
</DataTable>

## Santé Financière (Gitman & Startup)

<DataTable data={proj}>
  <Column id=vrt_por_ktoken title="VRT/kT (R$/1k)" fmt='$#,##0.0000'/>
  <Column id=burn_rate_ia title="Burn Rate IA (R$)" fmt='$#,##0.00'/>
  <Column id=kpi_icca title="ICCA (x)" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT (x)" fmt=num3/>
</DataTable>

## Pareto des Défaillances de ce Projet

<BarChart data={falhas_proj} x=categoria_falha y=quantidade title="Défaillances par catégorie" swapXY=true/>

## 🪙 Récupération de Coût (VRT) — 5 blocs + moyenne
<DataTable data={proj}>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="MOY." fmt='#,##0.00000'/>
</DataTable>

## ⏰ Heure Critique d'Interruption (BRT)
<BarChart data={hora_proj} x=hora_brt y=interrupcoes title="Interruptions par heure (BRT)" xAxisTitle="Heure (0-23)"/>

## ♻️ Taxonomie des Gaspillages (Lean Six Sigma)
<BarChart data={waste_proj} x=categoria_waste y=waste_tokens title="Gaspillage par catégorie (tokens pondérés)" swapXY=true labels=true/>

## 🔬 RCA — Hallucination par Type de Prompt (ce qui retarde ce projet)
<BarChart data={aluc_proj} x=prompt_categoria y=alucinacoes title="Hallucinations par type de prompt" swapXY=true labels=true sort=true/>

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="Type de prompt"/>
  <Column id=alucinacoes title="Hallucinations" fmt=num0/>
  <Column id=taxa_aluc title="Taux %" fmt=num1/>
</DataTable>

---

# 📌 Bottom-Line — Diagnostic Concluant et Solution Définitive
_Standard d'amélioration continue — source canonique : `foundations/solucoes_relatorios.md`._

## a) Dissertation des Gaspillages (Lean Six Sigma)
{#if waste_proj.length > 0}
Le **gaspillage dominant** de ce projet est **{waste_proj[0].categoria_waste}**, soit **{waste_proj[0].pct_do_projeto}%** du gaspillage pondéré. Il consomme tokens/trésorerie sans faire avancer et **pousse le CPP vers le haut**. La solution définitive et les autres catégories sont dans le tableau (appliquer par impact) :

<DataTable data={waste_proj}>
  <Column id=categoria_waste title="Gaspillage détecté"/>
  <Column id=waste_tokens title="Tokens gaspillés" fmt=num0/>
  <Column id=pct_do_projeto title="% du gaspillage" fmt=num1/>
  <Column id=solucao title="🛠️ Solution définitive (PDCA)" wrap=true/>
</DataTable>
{:else}
✅ Aucun gaspillage pertinent enregistré cette période.
{/if}

## b) Dissertation sur l'Hallucination de Prompts (RCA par taxonomie)
{#if aluc_proj.length > 0}
Le **type de prompt qui retarde le plus** ce projet est **{aluc_proj[0].prompt_categoria}**, avec **{aluc_proj[0].taxa_aluc}%** d'hallucination — le **goulot racine**. Chaque catégorie avec hallucination et sa contre-mesure définitive :

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="Type de prompt"/>
  <Column id=alucinacoes title="Hallucinations" fmt=num0/>
  <Column id=taxa_aluc title="Taux %" fmt=num1/>
  <Column id=solucao title="🛠️ Solution définitive (RCA)" wrap=true/>
</DataTable>
{:else}
✅ Aucune hallucination enregistrée cette période — aucun goulot détecté.
{/if}

## c) Amélioration Continue (PDCA / Kaizen)
1. **Plan** — attaquer d'abord le gaspillage dominant et le goulot ci-dessus.
2. **Do** — appliquer les solutions définitives des tableaux.
3. **Check** — mesurer la semaine suivante : IITA, IDLS, IOLI, ITR et latence.
4. **Act** — standardiser ce qui a marché dans le system prompt/pipeline et répéter.

> **Cap :** **CPP décroissant** semaine après semaine. Chaque gaspillage et hallucination réduits font baisser le CPP.
