Scheme
{
	LayoutTemplates
	{
		Frame
		{
			frame_close
			{
				xpos	r31
				ypos	7
				wide	24
				tall	24
				PinCorner	1
			}

			frame_maximize
			{
				visible	0
				xpos	r62
				ypos	7
				wide	24
				tall	24
				PinCorner	1
			}

			frame_minimize
			{
				visible	0
				xpos	r93
				ypos	7
				wide	24
				tall	24
				PinCorner	1
			}
			
			frame_title
			{
				xpos	0
				ypos	0
				wide	max
				tall	38
				AutoResize	1
			}
			
			frame_captiongrip
			{
				xpos	4
				ypos	4
				wide	r20
				tall	60
				AutoResize	1
			}

			frame_brGrip
			{
				xpos	r15
				ypos	r15
				wide	14
				tall	14
				PinCorner	3
			}
			
			frame_menu
			{
				visible	0
			}
		}
		
		PropertyDialog
		{
			sheet
			{
				xpos	6
				ypos	44
				wide	r6
				tall	r48
			}
			
			// these buttons are still a bit special - if some of them are hidden, they shuffle
			// across taking the place of other buttons to make sure there aren't gaps
			ApplyButton
			{
				xpos	r101
				ypos	r36
				wide	92
				tall	24
			}
			
			CancelButton
			{
				xpos	r203
				ypos	r36
				wide	92
				tall	24
			}
			
			OKButton
			{
				xpos	r304
				ypos	r36
				wide	92
				tall	24
			}
		}
		
		WizardPanel
		{
			subpanel
			{
				xpos	10
				ypos	28
				wide	r10
				tall	r48
				AutoResize	3
			}
		
			PrevButton
			{
				xpos	r306
				ypos	r36
				wide	92
				tall	24
				PinCorner	3
			}
			NextButton
			{
				xpos	r204
				ypos	r36
				wide	92
				tall	24
				PinCorner	3
			}
			CancelButton
			{
				xpos	r102
				ypos	r36
				wide	92
				tall	24
				PinCorner	3
			}
			FinishButton
			{
				xpos	r102
				ypos	r36
				wide	92
				tall	24
				PinCorner	3
			}
		}
	}
	Colors {}
	BaseSettings {}
}