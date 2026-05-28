import streamlit as st
from fpdf import FPDF

# Configuração da página (deve ser sempre a primeira linha do Streamlit)
st.set_page_config(page_title="Dieta FIT", page_icon="💪", layout="centered")

# ── FUNÇÃO PARA GERAR O PDF EM MEMÓRIA ─────────────────────────────
def criar_pdf(nome, peso, altura, idade, imc, classe_imc, tmb, tdee, kcal, proteina, gordura, carbo, fibra, perda_kg_semana):
    pdf = FPDF()
    pdf.add_page()
    
    # Cores e Fontes (Título Principal)
    pdf.set_font("helvetica", "B", 20)
    pdf.set_text_color(15, 76, 92) # Azul escuro
    pdf.cell(0, 10, "Plano Alimentar FIT", align="C", new_x="LMARGIN", new_y="NEXT")
    
    # Subtítulo do Objetivo
    pdf.set_font("helvetica", "I", 12)
    pdf.set_text_color(227, 100, 20) # Laranja
    pdf.cell(0, 8, "Foco: Perda de Peso & Preservacao de Massa Magra", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)

    # 1. Seção: Dados do Paciente
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(15, 76, 92)
    pdf.cell(0, 10, "1. Dados do Paciente", border="B", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("helvetica", "", 12)
    pdf.set_text_color(44, 62, 80)
    pdf.cell(0, 8, f"Nome: {nome}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(100, 8, f"Peso Atual: {peso} kg")
    pdf.cell(0, 8, f"Altura: {altura} cm", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(100, 8, f"Idade: {idade} anos", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    # 2. Seção: Avaliação Metabólica
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(15, 76, 92)
    pdf.cell(0, 10, "2. Avaliacao Metabolica", border="B", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("helvetica", "", 12)
    pdf.set_text_color(44, 62, 80)
    pdf.cell(100, 8, f"IMC Atual: {imc:.1f} ({classe_imc})")
    pdf.cell(0, 8, f"Metabolismo Basal (TMB): {tmb:.0f} kcal/dia", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(100, 8, f"Gasto Diario Total (TDEE): {tdee:.0f} kcal/dia", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    # 3. Seção: Metas de Calorias e Macros
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(15, 76, 92)
    pdf.cell(0, 10, "3. Meta Calorica e Macronutrientes", border="B", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(227, 100, 20)
    pdf.cell(0, 8, f"ALVO DIARIO: {kcal:.0f} kcal (Deficit de {tdee - kcal:.0f} kcal)", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("helvetica", "", 12)
    pdf.set_text_color(44, 62, 80)
    pdf.cell(0, 8, f"- Proteina: {proteina:.1f} g ({proteina * 4:.0f} kcal)", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 8, f"- Carboidrato: {carbo:.1f} g ({carbo * 4:.0f} kcal)", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 8, f"- Gordura: {gordura:.1f} g ({gordura * 9:.0f} kcal)", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 8, f"- Fibra Alimentar: {fibra:.1f} g (Minimo)", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    # 4. Seção: Projeções Estimadas de Resultados
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(15, 76, 92)
    pdf.cell(0, 10, "4. Projecao Estimada", border="B", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("helvetica", "", 12)
    pdf.set_text_color(44, 62, 80)
    pdf.cell(0, 8, f"Perda estimada por semana: ~{perda_kg_semana:.2f} kg", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 8, f"Perda estimada por mes: ~{perda_kg_semana * 4:.2f} kg", new_x="LMARGIN", new_y="NEXT")
    
    # 5. Seção: Caixa de Aviso e Ressalva sobre o IMC (AGORA INCLUÍDA NO PDF)
    pdf.ln(10)
    
    # Título do Alerta em Vermelho
    pdf.set_font("helvetica", "B", 11)
    pdf.set_text_color(200, 50, 50)
    pdf.cell(0, 6, "AVISO IMPORTANTE SOBRE O IMC:", new_x="LMARGIN", new_y="NEXT")
    
    # Corpo de Texto explicativo
    pdf.set_font("helvetica", "", 10)
    pdf.set_text_color(100, 100, 100) # Cinza escuro para leitura confortável
    aviso_imc = (
        "O IMC e uma metrica geral e nao diferencia massa muscular de gordura corporal. "
        "Individuos muito musculosos (como atletas) podem apresentar um IMC na faixa de "
        "'Sobrepeso' ou 'Obesidade' mesmo tendo um percentual de gordura muito baixo. "
        "Portanto, o IMC nao deve ser avaliado isoladamente. Para uma avaliacao precisa, "
        "um profissional deve medir sua composicao corporal utilizando metodos especificos "
        "(como dobras cutaneas ou bioimpedancia)."
    )
    pdf.multi_cell(0, 5, aviso_imc)
    
    # Rodapé Legal / Isenção de responsabilidade
    pdf.ln(8)
    pdf.set_font("helvetica", "I", 9)
    pdf.set_text_color(150, 150, 150)
    pdf.multi_cell(0, 5, "Nota legal: Este documento e uma estimativa matematica calculada via software. Procure sempre um nutricionista registrado para a prescricao de um plano alimentar individualizado.")

    # Retorna o PDF compilado em bytes pronto para o botão do Streamlit
    return bytes(pdf.output())


# ── CONSTRUÇÃO DA INTERFACE VISUAL (STREAMLIT) ─────────────────────

# Elementos de Cabeçalho da Página Web
st.title("💪 Calculadora de Dieta FIT")
st.markdown("Calcule seus macronutrientes para perda de peso com foco na preservação de massa muscular.")
st.divider()

# Formulário de entrada de dados do Paciente
st.subheader("👤 Seus Dados")
nome = st.text_input("Informe o seu nome:")

# Divisão em duas colunas simétricas para um layout limpo
col1, col2 = st.columns(2)
with col1:
    peso = st.number_input("Peso (kg)", min_value=30.0, max_value=300.0, value=70.0, step=0.1)
    altura = st.number_input("Altura (cm)", min_value=100.0, max_value=250.0, value=170.0, step=1.0)

with col2:
    idade = st.number_input("Idade", min_value=15, max_value=100, value=25, step=1)
    sexo = st.radio("Sexo", ["Masculino", "Feminino"])

st.write("") # Pequeno espaçador vertical
niveis = {
    "Sedentário (pouco ou nenhum exercício)": 1.2,
    "Levemente ativo (exercício leve 1-3 dias/semana)": 1.375,
    "Moderadamente ativo (exercício moderado 3-5 dias/semana)": 1.55,
    "Muito ativo (exercício intenso 6-7 dias/semana)": 1.725,
    "Extremamente ativo (exercício intenso diário ou trabalho físico)": 1.9
}
nivel_escolhido = st.selectbox("Nível de Atividade Física", list(niveis.keys()))

st.divider()

# Inicialização da Ação de Processamento
if st.button("Calcular Dieta", type="primary", use_container_width=True):
    
    if not nome:
        st.warning("⚠️ Por favor, informe o seu nome lá em cima para gerar o plano.")
    else:
        # Conversão das entradas visuais para variáveis de cálculo
        fator = niveis[nivel_escolhido]
        sexo_letra = 'M' if sexo == "Masculino" else 'F'

        # Cálculo matemático do IMC único baseado em metros
        imc = peso / ((altura / 100) ** 2)

        if imc < 18.5:
            st.error(f"🚨 Atenção, {nome}: seu IMC ({imc:.1f}) indica abaixo do peso.")
            st.write("Uma dieta de emagrecimento pode ser prejudicial. Consulte um médico ou nutricionista antes de continuar.")
        else:
            # Cálculo de TMB utilizando a Equação de Mifflin-St Jeor
            if sexo_letra == 'M':
                tmb = (10 * peso) + (6.25 * altura) - (5 * idade) + 5
                kcal_min = 1500
            else:
                tmb = (10 * peso) + (6.25 * altura) - (5 * idade) - 161
                kcal_min = 1200
            
            # Cálculo de Gasto Diário (TDEE) e aplicação do Deficit Inicial (20%)
            tdee = tmb * fator
            kcal = tdee * 0.80

            # Filtros de Segurança Contra Deficits Abusivos/Extremos
            if kcal < kcal_min:
                kcal = kcal_min
                st.toast(f"Deficit ajustado para o mínimo seguro: {kcal_min} kcal", icon="⚠️")
            if (tdee - kcal) > 1000:
                kcal = tdee - 1000
                st.toast("Deficit limitado a 1000 kcal/dia para segurança.", icon="⚠️")

            # Cálculo de Macronutrientes Focado na Preservação Muscular
            proteina = peso * 1.8
            gordura  = peso * 0.9
            fibra    = (kcal / 1000) * 14
            carbo    = (kcal - (proteina * 4) - (gordura * 9)) / 4

            # Gestão automática de carboidratos negativos para manter as proteínas intocadas
            if carbo < 0:
                st.warning("⚠️ Carboidratos negativos detectados. Ajustando gordura para garantir a proteína.")
                carbo = 0
                gordura = (kcal - (proteina * 4)) / 9
            elif carbo < 50:
                st.info("💡 A dieta resultou em carboidratos baixos (Low Carb) para não comprometer sua proteína.")

            # Cálculo Matemático das Estimativas de Emagrecimento Semanal/Mensal
            deficit_semanal = (tdee - kcal) * 7
            perda_kg_semana = deficit_semanal / 7700

            # Atribuição da Classificação de Faixa do IMC
            if imc < 25: classe_imc = 'Peso normal'
            elif imc < 30: classe_imc = 'Sobrepeso'
            elif imc < 35: classe_imc = 'Obesidade grau I'
            elif imc < 40: classe_imc = 'Obesidade grau II'
            else: classe_imc = 'Obesidade grau III'

            # ── EXIBIÇÃO DE RESULTADOS NA TELA WEB ────────────────────────
            st.success(f"Plano gerado com sucesso para **{nome}**!")

            # Blocos de métricas com visual moderno (Métricas de Metabolismo)
            st.subheader("📊 Avaliação de Metabolismo")
            col_m1, col_m2, col_m3 = st.columns(3)
            col_m1.metric("IMC", f"{imc:.1f}", classe_imc, delta_color="off")
            col_m2.metric("TMB (Basal)", f"{tmb:.0f} kcal")
            col_m3.metric("Gasto Total (TDEE)", f"{tdee:.0f} kcal")

            # Alvo calórico principal em destaque
            st.subheader("🎯 Meta Diária")
            st.metric("Calorias para Consumir", f"{kcal:.0f} kcal", f"-{tdee - kcal:.0f} kcal (Deficit diário)")

            # Divisão dos 4 macros em blocos horizontais organizados
            st.subheader("🍽️ Seus Macronutrientes")
            col_mac1, col_mac2, col_mac3, col_mac4 = st.columns(4)
            col_mac1.metric("🥩 Proteína", f"{proteina:.0f}g")
            col_mac2.metric("🍚 Carboidrato", f"{carbo:.0f}g")
            col_mac3.metric("🥑 Gordura", f"{gordura:.0f}g")
            col_mac4.metric("🌿 Fibras", f"{fibra:.0f}g")

            # Texto simples com projeção de emagrecimento teórico
            st.subheader("📉 Estimativa de Emagrecimento")
            st.write(f"🔹 **Por semana:** ~{perda_kg_semana:.2f} kg")
            st.write(f"🔹 **Por mês (4 semanas):** ~{perda_kg_semana * 4:.2f} kg")

            # ── CONSTRUTOR NATIVO DO BOTÃO DE DOWNLOAD ────────────────────
            st.divider()
            
            # Gera os bytes finais chamando a função atualizada
            pdf_final = criar_pdf(nome, peso, altura, idade, imc, classe_imc, tmb, tdee, kcal, proteina, gordura, carbo, fibra, perda_kg_semana)
            
            # Componente de Download em Destaque (Estilo de Botão Primário Azul)
            st.download_button(
                label="📥 Baixar Plano Completo em PDF",
                data=pdf_final,
                file_name=f"Plano_Dieta_{nome.replace(' ', '_')}.pdf",
                mime="application/pdf",
                type="primary"
            )
            
            # Acordeão expansível de aviso sobre a relatividade do IMC na web
            with st.expander("⚠️ Leia: Aviso sobre o IMC"):
                st.write("""
                O IMC é uma métrica geral e não diferencia massa muscular de gordura corporal. 
                Indivíduos muito musculosos (como atletas) podem apresentar um IMC na faixa de 
                "Sobrepeso" ou "Obesidade" mesmo tendo um percentual de gordura muito baixo. 
                Portanto, o IMC não deve ser avaliado isoladamente. Para uma avaliação precisa, 
                um profissional deve medir sua composição corporal utilizando métodos específicos.
                """)
            
            # Assinatura de rodapé amigável
            st.caption(f"Este cálculo é uma estimativa, {nome.split()[0]}. Consulte um nutricionista para um plano alimentar personalizado.")