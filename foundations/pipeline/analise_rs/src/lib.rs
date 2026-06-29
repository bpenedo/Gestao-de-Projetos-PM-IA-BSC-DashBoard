// Classificador textual Lean (RATE_LIMIT / ALUCINACAO_CODIGO / NENHUM) em Rust.
// Comportamento idêntico ao fallback puro-Python (analise.py::_classificar_py),
// porém CPU-bound acelerado para milhões de logs. Exposto via PyO3 como `analise_rs.classificar`.
use pyo3::prelude::*;

const RATE: [&str; 4] = ["error 429", "rate limit", "quota exceeded", "too many requests"];
const CORR: [&str; 11] = [
    "está errado", "esta errado", "nao funcionou", "não funcionou", "corrija o erro",
    "corrija", "esta quebrado", "está quebrado", "gerou erro", "refaca", "refaça",
];
const ERRIA: [&str; 7] = [
    "traceback (most recent call last)", "syntaxerror:", "nameerror:",
    "exception occurred", "internal server error", "unhandled exception", "nullpointer",
];

#[pyfunction]
fn classificar(prompt: &str, resposta: &str) -> (String, f64) {
    let p = prompt.to_lowercase();
    let r = resposta.to_lowercase();

    if RATE.iter().any(|s| p.contains(s) || r.contains(s)) {
        return ("RATE_LIMIT".to_string(), 5.0);
    }
    if CORR.iter().any(|s| p.contains(s)) || ERRIA.iter().any(|s| r.contains(s)) {
        return ("ALUCINACAO_CODIGO".to_string(), 0.0);
    }
    if r.trim().chars().count() < 10 || r.ends_with("...") {
        return ("ALUCINACAO_CODIGO".to_string(), 0.0);
    }
    ("NENHUM".to_string(), 0.0)
}

#[pymodule]
fn analise_rs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(classificar, m)?)?;
    Ok(())
}
