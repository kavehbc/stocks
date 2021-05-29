import streamlit as st
from fbprophet.diagnostics import cross_validation, performance_metrics
from fbprophet.plot import add_changepoints_to_plot, plot_cross_validation_metric


@st.cache(max_entries=50, ttl=900, allow_output_mutation=True,
          suppress_st_warning=True, show_spinner=False)
def cross_validating(model, initial_days=730, period_days=180, horizon_days=365):
    df_cv = cross_validation(model,
                             initial=str(initial_days) + ' days',
                             period=str(period_days) + ' days',
                             horizon=str(horizon_days) + ' days')
    return df_cv


@st.cache(max_entries=50, ttl=900, allow_output_mutation=True,
          suppress_st_warning=True, show_spinner=False)
def evaluating(df_cv):
    pm = performance_metrics(df_cv, rolling_window=0.1)
    return pm


def plot_validation(pm, df_cv, metric):
    st.write(pm.head())
    st.write(pm.tail())
    fig = plot_cross_validation_metric(df_cv, metric=metric, rolling_window=0.1)
    # plt.show()
    st.pyplot(fig)