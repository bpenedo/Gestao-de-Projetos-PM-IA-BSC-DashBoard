# ⚡ PERFORMANCE — Python tradicional vs Concorrente + Rust
> **Framework Gestão de Projetos (PM) IA com Painel BSC e DashBoard** · ©️ Bruno Penedo — 2026. https://linkedin.com/in/bpenedo - E-mail: bpenedo@gmail.com
> Classificacao e fetch MEDIDOS; cenario de producao modela
> fetch por latencia/pagina (~100ms) e usa a vazao medida da classificacao.

## Tabela comparativa (janela temporal em segundos)
| Etapa                              | Py tradic.(s)| Conc.+Rust(s)|  Ganho(s) | Ganho% |
|------------------------------------|-------------:|-------------:|----------:|-------:|
| Fetch I/O (24 pag, lat 50ms) MEDIDO|        1.210 |        0.303 |      0.907 |   75.0% |
| Classificacao 500k logs   MEDIDO  |        1.328 |        0.482 |      0.845 |   63.7% |
| CENARIO PROD: 500k/5000pag        |      501.328 |      125.482 |    375.845 |   75.0% |

## Sumario executivo

=== SUMARIO EXECUTIVO ===
- Classificacao (CPU): Python 1.328s -> Rust 0.482s  | ganho 0.845s (63.7%), 2.8x
- Fetch (I/O): sequencial 1.210s -> concorrente 0.303s | ganho 0.907s (75.0%), 4.0x
- CENARIO PROD (500k logs): 501.3s -> 125.5s | GANHO 375.8s (75.0%)

