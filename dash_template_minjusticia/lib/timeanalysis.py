import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
from lifelines import KaplanMeierFitter
from datetime import datetime, timedelta
from pathlib import Path
import os.path
#from lifelines import KaplanMeierFitter, CoxPHFitter


from datetime import datetime as dt
import json
import numpy as np
import pandas as pd

#Recall app
from app import app
try:
    if os.path.exists('output_data/time_analysis_df.csv'):
        df_mj_mod = pd.read_csv('output_data/time_analysis_df.csv',parse_dates=['FECHA_INGRESO','FECHA_SALIDA','FECHA_CAPTURA'])
    else:
        df_mj = pd.read_csv('data/reincidencia11junio2020_clean.csv', parse_dates=['FECHA_INGRESO','FECHA_SALIDA','FECHA_CAPTURA'])

        df_mj_mod = df_mj.copy()

        #Date variables are parsed to datetime
        df_mj_mod["FECHA_CAPTURA"] = pd.to_datetime(df_mj_mod["FECHA_CAPTURA"])
        df_mj_mod["FECHA_INGRESO"] = pd.to_datetime(df_mj_mod["FECHA_INGRESO"])
        df_mj_mod["FECHA_SALIDA"] = pd.to_datetime(df_mj_mod["FECHA_SALIDA"])
        #Month and year variables are defined
        df_mj_mod["MES_INGRESO_INT"]=df_mj_mod["FECHA_INGRESO"].dt.strftime('%m')
        df_mj_mod["ANO_INGRESO_INT"]=df_mj_mod["FECHA_INGRESO"].dt.strftime('%y')
        #Calculations on how much time have the criminal being outside since its last stay in jail
        for column in ['FECHA_INGRESO', 'FECHA_SALIDA', 'FECHA_CAPTURA']:
            df_mj_mod = df_mj_mod.sort_values(['INTERNOEN', column], ascending = False)

            df_mj_mod['DIAS' + column[5:]] = -1*(df_mj_mod[column].diff()/timedelta(days = 1))

            df_mj_mod.loc[(df_mj_mod.INTERNOEN != df_mj_mod.INTERNOEN.shift(1)) | (df_mj_mod['DIAS' + column[5:]] == 0),
                      ['DIAS' + column[5:]]] = (datetime.today() - df_mj_mod[column])/timedelta(days = 1)

        #It seems that sometimes entering and gettint out is switched, that's why we computed in absolute values
        df_mj_mod['DIAS_CONDENA'] = abs(df_mj_mod['FECHA_SALIDA'] - df_mj_mod['FECHA_INGRESO'])/timedelta(days = 1)
        df_mj_mod['DIAS_JUDICIALIZACION'] = df_mj_mod['FECHA_INGRESO'] - df_mj_mod['FECHA_CAPTURA']
        df_mj_mod['DIAS_LIBRE'] = df_mj_mod['DIAS_INGRESO'] - df_mj_mod['DIAS_CONDENA']
        #The individual finishes its sentence but she's incarcelated inmediately for another crime
        df_mj_mod.loc[df_mj_mod.DIAS_CAPTURA < 0, 'DIAS_CAPTURA'] = 0
        df_mj_mod.loc[df_mj_mod.DIAS_INGRESO < 0, 'DIAS_INGRESO'] = 0
        df_mj_mod.loc[df_mj_mod.DIAS_LIBRE < 0, 'DIAS_LIBRE'] = 0
        #The individual is still on jail
        df_mj_mod.loc[df_mj_mod['DIAS_LIBRE'].isnull(), 'DIAS_LIBRE'] = 0

        #Find the last date the criminal went out the jail, so that these observations are marked as censored
        last_df = df_mj_mod[['INTERNOEN', 'FECHA_INGRESO']].groupby('INTERNOEN').apply(lambda x: x.sort_values('FECHA_INGRESO', ascending = False).head(1)).reset_index(drop = True)
        #Censored
        last_df['CENSURADO_LIBRES'] = 0
        df_mj_mod = df_mj_mod.merge(last_df, on = ['INTERNOEN', 'FECHA_INGRESO'], how = 'left')
        #Event
        df_mj_mod.loc[df_mj_mod['CENSURADO_LIBRES'].isnull(), 'CENSURADO_LIBRES'] = 1
        #All criminals that haven't got out of jail yet have zero days out and they are not censored.
        df_mj_mod.loc[df_mj_mod['FECHA_SALIDA'].isnull(), 'CENSURADO_LIBRES'] = 1
        #Turned censored variables to integers instead of float
        df_mj_mod['CENSURADO_LIBRES'] = df_mj_mod['CENSURADO_LIBRES'].astype('int64')

        #We create a variable to count the amount of times the individual re-entered in jail
        df_mj_mod = df_mj_mod.merge(df_mj_mod.drop_duplicates(['INTERNOEN', 'FECHA_INGRESO']).groupby(['INTERNOEN']).size().reset_index(name = 'NUMERO_REINCIDENCIAS'), on = 'INTERNOEN', how = 'left')

        #We dropped SITUACION_JURIDICA and REINCIDENTE as both columns are constants
        df_mj_mod = df_mj_mod.drop(columns = ['SITUACION_JURIDICA', 'REINCIDENTE'])

        df_mj_mod.to_csv('output_data/time_analysis_df.csv',index=False)
except:
    df_mj = pd.read_csv('../retomintic/Data_UpdateJune13/reincidencia11junio2020_clean.csv', parse_dates=['FECHA_INGRESO','FECHA_SALIDA','FECHA_CAPTURA'])

    df_mj_mod = df_mj.copy()

    #Date variables are parsed to datetime
    df_mj_mod["FECHA_CAPTURA"] = pd.to_datetime(df_mj_mod["FECHA_CAPTURA"])
    df_mj_mod["FECHA_INGRESO"] = pd.to_datetime(df_mj_mod["FECHA_INGRESO"])
    df_mj_mod["FECHA_SALIDA"] = pd.to_datetime(df_mj_mod["FECHA_SALIDA"])
    #Month and year variables are defined
    df_mj_mod["MES_INGRESO_INT"]=df_mj_mod["FECHA_INGRESO"].dt.strftime('%m')
    df_mj_mod["ANO_INGRESO_INT"]=df_mj_mod["FECHA_INGRESO"].dt.strftime('%y')
    #Calculations on how much time have the criminal being outside since its last stay in jail
    for column in ['FECHA_INGRESO', 'FECHA_SALIDA', 'FECHA_CAPTURA']:
        df_mj_mod = df_mj_mod.sort_values(['INTERNOEN', column], ascending = False)

        df_mj_mod['DIAS' + column[5:]] = -1*(df_mj_mod[column].diff()/timedelta(days = 1))

        df_mj_mod.loc[(df_mj_mod.INTERNOEN != df_mj_mod.INTERNOEN.shift(1)) | (df_mj_mod['DIAS' + column[5:]] == 0),
                  ['DIAS' + column[5:]]] = (datetime.today() - df_mj_mod[column])/timedelta(days = 1)

    #It seems that sometimes entering and gettint out is switched, that's why we computed in absolute values
    df_mj_mod['DIAS_CONDENA'] = abs(df_mj_mod['FECHA_SALIDA'] - df_mj_mod['FECHA_INGRESO'])/timedelta(days = 1)
    df_mj_mod['DIAS_JUDICIALIZACION'] = df_mj_mod['FECHA_INGRESO'] - df_mj_mod['FECHA_CAPTURA']
    df_mj_mod['DIAS_LIBRE'] = df_mj_mod['DIAS_INGRESO'] - df_mj_mod['DIAS_CONDENA']
    #The individual finishes its sentence but she's incarcelated inmediately for another crime
    df_mj_mod.loc[df_mj_mod.DIAS_CAPTURA < 0, 'DIAS_CAPTURA'] = 0
    df_mj_mod.loc[df_mj_mod.DIAS_INGRESO < 0, 'DIAS_INGRESO'] = 0
    df_mj_mod.loc[df_mj_mod.DIAS_LIBRE < 0, 'DIAS_LIBRE'] = 0
    #The individual is still on jail
    df_mj_mod.loc[df_mj_mod['DIAS_LIBRE'].isnull(), 'DIAS_LIBRE'] = 0

    #Find the last date the criminal went out the jail, so that these observations are marked as censored
    last_df = df_mj_mod[['INTERNOEN', 'FECHA_INGRESO']].groupby('INTERNOEN').apply(lambda x: x.sort_values('FECHA_INGRESO', ascending = False).head(1)).reset_index(drop = True)
    #Censored
    last_df['CENSURADO_LIBRES'] = 0
    df_mj_mod = df_mj_mod.merge(last_df, on = ['INTERNOEN', 'FECHA_INGRESO'], how = 'left')
    #Event
    df_mj_mod.loc[df_mj_mod['CENSURADO_LIBRES'].isnull(), 'CENSURADO_LIBRES'] = 1
    #All criminals that haven't got out of jail yet have zero days out and they are not censored.
    df_mj_mod.loc[df_mj_mod['FECHA_SALIDA'].isnull(), 'CENSURADO_LIBRES'] = 1
    #Turned censored variables to integers instead of float
    df_mj_mod['CENSURADO_LIBRES'] = df_mj_mod['CENSURADO_LIBRES'].astype('int64')

    #We create a variable to count the amount of times the individual re-entered in jail
    df_mj_mod = df_mj_mod.merge(df_mj_mod.drop_duplicates(['INTERNOEN', 'FECHA_INGRESO']).groupby(['INTERNOEN']).size().reset_index(name = 'NUMERO_REINCIDENCIAS'), on = 'INTERNOEN', how = 'left')

    #We dropped SITUACION_JURIDICA and REINCIDENTE as both columns are constants
    df_mj_mod = df_mj_mod.drop(columns = ['SITUACION_JURIDICA', 'REINCIDENTE'])

    df_mj_mod.to_csv('output_data/time_analysis_df.csv',index=False)


# df_km = df_mj_mod[['INTERNOEN', 'FECHA_INGRESO', 'DIAS_LIBRE', 'CENSURADO_LIBRES', 'ANO_INGRESO_INT', 'NUMERO_REINCIDENCIAS']].groupby('INTERNOEN').apply(lambda x: x.sort_values('FECHA_INGRESO', ascending = False).tail(1)).reset_index(drop = True)
# A = df_mj_mod[['INTERNOEN', 'FECHA_INGRESO']].apply(lambda x: x['INTERNOEN'] +  str(x['FECHA_INGRESO']), axis = 1)
# B = df_km[['INTERNOEN', 'FECHA_INGRESO']].apply(lambda x: x['INTERNOEN'] + str(x['FECHA_INGRESO']), axis = 1)

# diff = set(A).difference(set(B))
# where_diff = A.isin(diff)

# df_kmkm = df_mj_mod.loc[where_diff, ['INTERNOEN', 'FECHA_INGRESO', 'DIAS_LIBRE', 'CENSURADO_LIBRES', 'ANO_INGRESO_INT', 'NUMERO_REINCIDENCIAS']].groupby('INTERNOEN').apply(lambda x: x.sort_values('FECHA_INGRESO', ascending = False).tail(1)).reset_index(drop = True)

# C = df_kmkm[['INTERNOEN', 'FECHA_INGRESO']].apply(lambda x: x['INTERNOEN'] + str(x['FECHA_INGRESO']), axis = 1)

# diff = diff.difference(set(C))
# where_diff = A.isin(diff)

# df_kmkmkm = df_mj_mod.loc[where_diff, ['INTERNOEN', 'FECHA_INGRESO', 'DIAS_LIBRE', 'CENSURADO_LIBRES', 'ANO_INGRESO_INT', 'NUMERO_REINCIDENCIAS']].groupby('INTERNOEN').apply(lambda x: x.sort_values('FECHA_INGRESO', ascending = False).tail(1)).reset_index(drop = True)

# D = df_kmkmkm[['INTERNOEN', 'FECHA_INGRESO']].apply(lambda x: x['INTERNOEN'] + str(x['FECHA_INGRESO']), axis = 1)

# diff = diff.difference(set(D))
# where_diff = A.isin(diff)

# df_kmkmkmkm = df_mj_mod.loc[where_diff, ['INTERNOEN', 'FECHA_INGRESO', 'DIAS_LIBRE', 'CENSURADO_LIBRES', 'ANO_INGRESO_INT', 'NUMERO_REINCIDENCIAS']].groupby('INTERNOEN').apply(lambda x: x.sort_values('FECHA_INGRESO', ascending = False).tail(1)).reset_index(drop = True)

# E = df_kmkmkmkm[['INTERNOEN', 'FECHA_INGRESO']].apply(lambda x: x['INTERNOEN'] + str(x['FECHA_INGRESO']), axis = 1)

# diff = diff.difference(set(E))
# where_diff = A.isin(diff)

# df_kmkmkmkmkm = df_mj_mod.loc[where_diff, ['INTERNOEN', 'FECHA_INGRESO', 'DIAS_LIBRE', 'CENSURADO_LIBRES', 'ANO_INGRESO_INT', 'NUMERO_REINCIDENCIAS']].groupby('INTERNOEN').apply(lambda x: x.sort_values('FECHA_INGRESO', ascending = False).tail(1)).reset_index(drop = True)


df_gen_fin = df_mj_mod.groupby(['INTERNOEN', 'GENERO'])['DIAS_CONDENA'].mean().reset_index(name = 'DIAS_CONDENA')
df_gen_fin.columns = ['ID', 'GENERO', 'DIAS_CONDENA']
#print(df_gen_fin)
df_gen_fin['GENERO'].replace({"MASCULINO": "Masculino", "FEMENINO": "Femenino"}, inplace=True)

fig_genero = px.box(
    df_gen_fin,
    x='GENERO',
    y='DIAS_CONDENA',
    color = 'GENERO',
    width=800, height=400)
fig_genero.update_layout(title='NUMERO TOTAL DE DIAS FUERA DE LA CARCEL',paper_bgcolor="#F8F9F9")

df = df_mj_mod.drop_duplicates(['INTERNOEN', 'FECHA_INGRESO']).groupby(['INTERNOEN', 'ACTIVIDADES_ESTUDIO'])['DIAS_CONDENA'].mean().reset_index(name = 'DIAS_CONDENA')
df.columns = ['id', 'Actividades de estudio', 'Días de condena']
df['Actividades de estudio'] = df['Actividades de estudio'].str.capitalize()

fig_act_est = px.box(
    df,
    x= 'Actividades de estudio',
    y='Días de condena',
    color = 'Actividades de estudio',
    width=800, height=400)
fig_act_est.update_layout(title='NUMERO DE DIAS EN LA CARCEL POR ACTIVIDADES DE EDUCACION',paper_bgcolor="#F8F9F9")

df = df_mj_mod.groupby(['INTERNOEN', 'ACTIVIDADES_ESTUDIO'])['DIAS_LIBRE'].mean().reset_index(name = 'DIAS_LIBRE')
df.columns = ['id', 'Actividades de estudio', 'Días en libertad']
df['Actividades de estudio'] = df['Actividades de estudio'].str.capitalize()

fig_freedom_days = px.box(
    df,
    x= 'Actividades de estudio',
    y='Días en libertad',
    color = 'Actividades de estudio',
    width=800, height=400)
fig_freedom_days.update_layout(title='NUMERO DE DÍAS EN LIBERTAD POR ACTIVIDADES DE EDUCACIÓN',paper_bgcolor="#F8F9F9", height=500)

df = df_mj_mod.groupby(['INTERNOEN', 'ACTIVIDADES_ENSEÑANZA'])['DIAS_CONDENA'].mean().reset_index(name = 'DIAS_CONDENA')
df.columns = ['id', 'Actividades de enseñanza', 'Días de condena']
df['Actividades de enseñanza'] = df['Actividades de enseñanza'].str.capitalize()

fig_teach = px.box(
    df,
    x= 'Actividades de enseñanza',
    y='Días de condena',
    color = 'Actividades de enseñanza',
    width=800, height=400)
fig_teach.update_layout(title='DIAS DE CONDENA VS. PERSONAS QUE REALIZAN ACTIVIDADES DE ENSEÑANZA',paper_bgcolor="#F8F9F9", height=500)

df = df_mj_mod.groupby(['INTERNOEN', 'ACTIVIDADES_ENSEÑANZA'])['DIAS_LIBRE'].mean().reset_index(name = 'DIAS_LIBRE')
df.columns = ['id', 'Actividades de enseñanza', 'Días en libertad']
df['Actividades de estudio'] = df['Actividades de enseñanza'].str.capitalize()

fig_freedom_teach = px.box(
    df,
    x= 'Actividades de enseñanza',
    y='Días en libertad',
    color = 'Actividades de enseñanza',
    width=800, height=400)
fig_freedom_teach.update_layout(title='DIAS EN LIBERTAD VS. PERSONAS QUE REALIZAN ACTIVIDADES DE ENSEÑANZA',paper_bgcolor="#F8F9F9", height=500)

df = df_mj_mod.groupby(['INTERNOEN', 'ACTIVIDADES_TRABAJO'])['DIAS_CONDENA'].mean().reset_index(name = 'DIAS_CONDENA')
df.columns = ['id', 'Actividades de trabajo', 'Días de condena']
df['Actividades de trabajo'] = df['Actividades de trabajo'].str.capitalize()

fig_work = px.box(
    df,
    x= 'Actividades de trabajo',
    y='Días de condena',
    color = 'Actividades de trabajo',
    width=800, height=400)
fig_work.update_layout(title='DIAS DE CONDENA VS. ACTIVIDADES DE TRABAJO',paper_bgcolor="#F8F9F9", height=500)

df = df_mj_mod.groupby(['INTERNOEN', 'ACTIVIDADES_TRABAJO'])['DIAS_LIBRE'].mean().reset_index(name = 'DIAS_LIBRE')
df.columns = ['id', 'Actividades de trabajo', 'Días en libertad']
df['Actividades de trabajo'] = df['Actividades de trabajo'].str.capitalize()

fig_freedom_work = px.box(
    df,
    x= 'Actividades de trabajo',
    y='Días en libertad',
    color = 'Actividades de trabajo',
    width=800, height=400)
fig_freedom_work.update_layout(title='DIAS EN LIBERTAD VS. ACTIVIDADES DE TRABAJO',paper_bgcolor="#F8F9F9", height=500)

### Survival graphs

fig_surv_1 = go.Figure()

# for i in [0, 1]:
#     kmf = KaplanMeierFitter()
#     kmf.fit(df_km.loc[df_km['NUMERO_REINCIDENCIAS']>i,'DIAS_LIBRE'], df_km.loc[df_km['NUMERO_REINCIDENCIAS']>i, 'CENSURADO_LIBRES'])

#     if i == 0:
#         name= 'Días fuera de la cárcel (95% IC)'
#         fillcolor='rgba(0,176,246,0.2)'
#         line_color='rgba(255,255,255,0)'
#         line_color_l='rgb(0,176,246)'
#     else:
#         name = 'Días fuera de la cárcel sólo con reincidentes (95% IC)'
#         fillcolor='rgba(231,107,243,0.2)'
#         line_color='rgba(255,255,255,0)'
#         line_color_l='rgb(231,107,243)'

#     df = kmf.survival_function_.reset_index()
#     df.columns = ['Dias', 'Probabilidad de pasar más días afuera']

#     df_interval = kmf.confidence_interval_survival_function_.reset_index()
#     df_interval.columns = ['Dias', 'lwr', 'upr']

#     fig_surv_1.add_trace(go.Scatter(
#         x=list(df_interval.Dias)+list(df_interval.Dias)[::-1],
#         y=list(df_interval.upr)+list(df_interval.lwr)[::-1],
#         fill='toself',
#         fillcolor=fillcolor,
#         line_color=line_color,
#         showlegend=False,
#         name=name
#     ))
#     fig_surv_1.add_trace(go.Scatter(
#         x=df['Dias'],
#         y=df['Probabilidad de pasar más días afuera'],
#         line_color=line_color_l,
#         name=name
#     ))

# fig_surv_1.update_layout(
#     xaxis_title ="Días",
#     yaxis_title = "P(t > T)",
#     title = 'Días entre la primera y segunda reincidencia',
#     font=dict(
#         family="Courier New, monospace",
#         size=18,
#         color="#7f7f7f"
#     ),
#     width=800, height=400
# )

# fig_surv_1.update_traces(mode='lines')

# fig_surv_2 = go.Figure()

# for i in [0, 2]:
#     kmf = KaplanMeierFitter()
#     kmf.fit(df_kmkm.loc[df_kmkm['NUMERO_REINCIDENCIAS']>i,'DIAS_LIBRE'], df_kmkm.loc[df_kmkm['NUMERO_REINCIDENCIAS']>i, 'CENSURADO_LIBRES'])

#     if i == 0:
#         name= 'Días fuera de la cárcel (95% IC)'
#         fillcolor='rgba(0,176,246,0.2)'
#         line_color='rgba(255,255,255,0)'
#         line_color_l='rgb(0,176,246)'
#     else:
#         name = 'Días fuera de la cárcel sólo con reincidentes (95% IC)'
#         fillcolor='rgba(231,107,243,0.2)'
#         line_color='rgba(255,255,255,0)'
#         line_color_l='rgb(231,107,243)'

#     df = kmf.survival_function_.reset_index()
#     df.columns = ['Dias', 'Probabilidad de pasar más días afuera']

#     df_interval = kmf.confidence_interval_survival_function_.reset_index()
#     df_interval.columns = ['Dias', 'lwr', 'upr']

#     fig_surv_2.add_trace(go.Scatter(
#         x=list(df_interval.Dias)+list(df_interval.Dias)[::-1],
#         y=list(df_interval.upr)+list(df_interval.lwr)[::-1],
#         fill='toself',
#         fillcolor=fillcolor,
#         line_color=line_color,
#         showlegend=False,
#         name=name
#     ))
#     fig_surv_2.add_trace(go.Scatter(
#         x=df['Dias'],
#         y=df['Probabilidad de pasar más días afuera'],
#         line_color=line_color_l,
#         name=name,
#     ))

# fig_surv_2.update_layout(
#     xaxis_title ="Días",
#     yaxis_title = "P(t > T)",
#     title = 'Días entre la segunda y tercera reincidencia',
#     font=dict(
#         family="Courier New, monospace",
#         size=18,
#         color="#7f7f7f"
#     ),
#     width=800, height=400
# )

# fig_surv_2.update_traces(mode='lines')

# fig_surv_3 = go.Figure()

# for i in [0, 3]:
#     kmf = KaplanMeierFitter()
#     kmf.fit(df_kmkmkm.loc[df_kmkmkm['NUMERO_REINCIDENCIAS']>i,'DIAS_LIBRE'], df_kmkmkm.loc[df_kmkmkm['NUMERO_REINCIDENCIAS']>i, 'CENSURADO_LIBRES'])

#     if i == 0:
#         name= 'Días fuera de la cárcel (95% IC)'
#         fillcolor='rgba(0,176,246,0.2)'
#         line_color='rgba(255,255,255,0)'
#         line_color_l='rgb(0,176,246)'
#     else:
#         name = 'Días fuera de la cárcel sólo con reincidentes (95% IC)'
#         fillcolor='rgba(231,107,243,0.2)'
#         line_color='rgba(255,255,255,0)'
#         line_color_l='rgb(231,107,243)'

#     df = kmf.survival_function_.reset_index()
#     df.columns = ['Dias', 'Probabilidad de pasar más días afuera']

#     df_interval = kmf.confidence_interval_survival_function_.reset_index()
#     df_interval.columns = ['Dias', 'lwr', 'upr']

#     fig_surv_3.add_trace(go.Scatter(
#         x=list(df_interval.Dias)+list(df_interval.Dias)[::-1],
#         y=list(df_interval.upr)+list(df_interval.lwr)[::-1],
#         fill='toself',
#         fillcolor=fillcolor,
#         line_color=line_color,
#         showlegend=False,
#         name=name,
#     ))
#     fig_surv_3.add_trace(go.Scatter(
#         x=df['Dias'],
#         y=df['Probabilidad de pasar más días afuera'],
#         line_color=line_color_l,
#         name=name,
#     ))

# fig_surv_3.update_layout(
#     xaxis_title ="Días",
#     yaxis_title = "P(t > T)",
#     title = 'Días entre la tercera y cuarta reincidencia',
#     font=dict(
#         family="Courier New, monospace",
#         size=18,
#         color="#7f7f7f"
#     ),
#     width=800, height=400
# )

# fig_surv_3.update_traces(mode='lines')

# fig_surv_4 = go.Figure()

# for i in [0, 4]:
#     kmf = KaplanMeierFitter()
#     kmf.fit(df_kmkmkm.loc[df_kmkmkm['NUMERO_REINCIDENCIAS']>i,'DIAS_LIBRE'], df_kmkmkm.loc[df_kmkmkm['NUMERO_REINCIDENCIAS']>i, 'CENSURADO_LIBRES'])

#     if i == 0:
#         name= 'Días fuera de la cárcel (95% IC)'
#         fillcolor='rgba(0,176,246,0.2)'
#         line_color='rgba(255,255,255,0)'
#         line_color_l='rgb(0,176,246)'
#     else:
#         name = 'Días fuera de la cárcel sólo con reincidentes (95% IC)'
#         fillcolor='rgba(231,107,243,0.2)'
#         line_color='rgba(255,255,255,0)'
#         line_color_l='rgb(231,107,243)'

#     df = kmf.survival_function_.reset_index()
#     df.columns = ['Dias', 'Probabilidad de pasar más días afuera']

#     df_interval = kmf.confidence_interval_survival_function_.reset_index()
#     df_interval.columns = ['Dias', 'lwr', 'upr']

#     fig_surv_4.add_trace(go.Scatter(
#         x=list(df_interval.Dias)+list(df_interval.Dias)[::-1],
#         y=list(df_interval.upr)+list(df_interval.lwr)[::-1],
#         fill='toself',
#         fillcolor=fillcolor,
#         line_color=line_color,
#         showlegend=False,
#         name=name,
#     ))
#     fig_surv_4.add_trace(go.Scatter(
#         x=df['Dias'],
#         y=df['Probabilidad de pasar más días afuera'],
#         line_color=line_color_l,
#         name=name,
#     ))

# fig_surv_4.update_layout(
#     xaxis_title ="Días",
#     yaxis_title = "P(t > T)",
#     title = 'Días entre la cuarta y quinta reincidencia',
#     font=dict(
#         family="Courier New, monospace",
#         size=18,
#         color="#7f7f7f"
#     ),
#     width=800, height=400
# )

# fig_surv_4.update_traces(mode='lines')

#################################################################################
# Here the layout for the plots to use.
#################################################################################
timeanalysis_output=html.Div([
	#Place the different graph components here.
	dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_genero, id='time_outside_jail_gender')),
	]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_act_est, id='time_convictions_edu_act')),
	]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_freedom_days, id='time_freedom_edu_act')),
	]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_teach, id='time_convictions_tea_activities')),
	]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_freedom_teach, id='time_freedom_tea_act')),
	]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_work, id='time_convictions_work_activities')),
	]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_freedom_work, id='time_freedom_work_act')),
        # dbc.Col(dcc.Graph(figure=fig_surv_1, id='fig_surv_1')),
	]),
    # dbc.Row([
    #     dbc.Col(dcc.Graph(figure=fig_surv_2, id='fig_surv_2')),
    #     dbc.Col(dcc.Graph(figure=fig_surv_3, id='fig_surv_3')),
	# ]),
    # dbc.Row([
    #     dbc.Col(dcc.Graph(figure=fig_surv_4, id='fig_surv_4')),
    #     dbc.Col(),
	# ]),
	],className="mj-body")


# survival_model=html.Div([
#     dbc.Row([
#         dbc.Col(dcc.Graph(figure=fig_surv_1, id='fig_surv_1')),
#         dbc.Col(dcc.Graph(figure=fig_surv_2, id='fig_surv_2'))
# 	]),
#     dbc.Row([
#         dbc.Col(dcc.Graph(figure=fig_surv_3, id='fig_surv_3')),
#         dbc.Col(dcc.Graph(figure=fig_surv_4, id='fig_surv_4')),
# 	]),
# 	],className="mj-body")