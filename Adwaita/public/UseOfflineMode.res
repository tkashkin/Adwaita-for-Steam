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

		URLLabel
		{
			font-style=none
			font-weight=700
			textcolor="window_fg"
		}
		URLLabel:hover
		{
			font-style=underline
		}

		Button
		{
			render
			{
				0="fill(x0, y0-1, x1, y0, border)"
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

		place { control="Label1,Label3,URLLabel1" dir=down spacing=16 margin-top=56 margin-left=16 margin-right=16 width=max }

		place { control="RetryButton,OfflineModeButton,QuitButton" dir=down align=bottom margin-left=0 margin-right=0 width=max height=42 spacing=1 }

		region { name="hidden" width=0 height=0 margin-left=-999 }
		place { control="frame_close,LabelAppearOffline" region="hidden" width=0 height=0 }
	}
}
