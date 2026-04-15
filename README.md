# O-Mini-SQAP-C-digo-Limpo-Matriz-de-Risco
Qualidade de software
Quality Gate Policy (IEEE 730 – Enforcement Rules)
# Regra 01 — Bloqueio por Inconsistência Financeira (Hard Gate)
Nenhuma alteração pode ser promovida para produção sem validação automatizada de consistência transacional (saldo × desconto × pagamento).
Enforcement técnico:
Pipeline CI/CD falha automaticamente se:
Testes de validação financeira não passarem
Cobertura < 85% no domínio crítico (pricing)
Uso obrigatório de testes de contrato para regra de pagamento
# Regra 02 — Proibição de Acoplamento UI ↔ Regra de Negócio
Nenhuma lógica de desconto/cupom pode residir na camada de interface ou integração.
Enforcement técnico:
Static Code Analysis (lint + arquitetura)
Falha automática se:
Funções de domínio importarem frameworks externos (FastAPI, DB, etc.)
Revisão obrigatória via Pull Request com checklist arquitetural

# Sumário Executivo – Gestão de Risco (Matriz PxI)
Evento de Risco:
Despacho logístico sem validação de pagamento (cupom aplicado sem saldo disponível).
Classificação:
Probabilidade: Alta (processo inexistente)
Impacto: Crítico (perda financeira direta + ruptura operacional)
Nível: Risco Extremo (PxI = 5 × 5)
itigação via SQA (IEEE 730):

A política de Quality Gate implementa validação preventiva no pipeline, impedindo que código inconsistente avance no ciclo de entrega. Ao deslocar a validação para a origem (shift-left), eliminamos falhas sistêmicas antes da produção.
Isso reduz diretamente o Change Failure Rate (DORA) ao garantir que nenhuma regra de negócio crítica seja liberada sem validação automatizada e isolamento arquitetural, transformando qualidade de reativa (SQC) para preventiva (SQA).
