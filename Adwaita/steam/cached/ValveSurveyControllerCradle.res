ValveSurveyControllerCradle.res
{
	styles
	{
		CSurveyControllerCradle
		{
			render
			{
				0="image(x0+16, y1-166, x0+28, y1-154, assets/corners/12_mask_window_bg/tl)"
				1="image(x1-28, y1-166, x1-16, y1-154, assets/corners/12_mask_window_bg/tr)"
				2="image(x0+16, y1-28, x0+28, y1-16, assets/corners/12_mask_window_bg/bl)"
				3="image(x1-28, y1-28, x1-16, y1-16, assets/corners/12_mask_window_bg/br)"
			}
		}
	}

	layout
	{
		place { control="Label1" x=16 y=16 width=max margin-right=16 }
		place { control="CradleImage" start="Label1" dir=down align=top-center width=200 height=127 margin-top=16 margin-right=16 }
		place { control="SurveyControllerCradleNo,SurveyControllerCradleYes,SurveyControllerCradleDontHave" dir=down align=bottom width=max height=50 margin-left=16 margin-right=16 margin-bottom=16 }
	}
}
