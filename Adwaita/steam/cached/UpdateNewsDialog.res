UpdateNewsDialog.res
{
	styles
	{
		FrameTitle
		{
			inset-left=90
			render
			{
				0="image(x0+16, y0+16, x0+32, y0+32, assets/icons/back_backdrop)"
				1="image(x0+56, y0+16, x0+72, y0+32, assets/icons/forward_backdrop)"
			}
		}
		FrameTitle:framefocus
		{
			render
			{
				0="image(x0+16, y0+16, x0+32, y0+32, assets/icons/back)"
				1="image(x0+56, y0+16, x0+72, y0+32, assets/icons/forward)"
			}
		}

		Button
		{
			textcolor=none
			font-size=1
		}

		HTML
		{
			inset="2 0 2 2"
		}
	}

	layout
	{
		place { control="frame_minimize,frame_close" align=right spacing=14 margin-right=12 y=12 }

		place { control="frame_title" width=max height=48 }
		place { control="PrevButton,NextButton" x=7 y=7 width=34 height=34 spacing=6 }

		place { control="HTMLSellPage" width=max height=max margin-top=48 }

		region { name="hidden" width=0 height=0 margin-left=-999 }
		place { control="CloseButton,BgRect,frame_maximize" region="hidden" width=0 height=0 }
	}
}
