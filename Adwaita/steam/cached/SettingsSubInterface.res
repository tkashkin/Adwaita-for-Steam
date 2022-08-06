SettingsSubInterface.res
{
	styles
	{
		CheckButton
		{
			inset="5 6 6 6"
			padding-right=64
			image="assets/pixel"
			render
			{
				0="image(x1-56, y0+12, x1-8, y1-12, assets/switch/unchecked)"
			}
			render_bg
			{
				0="fill(x0, y0, x1, y1, button_bg)"
				1="fill(x0, y1-1, x1, y1, headerbar_shade)"
			}
		}
		CheckButton:hover
		{
			render
			{
				0="image(x1-56, y0+12, x1-8, y1-12, assets/switch/unchecked_hover)"
			}
			render_bg
			{
				0="fill(x0, y0, x1, y1, button_hover_bg)"
				1="fill(x0, y1-1, x1, y1, headerbar_shade)"
			}
		}
		CheckButton:active
		{
			render_bg
			{
				0="fill(x0, y0, x1, y1, button_active_bg)"
				1="fill(x0, y1-1, x1, y1, headerbar_shade)"
			}
		}
		CheckButton:selected
		{
			render
			{
				0="image(x1-56, y0+12, x1-8, y1-12, assets/switch/checked)"
			}
		}
		CheckButton:selected:hover
		{
			render
			{
				0="image(x1-56, y0+12, x1-8, y1-12, assets/switch/checked_hover)"
			}
		}

		ComboBox
		{
			font-size=14
			inset="350 0 -12 0"
			render_bg {}
			render
			{
				0="fill(x0+12, y0, x1-12, y0+12, button_bg)"
				1="fill(x0, y0+12, x1, y1, button_bg)"
				2="image(x0, y0, x0+12, y0+12, assets/corners/12_w10/tl)"
				3="image(x1-12, y0, x1, y0+12, assets/corners/12_w10/tr)"
				4="fill(x0, y1-1, x1, y1, headerbar_shade)"
			}
		}
		ComboBox:hover
		{
			render
			{
				0="fill(x0+12, y0, x1-12, y0+12, button_hover_bg)"
				1="fill(x0, y0+12, x1, y1, button_hover_bg)"
				2="image(x0, y0, x0+12, y0+12, assets/corners/12_w15/tl)"
				3="image(x1-12, y0, x1, y0+12, assets/corners/12_w15/tr)"
				4="fill(x0, y1-1, x1, y1, headerbar_shade)"
			}
		}
		ComboBox:active
		{
			render
			{
				0="fill(x0+12, y0, x1-12, y0+12, button_hover_bg)"
				1="fill(x0, y0+12, x1, y1, button_hover_bg)"
				2="image(x0, y0, x0+12, y0+12, assets/corners/12_w15/tl)"
				3="image(x1-12, y0, x1, y0+12, assets/corners/12_w15/tr)"
				4="fill(x0, y1-1, x1, y1, headerbar_shade)"
			}
		}
		ComboBox:disabled
		{
			render
			{
				0="fill(x0+12, y0, x1-12, y0+12, button_disabled_bg)"
				1="fill(x0, y0+12, x1, y1, button_disabled_bg)"
				2="image(x0, y0, x0+12, y0+12, assets/corners/12_w5/tl)"
				3="image(x1-12, y0, x1, y0+12, assets/corners/12_w5/tr)"
				4="fill(x0, y1-1, x1, y1, headerbar_shade)"
			}
		}

		ComboBoxButton
		{
			render_bg
			{
				0="fill(x0, y0, x1, y1, window_bg)"
			}
		}

		Button
		{
			bgcolor="button_bg"
			render_bg {}
		}
		Button:hover
		{
			bgcolor="button_hover_bg"
		}
		Button:active
		{
			bgcolor="button_active_bg"
		}

		Label
		{
			font-size=14
			textcolor="window_fg"
			selectedtextcolor="window_fg"
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

		Divider
		{
			render_bg {}
			render
			{
				0="fill(x0, y0-1, x1, y0, window_bg)"
				1="image(x0, y0-12, x0+12, y0, assets/corners/12_mask_window_bg/bl)"
				2="image(x1-12, y0-12, x1, y0, assets/corners/12_mask_window_bg/br)"
				3="image(x0, y1, x0+12, y1+12, assets/corners/12_mask_window_bg/tl)"
				4="image(x1-12, y1, x1, y1+12, assets/corners/12_mask_window_bg/tr)"
			}
		}
	}

	layout
	{
		region { name="content" margin-left=16 width=520 height=max overflow=scroll-vertical }

		place { control="LanguageCombo,NotifyAvailableGamesCheck" region="content" margin-top=16 dir=down width=484 height=50 }

		place { control="Divider1" region="content" width=484 height=16 dir=down start="NotifyAvailableGamesCheck" }

		place { control="FavoriteWindowCombo,AutoLaunchCheck,BigPictureModeCheck" region="content" start="Divider1" dir=down width=484 height=50 }

		place { control="Divider2" region="content" width=484 height=16 dir=down start="BigPictureModeCheck" }

		place { control="SkinCombo,DPIScalingCheck,UrlBarCheck,DWriteCheck,SmoothScrollWebViewCheck,GPUWebViewCheck,H264HWAccelCheck,SetJumplistOptionsButton" region="content" start="Divider2" dir=down width=484 height=50 }

		place { control="Divider3" region="content" width=484 height=16 dir=down start="SetJumplistOptionsButton" }

		place { control="LabelLanguageCombo,LabelSteamChinaLanguageCombo" region="content" start="LanguageCombo" dir=down margin-top=-42 margin-left=12 width=335 }
		place { control="TranslationLabel" region="content" start="LanguageCombo" dir=down margin-top=-24 margin-left=12 width=335 }
		place { control="Label1" region="content" start="FavoriteWindowCombo" dir=down margin-top=-42 margin-left=12 width=335 }
		place { control="Label3" region="content" start="SkinCombo" dir=down margin-top=-32 margin-left=12 width=335 }
	}
}
