UseOfflineModeChosen.res
{
	styles
	{
		CUseOfflineModeDialog
		{
			bgcolor="popover_bg"
			textcolor="popover_fg"
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
	}

	layout
	{
		place { control="frame_title" width=max height=64 }

		place { control="Label1" margin-top=56 margin-bottom=50 margin-left=16 margin-right=16 width=max height=max }

		place { control="RetryButton,OfflineModeButton" align=bottom margin-left=0 margin-right=0 width=180 height=42 spacing=1 }

		region { name="hidden" width=0 height=0 margin-left=-999 }
		place { control="frame_close,QuitButton" region="hidden" width=0 height=0 }
	}
}
