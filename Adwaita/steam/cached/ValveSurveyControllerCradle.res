ValveSurveyControllerCradle.res
{
	styles
	{
		ImagePanel
		{
			render
			{
				0="image(x0, y1+16, x0+12, y1+28, assets/corners/12_mask_window_bg/tl)"
				1="image(x1-12, y1+16, x1, y1+28, assets/corners/12_mask_window_bg/tr)"
				2="fill(x0, y1+165, x1, y1+166, window_bg)"
				3="image(x0, y1+154, x0+12, y1+166, assets/corners/12_mask_window_bg/bl)"
				4="image(x1-12, y1+154, x1, y1+166, assets/corners/12_mask_window_bg/br)"
			}
		}
	}

	layout
	{
		place { control="Label1,CradleImage" x=16 y=16 width=max margin-right=16 spacing=16 }
		place { control="SurveyControllerCradleNo,SurveyControllerCradleYes,SurveyControllerCradleDontHave" start="CradleImage" dir=down width=max height=50 margin-top=16 margin-right=16 }
	}
}
