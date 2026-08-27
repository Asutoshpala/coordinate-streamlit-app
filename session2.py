from io import BytesIO

import streamlit as st
import matplotlib.pyplot as plt

st.title("📍 Plot Your Points")
st.write("Enter X and Y coordinates and see them on a graph!")

# Number of points
n = st.number_input(
    "How many points do you want to plot?",
    min_value=1,
    max_value=10,
    value=3,
    step=1
)

x_values = []
y_values = []

st.subheader("Enter Coordinates")

for i in range(n):
    col1, col2 = st.columns(2)

    with col1:
        x = st.number_input(
            f"X coordinate for Point {i + 1}",
            value=float(i + 1),
            key=f"x_{i}"
        )

    with col2:
        y = st.number_input(
            f"Y coordinate for Point {i + 1}",
            value=float(i + 1),
            key=f"y_{i}"
        )

    x_values.append(x)
    y_values.append(y)

if st.button("📊 Plot Points"):

    fig, ax = plt.subplots()

    ax.plot(
        x_values,
        y_values,
        marker="o",
        linestyle="-"
    )

    # Label each point
    for i in range(n):
        ax.annotate(
            f"({x_values[i]}, {y_values[i]})",
            (x_values[i], y_values[i])
        )

    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Coordinate Geometry")
    ax.grid(True)

    image_buffer = BytesIO()
    fig.savefig(image_buffer, format="png", bbox_inches="tight")
    st.session_state["plot_image"] = image_buffer.getvalue()

    st.pyplot(fig)
    plt.close(fig)

    st.success("Your points have been plotted!")

if "plot_image" in st.session_state:
    st.download_button(
        "⬇️ Download graph",
        data=st.session_state["plot_image"],
        file_name="coordinate-graph.png",
        mime="image/png",
    )

    st.html(
        """
        <button onclick="window.print()" style="
            padding: 0.45rem 0.8rem;
            border: 1px solid #777;
            border-radius: 0.35rem;
            background: white;
            color: #222;
            cursor: pointer;
            font-size: 0.95rem;
        ">🖨️ Print graph</button>
        """,
        unsafe_allow_javascript=True,
    )
