RegisterSubEnterCDKey.res
{
	styles
	{
		Label
		{
			font-size=12
			textcolor="button_disabled_fg"
			selectedtextcolor="button_disabled_fg"
		}

		LabelDull
		{
			font-size=14
			textcolor="window_fg"
			selectedtextcolor="window_fg"
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
				0="image(x1-28, y0+17, x1-12, y1-17, assets/icons/edit)"
			}
			render_bg
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
		TextEntry:hover
		{
			render_bg
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
		TextEntry:disabled
		{
			textcolor="button_disabled_fg"
			render_bg
			{
				0="fill(x0, y0+12, x1, y1-12, button_disabled_bg)"
				1="fill(x0+12, y0, x1-12, y0+12, button_disabled_bg)"
				2="fill(x0+12, y1-12, x1-12, y1, button_disabled_bg)"
				3="image(x0, y0, x0+12, y0+12, assets/corners/12_w5/tl)"
				4="image(x1-12, y0, x1, y0+12, assets/corners/12_w5/tr)"
				5="image(x0, y1-12, x0+12, y1, assets/corners/12_w5/bl)"
				6="image(x1-12, y1-12, x1, y1, assets/corners/12_w5/br)"
			}
		}
		TextEntry:focus
		{
			render
			{
				0="image(x0, y0, x0+13, y0+13, assets/focusring/12/tl)"
				1="image(x1-13, y0, x1, y0+13, assets/focusring/12/tr)"
				2="image(x0, y1-13, x0+13, y1, assets/focusring/12/bl)"
				3="image(x1-13, y1-13, x1, y1, assets/focusring/12/br)"
				4="fill(x0+13, y0, x1-13, y0+2, focusring)"
				5="fill(x0, y0+13, x0+2, y1-13, focusring)"
				6="fill(x1-2, y0+13, x1, y1-13, focusring)"
				7="fill(x0+13, y1-2, x1-13, y1, focusring)"
			}
		}
	}

	layout
	{
		place { control="InfoLabel" dir=down margin-top=16 margin-left=16 margin-right=16 width=max }

		place { control="CDKeyEntry" dir=down start="InfoLabel" margin-top=16 margin-right=16 width=max height=50 }
		place { control="Label2" start="CDKeyEntry" dir=down margin-left=12 margin-top=-43 }

		place { control="Label1" dir=down start="CDKeyEntry" margin-top=16 margin-right=16 width=max }

		region { name="hidden" width=0 height=0 margin-left=-999 }
		place { control="InstallLanguageLabel,LanguageCombo" region="hidden" width=0 height=0 }
	}
}
