import pandas as pd
import plotly.express as px


def create_auto_chart(df: pd.DataFrame):
    if df.empty or len(df.columns) < 2:
        return None

    datetime_columns = list(
        df.select_dtypes(
            include=["datetime", "datetimetz"]
        ).columns
    )

    numeric_columns = list(
        df.select_dtypes(
            include="number"
        ).columns
    )

    text_columns = list(
        df.select_dtypes(
            include=["object", "string", "category"]
        ).columns
    )

    # Tarih + sayı varsa çizgi grafik
    if datetime_columns and numeric_columns:
        x_column = datetime_columns[0]
        y_column = numeric_columns[0]

        figure = px.line(
            df,
            x=x_column,
            y=y_column,
            markers=True,
        )

        figure.update_layout(
            xaxis_title=x_column,
            yaxis_title=y_column,
        )

        return figure

    # Metin/kategori + sayı varsa yatay bar grafik
    if text_columns and numeric_columns:
        x_column = numeric_columns[0]
        y_column = text_columns[0]

        figure = px.bar(
            df,
            x=x_column,
            y=y_column,
            orientation="h",
            text=x_column,
        )

        figure.update_layout(
            xaxis_title=x_column,
            yaxis_title=y_column,
            yaxis=dict(
                categoryorder="total ascending"
            ),
        )

        return figure

    # İki sayısal sütun varsa saçılım grafiği
    if len(numeric_columns) >= 2:
        figure = px.scatter(
            df,
            x=numeric_columns[0],
            y=numeric_columns[1],
        )

        return figure

    return None