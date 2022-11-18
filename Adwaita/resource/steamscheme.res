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
				wide	0
				tall	0
				PinCorner	1
			}

			frame_maximize
			{
				visible	0
				xpos	-999
				ypos	0
				wide	0
				tall	0
				PinCorner	0
			}

			frame_minimize
			{
				visible	0
				xpos	-999
				ypos	0
				wide	0
				tall	0
				PinCorner	0
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
				xpos	24
				ypos	3
				wide	520
				tall	r0
			}

			frame_close
			{
				visible	0
				xpos	-999
				ypos	0
				wide	0
				tall	0
				PinCorner	0
			}
			
			frame_title
			{
				xpos	0
				ypos	0
				wide	max
				tall	48
				AutoResize	1
			}
			
			ApplyButton
			{
				visible	0
				xpos	-999
				ypos	0
				wide	50
				tall	0
				PinCorner	1
			}
			
			CancelButton
			{
				xpos	r57
				ypos	7
				wide	50
				tall	34
				PinCorner	1
			}
			
			OKButton
			{
				xpos	-999
				ypos	0
				wide	50
				tall	34
				PinCorner	1
			}
		}
		
		WizardPanel
		{
			subpanel
			{
				xpos	0
				ypos	48
				wide	r0
				tall	r0
				AutoResize	3
			}

			CancelButton
			{
				xpos	7
				ypos	7
				wide	80
				tall	0
				PinCorner	0
			}
		
			PrevButton
			{
				xpos	93
				ypos	7
				zpos	2
				wide	80
				tall	0
				PinCorner	0
			}

			NextButton
			{
				xpos	r87
				ypos	7
				wide	80
				tall	0
				PinCorner	1
			}

			FinishButton
			{
				xpos	r87
				ypos	7
				zpos	2
				wide	80
				tall	0
				PinCorner	1
			}
		}
	}
}
