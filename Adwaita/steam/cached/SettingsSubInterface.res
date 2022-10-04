SettingsSubInterface.res
{
	layout
	{
		region { name="content" margin-top=16 margin-left=16 width=520 height=max overflow=scroll-vertical }

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
