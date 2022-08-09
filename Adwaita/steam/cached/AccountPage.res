AccountPage.res
{
	styles
	{
		ImagePanel
		{
			render_bg
			{
				// background
				0="fill(x0, y0-14, x0+460, y0+86, button_bg)"
				1="fill(x0-12, y0-2, x0, y0+86, button_bg)"
				2="fill(x0+460, y0-2, x0+472, y0+86, button_bg)"
				3="image(x0-12, y0-14, x0, y0-2, assets/corners/12_w10/tl)"
				4="image(x0+460, y0-14, x0+472, y0-2, assets/corners/12_w10/tr)"
			}
			render
			{
				// separators
				0="fill(x0-12, y0+35, x0+472, y0+36, headerbar_shade)"
				1="fill(x0-12, y0+85, x0+472, y0+86, headerbar_shade)"
				// icons
				2="image(x0, y0+50, x0+24, y0+74, assets/icons_24/shield)"
				3="image(x0, y0+98, x0+24, y0+122, assets/icons_24/bug)"
			}
		}

		URLLabel
		{
			render
			{
				0="fill(x0, y0-17, x0+484, y0-16, window_bg)"
				1="image(x0, y0-28, x0+12, y0-16, assets/corners/12_mask_window_bg/bl)"
				2="image(x0+472, y0-28, x0+484, y0-16, assets/corners/12_mask_window_bg/br)"
				3="image(x0, y1, x0+12, y1+12, assets/corners/12_mask_window_bg/tl)"
				4="image(x0+472, y1, x0+484, y1+12, assets/corners/12_mask_window_bg/tr)"
			}
		}
	}

	layout
	{
		region { name="content" margin-top=16 margin-left=16 width=500 height=max }

		place { control="SecurityIcon" region="content" x=12 y=14 width=24 height=24 }
		place { control="SecurityStatusLabel,SecurityStatusState" region="content" x=48 y=7 spacing=2 dir=down }

		place { control="Label2,VacInfoLink" region="content" x=48 y=57 spacing=2 dir=down }

		place { control="BetaParticipationLabel,CurrentBetaLabel" region="content" x=48 y=106 spacing=2 dir=down }
		place { control="ChangeBetaButton" region="content" margin-left=-300 y=100 width=max height=50 }

		place { control="AccountLink" region="content" dir=down start="ChangeBetaButton" margin-top=16 width=max height=28 }

		place { control="NoPersonalInfoCheck,ChangeUserButton,ManageSecurityButton,ChangePasswordButton,ChangeContactEmailButton,ValidateContactEmailButton,MachineLockAccountButton" region="content" dir=down start="AccountLink" width=max height=50 }

		place { control="ReportBugLink" region="content" dir=down start="MachineLockAccountButton" margin-top=16 width=max height=28 }

		region { name="hidden" width=0 height=0 margin-left=-999 }
		place { control="LogOutLabel,AccountInfo,ContactEmailLabel,EmailInfo,Label1,Divider1,Divider2" region="hidden" }
	}
}