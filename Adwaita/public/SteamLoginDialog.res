SteamLoginDialog.res
{
	styles
	{
		CSteamLoginDialog
		{
			bgcolor="popover_bg"
			textcolor="popover_fg"
			minimum-height=360
		}

		FrameTitle
		{
			textcolor="popover_fg"
			font-size=20
			inset-left=10
			render_bg {}
		}

		Button
		{
			inset-left=10
			render
			{
				0="fill(x0, y0-1, x1+1, y0, border)"
				1="fill(x1, y0, x1+1, y1, border)"
			}
			render_bg {}
		}
		Button:hover
		{
			render_bg
			{
				0="fill(x0, y0, x1, y1, button_bg)"
			}
		}
		Button:focus
		{
			render_bg
			{
				0="fill(x0, y0, x1, y1, button_bg)"
			}
		}
		Button:active
		{
			render_bg
			{
				0="fill(x0, y0, x1, y1, button_hover_bg)"
			}
		}

		TextEntry
		{
			inset-left=9
			inset-right=9
			inset-top=6
			inset-bottom=-6
			textcolor="button_fg"
			shadowtextcolor="button_fg"
			selectedtextcolor="accent_fg"
			selectedbgcolor="accent_bg"
			render
			{
				0="fill(x0, y1-1, x1, y1, headerbar_shade)"
				1="image(x1-28, y0+17, x1-12, y1-17, assets/icons/edit)"
			}
			render_bg
			{
				0="fill(x0, y0+12, x1, y1, button_bg)"
				1="fill(x0+12, y0, x1-12, y0+12, button_bg)"
				2="image(x0, y0, x0+12, y0+12, assets/corners/12_w10/tl)"
				3="image(x1-12, y0, x1, y0+12, assets/corners/12_w10/tr)"
			}
		}
		TextEntry:hover
		{
			render_bg
			{
				0="fill(x0, y0+12, x1, y1, button_hover_bg)"
				1="fill(x0+12, y0, x1-12, y0+12, button_hover_bg)"
				2="image(x0, y0, x0+12, y0+12, assets/corners/12_w15/tl)"
				3="image(x1-12, y0, x1, y0+12, assets/corners/12_w15/tr)"
			}
		}
		TextEntry:disabled
		{
			textcolor="button_disabled_fg"
			render_bg
			{
				0="fill(x0, y0+12, x1, y1, button_disabled_bg)"
				1="fill(x0+12, y0, x1-12, y0+12, button_disabled_bg)"
				2="image(x0, y0, x0+12, y0+12, assets/corners/12_w5/tl)"
				3="image(x1-12, y0, x1, y0+12, assets/corners/12_w5/tr)"
			}
		}
		TextEntry:focus
		{
			render
			{
				0="image(x0, y0, x0+13, y0+13, assets/focusring/12/tl)"
				1="image(x1-13, y0, x1, y0+13, assets/focusring/12/tr)"
				2="fill(x0+13, y0, x1-13, y0+2, focusring)"
				3="fill(x0, y0+13, x0+2, y1-2, focusring)"
				4="fill(x1-2, y0+13, x1, y1-2, focusring)"
				5="fill(x0, y1-2, x1, y1, focusring)"
			}
		}

		TextEntryLarge
		{
			inset-left=9
			inset-right=9
			inset-top=6
			inset-bottom=-6
			bgcolor=none
			textcolor="button_fg"
			shadowtextcolor="button_fg"
			selectedtextcolor="accent_fg"
			selectedbgcolor="accent_bg"
			render
			{
				0="fill(x0, y1-1, x1, y1, headerbar_shade)"
				1="image(x1-28, y0+17, x1-12, y1-17, assets/icons/edit)"
			}
			render_bg
			{
				0="fill(x0, y0, x1, y1, button_bg)"
			}
		}
		TextEntryLarge:hover
		{
			bgcolor=none
			render
			{
				0="fill(x0, y1-1, x1, y1, headerbar_shade)"
				1="image(x1-28, y0+17, x1-12, y1-17, assets/icons/edit)"
			}
			render_bg
			{
				0="fill(x0, y0, x1, y1, button_hover_bg)"
			}
		}
		TextEntryLarge:disabled
		{
			bgcolor=none
			textcolor="button_disabled_fg"
			render_bg
			{
				0="fill(x0, y0, x1, y1, button_disabled_bg)"
			}
		}
		TextEntryLarge:focus
		{
			bgcolor=none
			render
			{
				0="fill(x0, y0, x1, y0+2, focusring)"
				1="fill(x0, y0+2, x0+2, y1-2, focusring)"
				2="fill(x1-2, y0+2, x1, y1-2, focusring)"
				3="fill(x0, y1-2, x1, y1, focusring)"
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
				0="fill(x0, y0, x1, y1-12, button_bg)"
				1="fill(x0+12, y1-12, x1-12, y1, button_bg)"
				2="image(x0, y1-12, x0+12, y1, assets/corners/12_w10/bl)"
				3="image(x1-12, y1-12, x1, y1, assets/corners/12_w10/br)"
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
				0="fill(x0, y0, x1, y1-12, button_hover_bg)"
				1="fill(x0+12, y1-12, x1-12, y1, button_hover_bg)"
				2="image(x0, y1-12, x0+12, y1, assets/corners/12_w15/bl)"
				3="image(x1-12, y1-12, x1, y1, assets/corners/12_w15/br)"
			}
		}
		CheckButton:active
		{
			image="assets/pixel"
			render_bg
			{
				0="fill(x0, y0, x1, y1-12, button_active_bg)"
				1="fill(x0+12, y1-12, x1-12, y1, button_active_bg)"
				2="image(x0, y1-12, x0+12, y1, assets/corners/12_w30/bl)"
				3="image(x1-12, y1-12, x1, y1, assets/corners/12_w30/br)"
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
				0="fill(x0, y0, x1, y1-12, button_disabled_bg)"
				1="fill(x0+12, y1-12, x1-12, y1, button_disabled_bg)"
				2="image(x0, y1-12, x0+12, y1, assets/corners/12_w5/bl)"
				3="image(x1-12, y1-12, x1, y1, assets/corners/12_w5/br)"
			}
		}

		Label
		{
			font-size=12
			textcolor="button_disabled_fg"
			selectedtextcolor="button_disabled_fg"
		}

		loginerror_style_body
		{
			font-size=14
			textcolor="warning"
			bgcolor=none
			padding-left=32
			render
			{
				0="image(x0+6, y0+9, x0+24, y0+25, assets/icons/warning)"
			}
		}
	}

	layout
	{
		place { control="frame_title" width=max height=64 }

		place { control="LoginProcessThrobber" align=right margin-top=24 margin-right=16 width=16 height=16 }

		place { control="UserNameEdit,PasswordEdit,SavePasswordCheck" dir=down margin-top=64 margin-left=16 margin-right=16 width=max height=50 }

		place { control="UserNameLabel" start="UserNameEdit" dir=down margin-left=12 margin-top=-43 }
		place { control="PasswordLabel" start="PasswordEdit" dir=down margin-left=12 margin-top=-43 }
		place { control="PasswordCapsLockLabel,PasswordCapsLockImage" start="PasswordEdit" dir=down align=right margin-top=-43 margin-right=12 }

		place { control="AlreadyLoggedIn,LoginProcessText,LoginErrorText" start="SavePasswordCheck" dir=down margin-top=16 margin-right=16 width=max }

		place { control="LostPasswordButton,CreateNewAccountButton" dir=down start="LoginErrorText" align=bottom margin-top=24 margin-bottom=43 margin-left=-16 width=max height=42 spacing=1 }
		place { control="CancelButton,LoginButton" align=bottom margin-left=0 margin-right=0 width=240 height=42 spacing=1 }

		region { name="hidden" width=0 height=0 margin-left=-999 }
		place { control="frame_close,ImagePanelLogo,Label2,Label4,LoginProcessImage,LoginProcessLabel,Divider1" region="hidden" width=0 height=0 }
	}
}
