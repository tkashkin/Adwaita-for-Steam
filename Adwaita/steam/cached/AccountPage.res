AccountPage.res
{
	styles
	{
		ImagePanel
		{
			render_bg
			{
				// background
				0="fill(x0, y0-14, x0+460, y0+135, button_bg)"
				-1="fill(x0-12, y0-2, x0, y0+123, button_bg)"
				-2="fill(x0+460, y0-2, x0+472, y0+123, button_bg)"
				-3="image(x0-12, y0-14, x0, y0-2, assets/corners/12_w10/tl)"
				-4="image(x0+460, y0-14, x0+472, y0-2, assets/corners/12_w10/tr)"
				-5="image(x0-12, y0+123, x0, y0+135, assets/corners/12_w10/bl)"
				-6="image(x0+460, y0+123, x0+472, y0+135, assets/corners/12_w10/br)"

				// separators
				1="fill(x0-12, y0+35, x0+472, y0+36, headerbar_shade)"
				2="fill(x0-12, y0+85, x0+472, y0+86, headerbar_shade)"

				// icons
				3="image(x0, y0+50, x0+24, y0+74, assets/icons_24/shield)"
				4="image(x0, y0+98, x0+24, y0+122, assets/icons_24/bug)"
			}
		}

		Label
		{
			textcolor="window_fg"
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
	}

	layout
	{
		region { name="content" margin-top=16 margin-bottom=16 margin-left=16 width=500 height=max }

		place { control="SecurityIcon" region="content" x=12 y=14 width=24 height=24 }
		place { control="SecurityStatusLabel,SecurityStatusState" region="content" x=48 y=7 spacing=2 dir=down }

		place { control="Label2,VacInfoLink" region="content" x=48 y=57 spacing=2 dir=down }

		place { control="BetaParticipationLabel,CurrentBetaLabel" region="content" x=48 y=106 spacing=2 dir=down }
		place { control="ChangeBetaButton" region="content" y=110 align=right margin-right=12 height=25 }

		place { control="AccountLink" region="content" y=156 }
		place { control="ReportBugLink" region="content" y=156 align=right }

		place { control="NoPersonalInfoCheck,ChangeUserButton,ManageSecurityButton,ChangePasswordButton,ChangeContactEmailButton,ValidateContactEmailButton,MachineLockAccountButton" region="content" y=180 width=max height=34 spacing=6 dir=down }

		region { name="hidden" width=0 height=0 margin-left=-999 }
		place { control="LogOutLabel,AccountInfo,ContactEmailLabel,EmailInfo,Label1,Divider1,Divider2" region="hidden" }
	}
}