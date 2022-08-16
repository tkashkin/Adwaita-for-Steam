InstallSubChooseApps_SingleApp.res
{
	styles
	{
		CInstallSubChooseApps
		{
			render
			{
				0="image(x0+16, y0+150, x0+28, y0+162, assets/corners/12_mask_window_bg/tl)"
				1="image(x1-28, y0+150, x1-16, y0+162, assets/corners/12_mask_window_bg/tr)"
				2="image(x0+16, y0+238, x0+28, y0+250, assets/corners/12_mask_window_bg/bl)"
				3="image(x1-28, y0+238, x1-16, y0+250, assets/corners/12_mask_window_bg/br)"
			}
		}

		Label
		{
			textcolor="window_fg"
			font-size=14
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
				0="gradient_horizontal(x0-6, y0, x0+6, y1, window_bg_transparent, window_bg)"
				1="fill(x0+6, y0, x1, y1, window_bg)"
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
	}

	layout
	{
		place { control="Label1" dir=down margin-top=16 margin-left=16 margin-right=16 width=max }

		place { control="InstallFolderLabel" dir=down start="Label1" margin-top=8 margin-right=16 width=max height=34 }
		place { control="InstallFolderCombo" dir=down start="InstallFolderLabel" margin-right=16 width=max height=50 }

		place { control="CreateShortcutCheck,CreateStartMenuShortcutCheck" dir=down margin-top=150 margin-left=16 margin-right=16 width=max height=50 }

		place { control="InstallSize,DriveSpace,DownloadTimeLabel" dir=down start="CreateStartMenuShortcutCheck" margin-top=16 width=200 }
		place { control="InstallSizeLabel" start="InstallSize" width=max }
		place { control="DriveSpaceLabel" start="DriveSpace" width=max }
		place { control="DownloadTimeInfo" start="DownloadTimeLabel" width=max }

		region { name="hidden" width=0 height=0 margin-left=-999 }
		place { control="InstallLanguageLabel,LanguageCombo" region="hidden" width=0 height=0 }
	}
}
