import reliability as reliability
from reliability.Distributions import Weibull_Distribution
from reliability.Distributions import Exponential_Distribution
from reliability.Distributions import Normal_Distribution
from reliability.Distributions import Lognormal_Distribution
from reliability.Distributions import Gamma_Distribution
from reliability.Distributions import Beta_Distribution
from reliability.Distributions import Loglogistic_Distribution
from reliability.Distributions import Gumbel_Distribution
from reliability.Repairable_systems import optimal_replacement_time
from reliability.Probability_plotting import plot_points
from reliability.Fitters import Fit_Everything
from reliability.Other_functions import make_right_censored_data
## import tkinter as tk
import re
import matplotlib
##matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import streamlit as st
import random
import json
#=================================

#================================= Part1 =================================#

    
def show_dist():
    distName = st.session_state.distName_tab
 
    with st.form(key='input_form_tab'):
        if distName == 'Weibull': 
            st.subheader('Please enter parameters of ' + distName + ' distribution')
            st.number_input('Alpha (scale parameter)', step=1, key='distWeibull_Alpha')
            st.number_input('Beta (shape parameter)', step=0.01, key='distWeibull_Beta')
           
        elif distName == 'Exponential':
            st.subheader('Please enter failure rate of ' + distName + ' distribution')
            st.number_input('Lambda (scale parameter)', step=0.000001, key='distExponential_Lambda')

        elif distName == 'Normal':
            st.number_input('μ = location parameter (−∞<μ<∞)', step=0.01, key='distNormal_MuParam')
            st.number_input('σ = scale parameter (σ>0)', step=0.01, key='distNormal_SigmaParam')

        elif distName == 'Lognormal':
            st.subheader('Please enter parameters of ' + distName + ' distribtion')
            st.number_input('μ = scale parameter (−∞<μ<∞)', step=0.01, key='distLognormal_MuParam')
            st.number_input('σ = shape parameter (σ>0)', step=0.01, key='distLognormal_SigmaParam')

        elif distName == 'Gamma':
            st.subheader('Please enter parameters of ' + distName + ' distribtion')
            st.number_input('α = scale parameter (α>0)', step=0.01, key='distGamma_AlphaParam')
            st.number_input('β = shape parameter (β>0)', step=0.01, key='distGamma_BetaParam')

        elif distName == 'Beta':
            st.subheader('Please enter parameters of ' + distName + ' distribtion')
            st.number_input('α = shape parameter (α>0)', step=0.01, key='distBeta_AlphaParam')
            st.number_input('β = shape parameter (β>0)', step=0.01, key='distBeta_BetaParam')

        elif distName == 'Loglogistic':
            st.subheader('Please enter parameters of ' + distName + ' distribtion')
            st.number_input('α = scale parameter (α>0)', step=0.01, key='distLoglogistic_AlphaParam')
            st.number_input('β = shape parameter (β>0)', step=0.01, key='distLoglogistic_BetaParam')

        elif distName == 'Gumbel':
            st.subheader('Please enter parameters of ' + distName + ' distribtion')
            st.number_input('μ = location parameter (−∞<μ<∞)', step=0.01, key='distGumbel_MuParam')
            st.number_input('σ = scale parameter (σ>0)', step=0.01, key='distGumbel_SigmaParam')
        
        sfButton = st.form_submit_button(label='Show Reliability Curve', on_click=show_dist)
        pdfButton = st.form_submit_button(label='Show Probebility Distribution Function Curve', on_click=show_dist)
        hfButton = st.form_submit_button(label='Show Hazard Function Curve', on_click=show_dist)
        cdfButton = st.form_submit_button(label='Show Cumulative Distribution Function Curve', on_click=show_dist)      
        chfButton = st.form_submit_button(label='Show Cumulative Hazard Function Curve', on_click=show_dist)
        plotButton = st.form_submit_button(label='Show All Plots and Stats', on_click=show_dist)
        b5Button = st.form_submit_button(label='Show B5', on_click=show_dist)

    if pdfButton or cdfButton or sfButton or hfButton or chfButton or  plotButton or b5Button:
        if distName == 'Weibull': 
            distWeibull_Alpha = st.session_state.distWeibull_Alpha
            distWeibull_Beta = st.session_state.distWeibull_Beta

            dist = Weibull_Distribution(alpha = distWeibull_Alpha, beta = distWeibull_Beta)  
 
        elif distName == 'Exponential':
            distExponential_Lambda = st.session_state.distExponential_Lambda

            dist = Exponential_Distribution(Lambda = distExponential_Lambda)

        elif distName == 'Normal':
            distNormal_MuParam = st.session_state.distNormal_MuParam
            distNormal_SigmaParam = st.session_state.distNormal_SigmaParam
    
            dist = Normal_Distribution(mu = distNormal_MuParam, sigma = distNormal_SigmaParam)

        elif distName == 'Lognormal':
            distLognormal_MuParam = st.session_state.distLognormal_MuParam
            distLognormal_SigmaParam = st.session_state.distLognormal_SigmaParam

            dist = Lognormal_Distribution(mu = distLognormal_MuParam, sigma = distLognormal_SigmaParam)

        elif distName == 'Gamma':
            distGamma_AlphaParam = st.session_state.distGamma_AlphaParam
            distGamma_BetaParam = st.session_state.distGamma_BetaParam

            dist = Gamma_Distribution(alpha = distGamma_AlphaParam, beta = distGamma_BetaParam)

        elif distName == 'Beta':
            distBeta_AlphaParam = st.session_state.distBeta_AlphaParam
            distBeta_BetaParam = st.session_state.distBeta_BetaParam

            dist = Beta_Distribution(alpha = distBeta_AlphaParam, beta = distBeta_BetaParam)

        elif distName == 'Loglogistic':
            distLoglogistic_AlphaParam = st.session_state.distLoglogistic_AlphaParam
            distLoglogistic_BetaParam = st.session_state.distLoglogistic_BetaParam

            dist = Loglogistic_Distribution(alpha = distLoglogistic_AlphaParam, beta = distLoglogistic_BetaParam)  

        elif distName == 'Gumbel':
            distGumbel_MuParam = st.session_state.distGumbel_MuParam
            distGumbel_SigmaParam = st.session_state.distGumbel_SigmaParam
    
            dist = Gumbel_Distribution(mu = distGumbel_MuParam, sigma = distGumbel_SigmaParam)        

        if pdfButton: 
            dist.PDF()
            st.pyplot()

        elif cdfButton:
            dist.CDF()
            st.pyplot()

        elif sfButton:
            dist.SF()
            st.pyplot()

        elif hfButton:
            dist.HF() 
            st.pyplot()

        elif chfButton:
            dist.CHF() 
            st.pyplot()

        elif plotButton:
            dist.plot() 
            st.pyplot()


        elif b5Button:
            st.write('B5: ', dist.b5) 
            
            
#=================================

def show_reli():
    distName = st.session_state.distName_reli

    with st.form(key='input_form'):
        if distName == 'Weibull': 
            st.subheader('Please enter parameters of ' + distName + ' distribtion')
            st.number_input('Alpha (scale parameter)', step=1, key='distWeibull_Alpha')
            st.number_input('Beta (shape parameter)', step=0.01, key='distWeibull_Beta')

        elif distName == 'Exponential':
            st.subheader('Please enter parameter of ' + distName + ' distribtion')
            st.number_input('Lambda (scale parameter)', step=0.000001, key='distExponential_Lambda')

        elif distName == 'Normal':
            st.subheader('Please enter parameters of ' + distName + ' distribtion')
            st.number_input('μ = location parameter (−∞<μ<∞)', step=0.01, key='distNormal_MuParam')
            st.number_input('σ = scale parameter (σ>0)', step=0.01, key='distNormal_SigmaParam')

        elif distName == 'Lognormal':
            st.subheader('Please enter parameters of ' + distName + ' distribtion')
            st.number_input('μ = scale parameter (−∞<μ<∞)', step=0.01, key='distLognormal_MuParam')
            st.number_input('σ = shape parameter (σ>0)', step=0.01, key='distLognormal_SigmaParam')

        elif distName == 'Gamma':
            st.subheader('Please enter parameters of ' + distName + ' distribtion')
            st.number_input('α = scale parameter (α>0)', step=0.01, key='distGamma_AlphaParam')
            st.number_input('β = shape parameter (β>0)', step=0.01, key='distGamma_BetaParam')

        elif distName == 'Beta':
            st.subheader('Please enter parameters of ' + distName + ' distribtion')
            st.number_input('α = shape parameter (α>0)', step=0.01, key='distBeta_AlphaParam')
            st.number_input('β = shape parameter (β>0)', step=0.01, key='distBeta_BetaParam')

        elif distName == 'Loglogistic':
            st.subheader('Please enter parameters of ' + distName + ' distribtion')
            st.number_input('α = scale parameter (α>0)', step=0.01, key='distLoglogistic_AlphaParam')
            st.number_input('β = shape parameter (β>0)', step=0.01, key='distLoglogistic_BetaParam')

        elif distName == 'Gumbel':
            st.subheader('Please enter parameters of ' + distName + ' distribtion')
            st.number_input('μ = location parameter (−∞<μ<∞)', step=0.01, key='distGumbel_MuParam')
            st.number_input('σ = scale parameter (σ>0)', step=0.01, key='distGumbel_SigmaParam')
       
       
       
        st.number_input('Time', step=1, key='reli_Time')
        
        submitButton = st.form_submit_button(label='Calculate Reliability', on_click=show_reli)
        
    if submitButton:
        reliTime = st.session_state.reli_Time

        if distName == 'Weibull':
            distWeibull_Alpha = st.session_state.distWeibull_Alpha
            distWeibull_Beta = st.session_state.distWeibull_Beta

            dist = Weibull_Distribution(alpha = distWeibull_Alpha, beta = distWeibull_Beta)  
            
            SF = dist.SF (reliTime) 
                        
            st.write('Reliability at this time is:  '    ,SF)
  
        elif distName == 'Exponential':
            distExponential_Lambda = st.session_state.distExponential_Lambda

            dist = Exponential_Distribution(Lambda = distExponential_Lambda)
           
            SF = dist.SF(reliTime) 
                 
            st.write('Reliability at this time is:  '    ,SF)


        elif distName == 'Normal':
            distNormal_MuParam = st.session_state.distNormal_MuParam
            distNormal_SigmaParam = st.session_state.distNormal_SigmaParam

            dist = Normal_Distribution(mu = distNormal_MuParam, sigma = distNormal_SigmaParam)

            SF = dist.SF(reliTime) 
                 
            st.write('Reliability at this time is:  '    ,SF)


           
        elif distName == 'Lognormal':
            distLognormal_MuParam = st.session_state.distLognormal_MuParam
            distLognormal_SigmaParam = st.session_state.distLognormal_SigmaParam

            dist = Lognormal_Distribution(mu = distLognormal_MuParam, sigma = distLognormal_SigmaParam)
            
            SF = dist.SF(reliTime) 
                 
            st.write('Reliability at this time is:  '    ,SF)           

        elif distName == 'Gamma':
            distGamma_AlphaParam = st.session_state.distGamma_AlphaParam
            distGamma_BetaParam = st.session_state.distGamma_BetaParam

            SF = dist.SF(reliTime) 
                 
            st.write('Reliability at this time is:  '    ,SF)            


        elif distName == 'Beta':
            distBeta_AlphaParam = st.session_state.distBeta_AlphaParam
            distBeta_BetaParam = st.session_state.distBeta_BetaParam

            SF = dist.SF(reliTime) 
                 
            st.write('Reliability at this time is:  '    ,SF)


        elif distName == 'Loglogistic':
            distLoglogistic_AlphaParam = st.session_state.distLoglogistic_AlphaParam
            distLoglogistic_BetaParam = st.session_state.distLoglogistic_BetaParam

            dist = Loglogistic_Distribution(alpha = distLoglogistic_AlphaParam, beta = distLoglogistic_BetaParam) 

            SF = dist.SF(reliTime) 
                 
            st.write('Reliability at this time is:  '    ,SF)            


        elif distName == 'Gumbel':
            distGumbel_MuParam = st.session_state.distGumbel_MuParam
            distGumbel_SigmaParam = st.session_state.distGumbel_SigmaParam
    
            dist = Gumbel_Distribution(mu = distGumbel_MuParam, sigma = distGumbel_SigmaParam)
           
            SF = dist.SF(reliTime) 
                 
            st.write('Reliability at this time is:  '    ,SF)            




#=================================

def show_ttf():
    distName = st.session_state.distName_ttf

    with st.form(key='input_form'):
        if distName == 'Weibull': 
            st.subheader('Please enter parameters of ' + distName + ' distribtion')
            st.number_input('Alpha (scale parameter)', step=1, key='distWeibull_Alpha')
            st.number_input('Beta (shape parameter)', step=0.01, key='distWeibull_Beta')

        elif distName == 'Exponential':
            st.subheader('Please enter parameter of ' + distName + ' distribtion')
            st.number_input('Lambda (scale parameter)', step=0.000001, key='distExponential_Lambda')
            

        elif distName == 'Normal':
            st.subheader('Please enter parameters of ' + distName + ' distribtion')
            st.number_input('μ = location parameter (−∞<μ<∞)', step=0.01, key='distNormal_MuParam')
            st.number_input('σ = scale parameter (σ>0)', step=0.01, key='distNormal_SigmaParam')

        elif distName == 'Lognormal':
            st.subheader('Please enter parameters of ' + distName + ' distribtion')
            st.number_input('μ = scale parameter (−∞<μ<∞)', step=0.01, key='distLognormal_MuParam')
            st.number_input('σ = shape parameter (σ>0)', step=0.01, key='distLognormal_SigmaParam')

        elif distName == 'Gamma':
            st.subheader('Please enter parameters of ' + distName + ' distribtion')
            st.number_input('α = scale parameter (α>0)', step=0.01, key='distGamma_AlphaParam')
            st.number_input('β = shape parameter (β>0)', step=0.01, key='distGamma_BetaParam')

        elif distName == 'Beta':
            st.subheader('Please enter parameters of ' + distName + ' distribtion')
            st.number_input('α = shape parameter (α>0)', step=0.01, key='distBeta_AlphaParam')
            st.number_input('β = shape parameter (β>0)', step=0.01, key='distBeta_BetaParam')

        elif distName == 'Loglogistic':
            st.subheader('Please enter parameters of ' + distName + ' distribtion')
            st.number_input('α = scale parameter (α>0)', step=0.01, key='distLoglogistic_AlphaParam')
            st.number_input('β = shape parameter (β>0)', step=0.01, key='distLoglogistic_BetaParam')

        elif distName == 'Gumbel':
            st.subheader('Please enter parameters of ' + distName + ' distribtion')
            st.number_input('μ = location parameter (−∞<μ<∞)', step=0.01, key='distGumbel_MuParam')
            st.number_input('σ = scale parameter (σ>0)', step=0.01, key='distGumbel_SigmaParam')
        
  
        st.number_input('Reliability', step=0.01, key='reli_Reliability')

        TTFButton = st.form_submit_button(label='Calculate TTF', on_click=show_ttf)

    
  
    if TTFButton:
        reli_Reliability= st.session_state.reli_Reliability

        if distName == 'Weibull':
            distWeibull_Alpha = st.session_state.distWeibull_Alpha
            distWeibull_Beta = st.session_state.distWeibull_Beta

            dist = Weibull_Distribution(alpha = distWeibull_Alpha, beta = distWeibull_Beta)  
            TTF = dist.inverse_SF (reli_Reliability) 
                    
            st.write('Time to failure for this chosen reliability is ', TTF)
            

        elif distName == 'Exponential':
            distExponential_Lambda = st.session_state.distExponential_Lambda

            dist = Exponential_Distribution(Lambda = distExponential_Lambda)
            TTF = dist.inverse_SF (reli_Reliability) 
                    
            st.write('Time to failure for this chosen reliability is ', TTF)

        elif distName == 'Normal':
            distNormal_MuParam = st.session_state.distNormal_MuParam
            distNormal_SigmaParam = st.session_state.distNormal_SigmaParam

            dist = Normal_Distribution(mu = distNormal_MuParam, sigma = distNormal_SigmaParam)
            TTF = dist.inverse_SF (reli_Reliability) 
                    
            st.write('Time to failure for this chosen reliability is ', TTF)

        elif distName == 'Lognormal':
            distLognormal_MuParam = st.session_state.distLognormal_MuParam
            distLognormal_SigmaParam = st.session_state.distLognormal_SigmaParam

            dist = Lognormal_Distribution(mu = distLognormal_MuParam, sigma = distLognormal_SigmaParam)
            TTF = dist.inverse_SF (reli_Reliability) 
                    
            st.write('Time to failure for this chosen reliability is ', TTF)


        elif distName == 'Gamma':
            distGamma_AlphaParam = st.session_state.distGamma_AlphaParam
            distGamma_BetaParam = st.session_state.distGamma_BetaParam

            dist = Gamma_Distribution(alpha = distGamma_AlphaParam, beta = distGamma_BetaParam)
            TTF = dist.inverse_SF (reli_Reliability) 
                    
            st.write('Time to failure for this chosen reliability is ', TTF)


        elif distName == 'Beta':
            distBeta_AlphaParam = st.session_state.distBeta_AlphaParam
            distBeta_BetaParam = st.session_state.distBeta_BetaParam

            dist = Beta_Distribution(alpha = distBeta_AlphaParam, beta = distBeta_BetaParam)
            TTF = dist.inverse_SF (reli_Reliability) 
                    
            st.write('Time to failure for this chosen reliability is ', TTF)


        elif distName == 'Loglogistic':
            distLoglogistic_AlphaParam = st.session_state.distLoglogistic_AlphaParam
            distLoglogistic_BetaParam = st.session_state.distLoglogistic_BetaParam

            dist = Loglogistic_Distribution(alpha = distLoglogistic_AlphaParam, beta = distLoglogistic_BetaParam)              
            TTF = dist.inverse_SF (reli_Reliability) 
                    
            st.write('Time to failure for this chosen reliability is ', TTF)


        elif distName == 'Gumbel':
            distGumbel_MuParam = st.session_state.distGumbel_MuParam
            distGumbel_SigmaParam = st.session_state.distGumbel_SigmaParam
    
            dist = Gumbel_Distribution(mu = distGumbel_MuParam, sigma = distGumbel_SigmaParam)
            TTF = dist.inverse_SF (reli_Reliability) 
                    
            st.write('Time to failure for this chosen reliability is: ', TTF)         

 #=================================   
def show_dfit():

    distName = st.session_state.distName_dfit

    with st.form(key='input_form_dfit'):
        if distName == 'No Censored': 
            st.subheader('Please enter  result  of ' + distName + ' test')

            #collect_numbers = lambda x : [float(i) for i in re.split("[^0-9]", x) if i != ""]
            collect_numbers = lambda x : [float(i) for i in x.split(', ') ]

            #numbers = st.text_input("Please enter Time to Failures")
            st.text_input ("Please enter Time to Failures", key= "numbers")
            
           
            #a = collect_numbers(numbers)
            



            #elif distName == 'Censored':
            #st.subheader('Please enter  result  of ' + distName + ' test')
            #st.number_input('Threshold ( Censore Parameter)',  key='threshold_fit' 
                    
            BestFitButton = st.form_submit_button(label='Best Fit Distribution', on_click=show_dfit)
             
             
            if BestFitButton:

                numbers=st.session_state.numbers
              
                a=[float(str(i)) for i in  numbers.split(',') ]              
                raw_data = a
                st.write (a)
                data = make_right_censored_data(raw_data, threshold=14)
                
                
                
#                 b=[9.97, 3.57, 11.13, 9.96, 9.8 , 8.85, 7.34, 11.86, 8.51, 8.12, 11.88, 10.92, 6.3, 10.76, 7.06, 13.85, 14.93, 10.56, 14.8, 5.23, 10.67, 4.89, 9.88, 5.6, 6.17, 11.62, 7.62, 5.8 , 7.55, 9.06, 10.29, 7.3, 12.09, 10.45, 10.67, 9.46, 13.97, 11.44, 6.74, 12.77, 17.94, 10.62, 15.61, 8.97, 11.31, 9.88, 9.97, 13.73, 10.98, 17.45, 11.07, 5.29, 9.24, 14.87, 9.66, 3.63, 7.89, 4.93, 20.64, 18.26, 14.07, 11.67, 13.58, 6.84, 8.43, 10.87, 9.13, 4.32, 19.18, 10.02, 10.66, 8.77, 8.04, 9.46, 14.55, 13.21, 9.37, 2.83, 14.03, 8.16, 11.47, 3.55, 12.33, 9.46, 10.59, 9.75, 9.07, 11.14, 18.41, 5.91, 8.66, 4.19, 13.23, 12.28, 7.47, 9.77, 12.13, 12.32, 6.86, 15.45]
#                 raw_data = b
#                 st.write (b)
#                 data = make_right_censored_data(b)
                results = Fit_Everything(failures=data.failures, right_censored=data.right_censored)
                st.write (" The best distribution fit is : ", results.best_distribution_name)
                #st.write ( results.best_distribution.parameters)
                st.write (" Alpha value is : ", results.best_distribution.parameters[0])
                st.write ( " Beta Value is : ",results.best_distribution.parameters[1])
                
        #   #raw_data = a
           # data = make_right_censored_data(raw_data, threshold=14)
           # results = Fit_Everything(failures=data.failures, right_censored=data.right_censored)

      

def show_ort():
    distName = st.session_state.distName_ort

    with st.form(key='input_form'):
        if distName == 'Weibull': 
            st.subheader('Please enter parameters of ' + distName + ' distribtion')
            st.number_input('Alpha (scale parameter)', step=1, key='distWeibull_Alpha')
            st.number_input('Beta (shape parameter)', step=0.01, key='distWeibull_Beta')

#         elif distName == 'Exponential':
#             st.subheader('Please enter parameter of ' + distName + ' distribtion')
#             st.number_input('Lambda (scale parameter)', step=0.000001, key='distExponential_Lambda')

#         elif distName == 'Normal':
#             st.subheader('Please enter parameters of ' + distName + ' distribtion')
#             st.number_input('μ = location parameter (−∞<μ<∞)', step=0.01, key='distNormal_MuParam')
#             st.number_input('σ = scale parameter (σ>0)', step=0.01, key='distNormal_SigmaParam')

#         elif distName == 'Lognormal':
#             st.subheader('Please enter parameters of ' + distName + ' distribtion')
#             st.number_input('μ = scale parameter (−∞<μ<∞)', step=0.01, key='distLognormal_MuParam')
#             st.number_input('σ = shape parameter (σ>0)', step=0.01, key='distLognormal_SigmaParam')

#         elif distName == 'Gamma':
#             st.subheader('Please enter parameters of ' + distName + ' distribtion')
#             st.number_input('α = scale parameter (α>0)', step=0.01, key='distGamma_AlphaParam')
#             st.number_input('β = shape parameter (β>0)', step=0.01, key='distGamma_BetaParam')

#         elif distName == 'Beta':
#             st.subheader('Please enter parameters of ' + distName + ' distribtion')
#             st.number_input('α = shape parameter (α>0)', step=0.01, key='distBeta_AlphaParam')
#             st.number_input('β = shape parameter (β>0)', step=0.01, key='distBeta_BetaParam')

#         elif distName == 'Loglogistic':
#             st.subheader('Please enter parameters of ' + distName + ' distribtion')
#             st.number_input('α = scale parameter (α>0)', step=0.01, key='distLoglogistic_AlphaParam')
#             st.number_input('β = shape parameter (β>0)', step=0.01, key='distLoglogistic_BetaParam')

#         elif distName == 'Gumbel':
#             st.subheader('Please enter parameters of ' + distName + ' distribtion')
#             st.number_input('μ = location parameter (−∞<μ<∞)', step=0.01, key='distGumbel_MuParam')
#             st.number_input('σ = scale parameter (σ>0)', step=0.01, key='distGumbel_SigmaParam')
        
  
        st.number_input('Preventive Maintenance Cost', step=0.01, key='reli_PMC')
        st.number_input('Corective Maintenance Cost', step=0.01, key='reli_CMC')

        TTFButton = st.form_submit_button(label='Calculate Optimal Replacement Cost', on_click=show_ort)    
  
 
    if TTFButton: 
        reli_PMC= st.session_state.reli_PMC
        reli_CMC= st.session_state.reli_CMC
        if distName == 'Weibull':
            distWeibull_Alpha = st.session_state.distWeibull_Alpha
            distWeibull_Beta = st.session_state.distWeibull_Beta

            optimal_replacement_time(cost_PM = reli_PMC, cost_CM = reli_CMC , weibull_alpha = distWeibull_Alpha, weibull_beta = distWeibull_Beta, q=0)
            st.pyplot()
            #st.write('Optimum replacement time  is ', TTF)
            

#         elif distName == 'Exponential':
#             distExponential_Lambda = st.session_state.distExponential_Lambda

#             optimal_replacement_time(cost_PM = reli_PMC, cost_CM = reli_CMC , Exponentioal_Lambda = distExponential_Lambda, q=0)
#             plt.show()

        # elif distName == 'Normal':
        #     distNormal_MuParam = st.session_state.distNormal_MuParam
        #     distNormal_SigmaParam = st.session_state.distNormal_SigmaParam
        #     optimal_replacement_time(cost_PM = reli_PMC, cost_CM = reli_CMC , weibull_alpha = distWeibull_Alpha, weibull_beta = distWeibull_Beta, q=0)
        #     plt.show()
        #    Exponential_Distribution(Lambda = distExponential_Lambda)
        # elif distName == 'Lognormal':
        #     distLognormal_MuParam = st.session_state.distLognormal_MuParam
        #     distLognormal_SigmaParam = st.session_state.distLognormal_SigmaParam

        #     dist = Lognormal_Distribution(mu = distLognormal_MuParam, sigma = distLognormal_SigmaParam)
        #     TTF = dist.inverse_SF (reli_Reliability) 
                    
        #     st.write('Time to failure for this chosen reliability is ', TTF)


        # elif distName == 'Gamma':
        #     distGamma_AlphaParam = st.session_state.distGamma_AlphaParam
        #     distGamma_BetaParam = st.session_state.distGamma_BetaParam

        #     dist = Gamma_Distribution(alpha = distGamma_AlphaParam, beta = distGamma_BetaParam)
        #     TTF = dist.inverse_SF (reli_Reliability) 
                    
        #     st.write('Time to failure for this chosen reliability is ', TTF)


        # elif distName == 'Beta':
        #     distBeta_AlphaParam = st.session_state.distBeta_AlphaParam
        #     distBeta_BetaParam = st.session_state.distBeta_BetaParam

        #     dist = Beta_Distribution(alpha = distBeta_AlphaParam, beta = distBeta_BetaParam)
        #     TTF = dist.inverse_SF (reli_Reliability) 
                    
        #     st.write('Time to failure for this chosen reliability is ', TTF)


        # elif distName == 'Loglogistic':
        #     distLoglogistic_AlphaParam = st.session_state.distLoglogistic_AlphaParam
        #     distLoglogistic_BetaParam = st.session_state.distLoglogistic_BetaParam

        #     dist = Loglogistic_Distribution(alpha = distLoglogistic_AlphaParam, beta = distLoglogistic_BetaParam)              
        #     TTF = dist.inverse_SF (reli_Reliability) 
                    
        #     st.write('Time to failure for this chosen reliability is ', TTF)


        # elif distName == 'Gumbel':
        #     distGumbel_MuParam = st.session_state.distGumbel_MuParam
        #     distGumbel_SigmaParam = st.session_state.distGumbel_SigmaParam
    
        #     dist = Gumbel_Distribution(mu = distGumbel_MuParam, sigma = distGumbel_SigmaParam)
        #     TTF = dist.inverse_SF (reli_Reliability) 
                    
        #     st.write('Time to failure for this chosen reliability is: ', TTF)     
    
#================================= Part2 =================================#
    
dist_list = ['Weibull', 'Exponential', 'Normal', 'Lognormal', 'Gamma', 'Beta', 'Loglogistic', 'Gumbel']

calculated_comps = {}
serial_list = {}
parallel_list = {}
comp_relations = {}
index = {}


comp_data_def_filename =  'comp_def.json'
comp_data_def_file = open(comp_data_def_filename)
comp_def_data = json.load(comp_data_def_file)
comp_data_def_file.close()

comp_config_filename =  'comp_config.txt'
comp_config_file = open(comp_config_filename)
comp_config_data = comp_config_file.read()
comp_config_file.close()

def Serial(*components_args):
    min_TTF = 1000000
    for arg in components_args:
        if type(arg) is str:
            min_TTF = min(min_TTF, calculated_comps[arg][index['index']]['TTF'])
        else: 
             min_TTF = min(min_TTF, arg)   

    serial_list[str(components_args)] = min_TTF
    return min_TTF

def Parallel(*components_arg):
    max_TTF = 0
    for arg in components_arg:
        if type(arg) is str:
            max_TTF = max(max_TTF, calculated_comps[arg][index['index']]['TTF'])
        else: 
            max_TTF = max(max_TTF, arg)   

    parallel_list[str(components_arg)] = max_TTF
    return max_TTF

def calculate(key, reliability):
    comp = comp_def_data[key]
    distName = comp['dist']
    param1 = comp['param1']
    param2 = comp['param2']

    if distName == 'Weibull':
        dist = Weibull_Distribution(alpha = param1, beta = param2)  

    elif distName == 'Exponential':
        dist = Exponential_Distribution(Lambda = param1)

    elif distName == 'Normal':
        dist = Normal_Distribution(mu = param1, sigma = param2)

    elif distName == 'Lognormal':
        dist = Lognormal_Distribution(mu = param1, sigma = param2)

    elif distName == 'Gamma':
        dist = Gamma_Distribution(alpha = param1, beta = param2)

    elif distName == 'Beta':
        dist = Beta_Distribution(alpha = param1, beta = param2)

    elif distName == 'Loglogistic':
        dist = Loglogistic_Distribution(alpha = param1, beta = param2)              

    elif distName == 'Gumbel':
        dist = Gumbel_Distribution(mu = param1, sigma = param2)

    ttf = dist.inverse_SF(reliability) 
    #ttf = dist.SF(reliability) 
    return round (ttf, 3)

def init_comp_data():
    iteration_count = st.session_state.iteration_count

    for iteration in range(iteration_count):
        for key in comp_def_data:
            if key not in calculated_comps : 
                calculated_comps[key] = []

            reliability = random.random()
            ttf = calculate(key, reliability)
            dist_values_dict = {'Reliability': reliability, 'TTF': ttf}

            calculated_comps[key].append(dist_values_dict)

def init_comp_relations():
    for key in comp_def_data:
        cmp_key = "'" + key + "'"
        comp_relations[cmp_key] = cmp_key
 
def show_ttf():
    init_comp_data()

    ttf_list = []
    iteration_count = st.session_state.iteration_count
    Confidence_Level=st.session_state.Confidence_Level
    Confidence_Level=Confidence_Level/100
    for iteration in range(iteration_count):
        #st.write('Iteration Info ( Iteration = ', iteration+1, ')')
        index['index'] = iteration
        ttf = eval(comp_config_data)
        ttf_list.append(ttf)

        # st.write("Serial Components reliability:")
        # st.write(serial_list)
        # st.write("Parallel Components reliability:")
        # st.write(parallel_list)
        # st.write('---------------------------')
        
        #st.write("Time To Failure List: ", ttf_list)

    a = (1 - Confidence_Level) / 2
    min_number = round (a * iteration_count)
   

    max_number = round(iteration_count - (a * iteration_count))
   
    ttf_list.sort()
    
    
    
 
    min_time_in_list = ttf_list [min_number]
   
    max_time_in_list= ttf_list [max_number-1]
    st.write ('System time to failure interval is: [', min_time_in_list ,',', max_time_in_list,']') 
    e = (  max_time_in_list - min_time_in_list )/2
    e= round (e,3)
    st.write ('System time to failure  is:' , e ) 

   
    plt.hist(ttf_list)
    #st.pyplot()
    plt.savefig('test.png')
    

    # st.write("-----------------")
    # st.write("Component Values:")
    # st.json(calculated_comps)

def Com_Sen():

    init_comp_data()

    ttf_list = []
    iteration_count = st.session_state.iteration_count
    Confidence_Level=st.session_state.Confidence_Level
    Confidence_Level=Confidence_Level/100
    for iteration in range(iteration_count):
        #st.write('Iteration Info ( Iteration = ', iteration+1, ')')
        index['index'] = iteration
        ttf = eval(comp_config_data)
        ttf_list.append(ttf)

        # st.write("Serial Components reliability:")
        # st.write(serial_list)
        # st.write("Parallel Components reliability:")
        # st.write(parallel_list)
        # st.write('---------------------------')
        
    st.write("Time To Failure List: ", ttf_list)

    a = (1 - Confidence_Level) / 2
    min_number = round (a * iteration_count)
   

    max_number = round(iteration_count - (a * iteration_count))
   
    ttf_list.sort()
    
    
    
 
    min_time_in_list = ttf_list [min_number]
   
    max_time_in_list= ttf_list [max_number-1]
    st.write ('System time to failure interval is: [', min_time_in_list ,',', max_time_in_list,']') 
    e = (  max_time_in_list - min_time_in_list )/2
    e= round (e,3)
    st.write ('System time to failure  is:' , e ) 

   
    plt.hist(ttf_list)
    plt.savefig('test.png')
    plt.show()

    st.write("-----------------")
    st.write("Component Values:")
    st.json(calculated_comps)

def show_comp_def_File():

    st.button(label='Add New Component', on_click=show_add_comp, args=('', ))
    st.write('-----------------')

    for compKey in comp_def_data:
        comp = comp_def_data[compKey]
        distName = comp["dist"]
        param1 = comp["param1"]
        param2 = comp["param2"]
        st.subheader(compKey)
        st.write("Distribution: ", distName, ", Param1: ", param1, ", Param2: ", param2) 
        st.button("Edit", key=compKey, on_click=show_add_comp, args=(compKey, )) 
        

def show_add_comp(compKey):
    with st.form(key='single_comp_def_form'):
        if compKey != '' :
            comp = comp_def_data[compKey]
            distName = comp["dist"]
            param1 = comp["param1"]
            param2 = comp["param2"]
        else:
            comp = ''
            distName = dist_list[0]
            param1 = 0.0
            param2 = 0.0

        st.subheader('Enter Component Information')
        st.text_input('Component Unique Name', key='comp_name', value=compKey)
        st.selectbox('Distribution', dist_list, key='comp_dist', index=dist_list.index(distName))
        st.number_input('param1', step=0.01, key='comp_param1', value=param1)
        st.number_input('param2', step=0.01, key='comp_param2', value=param2)

        submitButton = st.form_submit_button(label='Add/Edit Component', on_click=show_add_comp, args=(compKey, ))
        delButton = st.form_submit_button(label='Delete Component', on_click=show_add_comp, args=(compKey, ))

    if submitButton :

        comp_name = st.session_state.comp_name
        comp_dist = st.session_state.comp_dist
        comp_param1 = st.session_state.comp_param1
        comp_param2 = st.session_state.comp_param2

        comp_detail_dict =  {'dist': comp_dist, 'param1': comp_param1, 'param2': comp_param2}
        comp_def_data[comp_name] = comp_detail_dict

        json_object = json.dumps(comp_def_data, indent=4)
        with open(comp_data_def_filename, 'w') as outfile:  
            outfile.write(json_object)

        st.write('Component ', comp_name, ' was add/edited.')

    if delButton :
        comp_name = st.session_state.comp_name
        
        comp_def_data.pop(comp_name)

        json_object = json.dumps(comp_def_data, indent=4)
        with open(comp_data_def_filename, 'w') as outfile:
            outfile.write(json_object)

        st.write('Component ', comp_name, ' was deleted.')

def show_comp_config_File():
    c_c_filename =  'comp_config.txt'
    c_c_file = open(c_c_filename)
    c_c_data = c_c_file.read()

    # with st.form(key='comp_conf_form'):
    txt = st.text_area(label="Components Configuration", height=300, value=c_c_data)

    #     submitButton = st.form_submit_button(label='Update Components Configuration File', on_click=show_comp_config_File)

    # if submitButton:
    #     #comp_c_file = open(comp_config_filename, 'w')
    #     comp_c_file.write(txt) 
    #     comp_c_file.close()

    #     st.write('File ', comp_config_filename, ' was saved.')


def show_assistant_comp_config_File():
    if not comp_relations:
        init_comp_relations()

    with st.form(key='comp_relation_form'):

        st.subheader('Please enter components relations')
        st.radio('Select Relation Type:', ['Serial' ,
                'Parallel'], key='relation_type')
        st.multiselect('Components: ', comp_relations, key='selected_comps')

        if len(comp_relations) == 1:
            finalFlag = True
        else:
            finalFlag = False

        addButton = st.form_submit_button(label='Add', on_click=show_assistant_comp_config_File, disabled=finalFlag)
        saveFileButton = st.form_submit_button(label='Save Components Config', on_click=show_assistant_comp_config_File, disabled=not finalFlag)

    if addButton :

        relation_Type = st.session_state.relation_type
        selected_comps = st.session_state.selected_comps

        if(len(selected_comps)>1):

            new_key = relation_Type + "("
            
            for comp in selected_comps:
                new_key = new_key + " " + comp + " , "
                comp_relations.pop(comp) 

            new_key = new_key[:-2] 
            new_key = new_key + ")"
            comp_relations[new_key] = new_key

        st.button("Apply Relation", on_click=show_assistant_comp_config_File) 

    if saveFileButton :
        if len(comp_relations) == 1 :
            comp_c_file = open(comp_config_filename, 'w')
            for c in comp_relations:
                comp_c_file.write(c) 

            comp_c_file.close()

            st.write('File ', comp_config_filename, ' was saved.')   
    
def show_comp_rel():
    st.write("-----------------")
    st.title('Components Reliability Calculation')
    st.subheader("Scroll right for Calculation ➡️")
def show_sys_rel():
    st.write("-----------------")
    st.title('System Reliability Calculation')
    st.subheader("Scroll right for Calculation ➡️")
#=================================
    
comp_rel,tab_plots, tab_reliability, tab_ttf, tab_dfit, tab_ORT,sys_rel, tab_comp, tab_conf, tab_montc, tab_sen = st.sidebar.tabs(['Components Reliability',
    'Reliability Plots', 'Reliability','Time to Failure', 'Distribution Fitter', 'Optimal Replacement Time', 'System Reliability','Components Definition', 
                 'Configuration Definition'  ,'Monte Carlo Calculation','Sensitivity Analysis'])

with comp_rel:
    st.button('Components Reliability ', on_click=show_comp_rel)

with tab_plots:
    
    a = st.radio('To view the reliability plots and statistics related to your component, please select its distribution and enter parameters. Then choose your desire plot to show:', ['Weibull' ,
             'Exponential',
             'Normal',
             'Lognormal',
             'Gamma',
             'Beta',
             'Loglogistic',
             'Gumbel'], on_change=show_dist, key='distName_tab')
           

with tab_reliability:
    b= st.radio('To calculate the reliability of the component at each desire time, please select its distribution and enter parameters. Then enter your desire time and press the Calculte Reliability button.', ['Weibull' ,
             'Exponential',
             'Normal',
             'Lognormal',
             'Gamma',
             'Beta',
             'Loglogistic',
             'Gumbel'], on_change=show_reli, key='distName_reli')

with tab_ttf:
    C = st.radio('To calculate Time to failure of the component at each desire reliability, please select its distribution and enter parameters. Then enter your desire reliability and press the Calculte TTF button.', ['Weibull' ,
             'Exponential',
             'Normal',
             'Lognormal',
             'Gamma',
             'Beta',
             'Loglogistic',
             'Gumbel'], on_change=show_ttf, key='distName_ttf')

with tab_dfit:
    
    e = st.radio('To fit the best reliability distribution for your component test result, please enter your test result. Then click on best fit button:', ['No Censored' ,
             'Right censored'], 
             on_change=show_dfit, key='distName_dfit')
             
with tab_ORT:
    b= st.radio('To calculate the Optimom Replacement Time of the component, please select its distribution and enter parameters. Then enter your Preventive Maintenance Cost and Corective Maintenance Time and press the Calculte Optimal Replacement Time button.', 
                ['Weibull' ,
             'Exponential',
             'Normal',
             'Lognormal',
             'Gamma',
             'Beta',
             'Loglogistic',
             'Gumbel'], on_change=show_ort, key='distName_ort')
    
   
with sys_rel:
    st.button('System Reliability ', on_click=show_sys_rel)
    
with tab_comp:
    st.write('Steps for defining a componet:  \n1- Click on the Enter your component key.  \n2- Click on Add New Component key.    \n3- Type a unique name for your component.     \n4- Choose the component distribution from the list.     \n5- Enter your Parameters.      \n6- Click on Add/Edit componet.       \n7- Clike on Edit button for editing an existing component.')
    st.button('Enter your Components ', on_click=show_comp_def_File)

   # st.button('Components Config File', on_click=show_comp_config_File)
   # st.button('Assistant Components Config File', on_click=show_assistant_comp_config_File)

   # st.write("--------")

   # st.number_input('Iteration Count', step=1, value=1, key='iteration_count')
   # st.button('Calculate Random TTF', on_click=show_ttf)

with tab_conf:
   
    st.write('Steps for defining a System Configuration:       \n1-Click on Configuration Provider Assistant button.       \n2- Select the relation type for each component group.      \n3- Choose the components in each group.   \n4- Click on Add button.      \n5- Click on Apply Relation button.     \n6- Clike on Save System Structure.    \n7- Click on System  Configuration button to see the existing structure. ')   
    st.button('Configuration Provider Assistant', on_click=show_assistant_comp_config_File)
    st.button('System Configuration ', on_click=show_comp_config_File)
 

with tab_montc:
    st.write('Steps for Calculating the System Time To Failure:     \n1-Enter the number of iteration for calculation.      \n2- Click on the Calculate System TTF. ')
    st.number_input('Number of Senarios ', step=1, value=1, key='iteration_count')
    st.number_input('Confidence Level (Two-Side) ', step = 1, value=1, key='Confidence_Level')  
    st.button('Calculate System TTF', on_click=show_ttf)

with tab_sen:
    st.write('Based on the cut set method and by using the Birnbaum, criticality and Fussell-Vesely factors, the components are listed related to their sesitivity to system failing, then if there is budget for maintenance we offer to spend for fixing by this priority.   ')
    st.number_input('Available Budget ', step=1, value=1, key='budget')
    st.button('List the component based on their sensitivity', on_click= Com_Sen)


