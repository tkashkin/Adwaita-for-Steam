InstallSubComplete_RetailInstall.res
{
	styles
	{
		CInstallSubComplete
		{
			render
			{
				0="image(x0+16, y0+150, x0+28, y0+162, assets/corners/12_mask_window_bg/tl)"
				1="image(x1-28, y0+150, x1-16, y0+162, assets/corners/12_mask_window_bg/tr)"
			}
		}

		CheckButton
		{
			inset="5 6 6 6"
			padding-right=64
			image="assets/pixel"
			render
			{
				0="image(x1-60, y0+12, x1-12, y1-12, assets/switch/unchecked)"
			}
			render_bg
			{
				0="fill(x0, y0, x1, y1, button_bg)"
				1="fill(x0, y1-1, x1, y1, headerbar_shade)"
			}
		}
		CheckButton:hover
		{
			image="assets/pixel"
			render
			{
				0="image(x1-60, y0+12, x1-12, y1-12, assets/switch/unchecked_hover)"
			}
			render_bg
			{
				0="fill(x0, y0, x1, y1, button_hover_bg)"
				1="fill(x0, y1-1, x1, y1, headerbar_shade)"
			}
		}
		CheckButton:active
		{
			image="assets/pixel"
			render_bg
			{
				0="fill(x0, y0, x1, y1, button_active_bg)"
				1="fill(x0, y1-1, x1, y1, headerbar_shade)"
			}
		}
		CheckButton:selected
		{
			image="assets/pixel"
			render
			{
				0="image(x1-60, y0+12, x1-12, y1-12, assets/switch/checked)"
			}
		}
		CheckButton:selected:hover
		{
			image="assets/pixel"
			render
			{
				0="image(x1-60, y0+12, x1-12, y1-12, assets/switch/checked_hover)"
			}
		}
		CheckButton:disabled
		{
			image="assets/pixel"
			render
			{
				0="image(x1-60, y0+12, x1-12, y1-12, assets/switch/unchecked_disabled)"
			}
			render_bg
			{
				0="fill(x0, y0, x1, y1, button_disabled_bg)"
				1="fill(x0, y1-1, x1, y1, headerbar_shade)"
			}
		}
		CheckButton:disabled:selected
		{
			image="assets/pixel"
			render
			{
				0="image(x1-60, y0+12, x1-12, y1-12, assets/switch/checked_disabled)"
			}
			render_bg
			{
				0="fill(x0, y0, x1, y1, button_disabled_bg)"
				1="fill(x0, y1-1, x1, y1, headerbar_shade)"
			}
		}

		URLLabel
		{
			bgcolor="button_bg"
			font-size=14
			font-weight=400
			inset-left=12
			padding-top=0
			padding-bottom=0
			render_bg
			{
				0="fill(x0, y1-1, x1, y1, headerbar_shade)"
			}
			render
			{
				0="image(x1-28, y0+17, x1-12, y1-17, assets/icons/forward)"
				1="image(x0, y1-12, x1+12, y1, assets/corners/12_mask_window_bg/bl)"
				2="image(x1-12, y1-12, x1, y1, assets/corners/12_mask_window_bg/br)"
			}
		}
		URLLabel:hover
		{
			bgcolor="button_hover_bg"
			font-style=regular
		}
		URLLabel:active
		{
			bgcolor="button_active_bg"
		}
	}

	layout
	{
		place { control="InstallConfirm,Label1" dir=down margin-top=16 margin-left=16 margin-right=16 width=max spacing=8 }
		
		place { control="AutoLaunchCheck,DontShowAgainCheck,DownloadsPageLink" dir=down margin-top=150 margin-left=16 margin-right=16 width=max height=50 }

		region { name="hidden" width=0 height=0 margin-left=-999 }
		place { control="InstallLanguageLabel,LanguageCombo" region="hidden" width=0 height=0 }
	}
}
