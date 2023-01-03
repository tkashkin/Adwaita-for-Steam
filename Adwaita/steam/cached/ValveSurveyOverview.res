ValveSurveyOverview.res
{
	styles
	{
		Label
		{
			render
			{
				0="image(x0, y1+16, x0+12, y1+28, assets/corners/12_mask_window_bg/tl)"
				1="image(x1-12, y1+16, x1, y1+28, assets/corners/12_mask_window_bg/tr)"
			}
		}

		URLLabel
		{
			render
			{
				0="fill(x0, y0-17, x1, y0-16, window_bg)"
				1="image(x0, y0-28, x0+12, y0-16, assets/corners/12_mask_window_bg/bl)"
				2="image(x1-12, y0-28, x1, y0-16, assets/corners/12_mask_window_bg/br)"
			}
		}
	}

	layout
	{
		place { control="InfoLabel" x=16 y=16 width=max margin-right=16 }
		place { control="SurveyYesRadio,SurveyNoRadio" start="InfoLabel" dir=down width=max height=50 margin-top=16 margin-right=16 }
		place { control="PrivacyLink" start="SurveyNoRadio" dir=down width=max height=34 margin-top=16 margin-right=16 }
	}
}
