import streamlit as st

st.set_page_config(page_title="MultVet Poedeiras Caipiras", page_icon="🥚", layout="centered")

# Estilização Brand Board MultVet
st.markdown('''
    <style>
    .stApp { background-color: #F8F9FA; }
    h1, h2, h3 { color: #1B4D3E !important; }
    .resumo-card {
        background-color: #E8F5E9;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #1B4D3E;
        margin-bottom: 10px;
    }
    </style>
''', unsafe_allow_html=True)

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
taxa_postura = (ovos_dia / aves_vivas * 100) if aves_vivas > 0 else 0
duzias_dia = ovos_dia / 12
duzias_mes = duzias_dia * 30

consumo_ave_g = (racao_dia_kg / aves_vivas * 1000) if aves_vivas > 0 else 0

custo_racao_dia = racao_dia_kg * custo_kg_racao
custo_fixo_dia = outros_custos_mes / 30
custo_total_dia = custo_racao_dia + custo_fixo_dia

custo_por_duzia = (custo_total_dia / duzias_dia) if duzias_dia > 0 else 0
receita_dia = duzias_dia * preco_duzia
lucro_dia = receita_dia - custo_total_dia
lucro_mes = lucro_dia * 30
margem_lucro = (lucro_dia / receita_dia * 100) if receita_dia > 0 else 0

# Exibição dos Resultados
st.markdown("---")
st.header("📊 Resultados Zootécnicos e Financeiros")

c_m1, c_m2, c_m3 = st.columns(3)
c_m1.metric("Taxa de Postura", f"{taxa_postura:.1f}%")
c_m2.metric("Custo por Dúzia", f"R$ {custo_por_duzia:.2f}")
c_m3.metric("Lucro Estimado (Mês)", f"R$ {lucro_mes:.2f}", delta=f"{margem_lucro:.1f}% Margem")

col_r1, col_r2 = st.columns(2)
with col_r1:
    st.markdown('<div class="resumo-card">', unsafe_allow_html=True)
    st.subheader("Desempenho de Postura")
    st.write(f"• **Produção Diária:** {ovos_dia} ovos ({duzias_dia:.1f} dúzias/dia)")
    st.write(f"• **Produção Mensal:** {duzias_mes:.0f} dúzias/mês")
    st.write(f"• **Consumo por Ave:** {consumo_ave_g:.1f} g/ave/dia")
    st.markdown('</div>', unsafe_allow_html=True)

with col_r2:
    st.markdown('<div class="resumo-card">', unsafe_allow_html=True)
    st.subheader("Balanço Financeiro")
    st.write(f"• **Custo Total Diário:** R$ {custo_total_dia:.2f}")
    st.write(f"• **Receita Diária:** R$ {receita_dia:.2f}")
    st.write(f"• **Lucro por Dúzia:** R$ {(preco_duzia - custo_por_duzia):.2f}")
    st.markdown('</div>', unsafe_allow_html=True)
