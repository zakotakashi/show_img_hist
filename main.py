import numpy as np
import pandas as pd
import streamlit as st
from skimage.io import imread


def get_image():
    """download the image
    """

    img_url = \
        'https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Mount_Fuji_from_Mount_Aino.jpg/640px-Mount_Fuji_from_Mount_Aino.jpg'

    im = imread(img_url)

    st.image(
        im,
        caption='image from wikimedia commons',
        use_column_width=True
    )

    return im


def show_histogram(im):
    """show histgram of all colors
    """

    hist_red, _ = np.histogram(im[:, :, 0], bins=64)
    hist_green, _ = np.histogram(im[:, :, 1], bins=64)
    hist_blue, _ = np.histogram(im[:, :, 2], bins=64)
    hist = np.stack((hist_red, hist_green, hist_blue), axis=1)

    df_hist = pd.DataFrame(hist, columns=['R', 'G', 'B'])
    st.bar_chart(df_hist)

    return hist_red, hist_green, hist_blue


def show_color_selector(hist_red, hist_green, hist_blue):
    """choose one color
    """

    color = st.radio(
        "choose R, G, or B",
        ('R', 'G', 'B')
    )
    if color == 'R':
        df_hist = pd.DataFrame(hist_red)
        st.bar_chart(df_hist)
    if color == 'G':
        df_hist = pd.DataFrame(hist_green)
        st.bar_chart(df_hist)
    if color == 'B':
        df_hist = pd.DataFrame(hist_blue)
        st.bar_chart(df_hist)


def main():

    im = get_image()
    hist_red, hist_green, hist_blue = show_histogram(im)
    show_color_selector(hist_red, hist_green, hist_blue)


if __name__ == '__main__':
    main()
