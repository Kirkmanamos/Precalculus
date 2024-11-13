from manim import *

class RationalFunctionScene(Scene):
    def construct(self):
        # Set up axes
        axes = Axes(
            x_range=[-10, 10, 2],  # Twice the range in the x-direction
            y_range=[-14, 20, 2],  # Twice the range in the y-direction
            x_length=10,
            y_length=10,
            axis_config={"color": BLUE,
                         "include_numbers": True,
                         "font_size": 24
                         }
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        
        # Define rational function with vertical asymptote at x=3
        def rational_function_left(x):
            return (x + 2) / (x - 3) if x < 3 else np.nan

        def rational_function_right(x):
            return (x + 2) / (x - 3) if x > 3 else np.nan

        # Plot the function on two intervals, avoiding x=3
        graph_left = axes.plot(rational_function_left, x_range=[-10, 2.9], color=YELLOW)
        graph_right = axes.plot(rational_function_right, x_range=[3.1, 10], color=YELLOW)
        
        # Create asymptotes and other features
        vert_asymptote = DashedLine(
            start=axes.c2p(3, -10),
            end=axes.c2p(3, 16),
            color=RED
        )
        hor_asymptote = DashedLine(
            start=axes.c2p(9, 1),
            end=axes.c2p(-10, 1),
            color=RED
        )

        # Labels
        vert_asymptote_label = MathTex("x = 3", color=RED).next_to(vert_asymptote, RIGHT).shift(DOWN * 3)
        vert_asymptote_label2 = MathTex("\\text{V,A,}", color=RED).next_to(vert_asymptote_label, DOWN)
        hor_asymptote_label = MathTex("y = 1", color=RED).next_to(hor_asymptote, LEFT).shift(UP * 0.5)
        
        # Hole at x = 1
        hole = Dot(axes.c2p(1, (1 + 2) / (1 - 3)), color=PURE_GREEN).scale(1.2)
        hole_label = MathTex("\\text{Hole at } \\ x = 1").next_to(hole, DOWN).shift(LEFT * 3)
        hole_label.set(color=PURE_GREEN, font_size=34)

        # X-intercept at x = -2
        x_intercept = Dot(axes.c2p(-2, 0), color=PINK).scale(1.2)
        x_intercept_label = MathTex("\\text{x-intercept at } x = -2").next_to(x_intercept, UP * 1.5).shift(LEFT * 1.7)
        x_intercept_label.set(color=PINK, font_size=34)  

        # Factored form of the function
        factored_form = MathTex("f(x) = \\frac{(x-1)(x + 2)}{(x-1)(x - 3)}").to_corner(UL).scale(0.75)

        # Animate all components
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph_left), Create(graph_right), run_time=3)
        self.play(Create(vert_asymptote), Create(hor_asymptote))
        self.play(Write(vert_asymptote_label), Write(hor_asymptote_label))
        self.play(Write(vert_asymptote_label2), run_time=0.1)
        self.play(Create(hole), Write(hole_label))
        self.play(Create(x_intercept), Write(x_intercept_label))
        self.play(Write(factored_form))

        # Hold the final scene
        self.wait(6)
