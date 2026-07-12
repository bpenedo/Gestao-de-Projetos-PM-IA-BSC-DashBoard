---
title: "Projeto: {params.projeto}"
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
select categoria_waste, waste_tokens, pct_do_projeto, solucao from bsc.wastes_lean where project_name = '${params.projeto}' order by waste_tokens desc
```

```sql aluc_proj
select prompt_categoria, alucinacoes, taxa_aluc, solucao from bsc.alucinacao_categoria where project_name = '${params.projeto}' and alucinacoes > 0 order by alucinacoes desc
```

```sql mc_proj
select * from bsc.mc_estatisticas where project_name = '${params.projeto}' and variavel = 'VPL'
```

```sql mc_hist_proj
select bin_inferior, frequencia, cumul_pct from bsc.mc_histograma
where project_name = '${params.projeto}' and variavel = 'VPL' order by bin_idx
```

```sql mc_perc_proj
select percentil, valor from bsc.mc_percentis
where project_name = '${params.projeto}' and variavel = 'VPL' order by percentil
```

```sql mc_torn_proj
select variavel_entrada, beta_regressao, coef_correlacao from bsc.mc_tornado
where project_name = '${params.projeto}' and variavel_saida = 'VPL' order by ordem
```

```sql mc_todas_proj
select variavel, media, desvio_padrao, minimo, maximo, prob_menor_zero, var_5, cvar_5
from bsc.mc_estatisticas where project_name = '${params.projeto}'
```

```sql mcdm_proj
select metodo, score, rank_ from bsc.decisao_mcdm where project_name = '${params.projeto}' order by metodo
```

```sql ajuste_proj
select distribuicao, aic, ks_stat, ks_pvalue, rank_, escolhida
from bsc.mc_ajuste_distribuicao
where project_name = '${params.projeto}' and variavel = 'TOKENS' order by rank_
```

```sql ajuste_top_proj
select distribuicao, aic, ks_pvalue from bsc.mc_ajuste_distribuicao
where project_name = '${params.projeto}' and variavel = 'TOKENS' and escolhida = 1
```

```sql custo_tokens_proj
select media, desvio_padrao, maximo, var_5, cvar_5
from bsc.mc_estatisticas where project_name = '${params.projeto}' and variavel = 'CUSTO_TOKENS'
```

```sql robustez_proj
select metodo, prob_vitoria, prob_top3, rank_medio, rank_p05, rank_p95
from bsc.mcdm_robustez where project_name = '${params.projeto}' order by metodo
```

```sql robustez_consenso_proj
select prob_vitoria, prob_top3, rank_medio, rank_p05, rank_p95
from bsc.mcdm_robustez where project_name = '${params.projeto}' and metodo = 'CONSENSO (Borda)'
```

```sql robustez_dist_proj
select posicao, frequencia, pct from bsc.mcdm_robustez_dist
where project_name = '${params.projeto}' order by posicao
```

```sql crono_proj
select * from bsc.mc_cronograma where project_name = '${params.projeto}'
```

```sql crono_hist_proj
select classe_inf, frequencia, cumulativo from bsc.mc_cronograma_hist
where project_name = '${params.projeto}' order by classe_inf
```

```sql crono_crit_proj
select tarefa_id, nome, inicio, fim, duracao, folga, indice_criticidade, eh_critico
from bsc.cronograma_critico where project_name = '${params.projeto}' order by tarefa_id
```

```sql evm_proj
select * from bsc.evm_indices where project_name = '${params.projeto}'
```

```sql evm_serie_proj
select periodo, pv, ev, ac from bsc.evm_serie
where project_name = '${params.projeto}' order by periodo
```

```sql lat_proj
select dia, p50, p95, p99 from bsc.exec_latencia_tempo
where project_name = '${params.projeto}' order by dia
```

```sql burn_proj
select dia, tokens_acum, orcamento_acum from bsc.exec_tokens_burndown
where project_name = '${params.projeto}' order by dia
```

```sql qual_proj
select dia, taxa_erro, alerta_regressao from bsc.exec_qualidade_tempo
where project_name = '${params.projeto}' order by dia
```

```sql drift_proj
select dia, ks_stat, drift_alerta from bsc.exec_drift
where project_name = '${params.projeto}' order by dia
```

```sql risco_proj
select risco_id, categoria, descricao, dono, probabilidade, impacto, exposicao, nivel, status, mitigacao
from bsc.risco_registro where project_name = '${params.projeto}' order by exposicao desc
```

```sql risco_burn_proj
select dia, exposicao_total, exposicao_ideal from bsc.risco_burndown
where project_name = '${params.projeto}' order by dia
```

```sql cfd_proj
select dia, backlog, doing, review, done, wip from bsc.fluxo_cfd
where project_name = '${params.projeto}' order by dia
```

```sql fluxo_itens_proj
select dia_conclusao, cycle_time, lead_time from bsc.fluxo_itens
where project_name = '${params.projeto}' order by dia_conclusao
```

```sql fluxo_resumo_proj
select * from bsc.fluxo_resumo where project_name = '${params.projeto}'
```

# 🛠️ {params.projeto}

<BigValue data={proj} value=kpi_psr title="PSR (0-5)" fmt=num2/>
<BigValue data={proj} value=kpi_peuc title="PEUC (%)" fmt=num1/>
<BigValue data={proj} value=total_tokens title="Tokens" fmt=num0/>
<BigValue data={proj} value=kpi_cpp title="CPP (R$/%)" fmt='$#,##0.00'/>

## Diagnóstico de Eficiência

<DataTable data={proj}>
  <Column id=kpi_iita title="IITA % (alucinação)" fmt=num1/>
  <Column id=kpi_idls_lean title="IDLS % (waste Lean)" fmt=num1/>
  <Column id=kpi_ioli title="IOLI % (ociosidade)" fmt=num1/>
  <Column id=kpi_itr title="ITR (tok/req)" fmt=num0/>
  <Column id=kpi_ieet_hh_por_mtoken title="IEET (HH/M-tok)" fmt=num2/>
</DataTable>

## Saúde Financeira (Gitman & Startup)

<DataTable data={proj}>
  <Column id=vrt_por_ktoken title="VRT/kT (R$/1k)" fmt='$#,##0.0000'/>
  <Column id=burn_rate_ia title="Burn Rate IA (R$)" fmt='$#,##0.00'/>
  <Column id=kpi_icca title="ICCA (x)" fmt=num2/>
  <Column id=kpi_ibmt title="IBMT (x)" fmt=num3/>
</DataTable>

## Pareto de Falhas deste Projeto

<BarChart data={falhas_proj} x=categoria_falha y=quantidade title="Falhas por categoria" swapXY=true/>

## 🪙 Custo de Recuperação (VRT) — 5 blocos + média
<DataTable data={proj}>
  <Column id=vrt_50t title="50 tok" fmt='#,##0.00000'/>
  <Column id=vrt_100t title="100 tok" fmt='#,##0.00000'/>
  <Column id=vrt_250t title="250 tok" fmt='#,##0.00000'/>
  <Column id=vrt_500t title="500 tok" fmt='#,##0.00000'/>
  <Column id=vrt_por_ktoken title="1.000 tok" fmt='#,##0.00000'/>
  <Column id=vrt_media_blocos title="MÉDIA" fmt='#,##0.00000'/>
</DataTable>

## ⏰ Horário Crítico de Interrupção (BRT)
<BarChart data={hora_proj} x=hora_brt y=interrupcoes title="Interrupções por hora do dia (BRT)" xAxisTitle="Hora (0-23)"/>

## ♻️ Taxonomia de Wastes (Lean Six Sigma)
<BarChart data={waste_proj} x=categoria_waste y=waste_tokens title="Waste por categoria (tokens ponderados)" swapXY=true labels=true/>

## 🔬 RCA — Alucinação por Tipo de Prompt (o que atrasa este projeto)
<BarChart data={aluc_proj} x=prompt_categoria y=alucinacoes title="Alucinações por tipo de prompt" swapXY=true labels=true sort=true/>

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="Tipo de prompt"/>
  <Column id=alucinacoes title="Alucinações" fmt=num0/>
  <Column id=taxa_aluc title="Taxa %" fmt=num1/>
</DataTable>

---

## 🎲 Simulação de Monte Carlo do VPL (10.000 iterações)

> Cada fluxo periódico deste projeto vira uma **variável aleatória Triangular** (±30% em torno do valor base).
> A semente é fixa: rodar de novo dá exatamente o mesmo resultado.

<BigValue data={mc_proj} value=media title="VPL médio (R$)" fmt='$#,##0'/>
<BigValue data={mc_proj} value=desvio_padrao title="Desvio-padrão (R$)" fmt='$#,##0'/>
<BigValue data={mc_proj} value=prob_menor_zero title="P(VPL < 0) %" fmt=num2/>
<BigValue data={mc_proj} value=var_5 title="VaR 5% (R$)" fmt='$#,##0'/>

**Histograma de frequência do VPL** — 100 classes, do mínimo ao máximo simulados (a "curva de risco" do projeto).

<BarChart data={mc_hist_proj} x=bin_inferior y=frequencia title="Distribuição do VPL simulado" yAxisTitle="Frequência" xAxisTitle="VPL (R$)" colorPalette={['#FF0000']}>
  <ReferenceLine x=0 color=negative label="prejuízo"/>
</BarChart>

**Distribuição acumulada** — leia a probabilidade de o VPL ficar abaixo de qualquer valor.

<LineChart data={mc_hist_proj} x=bin_inferior y=cumul_pct title="Probabilidade acumulada do VPL (%)" yAxisTitle="Acumulado (%)" xAxisTitle="VPL (R$)">
  <ReferenceLine x=0 color=negative label="break-even"/>
</LineChart>

**Percentis do VPL (1% a 99%)** — o percentil 5% é o VaR: o pior cenário plausível.

<LineChart data={mc_perc_proj} x=percentil y=valor title="Percentis do VPL simulado" yAxisTitle="VPL (R$)" xAxisTitle="Percentil (%)">
  <ReferenceLine y=0 color=negative label="break-even"/>
</LineChart>

**Análise de sensibilidade (tornado)** — qual período mais move o VPL. O **beta** é o efeito de +R$ 1 no fluxo
daquele período sobre o VPL; a **correlação** mede o quanto a incerteza daquele período dita a incerteza do VPL.

<DataTable data={mc_torn_proj} rows=all rowShading=true>
  <Column id=variavel_entrada title="Variável de entrada"/>
  <Column id=beta_regressao title="Beta da regressão" fmt=num4 contentType=colorscale/>
  <Column id=coef_correlacao title="Coef. de correlação" fmt=num4 contentType=colorscale/>
</DataTable>

<BarChart data={mc_torn_proj} x=variavel_entrada y=coef_correlacao title="Tornado — correlação de cada período com o VPL" yAxisTitle="Correlação" swapXY=true sort=true colorPalette={['#FF0000']}/>

**Todas as saídas simuladas** (VPL, TIR, TIRM, VUL e ILL sob incerteza)

<DataTable data={mc_todas_proj} rows=all rowShading=true>
  <Column id=variavel title="Indicador"/>
  <Column id=media title="Média" fmt=num4/>
  <Column id=desvio_padrao title="Desvio-padrão" fmt=num4/>
  <Column id=minimo title="Mínimo" fmt=num4/>
  <Column id=maximo title="Máximo" fmt=num4/>
  <Column id=prob_menor_zero title="P(X<0) %" fmt=num2/>
  <Column id=var_5 title="VaR 5%" fmt=num4/>
  <Column id=cvar_5 title="CVaR 5%" fmt=num4/>
</DataTable>

## 📅 Cronograma Monte Carlo & Gantt (risco de prazo)

> As durações das tarefas são **estimativas de 3 pontos (PERT)** — otimista, mais provável, pessimista —
> simuladas 10.000 vezes pelo mesmo motor de Monte Carlo. A soma determinística do PERT é **otimista** por
> causa do viés de convergência (o `max` de caminhos paralelos empurra o término para depois); por isso o
> compromisso recomendável é o **P80**, não a estimativa determinística.

<BigValue data={crono_proj} value=p50 title="P50 — mediana (dias)" fmt=num1/>
<BigValue data={crono_proj} value=p80 title="P80 — commit (dias)" fmt=num1/>
<BigValue data={crono_proj} value=prazo_alvo title="Deadline baseline (dias)" fmt=num1/>
<BigValue data={crono_proj} value=prob_no_prazo title="P(no prazo) %" fmt=num1/>

**Gráfico de Gantt** — barras **vermelhas** são o caminho crítico; **azuis** têm folga (extensão cinza).
O **% em cada tarefa é o índice de criticidade**: em quantos por cento das 10.000 simulações aquela tarefa
caiu no caminho crítico — o que o CPM determinístico esconde.

<img src={'/mc/' + params.projeto.replaceAll(' ', '_') + '_gantt.png'} alt="Gráfico de Gantt com caminho crítico" style="width:100%;border-radius:8px;"/>

**Distribuição da data de término** — a "curva de risco" do prazo. A deadline baseline, o P50 e o P80 estão marcados.

<BarChart data={crono_hist_proj} x=classe_inf y=frequencia title="Distribuição da data de término (dias)" yAxisTitle="Frequência" xAxisTitle="Dias" colorPalette={['#FF0000']}/>

<LineChart data={crono_hist_proj} x=classe_inf y=cumulativo title="Probabilidade acumulada de término (%)" yAxisTitle="Acumulado (%)" xAxisTitle="Dias"/>

**Caminho crítico e criticidade por tarefa** — priorize quem tem alto índice de criticidade: é onde o atraso vira atraso do projeto.

<DataTable data={crono_crit_proj} rows=all rowShading=true>
  <Column id=tarefa_id title="#"/>
  <Column id=nome title="Tarefa"/>
  <Column id=inicio title="Início (dia)" fmt=num1/>
  <Column id=fim title="Fim (dia)" fmt=num1/>
  <Column id=folga title="Folga" fmt=num1/>
  <Column id=indice_criticidade title="Criticidade %" fmt=num1 contentType=colorscale/>
</DataTable>

## 📐 Earned Value Management (custo + prazo + escopo num só quadro)

> O padrão que une as três dimensões. **SPI** = adiantado/atrasado; **CPI** = dentro/fora do orçamento;
> **EAC** = quanto o projeto vai custar no total ao ritmo atual; **SPI(t)** (Earned Schedule) corrige o
> defeito conhecido do SPI, que converge para 1 no fim mesmo com o projeto atrasado.

<BigValue data={evm_proj} value=spi title="SPI (prazo)" fmt=num2/>
<BigValue data={evm_proj} value=cpi title="CPI (custo)" fmt=num2/>
<BigValue data={evm_proj} value=eac title="EAC — estimativa no término (R$)" fmt='$#,##0'/>
<BigValue data={evm_proj} value=spi_t title="SPI(t) — Earned Schedule" fmt=num2/>

**Curva S** — PV (planejado) · EV (agregado) · AC (custo real). Se EV está abaixo de PV, o projeto atrasa;
se AC está acima de EV, estoura o orçamento.

<img src={'/mc/' + params.projeto.replaceAll(' ', '_') + '_evm.png'} alt="Curva S do Earned Value Management" style="width:100%;border-radius:8px;"/>

<LineChart data={evm_serie_proj} x=periodo y={['pv','ev','ac']} title="PV · EV · AC por período (R$)" yAxisTitle="Acumulado (R$)" xAxisTitle="Período (semana)"/>

<DataTable data={evm_proj} rows=all>
  <Column id=sv title="SV (prazo, R$)" fmt='$#,##0' contentType=colorscale/>
  <Column id=cv title="CV (custo, R$)" fmt='$#,##0' contentType=colorscale/>
  <Column id=vac title="VAC (variação no término)" fmt='$#,##0' contentType=colorscale/>
  <Column id=tcpi title="TCPI (eficiência necessária)" fmt=num2/>
  <Column id=ieac_t title="Prazo estimado (períodos)" fmt=num1/>
</DataTable>

## ⚙️ Saúde de execução da IA no tempo (Langfuse real)

> O que diferencia de um framework financeiro: **saúde operacional ao longo do tempo**, dos logs reais
> do Langfuse. Latência sob SLO, orçamento de tokens, regressão de qualidade e *drift* do modelo.

**Latência p50/p95/p99 por dia** — a linha vermelha é o **SLO** (p95 ≤ 5 s). Cruzou, o serviço degradou.

<LineChart data={lat_proj} x=dia y={['p50','p95','p99']} title="Latência por dia (s)" yAxisTitle="segundos" xAxisTitle="dia">
  <ReferenceLine y=5 color=negative label="SLO p95 = 5s"/>
</LineChart>

**Token budget burndown** — consumo acumulado vs orçamento. Acima da linha de orçamento = estouro.

<LineChart data={burn_proj} x=dia y={['tokens_acum','orcamento_acum']} title="Tokens acumulados vs orçamento" yAxisTitle="tokens" xAxisTitle="dia"/>

**Tendência de qualidade** — taxa de erro por dia; um pico dispara o alerta de regressão (regra tipo SPC).

<LineChart data={qual_proj} x=dia y=taxa_erro title="Taxa de erro por dia (%)" yAxisTitle="% de erros" xAxisTitle="dia"/>

**Drift do modelo** — distância de Kolmogorov-Smirnov entre a distribuição de tokens do dia e a do 1º dia.
Passou do limiar, o comportamento do modelo mudou (não é intuição — é o mesmo KS do ajuste de distribuições).

<LineChart data={drift_proj} x=dia y=ks_stat title="Drift da distribuição de tokens (D de KS)" yAxisTitle="D de KS" xAxisTitle="dia">
  <ReferenceLine y=0.20 color=negative label="limiar de drift"/>
</LineChart>

## 🚨 Registro de risco & matriz Probabilidade × Impacto

> Complementa o Monte Carlo (risco quantitativo) com o **risco qualitativo** que o PMO cobra. A
> probabilidade de cada risco é **ancorada nos sinais reais** deste projeto: drift, violações de SLO,
> CPI e regressões de qualidade — não é chute.

**Matriz P × I** — cada bolha é um risco; quanto mais para o canto superior-direito, mais perigoso.

<ScatterPlot data={risco_proj} x=probabilidade y=impacto size=exposicao series=nivel title="Probabilidade × Impacto (bolha = exposição)" xAxisTitle="Probabilidade (1–5)" yAxisTitle="Impacto (1–5)" xMin=0 xMax=6 yMin=0 yMax=6/>

**Risk burndown** — a exposição ativa deve cair ao longo do tempo (linha ideal a zero). Se sobe, um risco reabriu.

<LineChart data={risco_burn_proj} x=dia y={['exposicao_total','exposicao_ideal']} title="Exposição total ao risco por dia" yAxisTitle="exposição (Σ P×I)" xAxisTitle="dia"/>

**Registro de risco** — ordenado por exposição; priorize os `crítico`/`alto` ainda `aberto`.

<DataTable data={risco_proj} rows=all rowShading=true>
  <Column id=categoria title="Categoria"/>
  <Column id=descricao title="Risco"/>
  <Column id=dono title="Dono"/>
  <Column id=probabilidade title="P" align=center/>
  <Column id=impacto title="I" align=center/>
  <Column id=exposicao title="Exposição" fmt=num0 contentType=colorscale/>
  <Column id=nivel title="Nível"/>
  <Column id=status title="Status"/>
  <Column id=mitigacao title="Mitigação"/>
</DataTable>

## 🌊 Fluxo de trabalho (Kanban): CFD, cycle time e throughput

> Fecha o lado da entrega. O **CFD** mostra WIP e gargalos de relance; o **cycle time P85** dá previsão
> por percentil (não por chute); o **throughput** é o ritmo real de conclusão.

<BigValue data={fluxo_resumo_proj} value=throughput_dia title="Throughput (itens/dia)" fmt=num1/>
<BigValue data={fluxo_resumo_proj} value=ct_p50 title="Cycle time P50 (dias)" fmt=num1/>
<BigValue data={fluxo_resumo_proj} value=ct_p85 title="Cycle time P85 (dias)" fmt=num1/>
<BigValue data={fluxo_resumo_proj} value=wip_medio title="WIP médio" fmt=num1/>

**Cumulative Flow Diagram** — faixas paralelas = fluxo saudável; uma faixa que engorda = gargalo/WIP preso.

<AreaChart data={cfd_proj} x=dia y={['backlog','doing','review','done']} title="CFD — itens por estado ao longo do tempo" yAxisTitle="itens" xAxisTitle="dia"/>

**Cycle time por item concluído** — a dispersão; a maioria dos itens fica abaixo do P85 (a linha de previsão).

<ScatterPlot data={fluxo_itens_proj} x=dia_conclusao y=cycle_time title="Cycle time dos itens concluídos (dias)" yAxisTitle="cycle time (dias)" xAxisTitle="conclusão"/>

## 🧮 Posição deste projeto em cada método multicritério

> **DEMATEL** deriva os pesos por influência; **ELECTRE I** e **PROMETHEE II** ranqueiam por sobreclassificação;
> **MAUT** por utilidade com aversão a risco; **MCDA-C** por função de valor ancorada em Neutro/Bom; e o
> **AHP-TOPSIS 2n** por proximidade à solução ideal. A posição final vem do consenso de Borda entre os cinco.

<DataTable data={mcdm_proj} rows=all rowShading=true>
  <Column id=metodo title="Método"/>
  <Column id=score title="Score" fmt=num4/>
  <Column id=rank_ title="Posição" contentType=colorscale/>
</DataTable>

<BarChart data={mcdm_proj} x=metodo y=rank_ title="Posição deste projeto por método (menor = melhor)" yAxisTitle="Posição" swapXY=true/>

## 🔎 Distribuição ajustada aos tokens REAIS deste projeto

> Em vez de **arbitrar** a distribuição do consumo de tokens, nós a **inferimos** da série histórica
> (`logs_langfuse`) — é o *ajuste de distribuições a dados*. Onze candidatas são ajustadas por máxima
> verossimilhança; vence a de **menor AIC**, e o teste de **Kolmogorov-Smirnov** mede a aderência.
>
> **Por que isto importa:** o VPL é *linear* nos fluxos de caixa, então simular só os fluxos com uma Triangular
> simétrica gera um tornado que apenas devolve os fatores de desconto `1/(1+i)ᵗ` — informação nenhuma. O sinal
> estocástico de verdade está **a montante**, nos tokens, que têm cauda pesada: alguns prompts consomem 10× o
> típico, e é essa cauda que estoura o orçamento.

<BigValue data={ajuste_top_proj} value=distribuicao title="Distribuição vencedora (menor AIC)"/>
<BigValue data={ajuste_top_proj} value=ks_pvalue title="Aderência KS (p-valor)" fmt=num3/>
<BigValue data={custo_tokens_proj} value=media title="Custo de tokens médio (R$)" fmt='$#,##0.00'/>
<BigValue data={custo_tokens_proj} value=maximo title="Pior caso simulado (R$)" fmt='$#,##0.00'/>

> ⚠️ **Como ler o p-valor:** acima de 0,05 não rejeitamos a aderência (o ajuste é plausível). **Abaixo de 0,05, a
> distribuição escolhida não descreve bem os seus dados** — use-a com ressalva, colete mais amostras ou trate a
> série como multimodal. O framework reporta isso em vez de esconder.

<DataTable data={ajuste_proj} rows=all rowShading=true>
  <Column id=rank_ title="#"/>
  <Column id=distribuicao title="Distribuição"/>
  <Column id=aic title="AIC (menor = melhor)" fmt=num1 contentType=colorscale/>
  <Column id=ks_stat title="KS D" fmt=num4/>
  <Column id=ks_pvalue title="KS p-valor" fmt=num4/>
  <Column id=escolhida title="Escolhida" fmt=boolean/>
</DataTable>

<BarChart data={ajuste_proj} x=distribuicao y=aic title="Comparação das candidatas por AIC (menor é melhor)" yAxisTitle="AIC" swapXY=true sort=true/>

## 🎯 Robustez da decisão — este projeto vence em quantos universos?

> Os pesos dos critérios **nunca são exatos**: são estimativas. Se 2 pontos percentuais no peso do IITA trocam o 1º
> com o 2º lugar, o "vencedor" é um artefato da calibração, não um fato do portfólio. Então perturbamos os pesos
> do DEMATEL com uma **Dirichlet** — `w' ~ Dir(κ·w)`, que preserva `E[w'] = w` e vive exatamente no simplex — e
> **reranqueamos 2.000 vezes**.
>
> O veredito deixa de ser *"este é o melhor"* e passa a ser **"este vence em P% dos universos de preferência
> plausíveis"**. É um intervalo de confiança sobre a **própria decisão**.

<BigValue data={robustez_consenso_proj} value=prob_vitoria title="Vence o consenso em (%)" fmt=num1/>
<BigValue data={robustez_consenso_proj} value=prob_top3 title="Fica no Top-3 em (%)" fmt=num1/>
<BigValue data={robustez_consenso_proj} value=rank_medio title="Posição típica" fmt=num2/>
<BigValue data={robustez_consenso_proj} value=rank_p95 title="Pior posição plausível (p95)" fmt=num0/>

**Distribuição das posições sob pesos perturbados** — uma barra única em 1º significa veredito **robusto**; barras
espalhadas significam que a posição deste projeto **depende de como você calibra os critérios**.

<BarChart data={robustez_dist_proj} x=posicao y=pct title="Em quantos % dos universos este projeto cai em cada posição" yAxisTitle="% dos universos" xAxisTitle="Posição no ranking" colorPalette={['#8E44AD']}/>

**Por método** — quando um método discorda muito dos demais, o consenso de Borda está *mascarando* uma divergência
de escola. Isso é informação: significa que a escolha depende de você preferir sobreclassificação, utilidade ou
função de valor.

<DataTable data={robustez_proj} rows=all rowShading=true>
  <Column id=metodo title="Método"/>
  <Column id=prob_vitoria title="Vence em (%)" fmt=num1 contentType=colorscale/>
  <Column id=prob_top3 title="Top-3 em (%)" fmt=num1/>
  <Column id=rank_medio title="Posição média" fmt=num2/>
  <Column id=rank_p05 title="Melhor caso (p05)" fmt=num0/>
  <Column id=rank_p95 title="Pior caso (p95)" fmt=num0/>
</DataTable>

<BarChart data={robustez_proj} x=metodo y=prob_vitoria title="Probabilidade de vitória por método (pesos perturbados)" yAxisTitle="% dos universos" swapXY=true/>

# 📌 Bottom-Line — Diagnóstico Conclusivo & Solução Definitiva
_Padrão de melhoria contínua — fonte canônica: `foundations/solucoes_relatorios.md`._

## a) Dissertação de Wastes (Lean Six Sigma)
{#if waste_proj.length > 0}
O **desperdício dominante** deste projeto é **{waste_proj[0].categoria_waste}**, responsável por
**{waste_proj[0].pct_do_projeto}%** do waste ponderado. Esse desperdício consome tokens/caixa sem
avançar o progresso e, portanto, **pressiona o CPP para cima**. A solução definitiva e as demais
categorias detectadas estão na tabela abaixo (aplicar em ordem de impacto):

<DataTable data={waste_proj}>
  <Column id=categoria_waste title="Waste detectado"/>
  <Column id=waste_tokens title="Tokens desperd." fmt=num0/>
  <Column id=pct_do_projeto title="% do waste" fmt=num1/>
  <Column id=solucao title="🛠️ Solução definitiva (PDCA)" wrap=true/>
</DataTable>
{:else}
✅ Sem waste relevante registrado neste período.
{/if}

## b) Dissertação de Alucinação de Prompts (RCA por taxonomia)
{#if aluc_proj.length > 0}
O **tipo de prompt que mais atrasa** este projeto é **{aluc_proj[0].prompt_categoria}**, com
**{aluc_proj[0].taxa_aluc}%** de alucinação — é o **gargalo-raiz** das entregas. Cada categoria com
alucinação detectada e sua contramedida definitiva:

<DataTable data={aluc_proj}>
  <Column id=prompt_categoria title="Tipo de prompt"/>
  <Column id=alucinacoes title="Alucinações" fmt=num0/>
  <Column id=taxa_aluc title="Taxa %" fmt=num1/>
  <Column id=solucao title="🛠️ Solução definitiva (RCA)" wrap=true/>
</DataTable>
{:else}
✅ Sem alucinações registradas neste período — nenhum gargalo de prompt detectado.
{/if}

## c) Melhoria Contínua (PDCA / Kaizen)
1. **Plan** — atacar primeiro o waste dominante e o prompt-gargalo apontados acima.
2. **Do** — aplicar as soluções definitivas das tabelas.
3. **Check** — medir na semana seguinte: IITA, IDLS, IOLI, ITR e latência.
4. **Act** — padronizar no system prompt/pipeline o que funcionou e repetir o ciclo.

> **Norte:** **CPP decrescente** semana a semana. Cada waste e cada alucinação reduzidos derrubam o CPP.
