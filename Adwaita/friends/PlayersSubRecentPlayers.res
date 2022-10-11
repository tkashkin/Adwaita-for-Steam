PlayersSubRecentPlayers.res
{
	styles
	{
		PlayersList
		{
			bgcolor=none
		}

		Button
		{
			bgcolor=none
			render_bg
			{
				0="fill(x0+6, y0, x1-6, y1, button_bg)"
				1="fill(x0, y0+6, x0+6, y1-6, button_bg)"
				2="fill(x1-6, y0+6, x1, y1-6, button_bg)"
				3="image(x0, y0, x0+6, y0+6, assets/corners/6_w10/tl)"
				4="image(x1-6, y0, x1, y0+6, assets/corners/6_w10/tr)"
				5="image(x0, y1-6, x0+6, y1, assets/corners/6_w10/bl)"
				6="image(x1-6, y1-6, x1, y1, assets/corners/6_w10/br)"
			}
			render {}
		}

		Button:disabled
		{
			textcolor="button_disabled_fg"
			render_bg
			{
				0="fill(x0+6, y0, x1-6, y1, button_disabled_bg)"
				1="fill(x0, y0+6, x0+6, y1-6, button_disabled_bg)"
				2="fill(x1-6, y0+6, x1, y1-6, button_disabled_bg)"
				3="image(x0, y0, x0+6, y0+6, assets/corners/6_w5/tl)"
				4="image(x1-6, y0, x1, y0+6, assets/corners/6_w5/tr)"
				5="image(x0, y1-6, x0+6, y1, assets/corners/6_w5/bl)"
				6="image(x1-6, y1-6, x1, y1, assets/corners/6_w5/br)"
			}
		}

		Button:hover
		{
			render_bg
			{
				0="fill(x0+6, y0, x1-6, y1, button_hover_bg)"
				1="fill(x0, y0+6, x0+6, y1-6, button_hover_bg)"
				2="fill(x1-6, y0+6, x1, y1-6, button_hover_bg)"
				3="image(x0, y0, x0+6, y0+6, assets/corners/6_w15/tl)"
				4="image(x1-6, y0, x1, y0+6, assets/corners/6_w15/tr)"
				5="image(x0, y1-6, x0+6, y1, assets/corners/6_w15/bl)"
				6="image(x1-6, y1-6, x1, y1, assets/corners/6_w15/br)"
			}
		}
	}

	layout {
		place { control="PlayersList" width=max height=max margin-top=30 margin-bottom=42 }
		place { control="AddFriendButton" align=bottom }
	}
}
