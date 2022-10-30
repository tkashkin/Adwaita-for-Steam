ChooseBetaDialog.res
{
	styles
	{
		CChooseBetaDialog
		{
			bgcolor="popover_bg"
			textcolor="popover_fg"
			minimum-width=440
		}

		FrameTitle
		{
			textcolor="popover_fg"
			font-size=20
			inset-left=10
			render_bg {}
		}

		Label
		{
			textcolor="popover_fg"
			font-size=15
		}

		URLLabel
		{
			font-style=none
			font-weight=700
			textcolor="popover_fg"
		}
		URLLabel:hover
		{
			font-style=underline
		}

		Button
		{
			inset-left=10
			render
			{
				0="fill(x0, y0-1, x1+1, y0, border)"
				1="fill(x1, y0, x1+1, y1, border)"
			}
			render_bg {}
		}
		Button:hover
		{
			render_bg
			{
				0="fill(x0, y0, x1, y1, button_bg)"
			}
		}
		Button:focus
		{
			render_bg
			{
				0="fill(x0, y0, x1, y1, button_bg)"
			}
		}
		Button:active
		{
			render_bg
			{
				0="fill(x0, y0, x1, y1, button_hover_bg)"
			}
		}

		ComboBox
		{
			font-size=14
			inset="8 0 -6 0"
			render_bg {}
			render
			{
				0="fill(x0, y0+12, x1, y1-12, button_bg)"
				1="fill(x0+12, y0, x1-12, y0+12, button_bg)"
				2="fill(x0+12, y1-12, x1-12, y1, button_bg)"
				3="image(x0, y0, x0+12, y0+12, assets/corners/12_w10/tl)"
				4="image(x1-12, y0, x1, y0+12, assets/corners/12_w10/tr)"
				5="image(x0, y1-12, x0+12, y1, assets/corners/12_w10/bl)"
				6="image(x1-12, y1-12, x1, y1, assets/corners/12_w10/br)"
			}
		}
		ComboBox:hover
		{
			render_bg {}
			render
			{
				0="fill(x0, y0+12, x1, y1-12, button_hover_bg)"
				1="fill(x0+12, y0, x1-12, y0+12, button_hover_bg)"
				2="fill(x0+12, y1-12, x1-12, y1, button_hover_bg)"
				3="image(x0, y0, x0+12, y0+12, assets/corners/12_w15/tl)"
				4="image(x1-12, y0, x1, y0+12, assets/corners/12_w15/tr)"
				5="image(x0, y1-12, x0+12, y1, assets/corners/12_w15/bl)"
				6="image(x1-12, y1-12, x1, y1, assets/corners/12_w15/br)"
			}
		}
		ComboBox:active
		{
			render_bg {}
			render
			{
				0="fill(x0, y0+12, x1, y1-12, button_hover_bg)"
				1="fill(x0+12, y0, x1-12, y0+12, button_hover_bg)"
				2="fill(x0+12, y1-12, x1-12, y1, button_hover_bg)"
				3="image(x0, y0, x0+12, y0+12, assets/corners/12_w15/tl)"
				4="image(x1-12, y0, x1, y0+12, assets/corners/12_w15/tr)"
				5="image(x0, y1-12, x0+12, y1, assets/corners/12_w15/bl)"
				6="image(x1-12, y1-12, x1, y1, assets/corners/12_w15/br)"
			}
		}
		ComboBoxButton
		{
			render {}
			render_bg
			{
				0="gradient_horizontal(x0-6, y0, x0+6, y1, popover_bg_transparent, popover_bg)"
				1="fill(x0+6, y0, x1, y1, popover_bg)"
			}
		}
	}

	layout
	{
		place { control="frame_title" width=max height=64 }

		place { control="Label1" dir=down margin-top=56 margin-left=16 margin-right=16 width=max }
		place { control="BetaListComboBox" dir=down margin-top=220 margin-left=16 margin-right=16 width=max height=50 }
		place { control="ReadMoreURL" start="BetaListComboBox" dir=down margin-top=16 margin-right=16 width=max }

		place { control="CancelButton,OKButton" align=bottom margin-left=0 margin-right=0 width=220 height=42 spacing=1 }

		region { name="hidden" width=0 height=0 margin-left=-999 }
		place { control="frame_close,Label2" region="hidden" width=0 height=0 }
	}
}