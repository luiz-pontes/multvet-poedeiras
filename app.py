import weasyprint
from weasyprint import HTML

html_content = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>MultVet Poedeiras Caipiras - Arquitetura e Código do Mini App</title>
    <style>
        @page {
            size: A4;
            margin: 15mm 12mm;
            background-color: #F8F9FA;
        }
        *, *::before, *::after {
            box-sizing: border-box;
        }
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            color: #2D3748;
            font-size: 10pt;
            line-height: 1.4;
        }
        .header {
            background-color: #1B4D3E;
            color: white;
            padding: 20px 25px;
            margin: -15mm -12mm 20px -12mm;
            border-bottom: 4px solid #13382D;
        }
        .header h1 {
            margin: 0;
            font-size: 18pt;
            color: #FFFFFF !important;
            font-weight: bold;
        }
        .header p {
            margin: 5px 0 0 0;
            font-size: 11pt;
            opacity: 0.9;
        }
        .badge {
            display: inline-block;
            background-color: #E8F5E9;
            color: #1B4D3E;
            padding: 4px 10px;
            border-radius: 12px;
            font-weight: bold;
            font-size: 9pt;
            margin-top: 8px;
        }
        .section {
            background-color: #FFFFFF;
            border-radius: 8px;
            padding: 15px 20px;
            margin-bottom: 15px;
            border: 1px solid #E2E8F0;
            border-left: 5px solid #1B4D3E;
        }
        .section-title {
            color: #1B4D3E;
            font-size: 13pt;
            font-weight: bold;
            margin-top: 0;
            margin-bottom: 10px;
            border-bottom: 1px solid #E2E8F0;
            padding-bottom: 5px;
        }
        ul {
            margin: 0;
            padding-left: 20px;
        }
        li {
            margin-bottom: 6px;
        }
        pre {
            background-color: #1E1E1E;
            color: #D4D4D4;
            padding: 12px;
            border-radius: 6px;
            font-family: 'Courier New', Courier, monospace;
            font-size: 8.5pt;
            white-space: pre-wrap;
            word-wrap: break-word;
            overflow-x: auto;
        }
        .footer {
            margin-top: 25px;
            text-align: center;
            font-size: 9pt;
            color: #718096;
            border-top: 1px solid #E2E8F0;
            padding-top: 10px;
        }
    </style>
</head>
<body>

    <div class="header">
        <h1>🥚 MultVet Poedeiras Caipiras</h1>
        <p>Documentação de Arquitetura & Código Base do Segundo Mini App</p>
        <span class="badge">Expansão de Portfólio — Agrotech</span>
    </div>

    <div class="section">
        <div class="section-title">1. Visão Geral & Métricas Chave</div>
        <p>O Mini App de <strong>Poedeiras Caipiras (Ovos)</strong> foi projetado para calcular a eficiência de postura, consumo alimentar e lucratividade diária/mensal por dúzia de ovos produzida.</p>
        <ul>
            <li><strong>Taxa de Postura (%):</strong> (Ovos Coletados no Dia / Aves Vivas) × 100</li>
            <li><strong>Produção em Dúzias:</strong> Ovos Coletados / 12</li>
            <li><strong>Consumo Médio por Ave:</strong> (Ração Diária em Kg / Aves Vivas) × 1000 (g/ave/dia)</li>
            <li><strong>Custo por Dúzia:</strong> (Custo Diário de Ração + Custo Fixo Diário) / Dúzias Produzidas</li>
            <li><strong>Margem de Lucro (%):</strong> (Lucro Total / Receita Total) × 100</li>
        </ul>
    </div>

    <div class="section">
        <div class="section-title">2. Estrutura do Código em Python (Streamlit)</div>
        <pre><code>import streamlit as st

st.set_page_config(page_title="MultVet Poedeiras Caipiras", page_icon="🥚", layout="centered")

# Estilização Brand Board MultVet
st.markdown("""
    &lt;style&gt;
    .stApp { background-color: #F8F9FA; }
    h1, h2, h3 { color: #1B4D3E !important; }
    .resumo-card {
        background-color: #E8F5E9;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #1B4D3E;
        margin-bottom: 10px;
    }
    &lt;/style&gt;
""", unsafe_allow_html=True)

# Autenticação
SENHA_CORRETA = "multvet2026"
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

if not st.session_state["autenticado"]:
    st.title("🔒 Acesso Restrito - MultVet Poedeiras")
    senha = st.text_input("Digite sua senha de acesso:", type="password")
    if st.button("Acessar Calculadora"):
        if senha == SENHA_CORRETA:
            st.session_state["autenticado"] = True
            st.rerun()
        else:
            st.error("Senha incorreta.")
    st.stop()

st.title("🥚 MultVet Poedeiras Caipiras")
st.caption("Gestão de Postura, Consumo & Lucratividade por Dúzia")
st.markdown("---")

# Entradas
st.header("1. Dados do Plantel & Coleta Diária")
col1, col2 = st.columns(2)
with col1:
    aves_vivas = st.number_input("Aves vivas no lote", min_value=1, value=500, step=10)
    ovos_dia = st.number_input("Ovos coletados por dia", min_value=0, value=400, step=10)
with col2:
    racao_dia_kg = st.number_input("Ração consumida por dia (kg)", min_value=0.0, value=55.0, step=1.0)
    custo_kg_racao = st.number_input("Custo do kg da ração (R$)", min_value=0.0, value=2.10, step=0.05)

st.header("2. Custos Adicionais e Vendas")
col3, col4 = st.columns(2)
with col3:
    outros_custos_mes = st.number_input("Outros custos mensais (luz, embalagem, etc) (R$)", min_value=0.0, value=300.0, step=10.0)
with col4:
    preco_duzia = st.number_input("Preço de venda da dúzia (R$)", min_value=0.0, value=12.00, step=0.50)

# Cálculos
taxa_postura = (ovos_dia / aves_vivas * 100) if aves_vivas &gt; 0 else 0
duzias_dia = ovos_dia / 12
duzias_mes = duzias_dia * 30

consumo_ave_g = (racao_dia_kg / aves_vivas * 1000) if aves_vivas &gt; 0 else 0

custo_racao_dia = racao_dia_kg * custo_kg_racao
custo_fixo_dia = outros_custos_mes / 30
custo_total_dia = custo_racao_dia + custo_fixo_dia

custo_por_duzia = (custo_total_dia / duzias_dia) if duzias_dia &gt; 0 else 0
receita_dia = duzias_dia * preco_duzia
lucro_dia = receita_dia - custo_total_dia
lucro_mes = lucro_dia * 30
margem_lucro = (lucro_dia / receita_dia * 100) if receita_dia &gt; 0 else 0

# Exibição dos Resultados
st.markdown("---")
st.header("📊 Resultados Zootécnicos e Financeiros")

c_m1, c_m2, c_m3 = st.columns(3)
c_m1.metric("Taxa de Postura", f"{taxa_postura:.1f}%")
c_m2.metric("Custo por Dúzia", f"R$ {custo_por_duzia:.2f}")
c_m3.metric("Lucro Estimado (Mês)", f"R$ {lucro_mes:.2f}", delta=f"{margem_lucro:.1f}% Margem")

col_r1, col_r2 = st.columns(2)
with col_r1:
    st.markdown('&lt;div class="resumo-card"&gt;', unsafe_allow_html=True)
    st.subheader("Desempenho de Postura")
    st.write(f"• **Produção Diária:** {ovos_dia} ovos ({duzias_dia:.1f} dúzias/dia)")
    st.write(f"• **Produção Mensal:** {duzias_mes:.0f} dúzias/mês")
    st.write(f"• **Consumo por Ave:** {consumo_ave_g:.1f} g/ave/dia")
    st.markdown('&lt;/div&gt;', unsafe_allow_html=True)

with col_r2:
    st.markdown('&lt;div class="resumo-card"&gt;', unsafe_allow_html=True)
    st.subheader("Balanço Financeiro")
    st.write(f"• **Custo Total Diário:** R$ {custo_total_dia:.2f}")
    st.write(f"• **Receita Diária:** R$ {receita_dia:.2f}")
    st.write(f"• **Lucro por Dúzia:** R$ {(preco_duzia - custo_por_duzia):.2f}")
    st.markdown('&lt;/div&gt;', unsafe_allow_html=True)
</code></pre>
    </div>

    <div class="footer">
        MultVet Agrotech — Módulo de Expansão: Avicultura de Postura Caipira 🥚
    </div>

</body>
</html>
"""

with open("multvet_poedeiras_caipiras.html", "w", encoding="utf-8") as f:
    f.write(html_content)

HTML("multvet_poedeiras_caipiras.html").write_pdf("multvet_poedeiras_caipiras.pdf")
print("PDF do Mini App Poedeiras gerado com sucesso!")
