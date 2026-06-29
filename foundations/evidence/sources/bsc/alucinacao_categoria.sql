-- Alucinação por TIPO DE PROMPT em cada projeto + SOLUÇÃO DEFINITIVA (RCA).
SELECT project_name, prompt_categoria,
  SUM(CASE WHEN tipo_erro='ALUCINACAO_CODIGO' THEN 1 ELSE 0 END) AS alucinacoes,
  COUNT(*) AS prompts,
  ROUND(SUM(CASE WHEN tipo_erro='ALUCINACAO_CODIGO' THEN 1 ELSE 0 END)*100.0/COUNT(*),1) AS taxa_aluc,
  CASE prompt_categoria
    WHEN 'Conversa/Aberto'        THEN 'Converter aberto em estruturado: system prompt restritivo + few-shot + guardrails de escopo'
    WHEN 'Geracao de Codigo'      THEN 'Few-shot valido + exigir testes + validacao de sintaxe/execucao + RAG das docs da lib'
    WHEN 'Raciocinio/Analise'     THEN 'Decomposicao em etapas + verificacao por etapa + self-consistency'
    WHEN 'Extracao de Dados'      THEN 'JSON mode/schema + regex de validacao + exemplos entrada-saida'
    WHEN 'RAG/Busca'              THEN 'Melhorar retrieval (re-rank) + citar fontes + grounding obrigatorio'
    WHEN 'Transformacao/Formato'  THEN 'Templates fixos + exemplos de saida + JSON mode'
    WHEN 'Sumarizacao'            THEN 'Limites de tamanho + instrucoes de fidelidade + QA factual'
    ELSE 'Padronizar prompt + exemplos'
  END AS solucao
FROM logs_langfuse
GROUP BY project_name, prompt_categoria
ORDER BY project_name, alucinacoes DESC;
