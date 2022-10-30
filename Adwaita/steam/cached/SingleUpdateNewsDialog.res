SingleUpdateNewsDialog.res
{
	styles
	{
		HTML
		{
			inset="2 0 2 2"
		}
	}

	layout
	{
		place { control="frame_minimize,frame_close" align=right spacing=14 margin-right=12 y=12 }

		place { control="frame_title" width=max height=48 }

		place { control="HTMLSellPage" width=max height=max margin-top=48 }

		region { name="hidden" width=0 height=0 margin-left=-999 }
		place { control="CloseButton,BgRect,frame_maximize" region="hidden" width=0 height=0 }
	}
}
