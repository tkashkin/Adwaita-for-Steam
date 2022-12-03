InstallSubChooseApps.res
{
	styles
	{
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
			image="assets/checkbox/unchecked"
			textcolor="button_fg"
			font-family=basefont
			font-size=15
			font-weight=400
			font-style=none
			render {}
			render_bg {}
		}
		CheckButton:hover
		{
			image="assets/checkbox/unchecked_hover"
			render {}
			render_bg {}
		}
		CheckButton:selected
		{
			image="assets/checkbox/checked"
			render {}
			render_bg {}
		}
		CheckButton:selected:hover
		{
			image="assets/checkbox/checked_hover"
			render {}
			render_bg {}
		}
		CheckButton:disabled
		{
			image="assets/checkbox/unchecked_disabled"
			textcolor="button_disabled_fg"
			render {}
			render_bg {}
		}
		CheckButton:selected:disabled
		{
			image="assets/checkbox/checked_disabled"
			render {}
			render_bg {}
		}
	}

	layout
	{
		place { control="Label1" dir=down margin-top=16 margin-left=16 margin-right=16 width=max }

		place { control="GameCheckButtonList" dir=down start="Label1" margin-top=8 margin-right=16 width=max height=130 }

		place { control="InstallFolderLabel" dir=down start="GameCheckButtonList" margin-top=8 margin-right=16 width=max height=34 }
		place { control="InstallFolderCombo" dir=down start="InstallFolderLabel" margin-right=16 width=max height=50 }

		place { control="InstallSize,DriveSpace,DownloadTimeLabel" dir=down start="InstallFolderCombo" margin-top=16 width=200 }
		place { control="InstallSizeLabel" start="InstallSize" width=max }
		place { control="DriveSpaceLabel" start="DriveSpace" width=max }
		place { control="DownloadTimeInfo" start="DownloadTimeLabel" width=max }
	}
}
